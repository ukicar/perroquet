---
description: Publier le site de la base sur un lien privé claude.ai pour le partager (Claude seulement ; sinon chacun le génère localement).
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/publish.md : ne pas modifier ici, modifier methode/commandes/publish.md. -->

# /publish : lien privé de partage

Cette commande dépend de Claude (outil Artifact). Dans un autre agent, explique que chacun peut générer le
site localement (`./pq view`) après `/sync`.

1. `./pq check` doit être sans erreur. Puis `./pq build --publish` (dossier `site_publish/`, ignoré par git).
2. Publie `site_publish/index.html` comme Artifact, avec **tous** les autres fichiers de `site_publish/` dans
   `files` (chemin publié = nom du fichier). Le lien existe déjà : **https://claude.ai/artifact/LSFjNo7rNK4Czatr2gqRqo**.
   Depuis une nouvelle conversation, lis-le d'abord (`action: read`) puis publie avec `url` égal à ce lien pour
   le mettre à jour au lieu d'en créer un autre. Seul son propriétaire, ou une personne à qui il a donné le
   droit de modifier (menu Partager), peut le mettre à jour.
3. Donne le lien à l'utilisateur ; il le partage lui-même.
