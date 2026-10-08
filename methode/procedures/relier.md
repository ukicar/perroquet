<!-- Procédure interne : utilisée par les commandes, pas une commande en soi. -->
# Procédure : relier deux fiches

Demande : ce que la commande appelante veut créer ou relier.

1. Identifie les deux fiches (ids exacts, `grep -ril`). Crée-les si besoin (`./pq fiche`).
2. Choisis la relation dans `schema/relations.yaml` (respecte les types autorisés `de` / `vers`). Si aucune ne
   convient, utilise `lie_a` avec une `note`, et signale-le.
3. Trouve la justification : des assertions (`preuves: [source.aN]`) ou une hypothèse (`hypothese: q#Hn`). S'il
   n'y en a pas, **ne crée pas la relation** : propose `/source` (si l'utilisateur a une référence) ou
   `/hypothesis` (si c'est une supposition).
4. Fixe la `confiance` d'après les preuves (voir `METHODE.md`), éventuellement `role`, `debut`, `fin`.
   Écris la relation dans la fiche du **sujet** (A), une seule fois.
5. `./pq check`, `./pq build`. Réponds en une ou deux lignes.
