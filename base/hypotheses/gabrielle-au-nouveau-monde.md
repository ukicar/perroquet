---
id: gabrielle-au-nouveau-monde
type: hypothese
nom: Gabrielle au Nouveau Monde
question: "Où Gabrielle d'Espinas vécut-elle après 1567 : partit-elle pour le Nouveau Monde (une colonie française près de Rio de Janeiro), ou resta-t-elle dans le Midi ?"
sujets: [gabrielle-d-espinas, rio-de-janeiro]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Après 1567, Gabrielle partit pour le Nouveau Monde, dans une colonie française près de Rio de Janeiro.", auteur: humain, confiance: improbable}
  - {id: H2, enonce: "Elle resta dans le Midi (Couserans, Lézat, Toulouse), où elle poursuivit ses droits et mourut.", auteur: agent, confiance: plausible}
  - {id: H3, enonce: "Elle quitta le Midi pour un autre lieu que le Brésil (refuge protestant comme le Béarn ou Genève, ou autre région du royaume).", auteur: agent, confiance: possible}
  - {id: H4, enonce: "Elle mourut peu après 1567, ou son sort est indéterminable.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Un rôle d'embarquement, un contrat d'affrètement (Rouen, Le Havre, Honfleur, La Rochelle) ou une chronique portugaise de prises nomme Gabrielle ou une dame de Roquemaurel partant pour le Brésil après 1567."
    ou_chercher: "Gaffarel 1878 et ses sources portugaises (Varnhagen) ; notaires de Rouen et de La Rochelle (AD Seine-Maritime, AD Charente-Maritime, salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Des actes notariés du Couserans ou de Lézat postérieurs à 1567 (quittance, tutelle de son enfant, testament, remariage) la montrent présente dans le Midi."
    ou_chercher: "AD Ariège, série 5 E, notaires du Couserans et de Lézat (salle de lecture)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "Elle figure dans un registre de refuge protestant (Livre des habitants de Genève, registres réformés du Béarn) après 1567."
    ou_chercher: "Geisendorf, Livre des habitants de Genève (imprimé) ; registres consistoriaux du Béarn (AD Pyrénées-Atlantiques)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H4
    attendu: "Le procès de 1610 sur l'amende de 3 000 livres est mené par ses héritiers et la dit « feue » ; ou un acte de tutelle de son enfant la dit morte peu après 1567."
    ou_chercher: "AD Haute-Garonne, arrêts civils de 1610 (salle de lecture) ; notaires du Couserans (AD Ariège 5 E)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: gaffarel-1878.a2, H1: II, H2: N, H3: N, H4: N, note: "Les derniers forts français de la baie de Rio tombent en janvier 1566 (Gaffarel) ou 1567 : avant l'arrêt du 24 mai 1567, il n'y a plus de colonie où aller."}
  - {preuve: gaffarel-1878.a1, H1: I, H2: N, H3: N, H4: N, note: "Le fort Coligny, cœur de la France Antarctique, est démoli dès 1560."}
  - {preuve: gaffarel-1878.a4, H1: I, H2: N, H3: N, H4: N, note: "En 1568, les Français renoncent à s'établir au Brésil."}
  - {preuve: gaffarel-1878.a5, H1: C, H2: N, H3: N, H4: N, note: "Restent vers 1575 un comptoir à Rio Real et un dépôt d'armes au cap Frio : des postes de traite, non une colonie ; seul appui, faible, de H1."}
  - {preuve: bardies-1903.a2, H1: N, H2: C, H3: N, H4: N, note: "En mai 1567 elle plaide au Parlement de Toulouse : elle est dans le Midi et y défend ses biens."}
  - {preuve: site-roquemaurel.a7, H1: N, H2: C, H3: N, H4: C, note: "L'amende de 3 000 livres qui lui revenait est encore disputée en 1610 (par elle ou ses ayants droit) : intérêts toujours ancrés à Toulouse."}
  - {preuve: monluc-lettres-ruble.a6, H1: C, H2: N, H3: C, H4: N, note: "Monluc dit les Roquemaurel réformés : la France Antarctique avait attiré des huguenots, et un refuge protestant reste concevable. Indice faible et sans doute erroné (religion-des-roquemaurel)."}
  - {preuve: roquemaurel-familles-du-midi.a3, H1: N, H2: C, H3: N, H4: C, note: "Morte avant le 3 septembre 1603 (l'auteur écrit « 3 novembre », coquille ; voir la note de a3) ; c'est son neveu de Lézat qui hérite de ses droits : sa succession s'ouvre dans le Midi."}
  - {preuve: roquemaurel-familles-du-midi.a4, H1: I, H2: C, H3: I, H4: I, note: "Une Gabrielle d'Espinas marraine à Lézat en 1589 : si c'est elle, elle vit à Lézat 22 ans après l'incendie (homonymie possible)."}
  - {preuve: registres-paroissiaux-lezat.a8, H1: N, H2: N, H3: N, H4: N, note: "La marraine de 1589 n'est pas trouvée à la date donnée : la présence de Gabrielle à Lézat en 1589 n'est pas confirmée."}
  - {preuve: registres-paroissiaux-lezat.a11, H1: I, H2: C, H3: I, H4: I, note: "Une « madamoyselle Gabrielle d'Espinas » est marraine à Lézat en novembre 1587 et juin 1588 : si c'est elle, elle vit à Lézat vingt ans après l'incendie (identité non établie)."}
contestations: []
meneur: H2
confiance: plausible
verdict: "La colonie française de Rio n'existait plus quand Gabrielle devint veuve : son fort principal fut démoli en 1560 et ses derniers forts pris en janvier 1566 ou 1567. Rien ne la montre hors du Midi : elle plaide à Toulouse en mai 1567, son procès court jusqu'en 1603 et ses droits passent à un neveu de Lézat. H2 mène ; une « madamoyselle Gabrielle d'Espinas » est d'ailleurs marraine à Lézat en 1587 et 1588, peut-être elle."
historique:
  - {date: "2026-10-08", changement: "création", cause: "proposée par l'utilisateur"}
  - {date: "2026-10-08", changement: "deux lignes ajoutées ; confiance inchangée", cause: "généalogie de J. de Roquemaurel (arrêt de 1603, baptême de 1589)"}
  - {date: "2026-10-08", changement: "lignes ajoutées (registre de Lézat lu sur l'original)", cause: "registres-paroissiaux-lezat.a5, a8"}
  - {date: "2026-10-08", changement: "verdict réécrit ; confiance inchangée", cause: "propagation : catalogue-ad09.a1, roquemaurel-familles-du-midi.a2, registres-paroissiaux-lezat.a8"}
  - {date: "2026-10-08", changement: "ligne ajoutée ; confiance inchangée", cause: "registres-paroissiaux-lezat.a10, a11"}
sous_questions: []
---
## La chronologie rend H1 très difficile

La France Antarctique de Villegagnon, dans la baie de Rio, perdit sa place forte en mars 1560 : Mem de Sá prit le
fort Coligny et le fit démolir [[gaffarel-1878.a1]]. Les Français restés sur le continent avec leurs alliés
tamoyos tinrent encore deux forts jusqu'à l'attaque de janvier 1566 selon Gaffarel (janvier 1567 selon d'autres
auteurs, à vérifier) ; les survivants s'enfuirent [[gaffarel-1878.a2]] et Mem de Sá fonda Rio de Janeiro
[[gaffarel-1878.a3]]. Un retour en 1568 au cap Frio tourna court : les Français « avaient renoncé à s'établir au
Brésil » [[gaffarel-1878.a4]]. Ne subsistèrent que des postes de traite (Rio Real, dépôt d'armes du cap Frio vers
1575) [[gaffarel-1878.a5]].

Or Gabrielle devient veuve vers le 2 février 1567 et plaide à Toulouse en mai 1567 [[bardies-1903.a2]]. Au mieux,
la colonie tombait au moment même de l'incendie de Soueix ; ensuite il n'y avait plus de colonie où s'installer,
seulement des comptoirs de traite et de contrebande d'armes, lieux d'hommes, de marins et de truchements.

## Ce qui reste pour H1

- Les postes du cap Frio vers 1575 [[gaffarel-1878.a5]] : une présence française près de Rio, mais pas un
  établissement pour une veuve noble.
- La France équinoxiale du Maranhão (1612-1615), au nord du Brésil et loin de Rio, est trop tardive (Gabrielle aurait
  eu au moins soixante-dix ans) ; ce rapprochement n'est pas sourcé ici.
- La réputation réformée que Monluc prête aux Roquemaurel [[monluc-lettres-ruble.a6]] pourrait faire penser aux
  huguenots de Villegagnon, mais elle est sans doute erronée ([[religion-des-roquemaurel]]).

## Pour H2 et H4

Ses intérêts restent à Toulouse : elle obtient l'arrêt de 1567 [[bardies-1903.a2]] et l'amende qui lui revenait est
encore disputée en 1610 [[site-roquemaurel.a7]]. Cela ne dit pas si elle était vivante en 1610 (H4). Les notaires
du Couserans et de Lézat (P2) et l'arrêt de 1610 (P4) trancheraient : ce sont des démarches sur place.

## Recherche faite

Gaffarel ne nomme ni Roquemaurel, ni Espinas, ni le Couserans
([[r-2026-10-08-gaffarel-1878-gabrielle-les-espinas-ou-l]]).
