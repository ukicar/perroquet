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

<!-- aide:debut -->
Dans Claude Code ou OpenCode, ouvert sur le dossier `perroquet`. Dix commandes suffisent ; tout le reste, l'agent le fait
seul. Vous pouvez aussi simplement lui parler : il suit les mêmes règles.

**Le cycle de recherche** : on part d'une idée, on la met à l'épreuve, on la fait attaquer.

| Commande | Quand l'utiliser |
|---|---|
| `/hypothesis "Gabrielle était protestante"` | Vous avez une idée ou un doute. L'agent la transforme en question, ajoute les explications concurrentes et dit ce qu'il faudrait trouver pour trancher. |
| `/test <question>` | Pour faire avancer une question. L'agent choisit les recherches les plus décisives, cherche dans les sources, ajoute ce qu'il trouve (ou note qu'il n'a rien trouvé) et met le verdict à jour. Si le verdict change, il le fait contester automatiquement. |
| `/challenge <question>` | Quand un verdict vous semble trop facile. Un second agent, qui ne voit que les preuves, essaie de le renverser. |
| `/next` | Quand vous ne savez pas quoi faire. L'agent fait le point (sur tout, ou sur une question : `/next <question>`) et propose les actions les plus utiles, avec la commande à copier. |

**Apporter de la matière**

| Commande | Quand l'utiliser |
|---|---|
| `/source <lien ou référence>` | Vous avez trouvé un document (Gallica, archives, livre, photo de registre). L'agent le classe, en extrait les faits avec citations, le transcrit si c'est un manuscrit, et le relie aux personnes et aux questions. |
| `/explore <personne, lieu, événement>` | Vous voulez tout savoir sur quelqu'un ou quelque chose, sans question précise. L'agent cherche, complète la fiche et propose des questions. |
| `/verify <source ou fiche>` | Avant de vous appuyer sur un fait. Un second agent relit la citation sur l'original ; sans cette relecture, rien ne peut être « établi ». |

**Partager**

| Commande | Quand l'utiliser |
|---|---|
| `/sync-gallica` | Quand Gallica a bloqué nos recherches (cela arrive souvent). L'agent reprend tout ce qui a été mis en attente : recherches, pages à lire. Si Gallica bloque encore, il le dit et on réessaie plus tard. |
| `/sync` | Au début et à la fin de chaque séance : récupère le travail de l'autre personne, envoie le vôtre, met à jour le site et le lien partagé. |
| `/view` | Pour ouvrir le site : graphe, hypothèses, fiches, chronologie, et la page **À faire sur place** (archives à visiter, demandes à envoyer, classées par lieu). |

Créer une fiche, relier deux personnes, transcrire, télécharger un scan : l'agent le fait de lui-même pendant
ces commandes (procédures dans `methode/procedures/`). Vous pouvez aussi le demander en une phrase
(« ajoute que Guillaume est le frère d'Arnaud, d'après le dossier d'Hozier »).

Cette liste : `/aide` dans l'agent, `./pq aide` dans un terminal, ou le tableau de bord du site.
<!-- aide:fin -->

## Ce qui ne figure pas ici

Le roman. Ce registre ne contient aucune invention : il sert de socle. Ce que vous imaginerez pour le livre
devra rester compatible avec ce qui est « établi » ou « probable » ici.
