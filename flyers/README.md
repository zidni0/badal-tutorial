# Flyers

Bengali-led marketing flyers for Badal Tutorial. 8.5×9.4in print spec.

## Layout

Files grouped by language folder:

- `flyers/bn/` — Bengali (canonical, 3 programs)
  - `regents-bn.html/.png` — Regents prep
  - `shsat-bn.html/.png` — SHSAT Brooklyn Tech/Stuyvesant
  - `esl-bn.html/.png` — ESL bridge program
- `flyers/uz/` — Uzbek (Latin)
  - `shsat-uz.html/.png`
- `flyers/ur/` — Urdu (RTL, Nastaliq)
  - `shsat-ur.html/.png`
- `flyers/zh/` — Simplified Chinese
  - `shsat-zh.html/.png`

## Render

```bash
wkhtmltoimage --width 816 --height 984 --quality 85 \
  --enable-local-file-access --javascript-delay 500 \
  --no-stop-slow-scripts file://./regents-bn.html ./regents-bn.png   # H=951 for SHSAT, H=943 for ESL
```

## Stack

- Inline HTML/CSS, Bengali-led layout (BN headline, EN subhead)
- Navy `#1B3A5C` + Gold `#D4A017` + Cream `#FAF7F0` + Green `#0F7B5C`
- Local Noto Sans Bengali fonts
- Phone: (718) 355-0851
