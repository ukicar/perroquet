---
description: Tester une question historique. Recherches ciblées sur les prédictions, ajout des sources et assertions trouvées, consignation des recherches négatives, mise à jour de la matrice et du verdict, rédaction d'une enquête.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/test.md : ne pas modifier ici, modifier methode/commandes/test.md. -->

# /test : mettre les hypothèses à l'épreuve des sources

Arguments : **$ARGUMENTS** (id de la question, puis éventuellement les prédictions à tester).

Lis `AGENTS.md` si ce n'est pas fait. Lis la fiche `base/hypotheses/<id>.md` en entier.

## 1. Choisir quoi tester
- Si des prédictions sont données, teste celles-là. Sinon choisis 1 à 3 prédictions `non_testee`, en priorité
  `diagnostique: haute` et accessibles en ligne. Annonce ton choix en une ligne.
- Crée l'enquête : `./pq fiche enquete "<titre>"` puis renseigne `hypothese`, `predictions`,
  `verdict_avant` (meneur + confiance actuels).

## 2. Chercher (rôle archiviste)
Délègue à l'**archiviste** (`methode/roles/archiviste.md`) — sous-agent si ton outil le permet, sinon
applique toi-même sa fiche. Pour chaque prédiction :
1. Déduis les termes (variantes graphiques : Espinas, Despinas, d'Espinasse, Lespinasse… ; latin ; noms de
   lieux anciens) et les fonds.
2. Lance les recherches avec `./pq search … --hyp <id> --objet "<Pn : ce qu'on cherche>"`. Chaque recherche
   est consignée automatiquement dans `base/recherches/`. Complète le corps de chaque fiche recherche par
   une ligne d'interprétation.
3. Les recherches web générales sont permises en complément ; consigne-les toi-même (fiche `recherche`).
4. Si la seule voie est une salle de lecture ou un compte (Geneanet, AD non numérisées), note-le comme
   `resultat: bloque` et passe la prédiction en `indecidable` avec ce qu'il faudrait consulter.

## 3. Verser ce qui est trouvé (rôle critique des sources)
Pour chaque document pertinent trouvé, applique `methode/roles/critique-des-sources.md` :
- crée ou complète la fiche source (classification, `fichiers:` si tu télécharges un scan dans `cache/`) ;
- extrais les assertions **avec citation verbatim et locus**, lues par toi dans cette session ;
- crée les fiches nouvelles nécessaires (`./pq fiche`) et les relations justifiées.

## 4. Mettre à jour la question
- Pour chaque prédiction testée : `statut` (confirmee / infirmee / indecidable), `resultat` (1–2 phrases),
  `enquetes: [<id enquête>]`, `preuves: [...]`.
- Ajoute à la `matrice` une ligne par nouvelle preuve (assertion ou recherche négative), notée pour **toutes**
  les hypothèses.
- `./pq score <id>`. Mets à jour `meneur`, `confiance`, `verdict` **seulement** si les nouvelles preuves le
  justifient, et ajoute une ligne datée à `historique` avec la cause.
- Si l'enquête fait naître une nouvelle question, crée-la (procédure `/hypothesis`) et ajoute-la à
  `sous_questions`. Si elle suggère une nouvelle hypothèse concurrente, ajoute-la (`auteur: agent`).

## 5. Clore l'enquête
- Fiche enquête : `recherches`, `ajouts` (sources, assertions `source.aN`, fiches), `changements`,
  `verdict_apres`, et un court récit dans le corps.
- `./pq check` (0 erreur), `./pq build`.
- Réponds en 8–12 lignes : ce qui a été cherché, trouvé, pas trouvé ; l'effet sur chaque hypothèse ; le
  verdict ; la meilleure prochaine étape (souvent `/challenge <id>` ou une prédiction précise).
