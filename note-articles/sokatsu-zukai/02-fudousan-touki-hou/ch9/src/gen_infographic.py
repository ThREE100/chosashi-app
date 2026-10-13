#!/usr/bin/env python3
"""総合記事② 不動産登記法編 第9章：図解インフォグラフィック11枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch9/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _PG2-1.md ／ _PG2-2.md ／ _PG2-3.md ／ _PG2-4.md ／ _PG2-5.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[3] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
TABLEFMT = "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def table_rows(rows):
    return [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]

# ============================================================ 図解1：第9章の5つの分かれ道（カードポスター）
def img1():
    cards = [
        ("区分建物の表示・合併・区分", "A small apartment building icon cut into two rooms by a thin dashed line, with a ledger book beside it.",
         ["床面積は、内側線で測る", "合併は、区分合併なら接続で足りる", "区分の登記では、承諾した建物に抵当権は残らない"], "非区分建物のルールを持ち込まない"),
        ("区分建物の表題登記の申請人", "A new apartment building icon with a small family register book and a document sheet beside it.",
         ["申請人は、新築した原始取得者", "相続人は、被承継人を表題部所有者として申請できる", "転得者は、代位して申請する"], "誰が申請するか"),
        ("申請の方法と期限", "Two small buildings joined by a short connecting corridor, with a calendar beside them.",
         ["新築なら、一棟の全部を併せて申請する", "既存の非区分建物どうしの接続は、一括して申請する", "合体は、合体の日から1月以内"], "併せてか、一括してか"),
        ("表題部の変更の登記", "A registry ledger page with a pencil and a rubber stamp.",
         ["義務者は、登記上の名義人", "期限は、変更の日から1月以内", "共用部分である旨の登記があっても、免除されない"], "誰が・いつまでに"),
        ("共用部分である旨の登記", "A small shared-room icon inside an apartment building, with a bundle of document sheets.",
         ["申請人は、その建物自身の名義人", "規約を設定したことを証する情報は、全員申請でも必要", "団地共用部分は、団地の建物がそろってから"], "申請人・添付情報・時期"),
    ]
    body = [lead("1080x2700", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, three short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("誰が・何と・いつまでに", "区分建物の登記の5つの分かれ道", "不動産登記法　区分建物の表示と共用部分")
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：区分建物の表示の3つの決まり
def img2():
    rows = [
        ("床面積の測り方", "壁その他の区画の内側線で囲まれた部分（非区分建物は中心線）", "規則115条"),
        ("柱が突き出ているとき", "凹凸をならして、壁面のみで囲まれた部分を求積する", "実務の取扱い（条文に明記なし）"),
        ("地下と地上にまたがるとき", "階層を地下一階付き平家建とは表示しない", "実務の取扱い（直接の条文は確認できていない）"),
    ]
    body = [lead("1080x1900", "This is a reference table poster with three columns (対比表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("区分建物の表示の3つの決まり", "非区分建物とどこが違うか", "不動産登記規則 第115条") + \
           ["--- TABLE ---", TABLEFMT + " Exactly 3 columns and exactly 3 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("区分建物の場面") + ", " + q("扱い") + ", " + q("根拠") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the string 「内側線」 in row 1 has a pale yellow highlighter marker. The cells of column 3 in rows 2 and 3 have a slightly darker pale gray fill to show that they are practice, not a written provision. Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q("区分建物は、非区分建物のルールをそのまま使えない") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：附属合併と区分合併
def img3():
    body = [lead("1080x1900", "This is a comparison poster with two side-by-side cards, one example strip, and one band."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("主従が要る合併、要らない合併", "附属合併と区分合併を並べる", "不動産登記事務取扱手続準則 第86条") + \
           ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("主たる建物と附属建物") + ", heading " + q("附属合併") + ", and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("主従の関係にないと、できない") + ", " + q("主従の関係が要る") + " (the string 「主従の関係が要る」 has a pale yellow highlighter marker).",
            "Right card: small tag " + q("区分建物どうし") + ", heading " + q("区分合併") + ", and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("互いに接続していないと、できない") + ", " + q("主従の関係は要らない") + " (the string 「主従の関係は要らない」 has a pale yellow highlighter marker).",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- EXAMPLE STRIP (below the two cards, a wide card with a dashed dark navy outline and a small dark navy tag " + q("たとえば") + ") ---",
            "Body " + q("名義人が同じ、隣り合う101号室と102号室") + " and " + q("主従の関係がなくても、接続していれば区分合併ができる") + ".",
            "Under the example strip, one wide dark navy band with large white text " + q("主従が要るのは、附属合併だけ") + "."]
    return finish(body, "Confirm there are exactly two cards with exactly two item lines each, that the headings 附属合併 and 区分合併 are not swapped, that the example strip is below the two cards, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解4：区分の登記と抵当権
def img4():
    body = [lead("1080x2300", "This is a vertical step poster with three step cards followed by two result cards side by side."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("建物を区分したとき", "抵当権が残るのはどちらか", "不動産登記規則 第130条第1項") + \
           ["--- STEPS ---",
            "Layout: three step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1, 2, 3 in order), one bold heading line, and one body line.",
            "STEP 1: heading " + q("抵当権つきの建物を、2個に区分する") + ", body " + q("建物の区分の登記を申請する") + ".",
            "STEP 2: heading " + q("原則は、区分後の各建物に引き継がれる") + ", body " + q("権利に関する登記を移記する（規則130条1項）") + ".",
            "STEP 3 (the card has a pale yellow highlighter marker on its heading): heading " + q("抵当権者が、一方の建物の消滅を承諾") + ", body " + q("消滅の承諾を証する情報を提供する") + ".",
            "--- RESULT CARDS (below the steps, two cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card, with no arrow into them and no check mark and no cross) ---",
            "Left result card: small tag " + q("抵当権の消滅を承諾") + ", heading " + q("承諾のあった建物") + ", body " + q("抵当権の登記は、載らない") + ".",
            "Right result card: small tag " + q("消滅の承諾がない") + ", heading " + q("承諾のない建物") + ", body " + q("抵当権の登記が、転写される") + " (the string 「転写される」 has a pale yellow highlighter marker).",
            "The two result cards have clearly different texts; the texts are NOT identical.",
            "Under the two result cards, one wide dark navy band with large white text " + q("抵当権が残るのは、承諾のない建物だけ") + "."]
    return finish(body, "Confirm there are exactly three step cards numbered 1 to 3 in order, followed by exactly two result cards side by side, that the arrows carry no labels, that the headings 承諾のあった建物 and 承諾のない建物 are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解5：区分建物の表題登記を申請するのは誰か
def img5():
    body = [lead("1080x2400", "This is a card poster with three stacked cards, one small pair of cards, and one band."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("区分建物の表題登記", "申請できるのは誰か", "不動産登記法 第47条・不動産登記令 別表12の項") + \
           ["--- THREE STACKED CARDS (all the same size, same pale gray fill, dark navy outline, each with a dark navy circle badge numbered 1 to 3 in order, one bold heading, one small gray tag, and two short body lines each with a small dark navy dot at its left end, NO number on the dots) ---",
            "CARD 1: heading " + q("新築した原始取得者") + ", tag " + q("法47条1項") + ", body " + q("表題登記を申請しなければならない") + ", " + q("所有権の取得の日から1月以内") + ".",
            "CARD 2 (the string 「申請することができる」 has a pale yellow highlighter marker): heading " + q("原始取得者の相続人") + ", tag " + q("法47条2項") + ", body " + q("被承継人を表題部所有者として、申請することができる") + ", " + q("義務ではなく、相続の日からの1月の期限もない") + ".",
            "CARD 3: heading " + q("区分建物の転得者") + ", tag " + q("民法423条") + ", body " + q("自分を表題部所有者とする申請は、できない") + ", " + q("原始取得者に代位して、申請できる") + ".",
            "--- SMALL PAIR (below the three cards: a small dark navy tag " + q("相続人が申請するときの添付情報（令別表12の項）") + " and under it two small cards side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left small card: heading " + q("ハ　所有権を証する情報") + ", body " + q("被承継人が所有権を取得したことの証明") + ".",
            "Right small card (its heading has a pale yellow highlighter marker): heading " + q("ト　一般承継を証する情報") + ", body " + q("相続があったことの証明") + ".",
            "The two small cards have clearly different texts; the texts are NOT identical.",
            "Under the small pair, one wide dark navy band with large white text " + q("相続の資料は、ハではなくトで出す") + "."]
    return finish(body, "Confirm there are exactly three stacked cards numbered 1 to 3 in order, followed by exactly two small cards side by side, that the headings of the two small cards (ハ and ト) are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解6：併せて申請か、一括して申請か
def img6():
    rows = [
        ("区分建物が属する一棟の建物を、新築した", "その一棟の他の区分建物の表題登記と、併せて", "法48条1項"),
        ("表題登記のある非区分建物に接続して、区分建物を新築した", "新築区分建物の表題登記と、既存建物の表題部の変更の登記を、併せて", "法48条3項・法52条1項"),
        ("表題登記のある二以上の非区分建物が、増築で相互に接続して区分建物になった", "表題部の変更の登記を、一括して", "法52条3項"),
        ("別の一棟の区分建物を、附属建物にする", "その一棟の他の区分建物の表題登記も、併せて", "法48条1項の趣旨（整理）"),
    ]
    body = [lead("1080x2100", "This is a reference table poster with three columns (場面と申請方法)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("併せて申請？一括して申請？", "区分建物の申請方法を整理する", "不動産登記法 第48条・第52条") + \
           ["--- TABLE ---", TABLEFMT + " Exactly 3 columns and exactly 4 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("場面") + ", " + q("申請の方法") + ", " + q("根拠") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the string 「一括して」 in the column-2 cell of row 3 has a pale yellow highlighter marker; every 「併せて」 is plain. The cell of column 3 in row 4 has a slightly darker pale gray fill to show that it is an organizing note, not a written provision. The words 「併せて」 and 「一括して」 differ; copy each exactly as given and do not change one into the other.",
            "Under the table, one wide dark navy band with large white text " + q("既存の非区分建物どうしの接続は、法52条3項で一括申請") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that only row 3 reads 一括して in column 2, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解7：合体による登記等の申請人と期限
def img7():
    rows = [
        ("3号", "いずれも表題登記がある建物", "表題部所有者"),
        ("5号", "いずれも所有権の登記がある建物", "所有権の登記名義人"),
        ("1号・2号・4号・6号", "上の2つ以外の組み合わせ", "号ごとに法49条1項が定める者"),
    ]
    body = [lead("1080x2100", "This is a poster with two top cards and a three-column table below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("合体による登記等", "誰が・いつまでに申請するか", "不動産登記法 第49条第1項") + \
           ["--- TWO CARDS (side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: heading " + q("申請するもの") + ", two body lines each with a small dark navy dot at its left end (NO number on the dots): " + q("合体後の建物の表題登記") + ", " + q("合体前の建物の表題部の登記の抹消") + ".",
            "Right card: heading " + q("期限") + ", body " + q("合体の日から1月以内") + " (the string 「1月以内」 has a pale yellow highlighter marker).",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- TABLE ---", "A small dark navy tag above the table: " + q("申請人は、合体前の建物の登記の状態で決まる") + ".",
            TABLEFMT + " Exactly 3 columns and exactly 3 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("合体前の建物") + ", " + q("申請人") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the strings 「表題部所有者」 in row 1 and 「所有権の登記名義人」 in row 2 have a pale yellow highlighter marker; the row 3 cells are plain. Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q("表題登記だけなら表題部所有者、所有権の登記ありなら登記名義人") + "."]
    return finish(body, "Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 3 data rows, that rows 1 and 2 read 表題部所有者 and 所有権の登記名義人 in column 3 and are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解8：表題部の変更の登記（誰が・いつまでに）
def img8():
    body = [lead("1080x2300", "This is a vertical timeline poster with three stage cards and one comparison card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("表題部の変更の登記", "誰が・いつから義務を負うか", "不動産登記法 第51条") + \
           ["--- TIMELINE ---",
            "Layout: one vertical center line down the middle of the canvas; three stage cards are placed top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each stage card has a dark navy badge with its stage name at the top left, one heading line, and two short body lines.",
            "STAGE CARD 1: badge " + q("変更があった日") + ", heading " + q("表題部の登記事項に、変更があった") + ", body " + q("家屋番号と共用部分である旨を除く事項") + " and " + q("建物の種類の変更も含まれる") + ".",
            "STAGE CARD 2 (the heading has a pale yellow highlighter marker): badge " + q("その日から1月以内") + ", heading " + q("名義人が、変更の登記を申請する") + ", body " + q("表題部所有者又は所有権の登記名義人（法51条1項）") + " and " + q("共用部分である旨の登記がある建物は、所有者") + ".",
            "STAGE CARD 3: badge " + q("変更の後に名義人になったとき") + ", heading " + q("その登記があった日から1月以内") + ", body " + q("変更後に名義人となった者が申請する（法51条2項）") + " and " + q("義務は、名義人になってから生じる") + ".",
            "--- COMPARISON CARD (below the timeline, a wide card with a dashed dark navy outline and a small dark navy tag " + q("比べると") + ") ---",
            "Heading " + q("所有権の移転の登記を受けていない取得者") + ", body " + q("まだ名義人ではないので、申請義務はない") + "."]
    return finish(body, "Confirm there are exactly three stage cards in the timeline in the order 変更があった日, その日から1月以内, 変更の後に名義人になったとき, followed by exactly one comparison card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解9：表題部の変更の登記に添えるもの
def img9():
    rows = [
        ("建物の所在（市区郡町村・字・地番）の変更　例：分筆で、建物の所在しない土地が生じたとき", "変更後の建物図面", "なし"),
        ("床面積の変更", "変更後の建物図面と各階平面図", "床面積が増加するときは、増加部分の所有権を証する情報"),
        ("共用部分である旨の登記がある建物の変更", "変更する事項に応じて、上のとおり", "当該建物の所有者を証する情報"),
    ]
    body = [lead("1080x1900", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("表題部の変更の登記に", "何を添えるか", "不動産登記令 別表14の項") + \
           ["--- TABLE ---", TABLEFMT + " Exactly 3 columns and exactly 3 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("変更する事項") + ", " + q("添える図面") + ", " + q("あわせて要るもの") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + table_rows(rows) + \
           ["Highlighting: the string 「建物図面」 in row 1 column 2 and the string 「建物図面と各階平面図」 in row 2 column 2 have a pale yellow highlighter marker. Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q("所在の変更は建物図面。床面積の変更は建物図面と各階平面図") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 3 data rows, that row 1 reads 変更後の建物図面 and row 2 reads 変更後の建物図面と各階平面図 in column 2, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解10：共用部分である旨の登記（申請人・申請情報・添付情報）
def img10():
    body = [lead("1080x2200", "This is a card poster with three numbered cards stacked in one column."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("共用部分である旨の登記", "申請人・申請情報・添付情報", "不動産登記法 第58条・不動産登記令 別表18の項") + \
           ["--- THREE STACKED CARDS (all the same size, same pale gray fill, dark navy outline, each with a dark navy circle badge numbered 1 to 3 in order, one bold heading, one small gray tag, and two short body lines each with a small dark navy dot at its left end, NO number on the dots) ---",
            "CARD 1: heading " + q("申請できるのは、その建物自身の名義人だけ") + ", tag " + q("申請人（法58条2項）") + ", body " + q("表題部所有者又は所有権の登記名義人") + ", " + q("同じ一棟の他の区分建物の名義人は、不可") + ".",
            "CARD 2 (the string 「家屋番号」 has a pale yellow highlighter marker): heading " + q("他の一棟の区分所有者が共用するとき") + ", tag " + q("申請情報") + ", body " + q("その区分所有者が所有する建物の家屋番号") + ", " + q("氏名又は名称ではない") + ".",
            "CARD 3 (the string 「全員で申請しても」 has a pale yellow highlighter marker): heading " + q("規約を設定したことを証する情報") + ", tag " + q("添付情報") + ", body " + q("全員で申請しても、省略できない") + ", " + q("所有権以外の権利があれば、その名義人の承諾を証する情報も要る") + ".",
            "Under the three cards, one wide dark navy band with large white text " + q("申請人の資格と、添付情報は別の話") + "."]
    return finish(body, "Confirm there are exactly three stacked cards numbered 1 to 3 in order, that card 2 reads 家屋番号 and not 氏名, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解11：団地共用部分と、公正証書で設定できる規約
def img11():
    rows = [
        ("規約共用部分を定める規約", "区分所有法4条2項"),
        ("規約による建物の敷地を定める規約", "区分所有法5条1項"),
        ("敷地利用権の分離処分を認める規約", "区分所有法22条1項ただし書"),
        ("敷地利用権の割合を別に定める規約", "区分所有法22条2項ただし書"),
    ]
    body = [lead("1080x2400", "This is a poster with a two-step section at the top and a four-row list card below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("団地共用部分は、いつ登記できる？", "公正証書で作れる規約は4つだけ", "不動産登記法 第58条・区分所有法 第32条") + \
           ["--- SECTION A: two step cards (stacked, same size, joined by one short straight dark navy arrow pointing down, no label on the arrow; each with a dark navy badge with its stage name at the top left, one heading line, and two short body lines) ---",
            "A small dark navy tag above the section: " + q("団地共用部分である旨の登記（令別表19の項）") + ".",
            "STEP CARD 1: badge " + q("甲棟は完成、乙棟は半年後に完成予定") + ", heading " + q("甲棟の管理人室を団地共用部分にしたい") + ", body " + q("共用すべき者の建物が、まだ存在しない") + " and " + q("申請できない") + " (the string 「申請できない」 has a pale yellow highlighter marker).",
            "STEP CARD 2: badge " + q("乙棟が完成してから") + ", heading " + q("共用すべき者の所有する建物が、申請情報になる") + ", body " + q("その建物が現に存在していることが必要") + " and " + q("申請できる") + ".",
            "--- SECTION B: one tall list card (a wide card with a dark navy outline and pale gray fill) ---",
            "A dark navy heading bar inside the card: " + q("最初の所有者が、公正証書で単独で設定できる規約（区分所有法32条）") + ". Exactly four rows, each with a small dark navy dot at its left end (NO number on the dots), the rule text first and a small gray tag at the right end of the row:"] + \
           [f"  Row {i}: {q(a)} {q(b)}" for i, (a, b) in enumerate(rows, 1)] + \
           ["Under the four rows, one small dark navy ribbon tag with white text " + q("共用部分の持分を床面積の割合と異ならせる規約は、この4つにない") + ".",
            "Under the list card, one wide dark navy band with large white text " + q("団地は建物がそろってから。公正証書は4つだけ") + "."]
    return finish(body, "Confirm section A has exactly two step cards with exactly one arrow between them, that section B has exactly four rows, that no extra row such as 14条4項 appears in the list, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "誰が・何と・いつまでに（区分建物の登記の5つの分かれ道）", "カードポスター型（俯瞰）", "1080×2700", "不登法編ch9_図解1_区分建物の登記の5つの分かれ道", "「この章の誤りの傾向」の段落の直後", img1, "00_zentai"),
    (2, "区分建物の表示の3つの決まり（非区分建物とどこが違うか）", "対比表型（3列）", "1080×1900", "不登法編ch9_図解2_区分建物の表示の3つの決まり", "【PG2-1】「中身の整理」の直後", img2, "PG2-1"),
    (3, "主従が要る合併、要らない合併（附属合併と区分合併）", "対比カード型（2列）", "1080×1900", "不登法編ch9_図解3_附属合併と区分合併", "【PG2-1】図解2の直後", img3, "PG2-1"),
    (4, "建物を区分したとき、抵当権が残るのはどちらか", "ステップ型＋結果カード", "1080×2300", "不登法編ch9_図解4_区分の登記と抵当権", "【PG2-1】「たとえば」の直後", img4, "PG2-1"),
    (5, "区分建物の表題登記、申請できるのは誰か", "カードポスター型", "1080×2400", "不登法編ch9_図解5_表題登記の申請人", "【PG2-2】「中身の整理」の直後", img5, "PG2-2"),
    (6, "併せて申請？一括して申請？（区分建物の申請方法）", "早見表型（3列）", "1080×2100", "不登法編ch9_図解6_併せてか一括してか", "【PG2-3】「中身の整理」の直後", img6, "PG2-3"),
    (7, "合体による登記等、誰が・いつまでに申請するか", "カード＋表型", "1080×2100", "不登法編ch9_図解7_合体による登記等", "【PG2-3】図解6の直後", img7, "PG2-3"),
    (8, "表題部の変更の登記、誰が・いつから義務を負うか", "時間の流れ型", "1080×2300", "不登法編ch9_図解8_変更登記の義務者と期限", "【PG2-4】「中身の整理」の直後", img8, "PG2-4"),
    (9, "表題部の変更の登記に、何を添えるか", "早見表型（3列）", "1080×1900", "不登法編ch9_図解9_変更登記の添付情報", "【PG2-4】図解8の直後", img9, "PG2-4"),
    (10, "共用部分である旨の登記（申請人・申請情報・添付情報）", "カードポスター型", "1080×2200", "不登法編ch9_図解10_共用部分の登記", "【PG2-5】「中身の整理」の直後", img10, "PG2-5"),
    (11, "団地共用部分は、いつ登記できる？／公正証書で作れる規約は4つだけ", "ステップ型＋リストカード", "1080×2400", "不登法編ch9_図解11_団地共用部分と公正証書", "【PG2-5】図解10の直後", img11, "PG2-5"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "PG2-1": ("prompt_infographic_PG2-01.md", "【PG2-1】区分建物の表示・合併・区分に、非区分建物のルールをどこまで持ち込めるか"),
    "PG2-2": ("prompt_infographic_PG2-02.md", "【PG2-2】区分建物の表題登記は、誰が申請できるのか（原始取得者・相続人・転得者）"),
    "PG2-3": ("prompt_infographic_PG2-03.md", "【PG2-3】区分建物の登記の申請は「併せて」か「一括して」か、いつまでか"),
    "PG2-4": ("prompt_infographic_PG2-04.md", "【PG2-4】建物の表題部の変更登記は、誰が・いつまでに・何を添えて申請するのか"),
    "PG2-5": ("prompt_infographic_PG2-05.md", "【PG2-5】共用部分である旨の登記は、誰が申請し、何を提供し、団地ではいつ申請できるのか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事② 不動産登記法編 第9章　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事②「直前期の苦手論点つぶし 不動産登記法編」第9章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch9.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この章の図解は『誰が・いつまでに・何を添えるか』の分類や手続の流れが中心で、はい／いいえの分岐ではないため、共通部品の配色の規則（青＝はい、赤＝いいえ）は入れず、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
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
