---
id: bardies-ou-samiac
type: hypothese
nom: Bardies ou Samiac, auteur de l'article du BSA 1903
question: "L'article du Bulletin de la Société ariégeoise de 1903, p. 77-84, que le site familial attribue à l'abbé Samiac, est-il l'article du baron de Bardies ?"
sujets: [bardies-1903, site-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Un seul article, du baron de Bardies ; Samiac n'y est qu'informateur (détails notariaux) et l'attribution du site est erronée.", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Deux textes distincts, l'un de Bardies, l'autre de Samiac, cités aux mêmes pages.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Un seul article, écrit en collaboration : Samiac en est co-auteur.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "La table du BSA t. IX et le titre de l'article (p. 77) portent le seul nom de Bardies ; aucun article de Samiac n'occupe ces pages."
    ou_chercher: "BSA t. IX (1903-1904), Gallica bpt6k57278962 : table des matières et vue 85."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Un article signé de Samiac figure dans un BSA de 1903 aux p. 77-84 d'un autre volume ou fascicule."
    ou_chercher: "Tables des BSA 1902-1905 (Gallica)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "L'article est signé conjointement par Bardies et Samiac."
    ou_chercher: "BSA t. IX, p. 77 et p. 84 (signature), Gallica bpt6k57278962."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a13, H1: I, H2: CC, H3: C, note: "« Abbé Samiac, B.S.A année 1903 pp. 77-84 » : attribution d'un site peu fiable."}
  - {preuve: bardies-1903.a7, H1: CC, H2: N, H3: I, note: "Bardies dit tenir de Samiac les détails notariaux : rôle d'informateur, peu compatible avec une co-signature."}
  - {preuve: bardies-1903.a1, H1: C, H2: I, H3: C, note: "L'article de Bardies occupe précisément les p. 77-84 du t. IX."}
  - {preuve: r-2026-10-06-gallica-gabrielle-d-espinas, H1: C, H2: I, H3: C, note: "« Gabrielle d'Espinas » n'apparaît que dans un imprimé, l'article de Bardies."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Les pages citées par le site (BSA 1903, p. 77-84) sont exactement celles de l'article de Bardies, seul imprimé où Gallica trouve Gabrielle, et Bardies remercie Samiac pour des détails notariaux. Il s'agit très vraisemblablement d'un seul texte, de Bardies, que le site attribue à son informateur : H1 est plausible, à confirmer sur la page de titre."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Raisonnement

Le site familial cite « Abbé Samiac, B.S.A année 1903 pp. 77-84 » [[site-roquemaurel.a13]]. L'article de Bardies
sur les guerres de religion en Couserans occupe les p. 77-84 du t. IX (1903-1904) [[bardies-1903.a1]], et le
plein texte de Gallica ne trouve « Gabrielle d'Espinas » que dans ce seul imprimé
([[r-2026-10-06-gallica-gabrielle-d-espinas]]). Bardies précise que les détails notariaux (actes de Marc Dupuy,
notaire à Saint-Girons, 1560 ; de Roque, 1557) lui ont été fournis par l'abbé Samiac [[bardies-1903.a7]].

**Inférence des notes** : les deux références désignent un seul texte ; le site a pris l'informateur pour
l'auteur. Si c'est le cas, [[site-roquemaurel]] et [[bardies-1903]] ne sont pas deux témoins indépendants pour
les faits qu'ils partagent.

La vérification de la page de titre sur Gallica ([[bardies-ou-samiac#P1]]) suffit à trancher.
