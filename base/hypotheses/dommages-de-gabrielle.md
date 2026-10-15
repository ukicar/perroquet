---
id: dommages-de-gabrielle
type: hypothese
nom: Gabrielle a-t-elle touché ses dommages
question: "Gabrielle d'Espinas a-t-elle perçu tout ou partie des réparations accordées par l'arrêt du 24 mai 1567 ?"
sujets: [gabrielle-d-espinas, arret-du-24-mai-1567, decret-du-25-juin-1575, arret-du-6-juillet-1576, proces-de-1610, jean-francois-de-mauleon]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Elle fut payée au moins en partie, sur le prix de la vente par décret des biens de Soulan (décret du 25 juin 1575, exécuté en 1576), le reliquat des 3 000 livres restant en procès en 1610.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Elle ne toucha jamais les sommes qui lui revenaient ; le procès encore pendant en 1610 en est la suite.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Elle fut payée intégralement, ou désintéressée par transaction, avant 1610 ; le procès de 1610 porte sur autre chose ou opposait d'autres parties.", auteur: agent, confiance: improbable}
predictions:
  - id: P1
    h: H1
    attendu: "Le procès-verbal d'exécution du décret ou l'ordre de distribution du prix nomme Gabrielle d'Espinas (ou ses ayants droit) parmi les opposants créanciers."
    ou_chercher: "Registres des décrets et saisies réelles du Parlement de Toulouse, 1575-1576 (AD31, cote à identifier) ; sacs à procès 2 B."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "L'arrêt de 1610 (ou son inventaire) dit les 3 000 livres dues en entier depuis 1567 et nomme les parties."
    ou_chercher: "AD31, registres d'arrêts civils de 1610 (non numérisés, salle de lecture) ; inventaire imprimé de la série B, tome 2."
    diagnostique: haute
    statut: indecidable
    resultat: "Les registres de 1610 ne sont pas en ligne et le tome 2 de l'inventaire imprimé manque sur archive.org : test impossible à distance."
    preuves: [r-2026-10-06-ad31-registres-1610-en-ligne, r-2026-10-06-inventaire-ad31-serie-b-tome-2]
    enquetes: []
  - id: P3
    h: [H1, H2]
    attendu: "Un sac à procès de la série 2 B concerne les dommages de Soueix ou le procès de 1610."
    ou_chercher: "Catalogue AD31, série 2 B."
    diagnostique: moyenne
    statut: indecidable
    resultat: "Aucun sac indexé ne concerne l'affaire ; l'indexation de la série 2 B est partielle."
    preuves: [r-2026-10-06-ad31-2b-sacs-a-proces-soueix]
    enquetes: []
  - id: P4
    h: H3
    attendu: "Une quittance de Gabrielle ou de ses héritiers, ou une transaction avec les détenteurs des biens de Soulan, se trouve chez les notaires du Couserans."
    ou_chercher: "AD Ariège, série 5 E (notaires de Saint-Girons, Oust), salle de lecture."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a7, H1: C, H2: CC, H3: I, note: "« L'amende de 3.000 livres destinée à Gabrielle d'Espinas fut l'objet d'un procès qui durait encore en 1610 » : sans note ni source."}
  - {preuve: ad31-1b-74.a7, H1: C, H2: N, H3: N, note: "Le décret est exécuté « en ce qui reste entre les opposans » : il y a une distribution entre créanciers où Gabrielle aurait pu figurer."}
  - {preuve: ad31-1b-74.a9, H1: N, H2: N, H3: N, note: "Gabrielle n'est pas nommée, mais l'entrée ne nomme que les parties à l'opposition : silence attendu."}
  - {preuve: site-roquemaurel.a19, H1: C, H2: C, H3: N, note: "Le décret adjuge à Guillaume la moitié de la part de Soulan : la famille du mari se paie sur les biens de Soulan, sans dire si la veuve en profite."}
  - {preuve: r-2026-10-06-ad31-2b-sacs-a-proces-soueix, H1: N, H2: N, H3: N, note: "Rien dans les sacs indexés ; indexation partielle."}
  - {preuve: roquemaurel-familles-du-midi.a2, H1: C, H2: C, H3: I, note: "En 1603, son neveu et héritier reprend encore devant le Parlement les droits nés de l'arrêt de 1567 : la créance n'était pas éteinte."}
  - {preuve: roquemaurel-familles-du-midi.a7, H1: C, H2: C, H3: I, note: "En 1607, Marguerite de Béon, détentrice des biens de Soulan, plaide contre ce neveu : le procès de 1610 oppose sans doute l'héritier de Gabrielle aux Béon-Soulan."}
  - {preuve: catalogue-ad09.a1, H1: C, H2: C, H3: I, note: "Le procès de Gabrielle contre Soulan court de 1567 à 1603 : la créance n'était pas réglée avant 1603."}
  - {preuve: catalogue-ad09.a2, H1: C, H2: C, H3: I, note: "En 1607-1610, Jean d'Espinas et la vicomtesse de Soulan plaident sur les places de Soulan et de Lescure : sans doute le procès de 1610."}
contestations: []
meneur: H1
confiance: possible
verdict: "Rien ne montre Gabrielle recevant les sommes de 1567. Son procès contre Soulan court de 1567 à 1603 (AD Ariège 1 J 94) ; en 1603 son neveu et héritier Jean d'Espinas reprend encore les droits nés de l'arrêt, et de 1607 à 1610 la vicomtesse de Soulan, détentrice des biens du meurtrier, plaide contre lui : la créance n'était donc pas éteinte (H3 affaiblie). Paiement partiel sur la vente par décret (H1) ou rien (H2) restent indécis ; les pièces de 1 J 94 trancheront."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "deux lignes ajoutées ; H3 affaiblie, confiance inchangée", cause: "roquemaurel-familles-du-midi.a2, a7 (arrêt de 1603, procès de 1607)"}
  - {date: "2026-10-08", changement: "deux lignes ajoutées ; H3 encore affaiblie", cause: "catalogue-ad09.a1, a2"}
  - {date: "2026-10-08", changement: "verdict réécrit ; confiance inchangée", cause: "propagation : catalogue-ad09.a1-a2, roquemaurel-familles-du-midi.a2, a7"}
sous_questions: [localisation-de-l-arret-du-24-mai-1567, enregistrement-du-decret-de-1575]
---
## Ce que l'on sait

Selon le résumé du site familial, l'arrêt du 24 mai 1567 accorde 5 000 livres pour les meubles, 3 000 livres
de dommages et 10 000 livres pour le « pallais » [[site-roquemaurel.a3]], et « l'amende de 3.000 livres
destinée à Gabrielle d'Espinas fut l'objet d'un procès qui durait encore en 1610 » [[site-roquemaurel.a7]],
phrase sans note. Le 25 juin 1575, Guillaume de Roquemaurel obtient un décret sur les biens de Soulan
[[ad31-1b-74.a5]], [[site-roquemaurel.a19]] ; le 6 juillet 1576, la cour ordonne qu'il soit exécuté « en ce qui
reste entre les opposans », malgré l'opposition de Jean-Antoine de Mauléon [[ad31-1b-74.a7]]. L'entrée ne
nomme personne d'autre [[ad31-1b-74.a9]].

## Raisonnement

**Inférence des notes** : dans une vente par décret, les « opposants » sont les créanciers qui se font payer
sur le prix ; titulaire de dommages adjugés, Gabrielle serait l'un d'eux. Ce n'est pas une preuve qu'elle fut
payée. Le procès de 1610 sur les 3 000 livres s'accorde avec H2 (rien payé) comme avec H1 (reliquat), et
contredit H3 s'il est exact.

**Parties probables en 1610 (inférence des notes, à chercher en salle de lecture)** : Gabrielle ou ses
héritiers (Espinas, ou les Roquemaurel de Soueix : [[marc-antoine-de-roquemaurel]] ou
[[jean-paul-de-roquemaurel]]) contre les détenteurs des biens de Soulan, [[marguerite-de-beon-de-sere]] puis
[[jean-louis-de-rochechouart]]. Le fait que Marguerite de Béon se soit emparée des biens de Soulan en 1603 vient
des notes sans source identifiée : il n'est pas utilisé ici comme preuve.

## Recherches faites

Registres de 1610 non numérisés ([[r-2026-10-06-ad31-registres-1610-en-ligne]]), tome 2 de l'inventaire
introuvable en ligne ([[r-2026-10-06-inventaire-ad31-serie-b-tome-2]]), sacs 2 B sans résultat
([[r-2026-10-06-ad31-2b-sacs-a-proces-soueix]]), 1 F 13 sans apport ([[r-2026-10-06-ad31-1-f-13-fonds-mondon]]).
