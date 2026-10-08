---
id: arbitrage-d-agen
type: hypothese
nom: Texte primaire de l'arbitrage d'Agen
question: "Où se trouve le texte de l'arbitrage rendu à Agen devant Monluc le 7 septembre 1567 entre Dominique Pontic et les syndics de Saint-Girons, du Couserans, de Lescure et de Montbrun, que le site familial cite d'après « Lestrade, op. cité » ?"
sujets: [arbitrage-d-agen-1567, dominique-pontic, blaise-de-monluc, saint-girons, etats-de-comminges]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "L'acte vient des registres des États de Comminges (Archives de Muret) et a été publié dans une autre série de Lestrade (Les Huguenots en Comminges, nouvelle série), que désigne « op. cité ».", auteur: humain, confiance: possible}
  - {id: H2, enonce: "L'acte a été publié dans la Revue de Comminges (t. X, t. XI ou autre).", auteur: agent, confiance: possible}
  - {id: H3, enonce: "L'acte a été publié ou résumé dans Bardies et Lestrade, Les Huguenots en Couserans (1933).", auteur: agent, confiance: possible}
  - {id: H4, enonce: "Aucun texte n'existe sous cette forme : référence erronée du site, acte mal daté ou mal décrit.", auteur: agent, confiance: possible}
  - {id: H5, enonce: "L'acte est bien dans le volume de 1900 de Lestrade, à une page que la recherche du 7 octobre n'a pas atteinte (OCR défaillant).", auteur: agent, confiance: improbable}
predictions:
  - id: P1
    h: H1
    attendu: "Un fascicule de la nouvelle série de Lestrade imprime l'arbitrage d'Agen du 7 septembre 1567."
    ou_chercher: "Lestrade, Les Huguenots en Comminges, nouvelle série (Gallica bpt6k96047673 et fascicules suivants) : ./pq search gallica-texte <ark> Agen Pontic."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "La Revue de Comminges imprime l'acte (avec la requête des villes ou à part)."
    ou_chercher: "Revue de Comminges t. X et XI (OCR archive.org revuedecomminges10 / 11) ; tables de la revue."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Bardies et Lestrade, Les Huguenots en Couserans (1933, rééd. 2007), cite ou imprime l'arbitrage d'Agen."
    ou_chercher: "Bardies et Lestrade, Les Huguenots en Couserans (1933) ; bibliothèque (non en ligne a priori)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H1
    attendu: "Les registres des États de Comminges conservés à Muret contiennent l'acte du 7 septembre 1567 ou le renvoi aux États de décembre 1567."
    ou_chercher: "Archives municipales de Muret, liasse 40, registres des États (salle de lecture)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P5
    h: H5
    attendu: "L'OCR du volume de 1900 contient « Agen », « arbitrage », « Montbrun » ou « 7 septembre 1567 » dans un document de 1567."
    ou_chercher: "Lestrade 1900, OCR local leshuguenotsenc00gascgoog.txt."
    diagnostique: haute
    statut: infirmee
    resultat: "Rien trouvé dans le volume de 1900 (p. 3-10 et 42-46 lues de près, le reste par l'OCR)."
    preuves: [r-2026-10-07-lestrade-1900-arbitrage-d-agen]
    enquetes: []
matrice:
  - {preuve: r-2026-10-07-lestrade-1900-arbitrage-d-agen, H1: C, H2: C, H3: C, H4: C, H5: I, note: "Recherche négative dans le volume de 1900 : écarte surtout H5 (l'OCR peut toutefois manquer un passage)."}
  - {preuve: site-roquemaurel.a25, H1: C, H2: C, H3: C, H4: I, H5: C, note: "Le site donne des détails précis (parties, lettres d'Henri II données à Blois en 1555), qui supposent un texte réel ; source faible et non vérifiée."}
  - {preuve: site-roquemaurel.a26, H1: C, H2: C, H3: C, H4: I, H5: C, note: "Renvoi aux prochains États, cohérent avec l'accord des États de décembre 1567 rapporté par les notes."}
  - {preuve: lestrade-1900.a5, H1: C, H2: C, H3: C, H4: N, H5: C, note: "Le conflit existe : saisies et emprisonnements de gens du Comminges à la poursuite des syndics de Saint-Girons et de Saint-Lizier."}
  - {preuve: lestrade-1900.a8, H1: C, H2: C, H3: C, H4: N, H5: C, note: "L'ordonnance du 11 juillet 1567 cite les deux parties à comparaître devant Monluc : une audience ultérieure à Agen est attendue."}
contestations: []
meneur: null
confiance: possible
verdict: "Le texte reste introuvable. Il n'est pas dans le volume de 1900 de Lestrade, et rien ne départage encore la nouvelle série de Lestrade, la Revue de Comminges et le volume de 1933 sur le Couserans. Les détails donnés par le site rendent peu probable une invention pure, mais il est seul à les donner. La consultation de la nouvelle série sur Gallica (P1) est le test le moins coûteux."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Ce qu'on sait

Seul le site familial rapporte l'arbitrage d'Agen du 7 septembre 1567 : Monluc entend Dominique Pontic et les syndics de
Saint-Girons, du Couserans, de Lescure et de Montbrun ; Saint-Girons invoque des lettres d'Henri II données à Blois en
1555 ; Monluc renvoie l'affaire aux prochains États ([[site-roquemaurel.a25]], [[site-roquemaurel.a26]]). Le site cite
« Lestrade, op. cité ». L'acte n'est pas dans le volume de 1900 ([[lestrade-1900.a18]],
[[r-2026-10-07-lestrade-1900-arbitrage-d-agen]]).

Le contexte rend l'acte vraisemblable. En juillet 1567, les gens du Comminges se plaignent des saisies faites à la
poursuite des syndics de Saint-Girons et de Saint-Lizier ([[lestrade-1900.a5]], [[lestrade-1900.a10]]). Monluc ordonne
aux deux parties de comparaître avec leurs états et commissions ([[lestrade-1900.a8]]). Les notes rapportent aussi un
accord des États de Comminges de décembre 1567 accordant 600 l. à Saint-Girons, au Couserans et à Lescure ; ce fait n'a
pas encore d'assertion sourcée dans la base.

Remarque d'agent : le 7 septembre 1567 (julien) est un dimanche. Ce n'est pas impossible pour un arbitrage tenu chez
Monluc, mais c'est un point à vérifier sur le texte.

## Pourquoi aucune hypothèse ne mène

H1, H2 et H3 désignent trois publications possibles du même document de Muret. Rien dans la base ne les départage,
puisqu'aucune n'a été consultée. H4 (référence erronée) n'est contredite que par les détails du site, une source faible.
H5 est presque écartée par la recherche négative.
