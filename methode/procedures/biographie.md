<!-- Procédure interne : utilisée par les commandes, pas une commande en soi. -->
# Procédure : écrire ou tenir à jour une biographie

Chaque personne a sa biographie dans `base/biographies/<id-de-la-personne>.md` : un récit en prose continue de
sa vie, sans références dans le texte. Les preuves et le degré de certitude vont **en marge**. Le site en fait
une page par personne (menu « Biographies ») ; dans la prose, le nom d'une personne qui a une biographie mène à
la sienne, ce qui permet de passer d'une vie à l'autre.

Quand l'appliquer : après une commande qui ajoute ou change un fait sur une personne, ou qui fait bouger la
confiance d'une question qui la concerne (`/test`, `/source`, `/explore`, `/challenge`) : reprends la
biographie de **chaque personne touchée**, et crée-la si elle n'existe pas. `./pq audit` signale les personnes
sans biographie.

## Avant d'écrire

Lance `./pq dossier <id>` : il donne la fiche de la personne (relations, synthèse), les assertions qui la
nomment avec leurs citations, et les questions qui la concernent (verdict, confiance). Lis aussi les
biographies déjà écrites de ses proches, pour que les récits s'accordent. Une personne mal connue a une biographie courte : un ou deux paragraphes valent mieux qu'un récit
délayé, et dire ce qu'on ignore fait partie du récit.

## Format

- Nom du fichier : l'id de la fiche personne (`base/biographies/guillaume-de-roquemaurel.md`).
- En-tête YAML : `titre` (le nom), `sous_titre` (une phrase : qui elle était, bornes connues), `mise_a_jour`
  (date du jour).
- Corps : paragraphes en français soigné, dans l'ordre de la vie. Liens vers les fiches avec libellé lisible
  (`[[arnaud-ii-de-roquemaurel|Arnaud de Roquemaurel]]`) : mets un lien à la première mention de chaque
  personne, lieu, famille ou événement. **Pas** de `[[source.aN]]` dans le texte courant.
- Note marginale : `{{<étiquette>|<commentaire court> [[source.aN|Libellé]]}}`, placée **après** la ponctuation
  de la phrase qu'elle qualifie. L'étiquette est :
  - une confiance (`etabli`, `probable`, `plausible`, `possible`, `improbable`, `refute`) quand le passage
    repose directement sur des assertions ;
  - `inconnu` quand le passage dit ce que les sources taisent ;
  - un id de question (`origine-de-gabrielle`) ou d'hypothèse (`origine-de-gabrielle#H1`) quand le passage
    dépend d'une question : la marge affiche alors la confiance **actuelle** de la question, sans rien recopier.
- Commentaire : une ou deux lignes au plus (d'où vient le fait, ce qui le limite), puis les preuves. Les notes
  longues décrochent de leur phrase dans la marge.

## Règles

1. Rien n'entre dans la biographie qui ne soit déjà dans une fiche (assertion, relation, verdict). La
   biographie résume la base ; elle n'est jamais une source.
2. L'étiquette ne dépasse pas la confiance de la relation ou du verdict correspondant dans la base.
3. Les citations reprises dans la prose sont verbatim, entre guillemets, telles que dans l'assertion.
4. Le doute s'écrit aussi dans la phrase (« semble-t-il », « peut-être », « à en croire Monluc ») quand la
   marge n'est pas `etabli` ou `probable`.
5. Chaque paragraphe porte au moins une note ; chaque note (sauf `inconnu`) cite au moins une preuve.
   `./pq check` le vérifie.
6. Mets à jour `mise_a_jour`, puis `./pq check` (0 erreur) et `./pq build`.
