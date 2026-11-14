"""Searches in online archives, usable by any agent through the shell.
Every search is logged as a `recherche` fiche (unless --no-log): a negative result is evidence too.

  pq search gallica <termes...>                catalogue + plein texte Gallica (SRU)
  pq search gallica-texte <ark> <termes...>    occurrences dans un document Gallica (ContentSearch, avec pages)
  pq search archive <termes...>                catalogue archive.org
  pq search archive-texte <identifiant>[/<fichier>] <termes...>   occurrences dans le texte OCR d'un livre archive.org
  pq search corpus <termes...> [--filtre m]    dans les livres choisis du corpus (corpus/livres.yaml), texte local
  pq search mdz-texte <bsb…> <termes...>       occurrences dans un livre numérisé de la BSB Munich (MDZ), avec pages
  pq search europeana <termes...>              notices Europeana (métadonnées, tous les termes ; clé dans tools/.europeana-key)
  pq search local <chemin> <termes...>         occurrences dans un fichier texte local (cache/…)

Tous ces outils lisent un texte déjà existant (couche texte des numérisations) : jamais d'OCR ni d'image.
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
    """`identifiant` ou `identifiant/fichier` (nom de base d'un volume dans un item à plusieurs volumes)."""
    identifier, _, volume = identifier.partition("/")
    path = os.path.join(CACHE_TXT, "archive", f"{identifier}{'--' + slugify(volume) if volume else ''}.txt")
    if os.path.exists(path):
        return path
    meta = _get(f"https://archive.org/metadata/{identifier}").json()
    names = [f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")
             and (not volume or f["name"] == f"{volume}_djvu.txt")]
    if not names:
        raise SystemExit(f"Pas de texte OCR (_djvu.txt) pour {identifier}" + (f"/{volume}" if volume else ""))
    if len(names) > 1 and not volume:
        print(f"Attention : {len(names)} volumes dans {identifier} ; lu : {names[0]}. "
              f"Préciser `{identifier}/<fichier>` parmi : " + " ; ".join(n[:-9] for n in names))
    txt = _get(f"https://archive.org/download/{identifier}/{names[0]}", timeout=300).text
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    return path


def grep_text(text, terms, url=None, context=220, limit=60):
    folded = fold(text)
    hits = []
    for t in terms:
        for m in re.finditer(r"(?<![a-z0-9])" + re.escape(fold(t)), folded):  # début de mot : « Solan » ≠ « Marsolan »
            a, b = max(0, m.start() - context), min(len(text), m.end() + context)
            snippet = re.sub(r"\s+", " ", text[a:b])
            hits.append({"terme": t, "titre": f"car. {m.start()} : …{snippet}…", "url": url})
            if len(hits) >= limit:
                return hits
    return hits


def archive_texte(identifier, terms):
    path = archive_text_path(identifier)
    text = open(path, encoding="utf-8").read()
    hits = grep_text(text, terms, url=f"https://archive.org/details/{identifier.partition('/')[0]}")
    return {"requete": " | ".join(terms), "perimetre": f"archive.org {identifier} (OCR, {os.path.relpath(path, REPO)})",
            "total": len(hits), "resultats": hits}


def _clean(s, n=300):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>|\{\{\{|\}\}\}", "", html.unescape(s or ""))).strip()[:n]


# ---------------------------------------------------------------- corpus : livres choisis (corpus/livres.yaml)
CORPUS = os.path.join(REPO, "corpus", "livres.yaml")


def corpus_entries(filtre=None):
    entries = yaml.safe_load(open(CORPUS, encoding="utf-8")) or []
    if filtre:
        f = fold(filtre)
        entries = [e for e in entries if f in fold(" ".join(str(e.get(k, "")) for k in ("id", "titre", "theme", "region")))]
    return entries


def corpus_cached(identifier):
    return os.path.exists(os.path.join(CACHE_TXT, "archive", f"{identifier}.txt"))


def corpus_fetch(filtre=None):
    """Télécharge le texte existant (_djvu.txt) des volumes absents du cache. Aucun OCR."""
    todo = [(e["id"], v) for e in corpus_entries(filtre) for v in e.get("archive", []) if not corpus_cached(v)]
    for i, (eid, v) in enumerate(todo, 1):
        try:
            archive_text_path(v)
            print(f"[{i}/{len(todo)}] {eid} : {v}")
        except (SystemExit, requests.RequestException) as e:
            print(f"[{i}/{len(todo)}] {eid} : {v} — échec ({e})")
    return len(todo)


def corpus_search(terms, filtre=None, avec=None, per_volume=3, limit=80):
    """Cherche les termes dans le texte local de chaque volume du corpus ; un résumé par livre, peu d'extraits.
    `avec` : ne garder que les passages où figure aussi un de ces mots (à ~220 caractères)."""
    out, counts, missing = [], {}, 0
    for e in corpus_entries(filtre):
        for v in e.get("archive", []):
            path = os.path.join(CACHE_TXT, "archive", f"{v}.txt")
            if not os.path.exists(path):
                missing += 1
                continue
            hits = grep_text(open(path, encoding="utf-8", errors="replace").read(), terms,
                             url=f"https://archive.org/details/{v}", limit=500)
            if avec:
                hits = [h for h in hits if any(fold(a) in fold(h["titre"]) for a in avec)]
            if hits:
                counts[f"{e['id']} [{v}]"] = len(hits)
                for h in hits[:per_volume]:
                    if len(out) < limit:
                        out.append({**h, "titre": f"{e['titre']} [{v}] {h['titre']}"})
    vols = sum(len(e.get("archive", [])) for e in corpus_entries(filtre))
    note = f" ; {missing} volume(s) pas encore téléchargé(s) : ./pq corpus --fetch" if missing else ""
    print("Occurrences par volume : " + (", ".join(f"{k} {n}" for k, n in sorted(counts.items(), key=lambda x: -x[1])) or "aucune"))
    return {"requete": " | ".join(terms) + (f" (avec {' | '.join(avec)})" if avec else ""),
            "total": sum(counts.values()), "resultats": out,
            "perimetre": f"corpus/livres.yaml{' (filtre ' + filtre + ')' if filtre else ''} : {vols - missing}/{vols} volumes lus{note}"}


# ---------------------------------------------------------------- MDZ (Bayerische Staatsbibliothek)
def mdz_texte(bsb, terms):
    bsb = re.search(r"bsb\d{8}", bsb).group(0)
    man = _get(f"https://api.digitale-sammlungen.de/iiif/presentation/v2/{bsb}/manifest").json()
    labels = {c["@id"]: c.get("label") for c in man["sequences"][0]["canvases"]}
    hits = []
    for t in terms:
        d = _get(f"https://api.digitale-sammlungen.de/iiif/services/search/v1/{bsb}", params={"q": t}).json()
        pages = {}
        for res in d.get("resources", []):
            on = res["on"] if isinstance(res["on"], str) else res["on"][0]
            pages[res["@id"]] = on.split("#")[0]
        for h in d.get("hits", []):
            canvas = pages.get((h.get("annotations") or [""])[0], "")
            label = labels.get(canvas, "?")
            num = canvas.rstrip("/").split("/")[-1] if canvas else ""
            snip = _clean(f"{h.get('before', '')}[{h.get('match', '')}]{h.get('after', '')}")
            hits.append({"terme": t, "titre": f"p. {label} : …{snip}…",
                         "url": f"https://www.digitale-sammlungen.de/view/{bsb}?page={num.lstrip('0') or num}"})
    return {"requete": " | ".join(terms), "perimetre": f"MDZ {bsb} : {_clean(str(man.get('label')), 150)}",
            "total": len(hits), "resultats": hits}


# ---------------------------------------------------------------- Europeana
def _key(name, env):
    if os.environ.get(env):
        return os.environ[env].strip()
    p = os.path.join(REPO, "tools", name)
    return open(p).read().strip() if os.path.exists(p) else None


def europeana(terms, maximum=20):
    key = _key(".europeana-key", "EUROPEANA_KEY")
    if not key:
        raise SystemExit("Clé Europeana absente : la mettre dans tools/.europeana-key.")
    q = " AND ".join(f'"{t}"' if " " in t else t for t in terms)
    d = _get("https://api.europeana.eu/record/v2/search.json",
             params={"wskey": key, "query": q, "rows": maximum, "profile": "standard"}).json()
    out = [{"titre": _clean((it.get("title") or ["?"])[0], 200), "auteur": _clean((it.get("dataProvider") or [""])[0], 80),
            "date": (it.get("year") or [""])[0], "url": (it.get("edmIsShownAt") or [it.get("guid", "").split("?")[0]])[0]}
           for it in d.get("items", [])]
    return {"requete": q, "perimetre": "Europeana, métadonnées (pas le texte des livres)", "total": d.get("totalResults", 0),
            "resultats": out}


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
    if t in ("gallica", "gallica-texte"):
        from .gallica import is_block, queue
        try:
            res = (gallica(args.termes, index=args.index, maximum=args.max, cql=args.cql) if t == "gallica"
                   else gallica_texte(args.termes[0], args.termes[1:]))
        except requests.RequestException as e:
            if not is_block(e):
                raise
            opts = {"index": args.index, "cql": args.cql, "max": args.max} if t == "gallica" else None
            gid = queue(t, args.termes, hyp=args.hyp, objet=args.objet, options=opts,
                        cause=f"{type(e).__name__} {getattr(e.response, 'status_code', '') or ''}".strip())
            print(f"Gallica refuse la requête ({getattr(e.response, 'status_code', type(e).__name__)}) : recherche mise en attente "
                  f"dans base/gallica/{gid}.md. Elle sera relancée par `./pq gallica --run` (ou /sync-gallica).")
            raise SystemExit(2)
    elif t == "archive":
        res = archive(args.termes, maximum=args.max)
    elif t == "archive-texte":
        res = archive_texte(args.termes[0], args.termes[1:])
    elif t == "corpus":
        res = corpus_search(args.termes, filtre=args.filtre, avec=args.avec)
    elif t == "mdz-texte":
        res = mdz_texte(args.termes[0], args.termes[1:])
    elif t == "europeana":
        res = europeana(args.termes, maximum=args.max)
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
