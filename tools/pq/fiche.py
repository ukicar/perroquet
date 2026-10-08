"""`pq fiche <type> <nom>`: create a new fiche from a template, after checking for near-duplicates."""
import os, datetime
import yaml
from .model import BASE, slugify, norm_name, as_list
from .search import git_user

TEMPLATES = {
    "personne": {"variantes": [], "naissance": None, "mort": None, "periode": None, "relations": []},
    "famille": {"variantes": [], "periode": None, "armes": None, "relations": []},
    "lieu": {"variantes": [], "coordonnees": None, "commune_actuelle": None, "relations": []},
    "evenement": {"date": None, "fin": None, "relations": []},
    "institution": {"variantes": [], "periode": None, "relations": []},
    "source": {"titre": None, "auteur": None, "date_redaction": None, "genre": "autre", "nature": "etude",
               "fiabilite": "F", "consultee": "non", "depot": None, "cote": None, "ark": None, "url": None,
               "distance": None, "biais": None, "citee_par": [], "fichiers": [], "assertions": []},
    "hypothese": {"question": None, "sujets": [], "statut": "ouverte",
                  "hypotheses": [{"id": "H1", "enonce": None, "auteur": "humain", "confiance": "possible"},
                                 {"id": "H2", "enonce": None, "auteur": "agent", "confiance": "possible"}],
                  "predictions": [], "matrice": [], "contestations": [], "meneur": None, "confiance": "possible",
                  "verdict": None, "historique": [], "sous_questions": []},
    "enquete": {"hypothese": None, "date": None, "auteur": None, "predictions": [], "recherches": [],
                "ajouts": {"sources": [], "assertions": [], "fiches": []}, "changements": [],
                "verdict_avant": None, "verdict_apres": None},
}


def run(base, args):
    t = args.type
    if t not in base.schema.types or t == "recherche":
        raise SystemExit(f"type inconnu ou réservé : {t} (types : {', '.join(k for k in base.schema.types if k != 'recherche')})")
    fid = args.id or slugify(args.nom)
    if t == "enquete" and not args.id:
        fid = f"e-{datetime.date.today().isoformat()}-{slugify(args.nom)[:40]}"
    if fid in base.fiches:
        raise SystemExit(f"existe déjà : {base.fiches[fid].rel}")
    target = norm_name(args.nom)
    similar = [f for f in base.fiches.values() if f.type == t and
               any(norm_name(str(n)) == target for n in [f.nom] + as_list(f.get("variantes")))]
    if similar and not args.force:
        print("Fiche(s) proche(s) déjà présente(s) :")
        for f in similar:
            print(f"  {f.rel} — {f.nom}")
        raise SystemExit("Rien créé. Relancer avec --force si c'est bien une autre entité.")
    meta = {"id": fid, "type": t, "nom": args.nom}
    meta.update(TEMPLATES.get(t, {}))
    if t == "enquete":
        meta["date"] = datetime.date.today().isoformat()
        meta["auteur"] = git_user()
    path = os.path.join(BASE, base.schema.types[t]["dossier"], f"{fid}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=110) + "---\n\n")
    print(os.path.relpath(path, os.path.dirname(BASE)))
