"""Assemble transcript/*.md into 1567_transcription.md (text, then the notes of every
page, then an index of bracketed readings)."""
import os, re, glob
from paths import TEXT as root
order = ["p05R","p07L","p07R","p08L","p08R","p09L","p09R","p10L","p10R","p11L","p11R",
         "p12L","p12R","p13L","p13R","p14L","p14R","p15L","p15R","p16L","p16R","p17L","p17R"]
head = """# Parlement de Toulouse — extrait des registres, année 1567

Source: BnF, ms. Français 5455, « Extrait particulier de tout ce qui s'est faict au Parlement
pendant la Ligue et années 1567 finissant 1569 le xi sep.bre », Gallica scan
btv1b9065178t, PDF pages 5–17 (folios 2r–13r). Transcription diplomatique, line by line;
the conventions (abbreviations kept, `[...]` = uncertain reading) are in CONVENTIONS.md.
Pass 1: Claude (Fable 5.1), pass 2: independent second readings, reconciled on the images.

## Recurring names, as written

- Presidents: Daffis (premier; "Jean Daffis" fol. 8v, 10v), de Paulo ("Anthoine de Paulo" fol. 10v),
  de Malrac (so on fol. 2r, 2v; the last letter is unclear elsewhere: [Malrac?] fol. 6v, 8r, 9r, 10v,
  [Malran?] fol. 11r), [Latoury?] (fol. 8r, 10v; "Nicolas"), du faur (fol. 8r).
- Councillors in the presence lists: Benoist, [Roguier?], de Molinier, Fabri / Faby, Doujat (fol. 2r,
  2v) / doussat (fol. 6v, 8r, 11r), de Bouard (fol. 2r) / Bouald, (P.) Sabatier ("Pierre Sabatier
  Cons.er" fol. 10v), Rangouse, Forez, de S.t Paul (maistre des requestes), de Gaugan, Guillemette /
  Guillemite, [Ouvoir?], [Dausour?] (fol. 6r).
- Officers: Daygua / [Deygua?], advocat general ("Bertrand daygua" fol. 10v); [Cunyez?] / [Cunyes?],
  tresorier general de France; M.e Pierre le fevre, receveur des exploitz et amandes; Mathurin
  [Baudoyn?], clerc des finances; Jean de Raymond, conseiller.
- Capitouls and others: M.e Jean Boyer, George [Burin?]; Andri [Tesse?], marchant; le Seigneur de la
  [Caunye?]; the sieur de Bellegarde; the seigneur de Joyeuse; Dampville; the Cardinal de Strocy.

"""
texts, notes, doubts = [], [], []
for p in order:
    f = f"{root}/transcript/{p}.md"
    if not os.path.exists(f): continue
    s = open(f, encoding="utf-8").read()
    title = s.splitlines()[0].lstrip("# ").strip()
    body, note = s, ""
    if "\nnotes:" in s:
        body, note = s.split("\nnotes:", 1)
    body = "\n".join(l for l in body.splitlines()[1:]).strip("\n")
    texts.append(f"## {title}\n\n```\n{body}\n```\n")
    if note.strip():
        notes.append(f"### {title}\n{note.strip()}\n")
    for l in body.splitlines():
        m = re.match(r"^(\d{2})\s{2}(.*)$", l)
        if m:
            for d in re.findall(r"\[[^\]]*\?\]|\[\.\.\.\]", m.group(2)):
                doubts.append(f"- {p} l.{m.group(1)}: {d}")
out = head + "\n".join(texts) + "\n# Notes\n\n" + "\n".join(notes) + \
      f"\n# Uncertain readings ({len(doubts)})\n\n" + "\n".join(doubts) + "\n"
open(f"{root}/1567_transcription.md", "w", encoding="utf-8").write(out)
nlines = sum(1 for t in texts for l in t.splitlines() if re.match(r"^\d{2}\s{2}", l))
print(f"{len(texts)} pages, {nlines} lines, {len(doubts)} bracketed readings -> 1567_transcription.md")
