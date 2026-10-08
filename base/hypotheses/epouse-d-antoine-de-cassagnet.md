---
id: epouse-d-antoine-de-cassagnet
type: hypothese
nom: Épouse d'Antoine de Cassagnet
question: "Qui était l'épouse d'Antoine de Cassagnet, seigneur de Tilladet, mère de Bernard (né en 1555) : Jeanne de Bezolles (Noulens) ou Jeanne de « Bresolles » (La Chenaye-Desbois) ?"
sujets: [antoine-de-cassagnet-tilladet, jeanne-de-bezolles, bernard-de-cassagnet-tilladet, famille-de-cassagnet]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Jeanne de Bezolles (seigneurie du Gers) ; « Bresolles » chez La Chenaye n'est qu'une graphie fautive du même nom.", auteur: humain, confiance: probable}
  - {id: H2, enonce: "Jeanne de Bresolles, d'une famille distincte des Bezolles ; Noulens aurait corrigé à tort.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Antoine eut une autre épouse, ou deux épouses successives dont une seule est connue ; la mère de Bernard reste à établir.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Un acte (contrat de mariage, testament d'Antoine ou de sa veuve, actes de Bernard) nomme « Jeanne de Bezolles », femme d'Antoine de Cassagnet, sieur de Tilladet."
    ou_chercher: "BnF, Cabinet des titres : Pièces originales et Dossiers bleus « Cassagnet » et « Bezolles » ; AD Gers, minutes notariales de Gondrin et de Valence-sur-Baïse (salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "L'imprimé de La Chenaye-Desbois (3e éd., art. « Cassagnet », col. 745-748) lu sur l'image porte une forme proche de Bezolles, ou la même édition déforme d'autres noms gascons (« Boulet » pour du Bouzet)."
    ou_chercher: "Gallica bpt6k54249441, vues 336-337 (lecture de l'image, pas de l'OCR)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Une famille noble « de Bresolles » est attestée en Gascogne au XVIe siècle et un acte la lie aux Cassagnet-Tilladet."
    ou_chercher: "Nobiliaires gascons (La Chenaye art. « Bresolles », O'Gilvy et Laffore) ; catalogue Gallica."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: noulens-1863.a4, H1: C, H2: I, H3: N, note: "Noulens, généalogiste gascon : « Jeanne de Bezolles »."}
  - {preuve: la-chenaye-desbois.a10, H1: N, H2: C, H3: N, note: "La Chenaye : « Jeanne de Bresolles » ; même prénom, nom à une lettre près."}
  - {preuve: la-chenaye-desbois.a5, H1: C, H2: N, H3: N, note: "La même notice (ou son OCR) écrit « Marguerite de Boulet » pour du Bouzet : elle déforme les noms gascons."}
  - {preuve: noulens-1863.a2, H1: C, H2: N, H3: N, note: "Noulens corrige La Chenaye sur le père de Marguerite du Bouzet : il est mieux informé sur ces familles."}
  - {preuve: la-chenaye-desbois.a11, H1: N, H2: N, H3: N, note: "Bernard, fils d'Antoine, né en 1555 ; sa mère n'y est pas nommée. Non diagnostique."}
contestations: []
meneur: H1
confiance: probable
verdict: "Antoine épousa probablement Jeanne de Bezolles. Noulens et La Chenaye s'accordent sur le prénom et ne divergent que d'une lettre sur le nom, et La Chenaye déforme d'autres noms gascons (« Boulet » pour du Bouzet). Aucun acte original n'a été lu : un second mariage (H3) n'est pas exclu."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les deux formes

Noulens donne pour femme à Antoine de Cassagnet « Jeanne de Bezolles » ([[noulens-1863.a4]]) ; La Chenaye-Desbois écrit
« Jeanne de Bresolles » ([[la-chenaye-desbois.a10]]). Le prénom est le même et les deux noms ne diffèrent que d'une
lettre. Selon les notes, Bezolles est une seigneurie du Gers. Les notes en concluent que la forme de
Noulens est la bonne : c'est une **inférence**, raisonnable.

## Pourquoi H1 mène

La même notice de La Chenaye (ou son OCR) déforme d'autres noms gascons : « Marguerite de Boulet » pour Marguerite du
Bouzet ([[la-chenaye-desbois.a5]]). Noulens corrige La Chenaye sur d'autres points de cette famille
([[noulens-1863.a2]]). On ne sait pas si « Bresolles » vient de l'imprimé ou de l'OCR : à vérifier sur l'image (P2).

## Ce qui reste ouvert

Aucun acte original (contrat, testament) n'a été lu. Si Antoine s'est marié deux fois, les deux formes pourraient
désigner deux femmes (H3), mais aucune source ne le suggère. La recherche dans O'Gilvy n'a rien donné sur les frères
([[r-2026-10-07-o-gilvy-freres-tilladet]]). La piste reste le Cabinet des titres (P1).
