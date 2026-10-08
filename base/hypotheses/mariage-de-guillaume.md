---
id: mariage-de-guillaume
type: hypothese
nom: Date du mariage de Guillaume de Roquemaurel et de Françoise de Roques
question: "Quand Guillaume de Roquemaurel épousa-t-il Françoise de Roques : en 1553 ou en 1560 ?"
sujets: [guillaume-de-roquemaurel, francoise-de-roques]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Par contrat du 2 décembre 1553 (devant Dupuy, notaire à Saint-Girons).", auteur: humain, confiance: probable}
  - {id: H2, enonce: "En 1560, date portée en marge de l'abrégé des preuves de Malte de 1677.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "À une autre date.", auteur: agent, confiance: improbable}
predictions:
  - id: P1
    h: H1
    attendu: "La minute du contrat, datée du 2 décembre 1553, se trouve dans les registres de Dupuy, notaire à Saint-Girons."
    ou_chercher: "AD Ariège, série 5 E, notaires de Saint-Girons (salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "AD Tarn-et-Garonne C 95, cité par le site familial, date aussi le contrat de 1553."
    ou_chercher: "AD Tarn-et-Garonne, C 95."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Le corps de l'abrégé de 1677 (et non la seule marge) cite un contrat de mariage de 1560."
    ou_chercher: "Cabinet d'Hozier 298, dossier 8136, images 142-143 (Gallica btv1b100803203)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: bnf-fr-32298.a5, H1: CC, H2: II, H3: I, note: "Le jugement de 1700 cite le « Contract de Mariage ... du deux decembre mil cinq cens cinquante trois » parmi les titres produits."}
  - {preuve: site-roquemaurel.a16, H1: C, H2: I, H3: I, note: "Le site donne la même date ; il cite fr. 32298 et AD82 C 95, donc en partie dépendant."}
  - {preuve: cabinet-d-hozier-298.a9, H1: I, H2: C, H3: N, note: "Date de 1560 en marge de l'abrégé de 1677 : peut viser un autre acte (quittance de dot, ratification)."}
contestations: []
meneur: H1
confiance: probable
verdict: "Le jugement de maintenue de 1700 cite expressément un contrat de mariage du 2 décembre 1553, titre produit devant l'intendant ; la date de 1560 n'apparaît qu'en marge de l'abrégé de 1677. H1 est probable ; la marge peut renvoyer à un autre acte de 1560."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Les témoignages

- Le jugement de Le Gendre (22 avril 1700) qui maintient Octavien de Roquemaurel, sieur de Montastruc, cite le
  « Contract de Mariage dud. Noble Guillaume de Roquemaurel avec Françoise de Roques du deux decembre mil cinq
  cens cinquante trois » [[bnf-fr-32298.a5]].
- Le site familial donne la même date, avec la filiation de Françoise (fille de Jacques Roques de Saint-Girons et
  de Guillaumette alias Gaudiette de Méritens) et le notaire Dupuy [[site-roquemaurel.a16]] ; il cite fr. 32298 et
  AD Tarn-et-Garonne C 95, et n'est donc pas entièrement indépendant.
- L'abrégé des preuves de Malte de 1677 date l'alliance de 1560 en marge [[cabinet-d-hozier-298.a9]].

## Raisonnement

Le jugement de 1700 cite un titre produit, avec la date en toutes lettres ; une marge d'abrégé est une note de
travail. **Inférence de l'agent** : Bardies signale des actes de Marc Dupuy, notaire à Saint-Girons, des 10 avril
et 1er juillet 1560 [[bardies-1903.a7]] ; si l'un d'eux concernait la dot de Françoise, il expliquerait la marge
de 1677. Ce n'est qu'une piste.

Marc-Antoine, fils de Guillaume et de Françoise, est dit né vers 1565 [[site-roquemaurel.a22]] : sans portée
pour départager.
