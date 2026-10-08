---
name: sync
description: Synchroniser la base avec GitHub — valider, enregistrer (commit), récupérer les changements de l'autre chercheur, envoyer.
argument-hint: '[message]'
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/sync.md : ne pas modifier ici, modifier methode/commandes/sync.md. -->

# /sync : partager le travail

1. `./pq sync -m "$ARGUMENTS"` (sans message, un résumé automatique est utilisé). La commande valide la base,
   fait le commit, `git pull --rebase`, puis `git push`.
2. En cas d'erreurs de validation : corrige-les (procédure `/audit`), puis relance.
3. En cas de conflit de fusion : `git status`, ouvre les fichiers en conflit. Ce sont des fiches YAML : garde
   **les deux** apports (assertions, lignes de matrice, contestations, historique), renumérote les ids en
   double (`a7` → `a8`), puis `git add`, `git rebase --continue`, `./pq check`, `git push`. N'écrase jamais le
   travail de l'autre personne.
4. `./pq build`. Réponds : ce qui a été envoyé, ce qui a été reçu (`git log --oneline -10`).
