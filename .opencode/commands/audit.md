---
description: Audit de méthode de la base — erreurs, preuves faibles, prédictions non testées, questions jamais contestées, fiches isolées — avec un plan d'action priorisé.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/audit.md : ne pas modifier ici, modifier methode/commandes/audit.md. -->

# /audit : où la preuve est-elle faible ?

Portée : **$ARGUMENTS** (vide = toute la base).

1. `./pq audit` et `./pq score`.
2. Corrige toi-même les **erreurs** (références cassées, valeurs hors vocabulaire) quand la correction est
   évidente et ne change aucun fait ; sinon explique-les.
3. Lis les avertissements et ajoute ta propre lecture critique :
   - verdicts plus forts que leurs preuves (confiance élevée sur assertions non vérifiées ou sources
     connues seulement par citation) ;
   - sources dépendantes présentées comme indépendantes (même informateur derrière deux publications) ;
   - assertions dont la citation semble paraphrasée ;
   - questions dont toutes les preuves sont non diagnostiques ;
   - meneur déclaré différent du meneur calculé.
4. Propose un **plan d'action** priorisé (5–10 lignes), chaque ligne avec la commande prête à copier
   (`/verify …`, `/test … P2`, `/challenge …`, `/research …`).
5. `./pq build`. Ne modifie aucun verdict dans cette commande.
