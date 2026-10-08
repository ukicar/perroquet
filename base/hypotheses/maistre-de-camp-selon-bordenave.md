---
id: maistre-de-camp-selon-bordenave
type: hypothese
nom: Tilladet maistre de camp selon Bordenave
question: "Pourquoi Bordenave appelle-t-il le Tilladet tué à Mont-de-Marsan en septembre 1569 (Antoine, selon son éditeur) « maistre de camp de l'infanterie de Monluc », alors que François (Saint-Orens) était le colonel des légionnaires en 1567 ?"
sujets: [antoine-de-cassagnet-tilladet, francois-de-cassagnet-saint-orens, escalade-de-mont-de-marsan-1569, legion-de-guyenne, blaise-de-monluc]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Le titre est exact : en 1569, après les changements de commandement de 1568, Antoine commandait effectivement l'infanterie de l'armée de Monluc.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Confusion : Bordenave donne au Tilladet tué la charge de son frère cadet, le maître de camp ou colonel des gens de pied.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Titre approximatif : Bordenave emploie « maistre de camp » au sens large de chef d'une troupe à pied lors de l'assaut, sans charge officielle.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Une montre, une commission ou une lettre de Monluc de 1569 (printemps-été) donne à Antoine (« Tilladet l'aisné », « sieur de Tilladet ») le commandement des gens de pied ou le titre de maître de camp."
    ou_chercher: "Monluc, Lettres, éd. Ruble, t. V, lettres de mars à septembre 1569 ; Commentaires, t. III, récit de 1569 avant Mont-de-Marsan ; BnF, montres de 1569 (fonds Clairambault, à localiser)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Dans les mois qui précèdent Mont-de-Marsan, les pièces nomment un autre chef des gens de pied (Saint-Orens, « Tilladet le jeune » ou le chevalier de Monluc), et les autres récits de l'escalade ne donnent pas ce titre au Tilladet tué."
    ou_chercher: "Ruble t. III, p. 300-320, et t. V (1569) ; d'Aubigné, Histoire universelle ; pièces fugitives d'Aubais (reconnaissance de Mont-de-Marsan, 18 sept. 1569, citée par Ruble)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Bordenave applique ailleurs « maistre de camp » à des capitaines qui n'avaient pas cette charge."
    ou_chercher: "Bordenave, Histoire de Béarn et Navarre, éd. P. Raymond (1873), Gallica bpt6k2063423 : relevé des emplois de « maistre de camp »."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: bordenave-raymond.a1, H1: C, H2: C, H3: C, note: "Le texte à expliquer : « Tilladet, maistre de camp de l'infanterie de Monluc » tué à l'entrée. Non diagnostique."}
  - {preuve: bordenave-raymond.a2, H1: C, H2: C, H3: C, note: "L'éditeur identifie Antoine, frère aîné de Saint-Orens. Non diagnostique."}
  - {preuve: monluc-commentaires-ruble.a24, H1: N, H2: C, H3: C, note: "Monluc : « monsieur de Tilladet », envoyé auprès de Damville, rallie à cheval les argoulets le long du fossé ; rien d'un chef de l'infanterie."}
  - {preuve: monluc-lettres-ruble.a24, H1: N, H2: C, H3: N, note: "3 févr. 1569 : « le cappitaine Tilladet le jeune » mène quinze enseignes de gens de pied ; c'est le cadet qui commande l'infanterie au début de 1569."}
  - {preuve: monluc-lettres-ruble.a26, H1: I, H2: C, H3: C, note: "Même lettre : Monluc demande pour « Tilladet l'aisné » une compagnie de gens d'armes, c'est-à-dire de cavalerie."}
  - {preuve: monluc-commentaires-ruble.a22, H1: C, H2: N, H3: C, note: "Note de Ruble : le chevalier de Monluc succède à Saint-Orens comme colonel des légionnaires en février 1568 ; la situation de 1567 ne vaut donc plus en 1569 (note peu sûre, crédibilité 4)."}
  - {preuve: monluc-commentaires-ruble.a23, H1: C, H2: N, H3: N, note: "1569 : Saint-Orens est à Libourne avec sa compagnie de gens d'armes ; il ne commande peut-être plus l'infanterie."}
  - {preuve: brantome-lalanne.a2, H1: N, H2: C, H3: N, note: "Brantôme (1567) : « le jeune Tilladet, maistre de camp des légionaires de Gascoigne » ; le titre est attaché au cadet."}
  - {preuve: brantome-lalanne.a3, H1: N, H2: C, H3: N, note: "Lalanne confond lui-même les frères (le maître de camp « tué devant Mont-de-Marsan ») : la confusion est facile."}
  - {preuve: bordenave-raymond.a4, H1: N, H2: C, H3: N, note: "L'éditeur de Bordenave se trompe sur l'année de la mort du frère (1568) : les Tilladet sont mal distingués autour de ce texte."}
contestations: []
meneur: H2
confiance: possible
verdict: "Indécis, avec un léger avantage pour la confusion des deux frères. En février 1569, Monluc confie les gens de pied à « Tilladet le jeune » et demande une compagnie de gens d'armes pour l'aîné. Dans son propre récit de Mont-de-Marsan, il montre Antoine à cheval avec les argoulets. Mais les commandements ont pu changer entre février et septembre 1569 : il faut les pièces de l'été 1569."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Le problème

Bordenave écrit que la garnison de Mont-de-Marsan fut massacrée « en despit de ce que Tilladet, maistre de camp de
l'infanterie de Monluc, avoit esté tué d'une harquebusade à l'entrée » ([[bordenave-raymond.a1]]). Son éditeur identifie
Antoine, frère aîné de Saint-Orens ([[bordenave-raymond.a2]]). Le Tilladet tué est bien l'aîné : Monluc le fait mourir
deux jours après sa blessure ([[monluc-commentaires-ruble.a24]]), et François vit encore en 1570 et au-delà
([[monluc-lettres-ruble.a28]]). Or le titre de maître de camp des légionnaires appartient à François en 1567
([[brantome-lalanne.a2]], [[brantome-lalanne.a1]], [[monluc-commentaires-ruble.a19]]).

## Pour H1 (titre exact en 1569)

Selon une note de Ruble, François n'est plus colonel des légionnaires à partir de février 1568
([[monluc-commentaires-ruble.a22]]), et il sert en 1569 avec sa compagnie de gens d'armes
([[monluc-commentaires-ruble.a23]]). Une redistribution des commandements en 1569 reste donc possible. C'est
l'hypothèse des notes, marquée comme incertaine.

## Pour H2 (confusion)

Au 3 février 1569, c'est « le cappitaine Tilladet le jeune » qui mène quinze enseignes de gens de pied
([[monluc-lettres-ruble.a24]]). Pour l'aîné, Monluc demande une compagnie de gens d'armes ([[monluc-lettres-ruble.a26]]).
À Mont-de-Marsan, Monluc montre Tilladet à cheval, ralliant les argoulets, pas à la tête de l'infanterie
([[monluc-commentaires-ruble.a24]]). Les érudits eux-mêmes confondent les frères à propos de ce titre
([[brantome-lalanne.a3]], [[bordenave-raymond.a4]]). Ces confusions modernes ne prouvent pas que Bordenave s'est trompé.

## H3

Rien dans la base n'indique comment Bordenave emploie ce titre ailleurs (P3).

## Ce qui trancherait

Les lettres et montres de l'été 1569 (P1, P2).
