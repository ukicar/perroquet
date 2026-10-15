---
id: date-de-l-execution-de-martin-tachard
type: hypothese
nom: Date de l'arrêt et de l'exécution de Martin Tachard
question: "Quel jour le parlement de Toulouse rendit-il l'arrêt contre Martin Tachard, et quel jour fut-il pendu : le 6 ou le 7 juillet 1567 ?"
sujets: [martin-tachard, execution-de-martin-tachard, parlement-de-toulouse]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "L'arrêt fut prononcé le 7 juillet 1567, signifié le même jour, et Tachard pendu ce jour-là (texte de 1570).", auteur: agent, confiance: plausible}
  - {id: H2, enonce: "L'arrêt fut rendu le 6 juillet 1567, puis signifié et exécuté le 7 (lecture qui concilie les deux dates du texte de 1619).", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Arrêt et exécution eurent lieu tous deux le 6 juillet 1567.", auteur: agent, confiance: improbable}
  - {id: H4, enonce: "Autre date, ou indéterminable sans le registre du parlement.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: [H1, H2, H3]
    attendu: "Le registre des arrêts criminels de juin-juillet 1567 contient l'arrêt contre Tachard avec sa date, et peut-être la mention de son exécution."
    ou_chercher: "AD Haute-Garonne, 1 B 3457, arrêts criminels de la Tournelle (catalogue-ad31.a2) ; à défaut, registres de la Grand'Chambre de juillet 1567."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: [H1, H2]
    attendu: "Les éditions intermédiaires (1582, f. 706 ; 1597, f. 698 ; 1608, f. 698, d'après Benoit) montrent quand « VII » est devenu « sixiesme » ; si le changement s'accompagne d'autres ajouts tirés du Discours de Pamiers, c'est une retouche d'éditeur et non une correction sur pièce."
    ou_chercher: "Gallica : Crespin, Histoire des martyrs, éditions de 1582, 1597, 1608 (rechercher « Tachard »)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: [H1, H2, H3]
    attendu: "Les annales de Toulouse (Lafaille) ou la France protestante datent l'exécution d'après une autre source que Crespin."
    ou_chercher: "Lafaille, Annales de Toulouse, t. II, année 1567 ; Haag, La France protestante, 1re éd., art. Tachard."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: crespin-1570.a25, H1: CC, H2: I, H3: I, H4: N, note: "1570 : « Prononcé à Tholouse en Parlement le VII. iour de Iullet »."}
  - {preuve: crespin-1570.a21, H1: C, H2: C, H3: I, H4: N, note: "1570 : arrêt signifié « LE VII. de Iullet » ; sous H1 et H2, signification et exécution le même jour."}
  - {preuve: crespin-histoire-des-martyrs.a9, H1: I, H2: C, H3: C, H4: N, note: "1619 : « le sixiesme iour de Iuillet ». Texte dérivé de 1570 ; le changement peut être une coquille, une retouche ou une correction sur pièce."}
contestations: []
meneur: H4
confiance: possible
verdict: "Indéterminable sans le registre du parlement (H4, par calcul ACH), mais parmi les dates proposées le 7 juillet 1567 (H1) est la mieux soutenue. Le texte de 1570, publié par Crespin trois ans après les faits, date l'arrêt et sa signification du même jour, le VII, et il est cohérent. Le « 6 juillet » vient de l'édition de 1619, qui se contredit en gardant le VII pour la signification. H2 (arrêt le 6, exécution le 7) reste possible. Seul le registre du parlement trancherait."
historique:
  - {date: "2026-10-08", changement: "création ; meneur H4 (possible), H1 plausible", cause: "lecture de l'édition de 1570 (crespin-1570.a21, a25) et relecture du texte de 1619 (crespin-histoire-des-martyrs.a9, a11)"}
sous_questions: []
---
## Ce que disent les textes

- **1570** (Crespin, dernière édition publiée par lui) : les commissaires Buet et Rudelle vont signifier l'arrêt
  « LE VII. de Iullet » ([[crespin-1570.a21]]) ; l'arrêt se termine par « Prononcé à Tholouse en Parlement le VII.
  iour de Iullet, M.D.LXVII. Ainsi signé, La Croix » ([[crespin-1570.a25]]). Puis : « CELA faict, aussi tost »
  Tachard chante le psaume 122, et « L'HEVRE venue » on le mène au supplice ([[crespin-1570.a26]],
  [[crespin-1570.a27]]). Le texte suggère une exécution le jour même, sans le dire en toutes lettres.
- **1619** (éd. Benoit) : même récit, signification « Le VII. de Iuillet » ([[crespin-histoire-des-martyrs.a11]]),
  mais l'arrêt est daté « le sixiesme iour de Iuillet » ([[crespin-histoire-des-martyrs.a9]]).

## Raisonnement

Le texte de 1619 recopie celui de 1570 : ses dates ne sont pas un second témoignage, sauf si l'éditeur a corrigé sur
une pièce. Or il ne corrige que l'une des deux dates, ce qui le rend incohérent sous H3 et ne s'accorde qu'avec H2
(un arrêt délibéré le 6 et signifié le 7). Sous H1, « sixiesme » est une retouche ou une erreur d'édition ; on sait
par ailleurs que le texte de 1619 a été retouché sur ce passage (le « chapeau blanc » ajouté,
[[crespin-histoire-des-martyrs.a3]]). La base retenait jusqu'ici le 6 juillet, d'après 1619 seul.

Le calcul ACH place en tête H4 (« indéterminable »), qui ne contredit rien. Parmi les dates précises, H1 a la plus
faible incohérence (0,36 contre 0,48 pour H2) et le témoin le plus ancien est cohérent avec lui-même. Seul le
registre (P1) permettrait de dépasser « plausible ».
