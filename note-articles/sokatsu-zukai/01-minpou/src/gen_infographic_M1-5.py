# 【M1-5】代理権の濫用と無権代理の相続：本人に効果は帰属するのか：図解インフォグラフィック2枚のプロンプトを組み立てる
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

# ---------------------------------------------------------------- 図解1：代理権の濫用と無権代理（対比表）
def img1():
    body = [lead("1080x1800", "This is a comparison table poster (対比表) with a short card below the table."), TEXTREQ, BGREQ, COLOR] + \
           header("代理権の濫用と無権代理", "本人に効果は帰属するか", "民法 第107条・第113条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("代理権の濫用") + " with a small light-gray tag " + q("代理権はある") + " under it; the third header " + q("無権代理") + " with a small light-gray tag " + q("代理権がない") + " under it. These two headers are NOT identical.",
            "Data row 1 (row label cell, dark navy, white text: " + q("どんな場面？") + "): second column " + q("代理権の範囲内で、自分や第三者の利益を図る目的で行為した") + "; third column " + q("代理権がないのに、代理人として契約をした") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("本人に効果が帰属するのは？") + "): second column " + q("相手方が善意無過失なら、帰属する。本人は無効を主張できない") + " with the words " + q("善意無過失") + " in a pale yellow highlighter marker; third column " + q("本人が追認したとき") + " with the word " + q("追認") + " in a pale yellow highlighter marker.",
            "Data row 3 (row label cell, dark navy, white text: " + q("相手方が悪意または有過失だと？") + "): second column " + q("目的を知り、又は知ることができたなら、無権代理行為とみなされる（107条）") + "; third column " + q("本人が追認しなければ、本人に効力を生じない（113条1項）") + ".",
            "The second-column and third-column cells of each data row have clearly different texts; the texts are NOT identical, so copy each cell exactly as given.",
            "--- CARD BELOW THE TABLE ---",
            "One wide rounded card with a dark navy outline and a pale gray fill, with a dark navy heading " + q("無権代理行為とみなされるのは") + " and one body line " + q("相手方が目的を知り、又は知ることができたときに限る") + ". Draw this card as ONE separate card below the table, not as a row of the table. Draw no arrow."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 3 data rows, that the second header is 「代理権の濫用」 and the third header is 「無権代理」 and they are not swapped, that every cell reads exactly as given, that the card below the table is one separate card, and that no check mark, cross mark, blue or red appears anywhere.")

# ---------------------------------------------------------------- 図解2：無権代理人が本人を相続したら（判定フロー）
def img2():
    body = [lead("1080x2300", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR] + \
           header("無権代理人が本人を相続したら", "追認を拒絶できるか", "民法 第113条1項") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, NOTE CARD, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, with at least 60 px of empty space between each diamond and its box so that the arrow label stays visible. All arrows are straight or have at most one right-angle bend and never cross each other. Do not draw any arrow that returns to an earlier node.",
            "NODE START (rounded pill, dark navy): " + q("無権代理人が、本人を相続した"),
            "NODE NOTE CARD (a small gray card directly below START, with no arrow of its own): " + q("無権代理は、本人が追認しなければ、本人に効力を生じない") + " on the first line and " + q("民法113条1項") + " on the second line.",
            "NODE DIAMOND 1: " + q("本人は、相続の前に追認を拒絶していたか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("拒絶の効果は確定している") + " on the first line and " + q("無権代理人は、請求を拒める") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("相続人は、無権代理人ひとりか？") + " The text is placed inside the diamond on 3 lines.",
            "  - Arrow right to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box): " + q("本人と無権代理人の地位が融合") + " on the first line, " + q("信義則上、追認の拒絶は許されない") + " on the second line and " + q("行為は当然に有効") + " on the third line.",
            "NODE RESULT 3 (red box): " + q("追認は共同相続人の全員でする") + " on the first line and " + q("他の相続人とともに拒絶し、請求を拒める") + " on the next two lines.",
            "Counts: 1 start node, 1 note card, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 1 and RESULT 3 have different texts, and RESULT 2 has its own text; do not copy one into another.",
            "--- NOTE CARD AT THE BOTTOM (one separate gray card below RESULT 3, with no arrow) ---",
            "Heading " + q("地位が最終的に一人に集まるときも同じ") + " and one body line " + q("無権代理人の地位を共同相続したあと、本人の地位も単独で承継した者は、拒絶できない") + ".",
            "--- SMALL TAG (light gray, centered at the very bottom) ---", q("判例の考え方")]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 1 note card under it, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 on the arrow to the right and a red label on the arrow going down, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, that no arrow label is hidden, and that the gray card at the bottom is one separate card with no arrow.")

META = [
    (1, "代理権の濫用と無権代理（本人に効果は帰属するか）", "対比表型（2列）＋カード1枚", "1080×1800", "代理権の濫用と無権代理", "「結論」「中身の整理」の代理権の濫用・無権代理の箇条書きの直後", img1),
    (2, "無権代理人が本人を相続したら追認を拒絶できるかの判定フロー", "フローチャート型", "1080×2300", "無権代理人が本人を相続したら", "「たとえば」の直後（判断のしかたの前）", img2),
]

def build_doc():
    out = ["# 【M1-5】図解インフォグラフィック プロンプト（2枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M1-5】（代理権の濫用と無権代理の相続：本人に効果は帰属するのか）に差し込む図解のプロンプトです。1枚には収まらないため（代理権の濫用と、無権代理人の相続の2つの流れがあるため）2枚に分けました。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は総合記事の【M1-5】の節と、民法第107条・第113条1項（`note-articles/laws/minpou-1-soukyoku-bukken.md`で原文を確認）の範囲です。\n")
    checks = {
        1: ["文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない",
            "表は3列（行見出し・代理権の濫用・無権代理）×3行で、左右の文言が全行で違う（見出しが入れ替わっていない）",
            "表の下のカード（無権代理行為とみなされるのは）が1枚だけあり、表の一部になっていない",
            "✓・✕・青・赤が表のどこにもない／背景が透過でなく、カードの下に追加のまとめがない"],
        2: ["文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない",
            "開始1・注記カード1・ひし形2・結果の箱3で、ひし形は右に青い「はい」、下に赤いラベルが付いている",
            "結果1・2が青い箱、結果3が赤い箱で、文言が入れ替わっていない",
            "下の灰色のカード（地位が最終的に一人に集まるとき）が矢印のない別カードで、「判例の考え方」の小さなタグが一番下にある",
            "背景が透過でなく、最後のカードの下に追加のまとめがない"],
    }
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解：{t}\n")
        out.append(f"- 型：{typ}")
        out.append(f"- サイズ：{size}")
        out.append(f"- 保存名：`M1-5_{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせてください。\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("検品チェック：")
        out += [f"- {c}" for c in checks[n]]
        out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M1-5.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
