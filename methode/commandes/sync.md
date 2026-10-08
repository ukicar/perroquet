---
description: Partager le travail — valider, enregistrer, récupérer le travail de l'autre personne, envoyer sur GitHub, régénérer le site et mettre à jour le lien partagé.
argument: "[message]"
---
# /sync : partager le travail

1. `./pq sync -m "$ARGUMENTS"` (sans message, un résumé automatique est utilisé). La commande valide la base,
   fait le commit, `git pull --rebase`, puis `git push`.
2. En cas d'erreurs de validation : corrige-les (voir `/next`, étape 1), puis relance.
3. En cas de conflit de fusion : `git status`, ouvre les fichiers en conflit. Ce sont des fiches YAML : garde
   **les deux** apports (assertions, lignes de matrice, contestations, historique), renumérote les ids en
   double (`a7` → `a8`), puis `git add`, `git rebase --continue`, `./pq check`, `git push`. N'écrase jamais le
   travail de l'autre personne.
4. `./pq build`. Si ton outil sait publier un Artifact claude.ai, mets aussi à jour le lien partagé
   (`methode/procedures/publier.md`) ; sinon ignore cette étape.
5. Réponds : ce qui a été envoyé, ce qui a été reçu (`git log --oneline -10`).
