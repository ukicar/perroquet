# Perroquet : instructions pour tout agent (Claude Code, OpenCode, autre)

Perroquet est une base de recherche historique **factuelle** sur Gabrielle d'Espinas (veuve d'Arnaud II de
Roquemaurel, seigneur de Soueix en Couserans, tué dans l'incendie de Soueix vers le 2 février 1567) et son
entourage. Ce n'est pas un roman : rien d'inventé n'entre dans la base. Les utilisateurs (deux personnes,
non programmeurs) pilotent la recherche par des commandes `/…` et en langage courant, et lisent le résultat
dans le site HTML (`./pq view`).

**Langue** : tout ce que tu écris dans la base est en **français**. Les citations de sources restent
**verbatim**, dans leur langue et graphie d'origine (moyen français compris), sans modernisation.

La méthode est décrite pour les humains dans [METHODE.md](METHODE.md). Les neuf commandes des utilisateurs
(`/hypothesis`, `/test`, `/challenge`, `/next`, `/source`, `/explore`, `/verify`, `/sync`, plus `/view`) sont
dans `methode/commandes/` ; les procédures internes qu'elles appellent (créer une fiche, relier, transcrire,
fichiers lourds, publier le lien) dans `methode/procedures/` ; les rôles des sous-agents dans `methode/roles/`.
Quand l'utilisateur demande en langage courant une de ces actions, suis la procédure correspondante. Les dossiers `.claude/` et
`.opencode/` sont **générés** par `./pq adapters` : ne jamais les modifier à la main.

## Règles absolues

1. **Aucune affirmation sans source.** Tout fait entre dans la base sous forme d'*assertion* dans la fiche de
   sa source, avec la **citation exacte** et le **locus** (page, folio, ligne). Une relation entre fiches cite
   ses preuves (`preuves: [source.aN]`) ou l'hypothèse qui la porte (`hypothese: id#H1`).
2. **Ne jamais inventer** une citation, une cote, une page, un ark, une date. Si tu n'as pas lu le passage
   toi-même dans cette session ou dans un fichier du dépôt, tu ne le cites pas : tu notes la piste à vérifier.
3. **Distinguer ce que dit la source de ce que tu en conclus.** Les assertions rapportent la source ; les
   conclusions vont dans les hypothèses (verdict, confiance) ou dans la synthèse d'une fiche, avec des liens.
4. **Toute question a des hypothèses concurrentes** (au moins deux, dont une « autre / inconnue » si besoin).
   On cherche aussi ce qui **réfuterait** l'hypothèse préférée.
5. **On n'élève jamais une confiance sans nouvelle preuve citée.** Chaque changement de verdict ou de
   confiance est daté dans `historique` avec sa cause.
6. **Les recherches négatives sont des preuves.** Toute recherche significative est consignée dans
   `base/recherches/` (`./pq search` le fait automatiquement).
7. **Les gros fichiers ne vont jamais dans git.** Scans, PDF, images : dans `cache/` (ignoré par git), déclarés
   dans la fiche source sous `fichiers:` avec l'URL d'origine. Seuls les textes (fiches, transcriptions) sont
   versionnés.
8. **Avant de terminer** une commande qui modifie la base : `./pq check` doit afficher 0 erreur. Corrige
   toi-même les erreurs. Puis `./pq build` pour mettre le site à jour.
9. Ne fais jamais `git push` ni de commit sauf via `/sync` (`./pq sync`) ou à la demande explicite.

## L'outil `./pq` (à utiliser par le shell)

| Commande | Rôle |
|---|---|
| `./pq check` / `./pq audit` | valider la base / voir aussi les avertissements de méthode |
| `./pq fiche <type> "<nom>"` | créer une fiche (détecte les doublons) ; types : personne famille lieu evenement institution source hypothese enquete |
| `./pq search gallica <termes…> [--index text] --hyp <id> --objet "<objet>"` | catalogue/plein texte Gallica |
| `./pq search gallica-texte <ark> <termes…>` | occurrences, avec pages, dans un document Gallica |
| `./pq search archive <termes…>` / `archive-texte <identifiant> <termes…>` | archive.org (catalogue / texte OCR) |
| `./pq search local <chemin> <termes…>` | dans un fichier texte local |
| `./pq score [id]` | scores ACH (incohérence pondérée) des hypothèses |
| `./pq fetch [--status]` | récupérer les gros fichiers manquants dans `cache/` |
| `./pq hash <fichier>` | empreinte sha256 à noter dans `fichiers:` |
| `./pq build` / `./pq view` | générer / ouvrir le site |
| `./pq sync` | valider, commit, pull --rebase, push |
| `./pq adapters` | régénérer `.claude/` et `.opencode/` depuis `methode/` |

Les recherches web générales (moteur de recherche de ton outil) sont permises en complément ; consigne alors
toi-même une fiche `recherche`. Les recherches qui demandent un compte (Geneanet…) ou une salle de lecture
sont proposées à l'utilisateur, jamais simulées.

## Format des fiches

Une fiche = `base/<dossier>/<id>.md`, en-tête YAML entre `---`, puis une synthèse en français (markdown).
`id` = nom du fichier : minuscules, chiffres, tirets (`gabrielle-d-espinas`). Types, dossiers et champs :
`schema/types.yaml`. Valeurs autorisées : `schema/vocabulaire.yaml`. Relations : `schema/relations.yaml`.

Liens dans le texte : `[[id]]`, `[[id|libellé]]`, assertion `[[source-id.a3]]`, hypothèse `[[question-id#H2]]`,
prédiction `[[question-id#P1]]`.

Dates : `"1567-05-24"`, `"1567-02"`, `"1567"` ; approximative : `"1567-02-02~"` ; incertaine : `"1567?"`.
`periode: [1540, 1610]` donne l'étendue de vie ou d'activité connue (frise et curseur du graphe).

### Entité (personne, famille, lieu, evenement, institution)

```yaml
---
id: gabrielle-d-espinas
type: personne
nom: Gabrielle d'Espinas
variantes: [Gabrielle Despinas, Gabrielle d'Espinasse]
naissance: null
mort: null
periode: [1557, 1610]          # bornes connues par les sources
relations:
  - {rel: epoux_de, vers: arnaud-ii-de-roquemaurel, preuves: [bardies-1903.a2], confiance: etabli}
  - {rel: participe_a, vers: arret-du-24-mai-1567, role: demanderesse, preuves: [bardies-1903.a2], confiance: probable}
  - {rel: membre_de, vers: famille-d-espinas-de-cardonne, hypothese: origine-de-gabrielle#H1, confiance: plausible}
---
Synthèse en français. Chaque phrase de fond renvoie à [[bardies-1903.a2]] ou à [[origine-de-gabrielle]].
```
Lieux : `coordonnees: [42.86, 1.20]` (lat, lon) quand elles sont sûres. Événements : `date` obligatoire, `fin`.
Relation : `rel`, `vers`, `confiance` (obligatoire), `preuves` et/ou `hypothese`, facultatifs `role`, `debut`,
`fin`, `note`. Écrire chaque relation **une seule fois**, dans la fiche du sujet (les symétriques aussi).

### Source

```yaml
---
id: bardies-1903
type: source
nom: Bardies, « Les guerres de religion en Couserans » (1903)
auteur: baron de Bardies
titre: "Les guerres de religion en Couserans"
date_redaction: "1903"
genre: article            # vocabulaire.genre
nature: etude             # original | copie | edition | etude | compilation
fiabilite: C              # A–F (code de l'Amirauté)
consultee: oui            # oui | partiel | non | inaccessible
depot: null
cote: null
ark: bpt6k57278962
url: https://gallica.bnf.fr/ark:/12148/bpt6k57278962
distance: 336             # années entre les faits et la rédaction
biais: "Érudit local ; s'appuie sur des preuves de Malte de 1763."
citee_par: []             # autres sources qui la citent
fichiers:                 # gros fichiers locaux, jamais dans git
  - {chemin: cache/…, url: …, sha256: …, recuperation: auto, note: …}
assertions:
  - id: a1
    texte: "Gabrielle d'Espinas, veuve d'Arnaud de Roquemaurel, obtient avec le procureur général un arrêt du 24 mai 1567 condamnant à mort Soulan et ses complices."
    citation: "un arrêt du Parlement de Toulouse, daté du 24 mai 1567, qui condamna à mort Jean François de Mauléon, sieur de Soulan, et une quinzaine de ses complices, à la requête de Gabrielle d'Espinas, veuve d'Arnaud de Roquemaurel, et du procureur général"
    locus: "p. 83 (Gallica f. 91)"
    sujets: [gabrielle-d-espinas, arnaud-ii-de-roquemaurel, jean-francois-de-mauleon]
    date: "1567-05-24"
    preuve: directe           # directe | indirecte | negative
    information: secondaire   # primaire | secondaire | inconnue
    credibilite: 2            # 1–6
    verifie: agent            # non | agent | humain
---
Critique de la source (provenance, auteur, fiabilité, limites) en français.
```

### Question et hypothèses (`base/hypotheses/`)

```yaml
---
id: origine-de-gabrielle
type: hypothese
nom: Origine familiale de Gabrielle d'Espinas
question: "De quelle famille Gabrielle d'Espinas est-elle issue ?"
sujets: [gabrielle-d-espinas]
statut: ouverte                     # ouverte | tranchee | suspendue
hypotheses:
  - {id: H1, enonce: "Elle appartient aux Espinas de Cardonne (Volvestre, diocèse de Rieux).", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Elle appartient à une autre famille d'Espinas du Comminges.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Elle n'est pas originaire du Comminges.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Les preuves de 1669 (jugement Bezons) font remonter la filiation des Espinas de Cardonne au XVIe s. et nomment une Gabrielle."
    ou_chercher: "Procès-verbaux Bezons, AD Hérault série C / AD31 C"
    diagnostique: haute          # haute | moyenne | faible
    statut: non_testee           # non_testee | confirmee | infirmee | indecidable
    resultat: null
    enquetes: []
matrice:                           # ACH : une ligne par preuve, une colonne par hypothèse
  - {preuve: site-roquemaurel.a4, H1: C, H2: C, H3: I, note: "« d'une maison du Comminges », sans source"}
contestations:
  - date: "2026-10-08"
    par: avocat-du-diable
    objections: ["…"]
    alternatives: ["…"]
    reponse: "…"
    effet: "aucun changement de confiance"
meneur: H1
confiance: plausible               # confiance dans le meneur
verdict: "Texte court : où en est la question et pourquoi."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes"}
sous_questions: []
---
Raisonnement détaillé, en français, avec liens.
```
Cellules : `CC` très cohérent, `C` cohérent, `N` neutre, `I` incohérent, `II` très incohérent. Le meneur est
l'hypothèse avec **le moins d'incohérence pondérée** (`./pq score`), pas celle qui a le plus de soutiens. Une
ligne notée pareil pour toutes les hypothèses n'est pas diagnostique. Une ligne peut citer une recherche
(`preuve: r-2026-10-07-…`) quand c'est une absence qui fait preuve.

### Enquête (`base/enquetes/`) : trace de chaque `/test`

```yaml
---
id: e-2026-10-08-origine-de-gabrielle
type: enquete
nom: "Test de P1 : preuves de noblesse de 1669"
hypothese: origine-de-gabrielle
date: "2026-10-08"
auteur: <git user.name>
predictions: [P1]
recherches: [r-2026-10-08-…]
ajouts: {sources: [], assertions: [], fiches: []}
changements: ["P1 : non_testee → indecidable (salle de lecture)"]
verdict_avant: "H1 plausible"
verdict_apres: "H1 plausible"
---
Récit de l'enquête.
```

### Recherche (`base/recherches/`) : créée par `./pq search`, complétée à la main

Champs : `date, auteur, outil, requete, perimetre, resultat (positif|negatif|partiel|bloque), resultats,
sources_creees, hypotheses`. Compléter le corps : ce que le résultat signifie, ce qu'il faut faire ensuite.

## Évaluer une source

- `nature` : l'acte lui-même (original) ou une copie, édition, étude, compilation ?
- `information` (par assertion) : l'informateur a-t-il vu les faits (primaire) ou rapporte-t-il (secondaire) ?
- `preuve` : l'assertion répond-elle directement à la question, indirectement, ou par une absence ?
- `fiabilite` A–F de la source, `credibilite` 1–6 de l'assertion (voir `schema/vocabulaire.yaml`).
- `consultee` : as-tu lu la source elle-même, ou seulement quelqu'un qui la cite (`citee_par`) ?
- `distance` et `biais` : délai entre les faits et l'écrit, intérêt de l'auteur (famille, parti, confession).

## Rôles (sous-agents)

`archiviste`, `critique-des-sources`, `avocat-du-diable`, `verificateur`, `paleographe` : voir
`methode/roles/`. Si ton outil ne permet pas de lancer un sous-agent, joue le rôle dans un passage séparé, en
suivant strictement sa fiche (l'avocat du diable ne lit que les preuves, pas le raisonnement).

## Repères du dossier

- `notes/` : notes de recherche d'origine (provenance, lecture seule). Elles ont été versées dans `base/`.
- `transcriptions/1567/` : transcription de BnF fr. 5455 (1567), conventions dans `CONVENTIONS.md`, outils
  dans `tools/transcription/` (images dans `cache/transcription_1567/images`).
- `cache/` : fichiers lourds et textes OCR téléchargés, propres à chaque machine.
