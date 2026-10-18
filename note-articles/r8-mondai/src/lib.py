# -*- coding: utf-8 -*-
"""令和8年度 択一式の解説記事を組み立てる共通部品。

- 問題文は exam-data/R08/takuitsu_R08_questions.json から読む（手で打ち直さない）。
- 見出し画像プロンプト・②問題全体・④間違いノートのプロンプトは、元データから組み立てる。
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)          # note-articles/r8-mondai
REPO = os.path.dirname(os.path.dirname(ROOT))
NOTE = os.path.dirname(ROOT)           # note-articles
EXAM = json.load(open(os.path.join(REPO, "exam-data", "R08", "takuitsu_R08_questions.json"), encoding="utf-8"))
QS = {q["questionNo"]: q for q in EXAM["questions"]}

# 予備校の解答速報（2026-10-18公開）の正解番号。法務省の公式正答の公表後に照合する。
ANSWER = {1: 1, 2: 3, 3: 3, 4: 3, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 4,
          11: 1, 12: 4, 13: 4, 14: 5, 15: 5, 16: 4, 17: 2, 18: 5, 19: 3, 20: 2}
WRONG_Q = {2, 7, 15, 17, 18}   # 設問が「誤っているもの」を問う
LET = "アイウエオ"


def combo(n):
    q = QS[n]
    return [c["text"] for c in q["combos"] if c["no"] == ANSWER[n]][0]


CANDIDATES = (
    "登記録権地建物図書請求還併測量条号証変更筆界特定続相欠格預貯金処分規約共用部敷区分合体抹消確認法定調査士業務"
    "破産取消停止判決錯誤虚偽強迫詐欺裁判所競売価賠償譲渡義務転許可農業委員会却下取下完了通知訂正申出区画整理換地"
    "仮従前覧説領認裁量属帳簿保存期間検査関係産続時効占有承継賃借役隣竹木囲繞通行袋設備給付図郭座標街境界"
    "抵当信託買戻順位現況目的附属床面積窓塔屋吹抜滅失借代位移転移送在順序橋"
)
NUM = "〇一二三四五六七八九"


def kansuji(n):
    if n < 10:
        return NUM[n]
    if n == 10:
        return "十"
    if n < 20:
        return "十" + NUM[n - 10]
    if n == 20:
        return "二十"
    raise ValueError(n)


def attention_kanji(text, limit=22):
    seen = []
    for ch in text:
        if ch in CANDIDATES and ch not in seen:
            seen.append(ch)
    return seen[:limit]


def kanji_in(text):
    out = []
    for ch in text:
        if "一" <= ch <= "鿿" and ch not in out:
            out.append(ch)
    return out


def C(h, ill, tag):
    return {"h": h, "ill": ill, "tag": tag}


COL_LABELS = ["A", "B"]


def infographic(n, d):
    cols = d["cols"]
    single = cols[0][0] is None
    title = d["info_title"]
    subtitle = "{} (令和8年度 第{}問)".format(d["theme"], n)
    texts = [title, subtitle]
    for label, color, cards in cols:
        if label:
            texts.append(label)
        for c in cards:
            texts += [c["h"], c["tag"], c["ill"]]
    kanji_txt = "・".join(attention_kanji("".join(texts)))
    total = sum(len(c[2]) for c in cols)
    if single:
        count_desc = "{} cards in a single column".format(total)
    else:
        count_desc = " and ".join("{} cards under 「{}」".format(len(cards), label) for label, color, cards in cols)
    L = []
    a = L.append
    a("Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,")
    a("clean flat-design isometric illustration style with soft pastel colors")
    a("(blue, green, beige, gray), rounded card sections, consistent with a")
    a("modern explainer-graphic aesthetic (icons: isometric buildings, land")
    a("plots, stamps, torn paper labels, etc. — adapt icon set to the topic).")
    a("")
    a("GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,")
    a("NOT a text-heavy explainer document. There is NO intro illustration and NO")
    a("paragraph of prose anywhere on this poster — go straight from the header")
    a("to the cards. Every card must communicate its point almost entirely")
    a("through the illustration (icons, X marks, checkmarks, small embedded")
    a("labels) plus one short heading and one short conclusion tag. Do NOT render")
    a("any full-sentence explanation, legal citation, or paragraph of body text")
    a("anywhere on the poster. If a piece of information cannot be expressed as a")
    a("short label (a few words) or drawn as an icon, leave it out rather than")
    a("writing it as prose.")
    a("")
    a("CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese")
    a("only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use")
    a("Simplified Chinese characters (simplified hanzi) under any circumstances,")
    a("even if a character looks similar. Do NOT use Traditional Chinese")
    a("characters (traditional hanzi) either, even where a traditional-hanzi")
    a("glyph looks close to the correct Japanese kanji form — every glyph must")
    a("match the standard Japanese Jōyō form exactly, not the Chinese")
    a("traditional variant. Do NOT render any character that is not standard")
    a("Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —")
    a("no Chinese-only characters, no Korean Hangul, no other non-Japanese")
    a("script, and no stray or decorative glyphs of any kind, even as small")
    a("background or texture elements. Every kanji must match standard Japanese")
    a("orthography exactly as written below, stroke-for-stroke. Reproduce the")
    a("exact text strings given below verbatim — do not paraphrase, translate,")
    a("summarize, or substitute any characters. Pay special attention to the")
    a("kanji {} — these".format(kanji_txt))
    a("must be rendered in their standard Japanese forms, never as Simplified")
    a("Chinese variants.")
    a("")
    a("BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque")
    a("from edge to edge. Do NOT generate a transparent or alpha-channel")
    a("background under any circumstances, even if the output file format")
    a("supports transparency. Fill the full canvas — including every corner and")
    a("margin outside the cards/columns — with a solid or illustrated opaque")
    a("background (the pale beige/gray tone used elsewhere in this style is a")
    a("good default). There must be no checkerboard pattern, no partially")
    a("transparent area, and no unpainted canvas edge anywhere in the final")
    a("image.")
    a("")
    a("COLOR RULE FOR MARKS: any check mark is drawn in green and any cross or")
    a("prohibition mark is drawn in red, regardless of the color of the column it")
    a("sits in. Draw only the legally correct rule on every card; never draw a")
    a("sentence that states a wrong rule.")
    a("")
    a("--- HEADER ---")
    a("Title (large, bold, 1行):")
    a(title)
    a("")
    a("Subtitle (smaller, centered, 1行):")
    a(subtitle)
    a("")
    a("（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の")
    a("ブロックは置かない。）")
    a("")
    num = 0
    for ci, (label, color, cards) in enumerate(cols):
        col_name = "COLUMN " + COL_LABELS[ci]
        if not single:
            a("--- {} HEADER (pill-shaped badge, color: {}) ---".format(col_name, color))
            a(label)
            a("")
        for c in cards:
            num += 1
            a("--- CARD {} ---".format(num) if single else "--- {}, CARD {} ---".format(col_name, num))
            a("Badge: a filled {} circle containing the number {} (numbers".format(color, num))
            a("run continuously across all columns — do not restart at 1 in column B).")
            a("Heading (bold, ONE line, ~20 characters or fewer):")
            a(c["h"])
            a("Illustration: {}".format(c["ill"]))
            a("Conclusion tag ({} banner below the illustration, 5-15 characters,".format(color))
            a("a keyword phrase — NOT a sentence, NOT a legal citation):")
            a(c["tag"])
            a("")
    a("--- FOOTER ---")
    a("")
    a("Final check before rendering: scan every kanji glyph and confirm it is")
    a("standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special")
    a("attention to {}. Also scan the entire canvas for any character that is not standard Japanese".format(kanji_txt))
    a("hiragana, katakana, or Jōyō kanji — including any Chinese-only character, Korean Hangul, other")
    a("non-Japanese script, or stray decorative glyph — and remove or redraw it so that only standard")
    a("Japanese text appears anywhere in the image. If any character renders as a Simplified or")
    a("Traditional Chinese variant, redraw that character in the correct Japanese form. Confirm the")
    a("number of cards equals {} exactly ({}), with no duplicated or missing cards,".format(total, count_desc))
    a("that badge numbers run 1-{} continuously without resetting,".format(total))
    a("confirm there is no intro illustration or paragraph block between the")
    a("header and the cards, and confirm that no card contains a full sentence of explanatory prose —")
    a("every card's takeaway must read as a short heading + a short conclusion tag, at a glance.")
    a("Confirm no card states a false rule — every card must show the legally correct rule only.")
    a("Confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon,")
    a("no re-listed ○/✕ grid of all 肢, and no additional text block of any kind — the image ends")
    a("immediately after the last card). Confirm the entire canvas, edge to edge, is filled with a")
    a("fully opaque background with no transparency or alpha channel anywhere.")
    return "\n".join(L)


def header_prompt(n, d):
    l1, l2, hl = d["h_l1"], d["h_l2"], d["h_hl"]
    assert hl in l2, (n, hl, l2)
    sub = "令和八年度　午後の部　第{}問　{}".format(kansuji(n), d["h_sub_topic"])
    for s in (l1, l2, sub):
        assert not re.search(r"[0-9A-Za-z０-９]", s), (n, s)
    rest = l2.replace(hl, "")
    kj = "、".join(kanji_in(l1 + l2 + sub))
    if rest:
        line2 = "Line 2 is larger; the phrase {} is red-orange and the rest is dark navy:".format(hl)
    else:
        line2 = "Line 2 is larger and red-orange:"
    return """Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the single character at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): this header image features ONE female character only: 藍子. Do NOT draw トリ先生 (the bird teacher) or any other character, person, or animal besides 藍子. Follow the attached 藍子 character-specification images exactly and do not redesign her. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the bottom center. POSE IS NOT FIXED: do not copy any pose from the attached images or from earlier header images; let her take a free, natural pose of your own choosing that fits the topic and suits her (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep her fully visible, with her face clear of the title text, and keep her hairstyle exactly as in the attached images. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
{l1}
{line2}
{l2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{sub}
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: {left}
Right side: {right}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the character and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {kj}; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm 藍子 is the only character in the image (no トリ先生), that she matches the attached references, and that she keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.""".format(
        l1=l1, line2=line2, l2=l2, sub=sub, left=d["h_left"], right=d["h_right"], kj=kj)


def mistake_prompt(n, letter, m):
    """④ 間違いノート型。m: title, sub, kind('FLOWCHART'|'COMPARISON'), body(list[str]), callout(list[str]), footer"""
    texts = [m["title"], m["sub"]] + m["body"] + m["callout"] + [m["footer"]]
    kj = "・".join(attention_kanji("".join(texts), 26))
    L = []
    a = L.append
    a("Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,")
    a("clean flat-design isometric illustration style with soft pastel colors")
    a("(blue, green, beige, gray), rounded panel sections, consistent with the")
    a("same visual language as the whole-problem poster for this article, but")
    a("built as a single detailed explainer panel rather than a multi-card")
    a("poster.")
    a("")
    a("MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: This image exists to resolve one")
    a("specific point of confusion, not to be a glanceable summary. Unlike a")
    a("quick-reference poster, this image MAY include flowchart branches with")
    a("written conditions, side-by-side comparisons with quoted article text,")
    a("and short explanatory sentences (1-3 sentences per callout box) labeled")
    a("「誤りやすいポイント」or similar. Prioritize clarity and completeness of")
    a("the reasoning over brevity. Use a green check mark for the correct rule")
    a("and a red cross mark for the wrong rule; never write any person's study")
    a("record, answer history, or past question numbers in the image.")
    a("")
    a("CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese")
    a("only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use")
    a("Simplified Chinese characters (simplified hanzi) under any circumstances,")
    a("even if a character looks similar. Do NOT use Traditional Chinese")
    a("characters (traditional hanzi) either, even where a traditional-hanzi")
    a("glyph looks close to the correct Japanese kanji form — every glyph must")
    a("match the standard Japanese Jōyō form exactly, not the Chinese")
    a("traditional variant. Do NOT render any character that is not standard")
    a("Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —")
    a("no Chinese-only characters, no Korean Hangul, no other non-Japanese")
    a("script, and no stray or decorative glyphs of any kind, even as small")
    a("background or texture elements. Reproduce the exact text strings given")
    a("below verbatim — do not paraphrase, translate, summarize, or substitute")
    a("any characters. Pay special attention to the kanji {} — always".format(kj))
    a("draw the standard Japanese (Jōyō) form.")
    a("")
    a("BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque")
    a("from edge to edge. Do NOT generate a transparent or alpha-channel")
    a("background under any circumstances, even if the output file format")
    a("supports transparency. Fill the full canvas — including every corner and")
    a("margin outside the panel/flowchart/comparison — with a solid or")
    a("illustrated opaque background. There must be no checkerboard pattern, no")
    a("partially transparent area, and no unpainted canvas edge anywhere in the")
    a("final image.")
    a("")
    a("--- HEADER ---")
    a("Title (large, bold):")
    a(m["title"])
    a("")
    a("Subtitle (smaller, centered):")
    a(m["sub"])
    a("")
    a("--- {} ---".format(m["kind"]))
    for b in m["body"]:
        a(b)
    a("")
    a("--- CALLOUT: 誤りやすいポイント ---")
    for c in m["callout"]:
        a(c)
    a("")
    a("--- FOOTER ---")
    a(m["footer"])
    a("")
    a("Final check before rendering: scan every kanji glyph and confirm it is")
    a("standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional")
    a("Chinese. Also scan the entire canvas for any character that is not")
    a("standard Japanese hiragana, katakana, or Jōyō kanji — including any")
    a("Chinese-only character, Korean Hangul, other non-Japanese script, or")
    a("stray decorative glyph — and remove or redraw it. Confirm every")
    a("heading, node label, and callout text matches the Japanese text given")
    a("above verbatim, with no paraphrasing and no substituted characters,")
    a("confirm nothing is rendered below the FOOTER's small footnote text (no")
    a("summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid, and")
    a("no additional text block of any kind), and confirm the entire canvas,")
    a("edge to edge, is filled with a fully opaque background with no")
    a("transparency or alpha channel anywhere.")
    return "\n".join(L)


def quote_block(n):
    q = QS[n]
    out = ["> " + q["stem"] + "  ", ">　  "]
    for a in q["alts"]:
        out.append("> {}　{}  ".format(a["label"], a["text"]))
        out.append(">　  ")
    if q.get("reference"):
        for line in q["reference"].split("\n"):
            out.append("> " + line + "  ")
        out.append(">　  ")
    out.append("> " + "　　".join("{}　{}".format(c["no"], c["text"]) for c in q["combos"]))
    return "\n".join(out)
