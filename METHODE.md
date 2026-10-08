# La méthode de Perroquet

Ce registre sert à établir ce qu'on peut savoir de la vie de Gabrielle d'Espinas, et à distinguer ce qui est
prouvé de ce qui est seulement plausible. Il applique quatre méthodes reconnues, adaptées à une recherche menée
avec des agents IA.

## 1. Tout part des sources, et chaque source est jugée

On ne recopie pas un fait : on note **ce que dit telle source**, avec la citation exacte et la page ou le
folio. C'est le modèle des « factoïdes » des bases prosopographiques (King's College, Londres) : la source dit X ;
la conclusion vient après, ailleurs.

Chaque source reçoit une **fiche critique** :

| Critère | Question posée | Exemple |
|---|---|---|
| Nature | Est-ce l'acte lui-même, une copie, une édition, une étude, une compilation ? | Registre 1 B 74 = original ; Bardies 1903 = étude |
| Information | L'auteur a-t-il vu les faits, ou les rapporte-t-il ? | Monluc en février 1567 : contemporain mais de seconde main |
| Preuve | L'assertion répond-elle directement à la question, indirectement, ou par une absence ? | « veuve d'Arnaud » : directe |
| Fiabilité (A–F) | Que vaut cette source en général ? | Code de l'Amirauté, utilisé en renseignement et en histoire |
| Crédibilité (1–6) | Que vaut cette assertion précise ? | Confirmée ailleurs = 1 ; impossible à juger = 6 |
| Consultée | L'avons-nous lue, ou seulement quelqu'un qui la cite ? | Vuillier 1998 : connue par Lasnier |

C'est la partie « critique des sources » du **Genealogical Proof Standard** (Board for Certification of
Genealogists, E. Shown Mills, *Evidence Explained*) et de la critique externe/interne des historiens.

## 2. Une question, plusieurs hypothèses

On ne teste jamais une hypothèse seule : on la met en **concurrence**. C'est l'**analyse des hypothèses
concurrentes** (ACH) de Richards Heuer :

1. On pose la question (« De quelle famille est Gabrielle ? »).
2. On écrit toutes les réponses raisonnables, y compris « une autre » ou « on ne peut pas savoir ».
3. On range chaque preuve dans une **matrice** : pour chaque hypothèse, la preuve est très cohérente (CC),
   cohérente (C), neutre (N), incohérente (I) ou très incohérente (II).
4. On pondère chaque preuve par la fiabilité de sa source et la crédibilité de l'assertion.
5. **L'hypothèse qui mène est celle que les preuves contredisent le moins**, pas celle qui accumule le plus
   d'indices favorables. Une preuve compatible avec toutes les hypothèses ne prouve rien : elle est marquée
   « non diagnostique ».

## 3. Des prédictions qu'on peut vérifier

Chaque hypothèse annonce ce qu'on **devrait trouver** si elle était vraie, et **où** (la falsification de
Popper appliquée aux archives). Exemple : « Si Gabrielle est une Espinas de Cardonne, les preuves de noblesse de
1669 doivent faire remonter la filiation au XVIe siècle. » Une prédiction est **diagnostique** quand son
résultat départagerait les hypothèses.

Tester une prédiction (`/test`), c'est chercher précisément là. Si on trouve, la base s'enrichit de la source et
de ses assertions. Si on ne trouve rien, on consigne la **recherche négative** : une absence là où on attendait
une mention est aussi une preuve, et elle évite de refaire la même recherche.

## 4. La contradiction organisée

Un agent séparé, l'**avocat du diable** (`/challenge`), reçoit uniquement les preuves, sans le raisonnement
qui a conduit au verdict, et cherche à le renverser : autre explication des mêmes faits, preuve mal lue,
source dépendante d'une autre, prédiction oubliée. Ses objections sont consignées, avec la réponse. Une
confiance ne change que sur preuve nouvelle, jamais sur simple argument.

## L'échelle de confiance

| Niveau | Sens |
|---|---|
| établi | prouvé par au moins une preuve directe vérifiée, sans contradiction non résolue |
| probable | fortement soutenu, aucune preuve contraire sérieuse |
| plausible | compatible avec les preuves, rien ne le confirme directement |
| possible | pas exclu, appui faible ou indirect |
| improbable | des preuves vont contre |
| réfuté | contredit par une preuve directe fiable |

Une assertion n'est « vérifiée » que si un second agent (ou vous) a relu la source indépendamment. Une
conclusion ne peut pas être « établie » sur des assertions non vérifiées.

## Le cycle de travail

```
 vous proposez       l'agent pose les         il cherche là où         la base grandit :
 une hypothèse  →    hypothèses concurrentes →  les prédictions     →   sources, assertions,
 (/hypothesis)       et leurs prédictions       le disent (/test)        recherches négatives
                                                                               │
 nouvelles questions  ←  verdict daté   ←   l'avocat du diable   ←   la matrice est
 (sous-questions)        et motivé          attaque (/challenge)      recalculée
```

Chaque `/test` laisse une **enquête** datée : ce qui a été cherché, trouvé, changé. On peut ainsi relire
comment chaque conclusion a été atteinte, et par qui.

## Les commandes

| Commande | Pour |
|---|---|
| `/hypothesis "…"` | proposer une hypothèse ; l'agent pose la question, les concurrentes et les prédictions |
| `/test <question> [P2]` | tester les prédictions : recherches ciblées, nouvelles sources, verdict mis à jour |
| `/clues <question>` | savoir quelles recherches feraient le plus avancer la question |
| `/challenge <question>` | faire attaquer le verdict par l'avocat du diable |
| `/research <fiche>` | explorer librement autour d'une personne, d'un lieu, d'un événement |
| `/source <lien ou référence>` | verser une source : critique, assertions avec citations, liens |
| `/fiche <type> "<nom>"` | créer une fiche (personne, famille, lieu, événement, institution) |
| `/link <a> <relation> <b>` | relier deux fiches, preuve à l'appui |
| `/verify <assertion ou source>` | faire relire une assertion sur la source par un second agent |
| `/transcribe <source>` | transcrire un manuscrit en double lecture |
| `/audit` | voir où la preuve est faible et ce qui reste à faire |
| `/fetch`, `/build`, `/view`, `/publish`, `/sync` | fichiers lourds, site, partage, synchronisation |

## Ce qui ne figure pas ici

Le roman. Ce registre ne contient aucune invention : il sert de socle. Ce que vous imaginerez pour le livre
devra rester compatible avec ce qui est « établi » ou « probable » ici.
