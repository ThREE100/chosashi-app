# -*- coding: utf-8 -*-
"""各記事（qNN-*.md）の末尾に、総論インフォグラフィック（②問題全体）と見出し画像（①）の
プロンプトを生成して付ける。記事本文は変更しない（「## インフォグラフィック プロンプト（問題全体）」
より後ろだけを作り直す）。

使い方：  python3 build.py            （全20問）
          python3 build.py 3 7        （第3問・第7問だけ）
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cards import Q  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MARK = "## インフォグラフィック プロンプト（問題全体）"

# Final check で「特に注意する漢字」の候補。実際にそのプロンプトに登場するものだけを使う。
KANJI_CANDIDATES = (
    "録権登記物地図測量図書筆界請求承諾抹消閉鎖転写移併附属敷専有共用区分団還付証印鑑謄遺産分割続"
    "配偶譲渡解除錯誤意思表示効力到達亡未成年産持分申請情報調査士法人関与受任脱退退職更正変更滅失"
    "表題管轄冠例外署名縮尺方位積担保抵当役承役要役貸借"
)

COLOR_NAME = {"green": "green", "blue": "blue"}
COL_LETTER = ["A", "B"]


def pick_kanji(text, limit=14):
    cnt = Counter(ch for ch in text if ch in KANJI_CANDIDATES)
    return [k for k, _ in cnt.most_common(limit)]


def info_prompt(n, d):
    cards = d["cards"]
    assert 4 <= len(cards) <= 6, (n, "カード数")
    cols = d["cols"]
    # 列の順に並んでいるか
    assert [c["col"] for c in cards] == sorted(c["col"] for c in cards), (n, "列の順")
    for c in cards:
        assert len(c["h"]) <= 20, (n, "見出しが20字超", c["h"], len(c["h"]))
        assert 5 <= len(c["tag"]) <= 15, (n, "結論タグが5〜15字でない", c["tag"], len(c["tag"]))
    subtitle = f"{d['theme']}(実践答練 第3回 第{n}問)"
    title = "\n".join(d["title"])

    body = []
    # 本体（Final check の漢字リスト算出用に、描画対象の日本語を集める）
    jp_text = title + subtitle + "".join(l for l, _ in cols)
    for c in cards:
        jp_text += c["h"] + c["tag"] + c["ill"]

    kan = pick_kanji(jp_text)
    kan_s = "・".join(kan)

    head = f"""Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric buildings, land
plots, stamps, torn paper labels, etc. — adapt icon set to the topic).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the cards. Every card must communicate its point almost entirely
through the illustration (icons, small embedded labels) plus one short
heading and one short conclusion tag. Do NOT render any full-sentence
explanation, legal citation, or paragraph of body text anywhere on the
poster. If a piece of information cannot be expressed as a short label (a
few words) or drawn as an icon, leave it out rather than writing it as
prose.

MARK RULE (critical): Draw a red ✕ mark ONLY on the cards whose
illustration below explicitly asks for one. Never draw ○ or ✓ marks
anywhere, never draw a ✕ on a card that does not ask for it, and never draw
the same mark on both sides of a contrasting pair. Do not invent any
number, amount, percentage, land number or person that is not written below.
Do not write any case number or precedent number anywhere.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Every kanji must match standard Japanese
orthography exactly as written below, stroke-for-stroke. Reproduce the
exact text strings given below verbatim — do not paraphrase, translate,
summarize, or substitute any characters. Pay special attention to the
kanji {kan_s} — these
must be rendered in their standard Japanese forms, never as Simplified
Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the cards/columns — with a solid or illustrated opaque
background (the pale beige/gray tone used elsewhere in this style is a
good default). There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, {len(d['title'])}行):
{title}

Subtitle (smaller, centered, 1行):
{subtitle}

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の
ブロックは置かない。）
"""
    body.append(head)

    num = 0
    per_col = [0, 0]
    for ci, (label, color) in enumerate(cols):
        L = COL_LETTER[ci]
        body.append(f"""
--- COLUMN {L} HEADER (pill-shaped badge, color: {COLOR_NAME[color]}) ---
{label}
""")
        for c in [x for x in cards if x["col"] == ci]:
            num += 1
            per_col[ci] += 1
            body.append(f"""
--- COLUMN {L}, CARD {num} ---
Badge: a filled {COLOR_NAME[color]} circle containing the number {num}.
Heading (bold, ONE line, ~20 characters or fewer):
{c['h']}
Illustration: {c['ill']}
Conclusion tag (a short {COLOR_NAME[color]} banner below the illustration, 5-15 characters):
{c['tag']}
""")
    foot = f"""
--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special
attention to {kan_s} and any
character that has a visually similar Simplified Chinese variant. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji — including any Chinese-only character, Korean Hangul, other non-Japanese script, or stray decorative glyph — and remove or redraw it so that only standard Japanese text appears anywhere in the image. If any character
renders as a Simplified or Traditional Chinese variant, redraw that character in the
correct Japanese form. Confirm the number of cards equals {num} exactly ({per_col[0]}
cards under the column A header and {per_col[1]} cards under the column B header), with no duplicated or missing cards, that badge
numbers run 1-{num} continuously across both columns without resetting,
confirm there is no intro illustration or paragraph block between the
header and the cards, and confirm that no card contains a full sentence
of explanatory prose — every card's takeaway must read as a short heading
+ a short conclusion tag, at a glance. Confirm every ✕ mark appears only on the cards that explicitly ask for it and no ○ or ✓ mark appears anywhere. Confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid of all 肢, and no additional text block of any kind — the image ends immediately after the last card). Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
"""
    body.append(foot)
    return "".join(body), per_col, kan


def header_prompt(n, d):
    h = d["hdr"]
    sub = f"実践答練 第3回 第{n}問"
    jp = h["l1"] + h["l2"] + sub
    kan = pick_kanji(jp + d["theme"], 10) or ["登", "記"]
    # ヘッダー画像の文字に実際に登場する難しい漢字だけを挙げる
    kan_h = [k for k in dict.fromkeys(ch for ch in (h["l1"] + h["l2"] + sub) if "一" <= ch <= "鿿")]
    kan_s = "、".join(kan_h)
    return f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: full-color flat-design isometric illustration with soft pastel colors
(blue, green, beige, gray), rounded shapes, consistent with the other
isometric explainer graphics of this note series. One single, simple scene
that expresses the theme of the article at a glance; no characters are
required (small, faceless isometric people icons are allowed).

LAYOUT: the title block sits at the top center, and the scene illustration
fills the area around and below it. Keep the title, the subtitle and the
main parts of the scene inside the central band of the image (about
1280x454px), so that the image survives the automatic center cropping of
the note article list. Keep a clear, uncluttered zone behind the title.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas, including every corner and
margin, with an opaque illustrated background (a pale sky-blue to cream
gradient is a good default). There must be no checkerboard pattern, no
partially transparent area, and no unpainted canvas edge anywhere in the
final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese
title in two lines at the top center, dark navy on a soft white glow so it
reads clearly:
{h['l1']}
{h['l2']}
Below the title, a light blue rounded pill-shaped subtitle band with navy
text:
{sub}
Do not write any other text anywhere in the image: no captions, no labels,
no signs with letters, no watermark, no panel numbers, no case numbers.

SCENE (illustration only, no text on any object): {h['scene']}. Draw it
soft and slightly faded toward the left and right edges so that it never
competes with the title.

Do not draw any flowchart, decision diamond, check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670
landscape; confirm the only text in the whole image is the two title lines
and the subtitle, reproduced exactly as written; scan every kanji glyph and
confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and
not Traditional Chinese, paying special attention to the kanji {kan_s}; if
any character renders as a Chinese variant, redraw it in the correct
Japanese form; and confirm the entire canvas, edge to edge, is filled with
a fully opaque background with no transparency or alpha channel.
"""


def tail(n, d):
    ip, per_col, kan = info_prompt(n, d)
    cols = d["cols"]
    desc1 = (
        f"その問題の5肢の正しいルールを、「{cols[0][0]}」（緑）と「{cols[1][0]}」（青）の2列・"
        f"{len(d['cards'])}枚の俯瞰カードポスターにまとめる構成です。通し番号バッジ・短い見出し・図解・短い結論タグだけで構成し、"
        "誤りの肢は正しい形に直して図解しています。"
    )
    desc2 = (
        "noteの見出し画像（1280×670px・比率1.91:1）用のプロンプトです。フルカラー・淡いパステルのアイソメトリック・"
        "フラットデザインで、問題のテーマを1シーンで表します。画像内の文字は、タイトル2行とサブタイトルだけです。"
    )
    hp = header_prompt(n, d)
    out = []
    out.append(f"{MARK}\n\n{desc1}\n\n```\n{ip}```\n")
    out.append(f"\n---\n\n## 見出し画像プロンプト\n\n{desc2}\n\n```\n{hp}```\n")
    return "\n".join(out)


def main(argv):
    targets = [int(a) for a in argv] or sorted(Q)
    for n in targets:
        d = Q[n]
        path = os.path.join(ROOT, d["file"])
        s = open(path, encoding="utf-8").read()
        i = s.find(MARK)
        if i >= 0:
            s = s[:i].rstrip("\n") + "\n"
        s = s.rstrip("\n") + "\n\n---\n\n" + tail(n, d)
        open(path, "w", encoding="utf-8").write(s)
        print("built", d["file"])


if __name__ == "__main__":
    main(sys.argv[1:])
