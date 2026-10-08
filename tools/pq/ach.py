"""Analysis of Competing Hypotheses (Heuer): scores computed from a hypothesis fiche's matrix.

Each matrix row is a piece of evidence (an assertion `source.aN` or a search `recherche-id`)
rated against every hypothesis: CC C N I II. A row's weight = source reliability x claim
credibility. The leading hypothesis is the one with the LOWEST weighted inconsistency
(evidence against it), not the one with the most support. Rows rated the same for every
hypothesis are non-diagnostic: they cannot discriminate and are flagged."""
from .model import as_list


def hyp_ids(fi):
    return [str(h.get("id")) for h in as_list(fi.get("hypotheses")) if isinstance(h, dict)]


def score(base, fi):
    voc = base.schema.voc["matrice"]
    hs = hyp_ids(fi)
    res = {h: {"incoherence": 0.0, "soutien": 0.0, "lignes": 0} for h in hs}
    rows = []
    for row in as_list(fi.get("matrice")):
        if not isinstance(row, dict):
            continue
        ref = str(row.get("preuve"))
        w = base.evidence_weight(ref)
        cells = {h: str(row.get(h, "N")) for h in hs}
        values = set(cells.values())
        diagnostic = len(values) > 1
        for h, c in cells.items():
            s = voc.get(c, {}).get("score", 0)
            if s < 0:
                res[h]["incoherence"] += w * -s
            elif s > 0:
                res[h]["soutien"] += w * s
            res[h]["lignes"] += 1
        rows.append({"preuve": ref, "poids": w, "cellules": cells, "diagnostique": diagnostic,
                     "note": row.get("note")})
    for h in hs:
        res[h]["incoherence"] = round(res[h]["incoherence"], 2)
        res[h]["soutien"] = round(res[h]["soutien"], 2)
    ranking = sorted(hs, key=lambda h: (res[h]["incoherence"], -res[h]["soutien"]))
    preds = [p for p in as_list(fi.get("predictions")) if isinstance(p, dict)]
    pstat = {}
    for p in preds:
        pstat[p.get("statut", "non_testee")] = pstat.get(p.get("statut", "non_testee"), 0) + 1
    leader = None
    if len(ranking) > 1 and rows:
        a, b = res[ranking[0]], res[ranking[1]]
        if (a["incoherence"], -a["soutien"]) < (b["incoherence"], -b["soutien"]):
            leader = ranking[0]   # strictly ahead; a tie means the evidence does not discriminate
    return {"hypotheses": res, "classement": ranking, "lignes": rows,
            "meneur_calcule": leader,
            "non_diagnostiques": sum(1 for r in rows if not r["diagnostique"]),
            "predictions": pstat}


def format_score(base, fi):
    s = score(base, fi)
    out = [f"{fi.id} — {fi.get('question', fi.nom)}"]
    names = {str(h.get("id")): h.get("enonce", "") for h in as_list(fi.get("hypotheses")) if isinstance(h, dict)}
    for h in s["classement"]:
        r = s["hypotheses"][h]
        out.append(f"  {h}: incohérence {r['incoherence']:>5}  soutien {r['soutien']:>5}  — {names.get(h, '')[:80]}")
    out.append(f"  meneur calculé : {s['meneur_calcule']}  (déclaré : {fi.get('meneur')})")
    out.append(f"  lignes : {len(s['lignes'])}, non diagnostiques : {s['non_diagnostiques']}")
    out.append(f"  prédictions : {s['predictions']}")
    return "\n".join(out)
