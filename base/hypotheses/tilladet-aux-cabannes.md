---
id: tilladet-aux-cabannes
type: hypothese
nom: Le Tilladet de la surprise des Cabannes
question: "Quel « Tilladet » conduisait les troupes qui surprirent les réfugiés de Pamiers aux Cabannes (25 ou 26 mai 1567), reçut le ministre Martin Tachard et le fit mener à Toulouse ?"
sujets: [francois-de-cassagnet-saint-orens, antoine-de-cassagnet-tilladet, famille-de-cassagnet, raid-des-cabannes-1567, martin-tachard, execution-de-martin-tachard]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "C'est François de Cassagnet, seigneur de Saint-Orens, le chef des compagnies de l'expédition de 1567, qui mena la même troupe aux Cabannes.", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "C'est Antoine de Cassagnet, seigneur de Tilladet, frère aîné de Saint-Orens.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "C'est un autre capitaine (un autre porteur du nom de Tilladet, ou un chef que les récits protestants appellent Tilladet par extension), ou la question est indéterminable.", auteur: agent, confiance: improbable}
predictions:
  - id: P1
    h: H1
    attendu: "La procédure du parlement de Toulouse contre Tachard (interrogatoire du 8 juin, arrêt du 7 (ou 6) juillet 1567) nomme le capitaine qui le livra « sieur de Saint-Orens », « Tilladet le jeune » ou « colonel des légionnaires »."
    ou_chercher: "AD Haute-Garonne, 1 B 3457, arrêts criminels de la Tournelle du 2 juin à juillet 1567 (catalogue-ad31.a2 ; voir r-2026-10-06-ad31-arret-du-24-mai-1567-lacunes) ; vérifier si le registre est numérisé."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Un récit ou un acte de mai-juin 1567 (Lafaille, Annales de Toulouse ; Histoire générale de Languedoc ; registres consulaires de Foix) nomme le chef « Tilladet l'aisné », « seigneur de Tilladet et de Caussens » ou Antoine."
    ou_chercher: "Lafaille, Annales de Toulouse, t. II, année 1567 ; Vic et Vaissète, Histoire générale de Languedoc, nouv. éd., t. XI-XII (Gallica)."
    diagnostique: haute
    statut: indecidable
    resultat: "Recherche du 7 octobre 2026 bloquée par la limitation de débit de Gallica (HTTP 429) : ni Lafaille ni l'HGL n'ont pu être lus. À relancer."
    preuves: [r-2026-10-07-gallica-lafaille-hgl]
    enquetes: []
  - id: P3
    h: H3
    attendu: "Le texte complet de Crespin ou du Discours de Pamiers, ou la procédure contre Tachard, désigne comme chef de l'entreprise un autre capitaine que Tilladet."
    ou_chercher: "Crespin, Histoire des martyrs, éd. Benoit, t. III, p. 648-649 (relecture complète) ; Archives curieuses, 1re s., t. VI, p. 341-343."
    diagnostique: moyenne
    statut: non_testee
    resultat: "8 oct. 2026 : Crespin relu en entier, éd. de 1570 et de 1619 : seul « le sieur de Tilladet & autres Capitaines » est nommé, et Tachard est amené à Tilladet (crespin-1570.a11, a13). Rien pour H3 de ce côté ; restent le Discours complet et la procédure."
    enquetes: []
matrice:
  - {preuve: discours-des-troubles-de-pamiers.a3, H1: C, H2: C, H3: I, note: "Les Cabannes furent attaquées par les mêmes troupes, « quand ils eurent exécuté leur commission » : le chef est celui de l'expédition (voir commandant-en-couserans-1567)."}
  - {preuve: lestrade-1900.a2, H1: C, H2: I, H3: I, note: "Le chef des compagnies de l'expédition est Saint-Orens ; combiné à la ligne précédente, cela désigne François. Inférence en deux temps."}
  - {preuve: discours-des-troubles-de-pamiers.a2, H1: C, H2: C, H3: I, note: "« sous la charge du capitaine Tilladet », sans prénom."}
  - {preuve: discours-des-troubles-de-pamiers.a8, H1: C, H2: C, H3: I, note: "« Tilladet le mena en triomphe par Foix », sans prénom."}
  - {preuve: crespin-1570.a11, H1: C, H2: C, H3: I, note: "1570 : « le sieur de Tilladet & autres Capitaines » chefs et conducteurs, sans prénom (1619 recopie)."}
  - {preuve: crespin-1570.a13, H1: C, H2: C, H3: I, note: "1570 : Tachard amené « audit Tilladet », sans prénom."}
  - {preuve: crespin-1570.a15, H1: C, H2: C, H3: I, note: "1570 : Tachard conduit à Toulouse « par le commādement dudit Tilladet » le 6 juin, sans prénom."}
  - {preuve: olhagaray-1629.a1, H1: C, H2: C, H3: I, note: "Prisonniers « menez au capitaine Tilladet », sans prénom."}
  - {preuve: castillon-histoire-du-comte-de-foix.a1, H1: N, H2: N, H3: N, note: "Cite Olhagaray : non indépendant, non compté."}
  - {preuve: benoit-1910.a1, H1: N, H2: N, H3: N, note: "Cite Olhagaray : non indépendant, non compté."}
  - {preuve: site-roquemaurel.a28, H1: C, H2: C, H3: I, note: "Girons de Roquemaurel aurait accompagné Tilladet aux Cabannes (site, sans source)."}
  - {preuve: site-roquemaurel.a24, H1: I, H2: C, H3: N, note: "La note 34 du site fait d'Antoine le capitaine Tilladet du Couserans (d'après La Chenaye, qui confond les frères)."}
  - {preuve: monluc-lettres-ruble.a24, H1: C, H2: N, H3: N, note: "En 1569 Monluc appelle « le cappitaine Tilladet le jeune » le chef de ses gens de pied ; c'est une analogie d'usage, pas une preuve pour 1567."}
  - {preuve: monluc-lettres-ruble.a26, H1: N, H2: N, H3: N, note: "« Tilladet l'aisné » (1569) : montre que les frères sont distingués quand il le faut ; rien sur 1567. Non diagnostique."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Le Tilladet des Cabannes est plausiblement François de Cassagnet, seigneur de Saint-Orens. Aucun récit ne donne son prénom ; on l'identifie en combinant le Discours de Pamiers (les mêmes troupes, une fois leur commission exécutée) et la requête des villes du Comminges, qui nomme Saint-Orens chef de l'expédition. La conclusion dépend donc de commandant-en-couserans-1567 et ne peut pas être plus forte qu'elle."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
  - {date: "2026-10-08", changement: "lignes Crespin rapportées à l'édition de 1570 ; P3 en partie examinée ; aucun changement de confiance", cause: "lecture de crespin-1570"}
sous_questions: [commandant-en-couserans-1567, date-du-raid-des-cabannes]
---
## La question

Les récits protestants de la surprise des Cabannes nomment toujours « Tilladet », jamais un prénom : le Discours des
troubles de Pamiers ([[discours-des-troubles-de-pamiers.a2]], [[discours-des-troubles-de-pamiers.a8]]), Crespin, dès
l'édition de 1570 ([[crespin-1570.a11]], [[crespin-1570.a13]], [[crespin-1570.a15]]) et
Olhagaray ([[olhagaray-1629.a1]]), que Castillon et Benoit recopient ([[castillon-histoire-du-comte-de-foix.a1]],
[[benoit-1910.a1]]). Toutes ces lignes sont compatibles avec les deux frères : elles ne départagent pas H1 et H2,
elles écartent seulement H3.

## Le raisonnement des notes (une inférence)

Le Discours de Pamiers dit que l'entreprise des Cabannes fut montée avec les troupes de l'expédition « quand ils eurent
exécuté leur commission » ([[discours-des-troubles-de-pamiers.a3]]). Or la requête des villes du Comminges nomme
Saint-Orens, colonel de la légion de Guyenne, comme chef de ces compagnies ([[lestrade-1900.a2]]). Si la même troupe
garde le même chef, le Tilladet des Cabannes est François. C'est une **inférence** des notes, raisonnable mais non
explicite : un autre chef aurait pu prendre la troupe après la « commission ». Elle hérite donc de toute l'incertitude de
[[commandant-en-couserans-1567]] et y ajoute la sienne.

## Contre

Seule la note 34 du site familial nomme Antoine ([[site-roquemaurel.a24]]), et elle traite du Couserans en général, pas
des Cabannes. La présence de Girons de Roquemaurel aux côtés de Tilladet ([[site-roquemaurel.a28]]) ne dit rien du
frère concerné.

## Ce qui trancherait

La procédure contre Tachard au parlement de Toulouse (P1) devrait nommer le capitaine qui l'a livré. Les annales
toulousaines (Lafaille) et l'Histoire générale de Languedoc (P2) n'ont pas pu être lues
([[r-2026-10-07-gallica-lafaille-hgl]]).
