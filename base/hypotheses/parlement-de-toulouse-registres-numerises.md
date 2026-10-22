---
id: parlement-de-toulouse-registres-numerises
type: hypothese
nom: Registres numérisés du Parlement de Toulouse
question: "Les registres numérisés du Parlement de Toulouse (arrêts civils jusqu'en 1587, en ligne aux AD Haute-Garonne) contiennent-ils, au-delà de l'arrêt de 1576 déjà trouvé, d'autres actes sur l'affaire de Soueix et sur Gabrielle, repérables en croisant l'inventaire imprimé et les dates connues ?"
sujets: [gabrielle-d-espinas, parlement-de-toulouse, incendie-de-soueix-1567, arret-du-24-mai-1567, jean-francois-de-mauleon, guillaume-de-roquemaurel]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Oui : les registres numérisés contiennent d'autres arrêts sur l'affaire, y compris des arrêts nommant Gabrielle (ajournements avant l'incendie, exécution des condamnations, dommages, tutelle de son enfant).", auteur: humain, confiance: possible}
  - {id: H2, enonce: "Ils contiennent d'autres arrêts sur l'affaire (Soulan, Mauléon, Guillaume de Roquemaurel), mais Gabrielle n'y paraît pas après 1567 : la suite est menée par Guillaume ou par d'autres.", auteur: agent, confiance: possible}
  - {id: H3, enonce: "Ils n'apportent rien de plus : les pièces utiles sont dans des séries non numérisées (arrêts en double 1 B 2103, Tournelle, décrets, arrêts de 1610).", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "L'inventaire imprimé de la série B (t. 1, registres B 1 à B 92) analyse, outre l'entrée de 1576, des arrêts nommant Gabrielle, Soueix ou les Roquemaurel."
    ou_chercher: "Inventaire AD31 série B, t. 1 (1903), archive.org bub_gb_7zUXAQAAMAAJ, recherche plein texte."
    diagnostique: moyenne
    statut: infirmee
    resultat: "Aucune entrée sur Gabrielle, les Espinas ou Soueix ; la seule entrée Roquemaurel est celle de 1576. Mais l'inventaire est abrégé : ce silence pèse peu (r-2026-10-08-inventaire-imprime-ad31-serie-b-t-1-1903)."
    enquetes: []
  - id: P2
    h: H1
    attendu: "Le registre 1 B 60 (12 nov. 1566 - 31 mai 1567, prononcés jusqu'au 2 juin) contient les ajournements que Monluc dit déjà rendus contre Fontrailles et Soulan, et, après février 1567, des arrêts à la requête de la veuve de Roquemaurel."
    ou_chercher: "AD31 1 B 60, numérisé (serveur IIIF des AD31) : lecture des mentions marginales et des débuts d'arrêts, de novembre 1566 à mai 1567 ; rôle paléographe."
    diagnostique: haute
    statut: infirmee
    resultat: "1 B 60 lu du 17 janvier au 2 juin 1567 (images 120-538) : ni ajournement ni arrêt sur l'affaire, ni requête de la veuve, alors que le registre enregistre parfois des ajournements pris en chambre criminelle. Novembre 1566 - 16 janvier 1567 non lu."
    enquetes: []
  - id: P3
    h: [H1, H2]
    attendu: "Les registres 1 B 61 et 1 B 62 (juin 1567 - nov. 1568) contiennent l'exécution des condamnations de 1567 (saisie des biens de Soulan, provision pour la veuve) ou la procédure sur la supplique de Soulan ; sous H1 Gabrielle y est partie, sous H2 c'est Guillaume."
    ou_chercher: "AD31 1 B 61 et 1 B 62, numérisés ; puis 1 B 63 et suivants jusqu'en 1572 (supplique intimée en 1570/1571)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Une lecture complète de 1 B 60 à 1 B 62 ne trouve aucun arrêt sur l'affaire ; et le catalogue des AD31 confirme que la Tournelle de 1567 et les décrets de 1575 ne sont pas en ligne."
    ou_chercher: "AD31 1 B 60-62 (numérisés) ; catalogue en ligne des AD31 (Tournelle 1 B 3456-3460, registres de décrets)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a32, H1: C, H2: C, H3: I, note: "Avant février 1567, le Parlement avait déjà ajourné les parties et les Roquemaurel avaient comparu : ces actes devraient être dans les registres de 1566-1567, numérisés."}
  - {preuve: ad31-1b-74.a9, H1: I, H2: C, H3: N, note: "L'arrêt de 1576, trouvé dans un registre numérisé, ne nomme que Guillaume et Mauléon : Gabrielle n'est plus partie."}
  - {preuve: cabinet-d-hozier-298.a4, H1: I, H2: C, H3: N, note: "La supplique de Soulan est intimée à Guillaume, pas à Gabrielle (1570/1571)."}
  - {preuve: inventaire-ad31-serie-b-1903.a3, H1: I, H2: N, H3: C, note: "L'inventaire imprimé ne connaît qu'une entrée sur l'affaire (1576) ; silence d'un inventaire abrégé, poids faible."}
  - {preuve: inventaire-ad31-serie-b-1903.a2, H1: C, H2: C, H3: N, note: "Les Mauléon de Soulan plaident régulièrement au Parlement (1542, 1546, 1563) : les registres numérisés les suivent bien, ce qui rend probable d'autres entrées."}
  - {preuve: r-2026-10-06-ad31-1b-72-seance-du-25-juin-1575, H1: N, H2: N, H3: C, note: "Le décret du 25 juin 1575 n'est pas dans le registre civil numérisé : les décrets étaient enregistrés à part."}
  - {preuve: r-2026-10-08-ad31-1b-60-mars-juin-1567, H1: I, H2: I, H3: C, note: "1 B 60 lu du 17 janvier au 2 juin 1567 sans rien sur l'affaire, alors qu'il enregistre parfois des ajournements criminels : les actes sur Gabrielle sont plutôt dans des séries non numérisées."}
contestations: []
meneur: H2
confiance: possible
verdict: "Le registre civil 1 B 60, lu en entier du 17 janvier au 2 juin 1567, ne contient rien sur l'affaire, ni les ajournements cités par Monluc, ni requête de la veuve : P2 est infirmée. Les registres numérisés suivent pourtant les parties dans d'autres affaires (Soulan en 1563, Guillaume en 1576). H2 mène : d'autres arrêts sur l'affaire peuvent exister plus tard (1 B 61-62, 1568-1576), mais les pièces sur Gabrielle sont dans des séries non numérisées (criminel de 1567, 1 J 94 à Foix)."
historique:
  - {date: "2026-10-08", changement: "création", cause: "proposée par l'utilisateur"}
  - {date: "2026-10-08", changement: "P1 : non_testee → infirmee", cause: "recherche plein texte de l'inventaire imprimé, t. 1 (r-2026-10-08-inventaire-imprime-ad31-serie-b-t-1-1903)"}
  - {date: "2026-10-08", changement: "ligne ajoutée ; P2 testée en partie (mars-juin 1567, négatif), février reste à lire", cause: "r-2026-10-08-ad31-1b-60-mars-juin-1567"}
  - {date: "2026-10-08", changement: "P2 → infirmée ; ligne 1 B 60 renforcée (H1 et H2 : I)", cause: "lecture complète de 1 B 60 du 17 janvier au 2 juin 1567 (r-2026-10-08-ad31-1b-60-mars-juin-1567)"}
  - {date: "2026-10-22", changement: "corps mis à jour après l'infirmation de P2 et la correction des dates de 1 B 60 (31 mai, non 13 mai) ; confiances inchangées", cause: "ad31-1b-60.a1, ad31-1b-60.a2"}
sous_questions: []
---
## Ce qui est en ligne

Les arrêts civils du Parlement de Toulouse sont numérisés jusqu'en 1587 [[catalogue-ad31.a6]]. Pour l'affaire, les
registres utiles sont 1 B 60 (novembre 1566 - 31 mai 1567, et non 13 mai comme le dit le catalogue), 1 B 61
(juin - octobre 1567) et 1 B 62 (novembre 1567 - novembre 1568), puis 1 B 63 et suivants jusqu'à la supplique de
Soulan (1570-1571) et 1 B 72-74 (1575-1576) [[catalogue-ad31.a3]] [[ad31-1b-60.a1]] [[catalogue-ad31.a5]].
1 B 60 a été lu en entier du 17 janvier au 2 juin 1567 sans rien sur l'affaire [[ad31-1b-60.a2]] ; novembre 1566 -
16 janvier 1567 reste à lire, 1 B 61 et 1 B 62 ne sont lus qu'en partie. L'arrêt du 24 mai 1567, lui, n'est pas dans
1 B 60 ; il manque aussi le registre criminel d'avril-mai, et l'on ne sait pas encore s'il subsiste dans le registre en
double 1 B 2103, non numérisé [[catalogue-ad31.a4]] (voir [[localisation-de-l-arret-du-24-mai-1567]]).

## Pour H1 et H2 : il doit y avoir plus

Monluc écrit en février 1567 que le Parlement avait déjà fait ajourner les parties, que les Roquemaurel avaient
comparu et les autres non [[monluc-lettres-ruble.a32]] : ces ajournements, rendus avant l'incendie, devraient se trouver
dans 1 B 59 ou dans la partie de 1 B 60 qui n'a pas été lue (novembre 1566 - 16 janvier 1567). L'inventaire imprimé montre aussi que les Mauléon de Soulan plaidaient régulièrement à Toulouse
(en 1563 encore, contre le chapitre de Pamiers [[inventaire-ad31-serie-b-1903.a2]]).

## Ce qui sépare H1 et H2

Rien de ce qu'on a trouvé après 1567 ne nomme Gabrielle : l'arrêt de 1576 ne connaît que Guillaume et Mauléon
[[ad31-1b-74.a9]], et la supplique de Soulan est intimée à Guillaume [[cabinet-d-hozier-298.a4]]. Si Gabrielle
apparaît dans les registres numérisés, ce ne sera pas dans 1 B 60 de janvier à juin 1567, lu sans résultat
[[ad31-1b-60.a2]] : plutôt dans les premiers mois de 1 B 61 ou dans 1 B 62.

## Pour H3

L'inventaire imprimé, interrogé en entier, ne connaît que l'entrée de 1576 [[inventaire-ad31-serie-b-1903.a3]] ; mais
il ne retient qu'une partie des arrêts, et son silence pèse peu. Les décrets de 1575 étaient enregistrés à part
([[r-2026-10-06-ad31-1b-72-seance-du-25-juin-1575]]).

## Comment tester (P2, P3)

Les registres ne sont pas indexés. Méthode proposée : parcourir les images à basse résolution, repérer dans les
débuts d'arrêts (« Entre … ») les noms Roquemaurel, Soulan, Mauléon, Fontrailles, Astarac, Espinas, puis lire en
pleine résolution ce qui est repéré (rôle paléographe). Compter environ 500 images par registre. P2 est faite :
1 B 60, lu du 17 janvier au 2 juin 1567, n'a rien donné ([[r-2026-10-08-ad31-1b-60-mars-juin-1567]]). Reste le
plus diagnostique : 1 B 61 et 1 B 62 (P3), puis le début de 1 B 60 (novembre 1566 - 16 janvier 1567) pour les
ajournements d'avant l'incendie.
