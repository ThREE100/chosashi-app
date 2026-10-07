#!/usr/bin/env python3
"""4コマ解説図解プロンプト（<ID>_prompt.md）の生成器。D0520_prompt.mdと同じ構成を、肢ごとの設計データ（SPECS）から作る。
使い方: python3 tools/drill/manga/gen_prompts.py [ID ...]   （省略時は全部）
生成後は必ず check_prompt.py を通すこと。設計（工程A）はSPECSに書く：登場人物の初出・矢印の意味・会話順・配色。
D0520_prompt.md は手作り（検品済みの見本）で、この生成器の対象外。"""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
RISKY = set(re.search(r'RISKY = set\("([^"]+)"\)', (HERE / "check_prompt.py").read_text(encoding="utf8")).group(1))

HEAD = """Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers{LETTERS_OK}. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. {PARTIES}

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall)."""

MOODS = ["藍子 confident, トリ先生 exasperated but caring", "藍子 puzzled, トリ先生 explaining with a wing-pointer",
         "both characters point together at the same figure; 藍子 realizing", "藍子 relieved, トリ先生 smiling proudly"]
ARC = "confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4)"
OPPOSITE = ("IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; "
            "the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.")

def article_title(i, src): return f"【土地家屋調査士受験生向け】4コマ解説図解{i}～{src}～"

def q(t): return f"「{t}」"
def hlpart(h): return f" with the part {q(h)} highlighted in yellow" if h else ""

def build(sp):
    pan = sp["panels"]
    letters = sp.get("letters", "")
    letters_ok = (f", and the full-width letters {' '.join(letters)} only where specified below" if letters else "")
    if letters:
        parties = (f"The legal parties {', '.join(letters)} are NOT characters: draw them only as small, faceless, flat pictogram figures, "
                   "each with a small round label tag containing the full-width letter given in the text plan.")
    else:
        parties = "Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below."
    body = HEAD.replace("{LETTERS_OK}", letters_ok).replace("{PARTIES}", parties) + "\n\n"
    body += f"TITLE BANNER: text {q(sp['title'])} in large bold letters; the part {q(sp['title_hl'])} has a yellow highlighter marker.\n\n"
    rows = [("タイトル帯", "—", sp["title"], sp["title_hl"] and f"「{sp['title_hl']}」を黄色マーカー")]
    for i, p in enumerate(pan):
        n = i + 1
        body += f"PANEL {n} ({p.get('mood', MOODS[i])}):\n- Label tab: {q(p['label'])}\n"
        rows.append((f"コマ{n} 見出し", "ラベル", p["label"], "—"))
        if p.get("opposite"): body += f"- {OPPOSITE}\n"
        for ln in p["fig"]: body += f"- {ln}\n"
        figstr = []
        for ln in p["fig"]:
            for t in re.findall(r"「([^」]+)」", ln):
                if t not in figstr: figstr.append(t)
        rows.append((f"コマ{n} 図", "図・カード", " / ".join(figstr), "—"))
        for b in p["bubbles"]:
            who, text, hl = b
            side = "left" if who == "藍子" else "right"
            role = "spoken first" if who == "藍子" else "spoken as the answer"
            body += f"- {who} bubble ({side}, {role}): {q(text)}{hlpart(hl)}.\n"
            rows.append((f"コマ{n}", f"{who}（{'左・先に話す' if who=='藍子' else '右・答える'}）", text, f"「{hl}」" if hl else "—"))
        if p.get("checklist"):
            body += ("- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: "
                     + ", ".join(q(c) for c in p["checklist"]) + ".\n")
            rows.append((f"コマ{n} チェック欄", "3項目（青✓）", " / ".join(p["checklist"]), "—"))
        body += "\n"
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
           "confirm every stamp, arrow, and label stays inside its own card or panel frame; ")
    if has_opp:
        fin += "confirm the left comparison card has only a blue check mark and the right card only a red cross; "
    fin += "confirm the background is fully opaque with no transparency, alpha channel, or checkerboard."
    body += fin
    return body, rows

def render(sp):
    body, rows = build(sp)
    out = f"# {sp['id']} 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）\n\n"
    out += (f"- 肢：{sp['id']}（{sp['topic']}、出典 {sp['src']}）。正解＝{sp['truth']}。誤解{sp['miscon']}回。\n"
            f"- 記事：`{sp['article']}` {sp['art_head']}\n- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）\n"
            "- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、"
            "どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。\n\n")
    out += "## 設計メモ（工程A）\n" + "\n".join(f"- {m}" for m in sp["design"]) + "\n\n"
    out += f"## 記事タイトル\n\n{article_title(sp['id'], sp['src'])}\n\n"
    if sp.get("lead"):
        out += "## note記事の冒頭文（試作）\n\n" + sp["lead"] + "\n\n"
    out += "## 構成表（文言の正本）\n\n| 領域 | 話者・用途 | 正確な文言 | 強調 |\n|---|---|---|---|\n"
    out += "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows) + "\n\n"
    out += "## プロンプト本体\n\n```text\n" + body + "\n```\n\n"
    out += ("## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）\n"
            f"- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/{sp['id']}_prompt.md` が NG 0件\n"
            + "".join(f"- [ ] 工程C：{c}\n" for c in sp["review"]) + "\n")
    out += ("## 生成後の照合チェック（文言の正本は上の構成表）\n- [ ] 4コマ縦一列／タイトル帯・結論帯あり\n"
            "- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ\n"
            "- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致\n- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている\n"
            "- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性\n- [ ] 簡体字・英字なし、背景が不透明\n"
            "- [ ] 記事の文言から外れていない（独自の理由づけなし）\n")
    return out

if __name__ == "__main__":
    from manga_specs import SPECS
    ids = sys.argv[1:] or list(SPECS)
    for i in ids:
        (HERE / f"{i}_prompt.md").write_text(render(SPECS[i]), encoding="utf8")
        print("generated", i)
