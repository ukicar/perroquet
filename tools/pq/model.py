"""Load the knowledge base (base/**/*.md with YAML front matter) and the schema."""
import os, re, glob, unicodedata
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(REPO, "base")
SCHEMA = os.path.join(REPO, "schema")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]")
RESERVED = {"index", "graphe", "chronologie", "audit", "hypotheses", "sources", "fiches",
            "enquetes", "recherches", "carte"}


def load_yaml(name):
    with open(os.path.join(SCHEMA, name), encoding="utf-8") as f:
        return yaml.safe_load(f)


class Schema:
    def __init__(self):
        self.types = load_yaml("types.yaml")
        self.relations = load_yaml("relations.yaml")
        self.voc = load_yaml("vocabulaire.yaml")
        self.folder_type = {t["dossier"]: name for name, t in self.types.items()}


def slugify(text):
    t = unicodedata.normalize("NFD", text)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").lower()
    t = re.sub(r"['’]", "-", t)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return re.sub(r"-{2,}", "-", t)


def norm_name(text):
    """Loose form of a name for duplicate detection: no accents, particles or punctuation."""
    t = slugify(text).replace("-", " ")
    t = re.sub(r"\b(de|d|du|des|la|le|les|sieur|seigneur|noble)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def year_of(value):
    """First 3-4 digit year in a date value ('1567-05-24', '1567~', 1567, 'c. 1560'), or None."""
    if value is None:
        return None
    m = re.search(r"(\d{3,4})", str(value))
    return int(m.group(1)) if m else None


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


class Fiche:
    def __init__(self, path, meta, body, schema):
        self.path = path
        self.rel = os.path.relpath(path, REPO)
        self.meta = meta or {}
        self.body = body
        self.id = os.path.splitext(os.path.basename(path))[0]
        folder = os.path.basename(os.path.dirname(path))
        self.folder_type = schema.folder_type.get(folder)
        self.type = self.meta.get("type") or self.folder_type
        self.nom = self.meta.get("nom") or self.id

    def get(self, k, d=None):
        return self.meta.get(k, d)

    def span(self):
        """(start_year, end_year) used by the time slider; None if undated."""
        m = self.meta
        if m.get("periode"):
            p = as_list(m["periode"])
            a = year_of(p[0]); b = year_of(p[-1])
            return (a, b or a)
        a = year_of(m.get("date") or m.get("naissance") or m.get("date_redaction"))
        b = year_of(m.get("fin") or m.get("mort")) or a
        if a is None and b is None:
            return None
        return (a or b, b)

    def relations(self):
        return [r for r in as_list(self.meta.get("relations")) if isinstance(r, dict)]


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---[ \t]*\n?(.*)$", text, re.S)
    if m:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    return {}, text


class Base:
    def __init__(self):
        self.schema = Schema()
        self.fiches = {}
        self.errors_load = []
        self.duplicates = []
        for path in sorted(glob.glob(os.path.join(BASE, "*", "*.md"))):
            try:
                meta, body = parse_file(path)
            except yaml.YAMLError as e:
                self.errors_load.append((os.path.relpath(path, REPO), f"YAML illisible : {e}"))
                continue
            fi = Fiche(path, meta, body, self.schema)
            if fi.id in self.fiches:
                self.duplicates.append((fi.rel, self.fiches[fi.id].rel))
                continue
            self.fiches[fi.id] = fi
        self._index()

    def _index(self):
        self.claims = {}      # "source.a3" -> (source fiche, claim dict)
        for fi in self.of_type("source"):
            for c in as_list(fi.get("assertions")):
                if isinstance(c, dict) and c.get("id"):
                    self.claims[f"{fi.id}.{c['id']}"] = (fi, c)

    def of_type(self, t):
        return [f for f in self.fiches.values() if f.type == t]

    def resolve(self, ref):
        """Resolve 'id', 'source.a3', 'hyp#H1', 'hyp#P2'. Returns (kind, fiche, item) or None."""
        ref = str(ref).strip()
        if "#" in ref:
            fid, anchor = ref.split("#", 1)
            fi = self.fiches.get(fid)
            if not fi:
                return None
            for key in ("hypotheses", "predictions"):
                for it in as_list(fi.get(key)):
                    if isinstance(it, dict) and str(it.get("id")) == anchor:
                        return (key, fi, it)
            return None
        if ref in self.fiches:
            return ("fiche", self.fiches[ref], None)
        if ref in self.claims:
            fi, c = self.claims[ref]
            return ("assertion", fi, c)
        return None

    def evidence_weight(self, ref):
        """Weight of a piece of evidence for ACH: source reliability x claim credibility."""
        voc = self.schema.voc
        r = self.resolve(ref)
        if not r:
            return 0.5
        kind, fi, item = r
        if kind == "assertion":
            rel = voc["fiabilite"].get(str(fi.get("fiabilite")), {}).get("poids", 0.5)
            cred = voc["credibilite"].get(item.get("credibilite"), voc["credibilite"].get(str(item.get("credibilite")), {}))
            cred = cred.get("poids", 0.5) if isinstance(cred, dict) else 0.5
            return round(rel * cred, 3)
        if kind == "fiche" and fi.type == "recherche":
            return 0.6   # a recorded negative or positive search
        return 0.5

    def edges(self):
        """All typed relations as dicts: src, dst, rel, confiance, hypothese, preuves, role, span."""
        out = []
        for fi in self.fiches.values():
            for r in fi.relations():
                out.append({
                    "src": fi.id, "dst": r.get("vers"), "rel": r.get("rel"),
                    "confiance": r.get("confiance"), "hypothese": r.get("hypothese"),
                    "preuves": as_list(r.get("preuves")), "role": r.get("role"),
                    "debut": year_of(r.get("debut")), "fin": year_of(r.get("fin") or r.get("debut")),
                    "note": r.get("note"),
                })
        return out

    def mentions(self):
        """source id -> set of entity ids mentioned by its claims."""
        out = {}
        for fi in self.of_type("source"):
            s = set()
            for c in as_list(fi.get("assertions")):
                if isinstance(c, dict):
                    s.update(str(x) for x in as_list(c.get("sujets")))
            out[fi.id] = s
        return out

    def body_links(self, fi):
        return [m.group(1).strip() + (("#" + m.group(2)) if m.group(2) else "") for m in LINK_RE.finditer(fi.body)]
