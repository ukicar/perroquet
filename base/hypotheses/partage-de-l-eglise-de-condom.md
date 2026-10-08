---
id: partage-de-l-eglise-de-condom
type: hypothese
nom: Partage de l'église de Condom en 1562
question: "Lequel des frères Cassagnet est le « capitaine Tilladet » qui, à Condom en 1562, partagea l'église entre catholiques (le chœur) et protestants (la nef) ?"
sujets: [antoine-de-cassagnet-tilladet, francois-de-cassagnet-saint-orens, condom, famille-de-cassagnet]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "C'est Antoine de Cassagnet, seigneur de Tilladet (note de Ruble III, 93 n. 2).", auteur: humain, confiance: possible}
  - {id: H2, enonce: "C'est François de Cassagnet, seigneur de Saint-Orens (index de l'édition Baum et Cunitz de Bèze).", auteur: humain, confiance: possible}
  - {id: H3, enonce: "Le texte de Bèze ne permet pas de choisir : les deux attributions sont des inférences d'éditeurs, ou il s'agit d'un autre capitaine.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H2
    attendu: "Le récit de Bèze sur Condom (1562) qualifie lui-même le capitaine de « sieur de Saint-Orens » ou de « jeune Tilladet »."
    ou_chercher: "Bèze, Histoire ecclésiastique, éd. Baum et Cunitz (Gallica), passage sur Condom en 1562, page donnée par l'index du t. III, art. « Tilladet » (Gallica bpt6k5728059b, vue 877)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "Les registres consulaires de Condom de 1562 nomment le capitaine qui commandait la ville « sieur de Tilladet » (et de Caussens), distinct de Saint-Orens."
    ou_chercher: "Registres consulaires de Condom, 1562 (AM Condom ou AD Gers ; Ruble III, 297 n. cite ces registres pour 1567)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Bèze n'écrit que « capitaine Tilladet » sans autre qualification : le titre de Saint-Orens de l'index serait alors une inférence des éditeurs, comme le prénom Antoine chez Ruble."
    ou_chercher: "Bèze, éd. Baum et Cunitz, même passage."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-commentaires-ruble.a17, H1: C, H2: I, H3: C, note: "Note de Ruble (d'après Bèze) : Antoine ; note d'éditeur, crédibilité 4."}
  - {preuve: beze-histoire-ecclesiastique.a1, H1: I, H2: C, H3: C, note: "Index Baum et Cunitz : « TILLADET, N. sieur de Saint-Orans, dit le capitaine » ; le « N. » montre que les éditeurs ignoraient le prénom : c'est aussi une identification d'éditeur."}
  - {preuve: monluc-commentaires-ruble.a8, H1: N, H2: C, H3: N, note: "Fin 1561, Monluc confie la première compagnie levée contre les huguenots au jeune Tilladet (Saint-Orens) : François commande dans l'Agenais-Condomois au début de 1562."}
  - {preuve: monluc-commentaires-ruble.a12, H1: N, H2: C, H3: N, note: "Astaffort, 1562 : le jeune Tilladet arrête les séditieux, non loin de Condom."}
  - {preuve: monluc-lettres-ruble.a19, H1: C, H2: C, H3: C, note: "Mars 1562 : un « cappitaine Tilladet » laissé à Fumel pour achever les procès (sans prénom ; l'index de Ruble dit Antoine) : non diagnostique."}
  - {preuve: gaullieur-1884.a3, H1: N, H2: N, H3: C, note: "Gaullieur donne à Antoine le « jeune Tilladet » de 1562 : les identifications de 1562 par les érudits sont peu sûres."}
contestations: []
meneur: H3
confiance: possible
verdict: "Indéterminable en l'état (H3), avec un léger avantage pour François (Saint-Orens) sur Antoine. Les deux attributions sont des inférences d'éditeurs : l'index de Bèze dit « sieur de Saint-Orans » mais ignore le prénom, et Ruble dit Antoine dans une note qui confond ailleurs les frères. On sait seulement que François commandait la compagnie de Monluc dans la région au début de 1562. Il faut lire le passage de Bèze lui-même."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les deux attributions

La note de Ruble sur Antoine (Commentaires III, 93 n. 2) lui attribue, d'après Bèze, le partage de l'église de Condom en
1562 entre catholiques et protestants ([[monluc-commentaires-ruble.a17]]). L'index de l'édition Baum et Cunitz de Bèze
range le même épisode sous « TILLADET, N. sieur de Saint-Orans, dit le capitaine »
([[beze-histoire-ecclesiastique.a1]]). Les deux éditeurs interprètent donc un même texte, et aucun des deux ne cite de
pièce donnant le prénom. Le « N. » de l'index montre que Baum et Cunitz ne connaissaient pas le prénom.

## Le contexte

Fin 1561, Monluc lève 200 arquebusiers et 100 argoulets et en donne la charge au « june Tilladet, qu'est aujourd'huy
monsieur de Sainct Orens » ([[monluc-commentaires-ruble.a8]]). Au début de 1562, ce jeune Tilladet opère autour d'Agen et
de Condom (Astaffort : [[monluc-commentaires-ruble.a12]]). C'est un léger appui pour H2. Un « cappitaine Tilladet »
sans prénom est aussi à Fumel en mars 1562 ([[monluc-lettres-ruble.a19]]) ; l'index de Ruble le donne à Antoine, sans
preuve dans le texte. Les érudits se sont souvent trompés sur les Tilladet de 1562 ([[gaullieur-1884.a3]]).

## Ce qui trancherait

Le passage même de Bèze (P1, P3) et les registres consulaires de Condom de 1562 (P2).
