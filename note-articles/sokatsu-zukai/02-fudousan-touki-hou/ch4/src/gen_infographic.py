#!/usr/bin/env python3
"""総合記事②不動産登記法編 第4章（土地の分筆・合筆・地積更正）：図解インフォグラフィック14枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PD-1.md ／ … ／ _PD-11.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
TABLE_STYLE = "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font."
GLANCE = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. "
          "Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. "
          "Do NOT render any full-sentence explanation or paragraph of body text.")

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

NOMARK = "no check mark, no cross mark, blue, or red appears anywhere"

# ------------------------------------------------------------ 部品：表（3列）
def table3(size, kind, t1, t2, sub, heads, rows, hl, band, extra_after=None):
    body = [lead(size, kind), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub) + [
        "--- TABLE ---",
        TABLE_STYLE + f" Exactly 3 columns and exactly {len(rows)} data rows, no merged cells.",
        "Header row (dark navy cells with white text): " + ", ".join(q(h) for h in heads) + ".",
        "Data rows, one per line, in this order (column 1 | column 2 | column 3):"]
    body += [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)]
    body += [hl + " Copy each cell exactly as given; cells that look alike differ in their wording, so do not change one into another."]
    if extra_after:
        body += extra_after
    if extra_after:
        body += ["At the very bottom of the poster, below everything else, one wide dark navy band with large white text " + q(band) + "."]
    else:
        body += ["Under the table, one wide dark navy band with large white text " + q(band) + "."]
    return body

# ------------------------------------------------------------ 部品：2列の対比（行ラベルつき）
def compare2(size, kind, t1, t2, sub, lcol, rcol, rows, band=None, note=None):
    body = [lead(size, kind), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub) + [
        "--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---", q(lcol),
        "--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---", q(rcol),
        "The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red."]
    for i, (label, l, r, hl) in enumerate(rows, 1):
        body += [f"--- ROW {i} (row label " + q(label) + ") ---", "Left card: " + l, "Right card: " + r]
        if hl:
            body += [hl]
    body += ["The left and right cards of each row have clearly different texts; the texts are NOT identical."]
    if band:
        body += ["Under the two columns, one wide dark navy band with large white text " + q(band) + "."]
    if note:
        body += ["At the bottom, one small light-gray tag centered across both columns: " + q(note)]
    return body

# ------------------------------------------------------------ 部品：カードポスター（番号つき・縦1列）
def cards_poster(size, t1, t2, sub, cards, n_word):
    body = [lead(size, f"This is a quick-reference poster with {n_word} numbered cards in one column; it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return body, f"Confirm the number of cards equals {len(cards)} exactly, numbered 1 to {len(cards)} in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, and confirm that {NOMARK}."

# ============================================================ 図解1：全体（5つの登記）
def img_zentai():
    cards = [
        ("分筆の登記", "A land plot icon split in two by a dashed boundary line, with a registry ledger card copied beside each part, no text on the cards.",
         ["申請人は、表題部所有者・登記名義人", "権利は、分筆後の各土地に転写される"], "権利者の承諾は不要"),
        ("権利を消す分筆", "A land plot split in two, with one ledger line shown faded in one part and a signed paper sheet beside it, no text on the sheet.",
         ["消すなら、権利者の承諾の情報", "承諾した土地には、消えた旨を記録"], "法40条・規則104条"),
        ("合筆の登記", "Two adjacent land plots being joined into one, with a small padlock-shaped tag on one plot, no text on the tag.",
         ["合筆できない場合は、法41条の6つ", "所有権以外の権利は、原則不可"], "例外は規則105条の4つ"),
        ("地積の更正の登記", "A land plot with a measuring tape and a pencil correcting a number on a registry page, no text on the page.",
         ["申請できる者は、法38条で限られる", "申請の期限も、義務もない"], "変更は1か月以内"),
        ("合筆の登記識別情報", "A small key-shaped card beside a document sheet with a rubber stamp, no text on the card or the sheet.",
         ["提供するのは、いずれか一筆分", "通知を受ける代理人は、特別の委任"], "理由は書くだけ"),
    ]
    body, ex = cards_poster("1080x2600", "分筆・合筆・地積更正", "申請する人と、権利の行方", "不動産登記法 第37条〜第41条", cards, "five")
    return finish(body, ex)

# ============================================================ PD-1：誰が申請できるか
def img_pd1():
    rows = [
        ("表題部所有者・所有権の登記名義人", "申請できる", "法39条1項"),
        ("表題部所有者の土地を買っただけの者", "自分では申請できない", "売主の承諾書があっても同じ"),
        ("土地の一部を買った者", "売主に代位して申請できる", "民法423条・令3条4号"),
        ("共有地の持分の一部を買った者（国を含む）", "当然には代位できない", "土地を分ける前提がない"),
        ("共有者の1人", "単独では申請できない（原則）", "承諾書を添えても同じ"),
        ("相続財産の管理人・不在者の財産管理人", "申請できる", "家庭裁判所の許可は要らない"),
    ]
    hl = "Highlighting: the string 「当然には代位できない」 of row 4 and the string 「家庭裁判所の許可は要らない」 of row 6 have a pale yellow highlighter marker; every other cell is plain."
    body = table3("1080x2000", "This is a reference table poster with three columns.", "分筆・合筆を申請できる人は？", "名義人と、代位できる人", "不動産登記法 第39条第1項",
                  ["申請する人", "申請できるか", "決め手"], rows, hl, "名義人以外は、代位の根拠があるときだけ")
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that only the two marked strings are highlighted, and that {NOMARK}.")

# ============================================================ PD-2：分筆すると権利はどうなる
def img_pd2():
    rows = [
        ("承諾の情報", "A plain document sheet icon drawn with a thin dashed outline, labeled " + q("要らない") + " and a small line " + q("仮差押え・賃借権・抵当権も同じ") + ".",
         "A signed document sheet labeled " + q("権利者の承諾の情報が要る") + ".",
         "In the left card the string 「要らない」 has a pale yellow highlighter marker."),
        ("権利の行方", "A registry ledger icon copied into two land plots, labeled " + q("分筆後の各土地に転写される") + ".",
         "A registry ledger icon with one stamped line, labeled " + q("承諾した土地には、消えた旨が記録される") + ".", None),
        ("共有の土地", "Two land plots, each with a small two-person pictogram, labeled " + q("東も西も、共有のまま") + ".",
         "A document sheet labeled " + q("単独所有にするには、持分移転の登記が別に必要") + ".", None),
    ]
    body = compare2("1080x1900", "This is a two-column comparison poster (対比表).", "分筆に、承諾は要る？", "要るのは、権利を消すときだけ", "不動産登記法 第40条・不動産登記規則 第102条",
                    "分筆するだけ", "分筆後の土地で権利を消す", rows,
                    band="分筆は区画の登記。権利は転写される")
    return finish(body, f"Confirm there are exactly 2 columns and exactly 3 rows of cards, that the left and right texts of each row are different, and that {NOMARK}.")

# ============================================================ PD-3：地積の書き方
def img_pd3():
    rows = [
        ("10平方メートル以下", "地目を問わない", "小数点以下第2位まで"),
        ("10平方メートルを超える", "宅地・鉱泉地", "小数点以下第2位まで"),
        ("10平方メートルを超える", "それ以外の地目", "整数（1平方メートル未満は切り捨て）"),
    ]
    hl = "Highlighting: the string 「地目を問わない」 of row 1 and the string 「整数（1平方メートル未満は切り捨て）」 of row 3 have a pale yellow highlighter marker; every other cell is plain. Rows 1 and 2 have the same text in column 3 on purpose; draw the same string in both."
    extra = ["--- TWO EXAMPLE CHIPS (side by side, same size, below the table) ---",
             "Left chip: " + q("例：公衆用道路 9.0025 → 9.00") + ". Right chip: " + q("例：畑 215.4766 → 215") + ".",
             "--- TWO NOTE CARDS (stacked, below the chips, each a wide card with a dashed dark navy outline) ---",
             "Note card 1: heading " + q("宅地造成工事中の畑") + ", body " + q("完成するまでは、従前の地目（畑）のまま") + " and a small gray tag " + q("現況主義からの整理") + ".",
             "Note card 2: heading " + q("地目変更と分筆を一の申請情報にするとき") + ", body " + q("地目変更の登記原因とその日付も書く") + " and a small gray tag " + q("規則35条7号") + "."]
    body = table3("1080x2400", "This is a reference table poster with three columns, followed by two example chips and two note cards.", "地積の桁は、どう決まる？", "10平方メートルが分かれ目", "不動産登記規則 第100条",
                  ["土地の大きさ", "地目", "地積の書き方"], rows, hl, "宅地・鉱泉地以外は、10平方メートル超で整数", extra_after=extra)
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 3 data rows, that rows 1 and 2 show the same string in column 3, that there are exactly two example chips and two note cards below the table, and that {NOMARK}.")

# ============================================================ PD-4：分筆に添える情報
def img_pd4():
    cards = [
        ("いつも添える", "A survey drawing sheet of a land plot split by a boundary line, no text on the drawing.",
         ["分筆後の土地の地積測量図", "分筆の添付情報の柱"], "令別表8の項"),
        ("地役権の範囲が一部になるとき", "Two land plot icons joined by a thin dotted footpath with a small document sheet beside it, no text on the sheet.",
         ["地役権者が作成した情報", "地役権図面も添える"], "承役地の分筆のとき"),
        ("規約を証する情報は？", "A building icon and a land plot icon separated by a thin line, with a small document sheet drawn with a thin dashed outline, no text on the sheet.",
         ["分筆の添付情報ではない", "要るのは、敷地権を消す建物の表題部の変更"], "令別表15の項"),
        ("承諾書の印鑑証明書", "A signed paper sheet and a round seal-certificate card side by side, no text on them.",
         ["承諾書側には、3か月の期限はない", "会社なら、会社法人等番号で省ける"], "期限なし"),
    ]
    body, ex = cards_poster("1080x2300", "分筆に添える情報は？", "柱は地積測量図", "不動産登記令 別表8の項・第19条", cards, "four")
    body += ["Below card 4, one small light-gray tag centered across the card width: " + q("申請書・委任状の印鑑証明書は、作成後3か月以内")]
    return finish(body, ex + " Also confirm that the small light-gray tag appears once, below card 4, and not inside any other card.")

# ============================================================ PD-5：権利を消す分筆の場面別の扱い
def img_pd5():
    rows = [
        ("乙土地について、権利を消す承諾", "甲土地に「乙土地について消滅」の付記。乙土地には転写しない", "規則104条2項"),
        ("甲土地について、権利を消す承諾", "甲土地に消滅の付記と抹消の記号。乙土地には転写される", "規則104条3項"),
        ("その権利の上に、第三者の権利があるとき", "第三者の承諾の情報も要る", "規則104条1項2号"),
        ("所有権移転請求権保全の仮登記", "承諾すれば消せる。乙土地に転写されない", "権利に関する登記の一つ"),
        ("差押えなど処分の制限の登記", "承諾の情報があっても、消せない", "実務の取扱い"),
        ("要役地の地役権", "地役権者が作成した情報で消せる", "規則104条6項"),
    ]
    hl = "Highlighting: the string 「消せない」 of row 5 has a pale yellow highlighter marker; every other cell is plain."
    body = table3("1080x2300", "This is a reference table poster with three columns.", "分筆で権利を消す場面", "どちらの土地に、何が記録される？", "不動産登記法 第40条・不動産登記規則 第104条",
                  ["場面", "登記の扱い", "根拠"], rows, hl, "甲・乙の両方で消す処理は、法40条の想定外")
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 6 data rows, that every cell reads exactly as given, that rows 1 and 2 differ in the words 乙土地 and 甲土地, and that {NOMARK}.")

# ============================================================ PD-6：権利を消した分筆は錯誤で戻せるか（判定の流れ図）
def img_pd6():
    body = [lead("1080x2300", "This is a flowchart poster (判定の流れ図)."), TEXTREQ, BGREQ, COLOR] + \
           header("分筆を錯誤で戻せる？", "分かれ目は、権利を消したか", "不動産登記法 第40条・第72条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit below the diamond, one to the left and one to the right of the center line, at the same height and the same size. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("分筆の登記を、錯誤で抹消したい"),
            "NODE DIAMOND 1: " + q("分筆のとき、権利を消す承諾の情報を出していないか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down-left with the BLUE label " + q("はい") + " to RESULT 1.",
            "  - Arrow down-right with the RED label " + q("いいえ") + " to RESULT 2.",
            "NODE RESULT 1 (blue box): " + q("錯誤を原因に、分筆の登記を抹消できる") + " on the first line and " + q("前から付いていた抵当権は、転写されただけ") + " on the second line.",
            "NODE RESULT 2 (red box): " + q("分筆錯誤だけでは、抹消できない") + " on the first line, " + q("先に、消えた権利の登記の回復が要る（法72条）") + " on the second line and " + q("回復には、利害関係人の承諾が要る") + " on the third line.",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts.",
            "--- SIDE NOTE (below the result boxes, a wide card with a dashed dark navy outline and a small gray tag " + q("右の扱いは、実務の取扱いによる整理") + ") ---",
            "Heading " + q("分かれ目は、承諾の情報を出したか") + ", body " + q("抵当権があるだけでは、分筆錯誤を妨げない") + "."]
    return finish(body, "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that no text overflows its box, that no arrow label is hidden, and that the side note appears once below the result boxes.")

# ============================================================ PD-7：合筆できない場合 第41条1号〜6号
def img_pd7():
    rows = [
        ("1号", "相互に接続していない土地", "例：離れた2筆"),
        ("2号", "地目又は地番区域が相互に異なる土地", "現況の地目が違えば不可（実務の取扱い）"),
        ("3号", "表題部所有者又は所有権の登記名義人が相互に異なる土地", "例：名義人がAとB"),
        ("4号", "持分を相互に異にする土地", "例：持分の割合が違う"),
        ("5号", "所有権の登記がない土地と、ある土地", "例：名義人が同じAでも不可"),
        ("6号", "所有権以外の権利に関する登記がある土地", "例外は規則105条"),
    ]
    hl = "Highlighting: the string 「現況の地目が違えば不可（実務の取扱い）」 of row 2 and the string 「名義人が同じAでも不可」 of row 5 have a pale yellow highlighter marker; every other cell is plain."
    extra = ["--- NOTE CARD (below the table, a wide card with a dashed dark navy outline and a small gray tag " + q("条文にない事由") + ") ---",
             "Heading " + q("制限にならないもの") + ", two body lines " + q("保安林の指定") + " and " + q("登記できない使用貸借") + "."]
    body = table3("1080x2300", "This is a reference table poster with three columns, followed by one note card.", "合筆できない場合は？", "第41条の6つの事由", "不動産登記法 第41条",
                  ["号", "合筆できない土地", "ひとこと"], rows, hl, "保安林・使用貸借は、合筆の制限にならない", extra_after=extra)
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 6 data rows numbered 1号 to 6号 in order, that every cell reads exactly as given, that there is exactly one note card below the table, and that {NOMARK}.")

# ============================================================ PD-8：第41条6号の原則と例外
def img_pd8():
    ok = ["承役地についてする地役権の登記", "担保権の登記（目的・受付・原因が同一）", "信託の登記（登記事項が同一）", "鉱害賠償登録に関する登記（登録番号が同一）"]
    ng = ["永小作権・採石権の登記（内容が同一でも）", "所有権の移転の仮登記（同一でも）", "敷地権である旨の登記", "要役地の地役権の登記"]
    body = [lead("1080x2300", "This is a comparison poster: one wide principle card at the top and two side-by-side list cards below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("所有権以外の権利があると", "原則どおり、合筆できない", "不動産登記法 第41条6号・不動産登記規則 第105条") + \
           ["--- PRINCIPLE CARD (a wide dark navy card at the top, with white text) ---",
            "Small label " + q("原則") + ", then the bold text " + q("所有権以外の権利の登記がある土地は、合筆できない") + ".",
            "--- TWO LIST CARDS (side by side, exactly the same size, top-aligned, each with exactly four rows; each row has the item text with a small dark navy dot at its left end, NO number on the dots) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("例外：規則105条の4つ") + ", with a small tag " + q("合筆できる") + ". The four rows, in this order:"] + \
           [f"  Row {i}: {q(x)}" for i, x in enumerate(ok, 1)] + \
           ["Right card: heading bar (pale gray fill, dark navy text) " + q("例外にない登記") + ", with a small tag " + q("合筆できない") + ". The four rows, in this order:"] + \
           [f"  Row {i}: {q(x)}" for i, x in enumerate(ng, 1)] + \
           ["Highlighting: the left-card row 1 and the right-card row 4 have a pale yellow highlighter marker. The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("登記が残る限り、実体が消えていても制限は外れない") + ".",
            "Under the band, one small light-gray tag centered: " + q("仮登記・敷地権である旨の登記は、実務の取扱い")]
    return finish(body, f"Confirm there are exactly two list cards with exactly four rows each, that the left card holds the four exceptions and the right card holds the four registrations that are not exceptions, that the two headings are not swapped, and that {NOMARK}.")

# ============================================================ PD-9a：承役地と要役地
def img_pd9a():
    rows = [
        ("合筆できるか", "A land plot icon with a small dotted footpath leading out of it, labeled " + q("できる（規則105条1号の例外）") + ".",
         "A land plot icon with a small dotted footpath leading into it, labeled " + q("できない（例外にない）") + ".",
         "In the right card the string 「できない」 has a pale yellow highlighter marker."),
        ("内容が同一のとき", "A document sheet labeled " + q("地役権の登記があるだけでは、妨げにならない") + ".",
         "A document sheet labeled " + q("目的・範囲・登記の年月日が同一でも、できない") + ".", None),
        ("申請情報", "A document sheet labeled " + q("設定範囲が一部になるなら、範囲を書く（令別表9の項）") + ".",
         "A document sheet labeled " + q("合筆できないので、書く場面にならない") + ".", None),
    ]
    body = compare2("1080x1900", "This is a two-column comparison poster (対比表).", "地役権のある土地の合筆", "承役地は可、要役地は不可", "不動産登記規則 第105条1号・不動産登記令 別表9の項",
                    "承役地の地役権の登記", "要役地の地役権の登記", rows,
                    band="例外になるのは、承役地側だけ")
    return finish(body, f"Confirm there are exactly 2 columns and exactly 3 rows of cards, that the left and right headers are not swapped, that the left and right texts of each row are different, and that {NOMARK}.")

# ============================================================ PD-9b：担保権の登記が同一とは
def img_pd9b():
    chips = ["登記の目的", "申請の受付の年月日", "受付番号", "登記原因", "登記原因の日付"]
    body = [lead("1080x2300", "This is a quick-reference poster: one wide chip card, one two-column example area and one note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("担保権の登記が同一とは？", "5点が同じで、全部が対応", "不動産登記規則 第105条2号") + \
           ["--- CHIP CARD (a wide pale gray card at the top with a dark navy outline) ---",
            "Heading " + q("同一といえる5点") + ", then exactly five chips in one row (or two short rows), each a rounded pale gray chip with a small dark navy dot, in this order:"] + \
           [f"  Chip {i}: {q(x)}" for i, x in enumerate(chips, 1)] + \
           ["The chips " + q("申請の受付の年月日") + " and " + q("受付番号") + " have a pale yellow highlighter marker.",
            "--- TWO EXAMPLE CARDS (side by side, exactly the same size, top-aligned, each heading placed fully INSIDE the card) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("合筆できる") + ", body " + q("甲に1件、乙に1件") + " and " + q("5点とも同一で、全部が対応") + ".",
            "Right card: heading bar (pale gray fill, dark navy text) " + q("合筆できない") + ", two body items each with a small dark navy dot: " + q("受付番号が違う（目的と原因は同じ）") + " and " + q("甲に2件、乙に1件で、一組だけ同一") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- NOTE CARD (below the example cards, a wide card with a dashed dark navy outline and a small gray tag " + q("実務の整理") + ") ---",
            "Heading " + q("破産手続開始の登記") + ", body " + q("終結の登記があれば、抹消しなくても合筆できる") + ".",
            "Under the note card, one wide dark navy band with large white text " + q("受付番号まで同一で、全部の担保権が対応すること") + "."]
    return finish(body, f"Confirm the chip card has exactly five chips in the given order, that there are exactly two example cards and one note card, that the two heading bars are not swapped, and that {NOMARK}.")

# ============================================================ PD-10：合筆の登記識別情報
def img_pd10():
    cards = [
        ("提供する", "A key-shaped card being handed over together with a document sheet, no text on the card or the sheet.",
         ["所有権の登記がある土地の合筆", "いずれか一筆の名義人分でよい"], "令8条"),
        ("通知を受ける", "A small envelope containing a key-shaped card, held by a person pictogram with a briefcase, no text on the envelope.",
         ["合筆後に、新しい通知がされる", "代理人が受けるには、特別の委任"], "規則62条2項"),
        ("提供できないとき", "A key-shaped card drawn with a thin dashed outline, next to a pencil writing one line on a form, no text on the form.",
         ["理由を申請情報に書けば足りる", "理由を証する情報は、要らない"], "令3条12号"),
    ]
    body, ex = cards_poster("1080x1900", "合筆の登記識別情報", "提供・通知・提供できないとき", "不動産登記令 第8条・第3条・不動産登記規則 第62条", cards, "three")
    return finish(body, ex)

# ============================================================ PD-11a：地積の変更と更正
def img_pd11a():
    rows = [
        ("どんな登記", "A land plot icon with a slightly different outline drawn over it, labeled " + q("地積に変更があったときの登記") + ".",
         "A registry page with a pencil correcting one line, labeled " + q("最初からの誤りを直す登記") + ".", None),
        ("申請の期限", "A calendar page icon without any number, labeled " + q("変更があった日から1か月以内") + ".",
         "A calendar page icon drawn with a thin dashed outline, labeled " + q("期限はない") + ".",
         "In the right card the string 「期限はない」 has a pale yellow highlighter marker."),
        ("申請の義務", "A rubber stamp icon, labeled " + q("申請しなければならない（法37条1項）") + ".",
         "A rubber stamp icon drawn with a thin dashed outline, labeled " + q("申請義務はない") + ".", None),
        ("申請できる者", "A person pictogram with a name tag, labeled " + q("表題部所有者・所有権の登記名義人") + ".",
         "A person pictogram with a name tag, labeled " + q("同じ名義人に限る（法38条）") + ".", None),
    ]
    body = compare2("1080x2100", "This is a two-column comparison poster (対比表).", "地積の変更と更正", "1か月以内の義務があるのは？", "不動産登記法 第37条・第38条",
                    "地積の変更の登記", "地積の更正の登記", rows,
                    band="更正には、申請の期限も義務もない")
    return finish(body, f"Confirm there are exactly 2 columns and exactly 4 rows of cards, that the left and right headers are not swapped, that the left and right texts of each row are different, and that {NOMARK}.")

# ============================================================ PD-11b：地積の更正を申請できる人
def img_pd11b():
    rows = [
        ("表題部所有者・所有権の登記名義人", "申請できる", "法38条"),
        ("共有者の1人", "単独で申請できる", "他の共有者の承諾の情報は要らない"),
        ("土地の一部の所有権を取得した者", "代位して、更正と分筆を申請できる", "所有権を証する情報を提供する"),
        ("更正を命ずる判決を得た利害関係人", "代位して申請できない", "表示の登記になじまない"),
        ("名義人が動かないとき", "登記官に更正を促す", "実測図などを添えて登記所に伝える"),
    ]
    hl = "Highlighting: the string 「代位して申請できない」 of row 4 has a pale yellow highlighter marker; every other cell is plain."
    body = table3("1080x1900", "This is a reference table poster with three columns.", "地積の更正を申請できる人は？", "名義人と、代位できる人", "不動産登記法 第38条",
                  ["申請する人", "申請できるか", "決め手"], rows, hl, "判決では代位できない。一部の所有権取得者ならできる")
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the marked string is highlighted, and that {NOMARK}.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "分筆・合筆・地積更正の全体像（5つの登記）", "カードポスター型（俯瞰）", "1080×2600", "不動産登記法編4章_図解1_全体像", "「この章の論点」の一覧の直後", img_zentai, "00_zentai"),
    (2, "分筆・合筆を申請できる人は？", "早見表型（3列）", "1080×2000", "不動産登記法編4章_図解2_分筆合筆を申請できる人", "【PD-1】「中身の整理」の直後", img_pd1, "PD-1"),
    (3, "分筆に、承諾は要る？（要るのは権利を消すときだけ）", "対比カード型（2列）", "1080×1900", "不動産登記法編4章_図解3_分筆に承諾は要るか", "【PD-2】「中身の整理」の直後", img_pd2, "PD-2"),
    (4, "地積の桁は、どう決まる？", "早見表型（3列）＋補足", "1080×2400", "不動産登記法編4章_図解4_地積の桁", "【PD-3】「中身の整理」の直後", img_pd3, "PD-3"),
    (5, "分筆に添える情報は？", "カードポスター型", "1080×2300", "不動産登記法編4章_図解5_分筆に添える情報", "【PD-4】「中身の整理」の直後", img_pd4, "PD-4"),
    (6, "分筆で権利を消す場面", "早見表型（3列）", "1080×2300", "不動産登記法編4章_図解6_分筆で権利を消す場面", "【PD-5】「中身の整理」の直後", img_pd5, "PD-5"),
    (7, "分筆を錯誤で戻せる？（判定の流れ図）", "フローチャート型", "1080×2300", "不動産登記法編4章_図解7_分筆を錯誤で戻せるか", "【PD-6】「中身の整理」の直後", img_pd6, "PD-6"),
    (8, "合筆できない場合は？（第41条の6つ）", "早見表型（3列）＋補足", "1080×2300", "不動産登記法編4章_図解8_合筆できない場合", "【PD-7】「中身の整理」の直後", img_pd7, "PD-7"),
    (9, "所有権以外の権利があると（原則と例外）", "対比カード型（原則＋2列）", "1080×2300", "不動産登記法編4章_図解9_第41条6号の原則と例外", "【PD-8】「中身の整理」の直後", img_pd8, "PD-8"),
    (10, "地役権のある土地の合筆（承役地は可、要役地は不可）", "対比カード型（2列）", "1080×1900", "不動産登記法編4章_図解10_承役地と要役地", "【PD-9】「中身の整理」の直後", img_pd9a, "PD-9"),
    (11, "担保権の登記が同一とは？", "カードポスター型", "1080×2300", "不動産登記法編4章_図解11_担保権の同一", "【PD-9】図解10の直後", img_pd9b, "PD-9"),
    (12, "合筆の登記識別情報", "カードポスター型", "1080×1900", "不動産登記法編4章_図解12_合筆の登記識別情報", "【PD-10】「中身の整理」の直後", img_pd10, "PD-10"),
    (13, "地積の変更と更正", "対比カード型（2列）", "1080×2100", "不動産登記法編4章_図解13_地積の変更と更正", "【PD-11】「中身の整理」の直後", img_pd11a, "PD-11"),
    (14, "地積の更正を申請できる人は？", "早見表型（3列）", "1080×1900", "不動産登記法編4章_図解14_地積の更正を申請できる人", "【PD-11】図解13の直後", img_pd11b, "PD-11"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PD-1": ("prompt_infographic_PD-1.md", "【PD-1】分筆を申請できるのは誰か。管理人・共有者・買主・国はどうか"),
    "PD-2": ("prompt_infographic_PD-2.md", "【PD-2】分筆に、権利者の承諾は必要か。分筆で権利と持分はどうなるか"),
    "PD-3": ("prompt_infographic_PD-3.md", "【PD-3】分筆の地積はどう書くか。地目変更との一括申請では何を書くか"),
    "PD-4": ("prompt_infographic_PD-4.md", "【PD-4】分筆の添付情報には何が必要か。承諾書の印鑑証明書の扱い"),
    "PD-5": ("prompt_infographic_PD-5.md", "【PD-5】分筆に伴って権利を消すにはどうするか（法第40条と規則第104条）"),
    "PD-6": ("prompt_infographic_PD-6.md", "【PD-6】権利を消した分筆は、錯誤で抹消できるか"),
    "PD-7": ("prompt_infographic_PD-7.md", "【PD-7】合筆できない場合（第41条第1号〜第5号）と、制限にならない事情"),
    "PD-8": ("prompt_infographic_PD-8.md", "【PD-8】所有権以外の権利の登記があると、原則として合筆できない（第41条第6号）"),
    "PD-9": ("prompt_infographic_PD-9.md", "【PD-9】合筆できる例外：承役地の地役権と同一の担保権（規則第105条）"),
    "PD-10": ("prompt_infographic_PD-10.md", "【PD-10】合筆の登記識別情報：通知を受ける代理人と、提供できない理由"),
    "PD-11": ("prompt_infographic_PD-11.md", "【PD-11】地積の更正の登記：申請人、代位、判決、期限"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第4章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この章の図解は『申請できるか』『合筆できるか』のような分類が中心で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
               "例外は、はい／いいえの判定の流れ図（分筆を錯誤で戻せるか）で、はい＝青、いいえ＝赤で描きます。"
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
