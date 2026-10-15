# 【M1-8】条件：追加の図解「既成条件の早見表（成就済み／不成就の確定 × 停止条件／解除条件）」1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-8.py）の判定フローは、契約の時にすでに成就していた場合（131条1項）だけを扱い、記事の「中身の整理」にある、成就しないことがすでに確定していた場合（131条2項）が図にないため補う。
# 実行: python3 gen_infographic_M1-8_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x1800", "This is a comparison table poster with three columns (早見表), followed by one note card and one closing band."), TEXTREQ, BGREQ,
            "Draw no check mark and no cross mark, and use no blue or red anywhere in this poster; use dark navy outlines and the pale yellow highlighter only for the strings marked as highlighted."] + \
           header("既成条件は、どうなる？", "成就済みか、不成就の確定か", "民法 第131条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 2 data rows, no merged cells.",
            "Header row (dark navy cells with white text), from left to right: the first cell is " + q("契約の時に、すでに") + "; the second header " + q("停止条件") + "; the third header " + q("解除条件") + ".",
            "Data row 1 (row label cell, dark navy, white text: " + q("成就していた") + " with the small light-gray tag " + q("131条1項") + " under it): second column " + q("無条件（有効）") + "; third column " + q("無効") + ". In this row the string " + q("無条件（有効）") + " has a pale yellow highlighter marker.",
            "Data row 2 (row label cell, dark navy, white text: " + q("成就しないと確定していた") + " with the small light-gray tag " + q("131条2項") + " under it): second column " + q("無効") + "; third column " + q("無条件（有効）") + ". In this row the string " + q("無条件（有効）") + " has a pale yellow highlighter marker.",
            "The strings " + q("無条件（有効）") + " and " + q("無効") + " each appear twice in the table on purpose, in diagonal positions (row 1 second column and row 2 third column hold " + q("無条件（有効）") + "; row 1 third column and row 2 second column hold " + q("無効") + "); draw each cell exactly as given and do not merge or swap any cells.",
            "--- NOTE CARD (a wide rounded card directly below the table, pale gray fill, dark navy outline, with NO arrow) ---",
            "Heading (bold, ONE line): " + q("成就した時から、とは別の問い") + ".",
            "Body (ONE line): " + q("ここで決まるのは、契約の時にすでに決まっていた場合の扱い") + ".",
            "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the note card) ---",
            q("不成就が確定していたら、") + " on the first line and " + q("成就済みの場合と結論が逆になる") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 2 data rows, that row 1 reads 無条件（有効） then 無効 and row 2 reads 無効 then 無条件（有効）, that exactly two cells are highlighted in pale yellow (the two 無条件（有効） cells), that there is exactly 1 note card followed by exactly 1 closing band, that no check mark or cross mark appears anywhere, and that no blue or red is used anywhere.")

META = [(1, "既成条件の早見表（成就済みか、不成就の確定か）", "対比表型（2×2）＋カード1枚＋帯", "1080×1800", "民法編1_M1-8_追加_既成条件の早見表", "【M1-8】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M1-8】条件：追加の図解「既成条件の早見表」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-8】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-8.md`）の判定フローは「契約の時にすでに成就していた場合」だけを扱うので、記事の「中身の整理」にある「成就しないことがすでに確定していた場合」（131条2項）を、2×2の早見表で補います。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は早見表で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append(f"保存名：`{fn}.png`\n")
    out.append("## 検品チェック\n")
    out.append("- 表は3列（行見出し・停止条件・解除条件）×データ2行で、1行目が「無条件（有効）」「無効」、2行目が「無効」「無条件（有効）」と斜めに入れ替わっているか。")
    out.append("- 黄色のマーカーが、2つの「無条件（有効）」のセルだけか。条番号（131条1項・131条2項）が行見出しの下に付いているか。")
    out.append("- 表の下にカードが1枚、その下に濃紺の帯が1つだけで、帯のあとに何も描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-8_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
