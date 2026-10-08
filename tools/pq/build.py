"""Render the knowledge base to a static site in site/ (open site/index.html, no server needed).
`build(base, publish=True)` writes site_publish/ for the claude.ai artifact (index.html without
its own document skeleton, as the artifact host adds one)."""
import os, re, json, shutil, datetime, subprocess
from markupsafe import Markup, escape
from jinja2 import Environment, FileSystemLoader
from markdown_it import MarkdownIt
from .model import REPO, LINK_RE, as_list, year_of
from .check import check
from . import ach

TPL = os.path.join(REPO, "site_templates")
ENTITY_TYPES = ("personne", "famille", "lieu", "evenement", "institution")


class Site:
    def __init__(self, base):
        self.b = base
        self.voc = base.schema.voc
        self.rels = base.schema.relations
        self.md = MarkdownIt("commonmark", {"html": True, "linkify": False}).enable("table")
        self.env = Environment(loader=FileSystemLoader(TPL), autoescape=True, trim_blocks=True, lstrip_blocks=True)
        f = self.env.filters
        f["lk"] = self.link
        f["conf"] = self.conf_chip
        f["chip"] = self.chip
        f["md"] = self.render_md
        f["typechip"] = self.type_chip
        f["rel"] = lambda r: self.rels.get(r, {}).get("libelle", r)
        f["fiab"] = lambda v: Markup(f'<span class="chip fiab" title="{escape(self.voc["fiabilite"].get(str(v), {}).get("libelle", ""))}">{escape(v)}</span>') if v else ""
        f["voc"] = lambda v, k: self.voc.get(k, {}).get(v, {}).get("libelle", v) if isinstance(self.voc.get(k, {}).get(v), dict) else self.voc.get(k, {}).get(v, v)
        self.env.globals["types"] = base.schema.types
        self.env.globals["voc"] = self.voc

    # ------------------------------------------------------------ helpers
    def href(self, ref):
        r = self.b.resolve(ref)
        if not r:
            return None
        kind, fi, item = r
        if kind == "assertion":
            return f"{fi.id}.html#{item['id']}"
        if kind in ("hypotheses", "predictions"):
            return f"{fi.id}.html#{item['id']}"
        return f"{fi.id}.html"

    def label(self, ref):
        r = self.b.resolve(ref)
        if not r:
            return str(ref)
        kind, fi, item = r
        if kind == "assertion":
            return f"{fi.nom.split(',')[0][:40]} · {item['id']}"
        if kind in ("hypotheses", "predictions"):
            return f"{fi.nom} · {item['id']}"
        return fi.nom

    def link(self, ref, label=None):
        if ref is None:
            return ""
        h = self.href(ref)
        lab = label or self.label(ref)
        if not h:
            return Markup(f'<span class="err" title="référence introuvable">{escape(ref)}</span>')
        title = ""
        r = self.b.resolve(ref)
        if r and r[0] == "assertion":
            c = r[2]
            title = (c.get("citation") or c.get("texte") or "")[:300]
        elif r and r[0] == "fiche":
            title = self.b.schema.types.get(r[1].type, {}).get("libelle", "")
        return Markup(f'<a href="{h}" title="{escape(title)}">{escape(lab)}</a>')

    def chip(self, value, vocname=None):
        if value in (None, ""):
            return ""
        lab = value
        if vocname:
            v = self.voc.get(vocname, {}).get(value)
            lab = v.get("libelle", value) if isinstance(v, dict) else (v or value)
            if vocname in ("statut_prediction", "statut_question", "verifie", "resultat"):
                lab = {"non_testee": "non testée", "confirmee": "confirmée", "infirmee": "infirmée", "indecidable": "indécidable",
                       "ouverte": "ouverte", "tranchee": "tranchée", "suspendue": "suspendue",
                       "non": "non vérifiée", "agent": "relue par agent", "humain": "vérifiée par vous",
                       "positif": "trouvé", "negatif": "négatif", "partiel": "partiel", "bloque": "bloqué"}.get(value, lab)
        return Markup(f'<span class="chip c-{escape(value)}">{escape(lab)}</span>')

    def conf_chip(self, value):
        if not value:
            return ""
        v = self.voc["confiance"].get(value, {})
        return Markup(f'<span class="chip c-{escape(value)}" title="{escape(v.get("aide", ""))}">{escape(v.get("libelle", value))}</span>')

    def type_chip(self, t):
        lab = self.b.schema.types.get(t, {}).get("libelle", t)
        return Markup(f'<span class="chip type-{t}"><span class="dot"></span><span style="color:var(--ink-2)">{escape(lab)}</span></span>')

    def render_md(self, text):
        if not text:
            return ""
        def sub(m):
            ref = m.group(1).strip() + (("#" + m.group(2)) if m.group(2) else "")
            return str(self.link(ref, m.group(3)))
        return Markup(self.md.render(LINK_RE.sub(sub, str(text))))

    # ------------------------------------------------------------ derived data
    def incoming(self):
        inc = {}
        for e in self.b.edges():
            inc.setdefault(str(e["dst"]), []).append(e)
        return inc

    def mentions_of(self):
        out = {}
        for cid, (src, c) in self.b.claims.items():
            for s in as_list(c.get("sujets")):
                out.setdefault(str(s), []).append((cid, src, c))
        return out

    def hyps_of(self):
        out = {}
        for h in self.b.of_type("hypothese"):
            for s in as_list(h.get("sujets")):
                out.setdefault(str(s), []).append(h)
            for row in as_list(h.get("matrice")):
                if isinstance(row, dict):
                    r = self.b.resolve(row.get("preuve"))
                    if r and r[0] == "assertion":
                        out.setdefault(r[1].id, [])
                        if h not in out[r[1].id]:
                            out[r[1].id].append(h)
                        out.setdefault(f"{r[1].id}.{r[2]['id']}", []).append(h)
                    elif r and r[0] == "fiche":
                        out.setdefault(r[1].id, []).append(h)
        return out

    def graph_data(self):
        b = self.b
        nodes, edges = [], []
        deg = {}
        mentions = b.mentions()
        for e in b.edges():
            if str(e["dst"]) in b.fiches:
                deg[e["src"]] = deg.get(e["src"], 0) + 1
                deg[str(e["dst"])] = deg.get(str(e["dst"]), 0) + 1
        for fi in b.fiches.values():
            if not b.schema.types.get(fi.type, {}).get("graphe"):
                continue
            span = fi.span() if fi.type in ENTITY_TYPES else None
            n = {"id": fi.id, "label": fi.nom, "type": fi.type, "deg": deg.get(fi.id, 0), "url": f"{fi.id}.html"}
            if span:
                n["a"], n["b"] = span
            if fi.type == "hypothese":
                n["conf"] = fi.get("confiance")
            if fi.type == "source":
                n["fiab"] = fi.get("fiabilite")
            nodes.append(n)
        ids = {n["id"] for n in nodes}
        for i, e in enumerate(b.edges()):
            if e["src"] in ids and str(e["dst"]) in ids:
                lab = self.rels.get(e["rel"], {}).get("libelle", e["rel"])
                inv = self.rels.get(e["rel"], {}).get("inverse") or lab
                edges.append({"id": f"r{i}", "source": e["src"], "target": str(e["dst"]), "rel": e["rel"],
                              "label": lab + (f" ({e['role']})" if e.get("role") else ""), "inverse": inv,
                              "conf": e.get("confiance"), "hyp": bool(e.get("hypothese")), "kind": "relation",
                              "a": e.get("debut"), "b": e.get("fin")})
        for sid, subj in mentions.items():
            for s in subj:
                if sid in ids and s in ids:
                    edges.append({"id": f"m-{sid}-{s}", "source": sid, "target": s, "rel": "mentionne",
                                  "label": "mentionne", "inverse": "mentionné par", "kind": "mention"})
        for h in b.of_type("hypothese"):
            for s in as_list(h.get("sujets")):
                if str(s) in ids:
                    edges.append({"id": f"h-{h.id}-{s}", "source": h.id, "target": str(s), "rel": "porte_sur",
                                  "label": "porte sur", "inverse": "objet de la question", "kind": "question"})
        for n in nodes:
            n["deg"] = sum(1 for e in edges if e["source"] == n["id"] or e["target"] == n["id"])
        return {"nodes": nodes, "edges": edges}

    def chronology(self):
        items = []
        for fi in self.b.of_type("evenement"):
            y = year_of(fi.get("date"))
            if y:
                items.append({"annee": y, "date": str(fi.get("date")), "kind": "evenement", "fiche": fi, "texte": fi.nom})
        for cid, (src, c) in self.b.claims.items():
            y = year_of(c.get("date"))
            if y:
                items.append({"annee": y, "date": str(c.get("date")), "kind": "assertion", "ref": cid, "src": src, "c": c,
                              "texte": c.get("texte")})
        items.sort(key=lambda x: (x["annee"], x["date"], 0 if x["kind"] == "evenement" else 1))
        years = {}
        for it in items:
            years.setdefault(it["annee"], []).append(it)
        return years

    def git_log(self, n=12):
        try:
            out = subprocess.run(["git", "log", f"-{n}", "--date=short", "--pretty=%ad\t%an\t%s"], cwd=REPO,
                                 capture_output=True, text=True).stdout
            return [l.split("\t", 2) for l in out.splitlines() if l.count("\t") >= 2]
        except Exception:
            return []

    # ------------------------------------------------------------ render
    def render(self, out):
        b = self.b
        if os.path.isdir(out):
            shutil.rmtree(out)
        os.makedirs(out)
        for f in ("style.css", "app.js", "graphe.js"):
            shutil.copy(os.path.join(TPL, f), out)
        rep = check(b, with_git=True)
        scores = {h.id: ach.score(b, h) for h in b.of_type("hypothese")}
        inc, men, hof = self.incoming(), self.mentions_of(), self.hyps_of()
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        common = {"now": now, "nb": {t: len(b.of_type(t)) for t in b.schema.types}, "nb_claims": len(b.claims),
                  "nb_err": len(rep.errors()), "nb_warn": len(rep.warnings())}

        def write(name, tpl, **ctx):
            html = self.env.get_template(tpl).render(**common, **ctx)
            with open(os.path.join(out, name), "w", encoding="utf-8") as f:
                f.write(html)

        hyps = sorted(b.of_type("hypothese"), key=lambda h: (h.get("statut") != "ouverte", h.nom))
        journal = sorted(b.of_type("enquete") + b.of_type("recherche"), key=lambda f: (str(f.get("date")), f.id), reverse=True)
        write("index.html", "index.html", page="index", title="Perroquet", hyps=hyps, scores=scores,
              journal=journal[:12], log=self.git_log(), rep=rep)
        write("hypotheses.html", "hypotheses.html", page="hypotheses", title="Questions et hypothèses", hyps=hyps, scores=scores)
        groups = [(t, sorted(b.of_type(t), key=lambda f: f.nom.lower())) for t in ENTITY_TYPES]
        write("fiches.html", "fiches.html", page="fiches", title="Fiches", groups=groups, inc=inc, men=men)
        write("sources.html", "sources.html", page="sources", title="Sources",
              sources=sorted(b.of_type("source"), key=lambda f: f.nom.lower()), hof=hof)
        write("chronologie.html", "chronologie.html", page="chronologie", title="Chronologie", years=self.chronology())
        write("journal.html", "journal.html", page="journal", title="Journal des enquêtes et recherches", journal=journal)
        write("audit.html", "audit.html", page="audit", title="Audit de méthode", rep=rep)
        g = self.graph_data()
        write("graphe.html", "graphe.html", page="graphe", title="Graphe", body_class="graph",
              graph=Markup(json.dumps(g, ensure_ascii=False).replace("</", "<\\/")),
              typecols=[(t, v["libelle_pluriel"]) for t, v in b.schema.types.items() if v.get("graphe")])

        for fi in b.fiches.values():
            ctx = {"fi": fi, "m": fi.meta, "title": fi.nom, "page": fi.type, "hof": hof.get(fi.id, [])}
            if fi.type == "hypothese":
                write(f"{fi.id}.html", "hypothese.html", s=scores[fi.id], **ctx,
                      enquetes=[e for e in b.of_type("enquete") if e.get("hypothese") == fi.id],
                      recherches=[r for r in b.of_type("recherche") if fi.id in [str(x) for x in as_list(r.get("hypotheses"))]],
                      claim=lambda ref: b.resolve(ref))
            elif fi.type == "source":
                write(f"{fi.id}.html", "source.html", **ctx, claims=[c for c in as_list(fi.get("assertions")) if isinstance(c, dict)],
                      hof_claim=lambda cid: hof.get(f"{fi.id}.{cid}", []))
            elif fi.type in ENTITY_TYPES:
                write(f"{fi.id}.html", "entite.html", **ctx, out_rel=fi.relations(), in_rel=inc.get(fi.id, []),
                      mentions=men.get(fi.id, []), span=fi.span())
            else:
                write(f"{fi.id}.html", "journal_fiche.html", **ctx)
        return rep


def build(base, publish=False):
    out = os.path.join(REPO, "site_publish" if publish else "site")
    s = Site(base)
    rep = s.render(out)
    if publish:
        p = os.path.join(out, "index.html")
        html = open(p, encoding="utf-8").read()
        html = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>", "", html, flags=re.I)
        html = re.sub(r"</head>\s*<body[^>]*>", "", html, flags=re.I)
        html = re.sub(r"</body>\s*</html>\s*$", "", html, flags=re.I)
        open(p, "w", encoding="utf-8").write(html)
    n = len(os.listdir(out))
    print(f"Site généré : {os.path.relpath(out, REPO)}/ ({n} fichiers) — {len(rep.errors())} erreur(s), {len(rep.warnings())} avertissement(s).")
    return out
