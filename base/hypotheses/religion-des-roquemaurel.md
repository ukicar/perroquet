---
id: religion-des-roquemaurel
type: hypothese
nom: Religion des Roquemaurel en 1567
question: "Arnaud II de Roquemaurel et ses frères étaient-ils catholiques ou réformés à l'époque de l'incendie de Soueix ?"
sujets: [famille-de-roquemaurel, arnaud-ii-de-roquemaurel, guillaume-de-roquemaurel, girons-de-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Les Roquemaurel de Soueix, Arnaud compris, étaient réformés (lecture littérale de Monluc, 14 février 1567).", auteur: agent, confiance: improbable}
  - {id: H2, enonce: "Toute la fratrie (Arnaud, Guillaume, Girons) était catholique.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Famille partagée : Arnaud et Guillaume catholiques, Girons seul passé à la Réforme (attesté avec les religionnaires en 1573).", auteur: humain, confiance: plausible}
predictions:
  - id: P1
    h: H3
    attendu: "Les documents de Lestrade ou de Bardies et Lestrade nomment Girons de Roquemaurel parmi les capitaines religionnaires (Montbrun, 1573)."
    ou_chercher: "Bardies et Lestrade, Les Huguenots en Couserans (1933, rééd. 2007), ch. 1 ; Lestrade, Les Huguenots en Comminges, nouvelle série ; BSA t. IX, p. 130."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: [H2, H3]
    attendu: "Le testament de Guillaume (22 janvier 1570, Dis, notaire d'Oust) ou les actes de la famille contiennent des legs pieux catholiques."
    ou_chercher: "BnF Pièces originales 2544 (non numérisé) ; preuves de Malte de 1763 (collection privée, Oust)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H1
    attendu: "Arnaud, Guillaume ou leurs biens figurent parmi les religionnaires poursuivis ou saisis par le Parlement de Toulouse en 1568-1569."
    ou_chercher: "AD31 1 B, arrêts civils 1568-1569 (numérisés) ; arrêts criminels de la Tournelle (1 B 3457 et suivants)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H2
    attendu: "Le capitaine de Roquemaurel protestant de 1573 se révèle être un autre Roquemaurel que Girons (autre branche)."
    ou_chercher: "Bardies 1903, p. 130 ; Bardies et Lestrade 1933."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a6, H1: CC, H2: I, H3: C, note: "« les Rocquemaurelz, qui sont aussi de la nouvelle religion » : contemporain mais de seconde main ; peut étendre à la famille la religion d'un frère."}
  - {preuve: monluc-lettres-ruble.a8, H1: C, H2: N, H3: C, note: "L'aîné aurait été maréchal des logis du feu roi de Navarre : milieu navarrais."}
  - {preuve: bardies-1903.a8, H1: N, H2: N, H3: C, note: "Bardies : ce maréchal des logis était Girons ; l'information de Monluc vise donc Girons."}
  - {preuve: bardies-1903.a9, H1: C, H2: I, H3: CC, note: "Un capitaine de Roquemaurel protestant à Montbrun en 1573, identifié à Girons après correction."}
  - {preuve: monluc-lettres-ruble.a18, H1: I, H2: C, H3: C, note: "Index de Ruble : « Roquemaurel (s. de), gentilh. cath. »."}
  - {preuve: discours-des-troubles-de-pamiers.a3, H1: II, H2: CC, H3: C, note: "Récit protestant hostile : « ce Roquemaurel » mène les troupes royales contre les réfugiés de Pamiers (mai 1567)."}
  - {preuve: site-roquemaurel.a28, H1: I, H2: C, H3: I, note: "Girons aurait accompagné Tilladet aux Cabannes ; gêne H3 sauf conversion de Girons après 1567. Source faible."}
  - {preuve: site-roquemaurel.a4, H1: I, H2: C, H3: C, note: "Deux prêtres tués au château d'Arnaud."}
  - {preuve: cabinet-d-hozier-298.a7, H1: I, H2: C, H3: C, note: "Guillaume fait gentilhomme ordinaire de la chambre en mars 1569 pour ses services de guerre, en pleine troisième guerre."}
contestations: []
meneur: H3
confiance: plausible
verdict: "Monluc est seul à dire les Roquemaurel réformés, et son renseignement sur « l'aîné » vise en fait Girons. Tout le reste (prêtres au château, Roquemaurel guidant les troupes royales, Guillaume au service du roi en 1569) contredit un foyer réformé à Soueix. L'hypothèse d'une famille partagée, Girons seul protestant, est plausible."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Les témoignages

- **Monluc**, le 14 février 1567, écrit que « les Rocquemaurelz, qui sont aussi de la nouvelle religion »
  [[monluc-lettres-ruble.a6]], et que l'aîné fut maréchal des logis du feu roi de Navarre
  [[monluc-lettres-ruble.a8]]. Il écrit douze jours après les faits, de seconde main.
- **Bardies** corrige : ce maréchal des logis était Girons [[bardies-1903.a8]] ; il identifie aussi à Girons,
  après s'être d'abord trompé sur Guillaume, le capitaine de Roquemaurel protestant de Montbrun en 1573
  [[bardies-1903.a9]].
- **Ruble** indexe « Roquemaurel (s. de), gentilh. cath. » [[monluc-lettres-ruble.a18]].
- Le ***Discours des troubles de Pamiers***, récit protestant, montre « ce Roquemaurel » dressant avec les
  troupes royales l'entreprise contre les réfugiés de Pamiers aux Cabannes [[discours-des-troubles-de-pamiers.a3]].
  Le site familial dit que c'était Girons [[site-roquemaurel.a28]] (source faible), ce qui gênerait H3 si Girons
  était déjà réformé en mai 1567.
- Au foyer d'Arnaud, deux prêtres sont tués [[site-roquemaurel.a4]] ; Guillaume est fait gentilhomme ordinaire
  de la chambre en 1569 pour ses services de guerre [[cabinet-d-hozier-298.a7]].

## Raisonnement

Les notes concluent, d'après Lestrade (affirmation non encore versée comme assertion), que seul Girons était
protestant. **Inférence** : Monluc a pu étendre à toute la famille la religion de Girons, dont il cite justement
la charge navarraise. H1 se heurte au récit protestant de Pamiers, hostile aux Roquemaurel et pourtant
explicite sur leur alignement royal. H2 doit expliquer le capitaine protestant de 1573 et le propos de Monluc.
H3 n'est gênée que par la présence supposée de Girons aux Cabannes, qu'une conversion postérieure à mai 1567
suffirait à expliquer.

Voir aussi [[religion-de-gabrielle]].
