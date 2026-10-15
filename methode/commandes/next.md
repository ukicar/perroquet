---
description: Que faire maintenant ? Fait le point sur toute la base ou sur une question, repère où la preuve est faible et propose les prochaines actions classées, chacune avec sa commande prête à copier.
argument: "[id de question, facultatif]"
---
# /next : que faire maintenant ?

Portée : **$ARGUMENTS** (vide = toute la base ; un id de question = cette question seulement).
Cette commande **ne modifie aucun fait ni aucun verdict** : elle observe et propose.

## 1. Faire le point
- `./pq audit` et `./pq score $ARGUMENTS`.
- Corrige toi-même les erreurs purement techniques (référence cassée, valeur hors vocabulaire) quand la
  correction ne change aucun fait ; sinon signale-les.

## 2. Repérer les faiblesses
Ajoute ta propre lecture critique aux avertissements :
- verdicts plus forts que leurs preuves (confiance élevée sur des assertions `verifie: non`, ou sur des sources
  connues seulement par citation) ;
- deux sources présentées comme indépendantes alors que l'une recopie l'autre ;
- questions dont toutes les preuves sont non diagnostiques, ou dont le meneur déclaré n'est pas le meneur calculé ;
- questions jamais contestées.

## 3. Trouver les meilleures pistes
Pour chaque question concernée, regarde les prédictions non testées ou indécidables et les **trous** (hypothèse
sans prédiction diagnostique, preuve-clé jamais lue directement). Pour chaque piste :
- **où** chercher (fonds, cote, édition, ark, type d'acte : contrat de mariage, testament, preuves de noblesse,
  compoix, registres protestants, sacs à procès…) et **comment** (`./pq search …`, en ligne, compte, salle de lecture) ;
- **ce que ça changerait** (quel résultat renforce ou affaiblit quelle hypothèse) ;
- **coût** : immédiat / long en ligne / déplacement.
Vérifie dans `base/recherches/` qu'elle n'a pas déjà été suivie. Si une piste mérite une prédiction formelle,
ajoute-la à la fiche (`statut: non_testee`) avec une ligne d'`historique` : c'est la seule écriture permise ici.

## 4. Répondre
Une liste classée de 3 à 7 actions, de la plus utile à la moins utile, chacune en deux lignes avec sa commande :
`/test <question> P2`, `/challenge <question>`, `/verify <source>`, `/explore <fiche>`, ou une démarche à faire
soi-même (salle de lecture, compte Geneanet). Toute démarche à faire sur place proposée ici est aussi notée dans
`base/demarches/` (`methode/procedures/demarche.md`) ; renvoie à la page « À faire sur place » du site. Puis `./pq build`.
