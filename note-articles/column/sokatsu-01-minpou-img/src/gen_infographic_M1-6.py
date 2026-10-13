# 【M1-6】取得時効：登記はだれに対して要り、占有の推定はどこまで及ぶのか：図解インフォグラフィック2枚のプロンプトを組み立てる
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
else:
    sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

# ---------------------------------------------------------------- 図解1：登記はだれに対して要るか（判定フロー）
def img1():
    body = [lead("1080x2300", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR] + \
           header("時効取得に登記は要る？", "相手と時点で決まる", "民法 第162条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, with at least 60 px of empty space between each diamond and its box so that the arrow label stays visible. All arrows are straight or have at most one right-angle bend and never cross each other. Do not draw any arrow that returns to an earlier node.",
            "NODE START (rounded pill, dark navy): " + q("占有者が、時効取得を主張する"),
            "NODE DIAMOND 1: " + q("主張する相手は、元の所有者か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("元の所有者は、時効の当事者") + " on the first line, " + q("対抗関係に立たない") + " on the second line and " + q("登記なしで主張できる") + " on the third line.",
            "NODE DIAMOND 2: " + q("第三者が所有権を得たのは、時効完成の前か？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow right to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box): " + q("元の所有者と同じ立場（当事者類似）") + " on the first line and " + q("登記なしで主張できる") + " on the next line.",
            "NODE RESULT 3 (red box): " + q("完成の後の第三者とは対抗関係") + " on the first line and " + q("登記の先後で決まる") + " on the next line.",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts, except that the string " + q("登記なしで主張できる") + " appears in both RESULT 1 and RESULT 2 on purpose; the other lines of every box are NOT identical.",
            "--- SMALL TAG (light gray, directly under RESULT 2 and RESULT 3, centered) ---", q("判例の考え方"),
            "--- NOTE CARD AT THE BOTTOM (one separate gray card below RESULT 3, with no arrow) ---",
            "Heading " + q("占有の推定とは別の問い") + " and one body line " + q("無過失が推定されるかは、この流れでは決まらない") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 on the arrow to the right and a red 「いいえ」 on the arrow going down, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, that no arrow label is hidden, and that the gray card at the bottom is one separate card with no arrow.")

# ---------------------------------------------------------------- 図解2：要件と占有の推定（早見表）
def img2():
    body = [lead("1080x1900", "This is a quick-reference table poster (早見表) with a short card below the table."), TEXTREQ, BGREQ, COLOR] + \
           header("取得時効の要件と占有の推定", "推定が及ぶのはどこまで", "民法 第162条・第186条1項") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 5 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is " + q("要素") + "; the second header " + q("20年の取得時効") + " with a small light-gray tag " + q("162条1項") + " under it; the third header " + q("10年の取得時効") + " with a small light-gray tag " + q("162条2項") + " under it; the fourth header " + q("占有の推定") + " with a small light-gray tag " + q("186条1項") + " under it. The three data headers are NOT identical.",
            "Data row 1 (row label cell, dark navy, white text: " + q("所有の意思") + "): second column " + q("必要") + "; third column " + q("必要") + "; fourth column " + q("推定される") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("善意") + "): second column " + q("不要") + "; third column " + q("必要（占有の開始の時）") + "; fourth column " + q("推定される") + ".",
            "Data row 3 (row label cell, dark navy, white text: " + q("平穏") + "): second column " + q("必要") + "; third column " + q("必要") + "; fourth column " + q("推定される") + ".",
            "Data row 4 (row label cell, dark navy, white text: " + q("公然") + "): second column " + q("必要") + "; third column " + q("必要") + "; fourth column " + q("推定される") + ".",
            "Data row 5 (row label cell, dark navy, white text: " + q("無過失") + "): second column " + q("不要") + "; third column " + q("必要（占有の開始の時）") + "; fourth column " + q("推定されない") + ". Draw this whole row 5 with a pale yellow highlighter marker behind the row label and the fourth-column cell.",
            "The cells " + q("必要") + ", " + q("不要") + " and " + q("推定される") + " repeat across rows on purpose; draw each of them exactly as given in the row where it is listed, and do not merge any cells.",
            "--- CARD BELOW THE TABLE ---",
            "One wide rounded card with a dark navy outline and a pale gray fill, with a dark navy heading " + q("推定されない無過失") + " and one body line " + q("10年で時効取得を主張する側が、自分で立証する") + ". Draw this card as ONE separate card below the table, not as a row of the table. Draw no arrow."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 5 data rows in the order 所有の意思, 善意, 平穏, 公然, 無過失, that only row 5 is highlighted and its fourth-column cell reads 推定されない while rows 1 to 4 read 推定される, that the card below the table is one separate card, and that no check mark, cross mark, blue or red appears anywhere.")

META = [
    (1, "時効取得に登記は要るかの判定フロー（相手と時点）", "フローチャート型", "1080×2300", "時効取得に登記は要るか", "「たとえば」の直後（判断のしかたの前）", img1),
    (2, "取得時効の要件と占有の推定（推定が及ぶ範囲）", "早見表型（4列）＋カード1枚", "1080×1900", "取得時効の要件と占有の推定", "「中身の整理」の占有の推定の箇条書きの直後", img2),
]

def build_doc():
    out = ["# 【M1-6】図解インフォグラフィック プロンプト（2枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M1-6】（取得時効：登記はだれに対して要り、占有の推定はどこまで及ぶのか）に差し込む図解のプロンプトです。論点が「登記は誰に対して要るか」と「占有の推定はどこまで及ぶか」の2つの別の問いなので、1枚ずつ（2枚）に分けました。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は総合記事の【M1-6】の節と、民法第162条・第186条1項（`note-articles/laws/minpou-1-soukyoku-bukken.md`で原文を確認）の範囲です。\n")
    checks = {
        1: ["文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない",
            "開始1・ひし形2・結果の箱3で、ひし形は右に青い「はい」、下に赤い「いいえ」が付いている",
            "結果1・2が青い箱、結果3が赤い箱で、文言が入れ替わっていない（完成の後の第三者だけが「登記の先後で決まる」）",
            "「判例の考え方」の小さなタグと、一番下の灰色のカード（占有の推定とは別の問い）が、矢印のない別の部品になっている",
            "背景が透過でなく、最後のカードの下に追加のまとめがない"],
        2: ["文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない",
            "表は4列（要素・20年・10年・占有の推定）×5行で、行の並びが所有の意思・善意・平穏・公然・無過失の順",
            "第4列は「無過失」の行だけが「推定されない」で、ほかの4行は「推定される」。無過失の行だけに黄色のマーカーがある",
            "表の下のカード（推定されない無過失）が1枚だけあり、表の一部になっていない",
            "✓・✕・青・赤が表のどこにもない／背景が透過でなく、カードの下に追加のまとめがない"],
    }
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解：{t}\n")
        out.append(f"- 型：{typ}")
        out.append(f"- サイズ：{size}")
        out.append(f"- 保存名：`M1-6_{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせてください。\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("検品チェック：")
        out += [f"- {c}" for c in checks[n]]
        out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M1-6.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
