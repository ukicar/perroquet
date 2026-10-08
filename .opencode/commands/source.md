---
description: Verser une source dans la base (lien Gallica, archive.org, archives, livre, référence, fichier local) — classification critique, extraction des assertions avec citations exactes, liens vers les fiches.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/source.md : ne pas modifier ici, modifier methode/commandes/source.md. -->

# /source : verser une source

Source : **$ARGUMENTS**. Applique le rôle `methode/roles/critique-des-sources.md`.

1. **Identifier.** Si c'est une source déjà dans la base (`ls base/sources`, `grep -ril`), complète-la ; sinon
   `./pq fiche source "<auteur, titre court (année)>"`.
2. **Obtenir le texte.**
   - Gallica : `./pq search gallica-texte <ark> <termes>` pour trouver les pages ; lis les pages utiles
     (texte OCR ou image IIIF `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<N>/full/full/0/native.jpg`).
   - archive.org : `./pq search archive-texte <identifiant> <termes>` (le texte OCR est mis en cache).
   - Fichier lourd (scan, PDF) : enregistre-le dans `cache/<dossier>/`, puis ajoute une entrée `fichiers:`
     (`chemin`, `url`, `sha256` via `./pq hash`, `recuperation: auto|manuel`, `note`). **Jamais hors de cache/.**
   - Manuscrit à lire : propose `/transcribe`.
3. **Classer** : genre, nature, fiabilite, consultee, auteur, date_redaction, distance, depot, cote, ark, url,
   biais, citee_par. Écris la critique de la source dans le corps (provenance, auteur, fiabilité, limites).
4. **Extraire les assertions** pertinentes pour Gabrielle et son entourage : une par fait, `texte` (français),
   `citation` verbatim recopiée de ce que tu as lu, `locus`, `sujets`, `date`, `preuve`, `information`,
   `credibilite`, `verifie: non`. Pas de citation reconstituée de mémoire.
5. **Relier** : crée les fiches manquantes, ajoute les relations justifiées par ces assertions. Si une
   assertion touche une question ouverte, ajoute la ligne de matrice correspondante et recalcule
   (`./pq score`), avec une ligne d'`historique` si le verdict bouge.
6. `./pq check`, `./pq build`. Réponds : la classification, le nombre d'assertions, les fiches et questions
   touchées.
