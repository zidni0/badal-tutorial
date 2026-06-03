# Flyers

Bengali-led marketing flyers for Badal Tutorial. 8.5×9.4in print spec.

## Files

- `regents-bn.png` / `regents-bn.html` — Regents prep ($250 / whole summer promo)
- `shsat-bn.png` / `shsat-bn.html` — SHSAT Brooklyn Tech/Stuyvesant/BHSEC ($250 / whole summer promo)
- `esl-bn.png` / `esl-bn.html` — ESL bridge program ($250 / whole summer promo)

## Render

```bash
wkhtmltoimage --width 816 --height 979 --quality 85 \
  --enable-local-file-access --javascript-delay 500 \
  --no-stop-slow-scripts file://./regents-bn.html ./regents-bn.png
```

## Stack

- Inline HTML/CSS, Bengali-led layout (BN headline, EN subhead)
- Navy `#1B3A5C` + Gold `#D4A017` + Cream `#FAF7F0` + Green `#0F7B5C`
- Local Noto Sans Bengali fonts
- Phone: (718) 355-0851
