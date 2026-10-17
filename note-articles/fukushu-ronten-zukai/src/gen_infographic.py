#!/usr/bin/env python3
"""論点別 復習用 図解インフォグラフィック40枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/fukushu-ronten-zukai/src/gen_infographic.py
出力: ../T01_xxx/prompt_infographic_T01.md …（論点ごとに1ファイル）。生成物は手で直さず、specs.py を直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[1] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
sys.path.insert(0, str(HERE))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final
from specs import TOPICS, SPECS

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
NUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
EXTRA_KANJI = list("竣嘱附閉鎖謄")

def header(t, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t[0]), q(t[1]), "Subtitle (smaller, centered, 1 line):", q(sub)]

def kj(txt):
    ks = kanji_in(txt)
    for k in EXTRA_KANJI:
        if k in txt and k not in ks:
            ks.append(k)
    return ks[:10]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kj(txt), extra)

def size_of(s):
    if s["kind"] == "table":
        h = 900 + 230 * len(s["rows"]) + (260 if s.get("note") else 0) + (150 if s.get("band") else 0)
    elif s["kind"] == "cards2":
        h = 1900 + (300 if s.get("note") else 0)
    else:
        h = 1500 + 330 * len(s["steps"]) - 330 * 2 + (330 if s.get("side") else 0)
    h = int(round(h / 100.0) * 100)
    return f"1080x{max(1600, min(2800, h))}"

def band_line(s, where):
    return [f"Under the {where}, one wide dark navy band with large white text {q(s['band'])}."] if s.get("band") else []

def note_lines(s):
    if not s.get("note"):
        return []
    head, items = s["note"]
    return ["--- NOTE CARD (below, a wide card with a dashed dark navy outline and a small dark navy tag " + q("補足") + ") ---",
            "Heading (bold): " + q(head), "Body lines, each with a small dark navy dot at its left end (NO number on the dots):"] + [q(x) for x in items]

def build_table(s, size):
    n, m = len(s["headers"]), len(s["rows"])
    body = [lead(size, f"This is a reference table poster with {NUM[n]} columns."), TEXTREQ, BGREQ, NOCOLOR] + header(s["title"], s["sub"])
    body += ["--- TABLE ---",
             f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {m} data rows, no merged cells.",
             "Every cell wraps its text onto as many lines as needed inside the cell; no cell text is cut off, shrunk below readable size, or overlaps another cell.",
             "Header row (dark navy cells with white text): " + ", ".join(q(h) for h in s["headers"]) + ".",
             "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"]
    for i, r in enumerate(s["rows"], 1):
        body.append(f"Row {i}: " + " | ".join(q(c) for c in r))
    if s.get("hl"):
        parts = [f"the string {q(sub)} inside the column-{c+1} cell of row {r+1}" for r, c, sub in s["hl"]]
        body.append("Highlighting: " + "; ".join(parts) + " has a pale yellow highlighter marker. Copy each cell exactly as given.")
    body += note_lines(s) + band_line(s, "table" if not s.get("note") else "note card")
    return finish(body, f"Confirm the table has exactly {n} columns and exactly {m} data rows, that every cell reads exactly as given and the cells are not shifted between rows, and that no check mark, cross mark, blue, or red appears anywhere.")

def build_cards2(s, size):
    body = [lead(size, "This is a comparison poster with two side-by-side cards."), TEXTREQ, BGREQ, NOCOLOR] + header(s["title"], s["sub"])
    body += ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---"]
    for side, d in (("Left", s["left"]), ("Right", s["right"])):
        body.append(f"{side} card: small tag {q(d['tag'])}, heading {q(d['head'])} (the string {q(d['head'])} has a pale yellow highlighter marker), and exactly {NUM[len(d['items'])]} short item lines, each with a small dark navy dot at its left end (NO number on the dots): " + ", ".join(q(x) for x in d["items"]) + ".")
    body.append("The two cards have clearly different texts; the texts are NOT identical.")
    body += note_lines(s) + band_line(s, "cards" if not s.get("note") else "note card")
    return finish(body, f"Confirm there are exactly two cards, that the left card has exactly {NUM[len(s['left']['items'])]} item lines and the right card has exactly {NUM[len(s['right']['items'])]} item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

def build_steps(s, size):
    k = len(s["steps"])
    body = [lead(size, f"This is a vertical step poster with {NUM[k]} step cards" + (" and one side note card." if s.get("side") else ".")), TEXTREQ, BGREQ, NOCOLOR] + header(s["title"], s["sub"])
    body += ["--- STEPS ---",
             f"Layout: {NUM[k]} step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (" + ", ".join(str(i) for i in range(1, k + 1)) + " in order), one bold heading line, and one body line."]
    for i, (h, b) in enumerate(s["steps"], 1):
        mark = " (the card has a pale yellow highlighter marker on its heading)" if s.get("hl_step") == i else ""
        body.append(f"STEP {i}{mark}: heading {q(h)}, body {q(b)}.")
    if s.get("side"):
        head, items = s["side"]
        body += ["--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---", "Heading (bold): " + q(head), "Body lines, each with a small dark navy dot at its left end (NO number on the dots):"] + [q(x) for x in items]
    body += band_line(s, "steps" if not s.get("side") else "side note card")
    return finish(body, f"Confirm there are exactly {NUM[k]} step cards numbered 1 to {k} in order" + (", followed by exactly one side note card" if s.get("side") else "") + ", that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

BUILD = {"table": build_table, "cards2": build_cards2, "steps": build_steps}
KIND_JA = {"table": "早見表型", "cards2": "対比カード型（2列）", "steps": "ステップ型"}

def main():
    tinfo = {t[0]: t for t in TOPICS}
    byt = {}
    for s in SPECS:
        byt.setdefault(s["topic"], []).append(s)
    for tid, name, short in TOPICS:
        folder = OUT / f"{tid}_{short}"
        folder.mkdir(exist_ok=True)
        lines = [f"# 論点別 復習用 図解インフォグラフィック プロンプト（{tid} {name}・{len(byt[tid])}枚）\n",
                 "この論点の理解に役立つ図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md` と `note-articles/joubun-nigate/common/infographic_parts.py`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
                 "図解はいずれも分類・早見表・手順で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果を入れません。\n",
                 "| 番号 | 図解 | 型 | サイズ | 保存名 |", "|---|---|---|---|---|"]
        blocks = []
        for s in byt[tid]:
            size = size_of(s)
            fname = f"{short}_図解{s['n']}_{s['file']}.png"
            lines.append(f"| 図解{tid}-{s['n']} | {s['title'][0]}（{s['title'][1]}） | {KIND_JA[s['kind']]} | {size.replace('x', '×')} | {fname} |")
            blocks += [f"\n## 図解{tid}-{s['n']}：{s['title'][0]}（{s['title'][1]}）\n", f"- 型：{KIND_JA[s['kind']]}　／　サイズ：{size.replace('x', '×')}　／　保存名：`{fname}`\n",
                       "```text", BUILD[s["kind"]](s, size), "```"]
        lines.append("\n画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。")
        (folder / f"prompt_infographic_{tid}.md").write_text("\n".join(lines + blocks) + "\n", encoding="utf8")
        print(tid, folder.name, len(byt[tid]))

if __name__ == "__main__":
    main()
