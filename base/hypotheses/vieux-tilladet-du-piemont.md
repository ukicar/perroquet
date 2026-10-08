---
id: vieux-tilladet-du-piemont
type: hypothese
nom: Le vieux Tilladet du Piémont
question: "Qui est « le vieux Tilladet » qui commande trente salades de la compagnie de M. de Termes en Piémont vers 1543-1544, alors que « le jeune Tilladet » (François, futur seigneur de Saint-Orens) sert dans la même campagne ?"
sujets: [antoine-de-cassagnet-tilladet, famille-de-cassagnet, marguerite-du-bouzet, bertrand-de-cassagnet, francois-de-cassagnet-saint-orens]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "C'est Antoine de Cassagnet, frère aîné de François : « vieux » oppose l'aîné au cadet (identification de l'index de Ruble).", auteur: humain, confiance: possible}
  - {id: H2, enonce: "C'est un Tilladet d'une génération antérieure : un fils (ou un parent) du premier mariage de Marguerite du Bouzet avec un seigneur de Tilladet, ou un oncle.", auteur: humain, confiance: possible}
  - {id: H3, enonce: "C'est un autre capitaine sans lien établi avec les Cassagnet (surnom, homonyme), ou la question est indéterminable.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Une montre de la compagnie de M. de Termes (années 1540) ou un acte de la même époque nomme « Antoine de Cassagnet, sieur de Tilladet » parmi les hommes d'armes ou chefs de salades."
    ou_chercher: "BnF, fonds Clairambault (montres et revues) et Pièces originales « Cassagnet » / « Tilladet » (Cabinet des titres), à localiser."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Les généalogies du Bouzet ou des seigneurs de Tilladet attestent un fils du premier mariage de Marguerite du Bouzet (un « de Tilladet » demi-frère d'Antoine et de François), vivant vers 1543."
    ou_chercher: "Noulens, Maisons historiques de Gascogne (1863), p. 24-26, texte complet (Gallica bpt6k5406179j, vues 33-35) ; Dossiers bleus et Pièces originales « Tilladet » et « du Bouzet » ; AD Gers, notaires de Gondrin."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Après les années 1540, Monluc ne parle plus du « vieux Tilladet » (mort ou retiré), alors que le capitaine Tilladet que l'index identifie à Antoine continue de servir (1550, 1551-1552, Verrue 1555)."
    ou_chercher: "Monluc, Commentaires, éd. Ruble, t. I-III (OCR archive.org commentairesetle01monl… 03monl), recherche « vieux Tilladet »."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-commentaires-ruble.a3, H1: C, H2: C, H3: C, note: "« le vieux Tilladet », sans prénom : le texte même de la question, compatible avec tout."}
  - {preuve: monluc-commentaires-ruble.a1, H1: C, H2: C, H3: N, note: "« le jeune Tilladet qui à présent est seigneur de Sainct Orenx » sert dans la même campagne : « vieux » s'oppose à ce « jeune », que ce soit un frère aîné ou un parent plus âgé."}
  - {preuve: monluc-commentaires-ruble.a5, H1: C, H2: C, H3: N, note: "« le june Tilhadet » mène une troupe avec Mons : même opposition."}
  - {preuve: monluc-lettres-ruble.a26, H1: N, H2: C, H3: N, note: "En 1569 Monluc appelle Antoine « Tilladet l'aisné », pas « le vieux Tilladet » ; indice lexical faible contre H1."}
  - {preuve: noulens-1863.a3, H1: N, H2: C, H3: N, note: "Marguerite du Bouzet épousa d'abord un seigneur de Tilladet et tint la salle de Tilladet à la fin du XVe siècle : une branche Tilladet antérieure aux Cassagnet a existé."}
  - {preuve: la-chenaye-desbois.a11, H1: N, H2: N, H3: N, note: "Bernard, fils d'Antoine, né en 1555 : Antoine né probablement vers 1520 (inférence des notes), donc jeune vers 1543. Trop incertain pour noter."}
  - {preuve: monluc-commentaires-ruble.a15, H1: C, H2: N, H3: N, note: "Antoine gouverneur de Verrue en Piémont en 1555 (note de Ruble) : il sert bien en Piémont, ce qui rend possible sa présence dès les années 1540."}
  - {preuve: noulens-1863.a7, H1: C, H2: N, H3: N, note: "Même fait chez Noulens (Verrue, 1555)."}
  - {preuve: monluc-commentaires-ruble.a2, H1: I, H2: N, H3: N, note: "Ruble se trompe sur le jeune Tilladet du même épisode (il le nomme Bernard, né en 1555) : son index, seul appui de H1, n'est pas sûr pour cette campagne."}
contestations: []
meneur: H2
confiance: possible
verdict: "Question ouverte. Le calcul place H2 (un Tilladet d'une génération antérieure) très légèrement en tête, faute d'appui solide pour H1 ; l'écart est minime et rien ne permet vraiment de choisir entre Antoine, frère aîné du « jeune Tilladet », et un Tilladet d'une génération antérieure issu du premier mariage de Marguerite du Bouzet. L'identification à Antoine ne repose que sur l'index de Ruble, qui se trompe sur le jeune Tilladet du même passage. Les généalogies du Bouzet et de Tilladet (Noulens, Cabinet des titres) sont la piste principale."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Le texte

Dans le récit des guerres de Piémont, Monluc mentionne « le vieux Tilladet », qui commande trente salades de la
compagnie de M. de Termes ([[monluc-commentaires-ruble.a3]]). Dans la même campagne, il nomme « le jeune Tilladet qui à
présent est seigneur de Sainct Orenx » ([[monluc-commentaires-ruble.a1]], [[monluc-commentaires-ruble.a5]]). Le
qualificatif « vieux » distingue donc un second Tilladet, plus âgé que François.

## H1 : Antoine

L'index de Ruble range ce « vieux Tilladet » sous Antoine (indication des notes, non versée comme assertion). Antoine est
bien l'aîné, et il sert en Piémont, où il est gouverneur de Verrue en 1555 ([[monluc-commentaires-ruble.a15]],
[[noulens-1863.a7]]). Deux réserves :
- l'index de Ruble se trompe sur le « jeune Tilladet » du même passage, qu'il appelle Bernard
  ([[monluc-commentaires-ruble.a2]]) ;
- en 1569 Monluc dit « Tilladet l'aisné », pas « le vieux » ([[monluc-lettres-ruble.a26]]). L'indice est faible, car
  l'usage peut avoir changé en vingt-cinq ans.

## H2 : une génération antérieure

Marguerite du Bouzet épousa d'abord un seigneur de Tilladet, puis Bertrand de Cassagnet ([[noulens-1863.a3]]). Un fils
de ce premier lit, ou un parent de ce seigneur, aurait porté le nom de Tilladet et pu être capitaine dans les années
1540. Ce n'est qu'une possibilité : aucune source de la base ne nomme ce fils. Les notes calculent qu'Antoine naquit
avant 1523 (testament de sa mère) et eut un fils en 1555 ([[la-chenaye-desbois.a11]]). C'est une **inférence**, qui ne
permet pas de dire s'il était déjà « vieux » vers 1543.

## Ce qui trancherait

Une généalogie du Bouzet ou des Tilladet (P2), ou une montre des années 1540 (P1). Le test P3, sur l'OCR des
Commentaires, est faisable mais peu discriminant.
