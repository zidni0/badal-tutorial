#!/usr/bin/env python3
"""Remove the old circular BT badge from the 816x1056 banner preview PNGs.

The user will place the new logo manually, so this script only paints the old
badge area back to the navy background color. It does NOT add a new badge.
"""

from PIL import Image

W, H = 816, 1056
BG = (0x1B, 0x3A, 0x5C, 0xFF)
OLD_CX, OLD_CY = 237, 100
OLD_AX, OLD_AY = 80, 77


def in_old_badge(x, y):
    return ((x - OLD_CX) / OLD_AX) ** 2 + ((y - OLD_CY) / OLD_AY) ** 2 <= 1.0


def remove_logo(src_path, out_path, lang):
    base = Image.open(src_path).convert("RGBA")
    px = base.load()

    for y in range(max(0, OLD_CY - OLD_AY - 2), min(H, OLD_CY + OLD_AY + 3)):
        for x in range(max(0, OLD_CX - OLD_AX - 2), min(W, OLD_CX + OLD_AX + 3)):
            if in_old_badge(x, y):
                px[x, y] = BG

    base.save(out_path, "PNG")
    print(f"Saved {out_path}")


if __name__ == "__main__":
    remove_logo(
        "/home/ihthos/badal-tutorial/banners/banner-en-flyer.png",
        "/home/ihthos/badal-tutorial/banners/banner-en-flyer.png",
        "en",
    )
    remove_logo(
        "/home/ihthos/badal-tutorial/banners/banner-bn-flyer.png",
        "/home/ihthos/badal-tutorial/banners/banner-bn-flyer.png",
        "bn",
    )
