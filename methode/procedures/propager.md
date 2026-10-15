<!-- Procédure interne : utilisée par les commandes, pas une commande en soi. -->
# Procédure : propager un changement dans toute la base

Une trouvaille ne vaut que si **tout ce qui en dépend** est mis à jour dans le même passage. Une fiche, une synthèse
ou une biographie qui dit encore ce que la base ne soutient plus rend le travail inutilisable.

Quand : à la fin de toute commande qui ajoute ou modifie une source, une assertion, une relation ou un verdict
(`/test`, `/source`, `/explore`, `/challenge`, `/verify`, `/sync-gallica`, versement d'un rapport d'agent).

1. `./pq impact <ids>` avec les sources, assertions (`source.a7`) et questions ajoutées ou modifiées ; ou
   `./pq impact` pour tout ce qui a changé depuis le dernier commit. La commande liste les fichiers qui citent
   ces éléments et les fiches (avec leur biographie) des personnes, familles, lieux et événements qu'ils nomment.
2. Pour **chaque** fichier listé :
   - fiche (personne, famille, lieu, événement, institution) : relations (nouvelles preuves, confiance), dates
     (`naissance`, `mort`, `periode`), et **synthèse réécrite** si son fil change (une hypothèse qui passe en tête
     se met en tête du texte ; on ne se contente pas d'ajouter une phrase à la fin) ;
   - biographie : même exigence (procédure `biographie.md`), `mise_a_jour` du jour ;
   - question : matrice, `verdict`, `meneur`, `confiance`, corps, `historique` ;
   - démarche : `pour`, `action`, statut.
   Un fichier qu'il n'y a pas lieu de changer est laissé tel quel, mais il a été relu.
3. `./pq check` (0 erreur), `./pq build`. Dans la réponse à l'utilisateur, dire quels fichiers ont été mis à jour.
