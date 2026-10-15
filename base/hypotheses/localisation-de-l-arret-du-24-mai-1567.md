---
id: localisation-de-l-arret-du-24-mai-1567
type: hypothese
nom: Où se trouve le texte de l'arrêt du 24 mai 1567
question: "Où subsiste aujourd'hui le texte de l'arrêt du Parlement de Toulouse du 24 mai 1567 contre Soulan et ses complices ?"
sujets: [arret-du-24-mai-1567, parlement-de-toulouse, tournelle, grand-chambre]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Une copie officielle subsiste aux AD Haute-Garonne dans le registre des arrêts en double de la Grand Chambre 1 B 2103 (avril-mai 1567).", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Le texte subsiste aux AD Haute-Garonne, mais ailleurs que dans 1 B 2103 (registre criminel mal coté, sacs à procès, autre série).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Aucun exemplaire ne subsiste aux AD Haute-Garonne : le texte n'est connu que par des copies hors du dépôt (Azémar, copie AJR, preuves de famille).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Le registre 1 B 2103 contient, à la date du 24 mai 1567 ou peu après, l'arrêt contre Jean-François de Mauléon à la requête de Gabrielle d'Espinas et du procureur général."
    ou_chercher: "AD Haute-Garonne, 1 B 2103 (non numérisé, salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Le registre criminel de la Tournelle couvrant avril-mai 1567 existe dans la série 1 B 3356-3883."
    ou_chercher: "Catalogue en ligne des AD Haute-Garonne, série 1 B (Tournelle)."
    diagnostique: moyenne
    statut: infirmee
    resultat: "1 B 3456 couvre février-26 mars 1567 et 1 B 3457 commence le 2 juin 1567 : les cotes se suivent, aucun registre pour avril-mai."
    preuves: [r-2026-10-06-ad31-arret-du-24-mai-1567-lacunes]
    enquetes: []
  - id: P3
    h: H3
    attendu: "Vuillier (1998, p. 52) donne en réalité pour référence une copie privée ou les papiers Azémar, et non une cote des AD Haute-Garonne."
    ou_chercher: "Vuillier, Histoire de la famille de Mauléon (1998), bibliothèque du CGLanguedoc, Toulouse."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H2
    attendu: "Un sac à procès de la série 2 B ou un registre d'arrêts sur requête contient la procédure contre Soulan (1567)."
    ou_chercher: "AD Haute-Garonne, série 2 B (indexation partielle) ; registres d'arrêts sur requête de 1567 (cote à identifier)."
    diagnostique: moyenne
    statut: indecidable
    resultat: "Aucun sac 2 B indexé ne concerne Soueix ou Soulan ; l'indexation est partielle."
    preuves: [r-2026-10-06-ad31-2b-sacs-a-proces-soueix]
    enquetes: []
matrice:
  - {preuve: bardies-1903.a4, H1: I, H2: I, H3: C, note: "L'arrêt fut retrouvé par Azémar « en dehors des archives de la Haute-Garonne » ; en 1903 les arrêts en double n'étaient sans doute pas dépouillés."}
  - {preuve: lasnier-2008.a3, H1: C, H2: C, H3: I, note: "Vuillier cite « extrait des registres du parlement de Toulouse, AD Haute-Garonne » ; peut reprendre l'intitulé d'une copie privée."}
  - {preuve: site-roquemaurel.a8, H1: C, H2: C, H3: C, note: "« Extraits des registres du parlement de Toulouse ; copie AJR » : copie privée tirée d'un registre ; compatible avec tout."}
  - {preuve: catalogue-ad31.a2, H1: C, H2: I, H3: C, note: "Pas de registre de la Tournelle pour avril-mai 1567."}
  - {preuve: catalogue-ad31.a3, H1: N, H2: I, H3: C, note: "Lacune du registre de Grand Chambre sur parchemin entre le 13 mai et le 2 juin 1567."}
  - {preuve: catalogue-ad31.a4, H1: C, H2: N, H3: N, note: "Le registre des arrêts en double d'avril-mai 1567 (1 B 2103) subsiste, non numérisé."}
  - {preuve: ad31-1b-60.a1, H1: C, H2: C, H3: N, note: "Le registre civil couvre bien le 24 mai 1567 mais ne reproduit pas les arrêts criminels : l'arrêt doit être cherché dans le criminel (registre manquant d'avril-mai) ou en double (1 B 2103)."}
  - {preuve: catalogue-ad09.a1, H1: N, H2: N, H3: C, note: "AD Ariège 1 J 94 contient le procès de Gabrielle contre Soulan, 1567-1603 : un exemplaire ou un extrait de l'arrêt peut s'y trouver, hors des AD Haute-Garonne (va dans le sens de Bardies)."}
contestations: []
meneur: H1
confiance: possible
verdict: "Le registre criminel d'avril-mai 1567 et le registre de Grand Chambre de la même période manquent ; le registre civil 1 B 60, qui va en fait jusqu'au 2 juin, ne contient pas l'arrêt. Subsistent, non numérisés, le registre des arrêts en double 1 B 2103 (AD Haute-Garonne) et les pièces du procès de Gabrielle, 1567-1603, aux AD Ariège (1 J 94), où un exemplaire de l'arrêt peut se trouver. H1 et H3 restent à égalité : lire 1 B 2103 et 1 J 94."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "ligne ajoutée", cause: "ad31-1b-60.a1 (registre civil lu jusqu'au 31 mai 1567)"}
  - {date: "2026-10-08", changement: "ligne ajoutée ; confiance inchangée", cause: "propagation : catalogue-ad09.a1 (1 J 94)"}
sous_questions: []
---
## Les registres où l'arrêt devrait être

L'arrêt est criminel : il devrait figurer dans les registres de la Tournelle. Or 1 B 3456 couvre février-26 mars
1567 et 1 B 3457 commence le 2 juin [[catalogue-ad31.a1]], [[catalogue-ad31.a2]] : le registre d'avril-mai est
perdu. Le registre de Grand Chambre sur parchemin présente la même lacune (1 B 60 finit le 13 mai, 1 B 61
commence le 2 juin) [[catalogue-ad31.a3]]. Subsiste le registre papier des « arrêts en double » 1 B 2103,
avril-mai 1567, non numérisé [[catalogue-ad31.a4]]. Voir [[r-2026-10-06-ad31-arret-du-24-mai-1567-lacunes]].

**Inférence des notes** : les gentilshommes accusés pouvaient demander à être jugés en Grand Chambre ; la
sentence contre Soulan pourrait donc être copiée dans 1 B 2103. C'est une hypothèse, non un fait.

L'arrêt n'est pas dans les registres civils numérisés ni dans BnF fr. 5455, qui ne couvre que
novembre-décembre 1567 [[bnf-fr-5455.a1]].

## Les témoignages sur la copie connue

- Bardies : l'arrêt fut trouvé par Théophile Azémar « en dehors des archives de la Haute-Garonne »
  [[bardies-1903.a4]].
- Lasnier cite Vuillier (1998, p. 52) : « extrait des registres du parlement de Toulouse, AD Haute-Garonne »
  [[lasnier-2008.a3]].
- Le site familial travaille sur une copie privée : « Extraits des registres du parlement de Toulouse ; copie
  AJR » [[site-roquemaurel.a8]].

Bardies et Vuillier se contredisent. **Inférence** : l'intitulé « extrait des registres » d'une copie privée a
pu suffire à Vuillier pour écrire « AD Haute-Garonne » ; inversement, un registre non dépouillé en 1903
(1 B 2103) a pu échapper à Azémar. Le calcul ACH ne départage pas H1 et H3 (incohérence égale) ; H1 est
gardée comme meneur parce que c'est la seule hypothèse testable en salle de lecture ([[localisation-de-l-arret-du-24-mai-1567#P1]]),
et H2 recule depuis que le registre de la Tournelle est connu pour perdu ([[localisation-de-l-arret-du-24-mai-1567#P2]]).
