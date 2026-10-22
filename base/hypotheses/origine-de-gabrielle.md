---
id: origine-de-gabrielle
type: hypothese
nom: Origine familiale de Gabrielle d'Espinas
question: "De quelle famille Gabrielle d'Espinas, veuve d'Arnaud II de Roquemaurel, est-elle issue ?"
sujets: [gabrielle-d-espinas, famille-d-espinas-de-cardonne, jean-d-espinas-caladroy, antonie-de-montesquieu, martin-d-espinas, jean-arnaud-d-espinas, pierre-espinas, achille-espinas]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Elle est fille de Pierre Espinas, seigneur de Cardonne (confrère à Lézat en 1528, testament du 4 janvier 1560), donc sœur d'Achille et de François Espinas.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Elle appartient aux Espinas de Cardonne/Gouzens, mais par une autre branche ou un autre père que Pierre et que Jean de Caladroy (Achille étant exclu comme père).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Elle est issue d'une autre famille d'Espinas ou d'Espinasse du Comminges, sans lien avec les Espinas de Lézat (Cardonne, Caladroy, Gouzens).", auteur: agent, confiance: improbable}
  - {id: H6, enonce: "Elle est la sœur (et non la fille) de Jean d'Espinas de Caladroy : tante de Martin, grand-tante de Jean d'Espinas (« tante » au sens large en 1603) ; la génération s'accorde mieux avec l'âge d'Arnaud II.", auteur: agent, confiance: possible}
  - {id: H5, enonce: "Elle est fille de Jean d'Espinas, seigneur de Caladroy à Lézat, et d'Antonie de Montesquieu, sœur de Martin d'Espinas (branche de Caladroy, probablement issue d'un frère ou d'un fils de Pierre de Cardonne).", auteur: agent, confiance: plausible}
  - {id: H4, enonce: "Elle est issue d'une famille d'Espinas étrangère au Comminges et au Volvestre (origine autre ou inconnue).", auteur: agent, confiance: improbable}
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
  - id: P6
    h: H5
    attendu: "L'arrêt du 22 novembre 1603 (et celui du 3 septembre 1603) nomme Gabrielle d'Espinas comme « sa tante », sœur de son père Martin, la dit feue, et présente Jean d'Espinas comme son héritier (non comme cessionnaire de ses droits)."
    ou_chercher: "AD Ariège, 1 J 94 (salle de lecture ou demande de reproduction)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P7
    h: [H1, H5]
    attendu: "Les registres paroissiaux de Lézat (GG 1, à partir de 1561 environ) nomment Gabrielle d'Espinas avec des Espinas de Caladroy (marraine en 1589, parrainages croisés)."
    ou_chercher: "Registres paroissiaux de Lézat-sur-Lèze, AD Ariège (numérisés en ligne ; site qui bloque les agents)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P8
    h: [H5, H6]
    attendu: "Les contrats de mariage d'Anne (26 janvier 1594) et de Claire d'Espinas (5 septembre 1599), petites-filles de Jean de Caladroy, nomment Gabrielle parmi les parents (tante ou grand-tante) ou la disent feue."
    ou_chercher: "Insinuations citées par la généalogie de 2026 (AD Haute-Garonne, registres d'insinuations 6 et 8, à confirmer) ; salle de lecture."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P9
    h: [H1, H5, H6]
    attendu: "Si les Caladroy ont acquis la créance par cession (et non par héritage), un acte entre Gabrielle et Jean ou Martin d'Espinas, payé 1 000 écus, existe chez les notaires de Lézat ; sous H5-H6, aucun acte de cession, mais un testament ou une succession ab intestat."
    ou_chercher: "Notaires de Lézat, 1567-1603 (AD Ariège 5 E) ; AD Ariège 1 J 94."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a1, H1: N, H2: N, H5: N, H6: N, H3: N, H4: I, note: "« d'une maison du Comminges » : Lézat (Cardonne) est en lisière du Comminges, Gouzens y touche ; phrase non sourcée. [Contestation 08/10 : « Comminges » au sens large couvre Lézat et le Volvestre ; non diagnostique entre H1-H3.]"}
  - {preuve: site-roquemaurel.a11, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Le site range Gabrielle chez les d'Espinas « du Comminges », branche de Cardonne ; même identification que nos notes, pas une preuve indépendante. [Contestation 08/10 : même auteur que la généalogie de 2026, opinion antérieure fondée sur l'homonymie : neutralisée pour ne pas compter deux fois le même auteur.]"}
  - {preuve: aubais-pieces-fugitives.a2, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Pierre, confrère en 1528, est de la génération qui convient pour un père de Gabrielle."}
  - {preuve: aubais-pieces-fugitives.a4, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Aucune fille nommée ; mais un jugement de noblesse ne suit que la ligne masculine : silence non diagnostique."}
  - {preuve: inventaire-archives-ginestet.a1, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Achille marié en 1566 : exclu comme père, mais de la génération d'une sœur de Gabrielle. [Contestation 08/10 : n'écarte qu'Achille, qu'aucune hypothèse ne propose : neutre.]"}
  - {preuve: bremond-1863.a2, H1: C, H2: C, H5: C, H6: C, H3: N, H4: N, note: "Les Espinas de Cardonne sont aussi seigneurs de Gouzens, en Volvestre : rend « maison du Comminges » acceptable pour eux."}
  - {preuve: registres-paroissiaux-lezat.a2, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Prénom Gabriel dans la lignée de Cardonne en 1611 : indice très faible. [Contestation 08/10 : indice de prénom trop faible : neutre.]"}
  - {preuve: ad31-serie-c-vingtiemes-rieux.a1, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "D'autres d'Espinas et Lespinasse existent en Volvestre au XVIIIe s. [Contestation 08/10 : XVIIIe s. et même juridiction que Cardonne : rien pour H3.]"}
  - {preuve: bnf-fr-32552.a2, H1: N, H2: C, H5: C, H6: C, H3: N, H4: N, note: "Le testament de Pierre (1560) nomme aussi un neveu Pierre : une autre ligne d'Espinas existait, ce qui donne corps à H2 ; filles non relevées, rien contre H1. [Contestation 08/10 : silence voulu sur les filles ; « neveu » peut valoir petit-fils : seulement un indice d'autres lignes.]"}
  - {preuve: gondal-1969.a1, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Un Jehan d'Espinas, seigneur de Cardonne en 1569 (renseignement privé) : autre Espinas contemporain, peut-être d'une autre ligne. [Contestation 08/10 : probablement Jean de Caladroy confondu avec un seigneur de Cardonne ; neutre.]"}
  - {preuve: inventaire-ad09-serie-b-1894.a1, H1: N, H2: N, H5: N, H6: N, H3: N, H4: I, note: "Un château de Cardonne « juridiction de Montesquieu-Volvestre » au XVIIIe s. : les Espinas de Cardonne seraient aussi du Volvestre, ce qui rend « maison du Comminges » plus littéral et rapproche H3 de H1-H2."}
  - {preuve: r-2026-10-07-gallica-espinas-de-cardonne-gabrielle, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "Aucun imprimé ne relie Gabrielle à une famille précise : absence attendue sous toutes les hypothèses."}
  - {preuve: roquemaurel-familles-du-midi.a2, H1: I, H2: I, H5: C, H6: C, H3: II, H4: II, note: "Arrêt du 22 novembre 1603 (AD Ariège 1 J 94, résumé par J. de Roquemaurel) : Jean d'Espinas de Caladroy, fils de Martin, succède « à sa tante » et reprend les droits de Gabrielle nés de l'arrêt de 1567. Source moderne, non indépendante du site familial, acte non vu. [Contestation 08/10 : CC → C. La tante n'est pas nommée et Gabrielle n'y est pas dite « feue » ; « tante » peut valoir grand-tante (H6) ; les 1 000 écus pourraient être le prix d'une cession de créance, sans parenté.]"}
  - {preuve: roquemaurel-familles-du-midi.a4, H1: N, H2: N, H5: N, H6: N, H3: I, H4: I, note: "Une Gabrielle d'Espinas marraine à Lézat en 1589 : une Gabrielle dans la parenté de Lézat ; homonymie possible. [Contestation 08/10 : identité de la marraine non établie ; ne vaut que pour l'ancrage à Lézat.]"}
  - {preuve: catalogue-ad09.a2, H1: C, H2: C, H5: C, H6: C, H3: N, H4: N, note: "Catalogue des AD Ariège, indépendant du généalogiste : un Jean d'Espinas plaide en 1607-1610 sur les biens de Soulan, dans le même article que le procès de Gabrielle (1567-1603). Confirme la cote et le lien Espinas–affaire de Soueix, pas la parenté exacte (héritage ou cession)."}
  - {preuve: registres-paroissiaux-lezat.a5, H1: N, H2: N, H5: C, H6: C, H3: N, H4: N, note: "Registre original : noble Martin d'Espinas a en 1589 un fils Jean et une fille Claire, comme le dit la généalogie de 2026 ; confirme la famille de Caladroy, pas Gabrielle."}
  - {preuve: registres-paroissiaux-lezat.a8, H1: N, H2: N, H5: N, H6: N, H3: N, H4: N, note: "La date du 6 août 1589 donnée par la généalogie est fausse ; mais une Gabrielle d'Espinas est marraine en 1587 et 1588 (ligne a11)."}
  - {preuve: registres-paroissiaux-lezat.a9, H1: N, H2: N, H5: C, H6: C, H3: N, H4: N, note: "Registre original : Jean d'Espinas et Antonie de Montesquieu, mariés, ont une fille Catherine baptisée en 1561 à Lézat ; le couple de H5 existe (ne dit rien de Gabrielle)."}
  - {preuve: registres-paroissiaux-lezat.a12, H1: N, H2: N, H5: C, H6: C, H3: N, H4: N, note: "Martin d'Espinas est dit seigneur de Caladrue dans le registre (1588)."}
  - {preuve: registres-paroissiaux-lezat.a11, H1: C, H2: C, H5: C, H6: C, H3: I, H4: I, note: "Une « madamoyselle Gabrielle d'Espinas » est marraine à Lézat en 1587 et 1588 (a10, a11) : une Gabrielle dans la parenté de Lézat ; identité avec la veuve non établie."}
contestations:
  - date: "2026-10-08"
    par: avocat-du-diable
    objections:
      - "H5 repose sur une seule pièce : le résumé, par un généalogiste de la famille, d'un arrêt de 1603 non vu, avec une cote corrompue (« | J 94 ») et une date incohérente (3 septembre ou 3 novembre)."
      - "Dans ce résumé, la tante n'est pas nommée et Gabrielle n'est pas dite « feue » (seulement « veuve dudit feu de Roquemaurel »)."
      - "« il donna 1 000 écus » peut désigner le prix d'une cession de la créance aux Caladroy : la succession ne prouverait alors aucune parenté."
      - "Chronologie : Arnaud II, fils d'un mariage d'environ 1513, est plus âgé qu'une fille de Jean de Caladroy marié vers 1540 ; une sœur de Jean (grand-tante de Jean III) s'accorde mieux."
      - "Rien ne relie Gabrielle à Antonie de Montesquieu ; le rattachement de la branche de Caladroy à Pierre de Cardonne n'est pas démontré (autre Jean d'Espinas à Lézat, de Périnhasse)."
      - "Le site familial et la généalogie de 2026 ont le même auteur : les compter tous deux revient à compter deux fois la même opinion."
      - "Plusieurs lignes de matrice étaient notées C alors qu'elles ne départagent rien (Ginestet, prénom Gabriel, Gondal, vingtièmes de Rieux) ; H3 était mal posée (Montesquieu-Volvestre est la juridiction de Cardonne)."
    alternatives:
      - "H6 : sœur de Jean d'Espinas de Caladroy (grand-tante de Jean III)."
      - "Cession : les Caladroy détiennent la créance de Gabrielle par achat, la « tante » de 1603 étant une autre femme (testé par P9)."
      - "Découper H5 : père (Jean de Caladroy), mère (Antonie), branche (issue de Pierre de Cardonne ou de Jean del Vignal)."
    reponse: "Objections fondées. a2 abaissée de CC à C et étendue à H6 ; site-roquemaurel.a11 neutralisée (même auteur) ; lignes non diagnostiques passées à N ; H3 reformulée pour exclure les Espinas de Lézat ; H6 ajoutée ; P6 précisée (tante nommée, feue, héritier ou cessionnaire), P8 et P9 ajoutées. Le découpage de H5 est noté dans le raisonnement : la mère et la branche ne sont pas dans la matrice comme preuves. Seule la lecture de 1 J 94 peut faire monter H5."
    effet: "H5 reste en tête, plausible mais fragile ; H6 ajoutée (possible) ; H2, H3, H4 → improbable ; H1 possible"
meneur: H5
confiance: plausible
verdict: "Seule pièce directe : le résumé, par le généalogiste de la famille, d'un arrêt du 22 novembre 1603 (AD Ariège 1 J 94, non vu) où Jean d'Espinas de Caladroy succède à « sa tante » et reprend les droits de Gabrielle. H5 (fille de Jean de Caladroy) mène, à égalité de cohérence avec H6 (sa sœur) ; le tout reste fragile : tante non nommée, cession possible, auteur non indépendant. Lire 1 J 94."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "ajout de H5 (Caladroy), qui devient meneur (plausible) ; H1 plausible → possible ; H2 restreinte aux autres branches", cause: "roquemaurel-familles-du-midi.a2 : arrêt du 22 novembre 1603 cité avec la cote AD Ariège 1 J 94"}
  - {date: "2026-10-08", changement: "trois lignes ajoutées à la matrice ; H2 renforcée (confiance inchangée)", cause: "BnF fr. 32552 (neveu Pierre en 1560), Gondal 1969, inventaire AD Ariège B 74"}
  - {date: "2026-10-08", changement: "contestation : a2 CC → C ; H6 ajoutée (possible) ; H2, H3, H4 possible → improbable ; lignes non diagnostiques neutralisées", cause: "objections de l'avocat du diable (même auteur pour site et généalogie, tante non nommée, cession possible)"}
  - {date: "2026-10-08", changement: "ligne ajoutée ; confiance inchangée", cause: "catalogue-ad09.a1-a2 : la cote 1 J 94 et le procès 1567-1603 sont confirmés par le catalogue des AD Ariège"}
  - {date: "2026-10-08", changement: "lignes ajoutées (registre de Lézat lu sur l'original)", cause: "registres-paroissiaux-lezat.a5, a8"}
  - {date: "2026-10-08", changement: "trois lignes ajoutées (registres de Lézat relus sur l'original) ; confiance inchangée", cause: "registres-paroissiaux-lezat.a9, a11, a12"}
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

## Nouveaux indices (8 octobre 2026)

La liste des titres produits devant Bezons (BnF fr. 32552) montre que le testament de Pierre (1560) nommait, outre
Achille et François, **Pierre, son neveu** [[bnf-fr-32552.a2]] : une autre ligne d'Espinas vivait à Lézat, ce que
confirment un Jehan d'Espinas seigneur de Cardonne en 1569 [[gondal-1969.a1]] et une Domenge d'Espinasse mariée
aux Médrano [[revue-de-gascogne-1880.a1]]. Cela multiplie les pères possibles de Gabrielle (H2) sans rien retirer à
H1, puisque les filles ne sont jamais relevées dans ces preuves. Un château de Cardonne est dit au XVIIIe siècle
« juridiction de Montesquieu-Volvestre » [[inventaire-ad09-serie-b-1894.a1]] : si c'est la même seigneurie,
« maison du Comminges » devient plus littéral. Le jugement complet de Sanson (1697), copié dans BnF fr. 32296-32301,
devrait analyser tous les actes produits : à lire dès que Gallica répondra.

## La piste de Caladroy (H5)

Jacques de Roquemaurel, auteur du site familial, a publié en 2026 une généalogie qui fait de Gabrielle la fille de Jean
d'Espinas, seigneur de Caladroy (Caladrue) à Lézat, et d'Antonie de Montesquieu [[roquemaurel-familles-du-midi.a1]].
La preuve invoquée : un arrêt du 22 novembre 1603 où Jean d'Espinas, fils de Martin, héritier de son père et « de sa
tante » par arrêt du 3 septembre 1603, reprend les droits nés de l'arrêt du 24 mai 1567 obtenu par Gabrielle
[[roquemaurel-familles-du-midi.a2]], dite alors morte [[roquemaurel-familles-du-midi.a3]]. C'est la première
identification appuyée sur une cote (AD Ariège 1 J 94). Elle explique bien pourquoi un Espinas réclame en 1603 ce
qui était dû à Gabrielle. Mais la source n'est pas indépendante du site et l'acte n'a pas été vu ; le résumé est
obscur par endroits. L'auteur ne donne pas de fille Gabrielle à Pierre de Cardonne, et rattache la branche de
Caladroy aux Cardonne (« probablement un fils ou un neveu de Pierre ») : voir le neveu Pierre du testament de 1560
[[bnf-fr-32552.a2]].

Depuis, deux pièces indépendantes du généalogiste confirment le cadre, sans trancher la parenté : le catalogue des
AD Ariège décrit bien, sous la cote 1 J 94, le procès de Gabrielle contre Soulan de 1567 à 1603 et la procédure de
la vicomtesse de Soulan contre Jean d'Espinas en 1607-1610 [[catalogue-ad09.a1]] [[catalogue-ad09.a2]] ; et le
registre de Lézat montre en 1589 les enfants de « noble martin despinac », Jean et Claire
[[registres-paroissiaux-lezat.a5]]. La marraine « Gabrielle » de 1589 n'est pas à la date donnée [[registres-paroissiaux-lezat.a8]], mais une
« madamoyselle Gabrielle d'Espinas » est marraine à Lézat en novembre 1587 et en juin 1588
[[registres-paroissiaux-lezat.a10]] [[registres-paroissiaux-lezat.a11]] ; le baptême de Catherine, fille de Jean
d'Espinas et d'Antonie de Montesquieu (1561), et le titre de Martin, « s.r de caladrue », sont confirmés sur
l'original [[registres-paroissiaux-lezat.a9]] [[registres-paroissiaux-lezat.a12]]. La contestation du 8 octobre a ramené la pièce de 1603 à un poids moyen (tante
non nommée, cession possible) et ajouté H6 (sœur de Jean de Caladroy).

## Recherches déjà faites

Gallica et Geneanet n'ont rien donné qui relie Gabrielle à une famille
([[r-2026-10-07-gallica-espinas-de-cardonne-gabrielle]], [[r-2026-10-07-geneanet-releves-gabrielle-espinas]],
[[r-2026-10-06-gallica-gabrielle-d-espinas]]) ; les arbres en ligne la donnent sans parents
[[arbres-geneanet-roquemaurel.a1]]. L'armorial de La Roque n'a pas répondu à la recherche OCR
([[r-2026-10-06-la-roque-armorial-ocr-espinas]]).

## Ce qui trancherait

Le testament de Pierre Espinas ([[origine-de-gabrielle#P1]]), la production de 1669 ([[origine-de-gabrielle#P2]])
ou le contrat de mariage ([[origine-de-gabrielle#P3]]) : aucun n'est en ligne.
