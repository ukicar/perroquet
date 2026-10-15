---
description: Faire relire sur l'original, par un second agent indépendant, les citations d'une source ou d'une fiche. Seules les citations ainsi relues peuvent fonder un fait « établi ».
argument: "<source-id.aN | source-id | fiche-id>"
---
# /verify : relecture indépendante

Cible : **$ARGUMENTS** (une assertion, toutes les assertions d'une source, ou toutes celles qui fondent une fiche).

1. Liste les assertions à vérifier (`verifie: non` en priorité).
2. Pour chacune, confie au rôle **verificateur** (`methode/roles/verificateur.md`), comme sous-agent
   indépendant si possible, **seulement** : la référence de la source (ark, page, fichier local, cote) et le
   locus — **pas** la citation ni le texte enregistrés. Il relit la source et rapporte ce qu'il y lit.
3. Compare sa lecture à l'assertion enregistrée :
   - identique (aux variantes de graphie près) → `verifie: agent` ;
   - différente → corrige `citation`/`texte`/`locus`, garde `verifie: non`, ajoute une `note` datée ;
     si la correction change une preuve de matrice, recalcule et consigne dans `historique`.
   - source inaccessible → laisse `verifie: non`, note pourquoi.
4. Ne mets **jamais** `verifie: humain` toi-même : c'est l'utilisateur qui le décide.
5. `./pq check`, `./pq build`. Réponds : vérifiées, corrigées, impossibles.

**Propagation (obligatoire avant de répondre)** : `./pq impact` sur ce qui a été ajouté ou modifié, puis mise à jour de chaque fichier listé (`methode/procedures/propager.md`).
