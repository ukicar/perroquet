"""Compare first-pass (transcript/) and second-pass (verify/) readings line by line.
Usage: compare.py [page ...]   (default: every page present in both folders)
Prints, for each line, the tokens that differ, after normalising what the conventions
leave free (case, punctuation, u/v, i/j, accents, brackets)."""
import sys, os, re, glob, difflib, unicodedata
from paths import TEXT as root

def lines(path):
    out = {}
    for l in open(path, encoding="utf-8"):
        m = re.match(r"^(\d{2})\s{2}(.*)$", l.rstrip("\n"))
        if m: out[int(m.group(1))] = m.group(2)
    return out

def norm(tok):
    t = unicodedata.normalize("NFD", tok)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.lower().replace("v", "u").replace("j", "i")
    t = re.sub(r"[\[\]?(),;:/.'’<>\\]", "", t)
    return t

def toks(s):
    return [t for t in re.split(r"\s+", s.strip()) if t]

pages = sys.argv[1:] or sorted(os.path.basename(f)[:-3] for f in glob.glob(f"{root}/verify/*.md")
                               if os.path.exists(f"{root}/transcript/{os.path.basename(f)}"))
total_lines = total_diff = 0
for page in pages:
    a = lines(f"{root}/transcript/{page}.md"); b = lines(f"{root}/verify/{page}.md")
    print(f"\n### {page}: pass1 {len(a)} lines, pass2 {len(b)} lines")
    for n in sorted(set(a) | set(b)):
        total_lines += 1
        if n not in a or n not in b:
            print(f"{n:02d}  ONLY IN {'pass1' if n in a else 'pass2'}: {a.get(n) or b.get(n)}"); total_diff += 1; continue
        ta, tb = toks(a[n]), toks(b[n])
        na, nb = [norm(t) for t in ta], [norm(t) for t in tb]
        if na == nb:
            if ta != tb:
                # same reading, differing only in bracket/accent/punctuation: show compactly
                pairs = [(x, y) for x, y in zip(ta, tb) if x != y]
                print(f"{n:02d}  ~ {' | '.join(f'{x} / {y}' for x, y in pairs)}")
            continue
        total_diff += 1
        sm = difflib.SequenceMatcher(a=na, b=nb)
        parts = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                parts.append(f"[{' '.join(ta[i1:i2]) or '-'}] vs [{' '.join(tb[j1:j2]) or '-'}]")
        print(f"{n:02d}  {'  '.join(parts)}")
print(f"\n{total_lines} lines compared, {total_diff} with substantive differences")
