---
id: identite-du-jeune-fontrailles
type: hypothese
nom: Identité du jeune Fontrailles
question: "Qui est le « jeune Fontrailles », frère du sénéchal d'Armagnac et beau-frère de Soulan, que Monluc désigne comme l'un des auteurs de l'attaque de Soueix ?"
sujets: [le-jeune-fontrailles, famille-d-astarac-fontrailles, jean-francois-de-mauleon, anne-d-astarac, jean-jacques-d-astarac]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Bernard d'Astarac, second frère du baron de Fontrailles, sénéchal d'Armagnac (identification de Bardies, « probablement »).", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Gabriel ou Michel d'Astarac, sous lesquels l'index de Ruble range les mentions de Fontrailles.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Un autre fils de Jean-Jacques d'Astarac, seigneur de Fontrailles, ni Bernard, ni Gabriel, ni Michel.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H2
    attendu: "Les pages de l'index de Ruble (t. V) renvoient la lettre 160 (14 février 1567) à l'article Gabriel ou Michel d'Astarac, et une note de Ruble donne le prénom."
    ou_chercher: "Monluc, Commentaires et lettres, éd. Ruble, t. V, p. 77-83 et index (archive.org commentairesetle05monl)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: [H1, H2, H3]
    attendu: "L'arrêt du 24 mai 1567 nomme, parmi les condamnés, le jeune Fontrailles avec son prénom."
    ou_chercher: "AD31 1 B 2103 (salle de lecture) ; Vuillier 1998, p. 52 et suiv. ; copie AJR."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H1
    attendu: "Un acte de famille des Astarac-Fontrailles (testament de Jean-Jacques d'Astarac, partage, contrat d'Anne d'Astarac du 8 mai 1560) nomme un fils cadet Bernard, vivant en 1567."
    ou_chercher: "Papiers Sentein (contrat de 1560) ; nobiliaires et généalogies imprimées des Astarac-Fontrailles (à identifier)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: bardies-1903.a10, H1: C, H2: I, H3: I, note: "Bardies : « probablement » Bernard d'Astarac, second frère du sénéchal ; sans source donnée."}
  - {preuve: monluc-lettres-ruble.a30, H1: I, H2: C, H3: I, note: "L'index de Ruble range les mentions de Fontrailles sous Gabriel et Michel d'Astarac ; on ignore sous lequel tombe la lettre de 1567 ; index sujet à erreurs."}
  - {preuve: monluc-lettres-ruble.a10, H1: C, H2: C, H3: C, note: "Frère du sénéchal d'Armagnac et beau-frère de Soulan depuis six mois : vrai de tout fils cadet de Jean-Jacques d'Astarac."}
  - {preuve: demembrement-vicomte-couserans.a4, H1: C, H2: C, H3: C, note: "Anne d'Astarac, femme de Soulan, est fille de Jean-Jacques d'Astarac, seigneur de Fontrailles : le jeune Fontrailles est son frère."}
contestations: []
meneur: H2
confiance: possible
verdict: "Le jeune Fontrailles est sûrement un frère d'Anne d'Astarac, femme de Soulan, et du sénéchal d'Armagnac ; son prénom n'est donné par aucune source primaire vue. Bardies dit « probablement » Bernard, l'index de Ruble donne Gabriel et Michel : le calcul met H2 légèrement devant, mais aucune hypothèse ne dépasse le possible."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Ce qui est sûr

Monluc fait du jeune Fontrailles le frère du sénéchal d'Armagnac, allié depuis six mois à son beau-frère le
sieur de Soulan [[monluc-lettres-ruble.a10]] ; il « n'a aucune religion » et pille indifféremment
[[monluc-lettres-ruble.a9]]. Soulan a épousé en 1560 Anne d'Astarac, fille de Jean-Jacques d'Astarac,
seigneur de Fontrailles et de Marestaing [[demembrement-vicomte-couserans.a3]],
[[demembrement-vicomte-couserans.a4]]. Le jeune Fontrailles est donc un fils cadet de Jean-Jacques
(inférence directe des notes), ce qui explique aussi la présence d'un sieur de Marestaing parmi les condamnés
[[site-roquemaurel.a9]].

## Le prénom

- Bardies l'identifie « probablement » à Bernard d'Astarac, second frère du baron de Fontrailles
  [[bardies-1903.a10]], sans donner sa source.
- L'index de Ruble range les mentions de Fontrailles sous Gabriel et Michel d'Astarac
  [[monluc-lettres-ruble.a30]] ; on ne sait pas sous quel article tombe la lettre de 1567. Cet index se trompe
  ailleurs sur les prénoms (il fait de François de Cassagnet un « Bernard », [[monluc-lettres-ruble.a29]]).

Les deux témoignages sont faibles ; le calcul ACH place H2 devant H1 d'une courte tête, uniquement par le
poids de l'édition Ruble. Vérifier l'index de Ruble ([[identite-du-jeune-fontrailles#P1]]) est le test le
moins coûteux ; l'arrêt de 1567 serait décisif ([[identite-du-jeune-fontrailles#P2]]).
