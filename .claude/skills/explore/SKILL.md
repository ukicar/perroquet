---
name: explore
description: Explorer librement les sources autour d'une personne, d'une famille, d'un lieu ou d'un événement, enrichir sa fiche et proposer des questions à partir des trous et des contradictions.
argument-hint: <id de fiche ou nom>
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/explore.md : ne pas modifier ici, modifier methode/commandes/explore.md. -->

# /explore : explorer autour d'une personne, d'un lieu, d'un événement

Sujet : **$ARGUMENTS**.

1. **Trouver ou créer la fiche.** `grep -ril "<nom>" base/` ; si rien, crée-la (procédure `methode/procedures/fiche.md`) (le type
   se déduit : personne, famille, lieu, evenement, institution). Vérifie les doublons possibles (variantes de
   graphie) avant de créer.
2. **Faire le point.** Lis la fiche, ses relations, les assertions qui la mentionnent
   (`grep -rn "<id>" base/sources`), les questions qui la concernent. Dresse pour toi la liste : ce qui est
   établi, ce qui est supposé, ce qui manque (dates, parents, conjoint, biens, confession, mort, actes).
3. **Chercher** (rôle `archiviste`) : plein texte Gallica et archive.org sur les variantes du nom, les éditions
   déjà connues (`./pq search gallica-texte <ark> …`, `archive-texte <id> …`), puis les pistes nouvelles.
   Toutes les recherches sont consignées (`--objet "…"`).
4. **Verser** (rôle `critique-des-sources`) les documents pertinents : fiches source, assertions verbatim,
   nouvelles fiches et relations justifiées.
5. **Rédiger la synthèse** de la fiche (corps, en français) : chaque phrase de fond renvoie à `[[source.aN]]`.
   Mets à jour `periode`, `naissance`, `mort`, `variantes` d'après les assertions.
6. **Proposer des questions.** Pour chaque contradiction entre sources ou chaque trou important, propose une
   question avec ses hypothèses (ne la crée que si l'utilisateur l'accepte, ou si elle est indispensable à la
   cohérence de la base).
7. `./pq check`, `./pq build`. Réponds : ce qui a été ajouté (sources, assertions, fiches), ce qui reste
   inconnu, les questions proposées avec la commande `/hypothesis "…"` prête à copier.
