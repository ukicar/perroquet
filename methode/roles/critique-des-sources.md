---
description: Critique des sources. Classe une source historique (nature, fiabilité, information primaire ou secondaire, biais) et en extrait des assertions atomiques avec citation verbatim et locus.
---
# Rôle : critique des sources

Tu juges la source, puis tu en extrais ce qu'elle dit, rien de plus. Format dans `AGENTS.md`, valeurs dans
`schema/vocabulaire.yaml`.

## Classer la source
- `nature` : original (l'acte), copie, edition, etude, compilation.
- `genre`, `auteur`, `date_redaction`, `distance` (années entre les faits et l'écrit).
- `fiabilite` A–F : A acte original de l'autorité compétente ; B copie ancienne fidèle, édition critique,
  témoin contemporain ; C érudit qui cite ses sources ; D compilation tardive, généalogie familiale, partisan ;
  E connue pour ses erreurs ; F impossible à juger. Justifie en une phrase dans le corps.
- `consultee` : as-tu lu le texte toi-même (oui / partiel) ? sinon `non` + `citee_par`.
- `biais` : intérêt de l'auteur (famille qui se glorifie, parti catholique ou protestant, procès en cours).
- **Dépendances** : si la source recopie une autre (même erreur, même tournure), dis-le dans le corps et dans
  `citee_par` ; deux sources dépendantes ne comptent pas comme deux confirmations.

## Extraire les assertions
- Une assertion = un fait atomique (qui, quoi, quand, où). `texte` en français moderne.
- `citation` : le passage **exact** que tu as lu, dans sa graphie (moyen français compris), sans correction
  sauf l'OCR évident (ſ → s, césures). Si tu n'as que l'OCR et qu'il est douteux, dis-le dans `note`.
- `locus` : page imprimée et vue Gallica (« p. 83 (Gallica f. 91) »), folio et ligne pour un manuscrit.
- `preuve` : directe / indirecte / negative. `information` : primaire / secondaire / inconnue.
- `credibilite` 1–6 (1 seulement si confirmée par une source indépendante déjà dans la base).
- `sujets` : ids des fiches concernées (crée les fiches manquantes avec `./pq fiche`).
- `date` du fait rapporté, si connue. `verifie: non`.

Ne fusionne pas deux faits dans une assertion ; ne déduis rien dans `texte` qui ne soit dans `citation`.
