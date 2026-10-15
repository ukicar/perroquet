---
id: monluc-et-gabrielle
type: hypothese
nom: Monluc et Gabrielle
question: "Existait-il un lien personnel (parenté, clientèle, protection) entre Blaise de Monluc et Gabrielle d'Espinas, ou la mention de « la pouvre femme » dans sa lettre au roi du 14 février 1567 relève-t-elle seulement de sa charge de lieutenant général en Guyenne ?"
sujets: [gabrielle-d-espinas, blaise-de-monluc, arnaud-ii-de-roquemaurel, famille-de-roquemaurel, incendie-de-soueix-1567, expedition-de-monluc-en-couserans-1567]
statut: ouverte
hypotheses:
  - {id: H1, enonce: "Gabrielle (ou sa famille d'origine) était une protégée de Monluc : un lien personnel explique qu'il parle d'elle et qu'il intervienne.", auteur: humain, confiance: improbable}
  - {id: H2, enonce: "Aucun lien personnel : Monluc parle d'elle dans un rapport officiel au roi, comme lieutenant général chargé de l'ordre en Guyenne ; l'atteinte à la veuve sert à montrer la gravité des désordres et à obtenir troupes et artillerie contre Fontrailles et Soulan.", auteur: agent, confiance: probable}
  - {id: H3, enonce: "Monluc n'a pas de lien avec Gabrielle elle-même, mais avec les Roquemaurel (réseau de l'aîné, ancien maréchal des logis du roi de Navarre, ou Guillaume), ce qui explique son intérêt pour l'affaire.", auteur: agent, confiance: possible}
predictions:
  - id: P1
    h: H1
    attendu: "Les lettres publiées de Monluc reviennent sur la veuve de Roquemaurel (recommandation, dommages, garde) après février 1567."
    ou_chercher: "Monluc, lettres, éd. Ruble, t. IV-V (index « Roquemaurel », « Espinas »)."
    diagnostique: haute
    statut: infirmee
    resultat: "L'édition Ruble ne mentionne les Roquemaurel que dans la lettre du 14 février 1567 (index : « querelle avec les Roquemaurel, 78 ») ; aucune autre lettre ne parle de la veuve."
    enquetes: []
  - id: P2
    h: H1
    attendu: "Une lettre inédite de Monluc, ou un acte où il intervient (sauvegarde, recommandation au Parlement, témoin d'un acte de Gabrielle ou des Espinas), montre un lien personnel."
    ou_chercher: "Lettres inédites de Monluc (BnF, fonds français, coll. Harlay Saint-Germain fr. 320 et 323) ; procédure de l'arrêt du 24 mai 1567 (AD31 1 B 2103, salle de lecture) ; production des Espinas devant Bezons (AD Tarn-et-Garonne, série C, vers C 87)."
    diagnostique: haute
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P3
    h: H2
    attendu: "Dans la même correspondance, Monluc rapporte au roi d'autres violences contre des particuliers qu'il ne connaît pas, dans les mêmes termes, pour appuyer des demandes de troupes ; et la veuve n'y est jamais nommée."
    ou_chercher: "Monluc, lettres, éd. Ruble, t. IV-V (lettres au roi de 1562-1570)."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
  - id: P4
    h: H3
    attendu: "Un Roquemaurel (Girons l'aîné, Guillaume) apparaît au service de Monluc ou dans son entourage (compagnie, commission, lettre) avant ou après 1567."
    ou_chercher: "Monluc, Commentaires et lettres, éd. Ruble ; Cabinet d'Hozier 298 et Dossiers bleus 581 (états de service des Roquemaurel) ; rôles de compagnies 1560-1570."
    diagnostique: moyenne
    statut: non_testee
    resultat: null
    enquetes: []
matrice:
  - {preuve: monluc-lettres-ruble.a3, H1: I, H2: C, H3: C, note: "Monluc ne la nomme pas : « sa femme », « la pouvre femme ». Un protecteur aurait vraisemblablement donné son nom."}
  - {preuve: monluc-lettres-ruble.a5, H1: C, H2: C, H3: C, note: "Indignation réelle, mais l'information est de seconde main (« l'on m'a mandé ») ; compatible avec tout, non diagnostique."}
  - {preuve: monluc-lettres-ruble.a6, H1: I, H2: C, H3: I, note: "Il croit les Roquemaurel réformés, ce que tout le reste contredit (religion-des-roquemaurel) : il les connaît mal."}
  - {preuve: monluc-lettres-ruble.a14, H1: I, H2: C, H3: I, note: "Il insiste sur la neutralité des troupes, levées hors du pays : posture d'arbitre, pas de protecteur d'une partie."}
  - {preuve: monluc-lettres-ruble.a8, H1: N, H2: C, H3: C, note: "L'aîné Roquemaurel servit le roi de Navarre : un réseau de cour possible, qui ne passe pas par Gabrielle."}
  - {preuve: monluc-lettres-ruble.a31, H1: N, H2: C, H3: N, note: "Il avait d'abord envoyé le vice-sénéchal : procédure ordinaire de maintien de l'ordre."}
  - {preuve: monluc-lettres-ruble.a17, H1: N, H2: C, H3: N, note: "« querelle particulière… où le Roy m'envoya » : mission royale."}
  - {preuve: monluc-lettres-ruble.a32, H1: N, H2: C, H3: C, note: "Il décrit l'affaire en juriste de l'ordre public : les Roquemaurel comparaissent, les autres non."}
  - {preuve: bardies-1903.a2, H1: N, H2: C, H3: N, note: "Gabrielle obtient justice au Parlement avec le procureur général, sans trace d'intervention de Monluc."}
  - {preuve: r-2026-10-08-monluc-commentaires-ed-ruble-t-3-mention, H1: N, H2: C, H3: N, note: "Les Commentaires (t. I-III) ne racontent pas l'affaire de Soueix : Monluc n'en parle pas dans son histoire, seulement dans une lettre au roi."}
contestations: []
meneur: H2
confiance: probable
verdict: "Monluc ne parle de Gabrielle que dans une lettre au roi, sans la nommer, d'après ce qu'on lui a rapporté ; ses Commentaires n'en disent rien et aucune autre lettre publiée ne revient sur elle. Le passage s'explique par sa charge : il rend compte d'une guerre privée et appuie une demande de troupes. Aucun indice de lien personnel ; reste à voir les lettres inédites et les pièces de procédure."
historique:
  - {date: "2026-10-08", changement: "création", cause: "proposée par l'utilisateur"}
sous_questions: []
---
## Le point de départ

L'utilisateur s'étonne qu'un chef militaire de ce rang « écrive dans l'histoire » au sujet d'une femme du Midi.
Il faut d'abord préciser ce que Monluc a écrit. Il n'en parle **pas dans ses Commentaires**, qui sont son œuvre
d'histoire : les tomes I-III de l'édition Ruble ne mentionnent ni Soueix, ni les Roquemaurel, ni Soulan
([[r-2026-10-08-monluc-commentaires-ed-ruble-t-1-mention]], [[r-2026-10-08-monluc-commentaires-ed-ruble-t-2-mention]],
[[r-2026-10-08-monluc-commentaires-ed-ruble-t-3-mention]]). Il en parle **une seule fois**, dans une lettre au roi
écrite à Agen le 14 février 1567, publiée par Ruble parmi ses lettres.

## Ce que dit la lettre

C'est un rapport de lieutenant général. Monluc expose une guerre privée entre Fontrailles et Soulan d'une part et
les Roquemaurel d'autre part, née « pour ung oyseau » [[monluc-lettres-ruble.a11]]. Le Parlement a ajourné les parties
[[monluc-lettres-ruble.a32]]. Il avait déjà envoyé le vice-sénéchal La Chappelle, à qui l'on a conseillé de repartir
faute d'un camp [[monluc-lettres-ruble.a31]]. Il raconte l'incendie : la femme de Roquemaurel et un enfant se jettent
par une fenêtre, les assaillants la prennent [[monluc-lettres-ruble.a3]] [[monluc-lettres-ruble.a4]], et « l'on m'a
mandé encores quelque chose de l'honneur de la pouvre femme » [[monluc-lettres-ruble.a5]]. Puis il demande des
hommes levés hors du pays par Tilladet [[monluc-lettres-ruble.a14]], de l'artillerie et le rasement des maisons
des coupables [[monluc-lettres-ruble.a15]].

## Pour et contre H1 (protégée de Monluc)

- Il ne la nomme pas et ne sait d'elle que ce qu'on lui rapporte [[monluc-lettres-ruble.a3]] [[monluc-lettres-ruble.a5]].
- Il se trompe probablement sur la religion de la famille [[monluc-lettres-ruble.a6]] (voir [[religion-des-roquemaurel]]).
- Il se pose en arbitre neutre [[monluc-lettres-ruble.a14]].
- Aucune lettre publiée ne revient sur elle (P1 infirmée dans l'édition Ruble), et elle obtient justice au
  Parlement avec le procureur général [[bardies-1903.a2]], sans trace d'intervention de Monluc.

Rien de cela n'exclut une relation que les sources taisent, mais aucun indice ne la suggère.

## Pourquoi alors cette mention (H2) ?

Elle n'a rien d'exceptionnel dans ce genre de lettre : Monluc devait justifier auprès du roi une expédition armée
dans un pays en paix (« Nous vivons en paix par toute ceste Guyenne, sans ceste querelle particulière »
[[monluc-lettres-ruble.a17]]). Le meurtre d'un gentilhomme brûlé dans sa maison et l'outrage fait à sa veuve, « chose
que de toute la sédition passée ne s'en est faict une pareille », sont les détails qui rendent la demande
pressante. C'est l'atrocité qui retient l'attention, pas la personne.

## H3 : un lien par les Roquemaurel

Monluc sait que l'aîné des Roquemaurel fut maréchal des logis du feu roi de Navarre et que la famille est « bien
apparentée de toutes parts » [[monluc-lettres-ruble.a8]] [[monluc-lettres-ruble.a7]]. Un réseau de cour ou de
service est possible, mais rien ne le montre encore (P4).

## Ce qui trancherait

Une lettre inédite ou une pièce de la procédure où Monluc intervient pour elle (P2) ; un Roquemaurel dans
l'entourage de Monluc (P4).
