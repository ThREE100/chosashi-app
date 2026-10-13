#!/usr/bin/env python3
"""総合記事②不動産登記法編 第6章：図解インフォグラフィック10枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PF1-1.md ／ _PF1-2.md ／ _PF1-3.md ／ _PF1-4.md ／ _PF1-5.md ／ _PF1-6.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
FLOWCOLOR = ("COLOR RULE (this flowchart): every arrow and every arrow label is dark navy; the strings 「はい」 and 「いいえ」 do not appear anywhere. "
             "The result boxes are colored by their outcome: a result box that says 「5号の制限に当たらない」 is BLUE, and a result box that says 「5号の制限に当たる」 is RED. Use dark navy for the start pill, the diamonds' outlines, the headings, and the badges, and a pale yellow highlighter only for strings marked as emphasized.")

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def table_rows(rows):
    return [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]

# ============================================================ 図解1：分棟・分割・合併・一括申請（役割マップ）
def img1():
    cards = [
        ("分棟", "A long single building icon with its middle section removed, leaving two small separate buildings, no text.",
         ["1棟の建物を、主と附属の2棟にする", "表題部の変更の登記", "登録免許税は、かからない"], "表題部の変更"),
        ("分割", "Two building icons being pulled apart, the smaller one drawn with a dashed outline, no text.",
         ["附属建物を、別の1個の建物にする", "所有者が申請する（職権ではしない）", "抵当権は承諾を証する情報で消せる"], "所有者の意思で別の建物に"),
        ("合併", "Two building icons being combined into one building icon, no text.",
         ["附属合併と区分合併がある", "法56条の制限に当たらないこと", "図面は合併後の姿で付ける"], "制限と図面"),
        ("一の申請情報", "Two application sheets clipped together into one, no text.",
         ["規則35条に挙がる組合せだけ", "表題部の変更と、分割・区分・合併", "分棟と分割も、まとめられる"], "規則35条"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, three short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("分棟・分割・合併の違い", "何の登記で、何を確かめる？", "不動産登記法 第54条・第56条／不動産登記規則 第35条")
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：法56条の5つ（早見表）
def img2():
    rows = [
        ("1号", "共用部分である旨の登記又は団地共用部分である旨の登記がある建物", "両方にあっても不可"),
        ("2号", "表題部所有者・所有権の登記名義人が相互に異なる建物", "名義人が違う"),
        ("3号", "表題部所有者・所有権の登記名義人が相互に持分を異にする建物", "持分が違う"),
        ("4号", "所有権の登記がない建物と、所有権の登記がある建物", "登記の有無が違う"),
        ("5号", "所有権等の登記以外の権利に関する登記がある建物", "例外は担保権と信託（規則131条）"),
    ]
    body = [lead("1080x1900", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合併できない建物は？", "法56条の5つを覚える", "不動産登記法 第56条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("合併の登記ができない建物") + ", " + q("見分け方") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the string 「両方にあっても不可」 of row 1 and the string 「例外は担保権と信託（規則131条）」 of row 5 have a pale yellow highlighter marker; the other cells are plain. Copy each cell exactly as given.",
            "Row order rule: the first column reads 「1号」, 「2号」, 「3号」, 「4号」, 「5号」 from top to bottom, each exactly once; no row is duplicated, merged, or missing.",
            "Under the table, one wide dark navy band with large white text " + q("地番区域が異なっても、建物は合併できる") + " and, directly below it, one smaller line of white text " + q("土地の合筆は、地番区域が異なると不可（法41条2号）") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 5 data rows in the order 1号 to 5号, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：住所が食い違うとき（ステップ）
def img3():
    body = [lead("1080x2400", "This is a vertical step poster with four step cards and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("住所が食い違うとき", "合併の前に何をする？", "建物の合併の登記（実務の取扱い）") + \
           ["--- STEPS ---",
            "Layout: four step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to 4 in order), one bold heading line, and one or two short body lines.",
            "STEP 1: heading " + q("甲建物の登記は、旧住所のまま") + ", body " + q("引っ越したあとに、乙建物を取得して登記した") + ".",
            "STEP 2: heading " + q("登記記録上の住所が、食い違う") + ", body " + q("同じ人でも、同一人とは扱われない") + ".",
            "STEP 3 (the card has a pale yellow highlighter marker on its heading): heading " + q("住所の変更を証する情報を付けても足りない") + ", body " + q("住民票を付けても、合併はできない") + ".",
            "STEP 4: heading " + q("先に、甲建物の住所の変更の登記をする") + ", body " + q("そのあとで、合併の登記を申請する") + ".",
            "--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("住居表示の実施で住所が変わったときも同じ") + ", body " + q("住居表示の実施を証する情報を付けても足りない") + " and a small gray tag " + q("条文に明記はなく、実務の取扱い") + "."]
    return finish(body, "Confirm there are exactly four step cards numbered 1 to 4 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解4：権利の登記がある建物は合併できるか（判定フロー）
def img4():
    body = [lead("1080x2900", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, FLOWCOLOR] + \
           header("権利の登記がある建物は", "合併できる？", "不動産登記法 第56条5号／不動産登記規則 第131条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. The result boxes of DIAMOND 1 and DIAMOND 2 sit to the RIGHT of their diamonds on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("合併しようとする2つの建物"),
            "NODE DIAMOND 1: " + q("所有権等以外の権利の登記が、ある？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. Under the diamond, a small gray caption " + q("所有権等：所有権・地上権・永小作権・地役権・採石権") + ".",
            "  - Arrow right to RESULT 1 with the dark navy label " + q("ない") + ".",
            "  - Arrow down to DIAMOND 2 with the dark navy label " + q("ある") + ".",
            "NODE RESULT 1 (blue box): " + q("5号の制限に当たらない") + " on the first line and " + q("ほかの号は別に確かめる") + " on the second line.",
            "NODE DIAMOND 2: " + q("その登記は、担保権の登記か信託の登記か？"),
            "  - Arrow down to DIAMOND 3 with the dark navy label " + q("そうである") + ".",
            "  - Arrow right to RESULT 2 with the dark navy label " + q("それ以外") + ".",
            "NODE RESULT 2 (red box): " + q("5号の制限に当たる") + " on the first line and " + q("賃借権などは、同一でも不可") + " on the second line.",
            "NODE DIAMOND 3: " + q("両建物で、決まった項目が同一か？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow down-left with the dark navy label " + q("同一") + " to RESULT 3.",
            "  - Arrow down-right with the dark navy label " + q("同一でない") + " to RESULT 4.",
            "NODE RESULT 3 (blue box): " + q("5号の制限に当たらない") + " on the first line and " + q("規則131条の例外に当たる") + " on the second line.",
            "NODE RESULT 4 (red box): " + q("5号の制限に当たる") + " on the first line and " + q("決まった項目が同一でない") + " on the second line.",
            "Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different second lines, and the two red result boxes have different second lines. The first-line strings " + q("5号の制限に当たらない") + " (blue) and " + q("5号の制限に当たる") + " (red) differ by two characters and are NOT identical; copy each exactly as given and never turn one into the other.",
            "--- TWO SIDE NOTE CARDS (below the flowchart, side by side, exactly the same size, each with a dashed dark navy outline and its heading placed fully INSIDE the card) ---",
            "Left card, heading " + q("同一でなければならない項目") + ", two body lines " + q("担保権の登記：登記の目的、受付の年月日及び受付番号、登記原因及びその日付") + " and " + q("信託の登記：法97条1項各号の登記事項") + ".",
            "Right card, heading " + q("工場財団の登記がある建物") + ", body " + q("同一の財団を組成していても、合併できない") + " and a small gray tag " + q("条文に直接の定めはない") + ".",
            "The two cards have clearly different texts; the texts are NOT identical."]
    return finish(body, "Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that every arrow label is dark navy and the strings 「はい」 and 「いいえ」 appear nowhere, that RESULT 1 and RESULT 3 are blue and read 5号の制限に当たらない and RESULT 2 and RESULT 4 are red and read 5号の制限に当たる, that exactly two side note cards sit below the flowchart, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解5：区分合併の要件（対比カード）
def img5():
    need = ["法56条の制限に当たらない", "互いに接続している"]
    noneed = ["効用上一体の関係にあること", "敷地権の割合が同じであること", "敷地権の有無が同じであること"]
    body = [lead("1080x2100", "This is a comparison poster with a banner at the top and two side-by-side list cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("区分合併に要るのは？", "要件は2つだけ", "不動産登記法 第54条・第56条／不動産登記規則 第133条") + \
           ["--- TOP BANNER (one wide dark navy band with white text) ---",
            q("区分合併：区分建物を、接続する区分建物に合併して一個の建物とする登記"),
            "--- TWO LIST CARDS (side by side, exactly the same size, top-aligned) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("要るもの（2つ）") + ". The two rows, in this order, each in a pale-yellow highlighted row:"] + \
           [f"  Row {i}: {q(x)}" for i, x in enumerate(need, 1)] + \
           ["Right card: heading bar (pale gray fill, dark navy text) " + q("要件にならないもの（3つ）") + ". The three rows, in this order:"] + \
           [f"  Row {i}: {q(x)}" for i, x in enumerate(noneed, 1)] + \
           ["The two cards have clearly different texts; the texts are NOT identical. Left card rows are all highlighted; right card rows are plain.",
            "Under the two cards, one wide dark navy band with large white text " + q("敷地権は、権利部ではなく表題部の登記事項") + " and, directly below it, one smaller line of white text " + q("接続していなければ、区分合併はできない") + "."]
    return finish(body, "Confirm there are exactly two cards, that the left card has exactly two rows and the right card has exactly three rows, that the two heading bars are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解6：分棟の流れ（ステップ）
def img6():
    body = [lead("1080x2400", "This is a vertical step poster with four step cards and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("分棟の登記は", "何を、どう申請する？", "不動産登記規則 第35条第7号") + \
           ["--- STEPS ---",
            "Layout: four step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to 4 in order), one bold heading line, and one or two short body lines.",
            "STEP 1: heading " + q("1棟の建物として登記されている") + ", body " + q("区分建物でない建物") + ".",
            "STEP 2: heading " + q("中間部分を取り壊し、障壁を施す") + ", body " + q("相互に接続しない2棟になる") + ".",
            "STEP 3 (the card has a pale yellow highlighter marker on its heading): heading " + q("分棟の登記をする") + ", two body lines " + q("主である建物と附属建物になる") + " and " + q("表題部の変更の登記で、課税されない") + ".",
            "STEP 4: heading " + q("別個の建物にするなら、分割の登記も要る") + ", body " + q("分棟の登記と分割の登記は、一の申請情報でできる") + ".",
            "--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("分棟は、滅失と新築ではない") + ", body " + q("抹消の登記と表題登記を一の申請情報でする決まりはない") + "."]
    return finish(body, "Confirm there are exactly four step cards numbered 1 to 4 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解7：規則35条の組合せ（早見表）
def img7():
    rows = [
        ("2号", "建物の分割の登記と、他の建物の附属建物とする合併の登記", "分割と附属合併"),
        ("3号", "区分建物である附属建物の分割の登記と、区分合併の登記", "相手が接続する区分建物のときだけ"),
        ("4号", "建物の区分の登記と、附属建物とする合併の登記", "区分と附属合併"),
        ("5号", "建物の区分の登記と、区分合併の登記", "相手が接続する区分建物のときだけ"),
        ("6号", "同一の不動産の表題部の変更の登記又は更正の登記どうし", "変更どうしは一括できる"),
        ("7号", "同一の不動産の表題部の変更の登記又は更正の登記と、建物の分割・区分・合併の登記", "増築の変更と分割／種類変更と合併／分棟と分割"),
    ]
    body = [lead("1080x2100", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("一の申請情報にできる", "建物の組合せは？", "不動産登記規則 第35条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 6 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("一の申請情報にできる登記") + ", " + q("ひとこと") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the string 「増築の変更と分割／種類変更と合併／分棟と分割」 of row 7 has a pale yellow highlighter marker; the other cells are plain. The cells of row 3 and row 5 in column 3 read the same; copy each cell exactly as given.",
            "Row order rule: the first column reads 「2号」, 「3号」, 「4号」, 「5号」, 「6号」, 「7号」 from top to bottom, each exactly once; no row is duplicated, merged, or missing (there is no 「1号」 row in this table).",
            "Under the table, one wide dark navy band with large white text " + q("目的が違っても、この号に当たれば一の申請情報にできる") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 6 data rows in the order 2号 to 7号 with no 1号 row, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解8：分割した乙建物の甲区（原則と例外）
def img8():
    body = [lead("1080x2500", "This is a comparison poster: two cards at the top, a three-stage row in the middle, and one wide card at the bottom."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("分割した乙建物には", "何が記録される？", "不動産登記規則 第128条") + \
           ["--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card, small tag " + q("規則128条1項") + ", heading " + q("原則は、転写") + ", three body lines " + q("分割前の甲建物の") + ", " + q("権利に関する登記を") + ", " + q("乙建物に転写する") + ".",
            "Right card, small tag " + q("規則128条2項") + ", heading " + q("例外は、旨を記録") + ", three body lines " + q("所有権の登記のあとに、") + ", " + q("附属建物の新築による") + ", " + q("表題部の変更の登記があるとき") + ", and under them a pale-yellow highlighted line " + q("転写に代えて、旨を記録する") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- THREE-STAGE ROW (below the two cards, with a small dark navy tag 「例外に当たる場面の順番」 above it; three cards in ONE row from left to right, all the same size; no arrows, no connectors) ---",
            "Stage card 1: badge " + q("まず") + ", text " + q("甲建物に所有権の登記") + ".",
            "Stage card 2: badge " + q("次に") + ", text " + q("附属建物を新築して変更の登記") + ".",
            "Stage card 3: badge " + q("最後に") + ", text " + q("その附属建物を分割して乙建物に") + ".",
            "--- WIDE CARD (at the bottom, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("旨を記録するとき、乙建物の甲区に記録されるもの") + ", three short rows each with a small dark navy dot at its left end (NO number on the dots): " + q("分割による所有権の登記をする旨") + ", " + q("所有権の登記名義人の氏名又は名称及び住所") + ", " + q("登記の年月日") + "."]
    return finish(body, "Confirm there are exactly two cards at the top (left 原則は、転写 and right 例外は、旨を記録, never swapped), exactly three stage cards in one row in the order まず, 次に, 最後に, and exactly one wide card at the bottom with exactly three rows, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解9：分割の登記の承諾と所在の記録
def img9():
    body = [lead("1080x2000", "This is a comparison poster with two side-by-side cards and one band."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("分割の登記の手続と記録", "承諾の要否と所在の記録", "不動産登記法 第54条第3項・第40条／不動産登記規則 第127条") + \
           ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("法54条3項・40条") + ", heading " + q("分割後の建物から抵当権を消すには") + ", and exactly three short rows, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("要る：権利者の承諾を証する情報") + ", " + q("要らない：登記識別情報") + ", " + q("第三者の権利の登記があれば、その者の承諾も要る") + ". The row " + q("要らない：登記識別情報") + " has a pale yellow highlighter marker.",
            "Right card: small tag " + q("規則127条3項") + ", heading " + q("分割で所在が変わるとき") + ", and exactly four short rows, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("変更後の所在") + ", " + q("分割により変更した旨") + ", " + q("変更前の所在を消す記号") + ", " + q("別に変更の登記を申請する必要はない") + ". The row " + q("別に変更の登記を申請する必要はない") + " has a pale yellow highlighter marker.",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("消すのに要るのは、承諾を証する情報だけ") + "."]
    return finish(body, "Confirm there are exactly two cards, that the left card has exactly three rows and the right card has exactly four rows, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解10：合併の登記の図面・登記識別情報・登録免許税
def img10():
    body = [lead("1080x2400", "This is a quick-reference poster: three numbered cards and two side note cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合併の登記に付けるもの", "図面・識別情報・税", "不動産登記令 別表16の項・第8条／登録免許税法 別表第一") + \
           ["--- THREE CARDS (stacked top to bottom, all the same size, each with a dark navy circle badge numbered 1 to 3 in order, one bold heading line, one small gray tag, and one pale-yellow body banner) ---",
            "CARD 1: heading " + q("合併後の建物図面及び各階平面図") + ", small gray tag " + q("令別表16の項") + ", body banner " + q("床面積に変更がなくても、省略できない") + ".",
            "CARD 2: heading " + q("いずれか一個の建物の名義人の登記識別情報") + ", small gray tag " + q("令8条1項3号・2項3号") + ", body banner " + q("所有権の登記がある建物の合併のとき") + ".",
            "CARD 3: heading " + q("合併後の建物の個数×1,000円") + ", small gray tag " + q("登録免許税法 別表第一") + ", body banner " + q("所有権の登記がある建物の分割・区分・合併") + ".",
            "--- TWO SIDE NOTE CARDS (below the three cards, stacked, each a wide card with a dashed dark navy outline and its heading placed fully INSIDE the card) ---",
            "Side note 1: heading " + q("分棟の登記（表題部の変更の登記）") + ", body " + q("登録免許税はかからない") + ".",
            "Side note 2: heading " + q("保存登記のあとに附属建物にした建物を、分割して乙建物の附属建物に合併するとき") + ", body " + q("甲建物の保存登記時ではなく、乙建物の名義人の登記識別情報を提供する") + " and a small gray tag " + q("条文に直接の定めはなく、実務の取扱い") + "."]
    return finish(body, "Confirm there are exactly three numbered cards (1 to 3 in order) followed by exactly two side note cards, that card 3 reads 合併後の建物の個数×1,000円, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "分棟・分割・合併・一の申請情報の違い（4つの登記）", "カードポスター型（俯瞰）", "1080×2300", "不登法編6章_図解1_分棟分割合併の違い", "「この章の誤りの傾向」の直前（論点一覧の直後）", img1, "00_zentai"),
    (2, "合併できない建物は？（法56条の5つ）", "早見表型（3列）", "1080×1900", "不登法編6章_図解2_法56条の5つ", "【PF1-1】「中身の整理」の直後", img2, "PF1-1"),
    (3, "住所が食い違うとき、合併の前に何をする？", "ステップ型", "1080×2400", "不登法編6章_図解3_住所の食い違い", "【PF1-1】「たとえば」の直後", img3, "PF1-1"),
    (4, "権利の登記がある建物は合併できる？（判定の流れ）", "フローチャート／判定フロー型", "1080×2900", "不登法編6章_図解4_権利の登記と合併の判定", "【PF1-2】「中身の整理」の直後", img4, "PF1-2"),
    (5, "区分合併に要るのは？（要件は2つだけ）", "対比カード型（2列）", "1080×2100", "不登法編6章_図解5_区分合併の要件", "【PF1-3】「中身の整理」の直後", img5, "PF1-3"),
    (6, "分棟の登記は何を、どう申請する？", "ステップ型", "1080×2400", "不登法編6章_図解6_分棟の流れ", "【PF1-4】「中身の整理」の直後", img6, "PF1-4"),
    (7, "一の申請情報にできる建物の組合せ（規則35条）", "早見表型（3列）", "1080×2100", "不登法編6章_図解7_規則35条の組合せ", "【PF1-4】図解6の直後", img7, "PF1-4"),
    (8, "分割した乙建物には何が記録される？（転写と旨の記録）", "対比カード型＋3段階", "1080×2500", "不登法編6章_図解8_分割後の乙建物の記録", "【PF1-5】「中身の整理」の直後", img8, "PF1-5"),
    (9, "分割の登記の承諾の要否と所在の記録", "対比カード型（2列）", "1080×2000", "不登法編6章_図解9_分割の承諾と所在の記録", "【PF1-5】図解8の直後", img9, "PF1-5"),
    (10, "合併の登記に付けるもの（図面・登記識別情報・登録免許税）", "カードポスター型", "1080×2400", "不登法編6章_図解10_合併の図面識別情報税", "【PF1-6】「中身の整理」の直後", img10, "PF1-6"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PF1-1": ("prompt_infographic_PF1-01.md", "【PF1-1】合併の登記ができないのはどんな場合か（法第56条）"),
    "PF1-2": ("prompt_infographic_PF1-02.md", "【PF1-2】抵当権・賃借権などの登記があるとき合併できるか（法第56条第5号・規則第131条）"),
    "PF1-3": ("prompt_infographic_PF1-03.md", "【PF1-3】区分建物の合併（区分合併）にはどんな要件があるか"),
    "PF1-4": ("prompt_infographic_PF1-04.md", "【PF1-4】分棟・分割の登記と、一の申請情報でまとめられる組合せ"),
    "PF1-5": ("prompt_infographic_PF1-05.md", "【PF1-5】分割の登記で、登記記録にはどう記録され、抵当権はどうなるか"),
    "PF1-6": ("prompt_infographic_PF1-06.md", "【PF1-6】合併の添付情報・登記識別情報・登録免許税"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第6章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この章の図解は『できない建物の一覧』『要る・要らない』のような分類が中心なので、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
               "フローチャート（図解4）だけは、分岐の矢印とラベルを濃紺にし、結果の箱を『5号の制限に当たらない＝青』『5号の制限に当たる＝赤』で塗り分けます（『はい』『いいえ』の文字は使いません）。"
               "画像の中には、図の番号・問題番号・個人の演習結果（誤答の回数など）を入れません。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |\n|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _, _k in items:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc, _k in items:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    return fname, "\n".join(out)

if __name__ == "__main__":
    for key in FILES:
        fname, doc = build_doc(key)
        (OUT / fname).write_text(doc, encoding="utf8")
        print(fname, len(doc))
