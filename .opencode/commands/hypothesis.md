---
description: Proposer une hypothèse historique. Crée la question, garde l'hypothèse de l'utilisateur, ajoute les hypothèses concurrentes, écrit les prédictions testables et remplit la matrice avec les preuves déjà dans la base.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/hypothesis.md : ne pas modifier ici, modifier methode/commandes/hypothesis.md. -->

# /hypothesis : poser une question et ses hypothèses concurrentes

Hypothèse proposée par l'utilisateur : **$ARGUMENTS**

Lis d'abord `AGENTS.md` (règles absolues et format) si ce n'est pas déjà fait dans cette session.

## 1. Comprendre et situer
1. Reformule l'hypothèse en une phrase précise et testable. Si elle est ambiguë au point de changer la
   recherche (quelle personne ? quelle période ?), pose **une** question à l'utilisateur, sinon avance.
2. Cherche si la question existe déjà : `ls base/hypotheses/`, `grep -ril "<mots clés>" base/hypotheses`.
   - Si une question existante couvre le sujet, **ajoute** l'hypothèse comme nouvelle `Hn` dans cette fiche
     (avec `auteur: humain`) au lieu de créer un doublon, puis passe à l'étape 4.
3. Repère les fiches concernées (personnes, lieux, événements) : `grep -ril` dans `base/`. S'il manque une
   fiche indispensable, crée-la avec `./pq fiche <type> "<nom>"`.

## 2. Créer la question
`./pq fiche hypothese "<titre court de la question>"` puis remplis l'en-tête (voir AGENTS.md, section
« Question et hypothèses ») :
- `question` : la question à laquelle l'hypothèse répond.
- `sujets` : les ids des fiches concernées.
- `hypotheses` : H1 = celle de l'utilisateur (`auteur: humain`), puis **au moins une concurrente** sérieuse
  (`auteur: agent`), et si utile une hypothèse « autre / indéterminable ». Les hypothèses doivent s'exclure
  autant que possible. Confiance initiale de chacune : `possible`, sauf preuve déjà connue.
- `statut: ouverte`, `historique: [{date: <aujourd'hui>, changement: "création", cause: "proposée par l'utilisateur"}]`.

## 3. Écrire les prédictions
Pour **chaque** hypothèse, 1 à 3 prédictions : ce qu'on devrait trouver si elle est vraie, et où. Une bonne
prédiction est :
- **observable** dans une source identifiable (fonds, cote, édition, ark, type d'acte) ;
- **diagnostique** : son résultat ne serait pas le même sous les autres hypothèses (`diagnostique: haute`) ;
- réaliste : accessible en ligne, ou alors signalée comme salle de lecture dans `ou_chercher` ; dans ce cas,
  note aussi la démarche (`methode/procedures/demarche.md`) pour qu'elle figure sur la page « À faire sur place ».
Pense aussi aux prédictions **négatives** (« si H2, on ne devrait jamais trouver … »).
Ids : P1, P2… ; `statut: non_testee`.

## 4. Remplir la matrice avec ce qu'on sait déjà
1. Cherche les assertions pertinentes : `grep -rn "<mots>" base/sources`, lis les fiches des sujets.
2. Pour chaque assertion utile, ajoute une ligne `{preuve: <source-id.aN>, H1: …, H2: …, note: …}`.
   Note chaque cellule honnêtement ; si la preuve est compatible avec tout, c'est `C` partout (non diagnostique).
3. Ajoute aussi les recherches négatives déjà consignées (`base/recherches/`) quand elles comptent.
4. `./pq score <id>` : le meneur est celui qui a le moins d'incohérence. Écris `meneur`, `confiance`
   (prudente : jamais `etabli` sans preuve directe vérifiée) et un `verdict` de 2–3 phrases.

## 5. Raisonnement et relations
- Corps de la fiche : en français, le raisonnement (ce qui pèse pour et contre chaque hypothèse), avec liens
  `[[source.aN]]`.
- Si l'hypothèse implique une relation (ex. « membre de telle famille »), ajoute-la dans la fiche du sujet
  avec `hypothese: <question-id>#H1` et la confiance de H1. Elle apparaîtra en pointillé dans le graphe.

## 6. Clore
1. `./pq check` (0 erreur) puis `./pq build`.
2. Réponds à l'utilisateur en 6–10 lignes : la question, les hypothèses, laquelle mène et pourquoi, les 2–3
   prédictions les plus diagnostiques, et la commande suivante conseillée (`/test <id> P…`).
