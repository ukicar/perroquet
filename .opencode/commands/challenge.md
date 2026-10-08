---
description: Faire attaquer le verdict d'une question historique par un avocat du diable indépendant, qui ne voit que les preuves, puis consigner ses objections et la réponse.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/challenge.md : ne pas modifier ici, modifier methode/commandes/challenge.md. -->

# /challenge : la contradiction organisée

Question : **$ARGUMENTS**.

## 1. Préparer le dossier de preuves (sans le raisonnement)
Rassemble dans un texte : la `question`, les énoncés des hypothèses (sans confiance ni meneur), et **toutes**
les preuves de la matrice avec, pour chacune, la citation verbatim, le locus, la classification de la source
(nature, fiabilité, consultée, distance, biais) et les recherches négatives. N'y mets **ni** le verdict, **ni**
les notes de matrice, **ni** le corps de la fiche.

## 2. Lancer l'avocat du diable
Confie ce dossier au rôle **avocat-du-diable** (`methode/roles/avocat-du-diable.md`), comme sous-agent
indépendant si ton outil le permet. Sinon, applique sa fiche dans un passage séparé en t'interdisant de
relire le raisonnement de la fiche.

## 3. Confronter
Compare son analyse au verdict actuel. Pour chaque objection :
- **fondée et prouvée par la base** → corrige la matrice (cellule mal notée, source dépendante d'une autre, etc.)
  et recalcule (`./pq score`) ;
- **fondée mais demandant une recherche** → ajoute une prédiction `non_testee` ou une hypothèse concurrente
  nouvelle (`auteur: agent`) ;
- **non fondée** → explique pourquoi dans `reponse`.

## 4. Consigner
Ajoute à `contestations` : `date`, `par: avocat-du-diable`, `objections`, `alternatives`, `reponse`, `effet`
(ex. « H1 probable → plausible », ou « aucun changement »). Toute modification de meneur ou de confiance va
aussi dans `historique` avec sa cause.

`./pq check`, `./pq build`. Réponds en 6–10 lignes : les objections les plus fortes, ce qui a changé, et ce
qu'il faudrait trouver pour trancher.
