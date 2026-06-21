#!/usr/bin/env python3
"""Measure the old circular BT badge in the original banner PNG."""
from PIL import Image
import math

src = "/tmp/orig-banner-en.png"
base = Image.open(src).convert("RGBA")
w, h = base.size

# Old badge: cream circle (#FAF7F0-ish) near top-left
# We'll scan for pixels that are light and close to the top-left area.
# Then find the bounding circle.

# Expected rough region
left = 100
right = 320
top = 10
bottom = 180

xs = []
ys = []
pixels = base.load()
for y in range(top, bottom):
    for x in range(left, right):
        r, g, b, a = pixels[x, y]
        # Cream background of badge: high values, all channels similar
        if r > 220 and g > 220 and b > 200 and abs(r - g) < 20 and abs(g - b) < 30:
            xs.append(x)
            ys.append(y)

if xs:
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    cx = (minx + maxx) // 2
    cy = (miny + maxy) // 2
    radius = max(maxx - minx, maxy - miny) // 2
    print(f"Bounding box: ({minx},{miny}) - ({maxx},{maxy})")
    print(f"Center: ({cx},{cy})")
    print(f"Diameter: {maxx-minx}x{maxy-miny}, approximate radius: {radius}")
else:
    print("No badge pixels found")
