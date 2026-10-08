"""crop.py <page> <name> <x0> <y0> <x1> <y1> [scale]  -> cache/zoom/<page>_<name>.png"""
import sys, os
from PIL import Image
page, name = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7]); scale = float(sys.argv[7]) if len(sys.argv) > 7 else 3.0
from paths import IMAGES, ZOOM
im = Image.open(f"{IMAGES}/{page}_full.png").convert("L")
c = im.crop((x0, y0, x1, y1)); c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
out = ZOOM
os.makedirs(out, exist_ok=True); c.save(f"{out}/{page}_{name}.png"); print(f"{page}_{name}.png {c.size}")
