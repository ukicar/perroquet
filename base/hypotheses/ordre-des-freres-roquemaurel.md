---
id: ordre-des-freres-roquemaurel
type: hypothese
nom: Ordre des frères Roquemaurel
question: "Lequel des fils de Jean de Roquemaurel et de Catherine d'Ustou était l'aîné : Arnaud (tué à Soueix en 1567), comme le dit l'histoire familiale, ou Girons, héritier d'Ustou et maréchal des logis de la compagnie du roi de Navarre ?"
sujets: [arnaud-ii-de-roquemaurel, girons-de-roquemaurel, guillaume-de-roquemaurel, jean-de-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Arnaud était l'aîné ; Guillaume, second fils, lui fut substitué dans le testament de 1552 ; Girons était un autre cadet.", auteur: agent, confiance: possible}
  - {id: H2, enonce: "Girons était l'aîné (l'« aîné » maréchal des logis du roi de Navarre dont parle Monluc) ; Arnaud, « le jeune Rocquemaurel », était un cadet.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "L'ordre est indéterminable : « le jeune » distingue Arnaud de son père, et l'« aîné » de Monluc désigne l'aîné vivant en 1567 ou un usage imprécis.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: [H1, H2]
    attendu: "Le testament de Jean de Roquemaurel du 27 octobre 1552 nomme ses fils dans l'ordre et désigne l'héritier universel."
    ou_chercher: "Notaires de Vic, Cabalby et Goudan (AD Ariège 5 E) ; copies dans BnF Pièces originales 2544 ou fr. 32298."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P2
    h: H2
    attendu: "Un acte des années 1550-1560 qualifie Girons de fils aîné, ou l'appelle « Roquemaurel » sans prénom comme chef de la maison."
    ou_chercher: "AD Ariège 1 J 94 ; actes d'Ustou (archives de Saint-Michel citées par Samiac)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: site-roquemaurel.a14, H1: C, H2: I, H3: N, note: "Le site dit Guillaume « second fils » substitué à « son frère aîné Arnaud » (testament de 1552), sans citer la pièce."}
  - {preuve: monluc-lettres-ruble.a8, H1: I, H2: C, H3: N, note: "« L'aîné Rocquemaurel » était maréchal des logis du feu roi de Navarre : ce n'est pas Arnaud, puisque Monluc oppose cet aîné au « jeune Rocquemaurel » tué."}
  - {preuve: samiac-bsa-1917-ustou.a3, H1: N, H2: C, H3: N, note: "Girons se dit en 1560 maréchal des logis de la compagnie du roi de Navarre : c'est l'aîné de Monluc. Lu par un agent, non relu."}
  - {preuve: monluc-lettres-ruble.a1, H1: N, H2: C, H3: C, note: "« le jeune Rocquemaurel » : cadet, ou simplement fils par rapport au père ; peu diagnostique."}
contestations: []
meneur: H3
confiance: possible
verdict: "Monluc distingue « l'aîné Rocquemaurel », maréchal des logis du roi de Navarre, du « jeune Rocquemaurel » tué à Soueix, et Samiac montre que ce maréchal des logis est Girons : Girons l'aîné et Arnaud cadet (H2) est la lecture la plus naturelle, mais l'histoire familiale fait d'Arnaud l'aîné, et « le jeune » peut seulement distinguer le fils du père. En l'état, la question est indécise (H3 mène par défaut) ; le testament de 1552 tranchera."
historique:
  - {date: "2026-10-08", changement: "création", cause: "propagation : inférence apparue en mettant à jour les biographies (samiac-bsa-1917-ustou.a3, monluc-lettres-ruble.a8)"}
sous_questions: []
---
Question ouverte lors de la mise à jour des biographies, pour que l'ordre des frères repose sur un verdict et non sur
une inférence glissée dans les récits. Monluc écrit que « l'aîné Rocquemaurel » avait été maréchal des logis du feu
roi de Navarre et appelle la victime « le jeune Rocquemaurel » [[monluc-lettres-ruble.a8]] [[monluc-lettres-ruble.a1]] ;
Samiac montre Girons, héritier d'Ustou, portant ce titre en 1560 [[samiac-bsa-1917-ustou.a3]]. L'histoire familiale
fait au contraire d'Arnaud l'aîné et de Guillaume le second fils, substitué à Arnaud en 1552
[[site-roquemaurel.a14]]. Le testament de 1552 (notaires de Vic) trancherait.
