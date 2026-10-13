#!/usr/bin/env python3
"""総合記事②不動産登記法編 第1章：図解インフォグラフィック18枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch1/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PA-1.md ／ _PA-2.md … （論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
TWOCARD = "(side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card)"
NOTID = "The two cards have clearly different texts; the texts are NOT identical."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def band(t):
    return "Under the cards, one wide dark navy band with large white text " + q(t) + "."

def table_block(cols, rows, hl):
    """早見表の共通部分。cols=列見出し、rows=行（列数ぶんのタプル）、hl=強調の説明文。"""
    n = len(cols)
    out = ["--- TABLE ---",
           f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {len(rows)} data rows, no merged cells.",
           "Header row (dark navy cells with white text): " + ", ".join(q(c) for c in cols) + ".",
           "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"]
    out += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    out.append(hl)
    return out

def card_list(cards, kind, size_note=""):
    """番号つきカードを縦に並べるポスター用。cards=(見出し, 絵の指示, [項目行], タグ)。"""
    out = []
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        out += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                "Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
               ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return out

def steps_block(steps, side=None):
    n = len(steps)
    out = ["--- STEPS ---",
           f"Layout: {n} step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to {n} in order), one bold heading line, and one or two short body lines."]
    for i, (h, body, hl) in enumerate(steps, 1):
        s = f"STEP {i}" + (" (heading has a pale yellow highlighter marker)" if hl else "") + ": heading " + q(h) + ", " + ("two body lines " if len(body) > 1 else "body ") + " and ".join(q(b) for b in body) + "."
        out.append(s)
    if side:
        out += ["--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---", "Heading " + q(side[0]) + ", body " + q(side[1]) + "."]
    return out

# ============================================================ 図解1：申請の肢を読む順番（全体）
def img1():
    cards = [
        ("何の登記か", "A small registry ledger with a pencil and a stamp, no text on the ledger.",
         ["変更・更正・保存・移転を見分ける", "表題部所有者の記録が決めるのは、保存まで"], "登記の種類"),
        ("誰が申請するか", "Two person pictograms side by side, one drawn with a thin dotted outline behind the other, no text.",
         ["名義人（その相続人）が原則", "代位・代理・保存行為は別に確かめる"], "申請人"),
        ("まとめて申請できるか", "Two document sheets joined by a paper clip, no text on the sheets.",
         ["同一の不動産の変更・更正と分筆・合筆", "規則35条の列挙だけ"], "一の申請情報"),
        ("何を添付するか", "A folder with three document sheets of different sizes, no text on the sheets.",
         ["所有権・住所の証明、承諾、図面", "借地権の証明は必須ではない"], "添付情報"),
        ("いつまでか", "A calendar page with a bracket spanning one month and a caution triangle sign.",
         ["取得・変更の日から1か月以内", "申請がなければ、まず催告"], "申請義務"),
    ]
    body = [lead("1080x2900", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("申請の肢は、この順で読む", "登記の種類から、期限まで", "不動産登記法 申請人・代位・代理・一括申請") + \
           card_list(cards, "poster")
    return finish(body, "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：表題部は何の後継か／表題部所有者が決めるもの
def img2():
    rows = [("表題部の変更の登記・更正の登記", "申請できる人（申請適格者）を決める", "代理人ではなく、申請適格者"),
            ("所有権の保存の登記", "申請できる人（申請適格者）を決める", "法74条1項1号"),
            ("所有権の移転の登記", "決めない", "保存のあとの手続（法32条）")]
    body = [lead("1080x2300", "This is a comparison poster: two cards at the top and a table below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("表題部所有者の記録は何を決める？", "表題部と権利部の前身から整理", "不動産登記法 第32条・第74条") + \
           ["One thin pale-yellow banner under the header with the text " + q("昭和35年の改正で、台帳と登記が一元化された") + ".",
            "--- TWO CARDS " + TWOCARD + " ---",
            "Left card, small tag " + q("表題部") + ", heading " + q("土地台帳・家屋台帳の後継") + ", body " + q("物理的状況を公示する公簿") + ".",
            "Right card, small tag " + q("権利部") + ", heading " + q("不動産登記の後継") + ", body " + q("権利関係を公示する制度") + ", and a small gray note " + q("登記簿は、帳簿そのものの呼び名") + ".",
            NOTID] + \
           table_block(["登記", "表題部所有者の記録は", "ポイント"], rows,
                       "Highlighting: the string " + q("決めない") + " in row 3 has a pale yellow highlighter marker; rows 1 and 2 are plain. Copy each cell exactly as given.") + \
           ["Under the table, one wide dark navy band with large white text " + q("決めるのは、変更・更正・保存まで") + "."]
    return finish(body, "Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 3 data rows, that the left card says 台帳 and the right card says 不動産登記, that only row 3 reads 決めない, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：表題部所有者を直す手続の仕分け
def img3():
    rows = [("売買などで所有者が替わった", "変更の登記はない。保存の登記をしたあと、移転の登記（法32条）"),
            ("持分の割合が後から変わった", "持分の変更の登記という手続はない。同じく保存の登記のあと移転の登記"),
            ("所有者が最初から誤って記録されている", "表題部所有者の更正の登記。申請できるのは真の所有者（法33条1項）"),
            ("持分が最初から誤って記録されている", "持分の更正の登記。申請できるのは表題部所有者である共有者（法33条3項）"),
            ("氏名・名称・住所の変更・更正", "表題部所有者以外は申請できない（法31条）")]
    body = [lead("1080x2100", "This is a reference table poster with two columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("表題部所有者を直す手続は？", "実体が変わったら移転、誤りなら更正", "不動産登記法 第31条〜第33条") + \
           table_block(["場面", "手続と、申請できる人"], rows,
                       "Highlighting: the strings " + q("変更の登記はない") + " in row 1, " + q("という手続はない") + " in row 2, " + q("真の所有者") + " in row 3, and " + q("表題部所有者である共有者") + " in row 4 have a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           ["Under the table, one wide dark navy band with large white text " + q("実体が変わったら移転。最初から誤りなら更正") + "."]
    return finish(body, "Confirm the table has exactly 2 columns and exactly 5 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解4：更正の添付情報の判定の流れ
def img4():
    body = [lead("1080x2400", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("更正の添付情報は何が要る？"), q("加わる者がいるかで分かれる"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第33条・令別表"),
            "--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, RESULT 1. RESULT 2 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The side note card sits at the bottom. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("表題部所有者についての更正の登記"),
            "NODE DIAMOND 1: " + q("新たに表題部所有者として加わる者がいるか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): the first line " + q("加わる者の証明が要る") + " and three body lines " + q("加わる者の所有権を証する情報") + ", " + q("加わる者の住所を証する情報") + ", " + q("外れる者がいれば、その承諾を証する情報") + ".",
            "NODE RESULT 2 (red box): the first line " + q("持分だけを直す更正") + " and two body lines " + q("持分が変わる他の共有者の承諾だけ") + ", " + q("所有権を証する情報は要らない") + ".",
            "--- SIDE NOTE CARD (a wide card with a dashed dark navy outline at the bottom, neutral dark navy text) ---",
            "Heading " + q("承諾が要る相手は、記録から外れる者・持分が変わる共有者だけ") + ", body " + q("承諾を証する情報の代わりに、その者に対抗できる裁判があったことを証する情報でもよい") + ".",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other."]
    return finish(body, "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解5：持分の更正で承諾が要るのは誰か
def img5():
    rows = [("甲", "10分の5", "10分の5", "変わらない：承諾は要らない"),
            ("乙", "10分の3", "10分の2", "減る：承諾が要る"),
            ("丙", "10分の2", "10分の3", "増える（申請する共有者）：承諾は要らない")]
    body = [lead("1080x1700", "This is a reference table poster with four columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("持分の更正、誰の承諾が要る？", "持分が変わる共有者だけ", "不動産登記法 第33条第3項・第4項") + \
           ["A small gray caption above the table: " + q("丙が申請して、乙の持分を10分の2、丙の持分を10分の3に直す") + "."] + \
           table_block(["共有者", "更正前", "更正後", "承諾"], rows,
                       "Highlighting: the string " + q("承諾が要る") + " in row 2 has a pale yellow highlighter marker; the other two rows are plain. Copy each cell exactly as given; the strings " + q("10分の2") + " and " + q("10分の3") + " differ by one digit, so copy each exactly and do not change one into the other.") + \
           ["Under the table, one wide dark navy band with large white text " + q("承諾が要るのは、持分を更正することとなる他の共有者だけ") + ".",
            "Under the band, one small gray note line " + q("承諾があれば、共有者の一人が単独で申請できる") + "."]
    return finish(body, "Confirm the table has exactly 4 columns and exactly 3 data rows, that every cell reads exactly as given, that only row 2 reads 承諾が要る, that the fractions 10分の2 and 10分の3 are copied exactly in rows 2 and 3, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解6：完了通知の通知先
def img6():
    rows = [("申請に基づく、表示に関する登記の完了", "申請人以外の表題部所有者（又は所有権の登記名義人）"),
            ("表題部所有者の更正の登記の完了", "更正前の表題部所有者"),
            ("表題部所有者である共有者の持分の更正の登記の完了", "更正前の表題部所有者"),
            ("職権による表示に関する登記の完了（例：職権による地目の変更）", "表題部所有者")]
    body = [lead("1080x2000", "This is a reference table poster with two columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("完了通知は誰に出す？", "更正のときは更正前の所有者", "不動産登記規則 第183条") + \
           table_block(["登記が完了したのは", "通知を受ける人"], rows,
                       "Highlighting: the string " + q("更正前") + " in rows 2 and 3 has a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           ["Under the table, one wide dark navy band with large white text " + q("通知を受ける人が2人以上いれば、その1人に通知すれば足りる") + ".",
            "Under the band, one small gray note line " + q("申請人には、別に登記完了証で知らせる") + "."]
    return finish(body, "Confirm the table has exactly 2 columns and exactly 4 data rows, that every cell reads exactly as given, that rows 2 and 3 both read 更正前の表題部所有者, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解7：区分建物の新築の判定の流れ
def img7():
    body = [lead("1080x2300", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("区分建物が新築されたとき", "何と併せて申請する？", "不動産登記法 第48条・第52条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. START at the top, then the DIAMOND, then the two result boxes at the bottom, one down-left and one down-right of the diamond, side by side with the same size. All arrows are straight or have at most one right-angle bend and never cross each other. All arrows and labels are dark navy.",
            "NODE START (rounded pill, dark navy): " + q("区分建物が新築されて、一棟の建物になった"),
            "NODE DIAMOND: " + q("接続する建物（区分建物を除く）に、表題登記があるか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy and carry the labels " + q("ない") + " and " + q("ある") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("ない") + " to RESULT 1.",
            "  - Arrow down-right with the label " + q("ある") + " to RESULT 2.",
            "NODE RESULT 1 (pale gray box with a dark navy outline): the first line " + q("他の区分建物の表題登記と併せる") + ", then body lines " + q("所有者が、他の区分建物の所有者に代わって申請できる") + " and a small tag " + q("法48条1項・2項") + ".",
            "NODE RESULT 2 (pale gray box with a dark navy outline): the first line " + q("既存建物の表題部の変更と併せる") + " (the string " + q("表題部の変更") + " has a pale yellow highlighter marker), then body lines " + q("既存建物の登記記録は残る。抹消ではない") + " and a small tag " + q("法48条3項・52条1項") + ".",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other."]
    return finish(body, "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 「ない」 and 「ある」 and never 「はい」 or 「いいえ」, that RESULT 1 is on the left and RESULT 2 is on the right, that no text overflows its box, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解8：誰が誰に代わって、何を申請できるか
def img8():
    cards = [
        ("未登記の建物に接続して新築", "Two small isometric buildings joined together, one with a dashed outline, no text.",
         ["新築した区分建物の所有者が", "他の区分建物の所有者に代わって", "他の区分建物の表題登記を申請できる（法48条2項）"], "新築側が代わって申請"),
        ("登記のある建物に接続して新築", "Two small isometric buildings joined together, one with a ledger card beside it, no text.",
         ["新築区分建物の所有者は、既存建物の変更の登記を代わって申請できる（法48条4項）", "既存建物の名義人は、新築区分建物の表題登記を代わって申請できる（法52条2項）"], "代位は両方向にある"),
        ("全部の原始取得者が、一部を売却", "A small apartment block icon with one door tagged with a key, no text.",
         ["原始取得者は、自分で申請できる（法47条1項）", "代位に限られない"], "代位の形をとるのは転得者"),
        ("区分建物を新築した人が亡くなった", "A small document sheet with a pen, and a faded person pictogram behind it, no text.",
         ["相続人は、被承継人を表題部所有者として申請できる（法47条2項）", "相続人自身を表題部所有者とする申請はできない"], "記録されるのは被承継人"),
    ]
    body = [lead("1080x2500", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. Do NOT render any paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("建物の表題登記、誰が誰に代わる？", "代位は両方向、相続人は被承継人", "不動産登記法 第47条・第48条・第52条") + \
           card_list(cards, "poster")
    return finish(body, "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a paragraph of body text.")

# ============================================================ 図解9：共有の表示登記は一人から単独で
def img9():
    body = [lead("1080x2300", "This is a card poster: three example cards, then two comparison cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("共有の表示登記は、一人から単独で", "保存行為だから代位は要らない", "民法 第252条第5項") + \
           ["--- THREE EXAMPLE CARDS (stacked top to bottom, all the same size, same pale gray fill, dark navy outline, each with a small dark navy tag at its top left and one bold heading line) ---",
            "Example 1: tag " + q("地積の更正の登記") + ", heading " + q("地積が減る更正も、一人から単独で") + ".",
            "Example 2: tag " + q("地目の変更の登記") + ", heading " + q("他の共有者が応じなくても、単独で") + ".",
            "Example 3: tag " + q("区分建物の表題登記") + ", heading " + q("原始取得者の一人から。共有者全員の持分を記録") + ".",
            "--- TWO COMPARISON CARDS " + TWOCARD + " ---",
            "Left card, small tag " + q("保存行為") + ", heading " + q("共有者の一人が、自分の名で申請") + ", body lines " + q("現況をそのまま記録するだけ") + " and " + q("処分や変更に当たらない") + ", with the heading highlighted with a yellow marker.",
            "Right card, small tag " + q("代位") + ", heading " + q("他の共有者に代位して申請") + ", body lines " + q("単独でできる場面では") + " and " + q("出番がない") + ".",
            NOTID,
            band("応じない共有者がいても、代位は要らない"),
            "Under the band, one small gray note line " + q("表示に関する登記を保存行為とする点は、条文に明記がなく解釈による") + "."]
    return finish(body, "Confirm there are exactly three example cards, followed by exactly two comparison cards, that the left comparison card is 共有者の一人が、自分の名で申請 and the right comparison card is 他の共有者に代位して申請, never swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解10：分筆を誰が申請できるか
def img10():
    rows = [("表題部所有者・所有権の登記名義人（その相続人）", "申請できる", "原則（法39条1項・30条）"),
            ("土地の一部の買主が設定した、抵当権者", "代位して申請できる", "担保の目的物（その部分）を特定する必要"),
            ("共有物分割の確定判決を得た共有者", "協力しない共有者に代位して申請できる", "判決正本が代位原因を証する情報"),
            ("土地の一部に地役権を得た、地役権者", "代位して申請できない", "保全の必要性がない"),
            ("遺産分割で、土地を取得する相続人", "申請できる", "遺産分割協議書と分筆後の地積測量図等"),
            ("遺産分割で、どちらも取得しない相続人", "申請できない", "取得する相続人が申請人になる")]
    body = [lead("1080x2400", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("分筆を申請できるのは誰？", "原則は名義人、代位は保全の必要性", "不動産登記法 第39条・第30条") + \
           table_block(["申請する人", "結論", "決め手"], rows,
                       "Highlighting: the cells of column 2 in rows 4 and 6 have a pale yellow highlighter marker over the whole cell text; the cells of column 2 in rows 1, 2, 3 and 5 are plain. The strings " + q("代位して申請できる") + " and " + q("代位して申請できない") + " differ by one character; copy each exactly as given and do not change one into the other.") + \
           ["Under the table, one wide dark navy band with large white text " + q("代位できるかは、保全の必要性があるかで決まる") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that row 2 reads 代位して申請できる and row 4 reads 代位して申請できない (never swapped), and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解11：代理申請の押印・氏名住所・署名・取下げ
def img11():
    cards = [
        ("押印するのは、誰か", "A document sheet with a rubber stamp and a pen held by a person pictogram, no text.",
         ["現に手続をする代理人が記名押印すれば足りる（令16条1項）", "本人（未成年者など）の押印は要らない"], "押印は代理人"),
        ("本人の氏名・住所は、書くか", "A name tag and an address card side by side, no text on them.",
         ["代理人が申請しても、本人の氏名・住所は申請情報の内容（令3条1号）", "成年後見人が代理でも、被後見人の氏名・住所を書く"], "本人の表示は必ず書く"),
        ("署名で足りるか", "A hand-signed paper next to a stamped paper, no text.",
         ["署名で足りる場合がある（規則47条）", "ただし、合筆の登記・合体による登記等・建物の合併の登記は署名では足りない（同条3号イ（6））"], "合筆・合体・合併は記名押印"),
        ("補正のための取下げ", "A document sheet being taken back by a hand, no text.",
         ["特別の委任は要らない", "通常の代理権の範囲（条文に明記はなく、実務上の整理）"], "取下げに特別の委任は不要"),
    ]
    body = [lead("1080x2700", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two short item lines, and one short conclusion tag. Do NOT render any paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("代理で申請するとき", "押印は代理人、本人の表示は必須", "不動産登記令 第16条・第3条") + \
           card_list(cards, "poster")
    return finish(body, "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a paragraph of body text.")

# ============================================================ 図解12：申請情報に書くもの・書かないもの
def img12():
    rows = [("申請人が法人のとき", "法人の名称・住所と、代表者の氏名（令3条2号）", "代表者の住所"),
            ("表題部所有者の氏名・住所の変更・更正", "変更後・更正後の氏名や住所", "変更前・更正前の氏名"),
            ("地積の変更と分筆を、一の申請情報で", "地積の変更の登記についてだけ、登記原因とその日付", "分筆の登記の原因と日付")]
    body = [lead("1080x1900", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("申請情報に、何を書く？", "書くものと、書かないもの", "不動産登記令 第3条・別表") + \
           table_block(["場面", "申請情報に書く", "書かない"], rows,
                       "Highlighting: the strings " + q("代表者の住所") + " in row 1, " + q("変更前・更正前の氏名") + " in row 2, and " + q("分筆の登記の原因と日付") + " in row 3 have a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           ["Under the table, one wide dark navy band with large white text " + q("分筆は形成的な登記。原因の日付は書かない") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解13：一の申請情報にまとめられる組合せ
def img13():
    rows = [("同じ土地の地積の更正と、更正後の分筆", "できる", "規則35条7号"),
            ("表題部所有者の住所・氏名の変更と、合筆", "できる", "規則35条7号"),
            ("土地の一部の分筆と、他の土地への合筆", "できる", "規則35条1号"),
            ("甲建物の附属建物の分割と、乙建物の附属建物とする合併", "できる", "規則35条2号"),
            ("区分建物の附属建物の分割と、接続する区分建物への合併", "接続していればできる", "規則35条3号"),
            ("甲建物の滅失と、乙建物の表題登記", "できない", "別の不動産で、目的も違う")]
    body = [lead("1080x2500", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("一の申請情報で、まとめられる？", "規則35条の組合せだけ", "不動産登記規則 第35条") + \
           table_block(["登記の組合せ", "まとめて申請", "根拠"], rows,
                       "Highlighting: the string " + q("できない") + " in row 6 and the string " + q("接続していれば") + " in row 5 have a pale yellow highlighter marker; the other cells in column 2 are plain. The strings " + q("できる") + " and " + q("できない") + " differ by one character; copy each exactly as given and do not change one into the other.") + \
           ["Under the table, two wide bands stacked: the first band, dark navy with large white text, " + q("原則は、目的と登記原因・日付が同一（令4条ただし書）") + "; the second band, pale gray with dark navy text, " + q("例外は、規則35条の限定列挙") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only row 6 reads できない and row 5 reads 接続していればできる, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解14：添付情報（何を添え、何は要らないか）
def img14():
    cards = [
        ("建物の表題登記", "A folder with a floor plan sheet, a certificate sheet and an address card, no text.",
         ["建物図面・各階平面図", "所有権を証する情報", "住所を証する情報"], "令別表の建物の表題登記"),
        ("他人の土地に建てた建物の表題登記", "A small house on a plot, with a dashed outline around a lease contract sheet, no text.",
         ["借地権を証する情報は、必須ではない", "敷地所有者の証明書も、所有権を証する情報に使える"], "借地権の証明は要らない"),
        ("建物の床面積の変更", "A floor plan sheet with an added room drawn with a dashed outline, no text.",
         ["変更後の建物図面・各階平面図", "増えた部分の所有権を証する情報", "一部取壊しの後に増築して一の申請なら、全体で減っても必要（実務上の取扱い）"], "増えた部分の証明が要る"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. Do NOT render any paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("建物の添付情報は？", "何を添え、何は要らないか", "不動産登記令 別表") + \
           card_list(cards, "poster")
    return finish(body, "Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a paragraph of body text.")

# ============================================================ 図解15：電子申請の添付情報の置き換え
def img15():
    body = [lead("1080x2100", "This is a comparison poster with two side-by-side cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("電子申請の添付情報、置き換えは？", "対象になるもの・ならないもの", "不動産登記令 第13条") + \
           ["--- TWO COLUMN CARDS " + TWOCARD + " ---",
            "Left card: small tag " + q("令13条1項") + ", heading " + q("置き換えられる") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("書面の添付情報を、電磁的記録にする") + ", " + q("作成者の電子署名を付ける") + ", " + q("登記官が定めた期間内に、書面を提示する") + ".",
            "Right card: small tag " + q("対象外") + ", heading " + q("置き換えられない") + " (the string " + q("置き換えられない") + " has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("申請人・代表者・代理人が作成した情報") + ", " + q("調査士が作る調査報告情報（代理人の作成）") + ", " + q("図面（地積測量図・建物図面など）") + ", " + q("地役権設定の範囲を証する、地役権者作成の情報") + ".",
            NOTID,
            band("調査士報告方式でも、地役権者作成の書面は書面の提示が必要")]
    return finish(body, "Confirm there are exactly two cards, that the left card has exactly three item lines and the right card has exactly four item lines, that the two headings 置き換えられる and 置き換えられない are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解16：申請義務と催告
def img16():
    body = [lead("1080x2500", "This is a vertical step poster with four step cards and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("申請義務は、いつ生じる？", "申請がなければ、まず催告", "不動産登記法 第36条・第51条") + \
           steps_block([
               ("義務が生じる", ["表題登記のない土地の所有権を取得した（法36条）", "建物の表題部の登記事項に変更があった（法51条1項）"], False),
               ("取得・変更の日から1か月以内に申請", ["義務を負うのは、取得した者・名義人", "売買の買主にも、義務は及ぶ"], True),
               ("申請がないとき", ["登記官は、見つけても直ちに職権で登記しない（表示の登記は職権でもできる。法28条）", "まず、申請義務のある者に催告する（準則63条1項）"], True),
               ("正当な理由なく怠ると", ["10万円以下の過料（法164条1項）"], False)],
               ("たとえば、敷地の分筆で建物の所在の地番が変わったとき", "建物の所在の変更の登記を、1か月以内に申請する義務を負う（法51条1項）"))
    return finish(body, "Confirm there are exactly four step cards numbered 1 to 4 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解17：本人確認調査の判定の流れ
def img17():
    body = [lead("1080x2600", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("本人確認調査は、必ずする？"), q("相当な理由があるときだけ"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第24条第1項"),
            "--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, each with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("登記の申請があった"),
            "NODE DIAMOND 1: " + q("申請を却下すべき場合か？") + " The text is placed inside the diamond on 2 lines.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("調査せず、却下する") + " on the first line and " + q("調査の対象にならない") + " on the second line.",
            "NODE DIAMOND 2: " + q("申請人となるべき者以外が申請していると疑うに足りる相当な理由があるか？") + " The text is placed inside the diamond on 4 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box): " + q("本人確認調査をしなければならない") + " on the first two lines and " + q("申請権限の有無を調査する（法24条1項）") + " on the next two lines.",
            "NODE RESULT 3 (red box): " + q("調査の義務は生じない") + " on the first line and " + q("申請の度に調べるのではない") + " on the second line.",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another."]
    return finish(body, "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解18：相当な理由の例と不正登記防止申出
def img18():
    body = [lead("1080x2400", "This is a comparison poster with two side-by-side cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("相当な理由と、不正登記防止申出", "列挙を確かめ、申出は出頭で", "不動産登記事務取扱手続準則 第33条・第35条") + \
           ["--- TWO COLUMN CARDS " + TWOCARD + " ---",
            "Left card: small tag " + q("準則33条1項") + ", heading " + q("相当な理由の例") + ", and exactly five short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("捜査機関等から、不正事件のおそれの通報") + ", " + q("不正登記防止申出から3月以内の申請") + ", " + q("同一の申請人に係る、他の不正事件の発覚") + ", " + q("前の住所地への通知後の、異議の申出") + ", " + q("登記識別情報の誤りによる補正等が複数回") + ".",
            "Right card: small tag " + q("準則35条1項") + ", heading " + q("不正登記防止申出") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("登記所に出頭してする") + ", " + q("申出書の送付だけではできない") + ", " + q("出頭できないやむを得ない事情があれば、委任による代理人でもよい") + ".",
            "At the bottom of the left card, one pale-yellow banner " + q("申請前3月以内の住所変更の登記は、この列挙にない") + ".",
            NOTID,
            band("住所変更が3月以内でも、それだけでは調査義務は生じない")]
    return finish(body, "Confirm there are exactly two cards, that the left card has exactly five item lines and the right card has exactly three item lines, that the pale-yellow banner is at the bottom of the left card, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "申請の肢は、この順で読む（5つの確認順）", "カードポスター型（俯瞰）", "1080×2900", "不登法編1_図解1_申請の肢を読む順", "章の冒頭（「この記事の使い方」の直後）", img1, "00_zentai"),
    (2, "表題部所有者の記録は何を決める？（表題部・権利部の前身）", "対比カード＋早見表型", "1080×2300", "不登法編1_図解2_表題部所有者の記録", "【PA-1】「中身の整理」の直後", img2, "PA-1"),
    (3, "表題部所有者を直す手続は？（変更・更正・保存・移転の仕分け）", "早見表型（2列）", "1080×2100", "不登法編1_図解3_表題部所有者を直す手続", "【PA-2】「中身の整理」の直後", img3, "PA-2"),
    (4, "更正の添付情報は何が要る？（加わる者がいるか）", "フローチャート型", "1080×2400", "不登法編1_図解4_更正の添付情報", "【PA-3】「中身の整理」の直後", img4, "PA-3"),
    (5, "持分の更正、誰の承諾が要る？", "早見表型（4列）", "1080×1700", "不登法編1_図解5_持分の更正の承諾", "【PA-3】「たとえば」の直後", img5, "PA-3"),
    (6, "完了通知は誰に出す？", "早見表型（2列）", "1080×2000", "不登法編1_図解6_完了通知の通知先", "【PA-4】「中身の整理」の直後", img6, "PA-4"),
    (7, "区分建物が新築されたとき、何と併せて申請する？", "フローチャート型（中立の分岐）", "1080×2300", "不登法編1_図解7_区分建物の新築", "【PA-5】「中身の整理」の直後", img7, "PA-5"),
    (8, "建物の表題登記、誰が誰に代わる？", "カードポスター型（4枚）", "1080×2500", "不登法編1_図解8_誰が誰に代わるか", "【PA-5】図解7の直後（「たとえば」の前）", img8, "PA-5"),
    (9, "共有の表示登記は、一人から単独で", "カードポスター型＋対比", "1080×2300", "不登法編1_図解9_共有の表示登記", "【PA-6】「中身の整理」の直後", img9, "PA-6"),
    (10, "分筆を申請できるのは誰？", "早見表型（3列）", "1080×2400", "不登法編1_図解10_分筆の申請人", "【PA-7】「中身の整理」の直後", img10, "PA-7"),
    (11, "代理で申請するとき（押印・本人の表示・署名・取下げ）", "カードポスター型（4枚）", "1080×2700", "不登法編1_図解11_代理で申請するとき", "【PA-8】「中身の整理」の直後", img11, "PA-8"),
    (12, "申請情報に、何を書く？（書くものと書かないもの）", "早見表型（3列）", "1080×1900", "不登法編1_図解12_申請情報の記載事項", "【PA-9】「中身の整理」の直後", img12, "PA-9"),
    (13, "一の申請情報で、まとめられる？（規則35条の組合せ）", "早見表型（3列）", "1080×2500", "不登法編1_図解13_一の申請情報", "【PA-10】「中身の整理」の直後", img13, "PA-10"),
    (14, "建物の添付情報は？（何を添え、何は要らないか）", "カードポスター型（3枚）", "1080×2300", "不登法編1_図解14_建物の添付情報", "【PA-11】「中身の整理」の直後", img14, "PA-11"),
    (15, "電子申請の添付情報、置き換えは？", "対比カード型（2列）", "1080×2100", "不登法編1_図解15_添付情報の置き換え", "【PA-11】図解14の直後", img15, "PA-11"),
    (16, "申請義務は、いつ生じる？（申請がなければ、まず催告）", "ステップ型", "1080×2500", "不登法編1_図解16_申請義務と催告", "【PA-12】「中身の整理」の直後", img16, "PA-12"),
    (17, "本人確認調査は、必ずする？", "フローチャート型", "1080×2600", "不登法編1_図解17_本人確認調査", "【PA-13】「中身の整理」の直後", img17, "PA-13"),
    (18, "相当な理由と、不正登記防止申出", "対比カード型（2列）", "1080×2400", "不登法編1_図解18_相当な理由と申出", "【PA-13】図解17の直後", img18, "PA-13"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PA-1": ("prompt_infographic_PA-1.md", "【PA-1】表題部所有者の記録は何の「前身」で、何を決める役割か"),
    "PA-2": ("prompt_infographic_PA-2.md", "【PA-2】表題部所有者を「変更」できるのか、誰が「更正」を申請できるのか"),
    "PA-3": ("prompt_infographic_PA-3.md", "【PA-3】表題部所有者の更正に、承諾情報と所有権証明情報のどちらが要るか"),
    "PA-4": ("prompt_infographic_PA-4.md", "【PA-4】表題部所有者の更正が完了したとき、完了通知は誰に出すのか"),
    "PA-5": ("prompt_infographic_PA-5.md", "【PA-5】建物の表題登記は誰が、どの登記と併せて、誰に代わって申請するのか"),
    "PA-6": ("prompt_infographic_PA-6.md", "【PA-6】共有の不動産の表示登記は、共有者の一人から単独で申請できるのか"),
    "PA-7": ("prompt_infographic_PA-7.md", "【PA-7】分筆の登記を、誰が申請でき、誰が代位して申請できるのか"),
    "PA-8": ("prompt_infographic_PA-8.md", "【PA-8】代理人が申請するとき、誰が押印し、本人の何を書き、取下げに特別の委任は要るか"),
    "PA-9": ("prompt_infographic_PA-9.md", "【PA-9】申請情報の記載事項：法人の代表者、更正前の氏名、登記原因とその日付"),
    "PA-10": ("prompt_infographic_PA-10.md", "【PA-10】どの登記と、どの登記を、一の申請情報でまとめて申請できるのか"),
    "PA-11": ("prompt_infographic_PA-11.md", "【PA-11】添付情報：何を添え、何は要らず、どの方式なら置き換えられるか"),
    "PA-12": ("prompt_infographic_PA-12.md", "【PA-12】申請義務はいつ生じ、申請のないときに登記官はどうするのか"),
    "PA-13": ("prompt_infographic_PA-13.md", "【PA-13】登記官の本人確認調査は、いつ義務になり、不正登記防止申出はどうするのか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第1章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "分類・早見表・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（フローチャート）の「はい」は青、「いいえ」は赤、中立の分岐（ある／ない）は濃紺です。"
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
