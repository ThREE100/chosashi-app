# 土地家屋調査士法 届出先の区別（経由か、両方か）図解インフォグラフィック5枚のプロンプトを組み立てる（共通部品は ../../../common/infographic_parts.py）
import re, pathlib
import sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

CARD_REQ = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. "
            "Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.")

# ---------------------------------------------------------------- 図解1：届出先の4パターン
def img1():
    cards = [
        ("調査士（個人）", "A person pictogram with the name tag " + q("調査士") + " handing a document sheet to a small building icon labeled " + q("調査士会") + ", and from that building a solid navy arrow leading to a larger building icon labeled " + q("調査士会連合会") + ".", "調査士会を経由して連合会へ"),
        ("調査士法人", "A building icon labeled " + q("調査士法人") + " with two separate solid navy arrows, one to a small building icon labeled " + q("調査士会") + " and one to a larger building icon labeled " + q("調査士会連合会") + ".", "調査士会と連合会の両方へ"),
        ("変更の登録を申請するとき", "A person pictogram with the name tag " + q("調査士") + " holding a small notice sheet, with one solid navy arrow to a small building icon labeled " + q("現に所属する調査士会") + " only (no second building).", "現に所属する調査士会だけ"),
        ("協会の成立の届出", "A building icon labeled " + q("公共嘱託登記土地家屋調査士協会") + " with two separate solid navy arrows, one to a building icon labeled " + q("法務局又は地方法務局の長") + " and one to a building icon labeled " + q("調査士会") + ".", "法務局の長と調査士会へ"),
    ]
    body = [lead("1080x2000", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."), CARD_REQ,
            TEXTREQ, BGREQ, COLOR] + header("届出先はどこ？", "経由か、両方か", "土地家屋調査士法 第14条・第34条ほか")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

# ---------------------------------------------------------------- 図解2：主語で分ける判定の流れ
def img2():
    body = [lead("1080x1800", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("まず、主語を見る", "届け出るのは、だれ？", "土地家屋調査士法") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 1. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("連合会への届出の肢を読む"),
            "NODE DIAMOND 1: " + q("手続をするのは、調査士か、調査士法人か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("調査士（個人）") + " and " + q("調査士法人") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("調査士（個人）") + " to RESULT 1.",
            "  - Arrow down-right with the label " + q("調査士法人") + " to RESULT 2.",
            "NODE RESULT 1 (blue box): " + q("調査士会を経由して") + " on the first line and " + q("連合会に届け出る") + " on the second line.",
            "NODE RESULT 2 (blue box): " + q("調査士会と連合会の") + " on the first line and " + q("両方に届け出る") + " on the second line.",
            "At the very bottom, one small light-gray tag centered across both result boxes: " + q("どちらにも、法務局への届出は出てこない"),
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings " + q("調査士会を経由して") + " and " + q("調査士会と連合会の") + " are NOT identical); do not copy one into the other."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 調査士（個人） and 調査士法人 and no はい or いいえ, that both result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden.")

# ---------------------------------------------------------------- 図解3：個人の届出（経由）の一覧表
def img3():
    rows = [("登録の申請", "9条1項", "事務所を設けようとする地の調査士会"),
            ("所属する調査士会の変更の登録の申請", "13条1項", "移転先の管轄区域の調査士会"),
            ("登録事項に変更が生じたときの届出", "14条", "所属する調査士会"),
            ("登録の取消し事由に当たるときの届出", "15条2項", "所属し、又は所属していた調査士会"),
            ("心身の故障のおそれがあるときの届出", "16条2項", "所属する調査士会")]
    body = [lead("1080x1900", "This is a quick-reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, COLOR] + \
           header("調査士（個人）の手続", "調査士会を経由して連合会へ", "土地家屋調査士法") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: " + q("手続") + ", " + q("条文") + ", " + q("経由する調査士会") + "."]
    for i, (a, b, c) in enumerate(rows, 1):
        body.append(f"Data row {i}: first column {q(a)}; second column {q(b)}; third column {q(c)}.")
    body += ["Under the table, one wide pale-yellow banner with dark navy text: " + q("どれも、経由先の調査士会を通して連合会に出す") + ".",
             "In data row 2, the words " + q("移転先") + " have a pale yellow highlighter marker. Every row has its own text exactly as given; the rows are NOT identical."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the words 移転先 in row 2 carry the yellow marker, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解4：法人の届出（両方）の一覧表
def img4():
    rows = [("成立の届出", "33条", "成立の日から2週間以内", "主たる事務所の所在地の調査士会"),
            ("定款の変更の届出", "34条2項", "変更の日から2週間以内", "主たる事務所の所在地の調査士会"),
            ("解散の届出（合併を除く）", "39条2項", "解散の日から2週間以内", "主たる事務所の所在地の調査士会"),
            ("合併の届出", "40条3項", "合併の日から2週間以内", "主たる事務所の所在地の調査士会"),
            ("清算結了の届出", "53条3項", "清算結了の登記後速やかに", "主たる事務所の所在地の調査士会"),
            ("新たに会員になったときの届出", "53条6項", "会員となった日から2週間以内", "その会員になった調査士会"),
            ("調査士会を退会したときの届出", "53条7項", "退会の日から2週間以内", "その退会した調査士会")]
    body = [lead("1080x2300", "This is a quick-reference table poster with four columns (早見表)."), TEXTREQ, BGREQ, COLOR] + \
           header("調査士法人の届出", "調査士会と連合会の両方へ", "土地家屋調査士法") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns and exactly 7 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: " + q("手続") + ", " + q("条文") + ", " + q("期限") + ", " + q("あわせて届け出る調査士会") + "."]
    for i, (a, b, c, d) in enumerate(rows, 1):
        body.append(f"Data row {i}: first column {q(a)}; second column {q(b)}; third column {q(c)}; fourth column {q(d)}.")
    body += ["Under the table, one wide pale-yellow banner with dark navy text: " + q("どの行も、調査士会連合会にもあわせて届け出る") + ".",
             "In data row 3 the words " + q("合併を除く") + " have a pale yellow highlighter marker, and in data row 5 the words " + q("登記後速やかに") + " have a pale yellow highlighter marker. Every row has its own text exactly as given, except that the fourth column of rows 1 to 5 reads the same on purpose; draw the same string in those five cells."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 7 data rows, that every cell reads exactly as given, that only the two marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解5：解散と合併の仕分け
def img5():
    body = [lead("1080x1900", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("調査士法人が解散したとき", "どの条文で届け出る？", "土地家屋調査士法 第39条・第40条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1. The two result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 1. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("調査士法人が解散した"),
            "NODE DIAMOND 1: " + q("解散の理由は、他の調査士法人との合併か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("合併") + " and " + q("合併以外") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("合併") + " to RESULT 1.",
            "  - Arrow down-right with the label " + q("合併以外") + " to RESULT 2.",
            "NODE RESULT 1 (blue box): " + q("40条3項の届出") + " on the first line, " + q("合併の日から2週間以内") + " on the second line and " + q("登記事項証明書を添える") + " on the third line.",
            "NODE RESULT 2 (blue box): " + q("39条2項の届出") + " on the first line, " + q("解散の日から2週間以内") + " on the second line and " + q("破産手続開始の決定もここ") + " on the third line.",
            "At the very bottom, one small light-gray tag centered across both result boxes: " + q("届出先は、どちらも調査士会と連合会"),
            "Counts: 1 start node, 1 diamond, 2 result boxes, 2 distinct paths from the start to a result box. The diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings " + q("40条3項の届出") + " and " + q("39条2項の届出") + " are NOT identical); do not copy one into the other."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 1 diamond and 2 result boxes, that the diamond shows only the two navy labels 合併 and 合併以外 and no はい or いいえ, that both result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden.")

# ---------------------------------------------------------------- 図解6：登記の申請と筆界特定の申請の対比表
def img6():
    rows = [("事務をつかさどる所", "登記所（法務局・地方法務局・支局・出張所）", "法務局又は地方法務局"),
            ("管轄の基準", "不動産の所在地", "対象土地の所在地"),
            ("二以上にまたがるとき", "事務を行う所が指定される", "事務を行う所が指定される"),
            ("指定がされる前", "一の登記所に申請できる", "一の法務局又は地方法務局に申請できる"),
            ("根拠", "不動産登記法6条", "不動産登記法124条")]
    body = [lead("1080x1900", "This is a comparison table poster with three columns (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("登記と筆界特定の申請先", "どこが違う？", "不動産登記法 第6条・第124条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("登記の申請") + "; the third header " + q("筆界特定の申請") + ". The two headers are NOT identical."]
    for i, (a, b, c) in enumerate(rows, 1):
        body.append(f"Data row {i} (row label cell, dark navy, white text: {q(a)}): second column {q(b)}; third column {q(c)}.")
    body += ["In data row 1 the words " + q("登記所") + " in the second column and the words " + q("法務局又は地方法務局") + " in the third column have a pale yellow highlighter marker, and in data row 4 the words " + q("申請できる") + " in both columns have a pale yellow highlighter marker. The second and third columns of data row 3 have the same text on purpose; draw the same string in both cells. Every other cell has its own text exactly as given."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 5 data rows, that every cell reads exactly as given, that only the marked phrases carry the yellow marker, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解7：管轄区域にまたがるとき、どこに申請するか
def img7():
    body = [lead("1080x2000", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("管轄区域にまたがるとき", "どこに申請する？", "不動産登記法 第6条・第124条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas for START, DIAMOND 1 and DIAMOND 2, in this order from top to bottom. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between them. RESULT 2 and RESULT 3 sit below DIAMOND 2, one at the lower left and one at the lower right. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("申請先を決める"),
            "NODE DIAMOND 1: " + q("対象の不動産は、二以上の管轄区域にまたがるか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("またがらない") + " and " + q("またがる") + "; do not draw the strings 「はい」 or 「いいえ」 on these arrows.",
            "  - Arrow right with the label " + q("またがらない") + " to RESULT 1.",
            "  - Arrow down with the label " + q("またがる") + " to DIAMOND 2.",
            "NODE RESULT 1 (blue box): " + q("所在地を管轄する所に") + " on the first line and " + q("申請する") + " on the second line.",
            "NODE DIAMOND 2: " + q("事務を行う所の指定は、されたか？") + " The text is placed inside the diamond on 3 lines. This diamond has TWO neutral navy branches with the labels " + q("された") + " and " + q("まだ") + ".",
            "  - Arrow down-left with the label " + q("された") + " to RESULT 2.",
            "  - Arrow down-right with the label " + q("まだ") + " to RESULT 3.",
            "NODE RESULT 2 (blue box): " + q("指定された所に") + " on the first line and " + q("申請する") + " on the second line.",
            "NODE RESULT 3 (blue box): " + q("そのうち一つに") + " on the first line and " + q("申請できる") + " on the second line.",
            "At the very bottom, one small light-gray tag centered across the canvas: " + q("筆界特定でも、登記でも同じ"),
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three blue boxes have different texts (the strings " + q("所在地を管轄する所に") + ", " + q("指定された所に") + " and " + q("そのうち一つに") + " are NOT identical); do not copy one into another."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show only their two navy labels and no はい or いいえ, that all three result boxes are blue and have different texts, that no text overflows its box, and that no arrow label is hidden.")

META = [
    (1, "届出先は、経由か、両方か（4つのパターン）", "カードポスター型", "1080×2000", "図解1_届出先は経由か両方か", "「ひとことで」の直後", img1),
    (2, "まず主語を見る（個人か、法人か）の判定の流れ", "フローチャート型", "1080×1800", "図解2_主語で分ける判定の流れ", "「部品1：まず、主語で分ける」の節の終わり", img2),
    (3, "調査士（個人）の手続の一覧表", "早見表型（3列）", "1080×1900", "図解3_個人の手続の一覧表", "「部品2：調査士（個人）」の節の終わり", img3),
    (4, "調査士法人の届出の一覧表", "早見表型（4列）", "1080×2300", "図解4_法人の届出の一覧表", "「部品3：調査士法人」の節の、届出の一覧のあと", img4),
    (5, "調査士法人が解散したとき、どの条文で届け出るか", "フローチャート型", "1080×1900", "図解5_解散と合併の仕分け", "「解散と合併は、条文が分かれる」の節の終わり", img5),
    (6, "登記の申請と筆界特定の申請の対比表", "対比表型（3列）", "1080×1900", "図解6_登記と筆界特定の申請先の対比表", "「部品5：登記は登記所、筆界特定は法務局又は地方法務局」の節の終わり", img6),
    (7, "管轄区域にまたがるとき、どこに申請するか", "フローチャート型", "1080×2000", "図解7_管轄にまたがるときの申請先", "「部品7：指定がされる前でも、そのうちの一つに申請できる」の節の終わり", img7),
]

def build_doc():
    out = ["# 届出先・申請先の決め方（調査士法の届出先／不動産登記法の申請先）　図解インフォグラフィック プロンプト（7枚）\n"]
    out.append("条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、届出先・申請先の決め方（第1部：土地家屋調査士法の届出先、調査士会を経由する場合と両方に届け出る場合。第2部：不動産登記法の申請先、登記と筆界特定）の記事に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号を入れません。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |\n|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。表の行数（図解3は5行、図解4は7行、図解6は5行）と、流れ図の分岐の数も確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).resolve().parent.parent.joinpath("prompt_infographic_art014-034.md").write_text(doc, encoding="utf8")
    print(len(doc))
