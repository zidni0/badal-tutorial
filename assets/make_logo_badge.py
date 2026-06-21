#!/usr/bin/env python3
"""Create circular badge versions of the Badal Tutorial crest logo."""
from PIL import Image, ImageDraw
import math

SRC = "/home/ihthos/Downloads/Logo Enhanced.jpg"
SIZES = {
    "large": (900, 72),   # banner: 900px canvas, 72% fill ratio (smaller crest inside circle)
    "small": (180, 65),   # flyer: 180px canvas, 65% fill ratio
}
BORDER_COLOR = "#D4A017"
BG_COLOR = "#FAF7F0"


def make_badge(size, fill_ratio, output):
    src = Image.open(SRC).convert("RGBA")
    # Crop to square around center
    w, h = src.size
    dim = min(w, h)
    left = (w - dim) // 2
    top = (h - dim) // 2
    src = src.crop((left, top, left + dim, top + dim))

    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    radius = size // 2
    border_width = max(2, size // 45)

    # Background circle
    draw.ellipse(
        [(border_width, border_width), (size - border_width, size - border_width)],
        fill=BG_COLOR,
        outline=BORDER_COLOR,
        width=border_width,
    )

    # Inner mask for logo
    inner_radius = radius - border_width - max(1, size // 60)
    mask = Image.new("L", (size, size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.ellipse(
        [(radius - inner_radius, radius - inner_radius),
         (radius + inner_radius, radius + inner_radius)],
        fill=255,
    )

    # Resize logo to fit inner circle with fill_ratio
    logo_diameter = int(inner_radius * 2 * fill_ratio)
    src = src.resize((logo_diameter, logo_diameter), Image.LANCZOS)

    # Center and composite
    x = (size - logo_diameter) // 2
    y = (size - logo_diameter) // 2
    canvas.paste(src, (x, y), src)
    canvas.putalpha(mask)

    canvas.save(output, "PNG")
    print(f"Saved {output} ({size}x{size})")


if __name__ == "__main__":
    make_badge(SIZES["large"][0], SIZES["large"][1] / 100, "/home/ihthos/badal-tutorial/assets/logo-badge-large.png")
    make_badge(SIZES["small"][0], SIZES["small"][1] / 100, "/home/ihthos/badal-tutorial/assets/logo-badge-small.png")
