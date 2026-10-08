---
id: preuves-de-malte-1763-1677
type: hypothese
nom: Preuves de Malte de 1763 et abrégé de 1677
question: "Les « preuves de Malte de Paul de Roquemaurel de Soueix, 21 avril 1763 » citées par Bardies et l'abrégé des preuves de Paul de Roquemaurel de Souis (1677) du Cabinet d'Hozier sont-ils deux dossiers distincts ?"
sujets: [preuves-de-malte-1763, cabinet-d-hozier-298, bardies-1903, famille-de-roquemaurel, supplique-de-soulan-au-roi]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Deux dossiers distincts : les preuves de 1677 pour Paul de Roquemaurel de Souis (né en 1663) et d'autres preuves, du 21 avril 1763, pour un Paul de Roquemaurel de Soueix plus tardif, qui reproduisent les mêmes titres.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Un seul dossier, celui de 1677 ; la date de 1763 est une erreur de Bardies (ou de sa source).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Le manuscrit d'Oust daté de 1763 est une copie ou expédition, faite en 1763, des preuves de 1677, et non de nouvelles preuves.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Un dossier de preuves d'un Roquemaurel daté de 1763 existe dans les archives de l'ordre de Malte (Grand Prieuré de Toulouse) ou à Malte, distinct de celui de 1677."
    ou_chercher: "Fonds du Grand Prieuré de Toulouse de l'ordre de Malte aux AD Haute-Garonne (cote à identifier) ; archives de l'ordre à Malte (National Library of Malta)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "Un Paul de Roquemaurel né vers 1740-1755 apparaît dans les registres paroissiaux d'Oust ou de Soueix."
    ou_chercher: "Registres paroissiaux d'Oust et de Soueix, AD Ariège (en ligne)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Relu sur les images, le texte de Bardies donne une autre date, ou la date « 1763 » s'avère une coquille de l'imprimé."
    ou_chercher: "Bardies, BSA t. IX, p. 77-84 (Gallica bpt6k57278962, vues 85-92)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Le manuscrit d'Oust porte une mention de copie ou d'expédition de 1763 de preuves faites en 1677."
    ou_chercher: "Manuscrit détenu en 1903 par la baronne de Roquemaurel à Oust (collection privée, localisation actuelle inconnue)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: bardies-1903.a5, H1: C, H2: I, H3: C, note: "Bardies décrit des preuves de Paul de Roquemaurel de Soueix du 21 avril 1763, manuscrit à Oust."}
  - {preuve: cabinet-d-hozier-298.a1, H1: C, H2: C, H3: C, note: "Abrégé de preuves de 1677 pour Paul de Roquemaurel de Souis, né en 1663 : même prénom, même terre ; compatible avec tout."}
  - {preuve: bardies-1903.a6, H1: C, H2: C, H3: C, note: "La supplique de Soulan est décrite presque dans les mêmes termes que dans l'abrégé de 1677 ; attendu sous toutes les hypothèses, des preuves postérieures reprenant les mêmes titres."}
  - {preuve: r-2026-10-06-geneawiki-preuves-de-malte-56-h, H1: N, H2: N, H3: N, note: "Aucun Roquemaurel dans la liste des preuves du Grand Prieuré de Saint-Gilles ; mais Toulouse relevait d'un autre prieuré."}
contestations: []
meneur: H1
confiance: possible
verdict: "Bardies décrit des preuves datées de 1763, l'abrégé du Cabinet d'Hozier des preuves faites en 1677 pour un Paul né en 1663 ; les deux citent la même supplique de Soulan. Rien ne départage deux dossiers distincts (H1) d'une copie de 1763 des preuves de 1677 (H3) ; l'erreur de date chez Bardies (H2) est la moins soutenue."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Les deux documents

- **Bardies (1903)** tire les faits de famille des « preuves de Malte de Paul de Roquemaurel de Soueix,
  21 avril 1763 », manuscrit chez la baronne de Roquemaurel à Oust [[bardies-1903.a5]], qui mentionnent une
  supplique de Soulan au roi sur l'incendie de Soueix et le meurtre d'Arnaud [[bardies-1903.a6]].
- **Cabinet d'Hozier 298** : abrégé des preuves de Paul de Roquemaurel de Souis, né en 1663, dressé à Toulouse
  en 1677 [[cabinet-d-hozier-298.a1]] ; il ne suit que la ligne directe [[cabinet-d-hozier-298.a2]] et
  mentionne la même « Suplique faite au Roi l'an 1567 » [[cabinet-d-hozier-298.a3]].

## Raisonnement

Même prénom, même terre, même pièce citée. Des preuves de Malte postérieures reprennent normalement les
titres déjà produits par un parent : la ressemblance des descriptions n'est donc pas diagnostique. Le calcul
ACH laisse H1 et H3 à égalité ; H1 est gardée comme meneur parce que c'est la lecture des notes, qui traitent
les deux documents comme distincts, et qu'elle se teste en ligne ([[preuves-de-malte-1763-1677#P2]]). La
recherche dans la liste du Grand Prieuré de Saint-Gilles ([[r-2026-10-06-geneawiki-preuves-de-malte-56-h]])
visait sans doute le mauvais prieuré : un candidat toulousain relevait du Grand Prieuré de Toulouse
(remarque de l'agent, à vérifier).

L'enjeu pour Gabrielle : si le manuscrit de 1763 est distinct et plus complet, il pourrait contenir des pièces
sur la branche d'Arnaud absentes de l'abrégé de 1677.
