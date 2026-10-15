# 【M3-5】地上権は、承諾なしで譲渡でき、地代は約束があって初めて生じる：図解インフォグラフィック1枚のプロンプトを組み立てる
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

def img1():
    body = [lead("1080x1900", "This is a comparison table poster (対比表) with a short card below the table."), TEXTREQ, BGREQ, COLOR] + \
           header("地上権と賃借権の違い", "承諾・地代・時効取得で整理する", "民法 第265条・第266条・第369条・第601条・第612条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("地上権") + " with a small light-gray tag " + q("物権") + " under it; the third header " + q("賃借権") + " with a small light-gray tag " + q("債権") + " under it.",
            "Data row 1 (row label cell, dark navy, white text: " + q("どんな権利？") + "): second column " + q("工作物や竹木を所有するため、他人の土地を使う権利") + "; third column " + q("賃料を払って、土地を使わせてもらう権利") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("譲渡するとき") + "): second column " + q("所有者の承諾なしに譲渡できる") + " with the words " + q("承諾なしに") + " in a pale yellow highlighter marker, and a second smaller line " + q("抵当権も設定できる") + "; third column " + q("賃貸人の承諾を得なければ譲渡できない") + " with the words " + q("承諾を得なければ") + " in a pale yellow highlighter marker.",
            "Data row 3 (row label cell, dark navy, white text: " + q("地代・賃料") + "): second column " + q("設定契約で定めて初めて生じる") + " with the words " + q("定めて初めて") + " in a pale yellow highlighter marker, and a second smaller line " + q("無償もあり、裁判所が額を定める制度はない") + "; third column " + q("賃料の支払が契約の前提") + ".",
            "The second-column and third-column cells of each data row have clearly different texts; the texts are NOT identical, so copy each cell exactly as given.",
            "--- CARD BELOW THE TABLE ---",
            "One wide rounded card below the table, pale gray fill with a dark navy outline, with a dark navy heading " + q("地上権の時効取得") + " and two short body lines: " + q("土地を使い続けている外形的な事実") + " and " + q("地上権を行使する意思が、外から分かること") + ". Beside the heading, a small icon of a house on a plot of land. This card has no check mark and no cross, and it is NOT part of the table."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 3 data rows, that every cell reads exactly as given, that the second and third columns differ in every row, that the card below the table appears once, and that no check mark or cross mark appears anywhere.")

META = [(1, "地上権と賃借権の違い（承諾・地代・時効取得）", "対比表型（2列＋カード1枚）", "1080×1900", "地上権と賃借権の違い_M3-5", "総合記事【M3-5】の「結論」の直後（または「中身の整理」の終わり）", img1)]

def build_doc():
    out = ["# 【M3-5】図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M3-5】（地上権は、承諾なしで譲渡でき、地代は約束があって初めて生じる）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は記事（`h21-mondai/q02-chijouken.md`）と法令DB（`note-articles/laws/`）の範囲です。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"- 図解：{t}")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせてください。\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("検品チェック：")
        out.append("- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない")
        out.append("- 表は3列（行見出し・地上権・賃借権）×3行で、左右の文言が全行で違う（取り違えていない）")
        out.append("- 「物権」は地上権の列、「債権」は賃借権の列の見出しの下にある（入れ替わっていない）")
        out.append("- 表の下のカード（地上権の時効取得）が1枚だけあり、表の一部になっていない")
        out.append("- ✓・✕・青・赤が表のどこにもない／背景が透過でなく、最後のカードの下に追加のまとめがない\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M3-5.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
