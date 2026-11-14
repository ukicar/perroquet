---
id: r-2026-10-26-archive-plein-texte-noms-du-dossier
type: recherche
nom: "archive.org, plein texte de tous les livres : noms du dossier (Roquemaurel, Soueix, Espinas, Soulan…)"
date: '2026-10-26'
auteur: ukicar
outil: archive-plein-texte (./pq search archive-plein-texte ; moteur plein texte d'archive.org)
requete: '"Roquemaurel" "Soueix" | "Roquemaurel" "Soulan" | "Gabrielle d''Espinas" | "Gabrielle Despinas" | "Espinas" "Lézat" | "Espinas" "Caladroy" | "Espinas" "Caladrue" | "Espinas" "Cardonne" | "Soueix" "1567" | "Mauléon" "Soueix" | "Roquemaurel" "Couserans" "1567" | "Despinas" "Roquemaurel" | "veuve de Roquemaurel" | "Arnaud de Roquemaurel" | "Soulan" "Espinas" | "sieur de Soulan" "1567" | "Roquemaurel" "Monluc" | "Espinas" "Rochefort" "Lézat" | "Espinas" "Galauba" | "Montesquieu" "Caladrue" | "Canals" "Lastronques" "Espinas" | "Pontic" "Roquemaurel"'
perimetre: "texte (couche OCR existante) de tous les livres d'archive.org ; tous les termes requis ; seuls les livres absents de la base ont été examinés"
resultat: negatif
resultats:
- titre: "Lestrade, Les Huguenots en Comminges (1900) : « Fontraille, Solan et Roquemaurel » en 1567 ; déjà dans la base"
  url: https://archive.org/details/leshuguenotsenco00lest
- titre: "Brémond, Nobiliaire toulousain (1863) : « Despinas ou Espinas (Gabriel et Jean-Auguste), sieur de Cardonne » ; déjà dans la base"
  url: https://archive.org/details/nobiliairetoulo00brgoog
- titre: "Inventaire sommaire des archives de l'Ariège (1894) : actes des Roquemaurel, coseigneurs de Soueix (XVIIIe s.)"
  url: https://archive.org/details/inventairesomm01arch
sources_creees: []
hypotheses: [origine-de-gabrielle, arbitrage-d-agen]
---
Premier essai de la recherche plein texte sur l'ensemble d'archive.org : elle trouve un livre même quand son titre ne
dit rien du sujet. Coût faible : on ne lit que de courts extraits, et le texte d'un livre n'est téléchargé dans
`cache/texte/` que s'il mérite un examen.

**Résultat.** Rien de nouveau sur Gabrielle d'Espinas. « Gabrielle d'Espinas » ne sort que dans la généalogie de
Jacques de Roquemaurel ([[roquemaurel-familles-du-midi]]) ; « veuve de Roquemaurel » et « Gabrielle Despinas » : 0.
« Espinas » + « Caladrue » ou « Montesquieu » + « Caladrue » : seulement cette même généalogie. Les livres pertinents
qui sortent sont déjà dans la base : Lestrade (1900), Brémond (1863), les *Commentaires* de Monluc (éd. de Ruble),
les *Mémoires et poésies de Jeanne d'Albret* (éd. de Ruble, 1893), la *Revue de Comminges*. Le reste est du bruit :
homonymes (Alfred et Georges Espinas, *espinas* « épines » en espagnol, Saint-Lary-Soulan), géologie de Soueix, guides,
presse moderne.

**Lestrade et l'arbitrage d'Agen.** Le texte d'archive.org de Lestrade (1900, première série) ne contient pas
l'arbitrage d'Agen du 7 septembre 1567 (recherche de « arbitr » : seulement des arbitrages de 1587-1596). La tâche
Gallica [[g-2026-10-08-lestrade-huguenots-en-comminges-nouvelle]] reste donc utile : elle vise la *nouvelle série*,
qui n'est pas sur archive.org.

**Suite.** Méthode abandonnée le jour même : fouiller tous les livres ramène surtout du bruit. On cherche
désormais dans une liste de livres choisis par thème, période et région (`corpus/livres.yaml`, `./pq search corpus`) :
voir [[r-2026-10-26-corpus-noms-du-dossier]].
