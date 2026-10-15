"""`pq dossier <id>`: everything the base holds about one fiche, as plain text — the material for a biography."""
from .model import as_list


def run(base, fid):
    fi = base.fiches.get(fid)
    if not fi:
        print(f"Aucune fiche {fid}.")
        return 1
    m = fi.meta
    print(f"# {fi.nom}  ({fi.type}, {fi.rel})")
    for k in ("variantes", "naissance", "mort", "periode", "date", "fin"):
        if m.get(k) not in (None, [], ""):
            print(f"{k}: {m[k]}")
    print("\n## Relations (dans cette fiche)")
    for r in fi.relations():
        print(f"- {r.get('rel')} → {r.get('vers')} [{r.get('confiance')}] preuves={as_list(r.get('preuves'))}"
              + (f" hypothese={r['hypothese']}" if r.get("hypothese") else "") + (f" role={r['role']}" if r.get("role") else "")
              + (f" debut={r['debut']}" if r.get("debut") else "") + (f" note={r['note']}" if r.get("note") else ""))
    print("\n## Relations (depuis d'autres fiches)")
    for e in base.edges():
        if str(e["dst"]) == fid:
            print(f"- {e['src']} —{e['rel']}→ ici [{e['confiance']}] preuves={e['preuves']}"
                  + (f" hypothese={e['hypothese']}" if e.get("hypothese") else "") + (f" role={e['role']}" if e.get("role") else "")
                  + (f" note={e['note']}" if e.get("note") else ""))
    print("\n## Synthèse de la fiche\n" + fi.body.strip())
    print("\n## Assertions qui la nomment")
    for cid, (src, c) in sorted(base.claims.items()):
        if fid in [str(s) for s in as_list(c.get("sujets"))]:
            print(f"- [[{cid}]] source {src.get('fiabilite')}, crédibilité {c.get('credibilite')}, {c.get('information')}, "
                  f"vérifiée: {c.get('verifie')} | {c.get('locus')}" + (f" | daté {c['date']}" if c.get("date") else ""))
            print(f"    texte : {c.get('texte')}")
            if c.get("citation"):
                print(f"    citation : « {c['citation']} »")
    print("\n## Questions qui la concernent")
    for h in base.of_type("hypothese"):
        if fid in [str(s) for s in as_list(h.get("sujets"))] or fid in h.body or any(
                fid in str(x.get("enonce", "")) for x in as_list(h.get("hypotheses")) if isinstance(x, dict)):
            print(f"- [[{h.id}]] {h.get('question')}  → meneur {h.get('meneur')} ({h.get('confiance')}), statut {h.get('statut')}")
            for x in as_list(h.get("hypotheses")):
                if isinstance(x, dict):
                    print(f"    {x.get('id')} [{x.get('confiance')}] {x.get('enonce')}")
            print(f"    verdict : {h.get('verdict')}")
    if fid in base.biographies:
        print(f"\n## Biographie existante : base/biographies/{fid}.md")
    return 0
