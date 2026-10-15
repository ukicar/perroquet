<!-- Procédure interne : utilisée par les commandes, pas une commande en soi. -->
# Procédure : noter une démarche à faire sur place

Une **démarche** est ce que seuls les utilisateurs peuvent faire : aller en salle de lecture, écrire à un service
d'archives, commander une reproduction, emprunter ou acheter un livre, contacter un particulier. Les démarches
vivent dans `base/demarches/` et la page « À faire sur place » du site (`a-faire.html`) les regroupe **par lieu**,
pour que les utilisateurs puissent préparer une visite.

Quand en créer une : chaque fois qu'une piste utile ne peut pas être suivie en ligne (prédiction dont
`ou_chercher` est une salle de lecture, source `consultee: non` ou `inaccessible` conservée dans un dépôt,
recherche `resultat: bloque`).

1. **Pas de doublon.** `grep -rl "<cote ou fonds>" base/demarches/` : si une démarche vise déjà le même dossier,
   ajoute seulement la prédiction à son champ `pour` (et précise `action` si besoin).
2. **Le lieu.** `depot` doit être une clé de `depots` dans `schema/vocabulaire.yaml` (dépôts d'archives,
   bibliothèques, détenteurs privés). S'il manque, ajoute-le avec `libelle`, `ville`, `url` (vérifiée, sinon `null`)
   et `acces` (adresse, conditions). Ne jamais inventer une adresse ou une URL.
3. **Créer** : `./pq fiche demarche "<titre court>"` puis remplir :
   - `cote` : la cote exacte si on la connaît, sinon « à identifier » avec le fonds ou la série ;
   - `action` : en une ou deux phrases, ce qu'il faut demander ou lire et ce qu'il faut photographier ;
   - `pourquoi` : ce que la pièce pourrait apprendre, en clair ;
   - `mode` (vocabulaire `mode`), `priorite` (`haute` = décisive pour une question importante) ;
   - `pour` : les prédictions servies (`question#P2`) ou les fiches concernées ; `sources` : les fiches source liées.
4. **Quand l'utilisateur rapporte une démarche faite** : `statut: faite`, `date_faite`, `resultat` en une phrase ;
   versez la pièce (`/source`) et mettez à jour les prédictions. Une démarche sans résultat utile est aussi
   consignée (`resultat`) : c'est une recherche négative. Une demande envoyée sans réponse : `statut: demandee`.
5. `./pq check`, `./pq build`.
