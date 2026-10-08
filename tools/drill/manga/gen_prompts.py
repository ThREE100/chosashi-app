#!/usr/bin/env python3
"""4コマ解説図解プロンプト（<ID>_prompt.md）の生成器。D0520_prompt.mdと同じ構成を、肢ごとの設計データ（SPECS）から作る。
使い方: python3 tools/drill/manga/gen_prompts.py [ID ...]   （省略時は全部）
生成後は必ず check_prompt.py を通すこと。設計（工程A）はSPECSに書く：登場人物の初出・矢印の意味・会話順・配色。
D0520_prompt.md は手作り（検品済みの見本）で、この生成器の対象外。"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
import ast
GARBLED = ast.literal_eval(re.search(r'GARBLED = (\{.*?\})', (HERE / "check_prompt.py").read_text(encoding="utf8")).group(1))
RISKY = set(re.search(r'RISKY = set\("([^"]+)"\)', (HERE / "check_prompt.py").read_text(encoding="utf8")).group(1))

HEAD = """Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers{LETTERS_OK}. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. {PARTIES}

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

{CONT}LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).{NOTE_LAYOUT}"""

HANDS = ["藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)",
         "藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)",
         "藍子's hands: ONE hand points at the diagram with an extended arm and the other hand hangs at her side or holds the clipboard; her hands are NOT clasped and no third hand appears",
         "藍子's hands: both hands raised in a small cheering fist (two hands in total)"]
CONT = "CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines."
MOODS = ["藍子 confident, トリ先生 exasperated but caring", "藍子 puzzled, トリ先生 explaining with a wing-pointer",
         "both characters point together at the same figure; 藍子 realizing", "藍子 relieved, トリ先生 smiling proudly"]
ARC = "confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4)"
OPPOSITE = ("IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; "
            "the right card shows a RED cross. Do not draw the same mark on both cards. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.")

OPPOSITE_LX = ("IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; "
               "the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.")

def article_title(i, src): return f"【土地家屋調査士受験生向け】4コマ解説図解{i}～{src}～"

def src_label(src):
    m = re.match(r"([HR])(\d+)-Q(\d+)(.+)$", src)
    era = "平成" if m.group(1) == "H" else "令和"; y = int(m.group(2))
    return f"{era}{'元' if (era == '令和' and y == 1) else y}年度　第{int(m.group(3))}問　{m.group(4)}"

def lead_text(lead1, src):
    return (lead1 + "\n\n択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（" + src_label(src) + "）。"
            "\n\n先に〇か×かを考えてから、読み進めてみてください。")

def q(t): return f"「{t}」"
def hlpart(h): return f" with the part {q(h)} highlighted in yellow" if h else ""

FIXED_OLD = "In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side."
FIXED_FLEX = ("In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. "
              "A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; "
              "in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble.")
CHARS_TXT = {
    "aiko": "ONLY 藍子 appears in this panel (no トリ先生), standing at the left and smaller than usual, so that the diagram can be drawn large",
    "tori": "ONLY トリ先生 appears in this panel (no 藍子), standing at the right and smaller than usual, so that the diagram or the items to memorize can be drawn large",
    "faces": "both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)",
    "side": "both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below)",
    "none": "NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large",
    "small": "both characters appear VERY SMALL (each about 110 px tall in total, clearly smaller than the full-size characters in the other panels, never more than one third of the panel height), 藍子 at the lower left corner and トリ先生 at the lower right corner, so that the diagram or the items to memorize fill the panel",
}

def build(sp):
    pan = sp["panels"]
    letters = sp.get("letters", "")
    letters_ok = (f", and the full-width letters {' '.join(letters)} only where specified below" if letters else "")
    if letters:
        parties = (f"The legal parties {', '.join(letters)} are NOT characters: draw them only as small, faceless, flat pictogram figures, "
                   "each with a small round label tag containing the full-width letter given in the text plan.")
    else:
        parties = "Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below."
    nl = (" Between panel 4 and the conclusion banner, a thin one-line note strip (about 50 px tall) with small text, as given in the NOTE LINE below." if sp.get("note") else "")
    flex = any(p.get("chars") for p in pan)
    head = HEAD.replace(FIXED_OLD, FIXED_FLEX) if flex else HEAD
    if any(p.get("chars") == "faces" for p in pan):
        head = head.replace("a character who is not drawn has no speech bubble.", "a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles.")
    body = head.replace("{LETTERS_OK}", letters_ok).replace("{PARTIES}", parties).replace("{NOTE_LAYOUT}", nl).replace("{CONT}", (CONT + "\n\n") if sp.get("cont", True) else "") + "\n\n"
    body += f"TITLE BANNER: text {q(sp['title'])} in large bold letters; the part {q(sp['title_hl'])} has a yellow highlighter marker.\n\n"
    rows = [("タイトル帯", "—", sp["title"], sp["title_hl"] and f"「{sp['title_hl']}」を黄色マーカー")]
    for i, p in enumerate(pan):
        n = i + 1
        cm = p.get("chars")
        if cm:
            assert cm in CHARS_TXT and p.get("mood"), "chars を指定するコマには mood も書く"
            who_hands = "" if cm in ("tori", "faces", "none") else f"; {p.get('hands', HANDS[i])}"
            body += f"PANEL {n} ({p['mood']}; {CHARS_TXT[cm]}{who_hands}):\n"
        else:
            body += f"PANEL {n} ({p.get('mood', MOODS[i])}; {p.get('hands', HANDS[i])}):\n"
        body += f"- Label tab: {q(p['label'])}\n"
        rows.append((f"コマ{n} 見出し", "ラベル", p["label"], "—"))
        if cm == "faces":
            nb = len(p["bubbles"]); rowh = min(120, 330 // max(nb, 1))
            body += ("- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). "
                     "The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. "
                     f"The RIGHT column is a vertical conversation of EXACTLY {nb} rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about {rowh} px tall, all rows the same height, never overlapping. "
                     "Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; "
                     "in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. "
                     f"So the right column shows exactly {nb} face icons and exactly {nb} speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. "
                     "The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.\n")
        if cm == "side":
            body += ("- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. "
                     "The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); "
                     "wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.\n")
        if p.get("opposite"): body += f"- {OPPOSITE_LX if p.get('opposite') == 'lx' else OPPOSITE}\n"
        for ln in p["fig"]: body += f"- {ln}\n"
        figstr = []
        for ln in p["fig"]:
            for t in re.findall(r"「([^」]+)」", ln):
                if t not in figstr: figstr.append(t)
        rows.append((f"コマ{n} 図", "図・カード", " / ".join(figstr), "—"))
        for k, b in enumerate(p["bubbles"], 1):
            who, text, hl = b[:3]
            brk = b[3] if len(b) > 3 else None
            assert not hl or hl in text, f"{sp['id']}: 強調語が台詞にない: {hl}"
            assert not brk or brk.replace("\n", "") == text, f"{sp['id']}: 改行版の台詞が正本と違う: {text}"
            side = "left" if who == "藍子" else "right"
            role = "spoken first" if who == "藍子" else "spoken as the answer"
            if cm == "faces": role = f"rally {k} of {len(p['bubbles'])}"
            if cm == "faces":
                side_txt = f"{side}, row {k} of {len(p['bubbles'])} in the conversation column; face icon at the {side.upper()} end of its own row"
            else:
                side_txt = f"{side}, {role}"
            body += f"- {who} bubble ({side_txt}): {q(brk or text)}{hlpart(hl)}." + (" The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines." if brk else "") + "\n"
            who_lbl = (f"{who}（{'左' if who=='藍子' else '右'}・{k}番目）" if cm == "faces" else f"{who}（{'左・先に話す' if who=='藍子' else '右・答える'}）")
            rows.append((f"コマ{n}", who_lbl, text, f"「{hl}」" if hl else "—"))
        if p.get("checklist"):
            body += ("- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: "
                     + ", ".join(q(c) for c in p["checklist"]) + ".\n")
            rows.append((f"コマ{n} チェック欄", "3項目（青✓）", " / ".join(p["checklist"]), "—"))
        body += "\n"
    if sp.get("note"):
        body += f"NOTE LINE (small text on a thin strip between panel 4 and the conclusion banner, one line, fully legible): {q(sp['note'])}\n\n"
        rows.append(("注記", "小さな注記（コマ4の下）", sp["note"], "—"))
    body += ("CONCLUSION BANNER (strong contrasting solid color, large text, two lines):\n"
             f"- Line 1: {q(sp['band1'])} with a yellow highlighter marker.\n- Line 2: {q(sp['band2'])}\n\n")
    rows.append(("結論帯", "1行目", sp["band1"], "黄色マーカー"))
    rows.append(("結論帯", "2行目", sp["band2"], "—"))
    body += f"EMOTIONAL ARC: {ARC}.\n\n"
    text_only = "".join(re.findall(r"[一-鿿]", body))
    kan = [k for k in sorted(RISKY & set(text_only))]
    has_opp = any(p.get("opposite") for p in pan)
    fin = ("Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly "
           "and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right "
           "and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; "
           f"confirm the characters {', '.join(kan)} are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; "
           "confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; ")
    if has_opp:
        if any(p.get("opposite") == "lx" for p in pan):
            fin += "confirm the left comparison card has only a red cross and the right card only a blue check mark; "
        else:
            fin += "confirm the left comparison card has only a blue check mark and the right card only a red cross; "
    if flex:
        fin = fin.replace("confirm 藍子 is always on the left and トリ先生 always on the right ", "confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified ")
    alltext = "".join(b[1] for p in pan for b in p["bubbles"]) + "".join("".join(p["fig"]) for p in pan)
    for w, bad in GARBLED.items():
        if w in alltext: fin += f"confirm that the word {q(w)} is spelled exactly like this everywhere (never {q(bad)}); "
    if any(p.get("chars") == "small" for p in pan):
        fin += "confirm that the very small characters are drawn at the specified small sizes (they must not grow and squeeze the diagram) and that nothing but the given text appears above the heads of the pictograms; "
    for p_ in pan:
        if p_.get("chars") == "faces":
            nb_ = len(p_["bubbles"])
            fin += (f"confirm that the conversation column has exactly {nb_} face icons and exactly {nb_} speech bubbles, one pair per row in the speaking order from top to bottom, "
                    "that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; ")
            break
    if any(p.get("chars") == "side" for p in pan):
        fin += "confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; "
    if any(p.get("chars") in ("faces", "small") for p in pan):
        fin += "confirm that nothing but the given text appears above the heads of the pictograms; "
    if any(p.get("chars") == "none" for p in pan):
        fin += "confirm that every panel marked as having no character contains no character and no speech bubble; "
    if sp.get("final_extra"):
        fin += sp["final_extra"].strip() + " "
    fin += "confirm the background is fully opaque with no transparency, alpha channel, or checkerboard."
    body += fin
    return body, rows


# ---------- 見出し画像（苦手分析シリーズと同じ構成。背景は水彩の空に統一） ----------
H_BG = {
 "A": ("苦手分析シリーズ踏襲（水彩の空）",
       "soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series",
       "a soft white cloud-shaped glow",
       "Fill the whole canvas with the pastel sky and soft clouds."),
}

def header_texts(sp):
    h = sp["header"]
    return h["h1"], h["h2"], f"4コマ解説図解　{sp['id']}　{sp['src']}"

def header_kanji(*lines):
    seen = []
    for ln in lines:
        for k in re.findall(r"[一-鿿]", ln):
            if k not in seen: seen.append(k)
    return seen

def header_prompt(sp, opt="A"):
    h = sp["header"]; h1, h2, sub = header_texts(sp)
    name, style, glow, bg = H_BG[opt]
    kan = ", ".join(header_kanji(h1, h2, sub))
    return f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: {style}. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
{bg}

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over {glow} so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
{h1}
Line 2 is larger; the phrase {h['hkey']} is red-orange and the rest is dark navy:
{h2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{sub}
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: {h['scene_l']}
Right side: {h['scene_r']}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {kan}; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere."""

def header_section(sp):
    h1, h2, sub = header_texts(sp)
    out = "## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）\n\n"
    out += ("noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。"
            "構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。\n\n")
    out += "### 見出し画像の文言（正本）\n\n| 領域 | 正確な文言 | 強調 |\n|---|---|---|\n"
    out += f"| タイトル1行目 | {h1} | 薄い黄色のマーカー |\n| タイトル2行目 | {h2} | 「{sp['header']['hkey']}」を赤みのあるオレンジ |\n| サブタイトル | {sub} | — |\n\n"
    out += f"### 見出し画像プロンプト本体\n\n```text\n{header_prompt(sp)}\n```\n\n"
    out += "### 見出し画像の検品\n- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし\n- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり\n- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない\n- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない\n\n"
    return out

def file_base(i, src): return f"4コマ解説図解{i}～{src}～"

def filename_section(sp):
    b = file_base(sp["id"], sp["src"]) + sp.get("fsuffix", "")  # 別案（B案など）は接尾辞で採用版の名前の衝突を避ける
    return ("## 画像ファイル名（名づけルール）\n\n"
            "ChatGPTで生成した画像は、保存するときに次の名前へ変更する（拡張子は生成された形式のまま：png・webp など）。`MANGA_RULES.md` の「画像ファイル名」に従う。\n\n"
            "| 画像 | ファイル名 |\n|---|---|\n"
            f"| 4コマ解説図解（本文用・採用版） | {b}.png |\n"
            f"| 見出し画像（採用版） | {b}_見出し.png |\n"
            f"| 途中の版・不採用の版（例：v01） | {b}_v01.png ／ {b}_見出し_v01.png |\n\n")

SECOND_DIR = HERE / "specs2"

def load_second():
    """第二案の設計データ（specs2/<ID>.py の SPEC2）を読み込む。第一案（SPECS[ID]）と同じ肢のIDで対応づける。"""
    d = {}
    if SECOND_DIR.is_dir():
        for f in sorted(SECOND_DIR.glob("D*.py")):
            ns = {}; exec(compile(f.read_text(encoding="utf8"), str(f), "exec"), {"__name__": f.stem, "__file__": str(f)}, ns)
            d[ns["SPEC2"]["id"]] = ns["SPEC2"]
    return d

def second_section(sp2):
    """第二案（B案型）の節：設計メモ2・構成表2・プロンプト本体2。ファイルの末尾に置く（check_prompt.py は第一案と第二案を別々に検査する）。"""
    body, rows = build(sp2)
    out = "\n## 第二案（B案）：構成表2とプロンプト本体2\n\n"
    out += ("上の構成表・プロンプト本体（第一案）は、定型の「ひっかけと勘違い」型で組んだもの。この第二案は、`D0314-B_prompt.md` と同じ型"
            "（しくみの図解→押さえどころ→本番での読み方→暗記3点。「ひっかけと勘違い」の対比カードは使わない）で組んだ別構成。"
            "どちらか1つを選んで、ChatGPTに貼る。見出し画像・記事タイトル・冒頭文は第一案と共通。第二案の本文画像は、保存名の末尾に `_B案` を付ける"
            "（例：`4コマ解説図解<ID>～<出典>～_B案.png`）。\n\n")
    out += "### 設計メモ2（工程A）\n" + "\n".join(f"- {m}" for m in sp2["design"]) + "\n\n"
    out += "### 構成表2（文言の正本）\n\n| 領域 | 話者・用途 | 正確な文言 | 強調 |\n|---|---|---|---|\n"
    out += "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows) + "\n\n"
    if sp2.get("extra_refs"):
        out += "### 記事に無い条文（ユーザー指示で追加）\n\n" + "".join(f"- {r}\n" for r in sp2["extra_refs"]) + "\n"
    out += "### プロンプト本体2\n\n```text\n" + body + "\n```\n\n"
    out += "### 第二案の品質ゲート（工程C）\n" + "".join(f"- [ ] 工程C：{c}\n" for c in sp2["review"])
    if sp2.get("rev"):
        out += "\n### 第二案の改訂履歴\n\n" + "".join(f"- {r}\n" for r in sp2["rev"])
    return out

THIRD_DIR = HERE / "specs3"

def load_third():
    """第三案の設計データ（specs3/<ID>.py の SPEC3）を読み込む。"""
    d = {}
    if THIRD_DIR.is_dir():
        for f in sorted(THIRD_DIR.glob("D*.py")):
            ns = {}; exec(compile(f.read_text(encoding="utf8"), str(f), "exec"), {"__name__": f.stem, "__file__": str(f)}, ns)
            d[ns["SPEC3"]["id"]] = ns["SPEC3"]
    return d

def third_section(sp3):
    """第三案（C案）の節：設計メモ3・構成表3・プロンプト本体3。第二案の後ろに置く。"""
    body, rows = build(sp3)
    out = "\n## 第三案（C案）：構成表3とプロンプト本体3\n\n"
    out += (sp3.get("intro3") or "第三案（C案）。第一案をもとに、「なぜそうなるのか」の理由の説明コマを加えた別構成。") + \
           "どれか1つを選んで、ChatGPTに貼る。見出し画像・記事タイトル・冒頭文は第一案と共通。第三案の本文画像は、保存名の末尾に `_C案` を付ける（例：`4コマ解説図解<ID>～<出典>～_C案.png`）。\n\n"
    out += "### 設計メモ3（工程A）\n" + "\n".join(f"- {m}" for m in sp3["design"]) + "\n\n"
    out += "### 構成表3（文言の正本）\n\n| 領域 | 話者・用途 | 正確な文言 | 強調 |\n|---|---|---|---|\n"
    out += "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows) + "\n\n"
    if sp3.get("extra_refs"):
        out += "### 記事に無い条文（ユーザー指示で追加）\n\n" + "".join(f"- {r}\n" for r in sp3["extra_refs"]) + "\n"
    out += "### プロンプト本体3\n\n```text\n" + body + "\n```\n\n"
    out += "### 第三案の品質ゲート（工程C）\n" + "".join(f"- [ ] 工程C：{c}\n" for c in sp3["review"])
    if sp3.get("rev"):
        out += "\n### 第三案の改訂履歴\n\n" + "".join(f"- {r}\n" for r in sp3["rev"])
    return out

SECOND = load_second()
THIRD = load_third()

def render(sp):
    body, rows = build(sp)
    out = f"# {sp['id']} 4コマ解説図解 プロンプト（ChatGPT貼付用・{sp.get('ver','v01')}）\n\n"
    out += (f"- 肢：{sp['id']}（{sp['topic']}、出典 {sp['src']}）。正解＝{sp['truth']}。誤解{sp['miscon'] if isinstance(sp['miscon'], str) else str(sp['miscon']) + '回'}。\n"
            f"- 記事：`{sp['article']}` {sp['art_head']}\n- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）\n"
            "- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、"
            "どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。\n\n")
    out += "## 設計メモ（工程A）\n" + "\n".join(f"- {m}" for m in sp["design"]) + "\n\n"
    out += f"## 記事タイトル\n\n{article_title(sp['id'], sp['src'])}\n\n"
    out += "## note記事の冒頭文\n\n" + lead_text(sp["lead1"], sp["src"]) + "\n\n"
    out += "## 構成表（文言の正本）\n\n| 領域 | 話者・用途 | 正確な文言 | 強調 |\n|---|---|---|---|\n"
    out += "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows) + "\n\n"
    if sp.get("extra_refs"):
        out += "## 記事に無い条文（ユーザー指示で追加）\n\n" + "".join(f"- {r}\n" for r in sp["extra_refs"]) + "\n"
    out += "## プロンプト本体\n\n```text\n" + body + "\n```\n\n"
    out += header_section(sp)
    out += filename_section(sp)
    out += ("## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）\n"
            + ("- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み\n" if sp.get("ippatsu") else "")
            + f"- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/{sp.get('fid', sp['id'])}_prompt.md` が NG 0件\n"
            + "".join(f"- [ ] 工程C：{c}\n" for c in sp["review"]) + "\n")
    out += ("## 生成後の照合チェック（文言の正本は上の構成表）\n- [ ] 4コマ縦一列／タイトル帯・結論帯あり\n"
            "- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ\n"
            "- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致\n- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている\n"
            "- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性\n- [ ] 簡体字・英字なし、背景が不透明\n"
            "- [ ] 記事の文言から外れていない（独自の理由づけなし）\n"
            "- [ ] 顔アイコン・小さなキャラが指定の大きさ。キャラなしのコマにキャラ・吹き出しがない\n"
            "- [ ] 図の部品（人物・バー・領域・タグ）の色が指定どおり（意味のない青・赤・緑・ピンクがない）。人物の頭の上に余計な印がない\n"
            "- [ ] 台詞の綴りが一字一句正本どおり（特に「原則」「まとめて」など崩れやすい語）\n")
    if sp.get("qa"):
        out += "\n## " + sp["qa"][0] + "\n" + "".join(f"- {r}\n" for r in sp["qa"][1:])
    if sp.get("rev"):
        out += "\n## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）\n\n" + "".join(f"- {r}\n" for r in sp["rev"])
    if sp.get("fid", sp["id"]) == sp["id"] and sp["id"] in SECOND:   # 第一案のファイルにだけ、第二案を追記する
        out += second_section(SECOND[sp["id"]])
    if sp.get("fid", sp["id"]) == sp["id"] and sp["id"] in THIRD:
        out += third_section(THIRD[sp["id"]])
    return out

def patch_d0520():
    """手作りのD0520_prompt.mdに、見出し画像のセクションと藍子の人体構造の指示を差し込む（既にあれば置き換える）。"""
    from manga_specs import D0520_HEADER_SP
    p = HERE / "D0520_prompt.md"; s = p.read_text(encoding="utf8")
    anat = re.search(r"ANATOMY \(critical, 藍子\):.*", HEAD).group(0)
    if "ANATOMY (critical" not in s:
        s = s.replace("\n\nFIXED POSITIONS", "\n\n" + anat + "\n\nFIXED POSITIONS", 1)
    else:
        s = re.sub(r"ANATOMY \(critical, 藍子\):[^\n]*", lambda m: anat, s, count=1)
    if "CONTINUITY:" not in s:
        s = s.replace("\n\nLAYOUT (top to bottom", "\n\n" + CONT + "\n\nLAYOUT (top to bottom", 1)
    from manga_specs import D0520_BREAKS
    for plain, brk in D0520_BREAKS.items():
        assert brk.replace("\n", "") == plain, plain
        s = s.replace(f"「{plain}」", f"「{brk}」")
    def _hands(m):
        return m.group(0) if "hands:" in m.group(0) else f"PANEL {m.group(1)} ({m.group(2)}; {HANDS[int(m.group(1)) - 1]}):"
    s = re.sub(r"^PANEL (\d) \(([^\n]*?)\):", _hands, s, flags=re.M)
    if "exactly two arms and two hands" not in s:
        s = s.replace("confirm the background is fully opaque", "confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque", 1)
    s = re.sub(r"## 見出し画像プロンプト.*?(?=## 作成時の品質ゲート)", "", s, flags=re.S)
    s = re.sub(r"## 画像ファイル名.*?(?=## 作成時の品質ゲート)", "", s, flags=re.S)
    s = s.replace("## 作成時の品質ゲート", header_section(D0520_HEADER_SP) + filename_section(D0520_HEADER_SP) + "## 作成時の品質ゲート", 1)
    p.write_text(s, encoding="utf8")

if __name__ == "__main__":
    from manga_specs import SPECS
    if "--check" in sys.argv:
        # 同期チェック：設計データから作り直した内容と、リポジトリの <ID>_prompt.md が一致するか。手で直した・直し忘れた版を検出する。
        bad = [i for i in SPECS if (HERE / f"{i}_prompt.md").read_text(encoding="utf8") != render(SPECS[i])]
        for i in bad: print(f"OUT OF SYNC {i}: {i}_prompt.md が manga_specs.py から生成した内容と違う（設計データを直して再生成する）")
        print(f"同期チェック: 不一致 {len(bad)}件"); sys.exit(1 if bad else 0)
    ids = [a for a in sys.argv[1:] if not a.startswith("--")] or list(SPECS) + ["D0520"]
    for i in ids:
        if i == "D0520":
            patch_d0520(); print("patched D0520"); continue
        (HERE / f"{i}_prompt.md").write_text(render(SPECS[i]), encoding="utf8")
        print("generated", i)
