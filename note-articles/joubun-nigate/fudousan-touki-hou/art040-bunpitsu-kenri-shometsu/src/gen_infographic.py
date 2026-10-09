# 第40条 図解インフォグラフィック6枚のプロンプトを組み立てる（共通部品は ../../../common/infographic_parts.py）
import re, pathlib
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

# ---------------------------------------------------------------- 図解1：5つの部品
def img1():
    cards = [
        ("どんなとき？", "A land plot icon split by a boundary line into two plots, with a registry ledger card beside it labeled " + q("所有権以外の権利の登記") + ".", "権利の登記がある土地の分筆"),
        ("何を添える？", "Two document sheets clipped together: the front sheet labeled " + q("分筆の申請情報") + " and the back sheet labeled " + q("承諾した情報") + ".", "申請と併せて提供"),
        ("だれが承諾する？", "A person pictogram with the name tag " + q("権利の登記名義人") + ", and behind it a smaller person pictogram with the name tag " + q("第三者") + " and the small note " + q("その権利を目的とする権利があるとき") + ".", "権利者と第三者"),
        ("何が登記される？", "A registry ledger page with one stamped line labeled " + q("消滅した旨") + " and a small land plot tag " + q("承諾に係る土地") + ".", "消滅した旨を登記"),
        ("地役権は？", "Two land plot icons side by side with dark navy tags " + q("要役地") + " and " + q("承役地") + ", and a small document sheet between them labeled " + q("扱いが違う") + ".", "規則に別の定め"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("分筆に伴う権利の消滅の登記", "条文を5つの部品で読む", "不動産登記法 第40条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ---------------------------------------------------------------- 図解2：分筆のあと、権利はどうなる
def img2():
    body = [lead("1080x1900", "This is a comparison table poster with three columns (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("分筆で抵当権はどうなる？", "承諾の有無と、消える土地", "不動産登記法 第40条・不動産登記規則 第102条・第104条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 2 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right, with a small light-gray tag under each of the three data headers: the first cell is empty; the second header " + q("承諾の情報がない") + " with the tag " + q("規則102条1項") + "; the third header " + q("乙土地について消す承諾") + " with the tag " + q("規則104条2項") + "; the fourth header " + q("分筆後の甲土地について消す承諾") + " with the tag " + q("規則104条3項") + ".",
            "In the third header the word " + q("乙土地") + " has a pale yellow highlighter marker, and in the fourth header the words " + q("甲土地") + " has a pale yellow highlighter marker. These two headers are NOT identical; do not copy one into the other.",
            "Data row 1 (row label cell, dark navy, white text: " + q("甲土地の記録") + "): second column " + q("抵当権が残る") + "; third column " + q("抵当権に、乙土地について消滅の付記") + "; fourth column " + q("抵当権に、消滅の付記と抹消の記号") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("乙土地の記録") + "): second column " + q("抵当権が転写される") + "; third column " + q("抵当権は転写しない") + "; fourth column " + q("抵当権が転写される") + ".",
            "The second-column cell and the fourth-column cell of data row 2 have the same text on purpose; draw the same string in both. Every other cell has its own text exactly as given."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 2 data rows, that every cell reads exactly as given, that the third and fourth headers differ in the highlighted words 乙土地 and 甲土地, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解3：判定フロー
def img3():
    body = [lead("1080x2600", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR] + \
           header("承諾の情報は要る？", "上から順に確かめる", "不動産登記法 第40条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("分筆の登記を申請する"),
            "NODE DIAMOND 1: " + q("分筆後の土地について、権利を消したいか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("承諾の情報は要らない") + " on the first line and " + q("権利は分筆後の各土地に転写される") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("消したいのは、所有権以外の権利の登記か？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow down to DIAMOND 3 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (red box): " + q("法40条の対象外") + " on the first line and " + q("仮差押え・差押えなど") + " on the second line.",
            "NODE DIAMOND 3: " + q("その権利を目的とする第三者の権利の登記があるか？") + " This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("ある") + " and " + q("ない") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("ある") + " to RESULT 3.",
            "  - Arrow down-right with the label " + q("ない") + " to RESULT 4.",
            "NODE RESULT 3 (blue box): " + q("権利者と第三者の承諾の情報を") + " on the first line and " + q("分筆の申請と併せて提供") + " on the second line.",
            "NODE RESULT 4 (blue box): " + q("権利者の承諾の情報を") + " on the first line and " + q("分筆の申請と併せて提供") + " on the second line.",
            "Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings " + q("権利者と第三者の承諾の情報を") + " and " + q("権利者の承諾の情報を") + " are NOT identical); do not copy one into the other."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「ある」 and 「ない」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden.")

# ---------------------------------------------------------------- 図解4：だれの承諾か
def img4():
    cards = [
        ("土地の所有者", "A person pictogram with the name tag " + q("土地の所有者") + ", drawn with a thin dotted outline to show that this person is not the one who consents.", "承諾する人ではない"),
        ("権利の登記名義人", "A person pictogram with the name tag " + q("抵当権者・地上権者など") + " holding a signed paper sheet.", "この人が承諾"),
        ("抵当証券があるとき", "A certificate icon with two small name tags next to it: " + q("所持人") + " and " + q("裏書人") + ".", "所持人・裏書人も"),
        ("第三者の権利があるとき", "A small stack of two cards: the lower card labeled " + q("抵当権") + " and the upper card labeled " + q("転抵当権") + ", with a person pictogram tagged " + q("転抵当権者") + " beside the stack.", "第三者の承諾も"),
        ("承諾の情報の形", "Two sheets side by side: the left sheet labeled " + q("登記名義人が作成した情報") + " and the right sheet, with a small gavel icon, labeled " + q("裁判があったことを証する情報") + ".", "作成した情報か裁判"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("だれの承諾の情報が要る？", "第40条の承諾する人", "不動産登記法 第40条・不動産登記規則 第104条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ---------------------------------------------------------------- 図解5：地役権（要役地と承役地）
def img5():
    body = [lead("1080x1800", "This is a two-column comparison poster (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("地役権が付いた土地の分筆", "要役地と承役地で違う", "不動産登記規則 第103条・第104条") + \
           ["--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("要役地の地役権"),
            "--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("承役地の地役権"),
            "The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red.",
            "--- ROW 1 (row label " + q("どんな土地？") + ") ---",
            "Left card: a land plot icon with a small arrow-free tag " + q("便益を受ける土地") + ".",
            "Right card: a land plot icon with a small arrow-free tag " + q("便益を供する土地") + ".",
            "--- ROW 2 (row label " + q("分筆のとき") + ") ---",
            "Left card: a document sheet labeled " + q("地役権者が作成した情報を、分筆の申請と併せて提供") + " and, under it, a second document sheet labeled " + q("土地の抵当権者など第三者の承諾の情報も併せて") + ".",
            "Right card: a document sheet labeled " + q("地役権設定の範囲が一部のとき、範囲を申請情報に書き、範囲を証する情報を添える") + ".",
            "--- ROW 3 (row label " + q("登記官がすること") + ") ---",
            "Left card: a registry ledger icon with the string " + q("地役権が消滅した旨を登記（規則104条6項）") + ".",
            "Right card: a registry ledger icon with the string " + q("地役権設定の範囲と地役権図面番号を記録（規則103条1項）") + ".",
            "The left and right cards of each row have clearly different texts; the texts are NOT identical."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 2 columns and exactly 3 rows of cards, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解6：消したあとに戻せるか
def img6():
    body = [lead("1080x1800", "This is a two-column comparison poster (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("分筆の登記を錯誤で戻せる？", "分かれ目は、権利を消したか", "不動産登記法 第40条・第72条") + \
           ["--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("権利が転写されただけ"),
            "--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("承諾で権利を消した"),
            "The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red.",
            "--- ROW 1 (row label " + q("分筆のとき") + ") ---",
            "Left card: a land plot icon split in two, with a ledger line copied into both parts, and the string " + q("分筆前からの抵当権が、各土地に引き継がれた") + ".",
            "Right card: a land plot icon split in two, with a ledger line crossed out in one part, and the string " + q("承諾の情報で、抵当権を消した") + ".",
            "--- ROW 2 (row label " + q("あとで錯誤と分かったら") + ") ---",
            "Left card: a document sheet labeled " + q("錯誤を原因に、分筆の登記を抹消できる") + ".",
            "Right card: a document sheet labeled " + q("分筆錯誤では、分筆の登記を抹消できない") + ".",
            "--- ROW 3 (row label " + q("やり直すには") + ") ---",
            "Left card: a small stamp icon with the string " + q("そのまま抹消の申請ができる") + ".",
            "Right card: a small stamp icon with the string " + q("消えた権利の登記の回復が先（法72条）") + " and, under it, the smaller string " + q("新たな利害関係人がいれば、その承諾が要る") + ".",
            "At the bottom, one small light-gray tag centered across both columns: " + q("右の列は、登記実務の取扱いによる整理"),
            "The left and right cards of each row have clearly different texts; the texts are NOT identical."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 2 columns and exactly 3 rows of cards plus the small gray tag at the bottom, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere.")

META = [
    (1, "第40条を5つの部品で読む", "カードポスター型（俯瞰）", "1080×2300", "図解1_第40条を5つの部品で読む", "条文の原文とひとことでの直後", img1),
    (2, "だれの承諾の情報が要る？", "カードポスター型", "1080×2300", "図解2_だれの承諾の情報が要る", "「部品3：だれが承諾するか」の節の終わり", img4),
    (3, "分筆で抵当権はどうなる（承諾の有無と、消える土地）", "対比表型（3列）", "1080×1900", "図解3_分筆で抵当権はどうなる", "「部品4：何が登記されるか」の節の終わり", img2),
    (4, "地役権が付いた土地の分筆（要役地と承役地）", "対比表型（2列）", "1080×1800", "図解4_地役権が付いた土地の分筆", "「部品5：地役権の特則」の節の終わり", img5),
    (5, "分筆の登記を錯誤で戻せるか", "対比表型（2列）", "1080×1800", "図解5_分筆の登記を錯誤で戻せるか", "「承諾で権利を消したあとは、錯誤で戻せるか」の節の終わり", img6),
    (6, "承諾の情報は要る？の判定フロー", "フローチャート型", "1080×2600", "図解6_承諾の情報は要るかの判定フロー", "「肢を読むときの確認の順番」の節の終わり", img3),
]

def build_doc():
    out = ["# 第40条　図解インフォグラフィック プロンプト（6枚）\n"]
    out.append("条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第40条（分筆に伴う権利の消滅の登記）の記事に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |\n|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).with_name("prompt_infographic_art040.md").write_text(doc, encoding="utf8")
    print(len(doc))
