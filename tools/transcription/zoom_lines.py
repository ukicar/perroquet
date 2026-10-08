"""Zoom on manuscript lines.
Usage: zoom_lines.py <page> [--n N] <line>[a|b] ...
Detects text lines on images/<page>_full.png by row-projection peaks. With --n N (the
number of lines in the transcript) the detected set is fitted to N lines: large gaps are
split, weakest extra peaks dropped, so that line numbers match the transcript.
Writes <page>_L<nn>.png (whole line, 1.35x) or <page>_L<nn>a/b.png (halves, 2x)."""
import sys, os
import numpy as np
from PIL import Image

args = sys.argv[1:]
page = args.pop(0)
N = None
if args and args[0] == "--n":
    args.pop(0); N = int(args.pop(0))
wanted = args
from paths import IMAGES, ZOOM
im = Image.open(f"{IMAGES}/{page}_full.png").convert("L")
g = np.asarray(im); H, W = g.shape
ink = (g < 110).astype(np.float32)
colf = ink.mean(axis=0); good = colf < 0.4
rowf = ink[:, good].mean(axis=1)
k = 31; rowf = np.convolve(rowf, np.ones(k)/k, mode="same")
thr = 0.05; sep = 30
peaks = []
for y in range(sep, H - sep):
    if rowf[y] >= thr and rowf[y] == rowf[y-sep:y+sep+1].max():
        if not peaks or y - peaks[-1] > sep: peaks.append(y)
# drop short marks (folio numbers, stamps): ink must span > 25% of the width
ys = []
for y in peaks:
    band = ink[max(0, y-30):y+30, :].mean(axis=0)
    xs = np.where(band > 0.02)[0]
    if len(xs) and (xs[-1] - xs[0]) > 0.25 * W: ys.append(y)
ys.sort()
if N and len(ys) >= 3:
    gaps = np.diff(ys); pitch = float(np.median(gaps))
    # merge peaks closer than 0.55 pitch (one line detected twice)
    merged = [ys[0]]
    for y in ys[1:]:
        if y - merged[-1] < 0.55 * pitch: merged[-1] = (merged[-1] + y) // 2
        else: merged.append(y)
    ys = merged
    while len(ys) < N:            # split the largest gap that contains ink (not a paragraph gap)
        gaps = np.diff(ys); order = np.argsort(-gaps); done = False
        for i in order:
            if gaps[i] < 1.5 * pitch: break
            mid = (ys[i] + ys[i+1]) // 2
            band = ink[mid-12:mid+12, :][:, good].mean()
            if band > 0.03:
                ys.insert(i + 1, mid); done = True; break
        if not done: break
    while len(ys) > N:            # drop the weakest peak
        i = int(np.argmin([rowf[y] for y in ys])); ys.pop(i)
lines = [(max(0, y-52), min(H, y+52)) for y in ys]
out = ZOOM
os.makedirs(out, exist_ok=True)
print(f"{page}: {len(lines)} lines" + (f" (fitted to {N})" if N else "") + " at y=" + ",".join(str((a+b)//2) for a, b in lines))
for spec in wanted:
    half = spec[-1] if spec[-1] in "ab" else None
    n = int(spec.rstrip("ab"))
    if n < 1 or n > len(lines): print(f"line {n}: out of range"); continue
    s, e = lines[n-1]
    line = im.crop((0, max(0, s-24), W, min(H, e+24)))
    if half:
        mid = W // 2; ov = 120
        x0, x1 = (0, mid+ov) if half == "a" else (mid-ov, W)
        c = line.crop((x0, 0, x1, line.height)); c = c.resize((c.width*2, c.height*2), Image.LANCZOS)
        c.save(f"{out}/{page}_L{n:02d}{half}.png")
    else:
        c = line.resize((int(line.width*1.35), int(line.height*1.35)), Image.LANCZOS)
        c.save(f"{out}/{page}_L{n:02d}.png")
    print(f"line {n}: y={s}-{e} -> {page}_L{n:02d}{half or ''}.png")
