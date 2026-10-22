---
id: mariage-d-arnaud-et-gabrielle
type: hypothese
nom: Date du mariage d'Arnaud de Roquemaurel et de Gabrielle d'Espinas
question: "Quand Arnaud II de Roquemaurel épousa-t-il Gabrielle d'Espinas ?"
sujets: [arnaud-ii-de-roquemaurel, gabrielle-d-espinas]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Entre 1550 et 1560.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Vers 1541 (au plus tard en 1549).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Entre 1561 et 1566, peu avant l'incendie.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: [H1, H2, H3]
    attendu: "Le contrat de mariage d'Arnaud et de Gabrielle porte une date (entre 1550 et 1560 sous H1)."
    ou_chercher: "Notaires du Couserans ou de Lézat, AD Ariège 5 E ; BnF Pièces originales 2544 ; Vuillier 2000."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Le testament de Jean de Roquemaurel (27 octobre 1552) mentionne la femme ou les enfants d'Arnaud."
    ou_chercher: "Cabalby et Goudan, notaires de Vic (AD Ariège 5 E) ; copies dans BnF Pièces originales 2544 ou fr. 32298."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Le testament de Pierre Espinas (4 janvier 1560) nomme Gabrielle comme fille à doter, non encore mariée (si elle est sa fille)."
    ou_chercher: "Notaires de Lézat, AD Ariège 5 E ; production de 1669 devant Bezons."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: arbres-geneanet-roquemaurel.a2, H1: I, H2: C, H3: I, note: "« mariée vers 1541 », copié d'un arbre à l'autre, sans source."}
  - {preuve: site-roquemaurel.a14, H1: C, H2: C, H3: N, note: "Guillaume, second fils, né vers 1518 : Arnaud est né avant ; substitué par le testament de 1552, ce qui convient à un Arnaud sans enfant à cette date."}
  - {preuve: monluc-lettres-ruble.a3, H1: C, H2: N, H3: C, note: "« sa femme et quelque enfant qu'il avoit » sautent par la fenêtre : un enfant encore auprès de sa mère en 1567."}
  - {preuve: inventaire-archives-ginestet.a1, H1: C, H2: I, H3: C, note: "Si Gabrielle est sœur d'Achille (marié en 1566, né vers 1535-1545), un mariage vers 1541 est presque impossible ; vaut seulement sous origine-de-gabrielle#H1."}
  - {preuve: roquemaurel-familles-du-midi.a9, H1: C, H2: I, H3: C, note: "Si Gabrielle est fille de Jean de Caladroy (origine-de-gabrielle#H5, meneur), ses parents se marient vers 1540 (estimation du généalogiste) : elle naît au plus tôt vers 1541, et un mariage vers 1541 est exclu. Sans portée sous H6 (sœur de Jean)."}
contestations: []
meneur: H1
confiance: possible
verdict: "La date « vers 1541 » des arbres en ligne n'a aucun appui. Si Gabrielle est fille de Jean d'Espinas de Caladroy (marié vers 1540, selon une estimation), le mariage ne peut guère être antérieur au milieu des années 1550 ; si elle est sa sœur, il peut être plus ancien. Les notes le placent dans les années 1550-1560 par inférence : H1 est possible, sans preuve directe ; le contrat reste à trouver (notaires de Lézat ou du Couserans, AD Ariège 1 J 94)."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "verdict réécrit ; confiance inchangée", cause: "propagation : origine-de-gabrielle (branche de Caladroy, H5-H6)"}
  - {date: "2026-10-21", changement: "ligne ajoutée à la matrice et raisonnement complété pour la branche de Caladroy ; confiance inchangée", cause: "roquemaurel-familles-du-midi.a9 (mariage de Jean de Caladroy estimé vers 1540) ; le raisonnement ne traitait encore que la filiation par Pierre Espinas"}
sous_questions: [origine-de-gabrielle]
---
## Ce que l'on a

Aucun acte ne date le mariage. Les arbres Geneanet disent Gabrielle « mariée vers 1541 », d'après un seul arbre
recopié, sans source [[arbres-geneanet-roquemaurel.a2]]. Le site familial dit seulement qu'Arnaud épousa une
femme « d'une maison du Comminges » et qu'ils eurent « au moins un fils » [[site-roquemaurel.a1]],
[[site-roquemaurel.a2]].

## Raisonnement (inférences)

- Guillaume, second fils, est né vers 1518 [[site-roquemaurel.a14]] : Arnaud, l'aîné selon le site, serait né
  avant ; un mariage vers 1541 serait donc possible pour lui. Mais Monluc l'appelle « le jeune Rocquemaurel »
  [[monluc-lettres-ruble.a1]], ce qui, si « jeune » vaut cadet, contredirait l'ordre de naissance du site.
- Le testament paternel de 1552 substitue Guillaume à Arnaud [[site-roquemaurel.a14]] : une telle clause
  convient à un héritier encore sans enfant.
- En 1567 un enfant est encore auprès de Gabrielle [[monluc-lettres-ruble.a3]].
- Sous la piste en tête ([[origine-de-gabrielle#H5]]), Gabrielle est fille de Jean d'Espinas de Caladroy, dont le
  mariage est estimé vers 1540 par le généalogiste [[roquemaurel-familles-du-midi.a9]] : elle naîtrait au plus tôt
  vers 1541, ce qui exclut un mariage vers 1541 et rend difficile un mariage avant le milieu des années 1550. Si elle
  est plutôt la sœur de Jean ([[origine-de-gabrielle#H6]]), elle est d'une génération plus ancienne et cet argument
  tombe.
- Sous l'ancienne hypothèse, fille de Pierre Espinas et sœur d'Achille, marié en 1566
  [[inventaire-archives-ginestet.a1]], elle serait née vers 1530-1548 : un mariage vers 1541 serait de même exclu
  ([[origine-de-gabrielle#H1]], aujourd'hui seulement possible).

Le contrat de mariage ([[mariage-d-arnaud-et-gabrielle#P1]]) ou le testament de 1552
([[mariage-d-arnaud-et-gabrielle#P2]]) trancheraient.
