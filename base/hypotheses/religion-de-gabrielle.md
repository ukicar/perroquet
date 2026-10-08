---
id: religion-de-gabrielle
type: hypothese
nom: Religion de Gabrielle d'Espinas en 1567
question: "Gabrielle d'Espinas était-elle catholique ou réformée au moment de l'incendie de Soueix (février 1567) ?"
sujets: [gabrielle-d-espinas, famille-de-roquemaurel, incendie-de-soueix-1567]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Elle était catholique, et l'était de naissance ; aucune conversion n'est attestée.", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Elle était réformée en 1567 (née dans une famille gagnée à la Réforme ou convertie avant 1567).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Un acte de Gabrielle (testament, fondation, élection de sépulture, legs pour messes) révèle une pratique catholique."
    ou_chercher: "Notaires du Couserans (Saint-Girons, Oust) et de Lézat, AD Ariège, série 5 E (salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "L'arrêt du 24 mai 1567 désigne les deux prêtres tués comme chapelains de la maison de Soueix (pratique catholique du foyer)."
    ou_chercher: "AD31 1 B 2103 (arrêts en double, avril-mai 1567, salle de lecture) ; Vuillier 1998, p. 52 ; copie AJR."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Gabrielle (ou « la dame de Soueix ») figure parmi les religionnaires poursuivis ou dont les biens furent saisis en 1568-1569, ou dans un registre de consistoire (Pamiers, Le Mas-d'Azil)."
    ou_chercher: "Arrêts du Parlement de Toulouse 1568-1569 (AD31 1 B, numérisés jusqu'en 1587) ; registres protestants du comté de Foix (lieu de conservation à identifier)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a4, H1: C, H2: I, note: "Deux prêtres tués dans le château : présence de prêtres au foyer en 1567. Source tardive et copie privée de l'arrêt."}
  - {preuve: bardies-1903.a2, H1: C, H2: N, note: "Poursuite conjointe avec le procureur général du Parlement de Toulouse ; mais le procureur général se joint à toute poursuite pour meurtre."}
  - {preuve: monluc-lettres-ruble.a6, H1: I, H2: C, note: "Monluc dit les Roquemaurel « de la nouvelle religion » ; il parle de la famille du mari, non de Gabrielle."}
  - {preuve: monluc-lettres-ruble.a18, H1: C, H2: I, note: "Ruble indexe le seigneur de Roquemaurel comme gentilhomme catholique (famille du mari)."}
  - {preuve: discours-des-troubles-de-pamiers.a3, H1: C, H2: I, note: "« Ce Roquemaurel » mène les troupes royales contre les réfugiés protestants de Pamiers en mai 1567."}
  - {preuve: aubais-pieces-fugitives.a2, H1: C, H2: N, note: "Pierre Espinas confrère de N.-D. de Bethléem en 1528 : famille catholique, si origine-de-gabrielle#H1 est vraie."}
  - {preuve: registres-paroissiaux-lezat.a3, H1: C, H2: N, note: "Les Despinas de Lézat baptisent à la paroisse catholique (1589-1735) ; vaut seulement si Gabrielle est de cette famille."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Aucun document ne dit la religion de Gabrielle. Les indices qui touchent son foyer (prêtres tués au château, poursuite avec le procureur général) et sa famille probable (confrérie de Lézat) vont dans le sens d'une catholique ; seul Monluc, qui parle des Roquemaurel et non d'elle, les dit réformés. H1 est plausible, sans plus."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: [religion-des-roquemaurel, origine-de-gabrielle]
---
## Indices

Aucun texte ne dit la religion de Gabrielle. Les notes concluaient « très probablement catholique, et de
naissance ; aucune trace de conversion ». Les indices, du plus fort au plus faible :

1. **Deux prêtres tués au château de Soueix.** Le résumé de l'arrêt du 24 mai 1567 donné par le site familial
   accorde 1 000 livres « aux héritiers des deux prêtres assassinés dans le château de Soueix »
   [[site-roquemaurel.a4]]. Des prêtres vivant ou de passage au château indiquent une pratique catholique du
   foyer en 1567. La source est tardive et dépend d'une copie privée de l'arrêt [[site-roquemaurel.a8]].
2. **Poursuite avec le procureur général** du Parlement de Toulouse [[bardies-1903.a2]]. L'alliance convient à
   une plaignante catholique, mais le procureur général se joint d'office aux poursuites pour meurtre : peu
   diagnostique.
3. **Sa famille probable** (voir [[origine-de-gabrielle]]) : Pierre Espinas est confrère de Notre-Dame de
   Bethléem à Lézat en 1528 [[aubais-pieces-fugitives.a2]] et les Despinas baptisent à la paroisse de Lézat
   [[registres-paroissiaux-lezat.a3]]. Ces deux lignes ne valent que si [[origine-de-gabrielle#H1]] est vraie.
4. **La famille du mari est contradictoire** : Monluc dit les Roquemaurel « de la nouvelle religion »
   [[monluc-lettres-ruble.a6]], alors que Ruble les indexe comme catholiques [[monluc-lettres-ruble.a18]] et que
   le *Discours des troubles de Pamiers* montre « ce Roquemaurel » à la tête des troupes royales contre les
   réfugiés protestants [[discours-des-troubles-de-pamiers.a3]]. Voir [[religion-des-roquemaurel]].

## Limites

La question des conversions après 1567 est hors de portée : aucune source postérieure ne décrit Gabrielle,
hormis le procès de 1610 connu par le seul site familial [[site-roquemaurel.a7]]. « Depuis quand » ne peut être
daté plus finement que son baptême, inconnu (inférence des notes : née vers 1530-1548 dans une paroisse
catholique, avant que la Réforme ne gagne le comté de Foix dans les années 1560).
