#!/usr/bin/env python3
"""総合記事③ 土地家屋調査士法編：図解インフォグラフィック10枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）。
使い方: python3 note-articles/sokatsu-zukai/03-chousashi-hou/src/gen_infographic.py
出力: ../prompt_infographic_00_zentai.md ／ _C1-1.md ／ _C1-2.md ／ _C1-3.md（論点ごとに1ファイル）。生成物は手で直さず、ここを直して再生成する。
画像の中に、個人の演習結果（誤答の回数・自分の回答）と問題番号は入れない。図の番号も入れない（番号は保存名と記事の挿入位置の管理用）。"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
COMMON = HERE.parents[2] / "joubun-nigate" / "common"
sys.path.insert(0, str(COMMON))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final, RISKY

OUT = HERE.parent
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

# ============================================================ 図解1：誰が・どこへ（役割マップ）
def img1():
    cards = [
        ("法務大臣", "A government building icon with a round blank seal stamp, and a small document sheet beside it.",
         ["懲戒処分をする", "会則の制定・変更を認可する", "審査請求の宛先になる"], "処分・認可・審査請求"),
        ("調査士会連合会", "A registration ledger book with a pen and a name tag, no text on the book.",
         ["登録をする", "登録を取り消す"], "登録と登録の取消し"),
        ("調査士会", "A small office building icon with an envelope passing through its door, no text on the envelope.",
         ["登録の申請などを経由する", "法人の届出の宛先になる（連合会と並んで）"], "経由と届出先"),
        ("法務局又は地方法務局の長", "A small local government office icon drawn with a thin dashed outline, with a document sheet being handed over.",
         ["聴聞の権限を委任されることはある", "懲戒処分は、しない"], "処分の主体ではない"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("誰が・どこへ・できるか", "土地家屋調査士法の4つの主体", "この法律の肢は、主体・宛先・できるかどうかで決まる")
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return finish(body, "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ============================================================ 図解2：依頼を拒めるか（3条1項の号の仕分け）
def img2():
    rows = [
        ("1号", "表示登記のための調査・測量", "拒めない"),
        ("2号", "表示登記の申請手続・審査請求の代理", "拒めない"),
        ("3号", "表示登記の申請書類の作成", "拒めない"),
        ("4号", "筆界特定の手続の代理", "拒める"),
        ("5号", "筆界特定の書類の作成", "拒めない"),
        ("6号", "前各号の事務についての相談", "4号に関する部分だけ拒める"),
        ("7号", "民間紛争解決手続の代理", "拒める"),
        ("8号", "その相談", "拒める"),
    ]
    body = [lead("1080x1900", "This is a reference table poster with three columns (対比表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("正当な事由なく拒めるのは？", "法3条1項の号で仕分ける", "土地家屋調査士法 第22条・第3条第1項") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 8 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("業務（法3条1項）") + ", " + q("正当な事由がなくても拒めるか") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: in column 3, the strings 「拒める」 of rows 4, 7 and 8 and the string 「4号に関する部分だけ拒める」 of row 6 have a pale yellow highlighter marker; every 「拒めない」 cell is plain. The cells 「拒める」 and 「拒めない」 differ by one character; copy each exactly as given and do not change one into the other.",
            "Under the table, one wide dark navy band with large white text " + q("調査士法人も同じ（法41条1項が法22条を準用）") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 8 data rows, that every cell reads exactly as given, that exactly the rows 4, 7 and 8 read 「拒める」 in column 3 and the other rows other than row 6 read 「拒めない」, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解3：22条と22条の2は別の話
def img3():
    rows = [
        ("1号", "相手方の協議を受けて賛助し、又はその依頼を承諾した事件", "同意があっても行えない"),
        ("2号", "相手方の協議を受けた事件で、信頼関係に基づくもの", "同意があっても行えない"),
        ("3号", "受任している事件の相手方からの依頼による他の事件", "同意があれば行える"),
        ("4号〜6号", "調査士法人の社員・使用人としての事件", "同意があっても行えない"),
        ("7号", "調査士法人の使用人としての、3号と同様の事件", "同意があれば行える"),
    ]
    body = [lead("1080x2300", "This is a comparison poster: two cards at the top and a table below."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("22条と22条の2は、別の話", "同意で行えるのはどれ？", "土地家屋調査士法 第22条・第22条の2") + \
           ["--- TWO CARDS (side by side, exactly the same size, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card, small tag " + q("法22条") + ", heading " + q("依頼を拒めるか") + ", body " + q("正当な事由がなければ、拒めない") + ".",
            "Right card, small tag " + q("法22条の2") + ", heading " + q("その事件の業務を行ってよいか") + ", body " + q("行ってはならない事件がある") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "--- TABLE ---",
            "A small dark navy tag above the table: " + q("法22条の2第2項（筆界特定手続代理関係業務）") + ".",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("行ってはならない事件") + ", " + q("依頼者の同意") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: the string 「同意があれば行える」 of rows 3 and 5 has a pale yellow highlighter marker; the three cells 「同意があっても行えない」 are plain. The two kinds of cells differ in their wording; copy each exactly as given and do not change one into the other.",
            "Under the table, one wide dark navy band with large white text " + q("同意で外れるのは、3号と7号だけ") + "."]
    return finish(body, "Confirm there are exactly two cards at the top and a table with exactly 3 columns and exactly 5 data rows, that rows 3 and 5 read 「同意があれば行える」 and rows 1, 2 and 4 read 「同意があっても行えない」, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解4：登録の取消し 義務と裁量
def img4():
    body = [lead("1080x1900", "This is a comparison poster with two side-by-side cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登録の取消しは、義務か裁量か", "15条と16条を並べる", "土地家屋調査士法 第15条・第16条") + \
           ["--- TWO COLUMN CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: small tag " + q("法15条1項") + ", heading " + q("取り消さなければならない") + " (the string 「取り消さなければならない」 has a pale yellow highlighter marker), and exactly four short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("業務を廃止したとき") + ", " + q("死亡したとき") + ", " + q("資格を有しないことが判明したとき") + ", " + q("欠格事由に当たるに至ったとき（2号の未成年者を除く）") + ".",
            "Right card: small tag " + q("法16条1項") + ", heading " + q("取り消すことができる") + " (the string 「取り消すことができる」 has a pale yellow highlighter marker), and exactly two short item lines, each with a small dark navy dot at its left end (NO number on the dots): " +
            q("引き続き2年以上業務を行わないとき") + ", " + q("心身の故障により業務を行うことができないとき") + ".",
            "The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("取り消すのは、どちらも調査士会連合会") + "."]
    return finish(body, "Confirm there are exactly two cards, that the left card has exactly four item lines and the right card has exactly two item lines, that the two headings are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解5：欠格事由と3年
def img5():
    rows = [
        ("1号", "拘禁刑以上の刑に処せられた者", "執行の終了などから3年"),
        ("2号", "未成年者", "3年の限定はない"),
        ("3号", "破産手続開始の決定を受けて復権を得ない者", "復権を得るまで"),
        ("4号", "公務員で、懲戒免職の処分を受けた者", "処分の日から3年"),
        ("5号", "調査士法による業務の禁止の処分を受けた者", "処分の日から3年"),
        ("6号", "測量法による登録の抹消の処分を受けた者", "処分の日から3年"),
        ("7号", "建築士法による免許の取消しの処分を受けた者", "処分の日から3年"),
        ("8号", "司法書士法による業務の禁止の処分を受けた者", "処分の日から3年"),
    ]
    body = [lead("1080x2000", "This is a reference table poster with three columns."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("欠格事由は、いつまで続くか", "多くは「3年」で外れる", "土地家屋調査士法 第5条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 8 data rows, no merged cells.",
            "Header row (dark navy cells with white text): " + q("号") + ", " + q("調査士となる資格を有しない者") + ", " + q("いつまで") + ".",
            "Data rows, one per line, in this order (column 1 | column 2 | column 3):"] + \
           [f"Row {i}: {q(a)} | {q(b)} | {q(c)}" for i, (a, b, c) in enumerate(rows, 1)] + \
           ["Highlighting: the string 「3年」 inside the column-3 cells of rows 1, 4, 5, 6, 7 and 8 has a pale yellow highlighter marker. Rows 2 and 3 have a slightly darker pale gray cell fill in column 3 to show that they have no 「3年」. Copy each cell exactly as given.",
            "Under the table, one wide dark navy band with large white text " + q("登録の取消しの義務から除かれるのは、2号の未成年者") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 8 data rows, that every cell reads exactly as given, that rows 2 and 3 do not contain 「3年」 as a period, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解6：執行猶予の時間の流れ
def img6():
    body = [lead("1080x2300", "This is a vertical timeline poster with three stage cards and one comparison card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("執行猶予中の調査士は？", "猶予の期間でみる欠格事由", "土地家屋調査士法 第5条1号・第15条") + \
           ["--- TIMELINE ---",
            "Layout: one vertical center line down the middle of the canvas; three stage cards are placed top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each stage card has a dark navy badge with its stage name at the top left, one heading line, and two short body lines.",
            "STAGE CARD 1: badge " + q("判決") + ", heading " + q("拘禁刑1年・執行猶予3年の判決") + ", body " + q("調査士が、刑に処せられた") + " and " + q("刑の全部の執行が猶予されている") + ".",
            "STAGE CARD 2: badge " + q("猶予の期間中") + ", heading " + q("欠格事由に当たる（法5条1号）") + ", body " + q("執行を終わってもいない") + " and " + q("受けることがなくなってもいない") + ". Under the card, a pale yellow banner " + q("連合会は、登録を取り消さなければならない（法15条1項4号）") + ".",
            "STAGE CARD 3: badge " + q("猶予の期間の満了") + ", heading " + q("刑の言渡しの効力が消える") + ", one body line " + q("欠格事由から外れる") + ".",
            "--- COMPARISON CARD (below the timeline, a wide card with a dashed dark navy outline and a small dark navy tag " + q("比べると") + ") ---",
            "Heading " + q("体調を崩して2年以上業務をしていない調査士") + ", body " + q("連合会は、取り消すことができるだけ（法16条1項）") + " and " + q("取り消す義務はない") + "."]
    return finish(body, "Confirm there are exactly three stage cards in the timeline in the order 判決, 猶予の期間中, 猶予の期間の満了, followed by exactly one comparison card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解7：審査請求先
def img7():
    body = [lead("1080x2000", "This is a vertical step poster with three step cards and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("登録の取消しに不服があるとき", "宛先は、法務大臣", "土地家屋調査士法 第12条・第17条") + \
           ["--- STEPS ---",
            "Layout: three step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1, 2, 3 in order), one bold heading line, and one body line.",
            "STEP 1: heading " + q("調査士会連合会が、登録を取り消す") + ", body " + q("取り消さなければならない場合も、取り消すことができる場合も（法15条1項・16条1項）") + ".",
            "STEP 2: heading " + q("取消しに不服がある") + ", body " + q("取り消された調査士が、争いたい") + ".",
            "STEP 3 (the card has a pale yellow highlighter marker on its heading): heading " + q("法務大臣に審査請求をする") + ", body " + q("法17条が、法12条1項を準用する") + ".",
            "--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("宛先は、処分をした連合会ではない") + ", body " + q("法務大臣は、連合会の上級行政庁とみなされる（法12条3項）") + "."]
    return finish(body, "Confirm there are exactly three step cards numbered 1 to 3 in order, followed by exactly one side note card, that the arrows carry no labels, that the heading of step 3 reads 法務大臣に審査請求をする, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解8：懲戒の手続の流れ
def img8():
    body = [lead("1080x2600", "This is a vertical step poster with five step cards and one side note card."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("懲戒処分の手続の流れ", "処分は法務大臣、聴聞は必須", "土地家屋調査士法 第42条〜第44条") + \
           ["--- STEPS ---",
            "Layout: five step cards stacked top to bottom on the center line, all the same size, joined by short straight dark navy arrows pointing down (no labels on the arrows). Each step card has a dark navy circle badge with the number (1 to 5 in order), one bold heading line, and one or two short body lines.",
            "STEP 1: heading " + q("違反の事実を、法務大臣に通知する") + ", body " + q("何人も、通知して措置を求められる（法44条1項）") + ".",
            "STEP 2: heading " + q("法務大臣が、必要な調査をする") + ", body " + q("通知があれば、調査しなければならない（法44条2項）") + ".",
            "STEP 3 (heading has a pale yellow highlighter marker): heading " + q("戒告・業務の停止なら、聴聞を行う") + ", body " + q("停止の期間が短くても、例外はない（法44条3項）") + ".",
            "STEP 4: heading " + q("聴聞の通知と、審理") + ", two body lines " + q("通知は、期日の1週間前まで（法44条4項）") + " and " + q("審理は、請求があれば公開（法44条5項）") + ".",
            "STEP 5: heading " + q("法務大臣が、処分をする") + ", two body lines " + q("調査士：戒告・2年以内の業務の停止・業務の禁止（法42条）") + " and " + q("調査士法人：戒告・2年以内の業務の停止・解散（法43条）") + ".",
            "--- SIDE NOTE CARD (below the steps, a wide card with a dashed dark navy outline) ---",
            "Heading " + q("法務局又は地方法務局の長は") + ", body " + q("聴聞の権限を委任されることはあるが、処分はしない") + " and a small gray tag " + q("施行規則35条の8第2項") + "."]
    return finish(body, "Confirm there are exactly five step cards numbered 1 to 5 in order, followed by exactly one side note card, that the arrows carry no labels, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解9：会則の認可
def img9():
    need = [("2号", "役員に関する規定"), ("3号", "会議に関する規定"), ("4号", "会員の品位保持に関する規定"),
            ("5号", "会員の執務に関する規定"), ("6号", "入会及び退会に関する規定（入会金を含む）"), ("12号", "その他調査士会の目的を達成するために必要な規定")]
    noneed = [("1号", "名称及び事務所の所在地"), ("7号", "調査士の研修に関する規定"), ("8号", "会員の業務に関する紛議の調停に関する規定"),
              ("9号", "調査士会及び会員に関する情報の公開に関する規定"), ("10号", "資産及び会計に関する規定"), ("11号", "会費に関する規定")]
    body = [lead("1080x2300", "This is a comparison poster with two side-by-side list cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("会則の変更に、認可は要るか", "法48条の号で仕分ける", "土地家屋調査士法 第48条・第49条") + \
           ["--- TWO LIST CARDS (side by side, exactly the same size, top-aligned, each with exactly six rows; each row has the item number at the left in a small dark navy tag and the item text) ---",
            "Left card: heading bar (dark navy fill, white text) " + q("認可が必要") + ", with a small tag " + q("法49条1項本文") + ". The six rows, in this order:"] + \
           [f"  Row {i}: {q(a)} {q(b)}" for i, (a, b) in enumerate(need, 1)] + \
           ["Right card: heading bar (pale gray fill, dark navy text) " + q("認可が不要") + ", with a small tag " + q("同項ただし書（変更のとき）") + ". The six rows, in this order:"] + \
           [f"  Row {i}: {q(a)} {q(b)}" for i, (a, b) in enumerate(noneed, 1)] + \
           ["Highlighting: the left-card row 5 (6号) and the right-card row 6 (11号) have a pale yellow highlighter marker. The two cards have clearly different texts; the texts are NOT identical.",
            "Under the two cards, one wide dark navy band with large white text " + q("入会金（6号）は認可が要る。会費（11号）は要らない") + "."]
    return finish(body, "Confirm there are exactly two cards with exactly six rows each, that the left card holds 2号, 3号, 4号, 5号, 6号 and 12号 and the right card holds 1号, 7号, 8号, 9号, 10号 and 11号, that the two heading bars are not swapped, and that no check mark, cross mark, blue, or red appears anywhere.")

# ============================================================ 図解10：調査士法人の届出
def img10():
    body = [lead("1080x2100", "This is a quick-reference poster: one destination card and three event cards."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("調査士法人の届出は、どこへ", "宛先と期限をそろえて覚える", "土地家屋調査士法 第33条・第34条・第39条") + \
           ["--- DESTINATION CARD (a wide dark navy card at the top, with white text) ---",
            "Small label " + q("届出先") + ", then the bold text " + q("主たる事務所の所在地の調査士会") + " and " + q("調査士会連合会") + " (the two joined by a small plus sign, with no text on the plus sign). Beside it a small pale gray card with dashed outline and the text " + q("法務局ではない") + ".",
            "--- EVENT CARDS (three cards stacked top to bottom, all the same size, each with a dark navy circle badge numbered 1 to 3 in order, one bold heading line, one pale-yellow deadline banner, and one small gray tag) ---",
            "CARD 1: heading " + q("調査士法人が成立したとき") + ", deadline banner " + q("成立の日から2週間以内") + ", small gray tag " + q("法33条") + ", and a body line " + q("登記事項証明書と定款の写しを添える") + ".",
            "CARD 2: heading " + q("定款を変更したとき") + ", deadline banner " + q("変更の日から2週間以内") + ", small gray tag " + q("法34条2項") + ".",
            "CARD 3: heading " + q("解散したとき（合併による解散を除く）") + ", deadline banner " + q("解散の日から2週間以内") + ", small gray tag " + q("法39条2項") + "."]
    return finish(body, "Confirm there is exactly one destination card at the top followed by exactly three event cards numbered 1 to 3 in order, that all three deadline banners read 2週間以内, that the small gray card reads 法務局ではない, and that no check mark, cross mark, blue, or red appears anywhere.")

# 番号, 題, 型, サイズ, 保存名(拡張子なし), 記事の挿入位置, 関数, 出力ファイル
META = [
    (1, "誰が・どこへ・できるか（4つの主体）", "カードポスター型（俯瞰）", "1080×2300", "調査士法編_図解1_誰がどこへできるか", "「土地家屋調査士法で落とすパターン」の段落の直後", img1, "00_zentai"),
    (2, "正当な事由なく拒めるのは？（法3条1項の号で仕分ける）", "対比表型（3列）", "1080×1900", "調査士法編_図解2_正当な事由なく拒めるのは", "【C1-1】「中身の整理」の直後", img2, "C1-1"),
    (3, "22条と22条の2は、別の話（同意で行えるのはどれ）", "対比表型＋カード", "1080×2300", "調査士法編_図解3_22条と22条の2は別の話", "【C1-1】「たとえば」の直後", img3, "C1-1"),
    (4, "登録の取消しは、義務か裁量か", "対比カード型（2列）", "1080×1900", "調査士法編_図解4_登録の取消しは義務か裁量か", "【C1-2】「中身の整理」の直後", img4, "C1-2"),
    (5, "欠格事由は、いつまで続くか（多くは3年）", "早見表型（3列）", "1080×2000", "調査士法編_図解5_欠格事由はいつまで続くか", "【C1-2】図解4の直後", img5, "C1-2"),
    (6, "執行猶予中の調査士は？（猶予の期間でみる欠格事由）", "時間の流れ型", "1080×2300", "調査士法編_図解6_執行猶予中の調査士は", "【C1-2】「たとえば」の直後", img6, "C1-2"),
    (7, "登録の取消しに不服があるとき（宛先は法務大臣）", "ステップ型", "1080×2000", "調査士法編_図解7_審査請求の宛先", "【C1-2】図解6の直後", img7, "C1-2"),
    (8, "懲戒処分の手続の流れ", "ステップ型", "1080×2600", "調査士法編_図解8_懲戒処分の手続の流れ", "【C1-3】「中身の整理」の直後", img8, "C1-3"),
    (9, "会則の変更に、認可は要るか（法48条の号で仕分ける）", "対比カード型（2列）", "1080×2300", "調査士法編_図解9_会則の認可", "【C1-3】図解8の直後", img9, "C1-3"),
    (10, "調査士法人の届出は、どこへ", "カードポスター型", "1080×2100", "調査士法編_図解10_調査士法人の届出", "【C1-3】図解9の直後", img10, "C1-3"),
]
FILES = {
    "00_zentai": ("prompt_infographic_00_zentai.md", "全体（章の冒頭）"),
    "C1-1": ("prompt_infographic_C1-1.md", "【C1-1】正当な事由がなくても依頼を拒めるのは、どの業務か（調査士法人でも同じか）"),
    "C1-2": ("prompt_infographic_C1-2.md", "【C1-2】登録はどんなときに取り消され、取消しに不服があるときは誰に争うのか（欠格事由を含む）"),
    "C1-3": ("prompt_infographic_C1-3.md", "【C1-3】懲戒の聴聞、会則の認可、法人の定款変更の届出は、誰が・どこで行うのか"),
}

def build_doc(key):
    fname, title = FILES[key]
    items = [m for m in META if m[7] == key]
    out = [f"# 総合記事③ 土地家屋調査士法編　図解インフォグラフィック プロンプト（{title}・{len(items)}枚）\n"]
    out.append("総合記事③「直前期の苦手論点つぶし 土地家屋調査士法編」（`note-articles/column/sokatsu-03-chousashi-hou.md`）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この科目の図解は『拒めるか・要るか』のような分類が中心で、はい／いいえの分岐ではないため、共通部品の配色の規則（青＝はい、赤＝いいえ）は入れず、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。"
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
