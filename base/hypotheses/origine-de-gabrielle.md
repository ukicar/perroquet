---
id: origine-de-gabrielle
type: hypothese
nom: Origine familiale de Gabrielle d'Espinas
question: "De quelle famille Gabrielle d'Espinas, veuve d'Arnaud II de Roquemaurel, est-elle issue ?"
sujets: [gabrielle-d-espinas, famille-d-espinas-de-cardonne, pierre-espinas, achille-espinas]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Elle est fille de Pierre Espinas, seigneur de Cardonne (confrère à Lézat en 1528, testament du 4 janvier 1560), donc sœur d'Achille et de François Espinas.", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Elle appartient aux Espinas de Cardonne/Gouzens, mais par une autre branche ou un autre père que Pierre (Achille étant exclu comme père).", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Elle est issue d'une autre famille d'Espinas ou d'Espinasse du Comminges, sans lien avec les Cardonne (par ex. celle de Montesquieu-Volvestre).", auteur: agent, confiance: possible}
  - {id: H4, enonce: "Elle est issue d'une famille d'Espinas étrangère au Comminges et au Volvestre (origine autre ou inconnue).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Le testament de Pierre Espinas du 4 janvier 1560 nomme une fille Gabrielle (dotée ou mariée à Arnaud de Roquemaurel)."
    ou_chercher: "Minutes des notaires de Lézat, AD Ariège, série 5 E (salle de lecture) ; ou copie produite devant Bezons en 1669."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: [H1, H2]
    attendu: "L'inventaire de production de Gabriel et Jean-Auguste Espinas devant Bezons (jugement du 2 août 1669) cite, parmi les titres du XVIe s., une alliance ou une dot avec les Roquemaurel."
    ou_chercher: "Procès-verbaux de la recherche de noblesse de Bezons : AD Hérault, série C, ou AD Haute-Garonne, série C (salle de lecture) ; décision Sanson du 29 mars 1697, AD Tarn-et-Garonne."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: [H1, H2, H3, H4]
    attendu: "Le contrat de mariage d'Arnaud de Roquemaurel et de Gabrielle d'Espinas nomme son père et sa maison (Pierre Espinas de Cardonne sous H1)."
    ou_chercher: "Notaires du Couserans ou de Lézat, AD Ariège 5 E ; BnF Pièces originales 2544 (dossier Roquemaurel, non numérisé) ; Vuillier, Histoire de la famille de Roquemaurel (2000), bibliothèque du CGLanguedoc."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H2
    attendu: "Un autre Espinas de Cardonne contemporain de Pierre (frère, cousin) apparaît dans les actes de Lézat avec une fille Gabrielle."
    ou_chercher: "Notaires de Lézat (AD Ariège 5 E) ; livre de la confrérie Notre-Dame de Bethléem de Lézat cité en 1669."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P5
    h: H3
    attendu: "Des actes du XVIe s. montrent une famille d'Espinas ou d'Espinasse noble à Montesquieu-Volvestre ou ailleurs en Comminges, liée aux Roquemaurel ou nommant une Gabrielle."
    ou_chercher: "Notaires de Montesquieu-Volvestre et de Rieux (AD Haute-Garonne, 3 E) ; Vuillier 2000."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a1, H1: C, H2: C, H3: C, H4: I, note: "« d'une maison du Comminges » : Lézat (Cardonne) est en lisière du Comminges, Gouzens y touche ; phrase non sourcée."}
  - {preuve: site-roquemaurel.a11, H1: C, H2: C, H3: C, H4: I, note: "Le site range Gabrielle chez les d'Espinas « du Comminges », branche de Cardonne ; même identification que nos notes, pas une preuve indépendante."}
  - {preuve: aubais-pieces-fugitives.a2, H1: C, H2: N, H3: N, H4: N, note: "Pierre, confrère en 1528, est de la génération qui convient pour un père de Gabrielle."}
  - {preuve: aubais-pieces-fugitives.a4, H1: N, H2: N, H3: N, H4: N, note: "Aucune fille nommée ; mais un jugement de noblesse ne suit que la ligne masculine : silence non diagnostique."}
  - {preuve: inventaire-archives-ginestet.a1, H1: C, H2: N, H3: N, H4: N, note: "Achille marié en 1566 : exclu comme père, mais de la génération d'une sœur de Gabrielle."}
  - {preuve: bremond-1863.a2, H1: C, H2: C, H3: N, H4: N, note: "Les Espinas de Cardonne sont aussi seigneurs de Gouzens, en Volvestre : rend « maison du Comminges » acceptable pour eux."}
  - {preuve: registres-paroissiaux-lezat.a2, H1: C, H2: C, H3: N, H4: N, note: "Prénom Gabriel dans la lignée de Cardonne en 1611 : indice très faible."}
  - {preuve: ad31-serie-c-vingtiemes-rieux.a1, H1: N, H2: N, H3: C, H4: N, note: "D'autres d'Espinas et Lespinasse existent en Volvestre au XVIIIe s."}
  - {preuve: r-2026-10-07-gallica-espinas-de-cardonne-gabrielle, H1: N, H2: N, H3: N, H4: N, note: "Aucun imprimé ne relie Gabrielle à une famille précise : absence attendue sous toutes les hypothèses."}
contestations: []
meneur: H1
confiance: plausible
verdict: "L'hypothèse de travail des notes (H1, fille de Pierre Espinas de Cardonne) n'est contredite par rien et la chronologie l'accepte, mais aucun document ne nomme Gabrielle dans cette famille. L'appartenance aux Espinas de Cardonne (H1 ou H2) reste plausible ; la filiation précise ne sera tranchée que par le testament de Pierre (1560), la production de 1669 ou le contrat de mariage."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Ce que l'on sait

Le seul imprimé qui nomme Gabrielle est l'article de Bardies : « Gabrielle d'Espinas, veuve d'Arnaud de
Roquemaurel » [[bardies-1903.a3]]. Aucune source vue ne donne ses parents. Le site familial dit qu'Arnaud
épousa une femme « d'une maison du Comminges » [[site-roquemaurel.a1]] et range les d'Espinas sous une
« ancienne famille noble du Comminges » dont la branche de Cardonne fut maintenue en 1669
[[site-roquemaurel.a11]] ; c'est la même identification que nos notes, non une preuve indépendante.

## Les Espinas de Cardonne (H1, H2)

La lignée imprimée par Aubais commence à Pierre Espinas, seigneur de Cardonne, confrère de Notre-Dame de
Bethléem à Lézat en 1528 [[aubais-pieces-fugitives.a2]], qui teste le 4 janvier 1560
[[aubais-pieces-fugitives.a3]] et a pour enfants Achille et François [[aubais-pieces-fugitives.a4]].
Aucune fille n'est nommée, mais un jugement de noblesse ne suit que les mâles : ce silence ne pèse pas.
Achille, seigneur de Cardonne, se marie le 13 mai 1566 [[inventaire-archives-ginestet.a1]].

**Inférences des notes (non des faits sourcés)** :
- Gabrielle, mère avant février 1567 [[monluc-lettres-ruble.a3]], ne peut être fille d'Achille, marié en 1566.
- Pierre, confrère en 1528, est né vers 1500-1508 ou avant ; une fille née vers 1530-1548 est possible.
- Achille, marié en 1566, est né vers 1535-1545 : il peut être un frère de Gabrielle.
- Cardonne est un quartier de Lézat [[revue-de-gascogne-1920.a1]], dans le comté de Foix et le diocèse de
  Rieux, non au sens strict en Comminges ; mais la famille tient aussi Gouzens [[bremond-1863.a2]], en
  Volvestre, à la lisière du Comminges. La formule du site peut donc être approximative.
- La récurrence du prénom Gabriel dans la lignée [[registres-paroissiaux-lezat.a2]] n'est qu'un indice faible.

## Les autres hypothèses

H3 s'appuie sur l'existence d'autres d'Espinas et Lespinasse à Montesquieu-Volvestre au XVIIIe siècle
[[ad31-serie-c-vingtiemes-rieux.a1]], peut-être la même souche. H4 n'a pour elle que l'absence de toute
preuve positive ; elle est seulement gênée par la formule « maison du Comminges » d'un site peu fiable.

## Recherches déjà faites

Gallica et Geneanet n'ont rien donné qui relie Gabrielle à une famille
([[r-2026-10-07-gallica-espinas-de-cardonne-gabrielle]], [[r-2026-10-07-geneanet-releves-gabrielle-espinas]],
[[r-2026-10-06-gallica-gabrielle-d-espinas]]) ; les arbres en ligne la donnent sans parents
[[arbres-geneanet-roquemaurel.a1]]. L'armorial de La Roque n'a pas répondu à la recherche OCR
([[r-2026-10-06-la-roque-armorial-ocr-espinas]]).

## Ce qui trancherait

Le testament de Pierre Espinas ([[origine-de-gabrielle#P1]]), la production de 1669 ([[origine-de-gabrielle#P2]])
ou le contrat de mariage ([[origine-de-gabrielle#P3]]) : aucun n'est en ligne.
