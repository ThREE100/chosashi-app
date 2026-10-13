#!/usr/bin/env python3
"""総合記事②不動産登記法編 第8章（敷地権）：図解インフォグラフィック12枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch8/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PG1-1.md ／ …／ _PG1-9.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
TABLE_STYLE = "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font."
CARD_FILL = "all the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card"

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def card_poster(size, t1, t2, sub, cards, arrows=False):
    """番号つきカードを縦1列に並べたカードポスター。cards = [(見出し, イラストの指示, 結論タグ)]"""
    n = len(cards)
    body = [lead(size, f"This is a quick-reference poster with {n} numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    if arrows:
        body.append("Between consecutive cards draw one short plain dark navy arrow pointing down; this arrow means only 'next step' and carries no text.")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {n} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, f"Confirm the number of cards equals {n} exactly, numbered 1 to {n} in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, and confirm that no check mark, cross mark, blue, or red appears anywhere.")

def table_block(cols, rows, extra_hl):
    out = ["--- TABLE ---",
           f"{TABLE_STYLE} Exactly {len(cols)} columns and exactly {len(rows)} data rows, no merged cells.",
           "Header row (dark navy cells with white text): " + ", ".join(q(c) for c in cols) + ".",
           "Data rows, one per line, in this order (" + " | ".join(f"column {i}" for i in range(1, len(cols) + 1)) + "):"]
    out += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    out.append(extra_hl)
    return out

def table_poster(size, t1, t2, sub, cols, rows, extra_hl, band, kind="reference table poster", top_band=None):
    body = [lead(size, f"This is a {kind}."), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    if top_band:
        body += ["Directly under the header, one wide dark navy band with large white text " + q(top_band) + "."]
    body += table_block(cols, rows, extra_hl)
    body += ["Under the table, one wide dark navy band with large white text " + q(band) + "."]
    return finish(body, f"Confirm the table has exactly {len(cols)} columns and exactly {len(rows)} data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

def steps_poster(size, t1, t2, sub, steps, sides, top_band=None):
    """矢印でつないだステップカード＋破線の補足カード。steps = [(見出し, 本文の行のリスト, タグ or None)]、sides = [(見出し, 本文, タグ or None)]"""
    n = len(steps)
    body = [lead(size, f"This is a vertical step poster with {n} step cards and {len(sides)} side note card{'s' if len(sides) > 1 else ''}."), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    if top_band:
        body += ["Directly under the header, one wide dark navy band with large white text " + q(top_band) + "."]
    body += ["--- STEPS ---",
             f"Layout: {n} step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to {n} in order), one bold heading line, and one or two short body lines."]
    for i, (h, lines, tag) in enumerate(steps, 1):
        s = f"STEP {i}: heading " + q(h) + ", " + ("body " + q(lines[0]) if len(lines) == 1 else "two body lines " + " and ".join(q(x) for x in lines))
        if tag: s += ", and a small gray tag " + q(tag)
        body.append(s + ".")
    body.append("--- SIDE NOTE CARD" + ("S" if len(sides) > 1 else "") + " (below the steps, " + ("each a wide card" if len(sides) > 1 else "a wide card") + " with a dashed dark navy outline) ---")
    for h, b, tag in sides:
        s = "Heading " + q(h) + ", body " + q(b)
        if tag: s += " and a small gray tag " + q(tag)
        body.append(s + ".")
    return finish(body, f"Confirm there are exactly {n} step cards numbered 1 to {n} in order, followed by exactly {len(sides)} side note card{'s' if len(sides) > 1 else ''}, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解1：敷地権の一生（章の冒頭）
def img1():
    cards = [
        ("敷地権が生じる", "A land plot icon joined to an apartment building icon by a small padlock icon, with a small paper tag labeled " + q("登記された敷地利用権") + ".", "分離して処分できない"),
        ("建物の表題部に載る", "A building ledger page with one new line labeled " + q("敷地権の表示") + ".", "原因及びその日付も記録"),
        ("土地に、敷地権である旨の登記", "A land ledger page with a rubber stamp and a small label " + q("敷地権である旨") + ".", "登記官が職権で"),
        ("処分と合筆に制限がかかる", "A land plot with a small padlock icon, and two adjacent land plots separated by a thin line that cannot be joined.", "原則、土地だけの処分は不可"),
        ("敷地権が消える", "A building ledger page with one crossed-out line labeled " + q("敷地権の表示") + ", and a small calendar tag " + q("1か月以内") + ".", "表題部の変更登記を申請"),
    ]
    return card_poster("1080x2500", "敷地権の一生", "生じて、載って、消えるまで", "不動産登記法 第44条・第46条・第51条・第73条", cards, arrows=True)

# ============================================================ 図解2：区分建物に入る部分（PG1-1）
def img2():
    rows = [("専有部分", "マンションの一室", "含まれる"),
            ("規約共用部分", "規約で共用と定めた集会室", "含まれる"),
            ("法定共用部分", "廊下・階段室", "含まれない")]
    body = [lead("1080x2000", "This is a comparison poster: two cards at the top and a table below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("区分建物に入る部分は？", "専有部分と共用部分の線引き", "不動産登記法 第2条22号・区分所有法 第4条") + \
           [f"--- TWO CARDS (side by side, {CARD_FILL}) ---",
            "Left card, heading " + q("構造上の独立性") + ", body " + q("壁・床・天井で区切られている") + ".",
            "Right card, heading " + q("利用上の独立性") + ", body " + q("それだけで住居・店舗などに使える") + ".",
            "The two cards have clearly different texts; the texts are NOT identical."] + \
           table_block(["部分", "たとえば", "区分建物か"], rows,
                       "Highlighting: the string 「含まれる」 of rows 1 and 2 has a pale yellow highlighter marker; the cell 「含まれない」 of row 3 is plain. The cells 「含まれる」 and 「含まれない」 differ by two characters; copy each exactly as given and do not change one into the other.") + \
           ["Under the table, one wide dark navy band with large white text " + q("専有部分と規約共用部分が、区分建物") + "."]
    return finish(body, "Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 3 data rows, that rows 1 and 2 read 含まれる and row 3 reads 含まれない in column 3, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：敷地権になれるか（判定の流れ。PG1-2）
def img3():
    body = [lead("1080x2000", "This is a flowchart poster (判定の流れ図)."), TEXTREQ, BGREQ, COLOR] + \
           header("敷地権になれるか", "上から順に確かめる", "不動産登記法 第44条第1項第9号") + \
           ["--- FLOWCHART ---",
            "Layout: a vertical main line down the center: START at the top, then DIAMOND 1, then DIAMOND 2, then RESULT 1 at the bottom. RESULT 2 sits to the right of DIAMOND 1 and RESULT 3 sits to the right of DIAMOND 2, each reached by one straight horizontal arrow. Keep at least 60 px of empty space around every arrow label so that the labels stay visible. All arrows are straight, and no arrows cross each other.",
            "NODE START (rounded pill, dark navy): " + q("専有部分のための敷地の権利"),
            "NODE DIAMOND 1: " + q("登記された権利か？") + " The text is placed inside the diamond on 2 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down with the label " + q("はい") + " to DIAMOND 2.",
            "  - Arrow right with the label " + q("いいえ") + " to RESULT 2.",
            "NODE DIAMOND 2: " + q("専有部分と分離して処分できないか？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow down with the label " + q("はい") + " to RESULT 1.",
            "  - Arrow right with the label " + q("いいえ") + " to RESULT 3.",
            "NODE RESULT 1 (white box, blue outline): " + q("敷地権になる"),
            "NODE RESULT 2 (white box, red outline): " + q("敷地権にならない") + " on the first line and " + q("使用借権は登記できない") + " on the second line.",
            "NODE RESULT 3 (white box, red outline): " + q("敷地権にならない") + " on the first line and " + q("規約に別段の定めがある") + " on the second line.",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The first line of RESULT 2 and RESULT 3 is the same string on purpose; their second lines differ.",
            "Under the flowchart, two small light-gray tags side by side: " + q("共有の持分でも、敷地権になる") + " and " + q("所有権・地上権・賃借権は登記できる") + "."]
    return finish(body, "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that the arrows pointing to the right result boxes are red with the label いいえ and the arrows pointing down are blue with the label はい, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解4：規約敷地（PG1-3）
def img4():
    cards = [
        ("規約敷地とは", "An apartment building and, next to it, a garden-and-parking land plot joined to it by a small paper tag labeled " + q("規約") + ".", "一体として管理・使用する土地"),
        ("他の建物の敷地でもよい", "One land plot overlapped by the outlines of two different apartment building icons, with no text on the buildings.", "妨げにならない"),
        ("規約の決め方", "A meeting table with several person pictograms seated, all in the same single light gray-blue color, and a small white card labeled " + q("出席は各過半数") + ".", "賛成は出席者の各4分の3以上"),
    ]
    return card_poster("1080x1900", "規約敷地とは何か", "決め方と、他の建物の敷地との関係", "区分所有法 第5条・第31条", cards)

# ============================================================ 図解5：区分建物の表題登記の申請（PG1-4）
def img5():
    cards = [
        ("一棟の全部を併せて申請", "An apartment building icon whose rooms are bound together by one ribbon labeled " + q("併せて") + ".", "敷地権の有無を問わない"),
        ("他の所有者に代わって申請できる", "Two person pictograms in the same single light gray-blue color, one handing a document sheet to the other.", "他の区分建物の所有者に代わって"),
        ("規約で敷地権にならないとき", "A land plot with a dashed outline and a document sheet labeled " + q("別段の定め") + ".", "その事由を証する情報"),
    ]
    return card_poster("1080x1900", "区分建物の表題登記", "申請のルールは3つ", "不動産登記法 第48条・不動産登記令 別表十二の項", cards)

# ============================================================ 図解6：専有部分の記録の言い方（PG1-5）
def img6():
    rows = [("専有部分の構造", "平家建", "1階建"),
            ("専有部分の床面積", "1階", "1階部分"),
            ("敷地権の最初の原因", "新築", "敷地権")]
    return table_poster("1080x1700", "専有部分の記録の言い方", "つい引かれる言い方に注意", "階層で区分した専有部分（登記実務の取扱い）",
                        ["欄", "つい引かれる言い方", "区分建物の欄の記録"], rows,
                        "Highlighting: every cell of column 3 has a pale yellow highlighter marker. Copy each cell exactly as given.",
                        "一棟の建物や隣の行の言い方を、そのまま写さない")

# ============================================================ 図解7：敷地権の原因の言い方（PG1-5）
def img7():
    rows = [("最初に敷地権が生じた", "年月日敷地権", "新築"),
            ("区分で割合が変わった", "年月日変更", "分割"),
            ("地上権の期間満了で消えた", "年月日敷地権消滅", "非敷地権"),
            ("規約で分離処分可能になった", "年月日非敷地権", "敷地権消滅")]
    return table_poster("1080x1900", "敷地権の原因の言い方", "できごとごとに決まっている", "区分建物の登記記録（登記実務の取扱い）",
                        ["できごと", "原因の書き方", "混ぜやすい言い方"], rows,
                        "Highlighting: every cell of column 2 has a pale yellow highlighter marker. The strings in rows 3 and 4 of columns 2 and 3 (「年月日敷地権消滅」, 「年月日非敷地権」, 「非敷地権」, 「敷地権消滅」) are similar but different; copy each exactly as given and do not swap them.",
                        "消える2つは、書き分ける")

# ============================================================ 図解8：原因の日付（判定の流れ。PG1-5）
def img8():
    body = [lead("1080x1800", "This is a flowchart poster (判定の流れ図)."), TEXTREQ, BGREQ, COLOR] + \
           header("敷地権の日付は、いつ？", "新築より前か、あとか", "登記原因の日付（登記実務の取扱い）") + \
           ["--- FLOWCHART ---",
            "Layout: START at the top center. DIAMOND 1 below START at the center. From DIAMOND 1 two arrows go down, one to the lower left and one to the lower right. RESULT 1 sits at the lower left and RESULT 2 at the lower right, side by side, each about 380 px wide, with at least 60 px of empty space above it so that the arrow labels stay visible. All arrows are straight and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("敷地権の登記原因の日付を決める"),
            "NODE DIAMOND 1: " + q("区分建物が生じる前から、敷地の登記した権利を持っていたか？") + " The text is placed inside the diamond on 4 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down-left with the label " + q("はい") + " to RESULT 1.",
            "  - Arrow down-right with the label " + q("いいえ") + " to RESULT 2.",
            "NODE RESULT 1 (white box, blue outline): " + q("区分建物が生じた日") + " on the first line and " + q("新築の日・区分した日など") + " on the second line.",
            "NODE RESULT 2 (white box, red outline): " + q("所有権取得の登記の日") + " on the first line and " + q("新築のあとに取得して登記したとき") + " on the second line.",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box.",
            "Under the flowchart, one small light-gray tag centered: " + q("条文に明記はなく、登記実務の取扱い")]
    return finish(body, "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the arrow to the left box is blue with the label はい and the arrow to the right box is red with the label いいえ, that no text overflows its box, and that no arrow label is hidden.")

# ============================================================ 図解9：敷地権の旨の登記と制限（PG1-6）
def img9():
    rows = [("敷地権の移転、敷地権を目的とする担保権の登記（土地）", "原則できない", "法73条2項"),
            ("建物のみの所有権の移転、建物のみを目的とする担保権の登記", "原則できない", "法73条3項"),
            ("合筆の登記（土地）", "できない", "法41条6号"),
            ("地目の変更の登記（土地）", "抹消せずにできる", "表示に関する登記")]
    return table_poster("1080x2000", "敷地権の旨の登記と制限", "できること・できないこと", "不動産登記法 第46条・第73条・第41条",
                        ["登記", "できるか", "根拠・理由"], rows,
                        "Highlighting: the string 「抹消せずにできる」 of row 4 has a pale yellow highlighter marker; the other cells of column 2 are plain. Copy each cell exactly as given.",
                        "処分と合筆は制限される。地目の変更は制限されない",
                        top_band="敷地権である旨の登記は、登記官が職権でする（法46条）")

# ============================================================ 図解10：敷地権が生じたときの申請（PG1-7）
def img10():
    steps = [("敷地権が生じる", ["規約で土地が建物の敷地になった、など"], None),
             ("建物と土地の名義人の住所を見比べる", ["違えば、先に住所の変更又は更正の登記"], "登記実務の取扱い"),
             ("変更から1か月以内に申請", ["敷地権の発生を原因とする表題部の変更の登記"], "法51条1項")]
    sides = [("区分合併で、非区分建物になるとき", "敷地権の抹消は、登記官が職権でする", "規則134条3項"),
             ("分離処分可能規約", "一部の区分建物だけについても、定められる", None)]
    return steps_poster("1080x2500", "敷地権が生じたときの申請", "住所をそろえて、1か月以内に", "不動産登記法 第51条・不動産登記規則 第134条", steps, sides)

# ============================================================ 図解11：敷地権に関する添付情報（PG1-8）
def img11():
    rows = [("敷地権付き区分建物どうしの合体（割合を合算するだけ）", "要らない（令別表十三の項ヘのかっこ書）"),
            ("規約敷地の分筆", "要らない（令別表八の項に挙がっていない）")]
    body = [lead("1080x2300", "This is a comparison poster: two list cards at the top and a table below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("敷地権の添付情報", "生じるときと消えるとき", "不動産登記令 別表十五の項・十三の項・八の項") + \
           [f"--- TWO LIST CARDS (side by side, {CARD_FILL}, each with exactly three rows; each row has a small dark navy dot at its left end, NO digit and NO letter on the dots) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("敷地権が生じるとき") + ", with a small tag " + q("令別表十五の項") + ". The three rows, in this order: " + q("規約敷地の規約を設定したことを証する情報") + ", " + q("割合の規約を設定したことを証する情報") + ", " + q("他の登記所の土地の登記事項証明書") + ".",
            "Right card: heading bar (pale gray fill, dark navy text) " + q("敷地権が消えるとき") + ", with a small tag " + q("令別表十五の項") + ". The three rows, in this order: " + q("規約を廃止したことを証する情報") + ", " + q("別段の定めなど、その他の事由を証する情報") + ", " + q("登記事項証明書は、要らない") + ".",
            "Highlighting: the right-card row 3 " + q("登記事項証明書は、要らない") + " has a pale yellow highlighter marker. The two cards have clearly different texts; the texts are NOT identical."] + \
           table_block(["場面", "規約を証する情報"], rows,
                       "Highlighting: the string 「要らない」 inside each of the two column-2 cells has a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           ["Under the table, one wide dark navy band with large white text " + q("登記事項証明書と割合の規約は、生じるときの添付情報") + "."]
    return finish(body, "Confirm there are exactly two list cards with exactly three rows each, that the left card holds the three items for 敷地権が生じるとき and the right card holds the three items for 敷地権が消えるとき, that the table has exactly 2 columns and exactly 2 data rows, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解12：敷地権が消えるとき抵当権はどうなる（PG1-9）
def img12():
    steps = [("分離処分できることになる", ["敷地権の変更の登記をする"], None),
             ("抵当権者の承諾情報を併せて提供", ["権利を消滅させることを承諾したことを証する情報"], None),
             ("登記官が、消滅した旨を登記", ["承諾に係る建物又は土地について"], "法55条1項")]
    sides = [("敷地のみの抵当権は、別扱い", "特定登記ではないので、同じ扱いにならない", "特定登記の定義からの整理")]
    return steps_poster("1080x2300", "敷地権が消えるとき", "抵当権はどうなる？", "不動産登記法 第55条第1項", steps, sides,
                        top_band="特定登記＝建物の抵当権で、敷地権にも及ぶもの")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "敷地権の一生（生じて、載って、消えるまで）", "カードポスター型（手順）", "1080×2500", "不登法8章_図解1_敷地権の一生", "「この章の論点」の一覧の直後", img1, "00_zentai"),
    (2, "区分建物に入る部分は？（専有部分と共用部分の線引き）", "対比カード＋表型", "1080×2000", "不登法8章_図解2_区分建物に入る部分", "【PG1-1】「中身の整理」の直後", img2, "PG1-1"),
    (3, "敷地権になれるか（判定の流れ）", "フローチャート型", "1080×2000", "不登法8章_図解3_敷地権になれるか", "【PG1-2】「中身の整理」の直後", img3, "PG1-2"),
    (4, "規約敷地とは何か（決め方と他の建物の敷地との関係）", "カードポスター型", "1080×1900", "不登法8章_図解4_規約敷地とは", "【PG1-3】「中身の整理」の直後", img4, "PG1-3"),
    (5, "区分建物の表題登記（申請のルールは3つ）", "カードポスター型", "1080×1900", "不登法8章_図解5_区分建物の表題登記", "【PG1-4】「中身の整理」の直後", img5, "PG1-4"),
    (6, "専有部分の記録の言い方（つい引かれる言い方に注意）", "対比表型（3列）", "1080×1700", "不登法8章_図解6_専有部分の記録の言い方", "【PG1-5】「中身の整理」の階数・床面積の箇所の直後", img6, "PG1-5"),
    (7, "敷地権の原因の言い方（できごとごとに決まっている）", "早見表型（3列）", "1080×1900", "不登法8章_図解7_敷地権の原因の言い方", "【PG1-5】「中身の整理」の原因の文言の箇所の直後（図解6の後）", img7, "PG1-5"),
    (8, "敷地権の日付は、いつ？（判定の流れ）", "フローチャート型", "1080×1800", "不登法8章_図解8_敷地権の日付", "【PG1-5】「たとえば」の直後", img8, "PG1-5"),
    (9, "敷地権の旨の登記と制限（できること・できないこと）", "早見表型（3列）", "1080×2000", "不登法8章_図解9_敷地権の旨の登記と制限", "【PG1-6】「中身の整理」の直後", img9, "PG1-6"),
    (10, "敷地権が生じたときの申請（住所をそろえて1か月以内に）", "ステップ型", "1080×2500", "不登法8章_図解10_敷地権が生じたときの申請", "【PG1-7】「中身の整理」の直後", img10, "PG1-7"),
    (11, "敷地権の添付情報（生じるときと消えるとき）", "対比カード＋表型", "1080×2300", "不登法8章_図解11_敷地権の添付情報", "【PG1-8】「中身の整理」の直後", img11, "PG1-8"),
    (12, "敷地権が消えるとき抵当権はどうなる？", "ステップ型", "1080×2300", "不登法8章_図解12_抵当権はどうなる", "【PG1-9】「中身の整理」の直後", img12, "PG1-9"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PG1-1": ("prompt_infographic_PG1-1.md", "【PG1-1】区分建物とは何か"),
    "PG1-2": ("prompt_infographic_PG1-2.md", "【PG1-2】何が敷地権になるのか"),
    "PG1-3": ("prompt_infographic_PG1-3.md", "【PG1-3】規約敷地とは何か"),
    "PG1-4": ("prompt_infographic_PG1-4.md", "【PG1-4】区分建物の表題登記の申請"),
    "PG1-5": ("prompt_infographic_PG1-5.md", "【PG1-5】敷地権付き区分建物の登記記録の書き方"),
    "PG1-6": ("prompt_infographic_PG1-6.md", "【PG1-6】敷地権である旨の登記と制限"),
    "PG1-7": ("prompt_infographic_PG1-7.md", "【PG1-7】敷地権の発生・消滅の変更登記の申請"),
    "PG1-8": ("prompt_infographic_PG1-8.md", "【PG1-8】敷地権に関する添付情報"),
    "PG1-9": ("prompt_infographic_PG1-9.md", "【PG1-9】敷地権が消えるとき抵当権はどうなるか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第8章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第8章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch8.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "分類・列挙が中心の図解（カードポスター・表・ステップ）は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
               "判定の流れ図（フローチャート）だけは、はい＝青・いいえ＝赤の配色です。"
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
