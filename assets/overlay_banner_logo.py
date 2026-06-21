#!/usr/bin/env python3
"""Overlay the new Badal Tutorial logo onto the old banner flyer PNGs."""
from PIL import Image
import sys

# Target bounding box for logo badge in the 816x1056 banner flyer PNGs
# These are hand-tuned to cover the old circular "BT" logo.
LOGO_BOX = {
    "en": (170, 22, 270, 122),   # left, top, right, bottom (100x100 badge), shifted back right ~0.33in
    "bn": (170, 22, 270, 122),
}
ERASE_MARGIN = 12
BG_COLOR = "#1B3A5C"


def overlay(src_path, out_path, lang):
    base = Image.open(src_path).convert("RGBA")
    badge = Image.open("/home/ihthos/badal-tutorial/assets/logo-badge-small.png").convert("RGBA")

    box = LOGO_BOX[lang]
    size = (box[2] - box[0], box[3] - box[1])

    # Erase old logo circle area (including its gold border) with background color
    from PIL import ImageDraw
    draw = ImageDraw.Draw(base)
    erase_box = [(box[0]-ERASE_MARGIN, box[1]-ERASE_MARGIN),
                 (box[2]+ERASE_MARGIN, box[3]+ERASE_MARGIN)]
    draw.ellipse(erase_box, fill=BG_COLOR)

    badge_resized = badge.resize(size, Image.LANCZOS)
    mask = badge_resized.split()[-1]
    base.paste(badge_resized, (box[0], box[1]), mask)
    base.save(out_path, "PNG")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    overlay("/tmp/orig-banner-en.png", "/home/ihthos/badal-tutorial/banners/banner-en-flyer.png", "en")
    overlay("/tmp/orig-banner-bn.png", "/home/ihthos/badal-tutorial/banners/banner-bn-flyer.png", "bn")
