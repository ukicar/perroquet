---
description: Verser un document que vous avez trouvé (lien Gallica, archive.org, archives, livre, référence, scan ou fichier local) — classement critique, faits extraits avec citations exactes, transcription si c'est un manuscrit, liens vers les fiches et les questions.
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
   - Fichier lourd (scan, PDF) : suis `methode/procedures/fichiers-lourds.md` (dans `cache/`, jamais dans git).
   - Manuscrit ou registre à déchiffrer : suis `methode/procedures/transcrire.md` (double lecture).
3. **Classer** : genre, nature, fiabilite, consultee, auteur, date_redaction, distance, depot, cote, ark, url,
   biais, citee_par. Écris la critique de la source dans le corps (provenance, auteur, fiabilité, limites).
4. **Extraire les assertions** pertinentes pour Gabrielle et son entourage : une par fait, `texte` (français),
   `citation` verbatim recopiée de ce que tu as lu, `locus`, `sujets`, `date`, `preuve`, `information`,
   `credibilite`, `verifie: non`. Pas de citation reconstituée de mémoire.
5. **Relier** : crée les fiches manquantes et les relations justifiées (procédures `methode/procedures/fiche.md`
   et `relier.md`). Si une
   assertion touche une question ouverte, ajoute la ligne de matrice correspondante et recalcule
   (`./pq score`), avec une ligne d'`historique` si le verdict bouge.
6. Reprends la biographie de chaque personne dont un fait a changé (`methode/procedures/biographie.md`).
7. `./pq check`, `./pq build`. Réponds : la classification, le nombre d'assertions, les fiches et questions
   touchées.

**Propagation (obligatoire avant de répondre)** : `./pq impact` sur ce qui a été ajouté ou modifié, puis mise à jour de chaque fichier listé (`methode/procedures/propager.md`).
