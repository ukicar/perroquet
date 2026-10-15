---
id: succession-de-soueix
type: hypothese
nom: Comment Guillaume devint seigneur de Soueix
question: "Pourquoi Guillaume de Roquemaurel, et non un fils d'Arnaud, est-il seigneur de Soueix dès mai 1567 ?"
sujets: [guillaume-de-roquemaurel, arnaud-ii-de-roquemaurel, gabrielle-d-espinas, soueix, jean-de-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Par la substitution du testament paternel de 1552, Arnaud étant mort sans fils survivant (le fils évoqué par le site mourut avant ou pendant l'incendie, ou n'exista pas).", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Guillaume porta le titre comme tuteur ou administrateur des biens d'un fils mineur d'Arnaud, encore vivant.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Guillaume acquit Soueix par un autre titre (achat, transaction avec la veuve, donation).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Le testament de Jean de Roquemaurel du 27 octobre 1552 substitue Guillaume à Arnaud si celui-ci meurt sans enfant mâle."
    ou_chercher: "Cabalby et Goudan, notaires de Vic (AD Ariège 5 E) ; BnF Pièces originales 2544 ; preuves de Malte de 1763."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "L'arrêt du 24 mai 1567 ou Vuillier 2000 mentionne la mort d'un enfant d'Arnaud, ou ne lui connaît aucun fils vivant."
    ou_chercher: "AD31 1 B 2103 ; Vuillier 1998 et 2000 ; copie AJR."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Des actes de 1567-1580 qualifient Guillaume de tuteur d'un fils d'Arnaud, ou montrent ce fils seigneur de Soueix à sa majorité."
    ou_chercher: "Notaires d'Oust et de Saint-Girons (AD Ariège 5 E) ; AD31 1 B, arrêts civils 1567-1587 (numérisés)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Un acte de vente, de transaction ou de donation de Soueix entre Gabrielle (ou un fils d'Arnaud) et Guillaume."
    ou_chercher: "Notaires du Couserans (AD Ariège 5 E) ; BnF Pièces originales 2544 (acte du 10 mai 1567)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a14, H1: CC, H2: C, H3: I, note: "Guillaume substitué à Arnaud dans le testament du père (27 octobre 1552)."}
  - {preuve: site-roquemaurel.a2, H1: I, H2: C, H3: N, note: "Arnaud et Gabrielle eurent « au moins un fils » : gêne H1 sauf si ce fils mourut avant Arnaud ou avec lui."}
  - {preuve: site-roquemaurel.a17, H1: C, H2: C, H3: C, note: "Guillaume est déjà seigneur de Soueix le 10 mai 1567, trois mois après l'incendie."}
  - {preuve: ad31-1b-74.a2, H1: C, H2: I, H3: C, note: "En 1576, Guillaume est encore « s.r de Suys » et agit en son nom propre : un pupille né avant 1567 approcherait de la majorité ; aucune mention de tutelle."}
  - {preuve: cabinet-d-hozier-298.a4, H1: C, H2: C, H3: N, note: "La supplique de Soulan est signifiée à Guillaume en 1570/71 : il représente les intérêts de la maison d'Arnaud."}
  - {preuve: roquemaurel-familles-du-midi.a6, H1: C, H2: I, H3: N, note: "Le généalogiste conjecture que l'enfant rescapé mourut peu après et fait succéder Guillaume par substitution : conjecture sans pièce, poids faible."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Guillaume est seigneur de Soueix dès mai 1567 et l'est encore en 1576 et en 1592-1594 ; le site familial attribue cette succession à une substitution dans le testament paternel de 1552, et le généalogiste de la famille conjecture que l'enfant rescapé mourut peu après. Cela suppose qu'Arnaud ne laissa pas de fils survivant : H1 est plausible, mais le sort de l'enfant reste inconnu ; ce sont les héritiers de Gabrielle (les Espinas), non un fils, qui poursuivent ses droits en 1603."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
  - {date: "2026-10-08", changement: "une ligne ajoutée ; confiance inchangée", cause: "roquemaurel-familles-du-midi.a6"}
  - {date: "2026-10-08", changement: "verdict réécrit ; confiance inchangée", cause: "propagation : roquemaurel-familles-du-midi.a6, a2 ; ad14-77f-627"}
sous_questions: [sort-de-gabrielle-a-soueix]
---
## Les faits

- Guillaume, second fils de Jean de Roquemaurel et de Catherine d'Ustou, fut substitué à son frère aîné Arnaud
  dans le testament de leur père du 27 octobre 1552 [[site-roquemaurel.a14]] ; le testament de 1552 est
  confirmé par le jugement de 1700, qui le dit mentionner Guillaume « l'un de ses fils » [[bnf-fr-32298.a6]].
- Le 10 mai 1567, Guillaume est déjà seigneur de Soueix [[site-roquemaurel.a17]] ; il l'est encore le
  6 juillet 1576 [[ad31-1b-74.a2]].
- Arnaud et Gabrielle eurent « au moins un fils » [[site-roquemaurel.a2]] ; lors de l'attaque, « sa femme et
  quelque enfant qu'il avoit se sont jetés par quelque fenestre » [[monluc-lettres-ruble.a3]].
- C'est à Guillaume, et non à Gabrielle, qu'est signifiée la supplique de Soulan [[cabinet-d-hozier-298.a4]].

## Raisonnement

Les notes expliquent la succession par la substitution de 1552. **Inférence de l'agent** : une substitution en
faveur d'un frère ne joue normalement que si l'héritier institué meurt sans enfant ; la présence d'un fils
d'Arnaud ferait alors obstacle. Il faut donc soit que ce fils soit mort (avant 1567, dans l'attaque ou juste
après), soit que l'information du site sur le fils soit erronée, soit que Guillaume n'ait été qu'administrateur
(H2), ce que dément le fait qu'il agisse en son nom propre en 1576. Le sort de l'enfant qui sauta par la fenêtre
avec Gabrielle est l'inconnue centrale.

Voir [[sort-de-gabrielle-a-soueix]] et [[bilan-de-l-incendie-de-soueix]].
