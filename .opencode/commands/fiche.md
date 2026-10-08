---
description: Créer une fiche (personne, famille, lieu, événement, institution) et la relier aux fiches existantes, preuves à l'appui.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/fiche.md : ne pas modifier ici, modifier methode/commandes/fiche.md. -->

# /fiche : créer une fiche et la relier

Demande : **$ARGUMENTS**.

1. Vérifie qu'elle n'existe pas sous une autre graphie (`grep -ril` sur le nom et ses variantes). Si elle
   existe, propose de la compléter au lieu d'en créer une.
2. `./pq fiche <type> "<nom>"`, puis remplis : `variantes`, dates (`naissance`, `mort`, `periode`, ou `date`/`fin`
   pour un événement), `coordonnees` d'un lieu seulement si elles sont sûres.
3. Cherche dans la base les assertions qui la concernent (`grep -rn` sur le nom et les variantes dans
   `base/sources`) : ajoute l'id de la fiche à leurs `sujets`.
4. Ajoute les relations justifiées (`rel`, `vers`, `preuves` ou `hypothese`, `confiance`) — vocabulaire dans
   `schema/relations.yaml`. Une relation sans preuve ni hypothèse est refusée.
5. Écris une synthèse courte avec liens. Si l'utilisateur a fourni des informations sans source, ne les
   affirme pas : note-les comme pistes dans la synthèse (« à vérifier ») ou propose `/hypothesis`.
6. `./pq check`, `./pq build`. Réponds avec la fiche créée, ses liens, et les manques.
