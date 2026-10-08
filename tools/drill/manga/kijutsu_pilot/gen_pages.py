#!/usr/bin/env python3
"""ページ構成表（page_spec.json）から、ChatGPTに貼るページ別プロンプトと、プロジェクト用の共通指示を生成する（方式A′）。
- 図・計算カード・答えバナーは ChatGPT に描かせない。空の薄い灰色の仮枠だけ描かせ、あとで compose_pages.py が貼り込む。
  → 図のPNGをChatGPTに添付する必要がない（GitHubのURLを読ませる必要もない）。
- 共通ルール（キャラクター・人体構造・文字・色）は『ChatGPTのプロジェクトの指示』に1回だけ貼る（00_project_instructions.md）。
  各ページのプロンプトは、そのページ固有の内容だけ（--standalone で共通ルールも含める）。
使い方: python3 tools/drill/manga/kijutsu_pilot/gen_pages.py <page_spec.json> [出力フォルダ] [--standalone]
"""
import json, pathlib, re, sys, ast

HERE = pathlib.Path(__file__).resolve().parent
MANGA = HERE.parent
GARBLED = ast.literal_eval(re.search(r'GARBLED = (\{.*?\})', (MANGA / "check_prompt.py").read_text(encoding="utf8")).group(1))
RISKY = set(re.search(r'RISKY = set\("([^"]+)"\)', (MANGA / "check_prompt.py").read_text(encoding="utf8")).group(1))
PH = "#E6E6E6"
SIZES_EN = {"FULL": "whole or upper body, about 440-520 px tall", "MID": "upper body, about 300 px tall", "SMALL": "small full-body figure, about 110 px tall", "FACES": "tiny round face icon only, about 80 px across, no body, no hands"}

EMO = {  # 表情ID: (名前, 描き方)
    "A1": ("自信満々", "confident: chest out, corners of the mouth up, bright eyes"),
    "A2": ("固まる・青ざめ", "frozen and pale: wide dot-like eyes, a sweat drop, one hand near the mouth"),
    "A3": ("ひらめき", "realizing: eyes wide open, an index finger raised or a small light-bulb sparkle"),
    "A4": ("確かめる・考える", "thinking carefully: a hand on the chin or holding a pen, eyes on the material"),
    "A5": ("安堵・達成", "relieved and pleased: a big smile, a small cheering fist"),
    "T1": ("呆れ・叱る（愛あり）", "exasperated but caring: narrowed eyes, pushing the round glasses up with a wing"),
    "T2": ("指し示す", "explaining: a wing points at the card or figure, the other wing at the side"),
    "T3": ("感心", "impressed: round eyes, a satisfied nod"),
    "T4": ("どや・念押し", "emphatic: chest out, wings spread, a confident smirk"),
}

COMMON = """CANVAS: ONE vertical Japanese study-manga page, 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same proportions. The whole image has a fully opaque, light cream background (no transparency, no alpha channel, no checkerboard).

TEXT: All text is Japanese only: standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, and the symbols that appear in the given strings. Never use simplified or traditional Chinese characters, Korean, Latin-alphabet words, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text, and do not add any text that is not listed. Numbers, decimal points, degree/minute/second marks, and full-width letters must be reproduced exactly.

CHARACTERS: The character-specification images in this project are the single authoritative reference for two recurring characters; reproduce them faithfully on every page: same face, body shape, clothing, colors, proportions, drawing style, and the same hairstyle for 藍子. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character; sharp-tongued but full of love for beginners; wings used as hands; round red glasses, a blue shirt, and a red neckerchief. (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; long wavy brown hair; earnest and headstrong. Do not redesign either character and do not add any other character. Persons in diagrams are not characters.

ANATOMY (critical, 藍子): exactly one head, one torso, two arms and two hands in total; each hand has exactly five fingers. Never draw extra arms, extra hands, floating or duplicated hands, or fused hands. Follow the hand assignment given for each appearance of 藍子 (for example one hand holds the clipboard while the other touches her chin). When she points, only ONE arm points. Change her pose from page to page.

APPEARANCE MODES (sizes are for the 1080x1920 page): FULL = the character's whole body or upper body, about 440-520 px tall; MID = upper body, about 300 px tall; SMALL = a small full-body figure, about 110 px tall; FACES = only a small round face icon about 80 px across (head only, no body, no hands). A character who is not listed for a zone is not drawn there. A character listed as silent shows only the expression and has no speech bubble.

SPEECH BUBBLES: white fill, thin dark navy outline, dark navy text, large high-contrast mobile-readable Japanese (character height at least 40 px). Every bubble tail points directly at its own speaker (藍子 is always on the LEFT side, トリ先生 always on the RIGHT side; a bubble sits on the same side as its speaker). Bubbles within a zone are stacked from top to bottom in the order given and never overlap each other, a character's face, or a placeholder rectangle. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines. A part marked as emphasized is highlighted with a yellow highlighter marker.

PLACEHOLDER RECTANGLES (critical): wherever a PLACEHOLDER is specified, draw ONLY a plain, completely empty, flat light-gray (#E6E6E6) rectangle with square corners at the given position and size. No outline decoration, no shadow, no text, no figure, no icon, and nothing overlapping it (no character, no bubble). Another program will paste the real content into it afterwards.

STYLE AND COLOR: clean, warm, trustworthy flat digital illustration; simple outlines; soft pastel colors. Use dark navy for outlines, tabs, and neutral parts. Use red ONLY for a part explicitly marked as red (an error or a correction); use blue only for a correct check mark when one is specified. Do not use pink, green, or orange anywhere, and do not color anything in meaningless colors. Do not draw any calculator keys or key sequences.

PAGE STRUCTURE: the page is divided top to bottom into the ZONES listed below; a zone starts at y and has the height h (px). Keep each zone's content inside its band with clear margins."""

def wrap(text, n=14):
    """吹き出しの文字列に、1行n字前後の意図的な改行を入れる（結合すると元の文字列）"""
    if len(text) <= n + 2: return text
    out, cur = [], ""
    for ch in text:
        cur += ch
        if len(cur) >= n - 4 and ch in "、。？！」』…" or len(cur) >= n + 1:
            out.append(cur); cur = ""
    if cur:
        if out and len(cur) <= 3: out[-1] += cur
        else: out.append(cur)
    return "\n".join(out)

def frame_rect(z):
    if z["type"] == "figure": f = z["frame"]; return f["x"], f["y"], f["w"], f["h"]
    f = z.get("frame", {"x": 40, "w": 1000}); return f["x"], z["y"] + 20, f["w"], z["h"] - 40

def q(t): return f"「{t}」"

def page_prompt(sp, p, standalone):
    sizes = SIZES_EN
    L = [f"PAGE: {p['page_id']}　（{p['template']}／{p['beat']}）", f"THIS PAGE'S ONE POINT: {p['one_point']}", "", "ZONES (top to bottom):"]
    texts = []
    for z in p["zones"]:
        t = z["type"]; hd = f"- ZONE {z['zone_id']}: y={z['y']}, h={z['h']} px, type={t}."
        if t in ("tab", "chapter_header"):
            style = ("a large dark-navy chapter header band with big bold white text, with a small decorative accent" if t == "chapter_header"
                     else "a thin dark-navy tab strip with small white text, flush left")
            nest = " (the inner 「」 marks are part of the text)" if "「" in z["text"] else ""
            L.append(f"{hd} Draw {style}; text {q(z['text'])}{nest}."); texts.append(z["text"])
        elif z.get("frame") or t in ("figure", "calc_card", "answer_banner", "note_card", "wrong_card", "obs_card", "point_card", "next_chapter_tag"):
            x, y, w, h = frame_rect(z)
            L.append(f"{hd} PLACEHOLDER: one empty light-gray ({PH}) rectangle at x={x}, y={y}, width={w}, height={h} px, and nothing else in this zone.")
        elif t == "reaction":
            L.append(f"{hd} No text and no speech bubble in this zone.")
        elif t == "dialogue":
            L.append(f"{hd}")
        if z.get("chars"):
            for c in z["chars"]:
                nm, how = EMO[c["emotion"]]
                silent = "silent" in c.get("note", "")
                hands = f" Hands: {c['hands']}." if c.get("hands") else ""
                side = "LEFT" if c["who"] == "藍子" else "RIGHT"
                extra = f" Note: {c['note']}." if c.get("note") and not silent else ""
                L.append(f"  - {q(c['who'])} appears at the {side} as {c['mode']} ({sizes[c['mode']]}); expression {c['emotion']} ({nm}): {how}." + hands + (" SILENT: expression only, no speech bubble." if silent else "") + extra)
        for k, b in enumerate(z.get("bubbles", []), 1):
            side = "left" if b["speaker"] == "藍子" else "right"
            hl = f" The part {q(b['highlight'])} is highlighted in yellow." if b.get("highlight") else ""
            L.append(f"  - Bubble {k} of {len(z['bubbles'])} ({b['speaker']}, {side}): {q(wrap(b['text']))}.{hl}"); texts.append(b["text"])
    alltext = "".join(texts)
    kan = sorted(RISKY & set(re.findall(r"[一-鿿]", alltext)))
    fin = ["FINAL CHECK before rendering:",
           "confirm there is exactly ONE page in one vertical column and every zone is in the given order and height;",
           "confirm every text string matches the given string exactly, with no extra text anywhere, and that no word or digit is dropped or altered;"]
    for w, bad in GARBLED.items():
        if w in alltext: fin.append(f"confirm that the word {q(w)} is spelled exactly like this (never {q(bad)});")
    if kan: fin.append(f"confirm that these characters are proper Japanese kanji forms: {' '.join(kan)};")
    fin += ["confirm that every PLACEHOLDER is a completely empty flat light-gray rectangle of the given position and size, with nothing drawn inside or over it;",
            "confirm that no character or speech bubble overlaps a placeholder, and that every bubble tail points at its own speaker (藍子 left, トリ先生 right);",
            "confirm that characters are drawn at the specified appearance mode sizes (FACES are tiny face icons, not larger) and silent characters have no bubble;",
            "confirm that 藍子 has exactly two arms and two hands with five fingers each and the same hairstyle as in the reference images;",
            "confirm that no pink, green, or orange is used, that red appears only where marked, and that no calculator keys are drawn;",
            "confirm the background is fully opaque with no transparency or checkerboard."]
    if p.get("continuity"): L += ["", f"CONTINUITY: {p['continuity']}"]
    L += ["", " ".join(fin)]
    body = "\n".join(L)
    if standalone: body = COMMON + "\n\n" + body
    return body

def project_instructions():
    return ("# ChatGPTプロジェクトの指示（1回だけ貼る）\n\n"
            "ChatGPTの「プロジェクト」を1つ作り（例：「記述式解説漫画 R7-Q21」）、次の手順で設定します。\n\n"
            "1. プロジェクトの**ファイル**に、キャラクターシート6枚（`キャラクターシート_藍子_01〜03`、`キャラクターシート_トリ先生_01〜03`。`CHATGPT_MANGA_WORKFLOW.md` §3）と `女性キャラクター_統一仕様書.md`（GitHubの `tools/drill/manga/女性キャラクター_統一仕様書.md`。最新版）を**1回だけ**アップロードする。\n"
            "2. プロジェクトの**指示**に、下の ```text のブロックを貼る。\n"
            "3. プロジェクトの中で新しいチャットを作り、`prompts/R7-Q21-02-01_prompt.md` の ```text の中身を貼って送る。以降、ページごとに同じチャットか新しいチャットで、各ページのプロンプトだけを貼る。\n"
            "4. 図（zu/のPNG）は**添付しない**。図・計算カード・答えバナーは仮枠だけ描かせ、`compose_pages.py` が貼る。\n\n"
            "```text\n" + COMMON + "\n\n"
            "WORKFLOW IN THIS PROJECT: each time the user pastes a PAGE specification, generate exactly ONE image for that page, following the common rules above and the page specification. "
            "Use the character-specification images in the project files as the only character reference. If the result does not show an actual image, say so and generate it again; never claim a page is finished without showing the image.\n```\n")

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    standalone = "--standalone" in sys.argv
    spec = json.loads(pathlib.Path(args[0]).read_text(encoding="utf8"))
    out = pathlib.Path(args[1]) if len(args) > 1 else HERE / "prompts"; out.mkdir(parents=True, exist_ok=True)
    (out / "00_project_instructions.md").write_text(project_instructions(), encoding="utf8")
    for p in spec["pages"]:
        body = page_prompt(spec, p, standalone)
        (out / f"{p['page_id']}_prompt.md").write_text(
            f"# {p['page_id']}　ChatGPT用プロンプト（{'共通ルール込み' if standalone else 'プロジェクトの指示を前提。このページ固有の内容だけ'}）\n\n"
            "```text\n" + body + "\n```\n", encoding="utf8")
    print(f"generated {len(spec['pages'])} page prompts + 00_project_instructions.md → {out}")
main()
