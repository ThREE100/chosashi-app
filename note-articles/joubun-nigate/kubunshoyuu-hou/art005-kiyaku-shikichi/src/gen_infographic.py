# 区分所有法 第5条（規約による建物の敷地）苦手克服：図解インフォグラフィック7枚のプロンプトを組み立てる（共通部品は ../../../common/infographic_parts.py）
import re, pathlib
import sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final, RISKY

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def card_poster(size, t1, t2, sub, cards, arrows=False):
    body = [lead(size, "This is a quick-reference poster with numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header(t1, t2, sub)
    if arrows:
        body.append("Between consecutive cards draw one short plain dark navy arrow pointing down; this arrow means only 'next step', carries no text, and is NOT a YES or NO arrow.")
    n = len(cards)
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {n} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), f"Confirm the number of cards equals {n} exactly, numbered 1 to {n} in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

def table_poster(size, t1, t2, sub, cols, rows, extra, kind="reference table poster (早見表)", ncols=None):
    body = [lead(size, f"This is a {kind}."), TEXTREQ, BGREQ, COLOR] + header(t1, t2, sub) + \
           ["--- TABLE ---",
            f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {len(cols)} columns and exactly {len(rows)} data rows, no merged cells. Draw no check mark and no cross mark.",
            "Header row (dark navy cells with white text), in this order: " + ", ".join(q(c) for c in cols) + "."]
    for n, r in enumerate(rows, 1):
        body.append(f"Data row {n}: " + ", ".join(q(c) for c in r) + ".")
    body += extra
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), f"Confirm the table has exactly {len(cols)} columns and exactly {len(rows)} data rows in the order given, that every cell reads exactly as given, and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解1：5つの言葉
def img1():
    cards = [
        ("法定敷地", "A simple apartment building icon standing on a land plot, with the small tag " + q("建物が所在する土地") + ".", "建物が所在する土地"),
        ("規約敷地", "An apartment building, and next to it a garden-and-passage land plot joined to it by a small paper tag labeled " + q("規約") + ".", "規約で敷地とした土地"),
        ("みなし規約敷地", "An apartment building with a part cut away, and a land plot that is no longer under the building drawn with a dotted outline.", "規約で定めたものとみなす"),
        ("敷地利用権", "A key icon beside a land plot with the label " + q("敷地に関する権利") + ".", "専有部分のための権利"),
        ("敷地権", "A document sheet with a small lock icon and the label " + q("分離して処分できない") + ".", "登記された敷地利用権"),
    ]
    return card_poster("1080x2300", "建物の敷地と敷地権", "5つの言葉を整理する", "区分所有法 第2条・第5条・第22条", cards)

# ---------------------------------------------------------------- 図解2：3種類の規約（＋廃止）
def img2():
    cols = ["規約", "根拠", "定めること", "登記で使う場面"]
    rows = [("規約敷地を定める規約", "区分所有法5条1項", "庭や通路などを建物の敷地とする", "敷地権が生じる。設定を証する情報"),
            ("割合を定める規約", "区分所有法22条2項ただし書", "敷地利用権の割合を、法定の割合と違うものにする", "敷地権の割合。設定を証する情報"),
            ("分離処分を可能とする規約", "区分所有法22条1項ただし書", "専有部分と敷地利用権を分離して処分できるようにする", "敷地権とならない。敷地権が消える"),
            ("規約敷地を定める規約の廃止", "区分所有法31条1項", "規約敷地でなくなる", "敷地権が消える。廃止を証する情報")]
    extra = ["The first column of the four data rows reads exactly " + ", ".join(q(r[0]) for r in rows) + " from top to bottom, each exactly once; data rows 1 and 4 start with the same words " + q("規約敷地を定める規約") + " on purpose, and data row 4 ends with the extra word " + q("の廃止") + " in a pale yellow highlighter marker so that the two rows are clearly different.",
             "Use dark navy outlines only; use no blue or red anywhere in this table."]
    return table_poster("1080x1900", "登記に出てくる3種類の規約", "と、規約敷地の規約の廃止", "区分所有法 第5条・第22条・第31条", cols, rows, extra, "reference table poster (早見表)")

# ---------------------------------------------------------------- 図解3：規約の決め方
def img3():
    cards = [
        ("集会の決議", "A meeting table with several person pictograms seated, and a small white card " + q("区分所有者と議決権の各過半数が出席") + ".", "出席者の4分の3以上"),
        ("公正証書", "A document sheet with a round seal labeled " + q("公正証書") + ", and a person pictogram with the name tag " + q("最初に専有部分の全部を所有する者") + ".", "最初の所有者が単独で"),
        ("一人だけの賛成", "A meeting table with many empty chairs and a single person pictogram holding a sheet labeled " + q("一人だけが賛成した議事録") + ".", "規約は成立しない"),
    ]
    return card_poster("1080x1800", "規約敷地を定める規約", "どう決める？", "区分所有法 第31条・第32条", cards)

# ---------------------------------------------------------------- 図解4：規約敷地ができるとき
def img4():
    cards = [
        ("規約を設定する", "A meeting table with a signed document sheet labeled " + q("規約") + ", and a land plot icon turning into part of the building site.", "土地が建物の敷地になる"),
        ("建物の表題部を変更する", "An apartment building ledger page with one new line labeled " + q("敷地権の表示") + ", and a small calendar tag " + q("1か月以内") + ".", "建物の側が申請"),
        ("土地に敷地権の旨を登記", "A land ledger page with a rubber stamp and the label " + q("敷地権である旨") + ".", "登記官が職権で"),
    ]
    return card_poster("1080x1900", "規約敷地ができたとき", "建物の登記と土地の登記", "不動産登記法 第46条・第51条", cards, arrows=True)

# ---------------------------------------------------------------- 図解5：添付情報の当てはめ表
def img5():
    cols = ["登記", "規約を設定したことを証する情報", "規約の廃止や、分離処分できる事由を証する情報", "他の登記所の土地の登記事項証明書"]
    rows = [("区分建物の表題登記", "要る（規約敷地のとき）", "分離処分可能規約で敷地権とならないときは、その事由の証明", "要る"),
            ("敷地権が生じる変更の登記", "要る", "敷地権でなかった権利が敷地権となるときは、その事由の証明", "要る"),
            ("敷地権が消える変更の登記", "要らない", "要る（廃止の証明、またはその他の事由の証明）", "要らない"),
            ("敷地権付き区分建物どうしの合体（割合を合算）", "要らない", "要らない", "要らない"),
            ("土地の分筆", "要らない", "要らない", "要らない")]
    extra = ["In the cells, the words beginning with " + q("要る") + " are written in BLUE and the words " + q("要らない") + " are written in RED; the longer cells that begin with other words are written in dark navy. Use words only.",
             "The cell " + q("要らない") + " appears several times on purpose, in data rows 3, 4 and 5; draw the same string in each of them. All other cells have their own text exactly as given.",
             "Under the table, one small light-gray tag centered: " + q("不動産登記令 別表の八・十二・十三・十五の項")]
    return table_poster("1080x2200", "規約の証明は、要る？要らない？", "登記の種類ごとに当てはめる", "区分所有法 第5条・第22条", cols, rows, extra)

# ---------------------------------------------------------------- 図解6：判定フロー（中立）
def img6():
    body = [lead("1080x2300", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR] + \
           header("規約の証明は、どれが要る？", "上から順に確かめる", "不動産登記令 別表の十二・十五の項") + \
           ["--- FLOWCHART ---",
            "Layout: START at the top center. DIAMOND 1 below START at the center. From DIAMOND 1 two arrows go down, one to the lower left and one to the lower right. DIAMOND 2 sits at the left (about one quarter of the width from the left edge) and DIAMOND 3 sits at the right (about three quarters of the width). Under DIAMOND 2 there are two result boxes side by side (RESULT 1 on the left, RESULT 2 on the right), and under DIAMOND 3 there are two result boxes side by side (RESULT 3 on the left, RESULT 4 on the right). Each result box is about 230 px wide, with at least 60 px of empty space above it so that the arrow labels stay visible. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "Color: in this flowchart every arrow, label, diamond outline, and result box outline is dark navy (neutral); use NO blue and NO red anywhere, and do not draw the strings 「はい」 or 「いいえ」.",
            "NODE START (rounded pill, dark navy): " + q("規約を証する情報を考える"),
            "NODE DIAMOND 1: " + q("敷地権は、消えるのか、生じるのか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down-left with the label " + q("消える") + " to DIAMOND 2.",
            "  - Arrow down-right with the label " + q("生じる") + " to DIAMOND 3.",
            "NODE DIAMOND 2: " + q("消える原因は、規約敷地を定めた規約の廃止か？") + " The text is placed inside the diamond on 4 lines.",
            "  - Arrow down-left with the label " + q("廃止") + " to RESULT 1.",
            "  - Arrow down-right with the label " + q("それ以外") + " to RESULT 2.",
            "NODE RESULT 1 (white box, navy outline): " + q("規約を廃止したことを証する情報"),
            "NODE RESULT 2 (white box, navy outline): " + q("その他の事由を証する情報") + " on the first two lines and " + q("分離処分可能規約の別段の定めなど") + " on the next two lines.",
            "NODE DIAMOND 3: " + q("敷地権の目的の土地は、規約で建物の敷地となった土地か？") + " The text is placed inside the diamond on 4 lines.",
            "  - Arrow down-left with the label " + q("規約敷地") + " to RESULT 3.",
            "  - Arrow down-right with the label " + q("それ以外") + " to RESULT 4.",
            "NODE RESULT 3 (white box, navy outline): " + q("規約を設定したことを証する情報"),
            "NODE RESULT 4 (white box, navy outline): " + q("規約敷地の規約の証明は要らない"),
            "Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The strings " + q("消える") + " and " + q("生じる") + " are different, and the two labels " + q("それ以外") + " appear on two different arrows on purpose.",
            "Under the flowchart, one small light-gray tag centered: " + q("割合の規約と、他の登記所の土地の登記事項証明書は、別に確かめる")]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that every arrow and box outline is dark navy with no blue or red anywhere, that the two arrows labeled それ以外 and the other labels read exactly as given, that no text overflows its box, and that no arrow label is hidden.")

# ---------------------------------------------------------------- 図解7：分離処分の流れ
def img7():
    cards = [
        ("原則：分離処分できない", "An apartment building and a land plot joined by a chain icon labeled " + q("一体") + ".", "専有部分と敷地権は一体"),
        ("規約に別段の定め", "A document sheet labeled " + q("分離処分可能規約") + " with a small note " + q("一部の区分建物だけでもよい") + ".", "分離して処分できる"),
        ("敷地権の登記を抹消", "A building ledger page with one crossed-out line labeled " + q("敷地権の表示") + ".", "表題部の変更の登記"),
        ("持分だけの移転登記", "A land plot with a rubber stamp and a small tag " + q("土地だけ") + ".", "土地だけを移転できる"),
    ]
    return card_poster("1080x2300", "土地の持分だけを売るには", "4つの順番", "区分所有法 第22条・不動産登記法 第73条", cards, arrows=True)

META = [
    (1, "建物の敷地と敷地権（5つの言葉）", "カードポスター型（俯瞰）", "1080×2300", "図解1_建物の敷地と敷地権", "「部品1：建物の敷地は3つ」の節の終わり", img1),
    (2, "登記に出てくる3種類の規約と、規約の廃止", "早見表型", "1080×1900", "図解2_登記に出てくる3種類の規約", "「部品3：登記に出てくる3種類の規約」の節の終わり", img2),
    (3, "規約敷地を定める規約の決め方", "カードポスター型", "1080×1800", "図解3_規約の決め方", "「部品4：規約の決め方」の節の終わり", img3),
    (4, "規約敷地ができたとき（建物の登記と土地の登記）", "カードポスター型（手順）", "1080×1900", "図解4_規約敷地ができたとき", "「部品5：規約敷地ができたとき・消えたとき」の節の終わり", img4),
    (5, "規約の証明は、要る？要らない？（当てはめ表）", "早見表型", "1080×2200", "図解5_規約の証明の当てはめ表", "「部品6：添付情報の当てはめ」の節の冒頭", img5),
    (6, "規約の証明は、どれが要る？（判定フロー）", "フローチャート型", "1080×2300", "図解6_規約の証明の判定フロー", "「部品6：添付情報の当てはめ」の節の終わり", img6),
    (7, "土地の持分だけを売るには（分離処分の流れ）", "カードポスター型（手順）", "1080×2300", "図解7_分離処分の流れ", "「部品7：分離処分と敷地権」の節の終わり", img7),
]

def build_doc():
    out = ["# 区分所有法 第5条（規約による建物の敷地）　図解インフォグラフィック プロンプト（7枚）\n"]
    out.append("条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、規約敷地（区分所有法 第5条）の記事に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号と問題番号を入れません。\n")
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
    pathlib.Path(__file__).with_name("prompt_infographic_art005.md").write_text(doc, encoding="utf8")
    print(len(doc))
