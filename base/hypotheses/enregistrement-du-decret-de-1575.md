---
id: enregistrement-du-decret-de-1575
type: hypothese
nom: Où fut enregistré le décret du 25 juin 1575
question: "Dans quel registre fut enregistré le décret du 25 juin 1575 adjugeant à Guillaume de Roquemaurel une part des biens de Soulan ?"
sujets: [decret-du-25-juin-1575, parlement-de-toulouse, guillaume-de-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Dans les registres propres aux décrets et saisies réelles du Parlement de Toulouse, tenus à part des registres d'arrêts.", auteur: humain, confiance: plausible}
  - {id: H2, enonce: "Dans les registres de la Chambre des Requêtes, rétablie en juin 1575.", auteur: agent, confiance: improbable}
  - {id: H3, enonce: "Ailleurs : autre chambre, minutes ou sacs seulement, ou recueil désigné par la référence « A.M.T tome II, p. 502 » du site familial.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Un registre des décrets ou des saisies réelles de 1575 contient, au 25 juin 1575, l'adjudication à Guillaume de Roquemaurel de la moitié de la part de Soulan sur Soulan, Erp, Araux et Régule."
    ou_chercher: "AD Haute-Garonne, série 1 B, registres de décrets / saisies réelles (cote à identifier dans le catalogue)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Les registres de la Chambre des Requêtes de 1575 contiennent le décret."
    ou_chercher: "AD Haute-Garonne, registres de la Chambre des Requêtes (cote à identifier)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H3
    attendu: "La référence « A.M.T tome II, p. 502 » désigne un recueil ou un fonds identifiable qui contient le décret."
    ou_chercher: "Site familial (page degres_couserans) ; hypothèse de lecture : Archives municipales de Toulouse, à vérifier."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: ad31-1b-72.a3, H1: C, H2: C, H3: C, note: "Le décret n'est pas copié dans le registre d'arrêts à la séance du 25 juin 1575 : attendu sous toutes les hypothèses."}
  - {preuve: ad31-1b-72.a5, H1: N, H2: C, H3: N, note: "La Chambre des Requêtes est rétablie en juin 1575."}
  - {preuve: ad31-1b-74.a5, H1: C, H2: I, H3: N, note: "« le decret obtenu de la Court par led. Roquemaurel » : décret de la Cour elle-même, non des Requêtes."}
  - {preuve: site-roquemaurel.a19, H1: C, H2: C, H3: C, note: "Contenu du décret donné par le site, sans cote d'archives identifiable."}
contestations: []
meneur: H1
confiance: plausible
verdict: "Le décret n'est pas dans le registre d'arrêts à sa date, et l'ordre d'exécution de 1576 le dit obtenu « de la Court ». L'hypothèse des notes, un enregistrement dans des registres de décrets tenus à part, est plausible ; la cote reste à trouver."
historique:
  - {date: "2026-10-08", changement: "création", cause: "migration des notes de recherche des 6-7 octobre 2026"}
sous_questions: []
---
## Recherches faites

La séance du samedi 25 juin 1575 du registre 1 B 72 (f. 178v-181v) a été lue : aucune entrée ne concerne
Roquemaurel, Soueix, Soulan ou Mauléon [[ad31-1b-72.a1]], [[ad31-1b-72.a2]], [[ad31-1b-72.a3]]
([[r-2026-10-06-ad31-1b-72-seance-du-25-juin-1575]]). Le décret est pourtant certain : l'ordre d'exécution du
6 juillet 1576 vise « le decret obtenu de la Court par led. Roquemaurel du xxv de Juing mil v.c lxxv »
[[ad31-1b-74.a5]] ([[r-2026-10-06-ad31-1b-74-ordre-d-execution-1576]]).

## Raisonnement

**Inférence des notes** : les décrets (ventes par décret de terres saisies) étaient enregistrés à part des arrêts.
La Chambre des Requêtes venait d'être rétablie (1 B 72, f. 147) [[ad31-1b-72.a5]], mais le décret est dit obtenu
« de la Court », ce qui désigne le Parlement plutôt que les Requêtes. Le site familial cite « A.M.T tome II,
p. 502 », référence non identifiée [[site-roquemaurel.a19]].
