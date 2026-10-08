---
description: Afficher la liste des commandes de Perroquet et quand utiliser chacune.
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/aide.md : ne pas modifier ici, modifier methode/commandes/aide.md. -->

# /aide

Affiche à l'utilisateur, tel quel et sans rien ajouter, le texte ci-dessous (il est recopié depuis
`methode/aide.md` par `./pq adapters`). Ne lance aucune autre action.

Dans Claude Code ou OpenCode, ouvert sur le dossier `perroquet`. Neuf commandes suffisent ; tout le reste, l'agent le fait
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
| `/sync` | Au début et à la fin de chaque séance : récupère le travail de l'autre personne, envoie le vôtre, met à jour le site et le lien partagé. |
| `/view` | Pour ouvrir le site : graphe, hypothèses, fiches, chronologie. |

Créer une fiche, relier deux personnes, transcrire, télécharger un scan : l'agent le fait de lui-même pendant
ces commandes (procédures dans `methode/procedures/`). Vous pouvez aussi le demander en une phrase
(« ajoute que Guillaume est le frère d'Arnaud, d'après le dossier d'Hozier »).

Cette liste : `/aide` dans l'agent, `./pq aide` dans un terminal, ou le tableau de bord du site.
