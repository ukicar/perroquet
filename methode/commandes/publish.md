---
description: Publier le site de la base sur un lien privé claude.ai pour le partager (Claude seulement ; sinon chacun le génère localement).
---
# /publish : lien privé de partage

Cette commande dépend de Claude (outil Artifact). Dans un autre agent, explique que chacun peut générer le
site localement (`./pq view`) après `/sync`.

1. `./pq check` doit être sans erreur. Puis `./pq build --publish` (dossier `site_publish/`, ignoré par git).
2. Publie `site_publish/index.html` comme Artifact, avec **tous** les autres fichiers de `site_publish/` dans
   `files` (chemin publié = nom du fichier). Réutilise le même chemin de fichier à chaque fois pour garder le
   même lien. Premier publish : `icon: "network"`, description en une phrase.
3. Donne le lien à l'utilisateur ; il le partage lui-même.
