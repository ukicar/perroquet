# Perroquet

Registre de recherche historique sur **Gabrielle d'Espinas**, veuve d'Arnaud II de Roquemaurel, seigneur de
Soueix en Couserans, tué dans l'incendie de Soueix vers le 2 février 1567.

Uniquement des faits sourcés et des hypothèses mises à l'épreuve, sans fiction. Des agents IA (Claude Code ou
OpenCode) font le travail d'archiviste et de critique ; vous pilotez par des commandes et lisez le résultat dans un
site local.

## Installer sur un nouvel ordinateur

```bash
git clone https://github.com/ukicar/perroquet.git
```

```bash
cd perroquet && tools/setup.sh
```

`setup.sh` installe les dépendances Python dans `.venv/`, génère les commandes pour Claude Code et OpenCode,
récupère les scans téléchargeables (`./pq fetch`) et construit le site. Les scans et PDF ne sont **pas** dans
git : ils vivent dans `cache/`, propre à chaque machine.

## Travailler

Ouvrez le dossier dans Claude Code (ou OpenCode) et utilisez les commandes :

| Commande | Pour |
|---|---|
| `/hypothesis "Gabrielle était protestante"` | proposer une hypothèse : l'agent pose les concurrentes et ce qu'il faudrait trouver |
| `/test <question>` | chercher dans les sources, verser ce qu'on trouve, mettre à jour le verdict |
| `/clues <question>` | savoir quelles recherches feraient avancer |
| `/challenge <question>` | faire attaquer le verdict par un avocat du diable |
| `/research <fiche>` | explorer autour d'une personne, d'un lieu, d'un événement |
| `/source <lien>` | verser une source (Gallica, archive.org, archives, livre) |
| `/fiche`, `/link`, `/verify`, `/transcribe` | créer, relier, faire vérifier, transcrire |
| `/audit` | voir où la preuve est faible |
| `/view` | ouvrir le site (graphe, hypothèses, fiches, chronologie) |
| `/sync` | partager : enregistrer, récupérer le travail de l'autre, envoyer |

On peut aussi parler normalement à l'agent : il suit les mêmes règles (`AGENTS.md`).

La méthode est expliquée dans [METHODE.md](METHODE.md).

## Organisation

| Dossier | Contenu |
|---|---|
| `base/` | la base : une fiche markdown par personne, famille, lieu, événement, institution, source, question, enquête, recherche |
| `methode/` | les procédures des commandes et les rôles des agents (indépendants de l'outil) |
| `schema/` | les vocabulaires contrôlés (types, relations, échelles) |
| `notes/` | les notes de recherche d'origine |
| `transcriptions/` | transcriptions de manuscrits |
| `tools/` | l'outil `pq` et les outils de transcription |
| `.claude/`, `.opencode/` | générés par `./pq adapters`, ne pas modifier |
| `cache/`, `site/` | fichiers lourds et site généré, hors git |
