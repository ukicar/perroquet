---
description: Faire avancer une question historique. Choisit les prédictions les plus décisives (ou celles indiquées), cherche dans les sources, verse ce qu'on trouve, consigne ce qu'on ne trouve pas, met à jour la matrice et le verdict, puis fait contester le verdict s'il a changé.
argument: "<id de la question> [P1 P2…]"
---
# /test : mettre les hypothèses à l'épreuve des sources

Arguments : **$ARGUMENTS** (id de la question, puis éventuellement les prédictions à tester).

Lis `AGENTS.md` si ce n'est pas fait. Lis la fiche `base/hypotheses/<id>.md` en entier.

## 1. Choisir quoi tester
- Si des prédictions sont données, teste celles-là.
- Sinon choisis toi-même 1 à 3 prédictions `non_testee`, en priorité `diagnostique: haute` et accessibles en
  ligne. S'il n'y en a pas d'utile, écris d'abord les prédictions qui manquent (voir étape 3 de `/next`).
  Annonce ton choix en une ligne.
- Crée l'enquête : `./pq fiche enquete "<titre>"` puis renseigne `hypothese`, `predictions`,
  `verdict_avant` (meneur + confiance actuels).

## 2. Chercher (rôle archiviste)
Délègue à l'**archiviste** (`methode/roles/archiviste.md`), en sous-agent si ton outil le permet, sinon
applique toi-même sa fiche. Pour chaque prédiction :
1. Déduis les termes (variantes : Espinas, Despinas, d'Espinasse, Lespinasse… ; latin ; noms de lieux anciens)
   et les fonds.
2. Lance les recherches avec `./pq search … --hyp <id> --objet "<Pn : ce qu'on cherche>"`. Chaque recherche
   est consignée dans `base/recherches/` ; complète le corps de chaque fiche recherche d'une ligne d'interprétation.
3. Les recherches web générales sont permises en complément ; consigne-les toi-même (fiche `recherche`).
4. Si la seule voie est une salle de lecture ou un compte (Geneanet, archives non numérisées) : `resultat: bloque`,
   prédiction `indecidable`, et note précisément ce qu'il faudrait consulter : crée ou complète la démarche
   correspondante (`methode/procedures/demarche.md`), qui apparaîtra sur la page « À faire sur place ».

## 3. Verser ce qui est trouvé
Pour chaque document pertinent, suis la commande `/source` (classification, assertions verbatim avec locus,
fiches et relations justifiées). Un manuscrit à déchiffrer suit `methode/procedures/transcrire.md`.

## 4. Mettre à jour la question
- Pour chaque prédiction testée : `statut` (confirmee / infirmee / indecidable), `resultat` (1–2 phrases),
  `enquetes: [<id enquête>]`, `preuves: [...]`.
- Ajoute à la `matrice` une ligne par nouvelle preuve (assertion ou recherche négative), notée pour **toutes**
  les hypothèses.
- `./pq score <id>`. Mets à jour `meneur`, `confiance`, `verdict` **seulement** si les nouvelles preuves le
  justifient, avec une ligne datée dans `historique`.
- Nouvelle question née de l'enquête → crée-la (procédure `/hypothesis`) et ajoute-la à `sous_questions`.
  Nouvelle explication possible → ajoute une hypothèse concurrente (`auteur: agent`).

## 5. Contester si le verdict a bougé
Si le meneur ou la confiance a changé, applique la commande `/challenge` sur la question avant de conclure
(avocat du diable indépendant). Sinon, propose-la seulement.

## 6. Clore
- Fiche enquête : `recherches`, `ajouts` (sources, assertions `source.aN`, fiches), `changements`,
  `verdict_apres`, court récit dans le corps.
- Si un fait ou un verdict a changé, reprends la biographie de chaque personne touchée
  (`methode/procedures/biographie.md`).
- `./pq check` (0 erreur), `./pq build`.
- Réponds en 8–12 lignes : ce qui a été cherché, trouvé, pas trouvé ; l'effet sur chaque hypothèse ; le verdict ;
  la meilleure prochaine étape.

**Propagation (obligatoire avant de répondre)** : `./pq impact` sur ce qui a été ajouté ou modifié, puis mise à jour de chaque fichier listé (`methode/procedures/propager.md`).
