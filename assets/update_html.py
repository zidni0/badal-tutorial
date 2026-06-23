#!/usr/bin/env python3
"""Batch update flyer and banner HTML sources per latest request.

Changes:
- Remove crest/logo from all flyers and banners (user will place logo manually).
- Update "Programs We Offer" subject lists across all languages.
- Update 8+ -> 18+ on banner trust bar.
- Ensure pricing is $265 (flyers already are; no banner price pill).
"""

import re
from pathlib import Path

ROOT = Path("/home/ihthos/badal-tutorial")


def read(path):
    return path.read_text(encoding="utf-8")


def write(path, text):
    path.write_text(text, encoding="utf-8")
    print(f"Updated {path}")


# ---------------------------------------------------------------------------
# Flyers
# ---------------------------------------------------------------------------

def remove_flyer_logo(html):
    # Remove the logo div entirely
    html = re.sub(
        r'<div class="flyer-logo"><img[^>]*alt="Badal Tutorial logo"[^>]*></div>\n',
        "",
        html,
    )
    # Compensate by reducing badges-row top margin so layout doesn't jump
    html = html.replace(
        '.badges-row { display: flex; flex-wrap: nowrap; gap: 5px; margin-top: 80px; margin-bottom: 4px; max-width: 64%; }',
        '.badges-row { display: flex; flex-wrap: nowrap; gap: 5px; margin-top: 10px; margin-bottom: 4px; max-width: 64%; }',
    )
    return html


def update_flyer_programs_bn(html):
    # Replace the three program columns with Math/Science, History/ELA, Test Prep/ESL
    old = re.search(
        r'(<!-- BODY: 3 program columns \+ hours card -->\s*<div class="body-bn">\s*<div class="programs-row">).*?(</div>\s*<!-- HOURS CARD -->)',
        html,
        re.DOTALL,
    )
    if not old:
        return html

    new_block = '''<!-- BODY: 3 program columns + hours card -->
  <div class="body-bn">
    <div class="programs-row">

      <!-- MATH & SCIENCE -->
      <div class="program-col regents">
        <div class="program-title">গণিত ও বিজ্ঞান</div>
        <div class="program-title-en">MATH & SCIENCE</div>
        <div class="program-divider" style="background:#0F7B5C;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">অ্যালজেব্রা ১ ও ২</div>
            <div class="program-text-en">Algebra I & II</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">জ্যামিতি</div>
            <div class="program-text-en">Geometry</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">লিভিং এনভায়রনমেন্ট</div>
            <div class="program-text-en">Living Environment</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">পৃথিবী বিজ্ঞান ও রসায়ন</div>
            <div class="program-text-en">Earth Science & Chemistry</div>
          </div>
        </div>
      </div>

      <!-- HISTORY & ENGLISH -->
      <div class="program-col esl">
        <div class="program-title">ইতিহাস ও ইংরেজি</div>
        <div class="program-title-en">HISTORY & ELA</div>
        <div class="program-divider"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">মার্কিন ইতিহাস</div>
            <div class="program-text-en">US History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">বিশ্ব ইতিহাস</div>
            <div class="program-text-en">Global History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">ইংরেজি ভাষা শিল্প</div>
            <div class="program-text-en">ELA / Reading</div>
          </div>
        </div>
      </div>

      <!-- TEST PREP & ESL -->
      <div class="program-col shsat">
        <div class="program-title">পরীক্ষা প্রস্তুতি ও ESL</div>
        <div class="program-title-en">TEST PREP & ESL</div>
        <div class="program-divider" style="background:#C8341B;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">রিজেন্টস</div>
            <div class="program-text-en">Regents</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">SAT</div>
            <div class="program-text-en">SAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">SHSAT</div>
            <div class="program-text-en">SHSAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-bn">ইএসএল ব্রিজ</div>
            <div class="program-text-en">ESL Bridge</div>
          </div>
        </div>
      </div>
    </div>

    <!-- HOURS CARD -->'''

    html = html[: old.start()] + new_block + html[old.end():]
    return html


def update_flyer_programs_zh(html):
    old = re.search(
        r'(<!-- BODY: 3 program columns \+ hours card -->\s*<div class="body-zh">\s*<div class="programs-row">).*?(</div>\s*<!-- HOURS CARD -->)',
        html,
        re.DOTALL,
    )
    if not old:
        return html

    new_block = '''<!-- BODY: 3 program columns + hours card -->
  <div class="body-zh">
    <div class="programs-row">

      <!-- MATH & SCIENCE -->
      <div class="program-col regents">
        <div class="program-title">数学与科学</div>
        <div class="program-title-en">MATH & SCIENCE</div>
        <div class="program-divider" style="background:#0F7B5C;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">代数 1 和 2</div>
            <div class="program-text-en">Algebra I & II</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">几何</div>
            <div class="program-text-en">Geometry</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">生物与环境</div>
            <div class="program-text-en">Living Environment</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">地球科学和化学</div>
            <div class="program-text-en">Earth Science & Chemistry</div>
          </div>
        </div>
      </div>

      <!-- HISTORY & ENGLISH -->
      <div class="program-col esl">
        <div class="program-title">历史与英语</div>
        <div class="program-title-en">HISTORY & ELA</div>
        <div class="program-divider"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">美国历史</div>
            <div class="program-text-en">US History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">世界历史</div>
            <div class="program-text-en">Global History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">英语语言艺术</div>
            <div class="program-text-en">ELA / Reading</div>
          </div>
        </div>
      </div>

      <!-- TEST PREP & ESL -->
      <div class="program-col shsat">
        <div class="program-title">备考与 ESL</div>
        <div class="program-title-en">TEST PREP & ESL</div>
        <div class="program-divider" style="background:#C8341B;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">Regents</div>
            <div class="program-text-en">Regents</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">SAT</div>
            <div class="program-text-en">SAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">SHSAT</div>
            <div class="program-text-en">SHSAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-zh">ESL 桥梁</div>
            <div class="program-text-en">ESL Bridge</div>
          </div>
        </div>
      </div>
    </div>

    <!-- HOURS CARD -->'''

    html = html[: old.start()] + new_block + html[old.end():]
    return html


def update_flyer_programs_uz(html):
    old = re.search(
        r'(<!-- BODY: 3 program columns \+ hours card -->\s*<div class="body-uz">\s*<div class="programs-row">).*?(</div>\s*<!-- HOURS CARD -->)',
        html,
        re.DOTALL,
    )
    if not old:
        return html

    new_block = '''<!-- BODY: 3 program columns + hours card -->
  <div class="body-uz">
    <div class="programs-row">

      <!-- MATH & SCIENCE -->
      <div class="program-col regents">
        <div class="program-title">Matematika va Fan</div>
        <div class="program-title-en">MATH & SCIENCE</div>
        <div class="program-divider" style="background:#0F7B5C;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Algebra I va II</div>
            <div class="program-text-en">Algebra I & II</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Geometriya</div>
            <div class="program-text-en">Geometry</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Living Environment</div>
            <div class="program-text-en">Living Environment</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Yer fani va Kimyo</div>
            <div class="program-text-en">Earth Science & Chemistry</div>
          </div>
        </div>
      </div>

      <!-- HISTORY & ENGLISH -->
      <div class="program-col esl">
        <div class="program-title">Tarix va Ingliz tili</div>
        <div class="program-title-en">HISTORY & ELA</div>
        <div class="program-divider"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">AQSh tarixi</div>
            <div class="program-text-en">US History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Jahon tarixi</div>
            <div class="program-text-en">Global History</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Ingliz tili / Reading</div>
            <div class="program-text-en">ELA / Reading</div>
          </div>
        </div>
      </div>

      <!-- TEST PREP & ESL -->
      <div class="program-col shsat">
        <div class="program-title">Test tayyorgarlik va ESL</div>
        <div class="program-title-en">TEST PREP & ESL</div>
        <div class="program-divider" style="background:#C8341B;"></div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">Regents</div>
            <div class="program-text-en">Regents</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">SAT</div>
            <div class="program-text-en">SAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">SHSAT</div>
            <div class="program-text-en">SHSAT</div>
          </div>
        </div>
        <div class="program-row">
          <span class="check">✓</span>
          <div>
            <div class="program-text-uz">ESL Ko'prik</div>
            <div class="program-text-en">ESL Bridge</div>
          </div>
        </div>
      </div>
    </div>

    <!-- HOURS CARD -->'''

    html = html[: old.start()] + new_block + html[old.end():]
    return html


def update_flyer_pricing(html):
    # Ensure any 250 is replaced with 265 in pricing contexts
    html = html.replace("$250", "$265")
    html = html.replace("$২৫০", "$২৬৫")
    return html


# ---------------------------------------------------------------------------
# Banners
# ---------------------------------------------------------------------------

def remove_banner_logo(html, lang):
    # Remove the logo-circle div (keep wordmark)
    html = re.sub(
        r'<div class="logo-circle">\s*<img[^>]*alt="Badal Tutorial logo"[^>]*>\s*</div>\s*',
        "",
        html,
    )
    # Also remove the unused .logo-mark CSS if it was still there
    return html


def update_banner_8plus(html, lang):
    if lang == "en":
        html = html.replace(
            '<div style="font-family:\'Noto Sans\',sans-serif;font-weight:900;font-size:2.6in;color:#D4A017;line-height:1;">8+</div>',
            '<div style="font-family:\'Noto Sans\',sans-serif;font-weight:900;font-size:2.6in;color:#D4A017;line-height:1;">18+</div>',
        )
    else:  # bn
        html = html.replace(
            '<div style="font-family:\'Noto Sans\',sans-serif;font-weight:900;font-size:2.6in;color:#D4A017;line-height:1;">৮+</div>',
            '<div style="font-family:\'Noto Sans\',sans-serif;font-weight:900;font-size:2.6in;color:#D4A017;line-height:1;">১৮+</div>',
        )
    return html


def update_banner_programs_en(html):
    # Replace subjects-pills block
    old = re.search(
        r'(<div class="subjects-pills">).*?(</div>\s*</div>\s*<!-- CTA BAR -->)',
        html,
        re.DOTALL,
    )
    if not old:
        return html

    # Reduce pill size a bit so 12-14 pills fit in the 6in subjects bar
    html = html.replace(
        '.pill { background:#FAF7F0; color:#1B3A5C; padding:0.6in 1.2in; border-radius:2.5in; font-family:\'Noto Sans\',sans-serif; font-weight:900; font-size:1.7in; letter-spacing:0.05in; text-transform:uppercase; border:0.12in solid #D4A017; }',
        '.pill { background:#FAF7F0; color:#1B3A5C; padding:0.4in 0.8in; border-radius:2.5in; font-family:\'Noto Sans\',sans-serif; font-weight:900; font-size:1.35in; letter-spacing:0.05in; text-transform:uppercase; border:0.12in solid #D4A017; }',
    )

    new_pills = '''    <div class="subjects-pills">
      <div class="pill">★ ESL ★</div>
      <div class="pill">★ MATH ★</div>
      <div class="pill">★ ALGEBRA I & II ★</div>
      <div class="pill">★ GEOMETRY ★</div>
      <div class="pill">★ SCIENCE ★</div>
      <div class="pill">★ LIVING ENV ★</div>
      <div class="pill">★ EARTH SCI ★</div>
      <div class="pill">★ CHEMISTRY ★</div>
      <div class="pill">★ US HISTORY ★</div>
      <div class="pill">★ GLOBAL HISTORY ★</div>
      <div class="pill">★ ELA ★</div>
      <div class="pill">★ REGENTS ★</div>
      <div class="pill">★ SAT ★</div>
      <div class="pill">★ SHSAT ★</div>
    </div>
  </div>

  <!-- CTA BAR -->'''

    html = html[: old.start()] + new_pills + html[old.end():]
    return html


def update_banner_programs_bn(html):
    old = re.search(
        r'(<div class="subjects-pills">).*?(</div>\s*</div>\s*<!-- CTA BAR -->)',
        html,
        re.DOTALL,
    )
    if not old:
        return html

    html = html.replace(
        '.pill { background:#FAF7F0; color:#1B3A5C; padding:0.6in 1.2in; border-radius:2.5in; font-family:\'Noto Sans\',sans-serif; font-weight:900; font-size:1.7in; letter-spacing:0.05in; text-transform:uppercase; border:0.12in solid #D4A017; }',
        '.pill { background:#FAF7F0; color:#1B3A5C; padding:0.4in 0.8in; border-radius:2.5in; font-family:\'Noto Sans\',sans-serif; font-weight:900; font-size:1.35in; letter-spacing:0.05in; text-transform:uppercase; border:0.12in solid #D4A017; }',
    )

    new_pills = '''    <div class="subjects-pills">
      <div class="pill">★ ESL ★</div>
      <div class="pill">★ গণিত ★</div>
      <div class="pill">★ অ্যালজেব্রা ১ ও ২ ★</div>
      <div class="pill">★ জ্যামিতি ★</div>
      <div class="pill">★ বিজ্ঞান ★</div>
      <div class="pill">★ লিভিং এনভায়রনমেন্ট ★</div>
      <div class="pill">★ পৃথিবী বিজ্ঞান ★</div>
      <div class="pill">★ রসায়ন ★</div>
      <div class="pill">★ মার্কিন ইতিহাস ★</div>
      <div class="pill">★ বিশ্ব ইতিহাস ★</div>
      <div class="pill">★ ELA ★</div>
      <div class="pill">★ রিজেন্টস ★</div>
      <div class="pill">★ SAT ★</div>
      <div class="pill">★ SHSAT ★</div>
    </div>
  </div>

  <!-- CTA BAR -->'''

    html = html[: old.start()] + new_pills + html[old.end():]
    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Flyers
    for lang, path in [
        ("bn", ROOT / "flyers/bn/unified-bn.html"),
        ("zh", ROOT / "flyers/zh/unified-zh.html"),
        ("uz", ROOT / "flyers/uz/unified-uz.html"),
    ]:
        html = read(path)
        html = remove_flyer_logo(html)
        html = update_flyer_pricing(html)
        if lang == "bn":
            html = update_flyer_programs_bn(html)
        elif lang == "zh":
            html = update_flyer_programs_zh(html)
        elif lang == "uz":
            html = update_flyer_programs_uz(html)
        write(path, html)

    # Banners
    for lang, path in [("en", ROOT / "banners/banner-en.html"), ("bn", ROOT / "banners/banner-bn.html")]:
        html = read(path)
        html = remove_banner_logo(html, lang)
        html = update_banner_8plus(html, lang)
        if lang == "en":
            html = update_banner_programs_en(html)
        else:
            html = update_banner_programs_bn(html)
        write(path, html)


if __name__ == "__main__":
    main()
