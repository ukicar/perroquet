---
id: commandant-en-couserans-1567
type: hypothese
nom: Commandant des troupes royales en Couserans en 1567
question: "Lequel des « Tilladet » commandait les compagnies levées par Monluc pour pacifier le Couserans et le Comminges au printemps 1567 : François de Cassagnet, seigneur de Saint-Orens, ou son frère aîné Antoine, seigneur de Tilladet ?"
sujets: [francois-de-cassagnet-saint-orens, antoine-de-cassagnet-tilladet, famille-de-cassagnet, expedition-de-monluc-en-couserans-1567, blaise-de-monluc, legion-de-guyenne]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Le « capitaine Tilladet » de 1567 est François de Cassagnet, seigneur de Saint-Orens (« Tilladet le jeune »), colonel de la légion de Guyenne.", auteur: humain, confiance: probable}
  - {id: H2, enonce: "Le « capitaine Tilladet » de 1567 est Antoine de Cassagnet, seigneur de Tilladet et de Caussens (« Tilladet l'aisné »).", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Les deux frères ont commandé en Couserans, ensemble ou l'un après l'autre (par exemple Saint-Orens pour la conduite des compagnies, Antoine pour la suite des opérations).", auteur: agent, confiance: possible}
  - {id: H4, enonce: "Le commandement revenait à un autre capitaine (Alexandre, Ampela…), Tilladet n'étant qu'un chef parmi d'autres ; ou la question est indéterminable.", auteur: agent, confiance: improbable}
predictions:
  - id: P1
    h: H1
    attendu: "L'original de la requête des villes du Comminges et les autres pièces de 1567 conservées à Muret (ordonnance du 11 juillet, états de dépense) nomment le chef « seigneur de Sainct Orens », « Tilladet le jeune » ou « colonel de la légion », jamais « Tilladet l'aisné » ni « seigneur de Tilladet et de Caussens »."
    ou_chercher: "Archives municipales de Muret, liasse 40, registres des États de Comminges (salle de lecture) ; texte imprimé dans Lestrade 1900, p. 3-10, et Revue de Comminges t. X."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "La commission royale ou la commission de Monluc pour l'expédition (printemps 1567, non publiée par Ruble) est adressée à Saint-Orens comme colonel des légionnaires."
    ou_chercher: "Commission à localiser : lettres de Charles IX et de Monluc de février-avril 1567 (BnF, fonds français ; coll. Harlay Saint-Germain) ; copies éventuelles dans les registres des États de Comminges (AM Muret, liasse 40)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Une pièce de mai-juin 1567 (rôle de la taxe, procédure contre Tachard, délibérations consulaires) nomme le chef « Tilladet l'aisné », « seigneur de Tilladet et de Caussens » ou Antoine de Cassagnet."
    ou_chercher: "Rôle du 4 avril 1568 (Lestrade 1900, p. 42-45, et original à Muret) ; arrêt du parlement de Toulouse contre Martin Tachard (6 juillet 1567 ; AD Haute-Garonne 1 B 3457, Tournelle, juin-juillet 1567, d'après catalogue-ad31.a2) ; Lafaille, Annales de Toulouse, t. II."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Les pièces de dépense de 1567-1568 distinguent deux chefs du nom de Tilladet, ou deux périodes (conduite des compagnies par Saint-Orens, puis présence d'un « sieur de Tilladet » jusqu'à son « partement »)."
    ou_chercher: "Rôle du 4 avril 1568 et pièces jointes (AM Muret, liasse 40 ; Lestrade 1900, p. 42-46)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P5
    h: H4
    attendu: "Le rôle de 1568 ou l'ordonnance du 11 juillet 1567 attribue la direction des compagnies à un autre capitaine (Alexandre, Ampela, Parron, Malvoisin)."
    ou_chercher: "Lestrade 1900, p. 42-46 ; AM Muret, liasse 40."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: lestrade-1900.a2, H1: CC, H2: II, H3: C, H4: I, note: "Seule pièce contemporaine qui nomme le chef : « le seigneur de Sainct Orens, colonel de la légion de Guienne », conducteur des compagnies et soi-disant commissaire."}
  - {preuve: revue-de-comminges-t10.a1, H1: C, H2: I, H3: N, H4: I, note: "Même requête réimprimée : pas une preuve indépendante, notée plus faiblement."}
  - {preuve: lestrade-1900.a8, H1: C, H2: C, H3: I, H4: I, note: "Ordonnance du 11 juillet 1567 : un seul « cappitaine Tilhadet », sans prénom, dont le départ clôt la période de dépense ; il est donc le chef, et l'ordonnance ne connaît qu'un Tilladet (contre H3)."}
  - {preuve: monluc-lettres-ruble.a14, H1: C, H2: C, H3: C, H4: I, note: "14 février 1567 : Monluc propose de faire lever 300-400 hommes par le « cappittaine Tilladet », sans prénom."}
  - {preuve: discours-des-troubles-de-pamiers.a2, H1: C, H2: C, H3: C, H4: I, note: "Trois cents arquebusiers « sous la charge du capitaine Tilladet », sans prénom."}
  - {preuve: crespin-histoire-des-martyrs.a1, H1: C, H2: C, H3: C, H4: N, note: "« le sieur de Tilladet & autres Capitaines » pour chefs : sans prénom, et d'autres capitaines présents."}
  - {preuve: lestrade-1900.a12, H1: N, H2: N, H3: N, H4: C, note: "Le rôle nomme aussi les capitaines Alexandre et Ampela : seul appui, faible, de H4."}
  - {preuve: lestrade-1900.a16, H1: C, H2: I, H3: C, H4: N, note: "Lestrade (secondaire) range « Tilladet de Saint-Orens » parmi les capitaines passés en Comminges en 1567 (liste qui peut inclure l'automne)."}
  - {preuve: bardies-1903.a11, H1: C, H2: I, H3: N, H4: N, note: "Bardies appelle le commandant « Tilladet de Saint-Orens » ; il recense Lestrade, donc probablement dépendant de lui."}
  - {preuve: site-roquemaurel.a24, H1: I, H2: C, H3: C, H4: N, note: "Note 34 du site : Antoine, d'après le résumé de carrière de La Chenaye, qui confond les deux frères ; poids faible."}
  - {preuve: monluc-lettres-ruble.a21, H1: C, H2: N, H3: N, H4: N, note: "9 oct. 1567 : « Tilladet de Saint-Orens, colonel des légions de Guyenne » ; François porte bien le nom de Tilladet et commande les gens de pied de la légion en 1567."}
  - {preuve: monluc-commentaires-ruble.a19, H1: C, H2: N, H3: N, H4: N, note: "Octobre 1567 : Saint-Orens « collonnel des légionnaires »."}
  - {preuve: brantome-lalanne.a1, H1: C, H2: N, H3: N, H4: N, note: "Brantôme : « Thilladet le jeune, qu'on nommoit M. de Sainct-Torains », colonel des légionnaires (fin 1567)."}
  - {preuve: monluc-lettres-ruble.a20, H1: C, H2: N, H3: N, H4: N, note: "5 juin 1566 : le « cappitaine Tilladet » porteur parle pour « les capitaines de sa légion » ; indice faible en faveur du colonel François (l'index de Ruble dit Antoine)."}
  - {preuve: monluc-lettres-ruble.a24, H1: C, H2: N, H3: N, H4: N, note: "3 févr. 1569 : c'est « le cappitaine Tilladet le jeune » qui mène quinze enseignes de gens de pied ; dans l'usage de Monluc, le Tilladet des gens de pied est le cadet."}
  - {preuve: monluc-lettres-ruble.a26, H1: N, H2: N, H3: N, H4: N, note: "Même lettre : « Tilladet l'aisné » demande une compagnie de gens d'armes ; montre que Monluc distingue les frères, sans rien dire de 1567. Non diagnostique."}
  - {preuve: noulens-1863.a5, H1: N, H2: N, H3: N, H4: N, note: "8 avril 1567 : Antoine et François présents au même contrat ; deux hommes distincts et vivants, lieu non précisé. Non diagnostique."}
contestations: []
meneur: H1
confiance: probable
verdict: "François de Cassagnet, seigneur de Saint-Orens, est très probablement le « capitaine Tilladet » de 1567 : la seule pièce contemporaine qui donne un nom (la requête des villes du Comminges) le désigne comme colonel de la légion de Guyenne conduisant les compagnies. L'attribution à Antoine ne repose que sur le site familial, qui recopie La Chenaye. Une seule pièce explicite, non revue sur l'original : la confiance reste « probable »."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## La question

Le nom « Tilladet » désigne au XVIe siècle deux frères Cassagnet : Antoine, l'aîné, seigneur de Tilladet et de Caussens,
et François, le cadet, seigneur de Saint-Orens, que Monluc appelle aussi « Tilladet le jeune »
([[monluc-commentaires-ruble.a14]], [[monluc-commentaires-ruble.a18]], [[monluc-lettres-ruble.a24]],
[[monluc-lettres-ruble.a26]]). Les deux sont vivants et distincts le 8 avril 1567 ([[noulens-1863.a5]],
[[noulens-1863.a6]]). Les récits de l'expédition de 1567 en Couserans ne donnent pas de prénom
([[monluc-lettres-ruble.a14]], [[discours-des-troubles-de-pamiers.a2]], [[crespin-histoire-des-martyrs.a1]],
[[lestrade-1900.a8]]).

## Pour H1 (François, Saint-Orens)

- La requête au roi des villes du Comminges, signée par le syndic Pontic, est la seule pièce de 1567 qui nomme le chef :
  Monluc fit mener les compagnies à Saint-Girons et Saint-Lizier « par le seigneur de Sainct Orens, colonel de la légion
  de Guienne » ([[lestrade-1900.a2]], réimprimée dans [[revue-de-comminges-t10.a1]]).
- François est bien appelé « Tilladet » quand il commande les gens de pied de la légion en 1567
  ([[monluc-lettres-ruble.a21]], [[monluc-commentaires-ruble.a19]], [[brantome-lalanne.a1]]).
- En 1569, quand Monluc distingue les frères, le Tilladet qui mène les enseignes de gens de pied est « le jeune »
  ([[monluc-lettres-ruble.a24]]). C'est une analogie, pas une preuve pour 1567.
- Lestrade et Bardies disent « Tilladet de Saint-Orens » ([[lestrade-1900.a16]], [[bardies-1903.a11]]), mais ce sont
  des lectures de la même requête et ils ne comptent guère comme preuves indépendantes.

## Pour H2 (Antoine)

Seule la note 34 du site familial ([[site-roquemaurel.a24]]) nomme Antoine. Elle reprend le résumé de carrière de La
Chenaye-Desbois, qui confond les deux frères (Verrue, Bordeaux et Mont-de-Marsan vont à Antoine, la légion à François).
Son poids est faible.

## H3 et H4

Rien n'atteste deux chefs successifs du nom de Tilladet (H3). L'ordonnance du 11 juillet 1567 ne connaît qu'un seul
« cappitaine Tilhadet », dont le « partement » clôt la période de dépense ([[lestrade-1900.a8]]) ; c'est plutôt contre
H3. Le seul appui de H3 est la note du site qui nomme Antoine ([[site-roquemaurel.a24]]). D'autres capitaines sont nommés (Alexandre, Ampela :
[[lestrade-1900.a12]]), mais toutes les pièces font de Tilladet le chef. H4 est donc improbable.

## Ce qui trancherait

Ce qui trancherait : l'original de la requête et les pièces de dépense conservés à Muret (P1, P4), et la commission de
l'expédition, non publiée par Ruble (P2). Sous H2, on devrait trouver « Tilladet l'aisné » ou le titre de Caussens dans
une pièce de mai-juin 1567 (P3). La question des Cabannes ([[tilladet-aux-cabannes]]) dépend de celle-ci.
