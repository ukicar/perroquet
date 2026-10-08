---
id: gouverneur-de-bordeaux-1568
type: hypothese
nom: Gouverneur de Bordeaux en 1568
question: "Lequel des deux frères Cassagnet fut gouverneur (ou commandant) de Bordeaux de la fin de 1567 ou de 1568 jusqu'au 6 février 1569, veille de la réception de Charles de Montferrand ?"
sujets: [antoine-de-cassagnet-tilladet, francois-de-cassagnet-saint-orens, bordeaux, charles-de-montferrand, blaise-de-monluc]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Antoine de Cassagnet, seigneur de Tilladet (« Tilladet l'aisné »), fut gouverneur de Bordeaux jusqu'au 6 février 1569.", auteur: humain, confiance: probable}
  - {id: H2, enonce: "François de Cassagnet, seigneur de Saint-Orens (« Tilladet de Saint-Orens »), fut ce gouverneur, quittant pour cela le commandement des légionnaires en février 1568.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Les deux frères se sont succédé à Bordeaux (ou l'un fut gouverneur en titre, l'autre commandant sur place), ou un autre Tilladet.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "L'ordre royal du 7/8 février 1568 qui fait de Tilladet le gouverneur de Bordeaux le nomme « sieur de Tilladet » (et de Caussens), sans le titre de Saint-Orens."
    ou_chercher: "BnF, collection Harlay Saint-Germain, fr. 320 (vol. 320, 1, f. 244 et vol. 320, 5, f. 191), d'après Ruble III, 93 n. 2."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "La même pièce de février 1568 nomme le gouverneur « sieur de Saint-Orens » ou « Tilladet de Saint-Orens », colonel des légionnaires."
    ou_chercher: "BnF, coll. Harlay Saint-Germain, fr. 320 (vol. 320, 1, f. 244 et 320, 5, f. 191)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H1
    attendu: "Les registres secrets du parlement de Bordeaux et les délibérations de la jurade (1568-1569), sur les conflits du gouverneur avec les jurats, le maire et la cour, le nomment « sieur de Tilladet » et jamais « Saint-Orens »."
    ou_chercher: "Devienne, Histoire de Bordeaux, p. 152 et suiv. (d'après Ruble V, 131 n. 1 et 141 n. 1) ; registres secrets du parlement de Bordeaux (copies BnF ou AD Gironde) ; Archives municipales de Bordeaux."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Les mêmes registres montrent un changement de titulaire entre la fin de 1567 et février 1569 (Saint-Orens puis Tilladet, ou l'inverse)."
    ou_chercher: "Registres secrets du parlement de Bordeaux ; jurade de Bordeaux, 1567-1569."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: archives-historiques-gironde-chronique.a2, H1: C, H2: I, H3: C, note: "Chronique bordelaise : le 6 février 1569 « le sieur de Tilhiadet qui auparavant estoit gouverneur s'en alla ». Le titre de seigneurie est celui d'Antoine ; François est d'ordinaire « Saint-Orens »."}
  - {preuve: archives-historiques-gironde-chronique.a3, H1: C, H2: I, H3: N, note: "Note de l'éditeur : Antoine, nommé par Monluc en 1567, mort à Mont-de-Marsan en 1569."}
  - {preuve: archives-historiques-gironde-chronique.a4, H1: C, H2: N, H3: N, note: "Table chronologique du même volume (Antoine) : même éditeur que la note, non indépendante ; pas comptée contre H2."}
  - {preuve: monluc-commentaires-ruble.a16, H1: C, H2: I, H3: N, note: "Ruble III, 93 n. 2 : Tilladet gouverneur en 1568 par ordre du roi, dans la note qui identifie Antoine."}
  - {preuve: monluc-lettres-ruble.a27, H1: C, H2: I, H3: N, note: "Ruble V, 142 n. 1 : Antoine gouverneur de Bordeaux."}
  - {preuve: monluc-commentaires-ruble.a22, H1: I, H2: C, H3: C, note: "Ruble III, 176 n. 1 et 234 n. 2 : « Tilladet de Saint-Orens » gouverneur ; Ruble se contredit (crédibilité 4)."}
  - {preuve: monluc-lettres-ruble.a25, H1: C, H2: N, H3: C, note: "3 févr. 1569 : Monluc défend « monsieur de Tilladet », qui n'a pas su contenter tout le monde (le gouverneur en conflit avec Bordeaux)."}
  - {preuve: monluc-lettres-ruble.a24, H1: C, H2: I, H3: N, note: "Même lettre : « le cappitaine Tilladet le jeune » est en campagne entre Lot et Dordogne avec quinze enseignes, trois jours avant le départ du gouverneur."}
  - {preuve: monluc-lettres-ruble.a26, H1: C, H2: N, H3: N, note: "Même lettre : Monluc demande une compagnie de gens d'armes pour « Tilladet l'aisné », au moment où celui-ci perd Bordeaux (rapprochement d'agent)."}
  - {preuve: monluc-commentaires-ruble.a21, H1: C, H2: I, H3: N, note: "Novembre 1567 : Saint-Orens part de Limoges avec les gens de pied envoyés au roi ; il n'est pas à Bordeaux à la fin de 1567."}
  - {preuve: brantome-lalanne.a1, H1: C, H2: I, H3: N, note: "Fin 1567 : Saint-Orens, colonel des légionnaires, au combat de Champoly en Auvergne."}
  - {preuve: gaullieur-1884.a4, H1: N, H2: N, H3: N, note: "L'historien de Bordeaux fusionne les frères (« Antoine de Tilladet, sieur de Saint-Orens ») : montre la confusion de la littérature, sans valeur pour trancher."}
contestations: []
meneur: H1
confiance: probable
verdict: "Antoine de Cassagnet, seigneur de Tilladet, est probablement le gouverneur de Bordeaux remplacé par Montferrand en février 1569. La chronique bordelaise dit « sieur de Tilhiadet », et dans sa lettre du 3 février 1569 Monluc distingue l'aîné du cadet, qui est alors en campagne. Seules deux notes de Ruble, contredites par ses autres notes, nomment Saint-Orens. L'ordre royal de février 1568 (coll. Harlay) n'a pas été lu."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les preuves

La chronique bordelaise éditée dans les *Archives historiques de la Gironde* rapporte que Montferrand fut reçu
gouverneur le lundi 7 février 1569 ([[archives-historiques-gironde-chronique.a1]]) et que, la veille, « le sieur de
Tilhiadet qui auparavant estoit gouverneur s'en alla » ([[archives-historiques-gironde-chronique.a2]]). La chronique ne
donne pas de prénom. Mais « sieur de Tilladet » est le titre d'Antoine, seigneur de Tilladet et de Caussens ; François
est désigné par sa seigneurie de Saint-Orens ou par « Tilladet le jeune ». L'éditeur identifie Antoine
([[archives-historiques-gironde-chronique.a3]], [[archives-historiques-gironde-chronique.a4]]).

Dans sa lettre au roi du 3 février 1569, Monluc défend « monsieur de Tilladet » contre les plaintes
([[monluc-lettres-ruble.a25]]). Dans la même lettre, il envoie « le cappitaine Tilladet le jeune » entre Lot et
Dordogne ([[monluc-lettres-ruble.a24]]) et demande une compagnie de gens d'armes pour « Tilladet l'aisné »
([[monluc-lettres-ruble.a26]]). Les notes de recherche en concluent que le Tilladet défendu est l'aîné. C'est une
**inférence** : elle est cohérente, mais la lettre ne dit pas en toutes lettres que l'aîné était le gouverneur.

Fin 1567, François conduit les gens de pied de l'armée de secours de Limoges en Auvergne ([[monluc-commentaires-ruble.a21]],
[[brantome-lalanne.a1]]). Il est donc difficilement à Bordeaux à ce moment-là.

## Contre H1

Ruble se contredit. Ses notes III, 93 n. 2 et V, 142 n. 1 nomment Antoine ([[monluc-commentaires-ruble.a16]],
[[monluc-lettres-ruble.a27]]). Ses notes III, 176 n. 1 et 234 n. 2 font de « Tilladet de Saint-Orens » le gouverneur, à
qui le chevalier de Monluc aurait succédé comme colonel en février 1568 ([[monluc-commentaires-ruble.a22]]). Cette
seconde version expliquerait pourquoi François quitte le commandement de la légion en 1568, ce qui donne à H2 (et à H3)
une petite vraisemblance. Elle reste isolée.

## Meneur déclaré

Le calcul ACH place H3 (succession des deux frères, ou partage du commandement) devant H1, parce que cette hypothèse
composite ne contredit aucune pièce. Mais aucune pièce ne l'appuie en propre, hormis les notes contradictoires de Ruble
([[monluc-commentaires-ruble.a22]], poids faible). Toutes les pièces qui nomment un gouverneur ne connaissent qu'un seul
« sieur de Tilladet ». On retient donc H1, plus simple et appuyée par la chronique et par la lettre de Monluc ; H3 reste
« possible ».

## Ce qui trancherait

L'ordre royal du 8 février 1568 cité par Ruble (coll. Harlay Saint-Germain, fr. 320 : P1, P2) et les registres
bordelais sur les conflits du gouverneur (P3, P4).
