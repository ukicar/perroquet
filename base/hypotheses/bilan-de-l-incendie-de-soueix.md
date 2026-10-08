---
id: bilan-de-l-incendie-de-soueix
type: hypothese
nom: Bilan de l'incendie de Soueix
question: "Combien de personnes moururent dans l'attaque de Soueix (février 1567), et les deux prêtres sont-ils comptés parmi les « six autres personnes » de Monluc ?"
sujets: [incendie-de-soueix-1567, arnaud-ii-de-roquemaurel, soueix, arret-du-24-mai-1567]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Sept morts : Arnaud et six autres, les deux prêtres compris parmi ces six (soit quatre serviteurs ou chambrières).", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Les deux prêtres s'ajoutent aux six (ou sept) serviteurs et chambrières : neuf morts ou davantage.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Autre bilan : une partie des « précipités » survécut, ou d'autres victimes moururent ensuite, de sorte que le total n'est ni sept ni neuf.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "La liste des victimes de l'arrêt du 24 mai 1567 compte sept personnes, Arnaud et les deux prêtres compris."
    ou_chercher: "AD31 1 B 2103 (arrêts en double, avril-mai 1567, salle de lecture) ; Vuillier, Histoire de la famille de Mauléon (1998), p. 52 et suiv. ; copie AJR."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "L'arrêt nomme les deux prêtres à part d'une liste de six ou sept serviteurs et chambrières."
    ou_chercher: "Mêmes lieux que P1."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: [H1, H2]
    attendu: "Les collations de bénéfices du diocèse de Couserans en 1567 montrent deux cures ou chapellenies vacantes « per obitum » en février 1567, avec le nom des prêtres."
    ou_chercher: "AD Ariège, série G (évêché de Couserans), si les registres de collations subsistent."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "L'arrêt ou Vuillier mentionne des blessés survivants parmi les serviteurs « précipités », ou des morts postérieures."
    ou_chercher: "Mêmes lieux que P1."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a2, H1: CC, H2: I, H3: I, note: "« bruslé la maison, le dict Rocquemaurel et six autres personnes » : sept morts selon un contemporain, de seconde main, douze jours après."}
  - {preuve: site-roquemaurel.a4, H1: C, H2: C, H3: C, note: "Indemnités aux héritiers des deux prêtres et à ceux des serviteurs : confirme les deux catégories, pas leur nombre."}
  - {preuve: site-roquemaurel.a5, H1: I, H2: C, H3: C, note: "Six serviteurs et chambrières « précipités du haut du château » : s'ils sont tous morts, le total dépasse sept."}
  - {preuve: site-roquemaurel.a6, H1: C, H2: C, H3: C, note: "« La liste fait apparaître sept personnes, le texte dit six » : sept peut être Arnaud et six autres (H1) ou sept serviteurs (H2)."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Monluc, seul témoin contemporain, compte Arnaud et six autres morts ; le résumé de l'arrêt par le site familial distingue deux prêtres et six serviteurs « précipités », sans dire qu'ils sont tous morts. H1 (sept morts, prêtres compris) est la lecture la moins contredite, mais seule la liste de l'arrêt peut trancher."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Les comptes

- **Monluc** (Agen, 14 février 1567) : les assaillants ont « bruslé la maison, le dict Rocquemaurel et six
  autres personnes » [[monluc-lettres-ruble.a2]], soit sept morts. Monluc écrit de seconde main.
- **Le site familial**, résumant l'arrêt du 24 mai 1567 d'après une copie privée [[site-roquemaurel.a8]] :
  1 000 livres aux héritiers des « deux prêtres assassinés dans le château de Soueix », 500 livres à ceux des
  serviteurs et chambrières [[site-roquemaurel.a4]] ; six serviteurs et chambrières « précipités du haut du
  château » [[site-roquemaurel.a5]] ; et en note : « La liste fait apparaître sept personnes, le texte dit six »
  [[site-roquemaurel.a6]]. L'arrêt nomme donc les victimes.

## Raisonnement

Si les deux prêtres sont parmi les six de Monluc, les morts sont Arnaud, deux prêtres et quatre serviteurs
(H1) ; la liste de sept de l'arrêt peut alors être Arnaud et ses six compagnons. Si les six « précipités »
sont tous des serviteurs morts, il faut ajouter les prêtres (H2). Mais « précipités » ne veut pas dire
tués : H3 reste ouverte. Ces trois lectures de la note 28 du site sont également possibles.

**Inférence des notes** : « héritiers » suppose des prêtres séculiers (chapelains du château ou prêtres de la
paroisse de Soueix), non des réguliers. Leur nom n'apparaît dans aucun imprimé
([[r-2026-10-06-pretres-de-soueix]]).

Gabrielle et un enfant se jetèrent par une fenêtre [[monluc-lettres-ruble.a3]] ; voir [[sort-de-gabrielle-a-soueix]].
