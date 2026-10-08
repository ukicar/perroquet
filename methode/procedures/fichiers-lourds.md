<!-- Procédure interne : utilisée par les commandes, pas une commande en soi. -->
# Procédure : fichiers lourds (scans, PDF)

Les scans et PDF ne vont **jamais** dans git : ils vivent dans `cache/`, propre à chaque machine.

## Enregistrer un nouveau fichier
1. Télécharge-le dans `cache/<dossier parlant>/<nom parlant>` (ex. `cache/AD31_1B74/fol198r.jpg`).
2. Ajoute une entrée dans la fiche source, sous `fichiers:` :
   `{chemin: cache/…, url: <adresse directe de téléchargement ou page d'origine>, sha256: <./pq hash cache/…>, recuperation: auto|manuel, note: <comment l'obtenir>}`.
   `auto` seulement si `url` télécharge directement le fichier (ex. image IIIF Gallica
   `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<N>/full/full/0/native.jpg`).

## Récupérer ce qui manque sur cette machine
`./pq fetch --status` pour voir ce qui manque, `./pq fetch [id de source]` pour télécharger. Pour les fichiers
`manuel`, explique où et comment les obtenir d'après leur note. Si un serveur refuse (Gallica limite parfois les
téléchargements), réessayer plus tard.
