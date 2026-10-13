#!/usr/bin/env python3
"""総合記事②不動産登記法編 第2章（添付情報・電子申請・登記識別情報・保存期間・登録免許税）：図解インフォグラフィック21枚のプロンプトを組み立てる
（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PB-1.md 〜 _PB-14.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
NOMARK = "no check mark, cross mark, blue, or red appears anywhere"

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

# ---------- 共通の組み立て部品 ----------
def table_poster(size, kind, t1, t2, sub, heads, rows, highlight, band, color=NOCOLOR):
    n = len(heads)
    body = [lead(size, kind), TEXTREQ, BGREQ, color] + header(t1, t2, sub) + \
           ["--- TABLE ---",
            f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {len(rows)} data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + ", ".join(q(h) for h in heads) + ".",
            "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"] + \
           [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)] + \
           [highlight + " Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q(band) + "."]
    ex = (f"Confirm the table has exactly {n} columns and exactly {len(rows)} data rows, that every cell reads exactly as given, and that {NOMARK}.")
    return finish(body, ex)

def two_cards(size, kind, t1, t2, sub, left, right, band, hl=None, color=NOCOLOR, note=None):
    """left/right = (tag, heading, [items])。見出しの黄色マーカーは hl=(左を強調するか, 右を強調するか)"""
    def card(side, c, mark):
        tag, head, items = c
        return (f"{side} card: small tag {q(tag)}, heading {q(head)}" + (" (the heading string has a pale yellow highlighter marker)" if mark else "") +
                f", and exactly {len(items)} short item lines, each with a small dark navy dot at its left end (NO number on the dots): " + ", ".join(q(x) for x in items) + ".")
    hl = hl or (False, False)
    body = [lead(size, kind), TEXTREQ, BGREQ, color] + header(t1, t2, sub) + \
           ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            card("Left", left, hl[0]), card("Right", right, hl[1]),
            "The two cards have clearly different texts; the texts are NOT identical."]
    if note:
        body += ["--- NOTE CARD (below the two cards, a wide card with a dashed dark navy outline) ---",
                 "Heading " + q(note[0]) + ", " + f"{len(note[1])} body lines " + " and ".join(q(b) for b in note[1]) + "."]
    body += ["Under the last card, one wide dark navy band with large white text " + q(band) + "."]
    ex = (f"Confirm there are exactly two cards, that the left card has exactly {len(left[2])} item lines and the right card has exactly {len(right[2])} item lines, that the two headings are not swapped, " +
          ("that there is exactly one note card below the two cards, " if note else "") + f"and that {NOMARK}.")
    return finish(body, ex)

def steps(size, t1, t2, sub, items, side, hl_step=None, color=NOCOLOR, lead_kind=None):
    """items = [(heading, [body lines])]。side = (heading, [body lines]) または None。"""
    n = len(items)
    body = [lead(size, lead_kind or f"This is a vertical step poster with {n} step cards" + (" and one side note card." if side else ".")), TEXTREQ, BGREQ, color] + header(t1, t2, sub) + \
           ["--- STEPS ---",
            f"Layout: {n} step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to {n} in order), one bold heading line, and one or two short body lines."]
    for i, (h, bl) in enumerate(items, 1):
        mark = " (the heading has a pale yellow highlighter marker)" if hl_step == i else ""
        body.append(f"STEP {i}{mark}: heading " + q(h) + ", " + (f"{len(bl)} body lines " if len(bl) > 1 else "body ") + " and ".join(q(b) for b in bl) + ".")
    if side:
        body += ["--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---",
                 "Heading " + q(side[0]) + ", " + (f"{len(side[1])} body lines " if len(side[1]) > 1 else "body ") + " and ".join(q(b) for b in side[1]) + "."]
    ex = (f"Confirm there are exactly {n} step cards numbered 1 to {n} in order" + (", followed by exactly one side note card" if side else "") +
          f", that the arrows carry no labels, and that {NOMARK}.")
    return finish(body, ex)

def cards_poster(size, t1, t2, sub, cards, band=None, color=NOCOLOR, kind=None):
    """cards = [(見出し, 絵, [項目], タグ)]。"""
    n = len(cards)
    body = [lead(size, kind or f"This is a quick-reference poster with {n} numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, color] + header(t1, t2, sub)
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {n} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 f"Item lines ({len(items)} short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    if band: body += ["Under the last card, one wide dark navy band with large white text " + q(band) + "."]
    return finish(body, f"Confirm the number of cards equals {n} exactly, numbered 1 to {n} in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, and confirm that {NOMARK}.")

# ============================================================ 全体（章の冒頭）
def img00():
    cards = [
        ("添付情報（何を添えるか）", "A stack of document sheets held together by a paper clip, with a small blank certificate on top, no text on the sheets.",
         ["省略できるのは添付情報だけ", "所有権を証する情報が要る場面", "作成後3月以内かどうか"], "何を添えるか"),
        ("電子申請と書面申請（どう出すか）", "A laptop beside an envelope and a rubber stamp, no text on the screen or the envelope.",
         ["電子署名とスキャン方式", "取下げ・却下・受領証・原本還付", "「一切の権限」では足りない行為"], "どう出すか"),
        ("登記識別情報と相続情報（受け取る・示す）", "A small key beside a registry ledger, with a family tree sheet drawn without any text.",
         ["誰に・どの登記で通知されるか", "提供・証明・再発行はない", "法定相続情報一覧図"], "受け取る・示す"),
        ("保存・証明書・登録免許税（しまう・見る・払う）", "Archive boxes with a calendar page, and a few coins beside a document sheet, no text on any object.",
         ["保存期間は何年か", "証明書の請求と附属書類の閲覧", "どの登記に課税されるか"], "しまう・見る・払う"),
    ]
    return cards_poster("1080x2300", "添付情報から登録免許税まで", "申請の「付属品」と「手続の作法」", "不動産登記法　第2章の全体像", cards)

# ============================================================ PB-1
def img_pb1():
    return two_cards("1080x2100", "This is a comparison poster with two side-by-side cards and one wide note card.", "省略できるのは、添付情報だけ", "申請情報の記載事項は省略できない", "不動産登記令 第3条・第7条／規則 第36条・第37条・第44条",
        ("申請情報（令3条）", "番号を出しても、書く", ["法人の代表者の氏名（令3条2号）", "会社法人等番号を提供しても省略できない"]),
        ("添付情報（令7条）", "番号や電子証明書で省略できる", ["代表者の資格を証する情報（会社法人等番号の提供で足りる）", "支配人の権限を証する情報（番号を有する法人の支配人等）", "住所を証する情報（署名用電子証明書の提供で足りる）"]),
        "省略できるのは添付情報。申請情報の記載事項は書く", hl=(True, False),
        note=("同時の申請は、援用できる", ["同一の登記所に同時に二以上の申請をするとき、共通の添付情報は一方に付ければ足りる（規則37条）", "もう一方の申請情報に、付けた旨を書く"]))

# ============================================================ PB-2
def img_pb2():
    rows = [
        ("建物の表題登記", "所有権を証する情報が要る", "敷地所有者の証明でも足りる（敷地が共有なら、共有者の一部の者でよい）"),
        ("土地の表題登記を、代位で嘱託する", "被代位者の所有権を証する情報が要る", "代位でも、省略できない（令別表4の項）"),
        ("共用部分である旨の規約を廃止した後の建物の表題登記", "所有権を証する情報が要る", "規約の廃止を証する情報とは別に必要（令別表21の項）"),
        ("合体前の建物のうち、表題登記だけがある建物", "提供しなくてよい", "表題部に所有者が記録されているため（実務上の取扱い）"),
        ("区分建物の表題登記を、他の区分建物の所有者が代位して申請する", "甲区分建物の所有権証明情報を、代位原因の証明に援用できる", "一棟の区分建物は一括して申請する決まり（法48条）"),
    ]
    return table_poster("1080x2000", "This is a reference table poster with three columns.", "所有権を証する情報は、いつ要るか", "代位でも規約廃止でも、省略できない", "不動産登記法・令別表　建物の表題登記ほか",
        ["場面", "所有権を証する情報", "補足"], rows,
        "Highlighting: in column 2, the string 「要る」 inside the cells of rows 1 to 3, and the string 「提供しなくてよい」 of row 4, have a pale yellow highlighter marker; the cells 「要る」 and 「提供しなくてよい」 differ in their wording, so copy each exactly as given.",
        "省かれるのは、表題部に所有者が記録されている建物だけ")

# ============================================================ PB-3
def img_pb3():
    rows = [
        ("共用部分である旨の登記", "令別表18の項", "所有権以外の権利の登記名義人の承諾を証する情報"),
        ("区分建物の表題登記（敷地が管轄外）", "令別表12の項", "その土地の登記事項証明書（不動産番号では省略できない）"),
        ("区分建物の表題登記（分離処分可能規約などで敷地権とならない）", "令別表12の項", "敷地権とならない事由を証する情報（規約など）"),
        ("敷地権の発生による建物の表題部の変更の登記", "令別表15の項", "他の登記所の管轄区域内の土地に限り、その土地の登記事項証明書"),
        ("規約敷地の分筆の登記", "令別表8の項", "規約を設定したことを証する情報は、要らない"),
        ("承役地の合筆の登記（地役権設定の範囲が一部）", "令別表9の項", "地役権者が作成した情報と、地役権図面"),
    ]
    return table_poster("1080x2300", "This is a reference table poster with three columns.", "特別の添付情報は、いつ必要か", "令別表の項で当てはめる", "不動産登記令 第6条・別表の8・9・12・15・18の項",
        ["登記", "令別表", "特別の添付情報"], rows,
        "Highlighting: the string 「その土地の登記事項証明書」 in row 2 and the string 「要らない」 in row 5 have a pale yellow highlighter marker. All other cells are plain.",
        "不動産番号は、申請情報を省略するためのもの")

# ============================================================ PB-4
def img_pb4():
    return two_cards("1080x2100", "This is a comparison poster with two side-by-side cards.", "「作成後3月以内」が要るのは？", "資格・権限・印鑑を示す書類", "不動産登記令 第16条〜第19条／規則 第36条・第72条",
        ("令16条3項・17条1項ほか", "作成後3月以内が要る", ["公務員が作った、代表者の資格・代理人の権限の書面（令17条1項）", "申請書に押印した人の印鑑に関する証明書（令16条3項）", "委任状に押印した本人の印鑑に関する証明書（令18条3項）", "番号に代えて出す登記事項証明書（規則36条2項）", "資格者代理人の職印に関する証明書（準則49条3項）"]),
        ("令19条ほか", "期限の定めはない", ["第三者の承諾書に付ける印鑑証明書（令19条）", "資格者代理人の本人確認情報そのもの（法23条4項1号・規則72条）"]),
        "本人確認情報そのものに、3月の縛りはない", hl=(True, True))

# ============================================================ PB-5
def img_pb5a():
    return steps("1080x2600", "電子申請の添付情報の約束事", "署名・スキャン・原本の提示", "不動産登記令 第12条・第13条",
        [("申請情報にも添付情報にも、電子署名", ["申請情報は申請人等、添付情報は作成者が行う（令12条）"]),
         ("書面の添付情報は、スキャンして送れる", ["表示に関する登記の電子申請で、作成者の電子署名つき（令13条1項）"]),
         ("申請人は、あとで原本を提示する", ["登記官が定めた相当の期間内に、登記官に提示（令13条2項）"])],
        ("スキャン方式の対象外", ["申請人・代表者・代理人が作った書面（委任状など）", "土地所在図・地積測量図・地役権図面・建物図面・各階平面図"]), hl_step=3)

def img_pb5b():
    return two_cards("1080x1900", "This is a comparison poster with two side-by-side cards.", "登記事項証明書の代わりは？", "不動産番号とは、役割が別", "不動産登記令 第6条・第11条",
        ("令6条", "不動産番号", ["申請情報の一部を省略するための番号", "土地の所在・地番・地目・地積などを書かずに済む"]),
        ("令11条", "登記情報の送信を受けるための情報", ["実務では、照会番号など", "登記事項証明書の提供に代えて、送信する"]),
        "登記事項証明書の代わりに、不動産番号は送れない", hl=(False, True))

# ============================================================ PB-6
def img_pb6():
    rows = [
        ("取下げの方法", "取り下げる旨の書面を、登記所に提出する", "取り下げる旨の情報を、電子情報処理組織で提供する"),
        ("取下げができる期間", "登記が完了するまで", "登記が完了するまで"),
        ("取下げ・却下のあとの添付書面", "申請書と添付書面を還付する（偽造の疑いのある書面は除く）", "特例方式で提出した書面には、準用される（規則附則24条1項）"),
        ("却下の決定書", "決定書を作成して交付する（送付もできる）", "決定書を作成して交付する（送付もできる）"),
        ("受領証", "申請が完了するまで請求できる（申請書と同一内容の書面を提出）", "書面申請をした申請人のための制度"),
    ]
    return table_poster("1080x2300", "This is a reference table poster with three columns.", "取下げ・却下・受領証", "入口と出口をそろえて覚える", "不動産登記規則 第38条・第39条・第54条",
        ["手続", "書面申請", "電子申請"], rows,
        "Highlighting: the string 「電子情報処理組織で提供する」 in row 1 column 3, and the string 「申請書と添付書面を還付する」 in row 3 column 2, have a pale yellow highlighter marker.",
        "代理人が取り下げるなら、取下げ用の委任状が別に要る（実務上の取扱い）")

# ============================================================ PB-7
def img_pb7a():
    return steps("1080x2600", "原本還付は、いつ・どう受け取る？", "請求は謄本つき、返るのは調査のあと", "不動産登記規則 第55条",
        [("原本と相違ない旨を記載した謄本を、提出する", ["書面申請の添付書面の原本の還付を請求できる（規則55条1項・2項）"]),
         ("登記官が調査をする", ["調査が完了する前には、還付されない"]),
         ("調査完了後に、原本を還付する", ["謄本と原本を照合して、還付する（規則55条3項）"]),
         ("送付で受け取ることもできる", ["申出により、書留郵便などで送付（規則55条6項・7項）"])],
        ("特例方式で出した書面も、請求できる", ["規則附則24条2項が、規則55条を準用する"]), hl_step=3)

def img_pb7b():
    return two_cards("1080x2000", "This is a comparison poster with two side-by-side cards.", "還付されない書面・省ける謄本", "相続関係説明図で省けるのは戸籍だけ", "不動産登記規則 第55条",
        ("規則55条1項ただし書・5項", "原本の還付を請求できない書面", ["印鑑に関する証明書", "その申請のためにのみ作成された委任状その他の書面", "偽造などの疑いがある書面"]),
        ("相続関係説明図を提出したとき", "謄本を省けるのは、戸籍関係書類だけ", ["戸籍の全部事項証明書など：謄本の提出を省略して、原本の還付を受けられる", "遺産分割協議書：対象外。原本と相違ない旨の謄本が要る"]),
        "遺産分割協議書には、謄本が要る", hl=(False, True))

# ============================================================ PB-8
def img_pb8():
    cards = [
        ("登録免許税の還付金の受領", "A coin and a small envelope with a blank receipt sheet, no text.",
         ["納めすぎた登録免許税（過誤納金）の還付金を受け取る", "「還付金を受領すること」の特別の委任が必要"], "金銭の受領"),
        ("電子申請での登記識別情報の提供", "A small padlock closing over a document sheet, no text.",
         ["登記識別情報を暗号化して提供する", "「暗号化に関する一切の権限」の特別の委任が必要"], "暗号化"),
        ("電子申請での登記識別情報の通知の受領", "A small padlock opening over a document sheet, no text.",
         ["通知を受けて、復号する", "「復号に関する一切の権限」の特別の委任が必要"], "復号"),
    ]
    return cards_poster("1080x2300", "「一切の権限」では足りない", "特別の委任が要る3つの行為", "実務上の取扱い", cards,
        band="委任状が「登記申請に関する一切の権限」だけなら、この3つはできない")

# ============================================================ PB-9
def img_pb9a():
    body = [lead("1080x2300", "This is a vertical decision-flow poster with two diamond questions, three result boxes, and one side note card."), TEXTREQ, BGREQ, COLOR] + \
           header("登記識別情報は、通知されるか", "申請人自らが登記名義人になるか", "不動産登記法 第21条／規則 第64条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical flow on the center line. Node 1 at the top is a rounded navy start box with white text " + q("登記が完了した") + ".",
            "Node 2 (a diamond question): " + q("その登記で、申請人自らが登記名義人となるか") + ". Two arrows leave it: the YES arrow (BLUE, with the small label " + q("はい") + " in blue) goes down to node 3, and the NO arrow (RED, with the small label " + q("いいえ") + " in red) goes to the right to the result box A.",
            "Result box A (RED outline, on the right of node 2): " + q("通知されない") + ", with one small gray line under it: " + q("例：合筆の土地の抵当権者") + ".",
            "Node 3 (a diamond question): " + q("あらかじめ、通知を希望しない旨の申出があるか") + ". Two arrows leave it: the YES arrow (BLUE, label " + q("はい") + " in blue) goes to the left to the result box B, and the NO arrow (RED, label " + q("いいえ") + " in red) goes down to the result box C.",
            "Result box B (BLUE outline, on the left of node 3): " + q("通知されない") + ".",
            "Result box C (RED outline, at the bottom): " + q("通知される") + ", with one small gray line under it: " + q("共有名義なら、名義人ごとに通知") + ".",
            "--- SIDE NOTE CARD (below the flow, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("表示に関する登記でも通知される") + ", body " + q("所有権の登記がある土地の合筆・建物の合体による登記等・建物の合併") + ".",
            "The arrows carry only the labels given above. The flow has exactly 3 result boxes and no other box. The letters A, B and C used in these instructions only identify the boxes and are never drawn in the image."]
    return finish(body, "Confirm there are exactly two diamond questions and exactly three result boxes (A, B, C), that every YES arrow and its label are blue and every NO arrow and its label are red, that the three result boxes read exactly as given, and that no check mark or cross mark is drawn.")

def img_pb9b():
    rows = [
        ("法定代理人が申請した", "法定代理人", "規則62条1項1号"),
        ("申請人が法人である", "その法人の代表者", "規則62条1項2号"),
        ("特別の委任を受けた代理人がいる", "その代理人", "規則62条2項"),
        ("共有名義の土地2筆を合筆した", "名義人ごとに、固有の内容", "法21条"),
    ]
    body = [lead("1080x2300", "This is a reference table poster with three columns, and two deadline cards below the table."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("通知を受けるのは、誰か", "名義人ごと、期限つき", "不動産登記規則 第62条・第64条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("場面") + ", " + q("通知を受ける者") + ", " + q("根拠") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)] + \
           ["Highlighting: the string 「名義人ごとに、固有の内容」 in row 4 has a pale yellow highlighter marker. Copy each cell exactly as given.",
            "--- TWO DEADLINE CARDS (below the table, side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("電子申請（規則64条1項2号）") + ", heading " + q("30日以内") + " (the heading has a pale yellow highlighter marker), body " + q("送信が可能になった時から、自分のファイルに記録しないと通知されない") + ".",
            "Right card: small tag " + q("書面申請（規則64条1項3号）") + ", heading " + q("3月以内") + " (the heading has a pale yellow highlighter marker), body " + q("登記完了の時から、書面を受領しないと通知されない") + ".",
            "The two cards have clearly different texts; the texts are NOT identical."]
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that there are exactly two deadline cards (電子申請 30日以内 on the left and 書面申請 3月以内 on the right, not swapped), and that {NOMARK}.")

# ============================================================ PB-10
def img_pb10a():
    body = [lead("1080x2500", "This is a vertical poster with one wide top card, three numbered cards, and one wide bottom card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登記識別情報をなくしたら", "再発行はなく、提供は一筆分", "不動産登記法 第22条・第23条／令 第8条") + \
           ["--- TOP CARD (a wide pale gray card with a dark navy outline) ---",
            "Heading " + q("再発行の制度はない") + " (the heading has a pale yellow highlighter marker), two body lines " + q("紛失・焼失しても、再発行されない") + " and " + q("漏えいのおそれは、失効の申出（規則65条）") + ".",
            "--- THREE NUMBERED CARDS (stacked top to bottom, all the same size, each with a dark navy circle badge numbered 1 to 3 in order, one bold heading line, and one short body line) ---",
            "A small dark navy tag above these cards: " + q("提供できないときの手当て") + ".",
            "CARD 1: heading " + q("事前通知") + ", body " + q("登記官が、登記名義人に通知する（法23条1項）") + ".",
            "CARD 2: heading " + q("資格者代理人の本人確認情報") + ", body " + q("申請の権限を有する登記名義人であることを確認（法23条4項1号）") + ".",
            "CARD 3: heading " + q("公証人の認証") + ", body " + q("申請書などに、公証人の認証を受ける（法23条4項2号）") + ".",
            "--- BOTTOM CARD (a wide dark navy card with white text) ---",
            "Heading " + q("提供する数") + ", body " + q("土地の合筆は、いずれか一筆分の登記識別情報で足りる（令8条2項1号）") + "."]
    return finish(body, f"Confirm there is exactly one top card, exactly three numbered cards numbered 1 to 3 in order, and exactly one bottom card, that the top card heading reads 再発行の制度はない, and that {NOMARK}.")

def img_pb10b():
    rows = [
        ("有効証明", "提供する登記識別情報が、有効であること", "提供する"),
        ("未通知証明", "登記識別情報が、通知されていないこと", "提供しない"),
        ("失効証明", "登記識別情報が、失効していること", "提供しない"),
    ]
    body = [lead("1080x2100", "This is a reference table poster with three columns, and one wide note card below the table."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登記識別情報に関する証明", "3つの種類と、資格者代理人", "不動産登記令 第22条／規則 第68条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 3 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("種類") + ", " + q("証明する内容") + ", " + q("登記識別情報の提供") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)] + \
           ["Highlighting: the string 「提供する」 in row 1 column 3 has a pale yellow highlighter marker; the cells 「提供する」 and 「提供しない」 differ in their wording, so copy each exactly as given.",
            "--- NOTE CARD (below the table, a wide card with a dashed dark navy outline) ---",
            "Small tag " + q("資格者代理人が代わりに請求するとき") + ", then two body lines " + q("代理人の権限を証する情報（委任状）は、要らない（規則68条7項）") + " and " + q("代わりに、登記の申請の代理を業とできる者であることを証する情報を提供（同条14項）") + "."]
    return finish(body, f"Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, that there is exactly one note card below the table, and that {NOMARK}.")

# ============================================================ PB-11
def img_pb11():
    cards = [
        ("申出先は、4つのどれでもよい", "A small map pin beside a government building icon, no text.",
         ["被相続人の本籍地または最後の住所地", "申出人の住所地", "被相続人名義の不動産の所在地"], "申出人の住所地も選べる"),
        ("代理人による申出", "A person icon handing a blank document sheet across a desk, no text.",
         ["法定代理人、または委任による代理人", "委任による代理人は、親族か戸籍法10条の2第3項に掲げる者に限る", "土地家屋調査士は、委任状のほか資格を示す書面も提供"], "委任状だけでは足りない"),
        ("保管と再交付", "A calendar page with a small archive box, no text.",
         ["保管は、作成の年の翌年から5年（規則28条の2第6号）", "写しの再交付の申出は、保存期間が満了するまで"], "5年"),
        ("使い方", "A document sheet with a family chart drawn without any text, and a small stamp.",
         ["写しを提供すれば、相続を証する情報に代えられる（規則37条の3第1項）", "住所入りの写しは、住所を証する情報も兼ねる", "建物の表題登記で兼ねる扱いは、実務上の取扱い"], "写しを提供する"),
    ]
    return cards_poster("1080x2700", "法定相続情報一覧図", "申出先は4つ、保管は5年", "不動産登記規則 第247条・第28条の2", cards)

# ============================================================ PB-12
def img_pb12():
    rows = [
        ("申請情報とその添付情報（表示・権利とも）", "30年間", "受付の日から"),
        ("土地所在図・地積測量図・建物図面・各階平面図", "永久。閉鎖すると30年間", "閉鎖した日から"),
        ("地役権図面", "閉鎖後30年間", "閉鎖した日から"),
        ("地図・地図に準ずる図面・建物所在図", "永久（閉鎖したものも）", "閉鎖しても永久"),
        ("土地に関する閉鎖登記記録", "50年間", "閉鎖した日から"),
        ("建物に関する閉鎖登記記録", "30年間", "閉鎖した日から"),
        ("法定相続情報一覧図つづり込み帳", "5年間", "作成の年の翌年から"),
    ]
    return table_poster("1080x2300", "This is a reference table poster with three columns.", "保存期間は、何年か", "起算点とセットで覚える", "不動産登記規則 第28条・第28条の2",
        ["保存される情報", "保存期間", "起算点"], rows,
        "Highlighting: the string 「閉鎖すると30年間」 in row 2 and the string 「永久（閉鎖したものも）」 in row 4 have a pale yellow highlighter marker; row 7 column 2 「5年間」 also has a pale yellow highlighter marker.",
        "建物所在図は閉鎖しても永久。地積測量図は閉鎖すると30年")

# ============================================================ PB-13
def img_pb13a():
    rows = [
        ("登記事項証明書", "請求できる", "規則194条3項"),
        ("登記事項要約書", "請求できない（請求書で請求）", "規則194条1項"),
        ("電磁的記録の地図などの内容を証明した書面", "請求できる", "規則200条4項"),
    ]
    return table_poster("1080x1900", "This is a reference table poster with three columns.", "オンラインで請求できるか", "登記事項証明書と、要約書の違い", "不動産登記規則 第194条・第200条",
        ["請求するもの", "電子情報処理組織での請求", "根拠"], rows,
        "Highlighting: the string 「請求できない（請求書で請求）」 in row 2 has a pale yellow highlighter marker; the cells 「請求できる」 and 「請求できない（請求書で請求）」 differ in their wording, so copy each exactly as given.",
        "登記事項要約書だけが、オンライン請求の対象外")

def img_pb13b():
    kinds = ["全部事項証明書", "現在事項証明書", "何区何番事項証明書", "所有者証明書", "一棟建物全部事項証明書", "一棟建物現在事項証明書"]
    body = [lead("1080x2500", "This is a comparison poster with two side-by-side list cards and one wide note card below them."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("証明書の種類と、閲覧・管轄", "6つの種類、閲覧は正当な理由", "不動産登記規則 第196条・第32条／法 第121条") + \
           ["--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("登記事項証明書の6種類") + ", with a small tag " + q("規則196条1項") + ". Exactly six rows, in this order, each with a small dark navy dot at its left end (NO number on the dots):"] + \
           [f"  Row {i}: {q(k)}" for i, k in enumerate(kinds, 1)] + \
           ["Right card: heading bar (dark navy fill, white text) " + q("登記簿の附属書類の閲覧") + ", with a small tag " + q("法121条") + ". Exactly three short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("図面は、何人も閲覧できる（2項）") + ", " + q("図面以外は、正当な理由がある部分に限る（3項）") + ", " + q("登記を申請した者は、自己が申請人の附属書類を閲覧できる（4項）") + ".",
            "Highlighting: the left-card row 6 " + q("一棟建物現在事項証明書") + " and the right-card second item line have a pale yellow highlighter marker. The two cards have clearly different texts; the texts are NOT identical.",
            "--- NOTE CARD (below the two cards, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("管轄が甲登記所から乙登記所に転属したとき") + ", body " + q("登記記録は乙登記所に移送され、以後の申請は乙登記所にする（規則32条1項）") + "."]
    return finish(body, f"Confirm there are exactly two cards, that the left card has exactly six rows and the right card has exactly three item lines, that the two heading bars are not swapped, that there is exactly one note card below the two cards, and that {NOMARK}.")

# ============================================================ PB-14
def img_pb14a():
    rows = [
        ("土地の分筆・建物の分割・区分", "課税される", "後の個数×1,000円"),
        ("土地の合筆・建物の合併", "課税される", "後の個数×1,000円"),
        ("一部地目変更", "課税範囲外", "かからない"),
        ("表題部の登記の抹消（合筆の登記の錯誤による抹消など）", "課税範囲外", "かからない"),
        ("墓地部分に関する登記（墳墓地に関する登記）", "非課税", "かからない"),
        ("国などが私人に代位してする分筆の嘱託", "非課税", "かからない"),
    ]
    return table_poster("1080x2300", "This is a reference table poster with three columns.", "表示の登記の登録免許税", "課税は分筆・区分と合筆・合併だけ", "登録免許税法 別表第一（十三）・第5条",
        ["登記", "課税の扱い", "金額"], rows,
        "Highlighting: the string 「後の個数×1,000円」 in rows 1 and 2 has a pale yellow highlighter marker; the cells 「課税される」, 「課税範囲外」 and 「非課税」 differ in their wording, so copy each exactly as given.",
        "分筆・区分と合筆・合併だけが、後の個数×1,000円")

def img_pb14b():
    cards = [
        ("再区分（1個の区分建物を2個にする）", "Two small apartment-building blocks separating from one block, no text.",
         ["区分後の2個で数える", "1個×1,000円ではなく、2個で2,000円"], "区分後の個数"),
        ("国と私人が共有する土地を、2筆に分筆する", "A plot of land divided into two plots with a small flag icon at its edge, no text.",
         ["分筆後の2筆で数える", "国の持分があっても、通常どおり課税"], "国が入っても課税"),
        ("敷地権の目的である土地の筆数", "Two small plots under one building block, no text.",
         ["数えない", "数えるのは、区分建物の個数"], "筆数は数えない"),
    ]
    return cards_poster("1080x2300", "個数は、後の数で数える", "再区分も、国との共有地も", "登録免許税法 別表第一（十三）イ", cards,
        band="分筆・区分・合筆・合併は、後の個数×1,000円")

# ---------- メタ：番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル ----------
B = "不動産登記法編2章_"
META = [
    (1, "添付情報から登録免許税まで（章の全体像）", "カードポスター型（俯瞰）", "1080×2300", B + "図解1_章の全体像", "この章の論点の一覧の直後（「この章の誤りの傾向」の前）", img00, "00_zentai"),
    (2, "省略できるのは、添付情報だけ", "対比カード型（2列）", "1080×2100", B + "図解2_省略できるのは添付情報だけ", "【PB-1】「中身の整理」の直後", img_pb1, "PB-1"),
    (3, "所有権を証する情報は、いつ要るか", "早見表型（3列）", "1080×2000", B + "図解3_所有権を証する情報", "【PB-2】「中身の整理」の直後", img_pb2, "PB-2"),
    (4, "特別の添付情報は、いつ必要か（令別表の項）", "早見表型（3列）", "1080×2300", B + "図解4_特別の添付情報", "【PB-3】「中身の整理」の直後", img_pb3, "PB-3"),
    (5, "「作成後3月以内」が要るのは？", "対比カード型（2列）", "1080×2100", B + "図解5_作成後3月以内", "【PB-4】「中身の整理」の直後", img_pb4, "PB-4"),
    (6, "電子申請の添付情報の約束事（署名・スキャン・原本の提示）", "ステップ型", "1080×2600", B + "図解6_電子申請の約束事", "【PB-5】「中身の整理」の直後", img_pb5a, "PB-5"),
    (7, "登記事項証明書の代わりは？（不動産番号とは別）", "対比カード型（2列）", "1080×1900", B + "図解7_不動産番号と照会番号", "【PB-5】「たとえば」の直後", img_pb5b, "PB-5"),
    (8, "取下げ・却下・受領証", "早見表型（3列）", "1080×2300", B + "図解8_取下げ却下受領証", "【PB-6】「中身の整理」の直後", img_pb6, "PB-6"),
    (9, "原本還付は、いつ・どう受け取る？", "ステップ型", "1080×2600", B + "図解9_原本還付の流れ", "【PB-7】「中身の整理」の直後", img_pb7a, "PB-7"),
    (10, "還付されない書面・省ける謄本", "対比カード型（2列）", "1080×2000", B + "図解10_還付されない書面", "【PB-7】「たとえば」の直後", img_pb7b, "PB-7"),
    (11, "「一切の権限」では足りない3つ", "カードポスター型", "1080×2300", B + "図解11_一切の権限では足りない", "【PB-8】「中身の整理」の直後", img_pb8, "PB-8"),
    (12, "登記識別情報は、通知されるか（判定の流れ）", "判定の流れ型", "1080×2300", B + "図解12_通知されるか", "【PB-9】「中身の整理」の直後", img_pb9a, "PB-9"),
    (13, "通知を受けるのは、誰か", "早見表型＋カード", "1080×2300", B + "図解13_通知を受ける者", "【PB-9】「たとえば」の直後", img_pb9b, "PB-9"),
    (14, "登記識別情報をなくしたら（再発行はない）", "カード型", "1080×2500", B + "図解14_なくしたら", "【PB-10】「中身の整理」の直後", img_pb10a, "PB-10"),
    (15, "登記識別情報に関する証明", "早見表型＋カード", "1080×2100", B + "図解15_登記識別情報の証明", "【PB-10】図解14の直後", img_pb10b, "PB-10"),
    (16, "法定相続情報一覧図", "カードポスター型", "1080×2700", B + "図解16_法定相続情報一覧図", "【PB-11】「中身の整理」の直後", img_pb11, "PB-11"),
    (17, "保存期間は、何年か", "早見表型（3列）", "1080×2300", B + "図解17_保存期間", "【PB-12】「中身の整理」の直後", img_pb12, "PB-12"),
    (18, "オンラインで請求できるか", "早見表型（3列）", "1080×1900", B + "図解18_オンライン請求", "【PB-13】「中身の整理」の直後", img_pb13a, "PB-13"),
    (19, "証明書の種類と、閲覧・管轄", "対比カード型＋カード", "1080×2500", B + "図解19_証明書の種類と閲覧", "【PB-13】図解18の直後", img_pb13b, "PB-13"),
    (20, "表示の登記の登録免許税", "早見表型（3列）", "1080×2300", B + "図解20_登録免許税の仕分け", "【PB-14】「中身の整理」の直後", img_pb14a, "PB-14"),
    (21, "個数は、後の数で数える", "カードポスター型", "1080×2300", B + "図解21_個数の数え方", "【PB-14】図解20の直後", img_pb14b, "PB-14"),
]

FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PB-1": ("prompt_infographic_PB-01.md", "【PB-1】添付情報は番号や電子証明書で省略できるのか。省略できるのは何か"),
    "PB-2": ("prompt_infographic_PB-02.md", "【PB-2】所有権を証する情報は、どんな場面で要り、何で足りるのか。代位の場合はどうか"),
    "PB-3": ("prompt_infographic_PB-03.md", "【PB-3】区分建物・敷地権・共用部分・地役権の添付情報は、いつ必要になるのか"),
    "PB-4": ("prompt_infographic_PB-04.md", "【PB-4】作成後3月以内のものが必要な書類と、期限のない書類の境目はどこか"),
    "PB-5": ("prompt_infographic_PB-05.md", "【PB-5】電子申請の添付情報には何が必要か。電子署名と原本提示の約束事"),
    "PB-6": ("prompt_infographic_PB-06.md", "【PB-6】申請の取下げ・却下・受領証は、どう扱われるのか"),
    "PB-7": ("prompt_infographic_PB-07.md", "【PB-7】原本還付は、いつ・どこまで・どう請求できるのか"),
    "PB-8": ("prompt_infographic_PB-08.md", "【PB-8】代理人に「一切の権限」を与えただけでは足りない行為は何か"),
    "PB-9": ("prompt_infographic_PB-09.md", "【PB-9】登記識別情報は、誰に・どんな登記で・どう通知されるのか"),
    "PB-10": ("prompt_infographic_PB-10.md", "【PB-10】登記識別情報の提供・証明・再発行は、どうなっているのか"),
    "PB-11": ("prompt_infographic_PB-11.md", "【PB-11】法定相続情報一覧図は、誰が・どこへ・どう使えるのか"),
    "PB-12": ("prompt_infographic_PB-12.md", "【PB-12】登記所が保存する情報の保存期間は、何を・いつから何年なのか"),
    "PB-13": ("prompt_infographic_PB-13.md", "【PB-13】登記事項証明書の交付・閲覧・管轄の移転は、どう扱われるのか"),
    "PB-14": ("prompt_infographic_PB-14.md", "【PB-14】表示に関する登記の登録免許税は、どの登記に・いくらかかるのか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事②不動産登記法編 第2章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②不動産登記法編の第2章「添付情報・電子申請・登記識別情報・保存期間・登録免許税」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "分類・対比・早見表が中心の図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。判定の流れ図（図解12）だけは、はい＝青・いいえ＝赤で描きます（緑には触れません）。"
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
