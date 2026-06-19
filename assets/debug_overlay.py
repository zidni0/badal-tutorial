#!/usr/bin/env python3
from PIL import Image, ImageDraw

base = Image.open("/tmp/orig-banner-en.png").convert("RGBA")
draw = ImageDraw.Draw(base)

# Current overlay box
box = (55, 10, 195, 150)
draw.rectangle(box, outline="red", width=2)
# Erase ellipse with margin 8
erase = [(box[0]-8, box[1]-8), (box[2]+8, box[3]+8)]
draw.ellipse(erase, outline="cyan", width=2)

base.save("/tmp/debug-overlay.png")
print("Saved /tmp/debug-overlay.png")
