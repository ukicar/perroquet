---
id: date-du-raid-des-cabannes
type: hypothese
nom: Date de la surprise des Cabannes
question: "Quel jour les troupes de Tilladet surprirent-elles les réfugiés de Pamiers aux Cabannes : le 25 mai 1567 (Crespin, Castillon) ou le 26 mai 1567 (Discours des troubles de Pamiers) ?"
sujets: [raid-des-cabannes-1567, les-cabannes, martin-tachard]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "La surprise eut lieu le matin du dimanche 25 mai 1567.", auteur: humain, confiance: possible}
  - {id: H2, enonce: "La surprise eut lieu à l'aube du lundi 26 mai 1567.", auteur: humain, confiance: possible}
  - {id: H3, enonce: "Autre date, ou indéterminable (par exemple marche de nuit du 25 au 26 que chaque récit date différemment).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: [H1, H2]
    attendu: "La procédure du parlement contre Tachard (interrogatoire du 8 juin, arrêt du 6 juillet 1567) rappelle la date de sa capture aux Cabannes."
    ou_chercher: "AD Haute-Garonne, 1 B 3457, arrêts criminels de la Tournelle du 2 juin à juillet 1567 (catalogue-ad31.a2)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H1
    attendu: "Olhagaray (1629), lu directement et non par Castillon, donne le 25 mai ; s'il dépend de Crespin, sa date ne compte pas comme témoin indépendant."
    ou_chercher: "Olhagaray, Histoire des comtes de Foix, Béarn et Navarre (1629), p. 561 env. (Gallica bpt6k53402668, vue 595)."
    diagnostique: faible
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: [H1, H2, H3]
    attendu: "Lafaille (Annales de Toulouse, t. II) ou l'Histoire générale de Languedoc donnent une date tirée d'une autre source (registres du parlement ou de Foix)."
    ou_chercher: "Lafaille, Annales de Toulouse, t. II, année 1567 ; Vic et Vaissète, nouv. éd., t. XI-XII (Gallica)."
    diagnostique: moyenne
    statut: indecidable
    resultat: "Recherche du 7 octobre 2026 bloquée (Gallica, HTTP 429). À relancer."
    preuves: [r-2026-10-07-gallica-lafaille-hgl]
    enquetes: []
matrice:
  - {preuve: crespin-histoire-des-martyrs.a2, H1: C, H2: I, H3: N, note: "Crespin : arrivée aux Cabannes le matin du 25 mai 1567."}
  - {preuve: discours-des-troubles-de-pamiers.a5, H1: I, H2: C, H3: N, note: "Discours de Pamiers (1567, contemporain) : surprise à l'aube du 26 mai 1567."}
  - {preuve: castillon-histoire-du-comte-de-foix.a2, H1: C, H2: N, H3: N, note: "Castillon (XIXe s.) donne le 25 mai, probablement d'après Crespin ou Olhagaray : non indépendant, pas compté contre H2."}
  - {preuve: crespin-histoire-des-martyrs.a5, H1: C, H2: C, H3: C, note: "« un vendredi 6 de juin » : le 6 juin 1567 (julien) est bien un vendredi (calcul d'agent). La chronologie de Crespin est précise, mais cela ne départage pas le 25 du 26."}
contestations: []
meneur: H3
confiance: possible
verdict: "Indéterminable en l'état (H3) : les témoins se contredisent. Crespin date la surprise du 25 mai 1567, le Discours des troubles de Pamiers, imprimé la même année, du 26. Castillon, qui dit le 25, dépend probablement de Crespin ou d'Olhagaray. Seule la procédure contre Tachard au parlement de Toulouse pourrait trancher."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche du 7 octobre 2026"}
sous_questions: []
---
## Les deux dates

- Crespin, *Histoire des martyrs* : les troupes arrivent aux Cabannes « le matin » du 25 mai 1567
  ([[crespin-histoire-des-martyrs.a2]]).
- *Discours des troubles advenus en la ville de Pamiers* (1567) : surprise « à l'aube » du 26 mai 1567, par quatre ou
  cinq cents arquebusiers et quarante chevaux ([[discours-des-troubles-de-pamiers.a5]]).
- Castillon d'Aspet, citant Olhagaray, donne le 25 mai ([[castillon-histoire-du-comte-de-foix.a2]]). Olhagaray (1629)
  et Castillon (XIXe siècle) peuvent dépendre de Crespin : on ne compte pas leur date comme un témoin de plus.

## Calendrier (calcul d'agent)

En calendrier julien, le 25 mai 1567 est un dimanche et le 26 un lundi. Le « vendredi 6 de juin » de Crespin, jour du
transfert de Tachard à Toulouse ([[crespin-histoire-des-martyrs.a5]]), tombe bien un vendredi, ce qui montre que ses
dates du procès sont soignées. Mais cela ne dit rien de la date du raid. Une marche de nuit commencée le 25 et une
surprise à l'aube du 26 réconcilieraient les deux textes (H3). C'est une simple possibilité, qu'aucune source n'appuie.

## Ce qui trancherait

La procédure contre Tachard (P1), si le registre de la Tournelle de juin-juillet 1567 la contient. Lafaille et
l'Histoire générale de Languedoc n'ont pas pu être lus ([[r-2026-10-07-gallica-lafaille-hgl]]).
