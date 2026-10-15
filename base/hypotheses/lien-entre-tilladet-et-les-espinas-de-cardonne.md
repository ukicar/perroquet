---
id: lien-entre-tilladet-et-les-espinas-de-cardonne
type: hypothese
nom: Lien entre Tilladet et les Espinas de Cardonne
question: "Le « capitaine Tilladet » (les Cassagnet) avait-il un lien de parenté, d'alliance ou de clientèle avec les Espinas de Cardonne, famille présumée de Gabrielle, et ce lien explique-t-il que Monluc l'ait envoyé en Couserans en 1567 ?"
sujets: [francois-de-cassagnet-saint-orens, antoine-de-cassagnet-tilladet, famille-de-cassagnet, famille-d-espinas-de-cardonne, gabrielle-d-espinas, blaise-de-monluc, expedition-de-monluc-en-couserans-1567]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Les Cassagnet-Tilladet étaient liés (parenté, alliance ou clientèle) aux Espinas de Cardonne ; c'est pour cela que Monluc envoya Tilladet en Couserans, pour venger Arnaud de Roquemaurel et protéger Gabrielle.", auteur: humain, confiance: improbable}
  - {id: H2, enonce: "Aucun lien avec les Espinas : Monluc choisit Tilladet pour des raisons de service (capitaine de la légion de Guyenne, son homme de confiance, étranger aux parties en querelle), dans une mission de pacification ordonnée par le roi.", auteur: agent, confiance: plausible}
  - {id: H3, enonce: "Un lien existait entre les Cassagnet et une des parties (Espinas, Roquemaurel, ou au contraire Astarac-Fontrailles ou Mauléon-Soulan), mais il ne fut pas la raison du choix de Tilladet.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Une généalogie ou un acte montre une alliance Cassagnet–Espinas (mariage, parrainage, procuration, témoin) au XVIe siècle."
    ou_chercher: "La Chenaye-Desbois, art. Cassagnet ; Noulens, Maisons historiques de Gascogne ; Lauzun, seigneurs de Fimarcon ; production des Espinas devant Bezons (AD Tarn-et-Garonne, série C, vers C 87, salle de lecture) ; Aubais, Pièces fugitives."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "La correspondance de Monluc ou les pièces de l'expédition (commission, ordonnance du 11 juillet 1567, rôle de 1568) donnent à Tilladet une mission envers la veuve de Roquemaurel ou sa famille (garde, restitution, protection)."
    ou_chercher: "Monluc, lettres, éd. Ruble, t. IV-V ; Lestrade 1900 (requête des villes du Comminges, ordonnance du 11 juillet 1567, rôle du 4 avril 1568) ; AM Muret, liasse 40."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Les pièces de 1567 décrivent une mission générale (lever des troupes hors du pays, raser les maisons de Fontrailles et de Soulan, cotiser des vivres, surprendre les réfugiés de Pamiers), sans rôle particulier pour Gabrielle ; et les généalogies des Cassagnet et des Espinas ne présentent aucune alliance."
    ou_chercher: "Monluc, lettres, éd. Ruble ; Lestrade 1900 ; La Chenaye-Desbois ; Aubais."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Une alliance Cassagnet avec les Roquemaurel, les Astarac-Fontrailles ou les Mauléon apparaît dans les généalogies, sans qu'aucune pièce de 1567 n'y fasse allusion."
    ou_chercher: "La Chenaye-Desbois, art. Cassagnet et Astarac ; Noulens ; Vuillier 1998 (Mauléon) et 2000 (Roquemaurel) ; Cabinet d'Hozier 298."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a14, H1: I, H2: CC, H3: N, note: "Monluc demande que Tilladet lève ses hommes hors du pays, parce que les gens du pays sont presque tous parents d'une partie ou de l'autre : le critère affiché est la neutralité, ce qui cadre mal avec un capitaine parent de la victime."}
  - {preuve: monluc-lettres-ruble.a17, H1: N, H2: C, H3: N, note: "« querelle particulière… où le Roy m'envoya » : mission royale de pacification."}
  - {preuve: lestrade-1900.a2, H1: N, H2: C, H3: N, note: "Les compagnies sont menées sur ordre du roi par Saint-Orens en qualité de colonel de la légion de Guyenne : choix de fonction."}
  - {preuve: monluc-lettres-ruble.a20, H1: N, H2: C, H3: N, note: "Dès 1566, Tilladet est l'homme de confiance de Monluc, envoyé porter ses lettres à la reine."}
  - {preuve: monluc-lettres-ruble.a5, H1: C, H2: C, H3: C, note: "Monluc s'indigne de l'atteinte à l'honneur de la veuve : compassion compatible avec toutes les hypothèses, non diagnostique."}
  - {preuve: monluc-lettres-ruble.a7, H1: C, H2: N, H3: C, note: "Les Roquemaurel sont « bien apparentés de toutes parts » : leurs alliances pèsent, mais rien ne nomme les Cassagnet."}
  - {preuve: la-chenaye-desbois.a3, H1: N, H2: C, H3: N, note: "Manaud de Cassagnet épouse en 1484 une Lasseran-de-Massencome, nom de la maison de Monluc : le lien connu des Cassagnet va vers Monluc lui-même, pas vers les Espinas (à confirmer)."}
  - {preuve: r-2026-10-08-lien-espinas-cassagnet-galard-occurrence, H1: I, H2: C, H3: I, note: "Aucun Espinas pertinent dans La Chenaye (vol. Cassagnet) ; même résultat dans Noulens, Galard et 1863 (r-…-occurrence-2, -3) et dans Monluc, t. I-V (r-2026-10-08-monluc-commentaires-et-lettres-ruble-t-0…) : pas d’alliance Cassagnet–Espinas dans ces imprimés (poids moyen)."}
contestations: []
meneur: H2
confiance: plausible
verdict: "Aucune source ne relie les Cassagnet aux Espinas de Lézat (Cardonne ou Caladroy) : les généalogies imprimées des Cassagnet et de leurs alliés et toute l'édition de Monluc ont été dépouillées sans résultat. Monluc donne lui-même la raison de son choix : lever des hommes hors du pays, parce que tout le pays est parent de l'une ou l'autre partie ; Tilladet y va comme colonel de la légion, sur ordre du roi. H2 (choix de service, sans lien) mène ; H1 demanderait une alliance documentée."
historique:
  - {date: "2026-10-08", changement: "création", cause: "proposée par l'utilisateur"}
  - {date: "2026-10-08", changement: "ligne ajoutée (recherche négative) ; verdict réécrit ; confiance inchangée", cause: "r-2026-10-08-lien-espinas-cassagnet-galard-occurrence (rapport de l'archiviste)"}
sous_questions: []
---
## La question

L'utilisateur propose que Tilladet ait eu un lien avec la famille de Gabrielle, les Espinas de Cardonne
(identification elle-même seulement plausible : [[origine-de-gabrielle]]), et que Monluc l'ait envoyé en Couserans
pour cette raison : venger Arnaud et protéger sa veuve. Deux choses sont à distinguer : **le lien existe-t-il**
(question de généalogie) et **a-t-il motivé le choix** (question de motifs, plus difficile).

## Ce qui pèse contre H1

- Monluc écrit au roi le 14 février 1567 qu'il faut faire lever trois ou quatre cents hommes par le capitaine
  Tilladet, et non des gens du pays, « parce qu'ilz sont presque tous parens d'une part ou d'autre »
  [[monluc-lettres-ruble.a14]]. Le motif qu'il donne lui-même est la **neutralité**. Un Tilladet allié à la veuve
  aurait contredit ce critère. Cela ne prouve pas qu'il n'y avait aucun lien (Monluc pouvait l'ignorer ou le taire),
  mais cela retire au lien son rôle d'explication.
- La mission est royale (« où le Roy m'envoya ») [[monluc-lettres-ruble.a17]] et Saint-Orens agit comme colonel de la
  légion de Guyenne [[lestrade-1900.a2]]. Tilladet est le capitaine de confiance de Monluc depuis au moins 1566
  [[monluc-lettres-ruble.a20]] : le choix s'explique sans parenté.
- Dans les faits, les troupes de Tilladet surprennent ensuite les réfugiés de Pamiers aux Cabannes
  ([[raid-des-cabannes-1567]]) : une pacification générale, pas une garde de la veuve. La justice pour Gabrielle
  passe par le Parlement de Toulouse, à sa requête et à celle du procureur général [[bardies-1903.a2]].

## Ce qui reste ouvert

- La compassion de Monluc pour « la pouvre femme » [[monluc-lettres-ruble.a5]] est réelle, mais elle ne dit rien
  d'un lien de famille.
- Le seul lien connu des Cassagnet dans nos sources va vers Monluc lui-même : Manaud de Cassagnet épousa en 1484
  Agnès de Lasseran-de-Massencome [[la-chenaye-desbois.a3]], nom de la maison de Monluc (rapprochement à vérifier :
  quelle branche des Lasseran ?).
- Aucune recherche n'a encore porté sur une alliance Cassagnet–Espinas : c'est l'objet de P1. Si elle était
  trouvée, H3 deviendrait au moins probable, et H1 devrait encore montrer que le lien a compté en 1567 (P2).

## Ce qui trancherait

Une alliance documentée dans les généalogies ou dans la production des Espinas devant Bezons (P1) ; une instruction
de Monluc ou de l'ordonnance du 11 juillet 1567 visant la veuve (P2).
