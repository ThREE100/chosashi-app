#!/usr/bin/env python3
"""総合記事②不動産登記法編 第3章：図解インフォグラフィック18枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch3/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PC-1.md ／ … ／ _PC-12.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。
配色：分類中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描く（NOCOLOR）。はい／いいえの流れ図だけ、はい＝青・いいえ＝赤（COLOR）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
ROWFMT = "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font."
CARDS_REQ = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. "
             "Every card communicates its point through the illustration plus one short heading, short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.")


def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]


def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)


def table_block(cols, rows, note=""):
    n = len(cols)
    colnames = " | ".join(f"column {i}" for i in range(1, n + 1))
    out = ["--- TABLE ---",
           f"{ROWFMT} Exactly {n} columns and exactly {len(rows)} data rows, no merged cells.",
           "Header row (dark navy cells with white text): " + ", ".join(q(c) for c in cols) + ".",
           f"Data rows, one per line, in this order ({colnames}):"]
    out += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    if note:
        out.append(note)
    return out


def band(text):
    return "Under the table, one wide dark navy band with large white text " + q(text) + "."


def card_poster(size, kind, t1, t2, sub, cards, n_expect):
    """カードを1列に並べるポスター。cards = (見出し, イラストの指示, [項目の行], 結論タグ)。"""
    body = [lead(size, kind), CARDS_REQ, TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub)
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, f"Confirm the number of cards equals {n_expect} exactly, numbered 1 to {n_expect} in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")


def steps_poster(size, t1, t2, sub, steps, side_note=None, band_text=None):
    """縦に積むステップカード。steps = (見出し, 本文[, 見出しにマーカー=True])。"""
    n = len(steps)
    body = [lead(size, f"This is a vertical step poster with {n} step cards" + (" and one side note card." if side_note else (" and one closing band." if band_text else "."))), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub) + \
           ["--- STEPS ---",
            f"Layout: {n} step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to {n} in order), one bold heading line, and one body line."]
    for i, s in enumerate(steps, 1):
        mark = " (the card has a pale yellow highlighter marker on its heading)" if len(s) > 2 and s[2] else ""
        body.append(f"STEP {i}{mark}: heading " + q(s[0]) + ", body " + q(s[1]) + ".")
    if side_note:
        body += ["--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---", "Heading " + q(side_note[0]) + ", body " + q(side_note[1]) + "."]
    if band_text:
        body.append("Under the steps, one wide dark navy band with large white text " + q(band_text) + ".")
    return finish(body, f"Confirm there are exactly {n} step cards numbered 1 to {n} in order" + (", followed by exactly one side note card" if side_note else "") + ", that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")


def timeline_poster(size, t1, t2, sub, stages, comp):
    """時間の流れ。stages = (バッジ, 見出し, [本文の行], 下の黄色い帯 or None)。comp = (見出し, [本文の行])。"""
    n = len(stages)
    body = [lead(size, f"This is a vertical timeline poster with {n} stage cards and one comparison card."), TEXTREQ, BGREQ, NOCOLOR] + header(t1, t2, sub) + \
           ["--- TIMELINE ---",
            f"Layout: one vertical center line down the middle of the canvas; {n} stage cards are placed top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each stage card has a dark navy badge with its stage name at the top left, one heading line, and one or two short body lines."]
    for i, (badge, h, bl, bn) in enumerate(stages, 1):
        s = f"STAGE CARD {i}: badge " + q(badge) + ", heading " + q(h) + ", body " + " and ".join(q(b) for b in bl) + "."
        if bn:
            s += " Under the card, a pale yellow banner " + q(bn) + "."
        body.append(s)
    body += ["--- COMPARISON CARD (below the timeline, a wide card with a dashed dark navy outline and a small dark navy tag " + q("比べると") + ") ---",
             "Heading " + q(comp[0]) + ", body " + " and ".join(q(b) for b in comp[1]) + "."]
    return finish(body, f"Confirm there are exactly {n} stage cards in the timeline in the given order, followed by exactly one comparison card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解1：全体（5つの場面）
def img1():
    cards = [
        ("地目・地積・地番の登記", "A land plot icon split by a boundary line into two plots, with a small calendar and a registry ledger beside it, no text on the ledger.",
         ["地目は、用途で一筆に一つ", "変更は、名義人が1か月以内"], "土地の表題・変更・分筆合筆"),
        ("地図の訂正の申出", "A cadastral map sheet with a pencil and a small document sheet beside it.",
         ["申出人は、名義人・一般承継人", "区画・地番ごとに、別の申出"], "申出人と方式"),
        ("地積測量図", "A survey drawing sheet with a ruler and a small folder icon.",
         ["誤りは、訂正の申出か更正", "閉鎖される場合は決まっている"], "訂正・閉鎖・記録事項"),
        ("公図の沿革", "An old rolled map sheet with a small tax-office building icon beside it.",
         ["改租図は、地租改正のときの図", "附属地図の保管先は、税務署"], "歴史と保管先"),
        ("筆界特定", "Two plots of land with a boundary line between them and a small stake, with a person pictogram holding a form.",
         ["申請人は、所有権登記名義人等", "却下には審査請求ができる"], "申請・却下・公開"),
    ]
    return card_poster("1080x2900", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document.",
                       "土地の表示と地図の手続", "5つの場面で整理する", "地目・地積・地図・地積測量図・筆界特定", cards, 5)


# ============================================================ 図解2：水に関わる土地の地目
def img2():
    rows = [
        ("耕地かんがい用の用水貯留池", "ため池", "準則68条17号"),
        ("かんがい用水でない水の貯留池", "池沼", "準則68条8号"),
        ("かんがい用又は悪水排せつ用の水路", "用悪水路", "準則68条16号"),
        ("水力発電のための水路又は排水路", "雑種地", "準則69条5号"),
    ]
    body = [lead("1080x1700", "This is a reference table poster with three columns (対比表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("水に関わる土地の地目", "ため池・池沼・用悪水路・雑種地", "不動産登記事務取扱手続準則 第68条・第69条") + \
           table_block(["土地の状況", "地目", "根拠"], rows,
                       "Highlighting: the strings 「ため池」 of row 1, 「池沼」 of row 2 and 「雑種地」 of row 4 have a pale yellow highlighter marker. Rows 1 and 2 have similar wording in column 1 but different meanings; copy each cell exactly as given and do not change one into the other.") + \
           [band("同じ水の土地でも、かんがい用かどうかと用途で地目が分かれる")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that row 1 reads ため池 and row 2 reads 池沼 in column 2, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解3：地目を決める順番
def img3():
    steps = [("土地全体の主な用途を見る", "わずかな差異があっても、全体で一つに決める", True),
             ("水に関わるなら、かんがい用か見る", "貯留池は、かんがい用ならため池、でなければ池沼。発電用の水路は雑種地"),
             ("建物が附随的か見る", "遊園地・ゴルフ場などで附随的なら、全体を一団の雑種地")]
    return steps_poster("1080x2000", "地目を決める順番", "土地全体の用途から考える", "不動産登記規則 第99条・準則 第68条・第69条", steps,
                        band_text="畑・雑種地のような複合地目は付けられない")


# ============================================================ 図解4：地目・地積の変更の起算点
def img4():
    stages = [("変更", "山林を切り開いて宅地にした", ["造成したのが地上権者や賃借人でも同じ"], None),
              ("1項", "変更当時の名義人", ["変更のあった日から1か月以内", "申請するのは、所有権の登記名義人（表題部所有者）"], None),
              ("2項", "変更の後に名義人になった人", ["自分の所有権の登記があった日から1か月以内"], "売買の日（取得の日）ではない")]
    comp = ("地積の変更の登記を併せる義務", ["地目変更の登記に併せて申請する義務の条文はない", "登記実務上の取扱いによる整理"])
    return timeline_poster("1080x2300", "地目・地積の変更登記", "誰が、いつから1か月？", "不動産登記法 第37条", stages, comp)


# ============================================================ 図解5：建物の表題部の変更登記
def img5():
    rows = [
        ("1項", "変更当時の名義人（共用部分の登記がある建物では所有者）", "変更のあった日"),
        ("2項", "変更の後に名義人になった人", "その人の所有権の登記があった日"),
        ("3項", "変更の後に共用部分である旨の登記があったときの所有者（1項・2項の人を除く）", "共用部分である旨の登記がされた日"),
        ("4項", "共用部分の登記がある建物で、変更の後に所有権を取得した人（3項の人を除く）", "所有権の取得の日"),
    ]
    body = [lead("1080x2200", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("建物の表題部の変更登記", "1か月の起算点は4通り", "不動産登記法 第51条・第44条") + \
           table_block(["項", "申請する人", "1か月の起算点"], rows,
                       "Highlighting: the string 「変更のあった日」 of row 1 and the string 「所有権の取得の日」 of row 4 have a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           ["Under the table, one wide card with a dashed dark navy outline: heading " + q("共用部分の登記がされても") + ", body " + q("1項の人の1か月は、変更の日から数え直さない") + ".",
            "Under that card, one wide dark navy band with large white text " + q("対象外は、家屋番号（2号）と共用部分である旨（6号）だけ") + ", and under the band one small light-gray tag " + q("所在（1号）や敷地権（9号）の変更は対象") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 4 data rows labeled 1項 to 4項 in order, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解6：土地の状況が変わったとき
def img6():
    rows = [
        ("一筆の一部が常時海面下に没した", "地積に関する変更の登記を申請する", "法37条1項"),
        ("一筆の全部が海面下に没して滅失した", "滅失の日から1か月以内に滅失の登記を申請する", "法42条"),
        ("土地が河川区域内の土地になった", "河川管理者が、その旨の登記を嘱託する", "法43条2項"),
        ("地目の変更の登記を申請するとき", "河川区域内の登記の抹消を経なくても申請できる", "前提とする規定はない"),
        ("電子申請で署名用電子証明書を提供した", "現在の住所を証する情報の提供に代えられる", "規則44条1項"),
    ]
    body = [lead("1080x2100", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("土地の状況が変わったとき", "登記の目的と、添える情報", "不動産登記法 第37条・第42条・第43条") + \
           table_block(["場面", "結論", "根拠"], rows,
                       "Highlighting: the strings 「地積に関する変更の登記」 of row 1 and 「滅失の登記」 of row 2 have a pale yellow highlighter marker. Rows 1 and 2 differ in the scope of the sinking (part or whole); copy each cell exactly as given and do not change one into the other.") + \
           [band("一部なら地積の変更、全部なら滅失。河川区域は管理者の嘱託")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that row 1 says 一部 and row 2 says 全部, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解7：分筆・合筆の地番
def img7():
    rows = [
        ("分筆", "支号のない土地は、分筆前の地番に支号を付ける（4号）", "要役地の地役権を消す分筆では、支号のない地番を残せる（5号）。どの土地に残すかは定めがない"),
        ("合筆", "合筆前の首位の地番にする（6号）", "特別の事情があれば、適宜の地番を定めてよい（7号）"),
    ]
    body = [lead("1080x1800", "This is a reference table poster with three columns (原則と例外)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("分筆・合筆の地番", "原則と、例外", "不動産登記事務取扱手続準則 第67条") + \
           table_block(["登記", "原則", "例外"], rows,
                       "Highlighting: the strings 「支号のない地番を残せる」 of row 1 and 「適宜の地番」 of row 2 have a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           [band("地役権を消す分筆と、特別の事情があるときは、例外を疑う")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 2 data rows (分筆 and 合筆), that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解8：合筆できない場合
def img8():
    rows = [
        ("1号", "相互に接続していない土地", "隣り合っているか"),
        ("2号", "地目又は地番区域が相互に異なる土地", "地目・地番区域が同じか"),
        ("3号", "表題部所有者又は所有権の登記名義人が相互に異なる土地", "名義人が同じか"),
        ("4号", "名義人が相互に持分を異にする土地", "持分が同じか"),
        ("5号", "所有権の登記がない土地と、所有権の登記がある土地", "所有権の登記の有無がそろうか"),
        ("6号", "所有権の登記以外の権利に関する登記がある土地（省令で定める例外を除く）", "権利に関する登記がないか"),
    ]
    body = [lead("1080x2300", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合筆できない6つの場合", "順に確かめる", "不動産登記法 第41条") + \
           table_block(["号", "合筆の登記ができない土地", "確かめること"], rows,
                       "Highlighting: the whole row 2 has a pale yellow highlighter marker. Copy each cell exactly as given.") + \
           [band("接続・地目・名義人・持分・権利の登記を順に確かめる"),
            "Under the band, one small light-gray tag centered: " + q("接続し名義人が同じでも、宅地と山林は2号で合筆できない")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 6 data rows labeled 1号 to 6号 in order, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解9：地図の訂正の申出
def img9():
    body = [lead("1080x2200", "This is a comparison poster with two side-by-side cards and one wide card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("地図の訂正の申出", "誰が、どこまでできる？", "不動産登記規則 第16条") + \
           ["Under the header, one wide pale yellow band with dark navy text " + q("対象は、地図の区画・地番（地図に準ずる図面は位置・形状・地番）の誤り") + ".",
            "--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("規則16条1項") + ", heading " + q("申出ができる人") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("表題部所有者") + ", " + q("所有権の登記名義人") + ", " + q("その相続人その他の一般承継人") + ".",
            "Right card: small tag " + q("申出の対象外") + ", heading " + q("申出ができない場合") + ", and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("人：移転登記を受ける前の買主") + ", " + q("事柄：地番を付け替える合意") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- WIDE CARD (below the two cards, a wide card with a dashed dark navy outline) ---",
            "Small tag " + q("規則16条15項") + ", heading " + q("登記官は、職権でも訂正できる") + ", body " + q("申出がなくても、誤りがあると認めたとき") + "."]
    return finish(body, "Confirm there are exactly two cards with exactly three item lines in the left card and exactly two item lines in the right card, followed by one wide card, that the two card headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解10：登記の申請と地図訂正の申出
def img10():
    rows = [
        ("一の情報にまとめる", "同じ不動産の表題部の変更・更正が二以上なら、一の申請情報でできる（規則35条6号）", "区画の訂正と地番の訂正、隣接する2筆の区画の訂正は、別々の申出"),
        ("書面で記名押印したとき", "記名押印した者の印鑑に関する証明書を添える（令16条2項。省令で定める場合を除く）", "署名又は記名押印はするが、印鑑証明書は不要（令16条2項は準用されない）"),
        ("たとえば", "地目変更と地積更正は、一の申請情報でできる", "甲土地と乙土地の区画なら2件。区画と地番も2件"),
    ]
    body = [lead("1080x2200", "This is a comparison table poster with three columns (対比表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登記の申請と地図訂正の申出", "まとめられる？印鑑証明書は？", "不動産登記規則 第16条・第35条・令 第16条") + \
           table_block(["項目", "登記の申請", "地図訂正の申出"], rows,
                       "Highlighting: the strings 「別々の申出」 of row 1 and 「印鑑証明書は不要」 of row 2 in column 3 have a pale yellow highlighter marker. Columns 2 and 3 have clearly different texts in every row; copy each cell exactly as given.") + \
           [band("申請の感覚を、申出に持ち込まない")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解11：地積測量図の誤りの直し方（流れ図）
def img11():
    body = [lead("1080x2500", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("地積測量図の誤りの直し方", "上から順に確かめる", "不動産登記規則 第88条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit side by side below DIAMOND 1, one to the left and one to the right of the center line, with at least 60 px of empty space between them so that the arrow labels stay visible. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("地積測量図に誤りがある"),
            "NODE DIAMOND 1: " + q("表題部の更正の登記ができる誤りか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down-left to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down-right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("更正の登記で直す") + " on the first line and " + q("訂正の申出はできない") + " on the second line, with the small gray tag " + q("規則88条1項ただし書") + ".",
            "NODE RESULT 2 (red box): " + q("訂正の申出で直す") + " on the first line and " + q("訂正後の図面を提供する") + " on the second line, with the small gray tag " + q("規則88条2項") + ".",
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two result boxes have different texts; do not copy one into the other.",
            "--- COMPARISON CARD (below the flowchart, a wide card with a dashed dark navy outline and a small dark navy tag " + q("地積に錯誤があるとき") + ") ---",
            "Heading " + q("更正の登記と併せて申し出るか") + ", then two body lines: " + q("地図の訂正の申出：併せて申し出る（規則16条2項）") + " and " + q("地積測量図の訂正の申出：併せる義務はない（規則88条3項で準用されない）") + ". Neutral dark navy outlines only; no blue and no red in this card."]
    return finish(body, "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is blue and RESULT 2 is red, that the comparison card below is neutral dark navy, that no text overflows its box, and that no arrow label is hidden.")


# ============================================================ 図解12：図面が閉鎖されるとき
def img12():
    body = [lead("1080x2100", "This is a comparison poster with two side-by-side cards and one wide band."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("図面が閉鎖されるとき", "限られた場合だけ", "不動産登記規則 第85条・第87条") + \
           ["--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("規則85条2項") + ", heading " + q("土地所在図・地積測量図・建物図面・各階平面図") + ", and exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("変更後・更正後の図面がある変更の登記・更正の登記をしたとき") + ", " + q("滅失の登記・表題部の抹消をしたとき") + ", " + q("換地処分の登記をしたとき") + ".",
            "Right card: small tag " + q("規則87条1項") + ", heading " + q("地役権図面") + ", and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("地役権の登記の抹消をしたとき") + ", " + q("地役権図面を添付情報とする分筆・合筆・変更・更正の登記をしたとき") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("合筆の登記だけでは、地積測量図は閉鎖されない") + "."]
    return finish(body, "Confirm there are exactly two cards with exactly three item lines in the left card and exactly two item lines in the right card, followed by one band, that the two card headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解13：地積測量図の記録事項
def img13():
    rows = [
        ("1号", "地番区域の名称", "省略の対象外"),
        ("2号", "方位", "省略の対象外"),
        ("3号", "縮尺", "省略の対象外"),
        ("4号", "地番（隣接地の地番を含む）", "省略の対象外"),
        ("5号", "地積及びその求積方法", "求積方法だけ省略できる"),
        ("6号", "筆界点間の距離", "省略できる"),
        ("7号", "平面直角座標系の番号又は記号", "省略できる"),
        ("8号", "基本三角点等に基づく測量の成果による筆界点の座標値", "省略できる"),
        ("9号", "境界標があるときは、その表示", "省略の対象外"),
        ("10号", "測量の年月日", "省略の対象外"),
    ]
    body = [lead("1080x2500", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("地積測量図の記録事項", "分筆で省略できるのは4つ", "不動産登記規則 第77条・準則 第72条") + \
           table_block(["号", "記録事項", "分筆の便宜省略"], rows,
                       "Highlighting: the cell 「方位」 of row 2 and the cell 「地積及びその求積方法」 of row 5 have a pale yellow highlighter marker. The cells 「省略できる」 and 「省略の対象外」 differ in wording; copy each exactly as given and do not change one into the other.") + \
           [band("省略できるのは、特別の事情があるとき、分筆後の1筆だけ"),
            "Under the band, one small light-gray tag centered: " + q("座標値を記録しても、方位は省略できない")]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 10 data rows labeled 1号 to 10号 in order, that rows 5, 6, 7 and 8 are the only rows whose third cell contains 省略できる, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解14：精度区分・署名押印・座標値
def img14():
    cards = [
        ("精度区分は、土地の地域で決まる", "A map sheet with three small zone icons in a row (houses, farmland, mountains), no text on the icons.",
         ["市街地地域：甲二まで", "村落・農耕地域：乙一まで", "山林・原野地域：乙三まで"], "地域で決まる。区分は上限"),
        ("地積測量図の作成者", "A drawing sheet with a pen signing in the corner and a small rubber stamp beside it, no text on the sheet.",
         ["署名するか、記名して押印する"], "署名すれば押印は不要"),
        ("電磁的記録に記録する地図", "A computer screen icon showing a map with small dots on the corners of the plots, no text on the screen.",
         ["各筆界点の座標値を記録する"], "座標値の記録"),
    ]
    return card_poster("1080x2300", "This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document.",
                       "地積測量図と地図の約束ごと", "精度・署名・座標値", "不動産登記規則 第10条・第13条・第74条・第77条", cards, 3)


# ============================================================ 図解15：公図の沿革
def img15():
    stages = [("明治初期", "地租改正", ["地租改正のときの図が改租図"], None),
              ("地押調査", "更正図等が作られた", ["正本は土地台帳附属地図として税務署が保管"], None),
              ("昭和25年", "登記所へ移管", ["土地台帳・家屋台帳とともに移された"], None),
              ("平成5年", "地図に準ずる図面", ["法律上の根拠を持つに至った"], None)]
    comp = ("保管先を取り違えない", ["市町村役場ではなく、税務署", "土地台帳は、税のための台帳だった"])
    return timeline_poster("1080x2600", "公図の沿革", "改租図から地図に準ずる図面まで", "土地台帳附属地図の保管先は税務署", stages, comp)


# ============================================================ 図解16：筆界特定の申請人
def img16():
    rows = [
        ("所有権の登記がある土地の所有権の登記名義人", "登記記録で確認できる", "法123条5号"),
        ("所有権の登記がない一筆の土地の表題部所有者", "登記記録で確認できる", "法123条5号"),
        ("表題登記がない土地の所有者", "所有権を有することを証する情報", "規則209条1項4号"),
        ("一筆の土地の一部の所有権を取得した人", "その旨を申請情報に書き、取得を証する情報を添える", "規則207条2項4号・209条1項5号"),
    ]
    body = [lead("1080x2300", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("筆界特定の申請", "誰が、何を添えるか", "不動産登記法 第131条・規則 第207条・第209条") + \
           table_block(["申請する人", "必要な情報", "根拠"], rows,
                       "Highlighting: the cell 「所有権を有することを証する情報」 of row 3 has a pale yellow highlighter marker. Rows 1 and 2 have the same text in column 2 on purpose; draw the same string in both. Every other cell has its own text exactly as given.") + \
           ["Under the table, one wide card with a dashed dark navy outline: heading " + q("一部を取得した人が、取得した部分以外の筆界を申請しても") + ", body " + q("却下の理由にならない") + ".",
            "Under that card, one wide dark navy band with large white text " + q("土地の状況は、図面を利用する等の方法で示せば足りる") + ", and under the band one small light-gray tag " + q("図面に限られない（規則207条4項）") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")


# ============================================================ 図解17：筆界特定の申請は却下される？（流れ図）
def img17():
    body = [lead("1080x2700", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("筆界特定の申請は却下される？", "特定済みの筆界を、再び申請", "不動産登記法 第132条・第156条・第158条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The YES result box of DIAMOND 2 sits at the bottom, to the left of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("筆界特定を申請する"),
            "NODE DIAMOND 1: " + q("その筆界は、既に筆界特定がされているか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("この理由では、却下されない") + " on the first line and " + q("ほかの却下事由は別に確かめる") + " on the second line.",
            "NODE DIAMOND 2: " + q("更に筆界特定をする、特段の必要があるか？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow down-left to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box): " + q("却下されない") + " on the first line and " + q("法132条1項7号ただし書") + " on the second line.",
            "NODE RESULT 3 (red box): " + q("却下される") + " on the first line and " + q("法132条1項7号") + " on the second line.",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The result boxes have different texts; do not copy one into another.",
            "--- SIDE NOTE CARD (below the flowchart, a wide card with a dashed dark navy outline and a small dark navy tag " + q("却下されたあと") + ") ---",
            "Three body lines, neutral dark navy outlines only (no blue and no red in this card): " + q("却下は、登記官の処分とみなされる（法132条2項）") + ", " + q("法務局又は地方法務局の長に審査請求ができる（法156条1項）") + ", " + q("審査請求の期間の制限はない（法158条）") + "."]
    return finish(body, "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 2 is blue and RESULT 1 and RESULT 3 are red, that the side note card below is neutral dark navy, that no text overflows its box, and that no arrow label is hidden.")


# ============================================================ 図解18：筆界特定の手続の相手と主体
def img18():
    cards = [
        ("立入調査の通知先", "A person pictogram standing at a garden gate with the name tag " + q("占有者") + " and a small notice sheet in front of the gate.",
         ["あらかじめ、日時と場所を通知", "通知の相手は、土地の占有者", "名義人に通知する規定はない"], "占有者"),
        ("筆界特定書の写し", "A document sheet with a row of three plain person pictograms in front of it, each holding a small coin icon, no text on the document.",
         ["手数料を納付して請求する", "請求できるのは、何人も"], "何人も"),
        ("却下への不服", "A decision sheet with a rubber stamp, and an arrow-free small building icon beside it with the tag " + q("法務局") + ".",
         ["却下された申請人が審査請求できる", "宛先は、法務局又は地方法務局の長"], "審査請求"),
    ]
    return card_poster("1080x2300", "This is a quick-reference poster with three numbered cards in one column; it is NOT a text-heavy document.",
                       "筆界特定の手続の相手と主体", "誰に通知し、誰が請求するか", "不動産登記法 第137条・第149条・第156条", cards, 3)


# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "土地の表示と地図の手続（5つの場面）", "カードポスター型（俯瞰）", "1080×2900", "不登法第3章_図解1_土地の表示と地図の手続", "『この章の誤りの傾向』の段落の直後", img1, "00_zentai"),
    (2, "水に関わる土地の地目（ため池・池沼・用悪水路・雑種地）", "早見表型（3列）", "1080×1700", "不登法第3章_図解2_水に関わる土地の地目", "【PC-1】『中身の整理』の直後", img2, "PC-1"),
    (3, "地目を決める順番", "ステップ型", "1080×2000", "不登法第3章_図解3_地目を決める順番", "【PC-1】『判断のしかた』の直後", img3, "PC-1"),
    (4, "地目・地積の変更登記：誰が、いつから1か月", "時間の流れ型", "1080×2300", "不登法第3章_図解4_地目地積の変更登記の起算点", "【PC-2】『中身の整理』の直後", img4, "PC-2"),
    (5, "建物の表題部の変更登記：1か月の起算点は4通り", "早見表型（3列）", "1080×2200", "不登法第3章_図解5_建物の表題部の変更登記の起算点", "【PC-3】『中身の整理』の直後", img5, "PC-3"),
    (6, "土地の状況が変わったとき：登記の目的と添える情報", "早見表型（3列）", "1080×2100", "不登法第3章_図解6_土地の状況が変わったとき", "【PC-4】『中身の整理』の直後", img6, "PC-4"),
    (7, "分筆・合筆の地番：原則と例外", "対比表型（3列）", "1080×1800", "不登法第3章_図解7_分筆合筆の地番", "【PC-5】『中身の整理』の直後", img7, "PC-5"),
    (8, "合筆できない6つの場合", "早見表型（3列）", "1080×2300", "不登法第3章_図解8_合筆できない6つの場合", "【PC-5】『たとえば』の直後", img8, "PC-5"),
    (9, "地図の訂正の申出：誰が、どこまでできる？", "対比カード型（2列）＋カード", "1080×2200", "不登法第3章_図解9_地図の訂正の申出", "【PC-6】『中身の整理』の直後", img9, "PC-6"),
    (10, "登記の申請と地図訂正の申出：まとめられる？印鑑証明書は？", "対比表型（3列）", "1080×2200", "不登法第3章_図解10_申請と申出の違い", "【PC-7】『中身の整理』の直後", img10, "PC-7"),
    (11, "地積測量図の誤りの直し方（判定の流れ）", "判定の流れ図型", "1080×2500", "不登法第3章_図解11_地積測量図の誤りの直し方", "【PC-8】『中身の整理』の直後", img11, "PC-8"),
    (12, "図面が閉鎖されるとき", "対比カード型（2列）", "1080×2100", "不登法第3章_図解12_図面が閉鎖されるとき", "【PC-8】『たとえば』の直後", img12, "PC-8"),
    (13, "地積測量図の記録事項（分筆で省略できるのは4つ）", "早見表型（3列）", "1080×2500", "不登法第3章_図解13_地積測量図の記録事項", "【PC-9】『中身の整理』の直後", img13, "PC-9"),
    (14, "地積測量図と地図の約束ごと（精度・署名・座標値）", "カードポスター型", "1080×2300", "不登法第3章_図解14_精度署名座標値", "【PC-9】『たとえば』の直後", img14, "PC-9"),
    (15, "公図の沿革（改租図から地図に準ずる図面まで）", "時間の流れ型", "1080×2600", "不登法第3章_図解15_公図の沿革", "【PC-10】『中身の整理』の直後", img15, "PC-10"),
    (16, "筆界特定の申請：誰が、何を添えるか", "早見表型（3列）＋カード", "1080×2300", "不登法第3章_図解16_筆界特定の申請人", "【PC-11】『中身の整理』の直後", img16, "PC-11"),
    (17, "筆界特定の申請は却下される？（判定の流れ）", "判定の流れ図型", "1080×2700", "不登法第3章_図解17_筆界特定の却下", "【PC-12】『中身の整理』の直後", img17, "PC-12"),
    (18, "筆界特定の手続の相手と主体", "カードポスター型", "1080×2300", "不登法第3章_図解18_筆界特定の相手と主体", "【PC-12】『たとえば』の直後", img18, "PC-12"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PC-1": ("prompt_infographic_PC-01.md", "【PC-1】地目は「土地全体の主な用途」で一つに決まるのか"),
    "PC-2": ("prompt_infographic_PC-02.md", "【PC-2】地目・地積の変更登記は、誰が、いつから1か月か"),
    "PC-3": ("prompt_infographic_PC-03.md", "【PC-3】建物の表題部の変更登記は、誰がいつから1か月を数えるのか"),
    "PC-4": ("prompt_infographic_PC-04.md", "【PC-4】土地の状況が変わったときの登記の目的と添付情報"),
    "PC-5": ("prompt_infographic_PC-05.md", "【PC-5】分筆・合筆の地番はどう付くか、合筆はいつできないか"),
    "PC-6": ("prompt_infographic_PC-06.md", "【PC-6】地図の訂正の申出は、誰が、何について、どこまでできるのか"),
    "PC-7": ("prompt_infographic_PC-07.md", "【PC-7】地図訂正の申出の方式"),
    "PC-8": ("prompt_infographic_PC-08.md", "【PC-8】地積測量図の訂正・閉鎖"),
    "PC-9": ("prompt_infographic_PC-09.md", "【PC-9】地図・地積測量図には何を記録し、どう作るのか"),
    "PC-10": ("prompt_infographic_PC-10.md", "【PC-10】公図の沿革"),
    "PC-11": ("prompt_infographic_PC-11.md", "【PC-11】筆界特定の申請"),
    "PC-12": ("prompt_infographic_PC-12.md", "【PC-12】筆界特定の却下・立入調査・結果の公開"),
}


def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第3章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "分類・早見表が中心の図は、青・赤・チェック・バツを使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。はい／いいえの判定の流れ図だけ、共通部品の配色の規則（青＝はい、赤＝いいえ）で描きます。"
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
