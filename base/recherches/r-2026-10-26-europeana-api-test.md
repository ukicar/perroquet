---
id: r-2026-10-26-europeana-api-test
type: recherche
nom: "Europeana : test de l'API (catalogue et presse plein texte) sur les noms du dossier"
date: '2026-10-26'
auteur: ukicar
outil: Europeana Search API (api.europeana.eu/record/v2) et API plein texte de la presse (newspapers.eanadev.org)
requete: 'Roquemaurel | Espinas | Despinas | Soueix | Couserans | Soulan | Caladroy | Cardonne | Mauléon AND Couserans | Rochefort AND Lézat | Caladroy OR Caladrue | Montesquieu-Volvestre | Couserans AND 1567 | Comminges AND généalogie ; presse : Roquemaurel, Espinas Cardonne, Soueix Couserans'
perimetre: "métadonnées de tout Europeana (dont notices Gallica et descriptions détaillées des manuscrits BnF) ; plein texte des journaux numérisés (surtout autrichiens, néerlandais, allemands, XIXe-XXe s.)"
resultat: negatif
resultats:
- titre: "BnF, Périgord 159 (Dossiers de Lespine, XLIII) : contient un dossier généalogique « Roquemaurel »"
  url: https://gallica.bnf.fr/ark:/12148/btv1b10034148k
- titre: "BnF, Clairambault 1068 : mémoire imprimé pour Claude-Françoise de Foix de Mauléon, vicomtesse de Couserans (XVIIe s., hors sujet)"
  url: https://gallica.bnf.fr/ark:/12148/btv1b9000863k
sources_creees: []
hypotheses: []
---
Une première série de 30 requêtes, lancée le 24 octobre par un script (`tools/europeana-search.sh`, supprimé depuis),
avait déjà donné le même constat : aucun document du XVIe siècle pertinent. L'API fonctionne avec la clé du projet (rangée dans `tools/.europeana-key`, ignorée par git). L'ancienne adresse
`www.europeana.eu/api/v2` redirige (301) vers `api.europeana.eu/record/v2`.

**Ce qu'Europeana interroge réellement.** La recherche porte sur les **métadonnées** (titre, auteur, sujets,
description), pas sur le texte des livres. Pour la France, ce sont pour l'essentiel les notices de Gallica : un
livre qui parle des Roquemaurel sans les nommer dans son titre n'apparaît pas. Pour les manuscrits numérisés de la
BnF, en revanche, la notice reprend le détail du contenu (« Contient : … ») : c'est le seul apport propre constaté.
Par défaut, plusieurs mots sont reliés par OU (« Espinas Cardonne » : 1 014 réponses) ; il faut écrire `AND`.
L'API plein texte de la presse ne couvre pas la presse française de Gallica : pour « Roquemaurel », 7 articles
(1823-1853), tous sur l'officier de marine du XIXe s.

**Résultats.** Rien sur Gabrielle d'Espinas, Soueix, Caladroy/Caladrue, Lézat, ni sur 1567 en Couserans. « Espinas »
ne ramène que les auteurs Alfred et Georges Espinas (XIXe-XXe s.) et des titres espagnols (*espinas* = épines).
« Soulan » : la monographie de Biros (1974), déjà connue par Gallica. Une seule piste nouvelle, faible : le recueil
Périgord 159 de la BnF (dossiers de l'abbé de Lespine) contient un dossier « Roquemaurel ». Rien n'indique qu'il
s'agisse des Roquemaurel du Couserans plutôt que d'une famille homonyme du Périgord ; non consulté.

**Suite.** Europeana n'apporte rien que Gallica ne donne déjà, sauf la recherche dans le contenu détaillé des
manuscrits BnF numérisés. Inutile de relancer des requêtes générales. Si l'on veut la piste Lespine : lire sur
Gallica le dossier « Roquemaurel » de Périgord 159 (vues à repérer) pour voir s'il concerne le Couserans.
