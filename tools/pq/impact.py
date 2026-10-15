"""`pq impact`: what must be reviewed after a change, so that no fiche, synthesis, biography or question
is left saying something the base no longer supports.

  pq impact                 changes since the last commit (git): new or edited sources, questions, fiches
  pq impact --since REF     changes since a git ref (e.g. HEAD~3, origin/main)
  pq impact <id> [<id>...]  what depends on these fiches or assertions

A change to a source reaches every fiche named in the `sujets` of its assertions; a change to a question reaches
its `sujets` and every fiche or biography that links the question. The command lists the files that refer to
any of these ids and have not themselves been edited since REF: each must be read again and brought up to date
(synthesis, relations, biography, verdict), or consciously left as is."""
import os, re, subprocess
from .model import Base, REPO, BASE, as_list, LINK_RE, MARGE_RE


def _changed_files(ref):
    out = subprocess.run(["git", "diff", "--name-only", ref, "--", "base"], cwd=REPO, capture_output=True, text=True).stdout.split()
    out += subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "base"], cwd=REPO, capture_output=True, text=True).stdout.split()
    return {os.path.join(REPO, p) for p in out if p.endswith(".md")}


def _ids_of_file(b, path):
    fid = os.path.splitext(os.path.basename(path))[0]
    return fid if fid in b.fiches else None


def _refs_in(text):
    """Every reference in a text, both as written ('source.a3', 'question#H1') and as bare fiche id."""
    refs = set()
    for m in LINK_RE.finditer(text):
        r = m.group(1).strip()
        refs.update({r, r.split(".")[0]})
    for m in MARGE_RE.finditer(text):
        r = m.group(1).strip().split("#")[0]
        refs.update({r, r.split(".")[0]})
    return refs


def plan(b, ids):
    """Two kinds of reach. `cited`: sources or questions whose text changed, so every file citing them must be
    re-read. `subjects`: fiches named by the changed assertions or questions, whose own fiche, biography and
    questions must be re-read (but not every file that happens to link them)."""
    cited, subjects = set(), set()
    for i in ids:
        fid = i.split("#")[0].split(".")[0]
        fi = b.fiches.get(fid)
        if not fi:
            continue
        if fi.type in ("source", "hypothese"):
            cited.add(i.split("#")[0])        # 'source' (all of it) or 'source.a3' (that assertion only)
        else:
            subjects.add(fid)
        if fi.type == "source":
            for c in as_list(fi.get("assertions")):
                if isinstance(c, dict) and (("." not in i) or i.endswith("." + str(c.get("id")))):
                    subjects.update(str(s) for s in as_list(c.get("sujets")))
    return cited, subjects


def dependents(b, cited, subjects):
    """Files that cite a changed source/question, plus the fiche, biography and questions of each subject."""
    hits = {}
    def add(path, why):
        hits.setdefault(path, set()).add(why)
    for fi in b.fiches.values():
        if fi.type in ("recherche", "gallica", "demarche", "enquete"):
            continue
        refs = _refs_in(fi.body)
        for r in fi.relations():
            for p in as_list(r.get("preuves")) + as_list(r.get("hypothese")):
                p = str(p).split("#")[0]
                refs.update({p, p.split(".")[0]})
        if fi.type == "hypothese":
            for row in as_list(fi.get("matrice")):
                if isinstance(row, dict):
                    p = str(row.get("preuve"))
                    refs.update({p, p.split(".")[0]})
        for c in (refs & cited) - {fi.id}:
            add(fi.path, c)
        if fi.id in subjects:
            add(fi.path, fi.id)
    for pid, (meta, body) in b.biographies.items():
        path = os.path.join(BASE, "biographies", pid + ".md")
        for c in _refs_in(body) & cited:
            add(path, c)
        if pid in subjects:
            add(path, pid)
    return {p: sorted(w) for p, w in hits.items()}


def run(args):
    b = Base()
    if args.ids:
        changed = set()
        cited, subjects = plan(b, args.ids)
        label = ", ".join(args.ids)
    else:
        ref = args.since or "HEAD"
        changed = _changed_files(ref)
        ids = {i for i in (_ids_of_file(b, p) for p in changed) if i}
        cited, subjects = plan(b, ids)
        label = f"modifications depuis {ref} ({len(changed)} fichier(s))"
    hits = dependents(b, cited, subjects)
    todo = {p: why for p, why in hits.items() if p not in changed}
    print(f"Impact de : {label}")
    print(f"{len(cited)} source(s)/question(s) modifiée(s), {len(subjects)} fiche(s) concernée(s) ; {len(todo)} fichier(s) qui en dépendent et n'ont pas été revus :\n")
    for p in sorted(todo, key=lambda p: (("biographies" not in p), p)):
        print(f"  {os.path.relpath(p, REPO)}  ← {', '.join(todo[p][:6])}{' …' if len(todo[p]) > 6 else ''}")
    if not todo:
        print("  (rien à revoir)")
    return 0
