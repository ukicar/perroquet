---
id: r-2026-10-26-corpus-noms-du-dossier
type: recherche
nom: "Corpus de livres choisis (thème, période, région) : noms du dossier"
date: '2026-10-26'
auteur: ukicar
outil: corpus (./pq search corpus ; texte existant des volumes archive.org, lu en local)
requete: 'Espinas | Despinas | Espinasse (avec Lézat, Cardonne, Gouzens, Caladr…, Roquemaurel, Gabrielle, Soueix, Couserans, Canals, Lastronques, Rochefort, Galauba) ; Roquemaurel (avec 1567, Soulan, Solan, Espinas, Gabrielle, Soueix, Fontraille, 1603, veuve) ; Gabrielle (avec Espinas, Despinas, Roquemaurel, Soueix, Caladr…) ; Soueix (avec 1567, incend…, brûl…, Solan, Soulan, Roquemaurel) ; Solan | Soulan (avec 1567, Mauléon, arrêt, Parlement) ; Caladrue | Caladroy | Caladroue'
perimetre: "corpus/livres.yaml : 23 ouvrages ou séries, 209 volumes (Lestrade, Castillon, Duclos, Histoire générale de Languedoc t. XI-XII, Gaches, Rabaud, de Ruble, Monluc, Dubédat, inventaires Haute-Garonne et Ariège, Du Bourg, O'Gilvy, Brémond, Archives historiques de la Gascogne, Revue de Comminges, Revue de Gascogne, Annales du Midi, Mémoires de la Société archéologique du Midi)"
resultat: negatif
resultats:
- titre: "Revue de Gascogne, vol. revuedegascognebullemen56 : « Messire Gaspard Despinas de Cardonne, habitant de Lézat » doit une rente à l'abbé de Lézat (XVIIIe s.)"
  url: https://archive.org/details/revuedegascognebullemen56
- titre: "Inventaire de l'Ariège (1894) : « demoiselle Anne d'Espinas, demeurant au château de Cardonne, juridiction de Montesquieu-Volvestre » donne ses biens à « noble Alexandre d'Espinas, son neveu » (date non relevée)"
  url: https://archive.org/details/inventairesomma00legrgoog
- titre: "Inventaire de l'Ariège (1894) : mars 1571, « frère Jean de Solan, prieur claustral » de l'abbaye ruinée de Combelongue"
  url: https://archive.org/details/inventairesomma00legrgoog
sources_creees: [durier-carsalade-huguenots-en-bigorre]
hypotheses: [origine-de-gabrielle]
---
Première recherche selon la méthode du corpus : on ne fouille pas tous les livres, seulement ceux qui peuvent
contenir quelque chose sur le dossier par leur thème (guerres de religion, Parlement de Toulouse, noblesse), leur
période (XVIe s.) ou leur région (Couserans, Comminges, comté de Foix, diocèse de Rieux, Toulousain). Leur texte
existant est téléchargé une fois dans `cache/texte/archive/`, puis lu en local ; on ne regarde que les passages où
deux termes se rencontrent (`--avec`), pour écarter les homonymes.

**Résultat pour la question.** Rien de nouveau sur Gabrielle d'Espinas ni sur la branche de Caladrue :
« Gabrielle » près d'Espinas, de Roquemaurel ou de Soueix, 0 ; « Caladrue », « Caladroy », « Caladroue », 0 dans les
209 volumes. Sur 1567, le corpus ne rend que les pièces déjà connues : les documents de Lestrade (requête du pays de
Comminges à Monluc, lettre sur la querelle de Solan et des Roquemaurel), la lettre de Monluc du 14 février 1567 et la
note de De Ruble dans les *Mémoires* de Jeanne d'Albret. Le silence de ces ouvrages régionaux sur Gabrielle et sur
Caladrue est lui-même une indication : la généalogie de Jacques de Roquemaurel ([[roquemaurel-familles-du-midi]])
reste la seule à les relier.

**Petites pistes, plus tardives** (non versées comme assertions : extraits non relus dans leur contexte) :
- Un Gaspard Despinas de Cardonne habite Lézat au XVIIIe siècle : les Espinas de Cardonne sont donc présents à Lézat,
  ce qui rapproche géographiquement les deux branches, mais deux siècles après les faits.
- Anne d'Espinas, au château de Cardonne, donne ses biens à son neveu Alexandre (date à relever dans l'inventaire de
  l'Ariège, déjà source de la base : [[inventaire-ad09-serie-b-1894]]).
- Un frère Jean de Solan, prieur de Combelongue en Couserans, en 1571 (même inventaire) : un Solan d'Église, à situer
  par rapport au sieur de Soulan.

**Contexte de la querelle de l'oiseau** (recherches complémentaires du même jour : Fontrailles près de 1566, Pamiers,
Solan ; oiseau, faucon, épervier près des noms des rivaux). Aucune autre source sur l'oiseau que Monluc et Crespin.
Mais une note des *Huguenots en Bigorre* replace Soulan dans son parcours de chef protestant du comté de Foix :
Pamiers tenu avec le jeune Fontrailles en 1566, présence probable dans l'armée de Montgomery en 1569
([[durier-carsalade-huguenots-en-bigorre]]).

**Suite.** Compléter le corpus quand un catalogue révèle un livre pertinent (ex. nouvelle série de Lestrade, bulletins
de la Société ariégeoise, si leur texte est sur archive.org).
