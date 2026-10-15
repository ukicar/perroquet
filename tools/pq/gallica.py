"""Gallica waiting list: what could not be done while Gallica blocked us (HTTP 403/429/5xx).

A job is a fiche base/gallica/<id>.md (type `gallica`). `pq search gallica|gallica-texte` queues itself when
Gallica refuses; an agent queues a page reading with `pq fiche gallica "<nom>"`.

  pq gallica            test access, list pending jobs
  pq gallica --run      if Gallica answers, replay the queued searches (logged as usual) and mark them done;
                        page readings are left for the agent (/sync-gallica)

The sweet-bnf MCP server (sweet-bnf.vercel.app) is reachable as `pq bnf <outil> '<json>'` (see bnf.py)."""
import os, datetime
import requests
import yaml
from .model import BASE, Base, slugify, as_list

DOSSIER = os.path.join(BASE, "gallica")
UA = {"User-Agent": "perroquet-recherche-historique/1.0 (usage personnel)"}
AUTO = ("gallica", "gallica-texte")   # jobs pq can replay by itself; anything else is read by the agent


class Bloque(Exception):
    """Gallica refused the request (rate limit, IP block, outage)."""


def is_block(exc):
    if isinstance(exc, (requests.ConnectionError, requests.Timeout)):
        return True
    r = getattr(exc, "response", None)
    return r is not None and (r.status_code in (403, 429) or r.status_code >= 500)


def accessible():
    """One cheap SRU request. Returns (ok, message)."""
    try:
        r = requests.get("https://gallica.bnf.fr/SRU", headers=UA, timeout=30,
                         params={"operation": "searchRetrieve", "version": "1.2", "query": 'gallica all "Couserans"',
                                 "maximumRecords": 1})
        if r.status_code == 200 and b"numberOfRecords" in r.content:
            return True, "Gallica répond."
        return False, f"Gallica refuse encore (HTTP {r.status_code})."
    except requests.RequestException as e:
        return False, f"Gallica injoignable ({type(e).__name__})."


def _write(meta, body=""):
    os.makedirs(DOSSIER, exist_ok=True)
    with open(os.path.join(DOSSIER, f"{meta['id']}.md"), "w", encoding="utf-8") as f:
        f.write("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=110) + "---\n" + body)


def queue(outil, termes, hyp=None, objet=None, cause="", options=None):
    """Queue a refused `pq search gallica|gallica-texte`. Returns the job id (an identical pending job is reused)."""
    b = Base()
    for j in b.of_type("gallica"):
        if j.get("statut") == "en_attente" and j.get("outil") == outil and as_list(j.get("termes")) == list(termes):
            return j.id
    today = datetime.date.today().isoformat()
    gid = base_id = f"g-{today}-{slugify(objet or ' '.join(termes))[:40].strip('-') or 'recherche'}"
    n = 2
    while os.path.exists(os.path.join(DOSSIER, f"{gid}.md")):
        gid, n = f"{base_id}-{n}", n + 1
    meta = {"id": gid, "type": "gallica", "nom": objet or f"{outil} : {' '.join(termes)}"[:120],
            "statut": "en_attente", "outil": outil, "termes": list(termes),
            "ark": termes[0] if outil == "gallica-texte" else None, "vues": None,
            "options": {k: v for k, v in (options or {}).items() if v not in (None, "gallica", 20)} or None,
            "action": "Relancer la recherche quand Gallica répondra (automatique : ./pq gallica --run).",
            "hyp": hyp, "pour": [], "tentatives": [{"date": today, "resultat": cause or "refusée"}],
            "recherche": None, "resultat": None}
    _write(meta)
    return gid


def _save(fi):
    _write(fi.meta, fi.body)


def run(args):
    b = Base()
    pending = [j for j in b.of_type("gallica") if j.get("statut") == "en_attente"]
    ok, msg = accessible()
    print(msg)
    auto = [j for j in pending if j.get("outil") in AUTO]
    lect = [j for j in pending if j.get("outil") not in AUTO]
    print(f"{len(pending)} tâche(s) en attente : {len(auto)} recherche(s) relançable(s) par pq, {len(lect)} lecture(s) pour l'agent.")
    for j in pending:
        where = j.get("ark") or " ".join(as_list(j.get("termes")))
        print(f"  [{j.get('outil') or 'lecture'}] {j.id} — {j.nom}" + (f" ({where})" if where else ""))
    if not args.run:
        if ok and pending:
            print("\nGallica répond : lancez `./pq gallica --run`, puis /sync-gallica dans l'agent pour les lectures.")
        return 0 if ok else 2
    if not ok:
        print("Rien relancé.")
        return 2
    from . import search
    today = datetime.date.today().isoformat()
    for j in auto:
        termes = as_list(j.get("termes"))
        try:
            o = j.get("options") or {}
            res = (search.gallica(termes, index=o.get("index", "gallica"), maximum=o.get("max", 20), cql=o.get("cql"))
                   if j.get("outil") == "gallica" else search.gallica_texte(termes[0], termes[1:]))
        except requests.RequestException as e:
            if is_block(e):
                j.meta.setdefault("tentatives", []).append({"date": today, "resultat": "refusée de nouveau"})
                _save(j)
                print(f"Gallica bloque de nouveau, arrêt ({j.id}).")
                return 2
            raise
        rid = search.log(j.get("outil"), res, hyp=j.get("hyp"), objet=j.nom)
        j.meta.update(statut="faite", recherche=rid, resultat=f"{res['total']} résultat(s)")
        j.meta.setdefault("tentatives", []).append({"date": today, "resultat": "faite"})
        _save(j)
        print(f"  ✓ {j.id} → {res['total']} résultat(s), consigné dans base/recherches/{rid}.md")
    if lect:
        print(f"\n{len(lect)} lecture(s) restent pour l'agent : /sync-gallica.")
    return 0
