---
name: transcribe
description: Transcrire un manuscrit ou registre ancien en double lecture indépendante (paléographie), puis comparer et réconcilier, et verser les passages utiles comme assertions.
argument-hint: <source-id ou fichier> [pages]
---
<!-- GÉNÉRÉ par `./pq adapters` depuis methode/commandes/transcribe.md : ne pas modifier ici, modifier methode/commandes/transcribe.md. -->

# /transcribe : transcription en double lecture

Cible : **$ARGUMENTS**.

1. **Préparer.** Le document doit être dans `cache/` (sinon `./pq fetch` ou téléchargement). Crée un dossier
   texte `transcriptions/<nom>/` avec `transcript/` et `verify/`, et copie-y `transcriptions/1567/CONVENTIONS.md`
   en l'adaptant (source, pages). Découpe les pages en images avec les outils de `tools/transcription/`
   (`PQ_TRANSCRIPTION=<nom> python3 tools/transcription/prep_images.py <dossier pages> cache/transcription_<nom>/images <première> <dernière>`) ;
   les images restent dans `cache/`.
2. **Lecture 1** (rôle `paleographe`) : une page = un fichier `transcript/<page>.md`, ligne à ligne, selon les
   conventions (abréviations conservées, `[mot?]` pour les doutes).
3. **Lecture 2** : un **autre** paléographe indépendant (sous-agent séparé, sans voir la lecture 1) écrit
   `verify/<page>.md`.
4. **Comparer** : `PQ_TRANSCRIPTION=<nom> python3 tools/transcription/compare.py` ; pour chaque divergence,
   regarde l'image agrandie (`zoom_lines.py`, `crop.py`, sorties dans `cache/zoom/`) et tranche ; le résultat
   réconcilié va dans `transcript/`.
5. **Assembler** le texte final et **verser** les passages pertinents comme assertions de la source (citation
   = texte réconcilié, `locus` = folio/ligne, `verifie: agent` puisque doublement lu).
6. `./pq check`, `./pq build`. Réponds : pages faites, lectures incertaines restantes, assertions versées.
