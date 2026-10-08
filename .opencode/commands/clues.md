---
description: Indiquer les pistes les plus utiles pour faire avancer une question historique — quelles sources consulter, avec quels termes, et ce que chaque résultat changerait.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/clues.md : ne pas modifier ici, modifier methode/commandes/clues.md. -->

# /clues : quelles recherches feraient le plus avancer la question ?

Question : **$ARGUMENTS**. Lis sa fiche, ses sources, et les recherches déjà faites (`grep -l "$ARGUMENTS" base/recherches/*`).

1. Pour chaque prédiction non testée ou indécidable, et pour chaque **trou** (une hypothèse sans prédiction
   diagnostique, une preuve-clé connue seulement par citation, une source jamais consultée), propose une piste :
   - **où** : fonds, cote, édition, ark/identifiant, ou type de document (contrats de mariage, testaments,
     preuves de noblesse, compoix, registres paroissiaux protestants, sacs à procès…) ;
   - **comment** : la commande exacte (`./pq search …`) ou l'accès (en ligne, compte, salle de lecture) ;
   - **ce que ça changerait** : quel résultat renforcerait ou affaiblirait quelle hypothèse ;
   - **coût** : immédiat / en ligne long / déplacement.
2. Vérifie que la piste n'a pas déjà été suivie (fiches `recherche`). Ne propose pas de refaire une recherche
   négative sans raison nouvelle (autre graphie, autre fonds).
3. Classe les pistes par **valeur diagnostique / coût**. Si une piste mérite une prédiction formelle, ajoute-la
   à la fiche (`statut: non_testee`) et note-le dans `historique`.
4. Ne lance pas les recherches (c'est `/test`), sauf une vérification rapide d'accessibilité.
5. `./pq check`, `./pq build`. Réponds par une liste classée de 3 à 7 pistes, chacune en 2 lignes, et la
   commande à lancer pour la meilleure (`/test <id> Pn`).
