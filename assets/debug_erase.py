#!/usr/bin/env python3
from PIL import Image, ImageDraw

base = Image.open("/tmp/orig-banner-en.png").convert("RGBA")
draw = ImageDraw.Draw(base)

# Draw erase bbox in red
bbox = (157, 22, 317, 178)
draw.ellipse(bbox, outline="red", width=3)

# Draw new badge bbox in cyan
new_box = (190, 0, 290, 100)
draw.rectangle(new_box, outline="cyan", width=3)

base.save("/tmp/debug-erase.png")
print("Saved /tmp/debug-erase.png")
