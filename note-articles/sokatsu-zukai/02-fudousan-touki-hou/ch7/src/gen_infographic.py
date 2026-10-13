#!/usr/bin/env python3
"""総合記事② 不動産登記法編 第7章（建物の合体による登記等）：図解インフォグラフィック10枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch7/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PF2-1.md ／ _PF2-2.md ／ _PF2-3.md ／ _PF2-4.md ／ _PF2-5.md ／ _PF2-6.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
TBL = "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

# ============================================================ 図解1：確かめる6つ（章の冒頭の全体図）
def img1():
    cards = [
        ("合体か、そうでないか", "Two small registry ledger books side by side, each with a tiny building icon, joined by a plain bracket into one larger building icon; no text anywhere.",
         ["別々に登記された建物が、一個になる", "主と附属の一体化は、合体ではない"], "別々の登記が条件"),
        ("合体前の登記は、どうなっているか", "Three building icons in a row: the first with a stamp mark, the second with a dashed outline, the third with a ledger book beneath it; no text anywhere.",
         ["すべて未登記なら、新築の表題登記", "登記のある建物があれば、合体による登記等"], "未登記か、登記ありか"),
        ("誰が、いつまでに申請するか", "A calendar page with a rubber stamp beside a plain person pictogram; no text anywhere.",
         ["申請人が並ぶ号は、一人から単独で申請できる", "合体の日から1か月以内"], "単独で、1か月以内"),
        ("合体前の権利は、どうなるか", "A house icon with a small padlock-shaped tag attached, and beside it a second thin dashed-outline tag that is not attached; no text anywhere.",
         ["抵当権などは、承諾を得て存続できる", "賃借権は、存続させられない"], "存続か、そうでないか"),
        ("合体後の持分は、書くのか", "A round pie shape divided into two slices placed in front of a small building icon; no numbers and no text anywhere.",
         ["同一人の建物は、持分を申請情報に書く", "存続登記がすべて同一なら、書かなくてよい"], "原則と、その例外"),
        ("何が、要らなくなるか", "A coin icon drawn with a dashed outline next to a document sheet with a rubber stamp; no text anywhere.",
         ["合体の登記等は、登録免許税がかからない", "住所の変更の登記は、先にしなくてよい"], "非課税・先の登記は不要"),
    ]
    body = [lead("1080x2700", "This is a quick-reference poster with six numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("合体による登記等", "確かめる6つの順番", "不動産登記法 第49条・第50条")
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 6 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (two short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, "Confirm the number of cards equals 6 exactly, numbered 1 to 6 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：合体による登記等とは何を申請するのか
def img2():
    body = [lead("1080x1800", "This is a vertical explainer poster: one before/after illustration card, two numbered application cards, one deadline band, and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体による登記等", "申請するのは、この2つ", "不動産登記法 第49条第1項") + \
           ["--- BEFORE/AFTER CARD (a wide pale gray card with a dark navy outline) ---",
            "Left half: the small tag " + q("合体前の建物") + ", two small building icons side by side, each with its own small registry ledger book beneath it (no text on the books). Right half: the small tag " + q("合体後の建物") + ", one larger building icon formed by joining the two, with one new ledger book beneath it (no text on the book). Between the two halves, exactly one plain right-pointing dark navy arrow that carries no text.",
            "--- TWO APPLICATION CARDS (stacked top to bottom, the same size, each with a dark navy circle badge numbered 1 and 2 in order, one bold heading line, and one body line; a dark navy bracket at their right side joins the two cards) ---",
            "CARD 1: heading " + q("合体後の建物の表題登記") + ", body " + q("新しい一個の建物として登記する") + ".",
            "CARD 2: heading " + q("合体前の建物の表題部の登記の抹消") + ", body " + q("合体前の各建物の表題部の登記を消す") + ".",
            "Next to the bracket, a small dark navy tag with white text " + q("2つを合わせて、合体による登記等") + ".",
            "--- DEADLINE BAND (a wide dark navy band with large white text) ---",
            q("申請の期限は、合体の日から1か月以内"),
            "--- SIDE NOTE CARD (below the band, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("滅失の登記ではない") + ", body " + q("建物がなくなるわけではないので、滅失の登記は申請しない") + "."]
    return finish(body, "Confirm there is exactly one before/after card, exactly two application cards numbered 1 and 2, one deadline band, and one side note card, that the arrow between the two halves carries no text, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：合体になる？ならない？
def img3():
    rows = [
        ("別々に登記された建物が、増築で一個になった", "合体になる", "合体による登記等を、1か月以内に申請する"),
        ("区分建物の隔壁を取り壊し、区分建物でない一個の建物になった", "合体になる", "滅失の登記ではなく、合体による登記等を申請する"),
        ("主である建物と附属建物が一体化した", "合体にならない", "建物の表題部の変更の登記で対応する"),
        ("附属建物が、他の建物と合体した", "合体になる", "分割の登記と合体による登記等は、別々の申請"),
    ]
    body = [lead("1080x2000", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体になる？ならない？", "場面で仕分ける", "不動産登記法 第49条") + \
           ["--- TABLE ---",
            TBL + " Exactly 3 columns and exactly 4 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("場面") + ", " + q("合体になるか") + ", " + q("申請の形") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: in column 2, the string 「合体にならない」 of row 3 has a pale yellow highlighter marker; the other three cells in column 2 are plain. In column 3, the string 「別々の申請」 of row 4 has a pale yellow highlighter marker. The cells 「合体になる」 and 「合体にならない」 differ by two characters; copy each exactly as given and do not change one into the other.",
            "Under the table, one wide dark navy band with large white text " + q("合体になるのは、別々に登記された建物が一個になったとき") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that only row 3 reads 「合体にならない」 in column 2, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解4：合体前の建物の登記の状態（判定の流れ）
def img4():
    body = [lead("1080x2300", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("合体前の建物の登記は", "どうなっているか", "不動産登記法 第49条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 and RESULT 3 sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("二以上の建物が合体して、一個の建物になった"),
            "NODE DIAMOND 1: " + q("合体前の建物は、いずれも表題登記がない建物か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("新築の建物の表題登記を申請する") + " on the first two lines, " + q("登記原因は、新築、新築、合体の形") + " on the next two lines, and the small gray tag " + q("実務の取扱い") + " on the last line.",
            "NODE DIAMOND 2: " + q("所有権の登記がある建物と、ない建物が混じっているか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down-left with the BLUE label " + q("はい") + " to RESULT 2.",
            "  - Arrow down-right with the RED label " + q("いいえ") + " to RESULT 3.",
            "NODE RESULT 2 (blue box): " + q("合体による登記等と、所有権の登記を併せて申請する") + " on the first three lines, " + q("未登記の建物の所有者や表題部所有者を、登記名義人とする") + " on the next three lines, and the small gray tag " + q("法49条1項後段") + " on the last line.",
            "NODE RESULT 3 (red box): " + q("合体による登記等だけを申請する") + " on the first two lines.",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another."]
    return finish(body, "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解5：誰が申請するか（法49条1項各号）
def img5():
    rows = [
        ("1号", "表題登記がない建物と、表題登記のみの建物", "未登記建物の所有者または表題部所有者"),
        ("2号", "表題登記がない建物と、所有権の登記がある建物", "未登記建物の所有者または所有権の登記名義人"),
        ("3号", "いずれも表題登記のみの建物", "表題部所有者"),
        ("4号", "表題登記のみの建物と、所有権の登記がある建物", "表題部所有者または所有権の登記名義人"),
        ("5号", "いずれも所有権の登記がある建物", "所有権の登記名義人"),
        ("6号", "三以上の建物で、未登記・表題登記のみ・所有権の登記ありが混じる", "未登記建物の所有者、表題部所有者または所有権の登記名義人"),
    ]
    body = [lead("1080x2200", "This is a reference table poster with three columns (早見表), followed by one dashed side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体の申請は、誰が？", "一人から単独で申請できる", "不動産登記法 第49条第1項") + \
           ["--- TABLE ---",
            TBL + " Exactly 3 columns and exactly 6 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("合体前の建物") + ", " + q("申請人") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: the string 「または」 inside the column-3 cells of rows 1, 2, 4 and 6 has a pale yellow highlighter marker; rows 3 and 5 have a slightly darker pale gray cell fill in column 3 because they name only one kind of person. Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q("申請人が二つ並ぶ号は、そのうちの一人から単独で申請できる") + ".",
            "--- SIDE NOTE CARD (below the band, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("共同申請の定めはない") + ", body " + q("権利に関する登記の共同申請（法60条）は、表示に関する登記にはない") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that rows 3 and 5 are the only rows with a single kind of person in column 3 and that rows 1, 2, 4 and 6 contain 「または」, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解6：1か月の数え始め
def img6():
    stages = [
        ("原則", "合体の日から1か月以内", "各号に定める申請人は、合体の日から数える", "法49条1項"),
        ("合体の後に持分を取得した人", "持分の取得の日から1か月以内", "合体前の未登記の建物の所有者から、持分を取得した人", "法49条3項"),
        ("合体の後に名義人になった人", "登記があった日から1か月以内", "表題部所有者または所有権の登記名義人になった人は、その者に係る更正の登記または所有権の登記があった日から数える", "法49条4項"),
    ]
    body = [lead("1080x2000", "This is a vertical poster with three stage cards and one closing band."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("1か月の数え始めは", "人によって違う", "不動産登記法 第49条第1項・第3項・第4項") + \
           ["--- STAGE CARDS ---",
            "Layout: three stage cards stacked top to bottom on the center line, all the same size, separated only by a small empty gap (no arrows, nothing drawn between them). Each stage card has a dark navy badge with its stage name at the top left, one bold heading line, one body text, and one small gray tag at the bottom right."]
    for i, (b, h, t, tag) in enumerate(stages, 1):
        body.append(f"STAGE CARD {i}: badge " + q(b) + ", heading " + q(h) + ", body " + q(t) + ", small gray tag " + q(tag) + ".")
    body += ["The three headings are different texts; do not copy one into another.",
             "--- CLOSING BAND (a wide pale yellow band with a thin dark navy outline and dark navy text) ---",
             q("1か月は同じ。数え始める日が違う")]
    return finish(body, "Confirm there are exactly three stage cards in the order 原則, 合体の後に持分を取得した人, 合体の後に名義人になった人, followed by exactly one closing band, that no arrow is drawn between the cards, that the badge of the first card reads 原則 exactly (never 思則), and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解7：権利の仕分け
def img7():
    rows = [
        ("所有権の登記以外の所有権に関する登記", "存続させられる", "権利者の承諾情報等（ト）"),
        ("先取特権・質権の登記", "存続させられる", "権利者の承諾情報等（ト）"),
        ("抵当権の登記", "存続させられる", "権利者の承諾情報等（ト）"),
        ("抵当証券が発行されている抵当権", "存続させられる", "承諾情報等（チ）と抵当証券"),
        ("賃借権の登記", "存続させられない（実務の整理）", "申請情報にも書かない"),
    ]
    body = [lead("1080x2100", "This is a reference table poster with three columns (早見表), followed by one dashed side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体前の権利は、どうなる？", "存続させる権利を仕分ける", "不動産登記法 第50条・不動産登記令 別表13の項") + \
           ["--- TABLE ---",
            TBL + " Exactly 3 columns and exactly 5 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("合体前の権利") + ", " + q("合体後の建物の持分に") + ", " + q("添えるもの") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: the string 「と抵当証券」 in the column-3 cell of row 4 has a pale yellow highlighter marker; row 5 has a slightly darker pale gray fill across all three cells to show that it is the one that cannot be kept. Copy each cell exactly as given; the cells 「存続させられる」 and 「存続させられない（実務の整理）」 differ in wording, so do not change one into the other.",
            "--- SIDE NOTE CARD (below the table, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("存続させずに消すとき") + ", body " + q("権利者が消滅を承諾した情報を提供して、消滅の登記をする（法50条）") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 5 data rows, that rows 1 to 4 read 「存続させられる」 and only row 5 reads 「存続させられない（実務の整理）」, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解8：添付情報を記号で結ぶ
def img8():
    rows = [
        ("イ", "建物図面"),
        ("ロ", "各階平面図"),
        ("ハ", "表題部所有者となる者が所有権を有することを証する情報"),
        ("ニ", "表題部所有者となる者の住所を証する情報"),
        ("ホ", "敷地権とならない事由を証する情報（合体前後とも敷地権の登記がない区分建物のときは不要）"),
        ("ヘ", "合体後の建物に敷地権が存するときの、規約を設定したことを証する情報など"),
        ("ト", "存続登記と同一の登記をするときの、権利者の承諾情報等"),
        ("チ", "抵当証券が発行されているときの、承諾情報等と抵当証券"),
        ("リ", "所有権の登記を併せて申請するときの、登記名義人となる者の住所を証する情報"),
    ]
    body = [lead("1080x2400", "This is a reference table poster with two columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体の添付情報", "記号で呼び分けて覚える", "不動産登記令 別表13の項") + \
           ["--- TABLE ---",
            TBL + " Exactly 2 columns and exactly 9 data rows, no merged cells. Column 1 is narrow and holds one katakana letter; column 2 is wide.",
            "Header row (dark navy cells with white text): " + q("記号") + ", " + q("添える情報") + ".",
            "Data rows, one per line, in this order (column 1 | column 2):"] + \
           [f"Row {i}: {q(a)} | {q(b)}" for i, (a, b) in enumerate(rows, 1)] + \
           ["Highlighting: the katakana letters of rows 3, 5, 7 and 8 (ハ, ホ, ト, チ) in column 1 have a pale yellow highlighter marker; all other cells are plain. The nine katakana letters in column 1 are different from each other and appear in the order イ, ロ, ハ, ニ, ホ, ヘ, ト, チ, リ; copy each exactly as given."]
    return finish(body, "Confirm the table has exactly 2 columns and exactly 9 data rows, that column 1 reads イ, ロ, ハ, ニ, ホ, ヘ, ト, チ, リ in this order with no letter duplicated or missing, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解9：持分を書くとき・書かなくてよいとき
def img9():
    same4 = ["登記の目的", "申請の受付の年月日及び受付番号", "登記原因及びその日付", "登記名義人"]
    body = [lead("1080x2100", "This is a comparison poster: two cards side by side at the top and one wide card below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体後の持分は、いつ書く？", "書く場合と、書かなくてよい場合", "不動産登記令 別表13の項申請情報ニ") + \
           ["--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("原則") + ", heading " + q("持分を書く") + " (the string 「持分を書く」 has a pale yellow highlighter marker), and two short body lines: " + q("存続登記がある建物の名義人が、他の建物の所有者・名義人と同一のとき") + ", " + q("同一でないとみなした場合の持分を、申請情報の内容とする") + ".",
            "Right card: small tag " + q("かっこ書の例外") + ", heading " + q("持分を書かなくてよい") + " (the string 「持分を書かなくてよい」 has a pale yellow highlighter marker), one body line " + q("二以上の存続登記が、次の4つともすべて同一のとき") + ", and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): " + ", ".join(q(x) for x in same4) + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- WIDE CARD (below the two cards, a wide card with a dashed dark navy outline) ---",
            "Small gray tag " + q("実務の取扱い（条文に明記なし）") + ", heading " + q("持分の割合を証する情報") + ", body " + q("全員が申請人で、申請情報とあわせて印鑑証明書を提供したときは、別に提供しない") + "."]
    return finish(body, "Confirm there are exactly two cards at the top, that the left card is the 原則 card with the heading 持分を書く and the right card is the 例外 card with the heading 持分を書かなくてよい and exactly four item lines, that the small tag of the left card reads 原則 exactly (never 思則), that exactly one wide card sits below them, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解10：合体の登記等で要らなくなるもの
def img10():
    cards = [
        ("登録免許税", "非課税", ["合体による登記等そのものは、課税されない", "課税されるのは、併せて申請する所有権の登記だけ"], "A coin icon drawn with a dashed outline beside a document sheet with a rubber stamp; no text anywhere."),
        ("住所の変更の登記", "実務の取扱い", ["名義人の住所が変わっていても、先に変更の登記はしない", "変更を証する情報を添付すれば足りる"], "A house icon with a small envelope beside it, and a document sheet carrying a rubber stamp; no text anywhere."),
        ("敷地権でない旨の証明", "令別表13の項ホのかっこ書", ["合体前の区分建物のいずれにも敷地権の登記がなく、合体後にもないとき", "敷地権でないことを証する情報は、要らない"], "A building icon standing on a small plot of land, with a plain document sheet beside it; no text anywhere."),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster: three numbered cards and one dashed comparison card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体の登記等で", "要らなくなるもの", "登録免許税法 別表第一・不動産登記令 別表13の項")
    for i, (h, tag, items, ill) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 3 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Two short item lines of dark navy text beside the illustration, each with a small dark navy dot at its left end (NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase):", q(tag)]
    body += ["--- COMPARISON CARD (below the three cards, a wide card with a dashed dark navy outline and a small dark navy tag " + q("比べると") + ") ---",
             "Heading " + q("建物の合併などは課税される") + ", body " + q("所有権の登記のある建物の分割・区分・合併は、1個につき1,000円") + "."]
    return finish(body, "Confirm there are exactly three numbered cards followed by exactly one comparison card, that card 1 has the tag 非課税, card 2 has the tag 実務の取扱い, and card 3 has the tag 令別表13の項ホのかっこ書, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "合体による登記等 確かめる6つの順番（章の全体図）", "カードポスター型（俯瞰）", "1080×2700", "登記法編7章_図解1_確かめる6つの順番", "章の冒頭（「この章の論点」の直後）", img1, "00_zentai"),
    (2, "合体による登記等とは何を申請するのか", "説明ポスター型", "1080×1800", "登記法編7章_図解2_合体による登記等とは", "【PF2-1】「中身の整理」の直後", img2, "PF2-1"),
    (3, "合体になる？ならない？（場面で仕分ける）", "早見表型（3列）", "1080×2000", "登記法編7章_図解3_合体になるならない", "【PF2-1】図解2の直後", img3, "PF2-1"),
    (4, "合体前の建物の登記は、どうなっているか（判定の流れ）", "判定の流れ型", "1080×2300", "登記法編7章_図解4_合体前の登記の状態", "【PF2-2】「中身の整理」の直後", img4, "PF2-2"),
    (5, "合体の申請は、誰が？（法49条1項の号）", "早見表型（3列）", "1080×2200", "登記法編7章_図解5_誰が申請するか", "【PF2-3】「中身の整理」の直後", img5, "PF2-3"),
    (6, "1か月の数え始めは、人によって違う", "ステージカード型", "1080×2000", "登記法編7章_図解6_1か月の数え始め", "【PF2-3】図解5の直後", img6, "PF2-3"),
    (7, "合体前の権利は、どうなる？（存続させる権利の仕分け）", "早見表型（3列）", "1080×2100", "登記法編7章_図解7_存続させる権利の仕分け", "【PF2-4】「中身の整理」の直後", img7, "PF2-4"),
    (8, "合体の添付情報（記号で呼び分けて覚える）", "早見表型（2列）", "1080×2400", "登記法編7章_図解8_添付情報の記号", "【PF2-4】図解7の直後", img8, "PF2-4"),
    (9, "合体後の持分は、いつ書く？", "対比カード型", "1080×2100", "登記法編7章_図解9_持分を書くとき", "【PF2-5】「中身の整理」の直後", img9, "PF2-5"),
    (10, "合体の登記等で、要らなくなるもの", "カードポスター型", "1080×2300", "登記法編7章_図解10_要らなくなるもの", "【PF2-6】「中身の整理」の直後", img10, "PF2-6"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PF2-1": ("prompt_infographic_PF2-1.md", "【PF2-1】合体とは何か。どんな場合が合体で、どんな場合は合体ではないのか"),
    "PF2-2": ("prompt_infographic_PF2-2.md", "【PF2-2】合体前の建物にどんな登記があるかで、申請の形はどう変わるか"),
    "PF2-3": ("prompt_infographic_PF2-3.md", "【PF2-3】合体による登記等は誰が、いつから1か月以内に申請するのか"),
    "PF2-4": ("prompt_infographic_PF2-4.md", "【PF2-4】合体前の建物の権利は、合体後の建物にどう引き継がれ、どう消えるのか"),
    "PF2-5": ("prompt_infographic_PF2-5.md", "【PF2-5】合体後の持分は、申請情報や添付情報にどう関わるのか"),
    "PF2-6": ("prompt_infographic_PF2-6.md", "【PF2-6】合体による登記等で、何が不要になるのか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事② 不動産登記法編 第7章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第7章「建物の合体による登記等」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch7.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この章の図解は、分類・早見表が中心のものは、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
               "判定の流れ図（図解4）だけは、はい＝青・いいえ＝赤です。"
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
