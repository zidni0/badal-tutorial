#!/usr/bin/env python3
"""Overlay the new crest badge onto the existing 816x1056 banner preview PNGs.

The new badge is placed over the old circular BT badge, then shifted slightly
up and right as requested. Any exposed remnants of the old badge outside the
new badge are painted back to the navy background color so no old "BT" logo
remains visible.
"""

from PIL import Image

# Banner preview dimensions and navy background color
W, H = 816, 1056
BG = (0x1B, 0x3A, 0x5C, 0xFF)

# Old BT badge ellipse parameters (from original preview PNG)
OLD_CX, OLD_CY = 237, 100
OLD_AX, OLD_AY = 80, 77

# New badge: 140x140 centered on old badge, then shifted up ~20 px and right ~10 px.
# This keeps the badge covering the old logo while giving the requested slight
# up/right nudge. It stays clear of the "BADAL TUTORIAL SERVICES" wordmark.
NEW_SIZE = 140
NEW_CX = OLD_CX + 10
NEW_CY = OLD_CY - 20
NEW_BOX = (
    NEW_CX - NEW_SIZE // 2,
    NEW_CY - NEW_SIZE // 2,
    NEW_CX + NEW_SIZE // 2,
    NEW_CY + NEW_SIZE // 2,
)

BADGE_PATH = "/home/ihthos/badal-tutorial/assets/logo-badge-small.png"


def in_old_badge(x, y):
    return ((x - OLD_CX) / OLD_AX) ** 2 + ((y - OLD_CY) / OLD_AY) ** 2 <= 1.0


def in_new_badge(x, y):
    half = NEW_SIZE / 2
    return abs(x - NEW_CX) <= half and abs(y - NEW_CY) <= half


def overlay(src_path, out_path, lang):
    base = Image.open(src_path).convert("RGBA")
    badge = Image.open(BADGE_PATH).convert("RGBA")

    px = base.load()

    # Erase any old-badge pixels not covered by the new badge. The exposed
    # crescent is on the bottom/left of the old badge, away from text.
    for y in range(max(0, OLD_CY - OLD_AY - 2), min(H, OLD_CY + OLD_AY + 3)):
        for x in range(max(0, OLD_CX - OLD_AX - 2), min(W, OLD_CX + OLD_AX + 3)):
            if in_old_badge(x, y) and not in_new_badge(x, y):
                px[x, y] = BG

    # Paste the new crest badge on top.
    size = (NEW_BOX[2] - NEW_BOX[0], NEW_BOX[3] - NEW_BOX[1])
    badge_resized = badge.resize(size, Image.LANCZOS)
    mask = badge_resized.split()[-1]
    base.paste(badge_resized, (NEW_BOX[0], NEW_BOX[1]), mask)
    base.save(out_path, "PNG")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    overlay(
        "/home/ihthos/badal-tutorial/banners/banner-en-flyer.png",
        "/home/ihthos/badal-tutorial/banners/banner-en-flyer.png",
        "en",
    )
    overlay(
        "/home/ihthos/badal-tutorial/banners/banner-bn-flyer.png",
        "/home/ihthos/badal-tutorial/banners/banner-bn-flyer.png",
        "bn",
    )
