---
id: total-du-role-de-1568
type: hypothese
nom: Total du rôle de la taxe de 1568
question: "Quel est le total du « Rolle de la Taxe, vérification et modération » des fournitures de 1567, dressé le 4 avril 1568 : 4 017 l. 12 s. 6 d. (Lestrade) ou 3 964 l. (Bardies, site familial) ?"
sujets: [role-de-la-taxe-1568, expedition-de-monluc-en-couserans-1567, comminges]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Le rôle porte un total de 4 017 l. 12 s. 6 d. ; le chiffre de 3 964 l. est une faute (de calcul ou de copie) de Bardies, recopiée par le site.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Le total exact est de 3 964 l. ; le chiffre de Lestrade est fautif (lecture ou impression).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Le rôle porte bien 4 017 l. 12 s. 6 d., mais 3 964 l. est aussi un chiffre juste qui mesure autre chose (somme recalculée d'une partie des articles, sommes avant ou après modération, total sans un article).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Le rôle original porte en somme finale 4 017 l. 12 s. 6 d."
    ou_chercher: "Archives municipales de Muret, liasse 40, registres des États de Comminges (États de L'Isle-en-Dodon, juillet 1568) ; salle de lecture."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H3
    attendu: "L'addition des articles imprimés par Lestrade (p. 42-45) ne donne pas 4 017 l. 12 s. 6 d. mais un autre total, voisin de 3 964 l., ce qui expliquerait le chiffre de Bardies."
    ou_chercher: "Lestrade 1900, p. 42-45 (OCR archive.org leshuguenotsenc00gascgoog ou Gallica bpt6k62556243) : additionner tous les articles."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Bardies (BSA 1903, p. 77-84) indique d'où il tire 3 964 l. (autre copie du rôle, autre pièce)."
    ou_chercher: "Bardies 1903, Gallica bpt6k57278962, vues 85-92."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: lestrade-1900.a15, H1: CC, H2: I, H3: C, note: "Lestrade, éditeur du document d'après les archives de Muret : total de 4 017 l. 12 s. 6 d."}
  - {preuve: bardies-1903.a12, H1: I, H2: C, H3: C, note: "Bardies, qui rend compte du livre de Lestrade, donne 3 964 l. sans source distincte connue."}
  - {preuve: site-roquemaurel.a27, H1: N, H2: C, H3: N, note: "Le site donne aussi 3 964 l. ; il suit Bardies (qu'il attribue à Samiac) : non indépendant, pas compté contre H1."}
  - {preuve: lestrade-1900.a14, H1: C, H2: C, H3: C, note: "Articles du rôle (Saint-Lizier 955 l., Muret 200 l.) : les détails n'ont pas été additionnés ; non diagnostique en l'état."}
contestations: []
meneur: H3
confiance: possible
verdict: "Le total porté au rôle est probablement 4 017 l. 12 s. 6 d., chiffre de Lestrade, qui édite le document d'après les archives de Muret ; H1 et H3 s'accordent sur ce point. Les 3 964 l. de Bardies, recopiés par le site, sont soit une faute (H1), soit une autre grandeur juste (H3, en tête au calcul) ; l'explication des notes (total avant l'article de 600 l.) ne tient pas, l'écart n'étant que de 53 l. 12 s. 6 d. Il faut additionner les articles imprimés (P2)."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les chiffres

Lestrade publie le rôle du 4 avril 1568 d'après les archives de Muret et en donne le total : 4 017 l. 12 s. 6 d.
([[lestrade-1900.a15]] ; contexte : [[lestrade-1900.a11]], [[lestrade-1900.a14]]). Bardies, qui rend compte du livre de
Lestrade dans le *Bulletin de la Société ariégeoise*, écrit 3 964 l. ([[bardies-1903.a12]]). Le site familial reprend ce
chiffre ([[site-roquemaurel.a27]]) ; il cite l'article de Bardies sous le nom de Samiac, et sa source n'est donc pas
indépendante.

## L'explication des notes ne tient pas (calcul d'agent)

Les notes suggéraient que 3 964 l. pourrait être un total « avant l'article de 600 l. » (les 600 l. accordées en décembre
1567 à Saint-Girons, au Couserans et à Lescure). L'arithmétique ne le permet pas : 4 017 l. 12 s. 6 d. − 3 964 l. =
53 l. 12 s. 6 d., et non 600 l. Aucun des articles relevés dans les notes ne vaut 53 l. 12 s. 6 d. L'écart peut venir
d'une addition refaite par Bardies, d'un article omis ou d'une faute d'impression (H3 ou H1).

## Meneur

H1 et H3 donnent le même total pour le rôle (4 017 l. 12 s. 6 d.) ; elles ne diffèrent que sur le statut des 3 964 l.
Le calcul met H3 en tête parce que le chiffre de Bardies n'y est pas une erreur. Sans l'addition des articles, ce n'est
qu'une possibilité.

## Ce qui trancherait

Additionner les articles imprimés par Lestrade (P2), faisable sur l'OCR ; vérifier le total sur l'original de Muret (P1) ;
chercher si Bardies cite une autre pièce (P3).
