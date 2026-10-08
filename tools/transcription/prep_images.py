"""Split each 300-DPI spread into left/right folio pages and cut each page into
3 overlapping horizontal strips for transcription.

Usage: python3 prep_images.py <src_dir> <out_dir> <first_page> <last_page>
Output names: pNNL / pNNR (PDF page NN, Left/Right side):
  pNNR_full.png  - the whole text block of that folio page
  pNNR_1.png ... pNNR_3.png - overlapping strips, top to bottom
"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw

src, out, first, last = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
os.makedirs(out, exist_ok=True)

def smooth(a, k):
    k = int(k); ker = np.ones(k) / k
    return np.convolve(a, ker, mode="same")

def find_gutter(g):
    H, W = g.shape
    col = g[int(H*0.15):int(H*0.85), :].mean(axis=0)
    col = smooth(col, 15)
    lo, hi = int(W*0.35), int(W*0.65)
    return lo + int(np.argmin(col[lo:hi]))

def longest_run(mask, maxgap):
    """Longest run of True values allowing gaps up to maxgap; returns (start, end)."""
    idx = np.where(mask)[0]
    if len(idx) == 0:
        return None
    best = (idx[0], idx[0]); start = idx[0]; prev = idx[0]
    for i in idx[1:]:
        if i - prev > maxgap:
            if prev - start > best[1] - best[0]:
                best = (start, prev)
            start = i
        prev = i
    if prev - start > best[1] - best[0]:
        best = (start, prev)
    return best

def text_bounds(g, x0, x1, y0, y1, ink_thr=110):
    """Bounding box of the handwriting inside a window: ignores very dark bands
    (page edges, gutter) and keeps the longest run of moderately inked columns/rows."""
    sub = g[y0:y1, x0:x1]
    ink = (sub < ink_thr).astype(np.float32)
    colf = smooth(ink.mean(axis=0), 25)
    cols = longest_run((colf > 0.004) & (colf < 0.45), 90)
    if cols is None:
        return None
    sub2 = ink[:, cols[0]:cols[1]]
    rowf = smooth(sub2.mean(axis=1), 25)
    rows = longest_run((rowf > 0.004) & (rowf < 0.5), 260)
    if rows is None:
        return None
    return (x0 + cols[0], y0 + rows[0], x0 + cols[1], y0 + rows[1])

report = []
for p in range(first, last + 1):
    path = f"{src}/hi-{p:03d}.png"
    if not os.path.exists(path) or p == 6:
        continue
    im = Image.open(path).convert("L")
    g = np.asarray(im)
    H, W = g.shape
    gx = find_gutter(g)
    sides = {
        "L": (max(0, gx - 1350), gx - 15),
        "R": (gx + 120, min(W, gx + 1850)),
    }
    for side, (wx0, wx1) in sides.items():
        if p == 5 and side == "L":
            continue
        bb = text_bounds(g, wx0, wx1, 200, 2600)
        if bb is None:
            report.append(f"p{p:02d}{side}: no text found"); continue
        x0, y0, x1, y1 = bb
        pad = 45
        x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
        x1, y1 = min(W, x1 + pad), min(H, y1 + pad)
        # keep the folio number (top-right of rectos) by extending upward a little
        page = im.crop((x0, y0, x1, y1))
        name = f"p{p:02d}{side}"
        page.save(f"{out}/{name}_full.png")
        h = y1 - y0
        n = 3; ov = 130
        step = (h - ov) / n
        for i in range(n):
            sy0 = int(i * step); sy1 = int(min(h, (i + 1) * step + ov))
            page.crop((0, sy0, x1 - x0, sy1)).save(f"{out}/{name}_{i+1}.png")
        report.append(f"{name}: gutter={gx} box=({x0},{y0},{x1},{y1}) size={x1-x0}x{y1-y0} strips={n}x~{int(step+ov)}px")
print("\n".join(report))
