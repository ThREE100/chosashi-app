#!/usr/bin/env python3
"""総合記事②不動産登記法編 第5章：図解インフォグラフィック19枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PE-1.md 〜 _PE-13.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
SAME = "The cards and cells have clearly different texts; the texts are NOT identical, so copy each character exactly as given."
FIT = "Cell and card text may wrap onto two or three lines: make every row and card tall enough that all of its text fits fully inside it, at least 24 px high, and nothing is cut off or overflows."
NOEND = "Draw no check mark and no cross mark anywhere in this image."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def table(size, kind, t1, t2, sub, cols, rows, hl, band, extra_pre=None, extra_post=None, fin=""):
    """3列以上の表のポスター。rows は各行が len(cols) 個のタプル。"""
    n, m = len(cols), len(rows)
    body = [lead(size, "This is a reference table poster with " + str(n) + " columns."), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    if extra_pre: body += extra_pre
    body += ["--- TABLE ---",
             f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {m} data rows, no merged cells. " + FIT,
             "Header row (dark navy cells with white text): " + ", ".join(q(c) for c in cols) + ".",
             "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"]
    body += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    body += ["Highlighting: " + hl + " Copy each cell exactly as given."]
    if extra_post: body += extra_post
    if band: body += ["At the bottom of the poster, below everything else, one wide dark navy band with large white text " + q(band) + "."]
    return finish(body, f"Confirm the table has exactly {n} columns and exactly {m} data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere. " + fin)

def two_cards(size, kind, t1, t2, sub, left, right, band, hl, fin=""):
    """左右2枚の比較カード。left/right = (タグ, 見出し, [項目...])。"""
    def card(side, c, hl_head=False):
        tag, head, items = c
        s = f"{side} card: small tag {q(tag)}, heading {q(head)}, and exactly {len(items)} short item lines, each with a small dark navy dot at its left end (NO number on the dots): " + ", ".join(q(x) for x in items) + "."
        return s
    body = [lead(size, "This is a comparison poster with two side-by-side cards."), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub) + \
           ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            card("Left", left), card("Right", right), "Highlighting: " + hl, FIT, "The two cards have clearly different texts; the texts are NOT identical."]
    if band: body += ["Under the two cards, one wide dark navy band with large white text " + q(band) + "."]
    return finish(body, f"Confirm there are exactly two cards, that the left card has exactly {len(left[2])} item lines and the right card has exactly {len(right[2])} item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere. " + fin)

# ============================================================ 図解1：全体
def img1():
    cards = [
        ("建物の数え方", "Two small houses joined by a dotted outline next to a single long building divided into sections, no text.",
         ["効用上一体の数棟は、一個にできる", "一棟の中の区分は、原則は別々"], "一個か、別々か"),
        ("表題部に書くこと", "A registry ledger page with a header block and a body block, no text.",
         ["所在・種類・構造・床面積", "区分建物は、一棟と専有部分で分ける"], "何を、どこに"),
        ("変わったとき", "A small house with a new extension and a blank form sheet, no text.",
         ["登記事項が変われば、変更の登記", "建て直し（再築）は、滅失と新築"], "変更か、滅失か"),
        ("分ける・つなぐ", "Two small buildings being joined by a short connector, no text.",
         ["申請できるのは、表題部所有者・登記名義人", "合併後の図面を添える"], "誰が、何を添える"),
        ("なくなったとき", "A small house icon with a crossed-out outline and a calendar page, no text.",
         ["滅失の登記は、滅失の日から1か月以内", "効用を失ったときが、滅失"], "誰が、いつ"),
        ("図面", "A blank site plan sheet and a blank floor plan sheet with a ruler, no text.",
         ["位置・形状・床面積が変わる登記で必要", "種類の変更などでは不要"], "要るか、要らないか"),
    ]
    body = [lead("1080x2900", "This is a quick-reference poster with six numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("建物の登記を、順に確かめる", "個数から図面まで、6つの見方", "建物の認定・床面積・建物図面・表題部の変更と滅失")
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 6 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (two short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, "Confirm the number of cards equals 6 exactly, numbered 1 to 6 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：登記記録の単位と区分
def img2():
    body = [lead("1080x2000", "This is a structure poster: three unit cards at the top and a block diagram below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登記記録は、何ごとに作る？", "表題部と権利部に分ける", "不動産登記法 第2条・第12条") + \
           ["--- UNIT CARDS (three cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card; a small dark navy tag " + q("登記記録の単位") + " above the row) ---",
            "Card 1: heading " + q("土地") + ", body " + q("一筆ごと") + ".",
            "Card 2: heading " + q("建物") + ", body " + q("一個の建物ごと") + ".",
            "Card 3: heading " + q("区分建物") + ", body " + q("専有部分ごと") + " and a smaller line " + q("専有部分が、一個の建物") + "; the string " + q("専有部分ごと") + " has a pale yellow highlighter marker.",
            "--- STRUCTURE DIAGRAM (below the cards; a small dark navy tag " + q("一つの登記記録の中身") + " above it) ---",
            "A block diagram with plain straight connecting lines and no arrowheads: at the top one wide dark navy box with white text " + q("登記記録") + "; two lines run down from it to two boxes of the same size side by side.",
            "Left box (pale gray fill, dark navy outline): heading " + q("表題部") + " and a small line " + q("表示に関する登記") + ".",
            "Right box (pale gray fill, dark navy outline): heading " + q("権利部") + " and a small line " + q("権利に関する登記") + ".",
            "Under the right box, two lines run down to two smaller boxes of the same size side by side, with a small bracket label " + q("権利部の中の区分") + " above them: left small box " + q("甲区") + " with the small line " + q("所有権") + ", right small box " + q("乙区") + " with the small line " + q("所有権以外") + ".",
            "Under the diagram, one wide card with a dashed dark navy outline: heading " + q("登記事項") + ", body " + q("登記記録として登記すべき事項のこと") + ".",
            SAME,
            "Under everything, one wide dark navy band with large white text " + q("甲区・乙区は、表題部と権利部の区分ではない") + "."]
    return finish(body, "Confirm there are exactly three unit cards and one block diagram with exactly five boxes (登記記録, 表題部, 権利部, 甲区, 乙区), that 甲区 and 乙区 sit under 権利部 and not under 表題部, that no arrowheads are drawn, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：建物の個数の判定の流れ
def img3():
    body = [lead("1080x2500", "This is a flowchart poster (判定の流れ) made of two sections."), TEXTREQ, BGREQ, COLOR] + \
           header("一個の建物にできる？", "数棟か、一棟の中かで見分ける", "不動産登記事務取扱手続準則 第78条") + \
           ["--- FLOWCHART ---",
            "Layout: two section panels stacked top to bottom, both the same size, each with a dashed dark navy outline and a small dark navy tag at its top left. In each panel there is ONE diamond placed at the left-center; the BLUE 「はい」 arrow goes straight down from the diamond to a blue result box directly below it; the RED 「いいえ」 arrow goes right from the diamond to a red result box on the same row, with at least 60 px of empty space between the diamond and the red box so that the arrow label stays visible. Arrows never cross.",
            "A banner at the very top, below the header, in dark navy with white text: " + q("まず、数棟か、一棟の中の区分かを見分ける") + ".",
            "SECTION 1 (tag " + q("数棟の建物") + "):",
            "NODE DIAMOND 1: " + q("効用上一体として利用される状態か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down with the BLUE label " + q("はい") + " to RESULT 1.",
            "  - Arrow right with the RED label " + q("いいえ") + " to RESULT 2.",
            "NODE RESULT 1 (blue box): " + q("所有者の意思に反しない限り、一個の建物") + " on the first two lines and the small tag " + q("準則78条1項") + ".",
            "NODE RESULT 2 (red box): " + q("別々の建物") + " on the first line and " + q("例：借主が別々の居宅の三棟") + " on the second line.",
            "SECTION 2 (tag " + q("一棟の建物の中の区分") + "):",
            "NODE DIAMOND 2: " + q("所有者が同一か？") + " The text is placed inside the diamond on 2 lines.",
            "  - Arrow down with the BLUE label " + q("はい") + " to RESULT 3.",
            "  - Arrow right with the RED label " + q("いいえ") + " to RESULT 4.",
            "NODE RESULT 3 (blue box): " + q("一棟の全部（離れていてもよい）又は隣接する数個の部分を、一個にできる") + " on three lines, the small line " + q("所有者の意思に反しない限り") + ", and the small tag " + q("準則78条2項ただし書") + ".",
            "NODE RESULT 4 (red box): " + q("各部分が、別々の一個の建物") + " on two lines and the small tag " + q("同項本文") + ".",
            "--- SIDE NOTE CARD (below the two sections, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("数棟を附属建物として一個にするには") + ", body " + q("主従の関係が前提（法2条23号）") + ".",
            "Counts: 2 diamonds, 4 result boxes, 4 distinct paths. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue boxes and the two red boxes have different texts; do not copy one into another."]
    return finish(body, "Confirm there are exactly 2 diamonds and 4 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 3 are blue and RESULT 2 and RESULT 4 are red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解4：新築の附属建物と建物の合併
def img4():
    return two_cards("1080x1800", "", "抵当権があると、できない？", "新築の附属建物と、合併は別", "不動産登記法 第56条",
                     ("法56条5号は働かない", "新築した建物を、附属建物にする",
                      ["主である建物の表題部の変更の登記で足りる", "主である建物に抵当権の登記があっても、妨げられない"]),
                     ("合併の制限がある", "既登記の建物どうしを、一つにする",
                      ["表題登記がある建物どうしを、一つにする", "権利に関する登記がある建物の合併を制限（法56条5号）"]),
                     "抵当権の制限が関係するのは、右の合併のほう",
                     "the string " + q("表題部の変更の登記で足りる") + " in the left card and the string " + q("合併を制限") + " in the right card have a pale yellow highlighter marker.",
                     "")

# ============================================================ 図解5：種類・構造の決め方
def img5():
    rows = [
        ("種類", "建物の主な用途", "用途が二以上なら、二以上の用途を連記する（規則113条）"),
        ("構造", "主な部分の構成材料・屋根の種類・階数", "床面積に算入しない部分の屋根の種類は、考えなくてよい"),
        ("地盤面から床上げされた平家建", "高床式平家建と表示する", "規則にも準則にも文言はなく、先例による取扱い"),
        ("区分建物の種類", "専有部分の事項（法44条1項3号）", "一棟の建物の表題部には、載らない"),
        ("区分建物の一棟の建物", "所在・構造及び床面積・名称", "法44条1項1号・7号・8号"),
    ]
    return table("1080x2300", "", "種類と構造は、何で決める？", "用途・材料・屋根・階数", "不動産登記規則 第113条・第114条",
                 ("項目", "決め方", "気をつける点"), rows,
                 "the string " + q("高床式平家建と表示する") + " of row 3 and the string " + q("専有部分の事項（法44条1項3号）") + " of row 4 have a pale yellow highlighter marker.",
                 "一棟の表題部に、種類は載らない")

# ============================================================ 図解6：床面積の基準線と記録のしかた
def img6():
    rows = [
        ("区分建物でない建物", "壁その他の区画の中心線（壁芯）", "規則115条"),
        ("区分建物の専有部分", "壁その他の区画の内側線（内法）", "規則115条（区分建物にあっては）"),
        ("区分建物が属する一棟の建物", "壁その他の区画の中心線（壁芯）", "内側線とするのは専有部分だけ"),
    ]
    post = ["--- RECORD CARD (below the table, a wide card with a dashed dark navy outline and a small dark navy tag " + q("記録のしかた") + ") ---",
            "Heading " + q("床面積の記録") + ", and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            ", ".join(q(x) for x in ["1平方メートルの100分の1未満は、切り捨てる（規則115条）", "平家建以外は、各階ごとに記録する（合計は不要）", "地階は、地上階の次に記録する", "平方メートル未満がなくても、00と記録する"]) + "."]
    return table("1080x2400", "", "床面積は、どの線で測る？", "専有部分だけが内法", "不動産登記規則 第115条・準則 第91条",
                 ("建物の区分", "床面積を測る線", "根拠・注意"), rows,
                 "the string " + q("壁その他の区画の内側線（内法）") + " of row 2 has a pale yellow highlighter marker; the other two cells of column 2 are plain.",
                 "専有部分は内法、一棟は壁芯", extra_post=post,
                 fin="Confirm that the record card has exactly four item lines.")

# ============================================================ 図解7：算入・不算入
def img7():
    body = [lead("1080x2500", "This is a poster with one small flowchart (判定の流れ) and two side note cards."), TEXTREQ, BGREQ, COLOR] + \
           header("床面積に算入する？ しない？", "低い天井・塔屋・観覧席", "不動産登記事務取扱手続準則 第82条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. START at the top, then DIAMOND 1. The BLUE 「はい」 arrow goes down to a blue result box; the RED 「いいえ」 arrow goes right to a red result box on the same row, with at least 60 px of empty space between the diamond and the red box so that the arrow label stays visible.",
            "NODE START (rounded pill, dark navy): " + q("天井の高さ1.5メートル未満の部分がある"),
            "NODE DIAMOND 1: " + q("地階・屋階の階全体が低いか？") + " The text is placed inside the diamond on 2 lines.",
            "  - Arrow down with the BLUE label " + q("はい") + " to RESULT 1.",
            "  - Arrow right with the RED label " + q("いいえ") + " to RESULT 2.",
            "NODE RESULT 1 (blue box): " + q("その階（特殊階）全体を、床面積に算入しない") + " on three lines and the small tag " + q("準則82条1号") + ".",
            "NODE RESULT 2 (red box): " + q("一室の一部が低いだけなら、その部分も一室の面積に算入する") + " on three lines and the small tag " + q("同号ただし書") + ".",
            "--- SIDE NOTE CARDS (two wide cards stacked below the flowchart, each with a dashed dark navy outline and a small dark navy tag at its top left) ---",
            "Card A, tag " + q("塔屋（屋上の階段室・機械室など）") + ", heading " + q("一部でも事務所・倉庫に使うと") + ", two body lines " + q("使っていない部分も含め、塔屋全体を") + " and " + q("床面積に算入する") + ", and a small gray tag " + q("条文にない取扱い") + ".",
            "Card B, tag " + q("観覧席") + ", heading " + q("野球場・競馬場などの観覧席") + ", body line " + q("屋根の設備のある部分の面積を、床面積とする") + ", and a small gray tag " + q("準則82条3号") + ".",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 side note cards. The diamond has exactly two exits, and no arrow leaves a result box."]
    return finish(body, "Confirm there is exactly 1 start node, 1 diamond, 2 result boxes and 2 side note cards, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解8：所在
def img8():
    rows = [
        ("二筆以上の土地にまたがる", "床面積の多い部分（附属建物があれば主である建物）の地番を先に書く", "準則88条2項"),
        ("地下車庫の附属建物が、別の地番にある", "その地番を、所在に後ろから記録する", "直接定めた条文はなく、実務の取扱い"),
        ("増築で、隣の土地にまたがった", "地番を所在に加える、表題部の変更の登記ができる", "変更の登記"),
        ("仮換地が指定された土地に新築", "現に登記記録がある土地（底地）の地番。予定地番の併記は任意", "実務の取扱い"),
        ("区分建物の非区分の附属建物", "専有部分に所在欄がないので、構造欄に所在を記録する", "規則別表三に明記はなく、実務の取扱い"),
    ]
    return table("1080x2400", "", "建物の所在は、どう書く？", "またがり・仮換地・附属建物", "不動産登記法 第44条第1項・準則 第88条",
                 ("場面", "所在の書き方", "根拠など"), rows,
                 "the string " + q("床面積の多い部分") + " of row 1 and the string " + q("構造欄に所在を記録する") + " of row 5 have a pale yellow highlighter marker.",
                 "所在は、現に建物がある土地の地番")

# ============================================================ 図解9：附属建物の表示（判定の流れ）
def img9():
    body = [lead("1080x2600", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("附属建物の表示は、何を書く？", "区分建物かどうかで分かれる", "不動産登記法 第44条第1項第5号") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two blue result boxes at the bottom sit one to the left and one to the right of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("主である建物に附属建物がある"),
            "NODE DIAMOND 1: " + q("附属建物は、区分建物か？") + " The text is placed inside the diamond on 2 lines.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("所在・種類・構造・床面積を書く") + " on two lines.",
            "NODE DIAMOND 2: " + q("主である建物と同じ一棟に属するか？") + " The text is placed inside the diamond on 3 lines. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("同じ一棟") + " and " + q("別の一棟") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("同じ一棟") + " to RESULT 2.",
            "  - Arrow down-right with the label " + q("別の一棟") + " to RESULT 3.",
            "NODE RESULT 2 (blue box): " + q("附属建物自体の種類・構造・床面積を書く") + " on three lines, and the small line " + q("一棟の所在・構造・床面積は、記録を要しない（準則89条）") + ".",
            "NODE RESULT 3 (blue box): " + q("附属建物自体の表示に加え、その一棟の所在地番も申請情報に書く") + " on four lines.",
            "--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("家屋番号は、一個の建物に一つ") + ", body " + q("附属建物には、別の家屋番号は付かない（管轄登記所が違っても同じ）") + " and a small gray tag " + q("法45条") + ".",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts; do not copy one into the other."]
    return finish(body, "Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 1 side note card, that DIAMOND 1 shows a blue 「はい」 and a red 「いいえ」, that DIAMOND 2 shows only the two navy labels 「同じ一棟」 and 「別の一棟」, that RESULT 1 is red and RESULT 2 and RESULT 3 are blue, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解10：保存登記の錯誤抹消
def img10():
    return two_cards("1080x1900", "", "保存登記が錯誤で消えたら", "登記記録は閉鎖される？", "表題部所有者の登記と所有権の保存の登記",
                     ("表題部所有者本人がした", "本人がした保存登記が抹消されたとき",
                      ["登記記録は、全部閉鎖される", "建物が現にあるので、改めて表題登記をする", "表題登記は、真の所有者の申請又は職権で"]),
                     ("相続人などがした", "承継人などがした保存登記が抹消されたとき",
                      ["相続人その他の一般承継人がした場合", "区分建物の所有権を取得した者がした場合", "表題部所有者の記録が復活し、閉鎖されない"]),
                     "どちらも、先例による取扱い",
                     "the string " + q("登記記録は、全部閉鎖される") + " in the left card and the string " + q("閉鎖されない") + " in the right card have a pale yellow highlighter marker.",
                     "")

# ============================================================ 図解11：転得者と敷地権の日付
def img11():
    body = [lead("1080x1900", "This is a vertical poster with two wide cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("表題登記まわりの特殊場面", "転得者の代位と敷地権の日付", "不動産登記法 第47条・不動産登記規則 第118条") + \
           ["--- TWO WIDE CARDS (stacked top to bottom, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card, each with a small dark navy tag at its top left) ---",
            "Card 1: tag " + q("区分建物の転得者") + ", heading " + q("原始取得者が申請しないとき") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("転得者には、表題登記の申請義務がない") + ", " + q("転得者が、原始取得者に代位して申請できる") + ", " + q("原始取得者を表題部所有者とする表題登記（民法423条）") + ".",
            "Card 2: tag " + q("敷地権の登記原因の日付") + ", heading " + q("新築後に敷地利用権を取得したとき") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("敷地権を取得した日（所有権の登記を備えた日と整理）") + ", " + q("表題登記の申請日ではない") + ", " + q("日付の決め方を定めた条文はなく、実務の取扱い") + ".",
            "Highlighting: the string " + q("代位して申請できる") + " in card 1 and the string " + q("申請日ではない") + " in card 2 have a pale yellow highlighter marker.",
            FIT, "The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("転得者は代位、日付は取得した日") + "."]
    return finish(body, "Confirm there are exactly two cards with exactly three item lines each, that the two tags are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解12：変更の登記が要るか
def img12():
    body = [lead("1080x2700", "This is a flowchart poster (判定の流れ) with two side note cards."), TEXTREQ, BGREQ, COLOR] + \
           header("変更の登記は、要る？ 要らない？", "登記事項が変わったかで見る", "不動産登記法 第51条第1項") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The final blue result box at the bottom sits below DIAMOND 2 on the center line. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("建物に変化があった"),
            "NODE DIAMOND 1: " + q("表題部の登記事項が変わったか？") + " The text is placed inside the diamond on 2 lines, with a smaller line under it " + q("（家屋番号と共用部分である旨を除く）") + ".",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("変更の登記は要らない") + " on the first line and " + q("外壁材の張替え・屋根材の変更（屋根の種類が同じ）") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("既存の建物を全部取り壊して、建て直したか？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow down to RESULT 3 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (red box): " + q("変更の日から1か月以内に、変更の登記を申請する") + " on three lines and the small tag " + q("法51条1項") + ".",
            "NODE RESULT 3 (blue box): " + q("滅失と新築として扱う") + " on the first line and " + q("表示を新しい建物に変える変更の登記はできない（準則83条）") + " on the next two lines.",
            "--- SIDE NOTE CARDS (two wide cards stacked below the flowchart, each with a dashed dark navy outline and a small dark navy tag at its top left) ---",
            "Card A, tag " + q("非区分建物に接続して区分建物を新築") + ", body " + q("区分建物の表題登記と、非区分建物の表題部の変更の登記を併せて申請（法48条3項）") + ".",
            "Card B, tag " + q("独立性のない増築部分") + ", body " + q("既存の建物に付合し、既存の建物の所有者のものになる（民法242条）") + ".",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 2 side note cards. Every diamond has exactly two exits, and no arrow leaves a result box."]
    return finish(body, "Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 2 side note cards, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are red and RESULT 3 is blue, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解13：附属建物の変更・更正の記録と申請
def img13():
    rows = [
        ("附属建物を新築したとき", "変更後の建物図面及び各階平面図と、所有権を有することを証する情報", "令別表14項ハ"),
        ("共有建物の表題部の変更", "共有者の1人から、単独で申請できる（代位ではない）", "民法252条5項（保存行為）"),
        ("独立性のない増築部分", "既存の建物の所有者のものになる。費用を出しただけでは共有者にならない", "民法242条（付合）"),
    ]
    pre = ["--- BEFORE / AFTER CARDS (two cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card; a small dark navy tag " + q("附属建物の種類・構造・床面積の変更・更正") + " above them; a short plain dark navy right-pointing arrow sits between the two cards, with no text on it) ---",
           "Left card, heading " + q("従前の附属建物の表示") + ", three item lines: " + q("符号") + ", " + q("従前の種類・構造・床面積") + " (drawn struck through with a thin line), and the small line " + q("符号を除く全部を抹消する") + "; only the first item line " + q("符号") + " has a pale yellow highlighter marker.",
           "Right card, heading " + q("変更後・更正後の表示") + ", three item lines: " + q("符号（従前のまま）") + ", " + q("変更後の種類・構造・床面積の全部を記録") + ", and the small tag " + q("準則94条1項") + ".",
           SAME]
    return table("1080x2400", "", "附属建物の変更は、全部を書き直す", "申請人と添付情報もそろえる", "不動産登記事務取扱手続準則 第94条",
                 ("場面", "申請人・添付など", "根拠"), rows,
                 "the string " + q("単独で申請できる") + " of row 2 has a pale yellow highlighter marker.",
                 "更正後の全部を記録し、従前は符号を除いて抹消", extra_pre=pre,
                 fin="Confirm that there are exactly two before/after cards above the table.")

# ============================================================ 図解14：分割・合併
def img14():
    rows = [
        ("分割の登記", "分割前の建物を特定する家屋番号を書く", "令3条8号ロ"),
        ("分割・区分・合併の登記", "分割後・区分後・合併後の建物図面及び各階平面図を添える", "令別表16項イ"),
        ("共用部分である旨の登記がある建物の分割・区分", "所有者を証する情報も添える", "令別表16項ロ"),
        ("合筆の登記後の建物の合併", "所在の変更の登記と合併の登記は、一の申請情報で申請できる", "令4条ただし書・規則35条7号"),
    ]
    pre = ["--- WHO CARD (a wide card with a dashed dark navy outline and a small dark navy tag " + q("誰が申請するか") + ", placed directly under the header) ---",
           "Heading " + q("表題部所有者又は所有権の登記名義人だけ") + " (tag " + q("法54条1項") + "), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
           q("共有なら、持分の価格の過半数で申請できる（現行）") + ", " + q("承諾書を添えて、一人でする仕組みはない") + ".",
           "The string " + q("持分の価格の過半数") + " has a pale yellow highlighter marker."]
    return table("1080x2400", "", "分割・合併の登記を、誰がする？", "申請人と、添える図面", "不動産登記法 第54条・不動産登記令 別表16の項",
                 ("登記", "申請情報・添付情報", "根拠"), rows,
                 "the string " + q("建物図面及び各階平面図") + " of row 2 has a pale yellow highlighter marker.",
                 "合併の登記にも、合併後の図面が要る", extra_pre=pre,
                 fin="Confirm that the who card appears once above the table.")

# ============================================================ 図解15：共用部分の登記
def img15():
    return two_cards("1080x1900", "", "共用部分の登記で、消えるものは？", "建物は残り、省略もできる", "不動産登記法 第58条・不動産登記令 第6条",
                     ("法58条4項", "共用部分である旨の登記をすると",
                      ["登記記録は存続し、一個の建物のまま", "職権で抹消されるのは、表題部所有者の登記又は権利に関する登記", "種類・構造・床面積などは残る"]),
                     ("令別表19項・令6条2項4号", "団地共用部分である旨の登記では",
                      ["共用すべき者の建物（区分建物でないとき）の所在・地番・家屋番号を書く", "不動産番号を申請情報にしたときは、それらを省略できる"]),
                     "消えるのは所有者と権利の登記。種類は消えない",
                     "the string " + q("職権で抹消されるのは、表題部所有者の登記又は権利に関する登記") + " in the left card and the string " + q("省略できる") + " in the right card have a pale yellow highlighter marker.",
                     "")

# ============================================================ 図解16：滅失の登記の申請人・添付・期限
def img16():
    rows = [
        ("通常の建物", "表題部所有者又は所有権の登記名義人が、滅失の日から1か月以内に申請", "法57条"),
        ("共用部分である旨の登記がある建物", "所有者が申請し、所有者を証する情報を添える。所有者の一人から申請できる", "法57条・令別表17項"),
        ("所有者が異なる区分建物が属する一棟の建物の全部滅失", "区分建物の所有者の一人から、一棟の建物の滅失の登記を申請できる", "先例による取扱い"),
        ("特定登記がある区分建物の滅失", "土地の抵当権も消滅させる承諾の情報を提供すると、その土地の抵当権が消滅した旨が記録される", "法55条4項"),
        ("申請情報・添付情報の保存期間", "受付の日から30年間", "規則28条9号"),
    ]
    return table("1080x2600", "", "建物の滅失の登記は、誰が・いつ？", "申請人・添付情報・保存期間", "不動産登記法 第57条",
                 ("場面", "申請人・添付情報など", "根拠"), rows,
                 "the string " + q("1か月以内") + " of row 1, the string " + q("所有者の一人から申請できる") + " of row 2 and the string " + q("30年間") + " of row 5 have a pale yellow highlighter marker.",
                 "共用部分の登記がある建物は、申請人が所有者")

# ============================================================ 図解17：滅失かどうか
def img17():
    body = [lead("1080x2600", "This is a flowchart poster (判定の流れ) with one side note card."), TEXTREQ, BGREQ, COLOR] + \
           header("滅失の登記が使えるのは、いつ？", "効用を失ったかで判断する", "不動産登記法 第57条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every RED 「いいえ」 branch leads down or right as described, and the blue result boxes sit to the RIGHT of their diamonds on the same row with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The red result box at the bottom sits below DIAMOND 2 on the center line. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("建物の滅失の登記を考える"),
            "NODE DIAMOND 1: " + q("社会通念上、建物が効用を失った状態か？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("建物の滅失") + " on the first line and " + q("滅失の日から1か月以内に、滅失の登記を申請する") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("区分建物として登記されているが、初めから区分していなかったことが明らかか？") + " The text is placed inside the diamond on 4 lines.",
            "  - Arrow right to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box): " + q("錯誤を原因として、滅失の登記を申請する") + " on two lines and the small tag " + q("先例による取扱い") + ".",
            "NODE RESULT 3 (red box): " + q("滅失の登記は申請できない") + " on the first line and " + q("例：火災で一部が焼けても、主要構造部が残り使える") + " on the next two lines.",
            "--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("滅失とは") + ", body " + q("社会通念上、建物が効用を失った状態") + " and " + q("定義した条文はなく、判例・先例の整理") + ".",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 1 side note card. Every diamond has exactly two exits, and no arrow leaves a result box."]
    return finish(body, "Confirm there is exactly 1 start node, 2 diamonds, 3 result boxes and 1 side note card, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解18：図面は要るか
def img18():
    rows = [
        ("所在・地番の変更（表題部の変更）", "変更後の建物図面", "令別表14項イ"),
        ("床面積の変更（表題部の変更）", "変更後の建物図面及び各階平面図", "令別表14項ロ"),
        ("附属建物の新築（表題部の変更）", "変更後の建物図面及び各階平面図（と所有権を証する情報）", "令別表14項ハ"),
        ("分割・区分・合併", "分割後・区分後・合併後の建物図面及び各階平面図", "令別表16項イ"),
        ("区分建物の増築", "増築した専有部分の変更箇所を示せば足りる", "登記実務の取扱い"),
        ("建物の種類の変更", "新たに提供する規定はない（図面が備え付けられていなくても）", "令別表14項に規定がない"),
        ("附属建物の滅失で、残る建物の位置・床面積が変わらない", "図面が提出済みなら、提供を省略できる", "実務上の整理"),
        ("共用部分である旨の規約を廃止した表題登記", "提供を要しない", "令別表21項に図面がない"),
    ]
    return table("1080x2900", "", "建物図面・各階平面図は、要る？", "令別表14項のイ・ロ・ハで見る", "不動産登記令 別表 十四の項・十六の項",
                 ("登記", "建物図面・各階平面図", "根拠"), rows,
                 "the cells of column 2 of rows 6, 7 and 8 (the rows that need no new drawing) have a pale yellow highlighter marker; the cells of column 2 of rows 1 to 5 are plain.",
                 "位置・形状・床面積が変わる登記では必要")

# ============================================================ 図解19：建物図面の作り方・保存期間
def img19():
    body = [lead("1080x2300", "This is a vertical poster with three wide cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("建物図面の作り方と保存期間", "記録事項・永久と30年・拡大表示", "不動産登記規則 第28条・第73条") + \
           ["--- THREE WIDE CARDS (stacked top to bottom, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card, each with a small dark navy tag at its top left) ---",
            "Card 1: tag " + q("規則73条2項") + ", heading " + q("電子署名で提供する図面にも、記録する") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("作成の年月日") + ", " + q("申請人の氏名又は名称") + ", " + q("作成者の氏名又は名称") + ". Under them one small line " + q("資格者代理人が電子署名をしても、省略されない") + ".",
            "Card 2: tag " + q("規則28条13号") + ", heading " + q("建物図面・各階平面図の保存期間") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("永久") + ", " + q("閉鎖したものは、閉鎖した日から30年間") + ", " + q("えい行移転で所在変更をした従前の図面も、30年") + ".",
            "Card 3: tag " + q("先例により認められた扱い") + ", heading " + q("建物が小さすぎて図示できないとき") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("本図には、位置のみを記入する") + ", " + q("用紙の余白に、適宜の縮尺で拡大表示する") + ", " + q("本図と拡大図で、方位をそろえる") + ".",
            "Highlighting: the string " + q("電子署名") + " in the heading of card 1, the string " + q("永久") + " in card 2 and the string " + q("位置のみを記入する") + " in card 3 have a pale yellow highlighter marker.",
            FIT, "The three cards have clearly different texts; the texts are NOT identical.",
            "Under the three cards, one wide dark navy band with large white text " + q("図面の保存は永久、閉鎖したら30年") + "."]
    return finish(body, "Confirm there are exactly three cards with exactly three item lines each (card 1 has one more small line), that the three tags are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
P = "不動産登記法編⑤_図解"
META = [
    (1, "建物の登記を、順に確かめる（個数・表示・変更・分合・滅失・図面）", "カードポスター型（俯瞰）", "1080×2900", P + "1_建物の登記を順に確かめる", "「この章の誤りの傾向」の段落の直後", img1, "00_zentai"),
    (2, "登記記録は、何ごとに作る？（単位と、表題部・権利部の区分）", "カード＋構造図型", "1080×2000", P + "2_登記記録の単位と区分", "【PE-1】「中身の整理」の直後", img2, "PE-1"),
    (3, "一個の建物にできる？（数棟か、一棟の中かで見分ける）", "判定の流れ型（フローチャート）", "1080×2500", P + "3_一個の建物にできるか", "【PE-2】「中身の整理」の直後", img3, "PE-2"),
    (4, "抵当権があると、できない？（新築の附属建物と合併は別）", "対比カード型（2列）", "1080×1800", P + "4_新築の附属建物と合併", "【PE-2】「たとえば」の直後", img4, "PE-2"),
    (5, "種類と構造は、何で決める？", "早見表型（3列）", "1080×2300", P + "5_種類と構造の決め方", "【PE-3】「中身の整理」の直後", img5, "PE-3"),
    (6, "床面積は、どの線で測る？（専有部分だけが内法）", "早見表型＋カード", "1080×2400", P + "6_床面積の基準線", "【PE-4】「中身の整理」の直後", img6, "PE-4"),
    (7, "床面積に算入する？ しない？（低い天井・塔屋・観覧席）", "判定の流れ型＋補足カード", "1080×2500", P + "7_床面積に算入するか", "【PE-4】図解6の直後", img7, "PE-4"),
    (8, "建物の所在は、どう書く？", "早見表型（3列）", "1080×2400", P + "8_建物の所在", "【PE-5】「中身の整理」の直後", img8, "PE-5"),
    (9, "附属建物の表示は、何を書く？（区分建物かどうかで分かれる）", "判定の流れ型", "1080×2600", P + "9_附属建物の表示", "【PE-6】「中身の整理」の直後", img9, "PE-6"),
    (10, "保存登記が錯誤で消えたら、登記記録は閉鎖される？", "対比カード型（2列）", "1080×1900", P + "10_保存登記の錯誤抹消", "【PE-7】「中身の整理」の直後", img10, "PE-7"),
    (11, "表題登記まわりの特殊場面（転得者の代位と敷地権の日付）", "縦カード型", "1080×1900", P + "11_転得者と敷地権の日付", "【PE-7】図解10の直後", img11, "PE-7"),
    (12, "変更の登記は、要る？ 要らない？", "判定の流れ型＋補足カード", "1080×2700", P + "12_変更の登記は要るか", "【PE-8】「中身の整理」の直後", img12, "PE-8"),
    (13, "附属建物の変更は、全部を書き直す（申請人と添付情報）", "対比カード＋早見表型", "1080×2400", P + "13_附属建物の変更と申請人", "【PE-8】図解12の直後", img13, "PE-8"),
    (14, "分割・合併の登記を、誰がする？（申請人と添える図面）", "早見表型＋カード", "1080×2400", P + "14_分割合併の申請人と図面", "【PE-9】「中身の整理」の直後", img14, "PE-9"),
    (15, "共用部分の登記で、消えるものは？", "対比カード型（2列）", "1080×1900", P + "15_共用部分の登記", "【PE-10】「中身の整理」の直後", img15, "PE-10"),
    (16, "建物の滅失の登記は、誰が・いつ？", "早見表型（3列）", "1080×2600", P + "16_滅失の登記の申請人", "【PE-11】「中身の整理」の直後", img16, "PE-11"),
    (17, "滅失の登記が使えるのは、いつ？（効用を失ったかで判断）", "判定の流れ型＋補足カード", "1080×2600", P + "17_滅失かどうか", "【PE-11】図解16の直後", img17, "PE-11"),
    (18, "建物図面・各階平面図は、要る？", "早見表型（3列）", "1080×2900", P + "18_図面は要るか", "【PE-12】「中身の整理」の直後", img18, "PE-12"),
    (19, "建物図面の作り方と保存期間", "縦カード型", "1080×2300", P + "19_建物図面の作り方と保存期間", "【PE-13】「中身の整理」の直後", img19, "PE-13"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PE-1": ("prompt_infographic_PE-01.md", "【PE-1】登記記録は何ごとに作られ、どう区分されるか"),
    "PE-2": ("prompt_infographic_PE-02.md", "【PE-2】建物の個数はどう決まるか（効用上一体・区分・附属建物の主従）"),
    "PE-3": ("prompt_infographic_PE-03.md", "【PE-3】建物の種類・構造は何でどう定めるか"),
    "PE-4": ("prompt_infographic_PE-04.md", "【PE-4】床面積の測り方と算入・不算入、記録の順序"),
    "PE-5": ("prompt_infographic_PE-05.md", "【PE-5】建物の所在はどう記録されるか（またがり・仮換地・附属建物）"),
    "PE-6": ("prompt_infographic_PE-06.md", "【PE-6】附属建物の表示で何を書き、何が省略できるか"),
    "PE-7": ("prompt_infographic_PE-07.md", "【PE-7】表題登記まわりの特殊場面（保存登記の錯誤抹消・転得者・敷地権の日付）"),
    "PE-8": ("prompt_infographic_PE-08.md", "【PE-8】表題部の変更・更正の登記が必要なとき、必要な添付情報と記録のしかた"),
    "PE-9": ("prompt_infographic_PE-09.md", "【PE-9】建物の分割・合併の登記（申請人・申請情報・添付情報）"),
    "PE-10": ("prompt_infographic_PE-10.md", "【PE-10】共用部分である旨の登記がある建物の扱い"),
    "PE-11": ("prompt_infographic_PE-11.md", "【PE-11】建物の滅失の登記（申請人・添付情報・滅失の意味・保存期間）"),
    "PE-12": ("prompt_infographic_PE-12.md", "【PE-12】建物図面・各階平面図の提供が必要か不要か"),
    "PE-13": ("prompt_infographic_PE-13.md", "【PE-13】建物図面の作成方法と保存期間"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事② 不動産登記法編 第5章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "判定の流れ図（フローチャート）では、はい＝青・いいえ＝赤で描きます。分類・早見表・比較カードの図は、はい／いいえの分岐ではないため、青・赤を使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
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
