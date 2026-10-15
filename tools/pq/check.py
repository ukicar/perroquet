"""Validation (errors block a sync) and method audit (warnings guide the research)."""
import os, re, subprocess
from .model import REPO, ID_RE, RESERVED, LINK_RE, MARGE_RE, as_list, norm_name
from . import ach

BINARY_EXT = (".pdf", ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".zip", ".djvu", ".gif")
ERR, WARN = "erreur", "avertissement"


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, where, msg, code=None):
        self.items.append({"niveau": level, "fichier": where, "message": msg, "code": code})

    def errors(self):
        return [i for i in self.items if i["niveau"] == ERR]

    def warnings(self):
        return [i for i in self.items if i["niveau"] == WARN]


def _enum(rep, voc, field, value, where, ctx=""):
    if value is None:
        return
    allowed = voc.get(field, {})
    if value not in allowed and str(value) not in {str(k) for k in allowed}:
        rep.add(ERR, where, f"{ctx}{field} = {value!r} : valeur inconnue (autorisées : {', '.join(map(str, allowed))})", "enum")


def _ref(rep, base, ref, where, ctx, kinds=None):
    r = base.resolve(ref)
    if not r:
        rep.add(ERR, where, f"{ctx}référence introuvable : {ref}", "ref")
        return None
    if kinds and r[0] not in kinds and not (r[0] == "fiche" and r[1].type in kinds):
        rep.add(ERR, where, f"{ctx}{ref} n'est pas du type attendu ({', '.join(kinds)})", "ref")
    return r


def check(base, with_git=True):
    rep = Report()
    S = base.schema
    voc = S.voc
    for where, msg in base.errors_load:
        rep.add(ERR, where, msg, "yaml")
    for a, b in base.duplicates:
        rep.add(ERR, a, f"id déjà utilisé par {b}", "doublon")

    for fi in base.fiches.values():
        w = fi.rel
        if not ID_RE.match(fi.id):
            rep.add(ERR, w, "nom de fichier invalide (minuscules, chiffres, tirets)", "id")
        if fi.id in RESERVED:
            rep.add(ERR, w, f"id réservé : {fi.id}", "id")
        if fi.type not in S.types:
            rep.add(ERR, w, f"type inconnu : {fi.type}", "type")
            continue
        if fi.folder_type and fi.type != fi.folder_type:
            rep.add(ERR, w, f"type {fi.type} rangé dans le dossier de {fi.folder_type}", "type")
        if fi.get("id") and fi.get("id") != fi.id:
            rep.add(ERR, w, f"id {fi.get('id')} différent du nom de fichier {fi.id}", "id")
        if not fi.get("nom"):
            rep.add(ERR, w, "champ nom manquant", "champ")
        for k in S.types[fi.type].get("obligatoire", []):
            if fi.get(k) in (None, "", []):
                rep.add(ERR, w, f"champ obligatoire manquant : {k}", "champ")

        # relations
        for i, r in enumerate(fi.relations()):
            ctx = f"relation {i+1} ({r.get('rel')} → {r.get('vers')}) : "
            rel = S.relations.get(r.get("rel"))
            if not rel:
                rep.add(ERR, w, ctx + "relation inconnue (voir schema/relations.yaml)", "rel")
            tgt = base.fiches.get(str(r.get("vers")))
            if not tgt:
                rep.add(ERR, w, ctx + "cible introuvable", "ref")
            elif rel:
                if rel.get("de") and fi.type not in rel["de"]:
                    rep.add(ERR, w, ctx + f"un(e) {fi.type} ne peut pas être sujet de {r.get('rel')}", "rel")
                if rel.get("vers") and tgt.type not in rel["vers"]:
                    rep.add(ERR, w, ctx + f"la cible est un(e) {tgt.type}, attendu : {', '.join(rel['vers'])}", "rel")
            _enum(rep, voc, "confiance", r.get("confiance"), w, ctx)
            if not r.get("confiance"):
                rep.add(ERR, w, ctx + "confiance manquante", "champ")
            if not r.get("preuves") and not r.get("hypothese"):
                rep.add(ERR, w, ctx + "ni preuves ni hypothese : une relation doit être justifiée", "justif")
            for p in as_list(r.get("preuves")):
                _ref(rep, base, p, w, ctx)
            if r.get("hypothese"):
                _ref(rep, base, r["hypothese"], w, ctx)
            if r.get("confiance") == "etabli":
                ok = [p for p in as_list(r.get("preuves")) if base.resolve(p) and base.resolve(p)[0] == "assertion"
                      and base.resolve(p)[2].get("verifie") in ("agent", "humain")]
                if not ok:
                    rep.add(WARN, w, ctx + "« établi » sans aucune assertion vérifiée (verifie: agent|humain)", "etabli-non-verifie")

        if fi.type == "source":
            _check_source(rep, base, fi)
        elif fi.type == "hypothese":
            _check_hypothese(rep, base, fi)
        elif fi.type == "enquete":
            _ref(rep, base, fi.get("hypothese"), w, "enquête : ")
            for k in ("recherches",):
                for x in as_list(fi.get(k)):
                    _ref(rep, base, x, w, f"{k} : ")
            aj = fi.get("ajouts") or {}
            for k, v in (aj.items() if isinstance(aj, dict) else []):
                for x in as_list(v):
                    _ref(rep, base, x, w, f"ajouts.{k} : ")
        elif fi.type == "demarche":
            _enum(rep, voc, "depots", fi.get("depot"), w)
            _enum(rep, voc, "statut_demarche", fi.get("statut"), w)
            _enum(rep, voc, "priorite", fi.get("priorite"), w)
            _enum(rep, voc, "mode", fi.get("mode"), w)
            for k in ("pour", "sources"):
                for x in as_list(fi.get(k)):
                    _ref(rep, base, x, w, f"{k} : ")
            if fi.get("statut") == "faite" and not fi.get("resultat"):
                rep.add(WARN, w, "démarche faite sans résultat noté (champ resultat)", "demarche-sans-resultat")
        elif fi.type == "gallica":
            _enum(rep, voc, "statut_gallica", fi.get("statut"), w)
            for x in as_list(fi.get("pour")) + as_list(fi.get("hyp")) + as_list(fi.get("recherche")):
                _ref(rep, base, x, w, "gallica : ")
            if fi.get("statut") == "faite" and not (fi.get("recherche") or fi.get("resultat")):
                rep.add(WARN, w, "tâche Gallica faite sans recherche ni résultat notés", "gallica-sans-resultat")
        elif fi.type == "recherche":
            _enum(rep, voc, "resultat", fi.get("resultat"), w)
            for k in ("sources_creees", "hypotheses"):
                for x in as_list(fi.get(k)):
                    _ref(rep, base, x, w, f"{k} : ")

        for l in base.body_links(fi):
            if not base.resolve(l):
                rep.add(ERR, w, f"lien [[{l}]] introuvable", "lien")

    _check_biographie(rep, base)
    _audit(rep, base)
    if with_git:
        _check_git(rep)
    return rep


def _check_source(rep, base, fi):
    w, voc = fi.rel, base.schema.voc
    for f in ("nature", "genre", "fiabilite", "consultee"):
        _enum(rep, voc, f, fi.get(f), w)
    seen = set()
    claims = [c for c in as_list(fi.get("assertions")) if isinstance(c, dict)]
    for c in claims:
        cid = c.get("id")
        ctx = f"assertion {cid} : "
        if not cid:
            rep.add(ERR, w, "assertion sans id", "champ"); continue
        if cid in seen:
            rep.add(ERR, w, ctx + "id en double", "doublon")
        seen.add(cid)
        if not c.get("texte"):
            rep.add(ERR, w, ctx + "texte manquant", "champ")
        if not c.get("citation") and c.get("preuve") != "negative":
            rep.add(WARN, w, ctx + "pas de citation verbatim", "sans-citation")
        for k in ("preuve", "information", "verifie"):
            _enum(rep, voc, k, c.get(k), w, ctx)
        if c.get("credibilite") is not None:
            _enum(rep, voc, "credibilite", c.get("credibilite"), w, ctx)
        for s in as_list(c.get("sujets")):
            if str(s) not in base.fiches:
                rep.add(ERR, w, ctx + f"sujet introuvable : {s}", "ref")
    for c in as_list(fi.get("citee_par")):
        _ref(rep, base, c, w, "citee_par : ")
    if not claims:
        rep.add(WARN, w, "source sans aucune assertion extraite", "source-vide")
    for fobj in as_list(fi.get("fichiers")):
        if isinstance(fobj, dict) and fobj.get("chemin") and not str(fobj["chemin"]).startswith("cache/"):
            rep.add(ERR, w, f"fichier {fobj['chemin']} hors de cache/ : les gros fichiers ne vont pas dans git", "fichier")


def _check_hypothese(rep, base, fi):
    w, voc = fi.rel, base.schema.voc
    _enum(rep, voc, "statut_question", fi.get("statut"), w)
    _enum(rep, voc, "confiance", fi.get("confiance"), w)
    hs = [h for h in as_list(fi.get("hypotheses")) if isinstance(h, dict)]
    ids = [str(h.get("id")) for h in hs]
    if len(hs) < 2:
        rep.add(ERR, w, "il faut au moins deux hypothèses concurrentes", "concurrence")
    if len(set(ids)) != len(ids):
        rep.add(ERR, w, "ids d'hypothèses en double", "doublon")
    for h in hs:
        if not h.get("enonce"):
            rep.add(ERR, w, f"{h.get('id')} : énoncé manquant", "champ")
        _enum(rep, voc, "auteur_hypothese", h.get("auteur"), w, f"{h.get('id')} : ")
        _enum(rep, voc, "confiance", h.get("confiance"), w, f"{h.get('id')} : ")
    if fi.get("meneur") and str(fi.get("meneur")) not in ids:
        rep.add(ERR, w, f"meneur {fi.get('meneur')} n'est pas une hypothèse de la fiche", "ref")
    pids = set()
    for p in as_list(fi.get("predictions")):
        if not isinstance(p, dict):
            continue
        ctx = f"prédiction {p.get('id')} : "
        pids.add(str(p.get("id")))
        for h in as_list(p.get("h")):
            if str(h) not in ids:
                rep.add(ERR, w, ctx + f"hypothèse {h} inconnue", "ref")
        _enum(rep, voc, "statut_prediction", p.get("statut"), w, ctx)
        _enum(rep, voc, "diagnostique", p.get("diagnostique"), w, ctx)
        if not p.get("attendu"):
            rep.add(ERR, w, ctx + "champ attendu manquant", "champ")
        for e in as_list(p.get("enquetes")):
            _ref(rep, base, e, w, ctx)
        for e in as_list(p.get("preuves")):
            _ref(rep, base, e, w, ctx)
    for row in as_list(fi.get("matrice")):
        if not isinstance(row, dict):
            continue
        ctx = f"matrice {row.get('preuve')} : "
        _ref(rep, base, row.get("preuve"), w, ctx)
        for h in ids:
            if h in row:
                _enum(rep, voc, "matrice", str(row[h]), w, ctx)
        for k in row:
            if k not in ("preuve", "note") and k not in ids:
                rep.add(ERR, w, ctx + f"colonne {k} ne correspond à aucune hypothèse", "ref")
    for k in ("sujets", "sous_questions"):
        for x in as_list(fi.get(k)):
            _ref(rep, base, x, w, f"{k} : ")


def _check_biographie(rep, base):
    """base/biographies/<id>.md : liens valides, notes marginales résolues, chaque paragraphe annoté et sourcé."""
    for pid, (meta, body) in sorted(base.biographies.items()):
        w = f"base/biographies/{pid}.md"
        if not ID_RE.match(pid):
            rep.add(ERR, w, "nom de fichier invalide (minuscules, chiffres, tirets)", "id")
        if pid not in base.fiches:
            rep.add(ERR, w, f"aucune fiche {pid} : le nom du fichier doit être l'id de la personne", "ref")
        _check_biographie_texte(rep, base, w, body)


def _norm_quote(t):
    return re.sub(r"\s+", " ", str(t).replace("’", "'")).strip()


def _check_biographie_texte(rep, base, w, body):
    corpus = [_norm_quote(c.get(k)) for _, c in base.claims.values() for k in ("citation", "texte") if c.get(k)]
    for q in re.findall(r"«\s*(.+?)\s*»", re.sub(r"\[\[[^\]]*\]\]", "", body), re.S):
        nq = _norm_quote(q)
        if nq and not any(nq in c for c in corpus):
            rep.add(WARN, w, f"citation « {nq[:60]} » introuvable telle quelle dans les assertions", "citation-biographie")
    for m in LINK_RE.finditer(body):
        ref = m.group(1).strip() + (("#" + m.group(2)) if m.group(2) else "")
        if not base.resolve(ref):
            rep.add(ERR, w, f"lien [[{ref}]] introuvable", "lien")
    for m in MARGE_RE.finditer(body):
        tag, note = m.group(1), m.group(2)
        if not base.marge(tag):
            rep.add(ERR, w, f"note marginale {{{{{tag}|…}}}} : ni une confiance ({', '.join(base.schema.voc['confiance'])}, "
                            f"inconnu) ni une question ou hypothèse existante", "marge")
        elif tag not in base.schema.voc.get("marge", {}) and not LINK_RE.search(note):
            rep.add(WARN, w, f"note marginale {{{{{tag}|{note.strip()[:40]}…}}}} sans aucune preuve [[…]]", "marge-sans-preuve")
    for para in body.split("\n\n"):
        p = para.strip()
        if p and not p.startswith("#") and not MARGE_RE.search(p):
            rep.add(WARN, w, f"paragraphe sans note marginale : « {p[:50]}… »", "marge-absente")


def _audit(rep, base):
    mentions = base.mentions()
    mentioned = set().union(*mentions.values()) if mentions else set()
    linked = set()
    for e in base.edges():
        linked.add(e["src"]); linked.add(str(e["dst"]))
    for h in base.of_type("hypothese"):
        linked.update(str(x) for x in as_list(h.get("sujets")))

    for fi in base.of_type("hypothese"):
        w = fi.rel
        s = ach.score(base, fi)
        if not s["lignes"]:
            rep.add(WARN, w, "matrice vide : aucune preuve évaluée", "matrice-vide")
        elif fi.get("meneur") and s["meneur_calcule"] and str(fi.get("meneur")) != s["meneur_calcule"]:
            rep.add(WARN, w, f"meneur déclaré {fi.get('meneur')} ≠ meneur calculé {s['meneur_calcule']} (moins d'incohérences)", "meneur")
        nt = s["predictions"].get("non_testee", 0)
        if nt:
            rep.add(WARN, w, f"{nt} prédiction(s) non testée(s)", "predictions")
        if not as_list(fi.get("contestations")) and fi.get("statut") != "suspendue":
            rep.add(WARN, w, "jamais contestée (/challenge)", "jamais-contestee")
        if fi.get("confiance") == "etabli":
            verified = [r for r in s["lignes"] if base.resolve(r["preuve"]) and base.resolve(r["preuve"])[0] == "assertion"
                        and base.resolve(r["preuve"])[2].get("verifie") in ("agent", "humain")]
            if not verified:
                rep.add(WARN, w, "verdict « établi » sans preuve vérifiée", "etabli-non-verifie")
        if s["lignes"] and s["non_diagnostiques"] == len(s["lignes"]):
            rep.add(WARN, w, "aucune preuve diagnostique : rien ne départage les hypothèses", "non-diagnostique")

    for fi in base.fiches.values():
        if fi.type in ("personne", "famille", "lieu", "evenement", "institution"):
            if fi.id not in linked and fi.id not in mentioned:
                rep.add(WARN, fi.rel, "fiche isolée : aucune relation ni mention", "orpheline")
            if fi.type in ("personne", "famille", "evenement") and not fi.span():
                rep.add(WARN, fi.rel, "aucune date (naissance/mort/periode/date) : invisible sur la frise", "sans-date")
            if not fi.body.strip():
                rep.add(WARN, fi.rel, "pas de synthèse rédigée", "sans-synthese")
            if fi.type == "personne" and fi.id not in base.biographies:
                rep.add(WARN, fi.rel, "pas de biographie (base/biographies/)", "sans-biographie")

    # possible duplicates
    seen = {}
    for fi in base.fiches.values():
        if fi.type not in ("personne", "famille", "lieu", "institution"):
            continue
        for n in [fi.nom] + [str(v) for v in as_list(fi.get("variantes"))]:
            k = (fi.type, norm_name(n))
            if k[1] and k in seen and seen[k] != fi.id:
                rep.add(WARN, fi.rel, f"doublon possible avec {seen[k]} (« {n} »)", "doublon-possible")
            seen.setdefault(k, fi.id)


def _check_git(rep):
    try:
        out = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, capture_output=True, text=True, check=True).stdout
    except Exception:
        return
    for f in filter(None, out.split("\0")):
        p = os.path.join(REPO, f)
        if f.lower().endswith(BINARY_EXT):
            rep.add(ERR, f, "fichier binaire suivi par git : il doit rester dans cache/", "binaire")
        elif os.path.exists(p) and os.path.getsize(p) > 2_000_000:
            rep.add(ERR, f, "fichier de plus de 2 Mo suivi par git", "taille")
