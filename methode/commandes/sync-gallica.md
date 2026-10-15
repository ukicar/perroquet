---
description: Reprendre le travail en attente de Gallica — quand Gallica débloque, relancer les recherches mises en attente, faire les lectures de pages notées, verser ce qui est trouvé et mettre à jour les questions.
argument: "[id de tâche ou de question, facultatif]"
---
# /sync-gallica : reprendre le travail en attente de Gallica

Gallica bloque souvent nos requêtes (HTTP 403 ou 429) quand on en envoie trop. Ce qui n'a pas pu être fait est
noté dans `base/gallica/` (une fiche par tâche, `statut: en_attente`) :
- les recherches `./pq search gallica…` refusées s'y mettent **d'elles-mêmes** ;
- les lectures de pages (une vue, un volume à parcourir) y sont notées par l'agent (`./pq fiche gallica "<nom>"`,
  champs `ark`, `vues`, `action`, `hyp`, `pour`).
Portée : **$ARGUMENTS** (vide = toutes les tâches en attente).

## 1. Gallica répond-il ?
`./pq gallica` : teste l'accès et liste les tâches. S'il répond encore « refuse », **arrête-toi** : dis-le à
l'utilisateur, avec le nombre de tâches en attente, et propose de réessayer plus tard (le blocage dure souvent
une à quelques heures). Ne martèle pas Gallica : c'est ce qui prolonge le blocage.

## 2. Les recherches automatiques
`./pq gallica --run` relance les recherches en attente, les consigne dans `base/recherches/` comme d'habitude et
marque les tâches `faite`. Complète le corps de chaque fiche recherche créée (interprétation, suite à donner),
comme après tout `./pq search`. Si Gallica bloque de nouveau en cours de route, la commande s'arrête : passe à
l'étape 5.

## 3. Les lectures (rôle `archiviste`, `paleographe` pour un manuscrit)
Pour chaque tâche `outil: lecture` en attente, par ordre de priorité (d'abord celles qui servent une prédiction
`diagnostique: haute`) :
- lis ce que demande `action` : `./pq search gallica-texte <ark> <termes…>` pour repérer les pages, puis
  `./pq bnf get_page_text '{"ark": "<ark>", "page": N}'` pour l'OCR d'une page, ou l'image IIIF pour un manuscrit ;
- **va doucement** : quelques secondes entre deux requêtes, pas plus d'une vingtaine de pages d'affilée ;
- verse ce qui est trouvé (rôle `critique-des-sources` : fiche source, assertions verbatim avec locus) et mets à
  jour les prédictions concernées (`pour`) comme dans `/test` (matrice, statut, `historique`) ;
- marque la tâche : `statut: faite`, `resultat` en une phrase, `recherche` (id de la fiche recherche s'il y en a
  une) et une ligne dans `tentatives`. Une lecture qui ne trouve rien est aussi `faite` : c'est une recherche
  négative, à consigner.
Si Gallica bloque de nouveau : ajoute une ligne `tentatives` (date, « refusée ») à la tâche en cours et arrête.

## 4. Questions touchées
Pour chaque question dont une prédiction a changé : `./pq score <id>`, mets à jour `meneur`, `confiance` et
`verdict` si les preuves le justifient (règle 5 : jamais sans nouvelle preuve citée), avec une ligne d'`historique`.
Si un verdict change, fais-le contester (`/challenge`).

## 5. Clore
`./pq check` (0 erreur), `./pq build`. Réponds : ce qui a été fait, ce qui a été trouvé (avec les liens), ce qui
reste en attente (`./pq gallica`), et la prochaine commande utile.

**Propagation (obligatoire avant de répondre)** : `./pq impact` sur ce qui a été ajouté ou modifié, puis mise à jour de chaque fichier listé (`methode/procedures/propager.md`).
