"""実践答練 第2回（択一式 第1問〜第20問）の記事を組み立てる共通部品。

記事の本文（導入文〜見出し画像用フレーズ）は body/qNN.md に手で書き、
問題文・正解・図解・見出し画像の指定は specs.py に書く。
build.py が両方を合わせて、../qNN-xxx.md を作る。
"""
import re

ANS_LABELS = "アイウエオ"

# 画像生成AIが簡体字にしやすい漢字（そのプロンプト自身に登場するものだけを Final check に挙げる）
RISKY_KANJI = list(
    "誤権録登記地番建物所請還区分併筆界特定懲戒処聴聞委嘱届経由譲渡続償与護解除催隣竹枝囲障壁識別通補正"
    "敷効継承閉鎖滅失附属図面測量変更更抹消存続転写割合賃借担保抵当証券共有管轄限務連"
)


def quote_block(spec):
    """問題文の引用ブロック（format-template の書式：各行の間に全角スペースだけの行、行末に半角スペース2つ）。"""
    lines = []
    for item in spec["quote"]:
        lines.append(item)
    out = []
    for i, l in enumerate(lines):
        last = i == len(lines) - 1
        out.append("> " + l + ("" if last else "  "))
        if not last:
            out.append(">　  ")
    return "\n".join(out)


def quote_block_dialogue(spec):
    """教授・学生の対話形式の問題文（発言の間に空の引用行を入れる）。"""
    out = []
    items = spec["quote"]
    for i, l in enumerate(items):
        last = i == len(items) - 1
        out.append("> " + l + ("" if last else "  "))
        if not last:
            out.append(">")
    return "\n".join(out)


def pick_kanji(text, limit=16):
    seen = []
    for k in RISKY_KANJI:
        if k in text and k not in seen:
            seen.append(k)
    # 登場回数の多い順
    seen.sort(key=lambda k: -text.count(k))
    return seen[:limit]


CRIT = """CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
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
kanji {kanji}, which have visually
similar but structurally different Simplified Chinese counterparts —
always draw the standard Japanese (Jōyō) form."""

BG = """BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the cards/columns — with a solid or illustrated opaque
background (the pale beige/gray tone used elsewhere in this style is a
good default). There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image."""

GLANCE = """GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the cards. Every card must communicate its point almost entirely
through the illustration (icons, X marks, checkmarks, small embedded
labels) plus one short heading and one short conclusion tag. Do NOT render
any full-sentence explanation, legal citation, or paragraph of body text
anywhere on the poster. If a piece of information cannot be expressed as a
short label (a few words) or drawn as an icon, leave it out rather than
writing it as prose."""

COLOR_RULE = """COLOR RULE (critical): Use green for every "yes / allowed / correct" mark (checkmarks) and red
for every "no / not allowed / not required" mark (✕ marks). Never use blue for a checkmark. One box or
card shows only ONE kind of mark — never a checkmark and a ✕ together in the same box."""


def infographic_prompt(spec):
    g = spec["info"]
    cols = g.get("columns")  # None または [(ラベル, 色), (ラベル, 色)]
    cards = g["cards"]
    title = "\n".join(g["title"])
    parts = []
    # 本文（カード部分）を先に作って、漢字リストをそこから拾う
    body = []
    body.append("--- HEADER ---")
    body.append("Title (large, bold, %d行):" % len(g["title"]))
    body.append(title)
    body.append("")
    body.append("Subtitle (smaller, centered, 1行):")
    body.append(g["subtitle"])
    body.append("")
    body.append("（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の")
    body.append("ブロックは置かない。）")
    body.append("")
    colname = {}
    if cols:
        for lab, colr in cols:
            colname[lab] = colr
    cur_col = None
    n = 0
    for c in cards:
        n += 1
        if cols:
            lab = c["col"]
            if lab != cur_col:
                cur_col = lab
                body.append("--- COLUMN %s HEADER (pill-shaped badge, color: %s) ---" % ("AB"[[x[0] for x in cols].index(lab)], colname[lab]))
                body.append(lab)
                body.append("")
            colr = colname[lab]
            head = "--- COLUMN %s, CARD %d ---" % ("AB"[[x[0] for x in cols].index(lab)], n)
        else:
            colr = g.get("color", "green")
            head = "--- CARD %d ---" % n
        body.append(head)
        body.append("Badge: a filled %s circle containing the number %d." % (colr, n))
        body.append("Heading (bold, ONE line, ~20 characters or fewer):")
        body.append(c["heading"])
        body.append("Illustration: " + c["illust"])
        body.append("Conclusion tag (%s banner below the illustration, 5-15 characters):" % colr)
        body.append(c["tag"])
        body.append("")
    body_text = "\n".join(body)
    kanji = "・".join(pick_kanji(body_text))

    head = [
        "Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,",
        "clean flat-design isometric illustration style with soft pastel colors",
        "(blue, green, beige, gray), rounded card sections, consistent with a",
        "modern explainer-graphic aesthetic (icons: %s — adapt icon" % g["icons"],
        "set to the topic).",
        "",
        GLANCE,
        "",
        CRIT.format(kanji=kanji),
        "",
        BG,
        "",
        COLOR_RULE,
        "",
    ]
    foot = [
        "--- FOOTER ---",
        "",
        "Final check before rendering: scan every kanji glyph and confirm it is",
        "standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, especially",
        "%s. If any character renders" % kanji,
        "as a Simplified or Traditional Chinese variant, redraw that character in the correct",
        "Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji — including any Chinese-only character, Korean Hangul, other non-Japanese script, or stray decorative glyph — and remove or redraw it so that only standard Japanese text appears anywhere in the image. Confirm the number of cards equals %d exactly, with no" % len(cards),
        "duplicated or missing cards, that badge numbers run 1-%d continuously" % len(cards),
        "across all columns without resetting, confirm there is no intro",
        "illustration or paragraph block between the header and the cards, and",
        "confirm that no card contains a full sentence of explanatory prose —",
        "every card's takeaway must read as a short heading + a short conclusion",
        "tag, at a glance. Confirm that no box shows both a checkmark and a ✕ at the same time, and that every checkmark is green and every ✕ is red. Confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid of all 肢, and no additional text block of any kind — the image ends immediately after the last card). Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.",
    ]
    return "\n".join(head) + "\n" + body_text + "\n" + "\n".join(foot)


def midashi_prompt(spec):
    m = spec["midashi"]
    lines = [m["line1"]] + ([m["line2"]] if m.get("line2") else [])
    text_all = "".join(lines) + m["subtitle"] + m["left"] + m["right"]
    kanji = "・".join(pick_kanji("".join(lines) + m["subtitle"], 14))
    two = len(lines) == 2
    p = []
    p.append("Create a note.com article header image (eyecatch thumbnail), 1280x670px")
    p.append("(1.91:1 landscape aspect ratio).")
    p.append("")
    p.append("STYLE: full-color flat-design isometric illustration with soft pastel colors (blue, green, beige, gray), rounded shapes, clean outlines, consistent with the other note.com explainer-graphic images of this series. One simple scene, not a poster: a clear uncluttered zone for the title at the top center, and the topic icons placed softly on the left and right sides. Do not draw any human face close-up; if people appear, draw them as small simple isometric figures.")
    p.append("Fill the whole canvas with a pale sky-blue to cream gradient background.")
    p.append("")
    p.append(CRIT.format(kanji=kanji).replace("Pay special attention", "Arabic numerals 0-9 are allowed ONLY inside the subtitle band. Pay special attention"))
    p.append("")
    p.append(BG)
    p.append("")
    p.append("TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in %s at the top center, over a soft white rounded glow so it reads clearly. %s" % (
        "two lines" if two else "one line",
        "Line 1 is dark navy:" if two else "The title is dark navy:"))
    p.append(lines[0])
    if two:
        if m.get("key"):
            p.append("Line 2 is larger and dark navy, with the phrase 「%s」 in red-orange:" % m["key"])
        else:
            p.append("Line 2 is larger and dark navy:")
        p.append(lines[1])
    p.append("Below the title, a light blue rounded pill-shaped subtitle band with navy text:")
    p.append(m["subtitle"])
    p.append("Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.")
    p.append("")
    p.append("TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title):")
    p.append("Left side: " + m["left"])
    p.append("Right side: " + m["right"])
    p.append("")
    p.append("LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the title and the main icons near the center and away from the extreme edges, so that the image survives the center cropping that note applies (the article list shows only the middle 1280x454 band). Do not draw any flowchart, diamond, arrow between boxes, checkmark, or cross mark.")
    p.append("")
    p.append("Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the title and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji %s; if any character renders as a Chinese variant, redraw it in the correct Japanese form; scan the whole canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji (the digits in the subtitle band excepted) and remove it; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere." % kanji)
    return "\n".join(p)
