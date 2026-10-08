---
id: date-de-l-intervention-de-monluc
type: hypothese
nom: Commission et date de l'intervention de Monluc en 1567
question: "Quand Monluc vint-il en personne en Couserans et en Comminges en 1567 pour faire poser les armes à Soulan et aux Roquemaurel : dès la fin de mars ou en avril, comme le suggèrent ses lettres, ou seulement en mai, comme l'écrit Courteault ? Et de quand date sa commission royale ?"
sujets: [expedition-de-monluc-en-couserans-1567, blaise-de-monluc, charles-ix, saint-girons, saint-lizier, muret]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Monluc, déjà muni de la commission royale le 31 mars 1567, arrive en Couserans à la fin de mars ou en avril.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Monluc n'arrive en personne qu'en mai 1567 (Courteault), quelle que soit la date de la commission.", auteur: humain, confiance: possible}
  - {id: H3, enonce: "Monluc fit plusieurs séjours (avril et mai-juin), ou sa venue se place à une autre date ; indéterminable en l'état.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Le rôle de la taxe et ses pièces datent d'avril 1567 les étapes de Monluc et de son train (Aurignac, Saint-Lizier, Muret, montre de Muret)."
    ou_chercher: "Lestrade 1900, p. 42-45 (dates des articles du rôle) ; AM Muret, liasse 40."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Des lettres de Monluc d'avril 1567 sont datées d'Agen, d'Estillac ou d'ailleurs hors du Comminges, et les premières pièces datées du Couserans sont de mai."
    ou_chercher: "Monluc, Lettres, éd. Ruble, t. V (lettres d'avril-mai 1567, après la p. 86) ; source de Courteault 1909, p. 230-231 (« en mai »)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Les pièces de dépense distinguent un premier passage (compagnies, mars-avril) et un second passage de Monluc avec son train (mai-juin)."
    ou_chercher: "Rôle du 4 avril 1568 (Lestrade 1900, p. 42-46 ; AM Muret, liasse 40)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: [H1, H2, H3]
    attendu: "La commission royale (lettres de Charles IX chargeant Monluc de faire poser les armes à Soulan et aux Roquemaurel) est datée entre le 14 février et le 31 mars 1567."
    ou_chercher: "À localiser : lettres de Charles IX de février-mars 1567 (BnF, fonds français) ; copies dans les registres des États de Comminges (AM Muret, liasse 40) ou dans les registres du parlement de Toulouse."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a14, H1: C, H2: C, H3: C, note: "14 février 1567 : Monluc propose une expédition et une levée par Tilladet ; il n'est pas encore parti. Non diagnostique."}
  - {preuve: monluc-lettres-ruble.a16, H1: C, H2: I, H3: C, note: "31 mars 1567 : il demande deux canons aux capitouls « pour marcher contre Solan et Fonterailles » : départ imminent."}
  - {preuve: monluc-lettres-ruble.a17, H1: C, H2: N, H3: C, note: "31 mars 1567 : la querelle du haut Comminges, « où le Roy m'envoya » : la commission est déjà donnée."}
  - {preuve: courteault-1909.a1, H1: I, H2: C, H3: C, note: "Courteault : « en mai, il fut obligé d'aller lui-même » ; historien sérieux mais sans source citée dans les notes (crédibilité 3)."}
  - {preuve: discours-des-troubles-de-pamiers.a3, H1: C, H2: N, H3: C, note: "La commission est « exécutée » avant la surprise des Cabannes (25/26 mai) : facile sous H1, serré mais possible sous H2."}
  - {preuve: lestrade-1900.a8, H1: C, H2: C, H3: C, note: "Ordonnance du 11 juillet : « nostre venue » à Saint-Girons et Saint-Lizier, sans date. Non diagnostique."}
  - {preuve: lestrade-1900.a13, H1: C, H2: C, H3: C, note: "Dépenses de Monluc et de son train à Aurignac, Saint-Lizier et Muret, sans date dans l'assertion. Non diagnostique."}
  - {preuve: noulens-1863.a6, H1: N, H2: C, H3: C, note: "8 avril 1567 : Saint-Orens, probable chef des compagnies, assiste à un contrat de mariage de la famille du Bouzet (lieu non précisé) ; léger indice que les troupes n'étaient pas encore en Couserans."}
contestations: []
meneur: H3
confiance: possible
verdict: "Indécis. Le 31 mars 1567, Monluc a déjà sa commission et s'apprête à marcher ; Courteault place sa venue en mai sans source connue. Le calcul ACH met en tête l'hypothèse de plusieurs séjours, seulement parce qu'elle s'accorde avec tout ; aucune pièce ne l'appuie. Les dates des articles du rôle de 1568 et les lettres d'avril-mai 1567 devraient trancher."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les deux datations

- Monluc au roi, 14 février 1567 : il demande des troupes, de l'artillerie et le rasement des maisons de Fontrailles et
  de Soulan, et propose de faire lever des hommes par le capitaine Tilladet ([[monluc-lettres-ruble.a14]],
  [[monluc-lettres-ruble.a15]]).
- Monluc aux capitouls de Toulouse, 31 mars 1567 : il demande deux canons « pour marcher contre Solan et Fonterailles »
  et écrit que le roi l'a envoyé au haut Comminges ([[monluc-lettres-ruble.a16]], [[monluc-lettres-ruble.a17]]). La
  commission royale est donc antérieure au 31 mars. Elle n'est pas publiée par Ruble.
- Courteault (1909) : « en mai, il fut obligé d'aller lui-même », avec trois compagnies de gens d'armes et quatre cents
  arquebusiers ([[courteault-1909.a1]]).

## Comment lire ces pièces

La lettre du 31 mars annonce un départ, elle ne le prouve pas. Les canons ont pu tarder, comme Monluc lui-même, ce qui
s'accorderait avec Courteault. La commission était « exécutée » avant la surprise des Cabannes, à la fin de mai
([[discours-des-troubles-de-pamiers.a3]]) ; cela laisse peu de temps sous H2, mais ce n'est pas impossible. Le
8 avril 1567, Saint-Orens est présent à un contrat de mariage des du Bouzet ([[noulens-1863.a6]]). Si le lieu était
loin du Couserans, cela suggérerait que les compagnies n'y étaient pas encore. C'est une **inférence** fragile, car le
lieu de l'acte n'est pas connu.

L'ordonnance du 11 juillet 1567 parle de « nostre venue » à Saint-Girons et Saint-Lizier ([[lestrade-1900.a8]]), et le
rôle de 1568 enregistre les dépenses de Monluc et de son train ([[lestrade-1900.a13]]). Mais les assertions de la base
ne donnent pas les dates de ces articles. C'est là que se trouve le test le plus direct (P1, P3).

## Meneur

Le calcul ACH met H3 en tête parce que cette hypothèse vague ne contredit aucune pièce, pas parce qu'une pièce l'appuie.
On la garde comme meneur calculé, avec une confiance seulement « possible ».
