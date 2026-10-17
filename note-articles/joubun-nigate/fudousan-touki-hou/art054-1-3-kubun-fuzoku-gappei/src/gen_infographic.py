# 不動産登記法 第54条1項3号 区分合併と附属合併の使い分け 図解インフォグラフィック5枚のプロンプトを組み立てる（共通部品は ../../../common/infographic_parts.py）
import re, pathlib
import sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

CARD_REQ = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. "
            "Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.")

# ---------------------------------------------------------------- 図解1：建物の合併は2種類（カードポスター）
def img1():
    cards = [
        ("附属合併", "Two separate isometric house icons labeled " + q("甲建物") + " and " + q("乙建物") + ", with a solid navy arrow from the first house into a small annex box attached to the second house, and a small pale tag " + q("主たる建物と附属建物") + " between them.", "主従の関係が要る"),
        ("区分合併", "Two attached rooms of one apartment building labeled " + q("甲建物") + " and " + q("乙建物") + ", side by side and touching, with a solid navy arrow merging them into one single room.", "接続していることが要る"),
        ("共通の制限", "A registry ledger card with a small stop-sign icon beside it and the small tag " + q("法56条") + ".", "どちらの合併にも同じ"),
        ("両方の要件がそろうとき", "Two touching apartment rooms with a small double-headed branch icon pointing to a left small label " + q("附属合併") + " and to a right small label " + q("区分合併") + ".", "どちらも申請できる"),
    ]
    body = [lead("1080x2000", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."), CARD_REQ,
            TEXTREQ, BGREQ, COLOR] + header("建物の合併は2種類", "附属合併と区分合併", "不動産登記法 第54条1項3号")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ---------------------------------------------------------------- 図解2：附属合併と区分合併の対比表
def img2():
    rows = [("どんな合併？", "甲建物を、乙建物の附属建物とする", "接続する区分建物を、一個の建物にする"),
            ("甲建物は？", "区分建物でも、そうでなくてもよい", "区分建物であること"),
            ("接続は？", "要らない", "必要"),
            ("主従の関係は？", "必要", "要らない"),
            ("根拠", "規則132条・準則86条1号", "規則133条・準則86条2号")]
    body = [lead("1080x1900", "This is a comparison table poster with three columns (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("附属合併と区分合併", "要件はどこが違う？", "不動産登記法 第54条1項3号") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("附属合併") + "; the third header " + q("区分合併") + ". The two headers are NOT identical."]
    for i, (a, b, c) in enumerate(rows, 1):
        body.append(f"Data row {i} (row label cell, dark navy, white text: {q(a)}): second column {q(b)}; third column {q(c)}.")
    body += ["In data row 3 the words " + q("要らない") + " in the second column have a pale yellow highlighter marker, and in data row 4 the words " + q("要らない") + " in the third column have a pale yellow highlighter marker. Every other cell has its own text exactly as given."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the two marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解3：どちらの合併になるかの判定の流れ
def img3():
    body = [lead("1080x2900", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("どちらの合併になる？", "上から順に確かめる", "不動産登記法 第54条1項3号・第56条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas for START, DIAMOND 1 and DIAMOND 2, in this order from top to bottom. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between them. Below DIAMOND 2 the chart splits: DIAMOND 3 sits at the lower left and DIAMOND 4 sits at the lower right, on the same row. RESULT 2 and RESULT 3 sit below DIAMOND 3, one at the lower left and one at the lower center-left. RESULT 4 and RESULT 5 sit below DIAMOND 4, one at the lower center-right and one at the lower right. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("甲建物と乙建物の合併を考える"),
            "NODE DIAMOND 1: " + q("第56条の制限に当たるか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("当たる") + " and " + q("当たらない") + "; do not draw the strings 「はい」 or 「いいえ」 on these arrows.",
            "  - Arrow right with the label " + q("当たる") + " to RESULT 1.",
            "  - Arrow down with the label " + q("当たらない") + " to DIAMOND 2.",
            "NODE RESULT 1 (red box): " + q("どちらの合併も") + " on the first line and " + q("できない") + " on the second line.",
            "NODE DIAMOND 2: " + q("どちらも区分建物で、互いに接続しているか？") + " The text is placed inside the diamond on 3 lines. This diamond has TWO neutral navy branches with the labels " + q("接続する区分建物") + " and " + q("それ以外") + ".",
            "  - Arrow down-left with the label " + q("接続する区分建物") + " to DIAMOND 3.",
            "  - Arrow down-right with the label " + q("それ以外") + " to DIAMOND 4.",
            "NODE DIAMOND 3: " + q("主従の関係もあるか？") + " This diamond has TWO neutral navy branches with the labels " + q("ある") + " and " + q("ない") + ".",
            "  - Arrow down-left with the label " + q("ある") + " to RESULT 2.",
            "  - Arrow down-right with the label " + q("ない") + " to RESULT 3.",
            "NODE RESULT 2 (blue box): " + q("附属合併も") + " on the first line and " + q("区分合併も選べる") + " on the second line.",
            "NODE RESULT 3 (blue box): " + q("区分合併が") + " on the first line and " + q("できる") + " on the second line.",
            "NODE DIAMOND 4: " + q("主従の関係があるか？") + " This diamond has TWO neutral navy branches with the labels " + q("ある") + " and " + q("ない") + ".",
            "  - Arrow down-left with the label " + q("ある") + " to RESULT 4.",
            "  - Arrow down-right with the label " + q("ない") + " to RESULT 5.",
            "NODE RESULT 4 (blue box): " + q("附属合併が") + " on the first line and " + q("できる") + " on the second line.",
            "NODE RESULT 5 (red box): " + q("どちらの合併も") + " on the first line and " + q("できない") + " on the second line.",
            "Counts: 1 start node, 4 diamonds, 5 result boxes (3 blue boxes and 2 red boxes), 5 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three blue boxes have different texts (the strings " + q("附属合併も") + ", " + q("区分合併が") + " and " + q("附属合併が") + " are NOT identical); do not copy one into another. The two red boxes have the same text on purpose."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 4 diamonds and 5 result boxes, that every diamond shows only its two navy labels and no はい or いいえ, that RESULT 1 and RESULT 5 are red and RESULT 2, RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden.")

# ---------------------------------------------------------------- 図解4：場面ごとの早見表
def img4():
    rows = [("第56条の制限に当たる", "できない", "できない"),
            ("接続する区分建物どうしで、主従の関係もある", "できる", "できる"),
            ("接続する区分建物どうしで、主従の関係はない", "できない", "できる"),
            ("区分建物どうしだが接続しておらず、主従の関係はある", "できる", "できない"),
            ("区分建物でない建物がからみ、主従の関係はある", "できる", "できない"),
            ("主従の関係もなく、接続する区分建物どうしでもない", "できない", "できない")]
    body = [lead("1080x2300", "This is a quick-reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, COLOR] + \
           header("場面ごとの早見表", "どの合併ができる？", "不動産登記法 第54条1項3号") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: " + q("場面") + ", " + q("附属合併") + ", " + q("区分合併") + "."]
    for i, (a, b, c) in enumerate(rows, 1):
        body.append(f"Data row {i}: first column {q(a)}; second column {q(b)}; third column {q(c)}.")
    body += ["In data row 2 the words " + q("主従の関係もある") + " in the first column have a pale yellow highlighter marker. Every row has its own first-column text exactly as given; the second and third columns use only the two strings " + q("できる") + " and " + q("できない") + " exactly as listed row by row."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only the marked phrase in data row 2 carries the yellow marker, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解5：両方できるとき、合併後の姿で選ぶ
def img5():
    body = [lead("1080x1800", "This is a two-card choice poster."), TEXTREQ, BGREQ, COLOR] + \
           header("両方の要件がそろったら", "合併後の姿で選ぶ", "不動産登記法 第54条1項3号・不動産登記規則 第132条・第133条") + \
           ["--- TWO CARDS ---",
            "Two large cards stacked top and bottom, both exactly the same size, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, with no arrow and no connector between them, and with no check mark and no cross mark. The cards are separated only by a small empty gap.",
            "Top card, heading " + q("附属合併を選ぶ") + ", an illustration of two touching apartment rooms where the second room has a small annex box labeled " + q("附属建物") + ", and two body lines: " + q("甲建物が、乙建物の附属建物になる") + ", " + q("乙建物の登記記録に入り、甲建物の登記記録は閉鎖") + ".",
            "Bottom card, heading " + q("区分合併を選ぶ") + ", an illustration of two touching apartment rooms merged into one room, and two body lines: " + q("甲建物と乙建物が、一個の建物になる") + ", " + q("一棟の全部を合併すると、区分建物でなくなることがある") + ".",
            "Under the two cards, one wide dark navy band with large white text " + q("条文は選び方を定めていない") + ", and under it one wide pale-yellow banner with dark navy text " + q("問題文の指示と、合併後の姿で決める") + ".",
            "The top and bottom cards have clearly different texts; the texts are NOT identical."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly two cards plus the dark navy band and the pale-yellow banner, that the two cards have different texts, that no text overflows its box, and that no check mark or cross mark appears anywhere.")

META = [
    (1, "建物の合併は2種類（附属合併と区分合併）", "カードポスター型", "1080×2000", "図解1_建物の合併は2種類", "「ひとことで」の直後", img1),
    (2, "附属合併と区分合併の要件の対比表", "対比表型（3列）", "1080×1900", "図解2_附属合併と区分合併の対比表", "「部品1：合併の登記は2種類」の節の終わり", img2),
    (3, "どちらの合併になるかの判定の流れ", "フローチャート型", "1080×2900", "図解3_どちらの合併になるかの判定の流れ", "「部品4：両方の要件がそろうとき」の直前（判断の流れの節）", img3),
    (4, "場面ごとの早見表（どの合併ができるか）", "早見表型（3列）", "1080×2300", "図解4_場面ごとの早見表", "判定の流れの直後", img4),
    (5, "両方できるとき、合併後の姿で選ぶ", "二択カード型", "1080×1800", "図解5_合併後の姿で選ぶ", "「部品4：両方の要件がそろうとき」の節の終わり", img5),
]

def build_doc():
    out = ["# 区分合併と附属合併の使い分け　図解インフォグラフィック プロンプト（5枚）\n"]
    out.append("条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第54条1項3号（建物の合併の登記）の記事に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |\n|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。表の行数（図解2は5行、図解4は6行）と、図解3の分岐（ひし形4つ・結果5つ）も確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).resolve().parent.parent.joinpath("prompt_infographic_art054-1-3.md").write_text(doc, encoding="utf8")
    print(len(doc))
