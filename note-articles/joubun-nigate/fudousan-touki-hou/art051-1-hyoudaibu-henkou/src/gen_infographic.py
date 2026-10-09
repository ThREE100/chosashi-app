# 第51条第1項 図解インフォグラフィック6枚のプロンプトを組み立てる
import re, pathlib

RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")

def q(t): return f"「{t}」"

def kanji_in(text):
    return [k for k in sorted(RISKY & set(re.findall(r"[一-鿿]", text)))]

def lead(size, kind):
    return (f"Create a Japanese-language infographic, portrait layout, {size} pixels, clean flat-design isometric illustration style with soft pastel colors "
            f"(light blue, cream, beige, gray), rounded card sections, in the same explainer-graphic style as the other posters of this series (icons: isometric houses, registry ledgers, calendars, rubber stamps, document sheets). {kind}")

TEXTREQ = ("CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only: hiragana, katakana, and Jōyō (regular Japanese) kanji, plus Arabic numerals and the symbols 「」（）・：／ as written below. "
           "Do NOT use Simplified Chinese characters and do NOT use Traditional Chinese characters, even where a glyph looks close to the correct Japanese kanji; every glyph must match the standard Japanese Jōyō form exactly. "
           "Do NOT render any other non-Japanese script (no Korean Hangul, no Latin words) and no stray or decorative glyphs of any kind, even as small background or texture elements. "
           "Reproduce the exact text strings given below verbatim; do not paraphrase, shorten, translate, reorder, or substitute any characters, and do not add any text that is not listed.")

BGREQ = ("BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. "
         "Fill the full canvas, including every corner and margin outside the cards, with a solid pale beige background. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.")

COLOR = ("COLOR RULE: affirmative labels and the YES branch (arrows, labels, and result boxes of any flowchart) are BLUE. Negative labels and the NO branch (arrows, labels, and result boxes of any flowchart) are RED. "
         "Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, badges, and headings, and a pale yellow highlighter only for strings marked as emphasized.")

def final(kanji, extra):
    kj = ", ".join(kanji)
    return (f"Final check before rendering: scan every kanji glyph and confirm it is standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {kj}; "
            "if any character renders as a Chinese variant, redraw it in the correct Japanese form. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji "
            "(including Chinese-only characters, Korean Hangul, other non-Japanese script, or stray decorative glyphs) and remove or redraw it. "
            + extra +
            " Confirm nothing is rendered below the last element: no summary recap panel, no trophy or medal icon, no re-listed grid, and no additional text block of any kind. "
            "Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.")

IMAGES = []   # (番号, タイトル, 型, サイズ, ファイル名, 挿入位置, プロンプト)

# ---------------------------------------------------------------- 図解1：5つの部品
def img1():
    cards = [
        ("何が変わったら？", "An isometric small house icon beside a registry ledger card labeled " + q("登記事項") + "; three small name tags around the house: " + q("所在") + ", " + q("床面積") + ", " + q("敷地権") + ".", "登記事項の変更"),
        ("誰が申請する？", "Two person pictograms side by side with name tags " + q("表題部所有者") + " and " + q("所有権の登記名義人") + ". Beside them, a third person pictogram inside a dotted frame with the tag " + q("所有者") + " and a small note " + q("共用部分の登記がある建物") + ".", "名義人（共用部分は所有者）"),
        ("いつまでに？", "A calendar page with one circled date tagged " + q("変更があった日") + " and a wide bracket spanning one month from that date, tagged " + q("1か月以内") + ".", "変更から1か月以内"),
        ("何を申請する？", "A document sheet with a rubber stamp, labeled " + q("変更の登記") + ".", "変更の登記を申請"),
        ("怠るとどうなる？", "A caution triangle sign and a coin icon, with the small note " + q("正当な理由がない場合") + " and the label " + q("10万円以下の過料") + ".", "10万円以下の過料"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("建物の表題部の変更の登記"), q("条文を5つの部品で読む"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第51条第1項")]
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill, "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")
    return txt + "\n--- FOOTER ---\n" + fin

# ---------------------------------------------------------------- 図解2：44条1項の9つの登記事項
ROWS2 = [("1号", "所在", "対象", "分筆で地番が変わった"),
         ("2号", "家屋番号", "対象外", "登記所が付す番号"),
         ("3号", "種類・構造・床面積", "対象", "増築、用途の変更、屋根の種類の変更"),
         ("4号", "名称", "対象", "建物の名称を変えた"),
         ("5号", "附属建物", "対象", "附属建物の新築、取壊し"),
         ("6号", "共用部分である旨", "対象外", "共用部分の登記で扱う"),
         ("7号", "一棟の建物の構造・床面積", "対象", "一棟の床面積の変更"),
         ("8号", "一棟の建物の名称", "対象", "一棟の建物の名称を変えた"),
         ("9号", "敷地権", "対象", "敷地権が生じた、割合が変わった")]

def img2():
    body = [lead("1080x2200", "This is a reference table poster (早見表)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("44条1項の9つの登記事項"), q("変更の登記が要るのはどれ？"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第44条第1項・第51条第1項"),
            "--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns and exactly 9 data rows, no merged cells.",
            "Header row (dark navy cells with white text), in this order: " + ", ".join(q(c) for c in ["号", "登記事項", "第51条1項の対象", "変わる場面の例"]) + "."]
    for n, (g, item, tgt, ex) in enumerate(ROWS2, 1):
        body.append(f"Data row {n}: " + ", ".join(q(c) for c in [g, item, tgt, ex]) + ".")
    body += ["In the third column, the string " + q("対象") + " is written in BLUE and the string " + q("対象外") + " is written in RED. The two rows whose third column is " + q("対象外") + " (data rows 2 and 6) have a pale gray row background so they stand out; the other seven rows keep the alternating colors. Use words only in that column; draw no check mark and no cross mark.",
             "Along the right edge of data rows 7, 8, and 9, draw one dark navy bracket with the small tag " + q("区分建物のみ") + ".",
             "Row order rule: the first column reads " + ", ".join(q(r[0]) for r in ROWS2) + " from top to bottom, each exactly once; no row is duplicated, merged, or missing."]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 9 data rows in the order 1号 to 9号, that every cell reads exactly as given, that exactly two rows (2号 and 6号) show the red string 対象外, and that the other seven rows show the blue string 対象.")
    return txt + "\n--- FOOTER ---\n" + fin

# ---------------------------------------------------------------- 図解3：判定フロー
def img3():
    body = [lead("1080x2600", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("変更の登記は要る？"), q("上から順に確かめる"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第51条第1項"),
            "--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("変更の登記が要るか考える"),
            "NODE DIAMOND 1: " + q("登記事項（家屋番号と共用部分である旨を除く）に食い違いが出たか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("第51条1項の対象外") + " on the first line and " + q("外壁・屋根の材料の張り替えだけ、表題部所有者の住所の変更など") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("登記をしたあとで、現実が変わったからか？"),
            "  - Arrow down to DIAMOND 3 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (red box): " + q("更正の登記（法53条）") + " on the first line and " + q("申請の義務はない") + " on the second line.",
            "NODE DIAMOND 3: " + q("共用部分である旨の登記がある建物か？") + " This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("ある") + " and " + q("ない") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows.",
            "  - Arrow down-left with the label " + q("ある") + " to RESULT 3.",
            "  - Arrow down-right with the label " + q("ない") + " to RESULT 4.",
            "NODE RESULT 3 (blue box): " + q("所有者が申請する") + " on the first line and " + q("変更があった日から1か月以内") + " on the second line.",
            "NODE RESULT 4 (blue box): " + q("表題部所有者・所有権の登記名義人が申請する") + " on the first two lines and " + q("変更があった日から1か月以内") + " on the third line.",
            "Counts: 1 start node, 3 diamonds, 4 result boxes, 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings " + q("所有者が申請する") + " and " + q("表題部所有者・所有権の登記名義人が申請する") + " are NOT identical); do not copy one into the other."]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「ある」 and 「ない」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that no text overflows its box, and that no arrow label is hidden.")
    return txt + "\n--- FOOTER ---\n" + fin

# ---------------------------------------------------------------- 図解4：通常の建物と共用部分の建物
def img4():
    body = [lead("1080x1700", "This is a two-column comparison poster (対比表)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("変更の登記は、だれが申請する？"), q("通常の建物と共用部分の建物"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第51条第1項"),
            "--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("通常の建物"),
            "--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("共用部分である旨の登記がある建物"),
            "The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere.",
            "--- ROW 1 (row label " + q("登記記録") + ") ---",
            "Left card: a simple ledger icon with the string " + q("表題部所有者または所有権の登記名義人が記録されている") + ".",
            "Right card: a simple ledger icon with an empty name field and the string " + q("名義人の登記は抹消されている（法58条4項）") + ".",
            "--- ROW 2 (row label " + q("申請する人") + ") ---",
            "Left card: a person pictogram with the name tag " + q("表題部所有者または所有権の登記名義人") + ".",
            "Right card: a person pictogram with the name tag " + q("所有者（法51条1項かっこ書）") + ".",
            "--- BOTTOM BAND (one wide dark navy band across both columns, white text) ---",
            q("どちらも、変更があった日から1か月以内に変更の登記を申請"),
            "The left and right cards of each row have clearly different texts; the texts are NOT identical."]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm there are exactly 2 columns and exactly 2 rows of cards plus one bottom band, that the left and right texts of each row are different, and that no check mark or cross mark appears anywhere.")
    return txt + "\n--- FOOTER ---\n" + fin

# ---------------------------------------------------------------- 図解5：1項〜4項
ROWS5 = [("1項", "変更があった当時の名義人（共用部分の建物は所有者）", "変更があった日"),
         ("2項", "変更のあとに名義人になった者", "その者の登記があった日"),
         ("3項", "変更のあとに共用部分の登記がされたときの所有者（1項・2項の人を除く）", "共用部分の登記がされた日"),
         ("4項", "共用部分の登記がある建物で、変更のあとに所有権を取得した者（3項の人を除く）", "所有権の取得の日")]

def img5():
    body = [lead("1080x1600", "This is a reference table poster (早見表)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("1か月は、だれが、いつから数える？"), q("第51条の1項〜4項"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第51条"),
            "--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells.",
            "Header row (dark navy cells with white text), in this order: " + ", ".join(q(c) for c in ["項", "申請する人", "1か月の起算点"]) + "."]
    for n, r in enumerate(ROWS5, 1):
        body.append(f"Data row {n}: " + ", ".join(q(c) for c in r) + ".")
    body += ["In data row 2, under the third-column string, add one line of small gray text: " + q("表題部所有者は更正の登記、名義人は所有権の登記") + ".",
             "Data row 1 is highlighted with a pale yellow row background and a small dark navy tag " + q("この記事の対象") + " at its left edge. The other three rows keep the alternating colors.",
             "The four first-column strings " + ", ".join(q(r[0]) for r in ROWS5) + " are all different; each appears exactly once.",
             "Draw no check mark and no cross mark; use no blue or red anywhere except for the dark navy header cells."]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 4 data rows in the order 1項, 2項, 3項, 4項, that every cell reads exactly as given, and that only data row 1 is highlighted.")
    return txt + "\n--- FOOTER ---\n" + fin

# ---------------------------------------------------------------- 図解6：似ている登記との区別
ROWS6 = [("変更の登記（法51条1項）", "登記のあとで、事実が変わった", "あり：変更の日から1か月以内"),
         ("更正の登記（法53条）", "登記したときから、誤っていた", "なし"),
         ("表題部所有者の氏名・住所の変更（法31条）", "表題部所有者の住所などが変わった", "なし"),
         ("建物の分割（法54条）", "附属建物を別の一個の建物にする", "なし"),
         ("建物の滅失（法57条）", "建物がなくなった", "あり：滅失の日から1か月以内")]

def img6():
    body = [lead("1080x1700", "This is a reference table poster (早見表)."), TEXTREQ, BGREQ, COLOR,
            "--- HEADER ---", "Title (large, bold, 2 lines):", q("似ているけれど違う登記"), q("申請の義務があるのはどれ？"),
            "Subtitle (smaller, centered, 1 line):", q("不動産登記法 第31条・第51条・第53条・第54条・第57条"),
            "--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 5 data rows, no merged cells.",
            "Header row (dark navy cells with white text), in this order: " + ", ".join(q(c) for c in ["登記", "どんなとき", "申請の義務"]) + "."]
    for n, r in enumerate(ROWS6, 1):
        body.append(f"Data row {n}: " + ", ".join(q(c) for c in r) + ".")
    body += ["In the third column, strings that begin with " + q("あり") + " are written in BLUE and the string " + q("なし") + " is written in RED. Use words only; draw no check mark and no cross mark.",
             "Data row 1 is highlighted with a pale yellow row background and a small dark navy tag " + q("この記事の対象") + " at its left edge.",
             "The three rows whose third column is " + q("なし") + " (data rows 2, 3, and 4) have the identical third-column string; that is intended, so draw the same string in all three."]
    txt = "\n".join(body)
    fin = final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 5 data rows in the order given, that every cell reads exactly as given, that exactly two rows show a blue string beginning with あり and exactly three rows show the red string なし.")
    return txt + "\n--- FOOTER ---\n" + fin

META = [
    (1, "第51条第1項を5つの部品で読む", "カードポスター型（俯瞰）", "1080×2300", "図解1_第51条1項を5つの部品で読む",
     "条文の原文とひとことでの直後（「条文を5つの部品に分けて読む」の節の冒頭）", img1),
    (2, "44条1項の9つの登記事項と、51条1項の対象", "早見表型", "1080×2200", "図解2_44条1項の9つの登記事項",
     "「どの欄が変わったら対象か」の節の冒頭", img2),
    (3, "変更の登記は要る？の判定フロー", "フローチャート型", "1080×2600", "図解3_変更の登記は要るかの判定フロー",
     "「どの欄が変わったら対象か」の節の終わり（「確認する順番」の直前）", img3),
    (4, "通常の建物と共用部分の建物で、申請する人が違う", "対比表型", "1080×1700", "図解4_通常の建物と共用部分の建物",
     "「誰が申請するか」の節（部品2）の終わり", img4),
    (5, "第51条の1項〜4項の申請する人と起算点", "早見表型", "1080×1600", "図解5_1項から4項の起算点",
     "「他の項との違い」の節", img5),
    (6, "似ているけれど違う登記（更正・住所の変更・分割・滅失）", "早見表型", "1080×1700", "図解6_似ているけれど違う登記",
     "「隣の条文との違い」の節", img6),
]

def build_doc():
    out = ["# 第51条第1項　図解インフォグラフィック プロンプト（6枚）\n"]
    out.append("条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第51条第1項の記事に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |\n|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        p = fnc()
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + p + "\n```\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).with_name("prompt_infographic_art051-1.md").write_text(doc, encoding="utf8")
    print(len(doc))
