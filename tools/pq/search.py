"""Searches in online archives, usable by any agent through the shell.
Every search is logged as a `recherche` fiche (unless --no-log): a negative result is evidence too.

  pq search gallica <termes...>                catalogue + plein texte Gallica (SRU)
  pq search gallica-texte <ark> <termes...>    occurrences dans un document Gallica (ContentSearch, avec pages)
  pq search archive <termes...>                catalogue archive.org
  pq search archive-texte <identifiant> <termes...>   occurrences dans le texte OCR d'un livre archive.org
  pq search local <chemin> <termes...>         occurrences dans un fichier texte local (cache/…)
"""
import os, re, html, json, datetime, subprocess, unicodedata
import xml.etree.ElementTree as ET
import requests
import yaml
from .model import REPO, BASE, slugify

UA = {"User-Agent": "perroquet-recherche-historique/1.0 (usage personnel)"}
CACHE_TXT = os.path.join(REPO, "cache", "texte")


def fold(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return s.replace("v", "u").replace("j", "i").replace("ſ", "s")


def git_user():
    try:
        return subprocess.run(["git", "config", "user.name"], cwd=REPO, capture_output=True, text=True).stdout.strip() or os.environ.get("USER", "inconnu")
    except Exception:
        return os.environ.get("USER", "inconnu")


def _get(url, **kw):
    r = requests.get(url, headers=UA, timeout=kw.pop("timeout", 60), **kw)
    r.raise_for_status()
    return r


# ---------------------------------------------------------------- Gallica
def gallica(terms, index="gallica", maximum=20, cql=None):
    if not cql:
        cql = " or ".join(f'{index} all "{t}"' for t in terms)
    r = _get("https://gallica.bnf.fr/SRU", params={"operation": "searchRetrieve", "version": "1.2",
             "query": cql, "maximumRecords": maximum, "startRecord": 1})
    root = ET.fromstring(r.content)
    ns = {"srw": "http://www.loc.gov/zing/srw/", "dc": "http://purl.org/dc/elements/1.1/"}
    total = root.findtext("srw:numberOfRecords", default="0", namespaces=ns)
    out = []
    for rec in root.iter("{http://www.loc.gov/zing/srw/}record"):
        def all_(tag):
            return [e.text.strip() for e in rec.iter(f"{{http://purl.org/dc/elements/1.1/}}{tag}") if e.text]
        ids = [i for i in all_("identifier") if "ark:" in i]
        out.append({"titre": " ; ".join(all_("title"))[:300], "auteur": " ; ".join(all_("creator"))[:150],
                    "date": " ; ".join(all_("date")), "url": ids[0] if ids else None})
    return {"requete": cql, "total": int(total or 0), "resultats": out}


def gallica_texte(ark, terms):
    ark = ark.split("/")[-1].split(".")[0]
    hits = []
    for t in terms:
        r = _get("https://gallica.bnf.fr/services/ContentSearch", params={"ark": ark, "query": t})
        txt = r.text
        for item in re.findall(r"<item>(.*?)</item>", txt, re.S):
            page = re.search(r"<p_id>(.*?)</p_id>", item)
            content = re.search(r"<content>(.*?)</content>", item, re.S)
            p = page.group(1) if page else ""
            num = re.sub(r"\D", "", p)
            snippet = html.unescape(re.sub(r"<[^>]+>", "", html.unescape(content.group(1) if content else "")))
            hits.append({"terme": t, "titre": f"{p} : {snippet.strip()[:300]}",
                         "url": f"https://gallica.bnf.fr/ark:/12148/{ark}/f{num}.item" if num else f"https://gallica.bnf.fr/ark:/12148/{ark}"})
    return {"requete": " | ".join(terms), "perimetre": f"gallica ark:/12148/{ark}", "total": len(hits), "resultats": hits}


# ---------------------------------------------------------------- archive.org
def archive(terms, maximum=20):
    q = " OR ".join(f'"{t}"' for t in terms)
    r = _get("https://archive.org/advancedsearch.php", params={"q": q, "fl[]": ["identifier", "title", "creator", "date"],
             "rows": maximum, "output": "json"})
    d = r.json()["response"]
    out = [{"titre": str(x.get("title"))[:300], "auteur": str(x.get("creator", ""))[:150], "date": str(x.get("date", "")),
            "url": f"https://archive.org/details/{x['identifier']}"} for x in d["docs"]]
    return {"requete": q, "total": d["numFound"], "resultats": out}


def archive_text_path(identifier):
    path = os.path.join(CACHE_TXT, "archive", f"{identifier}.txt")
    if os.path.exists(path):
        return path
    meta = _get(f"https://archive.org/metadata/{identifier}").json()
    names = [f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")]
    if not names:
        raise SystemExit(f"Pas de texte OCR (_djvu.txt) pour {identifier}")
    txt = _get(f"https://archive.org/download/{identifier}/{names[0]}", timeout=300).text
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    return path


def grep_text(text, terms, url=None, context=220, limit=60):
    folded = fold(text)
    hits = []
    for t in terms:
        for m in re.finditer(re.escape(fold(t)), folded):
            a, b = max(0, m.start() - context), min(len(text), m.end() + context)
            snippet = re.sub(r"\s+", " ", text[a:b])
            hits.append({"terme": t, "titre": f"car. {m.start()} : …{snippet}…", "url": url})
            if len(hits) >= limit:
                return hits
    return hits


def archive_texte(identifier, terms):
    path = archive_text_path(identifier)
    text = open(path, encoding="utf-8").read()
    hits = grep_text(text, terms, url=f"https://archive.org/details/{identifier}")
    return {"requete": " | ".join(terms), "perimetre": f"archive.org {identifier} (OCR, {os.path.relpath(path, REPO)})",
            "total": len(hits), "resultats": hits}


def local(path, terms):
    p = path if os.path.isabs(path) else os.path.join(REPO, path)
    text = open(p, encoding="utf-8", errors="replace").read()
    hits = grep_text(text, terms, url=None)
    return {"requete": " | ".join(terms), "perimetre": os.path.relpath(p, REPO), "total": len(hits), "resultats": hits}


# ---------------------------------------------------------------- logging
def log(outil, res, hyp=None, objet=None):
    today = datetime.date.today().isoformat()
    slug = slugify(objet or res["requete"])[:40].strip("-") or "recherche"
    base_id = f"r-{today}-{slug}"
    rid, n = base_id, 2
    while os.path.exists(os.path.join(BASE, "recherches", f"{rid}.md")):
        rid, n = f"{base_id}-{n}", n + 1
    meta = {
        "id": rid, "type": "recherche", "nom": objet or f"{outil} : {res['requete']}"[:120],
        "date": today, "auteur": git_user(), "outil": outil, "requete": res["requete"],
        "perimetre": res.get("perimetre", outil),
        "resultat": "positif" if res["total"] else "negatif",
        "total": res["total"],
        "resultats": [{k: v for k, v in r.items() if v} for r in res["resultats"][:25]],
    }
    if hyp:
        meta["hypotheses"] = [hyp]
    path = os.path.join(BASE, "recherches", f"{rid}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=110) + "---\n\n"
                "Interprétation : _à compléter par l'agent (pertinence des résultats, suite à donner)._\n")
    return rid


def run(args):
    t = args.outil
    if t == "gallica":
        res = gallica(args.termes, index=args.index, maximum=args.max, cql=args.cql)
    elif t == "gallica-texte":
        res = gallica_texte(args.termes[0], args.termes[1:])
    elif t == "archive":
        res = archive(args.termes, maximum=args.max)
    elif t == "archive-texte":
        res = archive_texte(args.termes[0], args.termes[1:])
    elif t == "local":
        res = local(args.termes[0], args.termes[1:])
    else:
        raise SystemExit(f"outil inconnu : {t}")
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        print(f"[{t}] {res['requete']} — {res['total']} résultat(s)" + (f" dans {res['perimetre']}" if res.get("perimetre") else ""))
        for r in res["resultats"]:
            line = r.get("titre", "")
            extra = " | ".join(x for x in (r.get("auteur"), r.get("date")) if x)
            print(f"- {line}" + (f" [{extra}]" if extra else "") + (f"\n  {r['url']}" if r.get("url") else ""))
    if not args.no_log:
        rid = log(t, res, hyp=args.hyp, objet=args.objet)
        print(f"\n→ consigné dans base/recherches/{rid}.md")
