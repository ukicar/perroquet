---
id: mort-de-soulan
type: hypothese
nom: Soulan est-il mort à Lunel en 1570
question: "Jean-François de Mauléon, sieur de Soulan, est-il mort à Lunel en 1570, comme le veut une tradition, ou plus tard ?"
sujets: [jean-francois-de-mauleon]
statut: tranchee
hypotheses:
  - {id: H1, enonce: "Il mourut à Lunel en 1570 (tradition).", auteur: agent, confiance: refute}
  - {id: H2, enonce: "Il était encore vivant le 5 juin 1571 et mourut plus tard, à une date et en un lieu inconnus.", auteur: humain, confiance: probable}
predictions:
  - id: P1
    h: H2
    attendu: "Un acte postérieur à 1570 montre Soulan agissant en personne."
    ou_chercher: "« Démembrement de la vicomté de Couserans », BSA (Gallica bpt6k5405682f), p. 57-58, d'après les papiers Sentein."
    diagnostique: haute
    statut: confirmee
    resultat: "Dernier accord de Jean-François de Mauléon avec les habitants de Soulan le 5 juin 1571."
    preuves: [demembrement-vicomte-couserans.a6]
    enquetes: []
  - id: P2
    h: H1
    attendu: "La tradition de Lunel repose sur un acte ou une chronique contemporaine datée de 1570."
    ou_chercher: "Source de la tradition à identifier (Vuillier 1998 ; généalogies des Mauléon)."
    diagnostique: moyenne
    statut: infirmee
    resultat: "La source retrouvée n'est pas un acte sur Soulan : c'est une conjecture des éditeurs des Huguenots en Bigorre (1883), qui rapprochent Solan du « Lalou beau-frère de Fontrailles » de La Popelinière, tué au siège de Lunel en 1570 (durier-carsalade-huguenots-en-bigorre.a6). La Popelinière parle de « la Louë », maréchal de camp, mort près de Montpellier la nuit du 1er avril 1570, sans le dire sieur de Soulan (la-popeliniere-1572.a1)."
    enquetes: []
  - id: P3
    h: H2
    attendu: "Le décret du 25 juin 1575 ou la procédure de 1576 qualifie Jean-François de « feu », ce qui borne sa mort avant 1575-1576 ; sinon il était encore vivant."
    ou_chercher: "Procès-verbal d'exécution du décret (AD31, registres des décrets, cote à identifier) ; papiers Sentein."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: demembrement-vicomte-couserans.a6, H1: II, H2: CC, note: "Vivant le 5 juin 1571 (accord avec les habitants de Soulan), d'après les papiers Sentein."}
  - {preuve: ad31-1b-74.a3, H1: N, H2: N, note: "En 1576, c'est Jean-Antoine de Mauléon, non Jean-François, qui s'oppose à l'exécution du décret : indice possible d'un décès avant 1576, sans plus."}
  - {preuve: roquemaurel-familles-du-midi.a2, H1: N, H2: C, note: "Soulan est dit « feu » dans la remontrance du 22 novembre 1603 : borne haute de sa mort (résumé non vérifié)."}
  - {preuve: demembrement-vicomte-couserans.a9, H1: N, H2: C, note: "Pièce du même 22 novembre 1603 : Marguerite de Béon « s'estoit emparée de toutz les biens dudit feu Jehan-Francoys de Mauléon » (lue par un agent, non relue)."}
  - {preuve: durier-carsalade-huguenots-en-bigorre.a6, H1: C, H2: I, note: "Conjecture d'éditeur (1883) : si Solan est « Lalou », il fut tué au siège de Lunel le 31 mars 1570. Ressemblance de noms (Lalous / Alos) seulement ; probable origine de la tradition."}
  - {preuve: la-popeliniere-1572.a1, H1: N, H2: N, note: "La Popelinière : « la Louë », maréchal de camp, beau-frère de Fonterailles, tué près de Montpellier le 1er avril 1570 ; ne nomme pas Soulan. Non diagnostique sans l'identification."}
  - {preuve: durier-carsalade-huguenots-en-bigorre.a4, H1: N, H2: N, note: "Soulan colonel à Ibos à l'été 1569 : vivant en 1569, ce que les deux hypothèses admettent."}
contestations: []
meneur: H2
confiance: probable
verdict: "La mort à Lunel en 1570 est contredite par l'accord que Soulan passe avec ses habitants le 5 juin 1571, rapporté par une étude fondée sur les papiers Sentein. Il est dit « feu » le 22 novembre 1603 : il mourut donc entre juin 1571 et novembre 1603, à une date et en un lieu inconnus. H2 est probable ; elle deviendra établie quand ces assertions auront été relues sur les pièces. La tradition de Lunel vient sans doute d'une conjecture d'éditeurs de 1883 qui confondaient Soulan avec « la Louë », maréchal de camp tué en 1570."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "deux lignes ajoutées ; borne haute 1603 ; confiance inchangée", cause: "propagation : roquemaurel-familles-du-midi.a2, demembrement-vicomte-couserans.a9"}
  - {date: "2026-10-26", changement: "P2 non_testee → infirmee ; trois lignes de matrice ; confiance inchangée (H2 probable)", cause: "origine de la tradition retrouvée : durier-carsalade-huguenots-en-bigorre.a6, la-popeliniere-1572.a1"}
sous_questions: []
---
## La réfutation de Lunel 1570

L'article « Démembrement de la vicomté de Couserans », fondé sur les papiers de la famille Sentein, fait de
Jean-François le fils unique de Raymond-Roger de Mauléon et de Marguerite de Lordat
[[demembrement-vicomte-couserans.a1]] et le montre vivant le 5 juin 1571, date d'un dernier accord avec les
habitants de Soulan [[demembrement-vicomte-couserans.a6]]. Il n'est donc pas mort à Lunel en 1570. La source de
la tradition de Lunel n'est pas identifiée dans les notes.

L'assertion n'est pas encore vérifiée par une seconde lecture : la question est tranchée, mais la confiance
reste « probable ».

## La date réelle

**Inférences, non des faits** :
- En 1576, l'opposant au décret est Jean-Antoine de Mauléon [[ad31-1b-74.a3]] ; Jean-François n'ayant pas
  d'enfant [[demembrement-vicomte-couserans.a5]], Jean-Antoine pourrait agir comme héritier, ce qui suggérerait
  un décès avant 1576. Il pourrait aussi agir pour son propre compte face à un condamné contumax.
- Les notes signalent qu'en 1603 Marguerite de Béon de Sère détenait les biens de « feu » Jean-François ; ce fait
  n'a pas de source identifiée et n'est pas utilisé.

Voir aussi [[supplique-de-soulan]] : sa supplique au roi est signifiée en mars 1570 ou 1571.

## D'où vient la tradition de Lunel (2026-10-26)

Les éditeurs des *Huguenots en Bigorre* rapprochent le capitaine Solan du « Lalou beau-frère de Fontrailles » de La
Popelinière, parce que Solan était seigneur d'Alos et que Montamat, un Fontrailles, avait épousé Isabeau de Solan ; ils
ajoutent que, si c'est le même homme, il fut tué au siège de Lunel dans la nuit du 31 mars 1570
[[durier-carsalade-huguenots-en-bigorre.a6]]. La Popelinière, relu sur son texte de 1572, parle de « la Louë »,
maréchal de camp, beau-frère de Fonterailles, tué en son quartier à une lieue de Montpellier la nuit du 1er avril 1570
[[la-popeliniere-1572.a1]] : il ne le rattache pas à Soulan. La tradition repose donc sur une identification
conjecturale, que l'accord du 5 juin 1571 contredit [[demembrement-vicomte-couserans.a6]]. Les mêmes éditeurs
montrent d'ailleurs Soulan vivant et colonel dans l'armée de Montgomery à l'été 1569
[[durier-carsalade-huguenots-en-bigorre.a4]] ([[campagne-de-montgomery-en-bigorre-1569]]).
