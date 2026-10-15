# 【M1-1】無効と取消しは何が違うのか：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2000", "This is a comparison table poster with three columns (対比表), followed by two note cards and one closing band."), TEXTREQ, BGREQ, COLOR] + \
           header("無効と取消しの違い", "三つの場面で比べる", "民法 総則（無効と取消し）") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this poster; use dark navy outlines and the pale yellow highlighter only for the strings marked as highlighted.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("無効") + "; the third header " + q("取消し") + ".",
            "Data row 1 (row label cell, dark navy, white text: " + q("追認したら") + "): second column " + q("追認しても、効力を生じない") + " with the small gray tag " + q("119条") + "; third column " + q("追認すれば、以後は取り消せない") + " with the small gray tag " + q("122条") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("時間がたつと") + "): second column " + q("何年たっても、有効にならない") + "; third column " + q("5年（行為の時から20年）で取消権が消える") + " on the first two lines and " + q("確定的に有効になる") + " on the next line, with the small gray tag " + q("126条") + ". In this third-column cell the string " + q("確定的に有効になる") + " has a pale yellow highlighter marker.",
            "Data row 3 (row label cell, dark navy, white text: " + q("主張できる人") + "): second column " + q("だれでも主張できる") + "; third column " + q("取消権者だけ") + " on the first line and " + q("本人・代理人・承継人など") + " on the second line, with the small gray tag " + q("120条") + ". In this third-column cell the string " + q("取消権者だけ") + " has a pale yellow highlighter marker.",
            "Every cell has its own text exactly as given; no two cells carry the same string.",
            "--- NOTE CARD 1 (a wide rounded card directly below the table, pale gray fill, dark navy outline) ---",
            "Heading (bold, ONE line): " + q("取り消すと"),
            "Body (ONE line): " + q("初めから無効だったものとみなされる") + " with the small gray tag " + q("121条") + ".",
            "Under the body, a small dark navy tag: " + q("将来に向かってだけ、ではない") + ".",
            "--- NOTE CARD 2 (a wide rounded card below note card 1, same style) ---",
            "Heading (bold, ONE line): " + q("無効と知って追認したとき"),
            "Body (ONE line): " + q("新たな行為をしたものとみなされる") + " with the small gray tag " + q("119条ただし書") + ".",
            "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below note card 2) ---",
            q("取消しのみ、と言い切る文は") + " on the first line and " + q("無効にも当てはまる性質かを確かめる") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 3 data rows, that the second and third columns of every row have different texts, that exactly two strings are highlighted in pale yellow (確定的に有効になる and 取消権者だけ), that there are exactly 2 note cards followed by exactly 1 closing band, that no check mark or cross mark appears anywhere, and that no blue or red is used anywhere.")

META = [(1, "無効と取消しの違い（三つの場面で比べる）", "対比表型（2列）", "1080×2000", "図解1_無効と取消しの違い", "【M1-1】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M1-1】無効と取消しは何が違うのか　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-1】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
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
    out.append("- 表は3列（行見出し・無効・取消し）×データ3行で、各セルの文字が指定どおりか（119条・122条・126条・120条・121条・119条ただし書の条番号を含む）。")
    out.append("- 黄色のマーカーが、「確定的に有効になる」と「取消権者だけ」の2か所だけか。青・赤・チェック・×が一つもないか。")
    out.append("- 表の下にカードが2枚、その下に濃紺の帯が1つだけで、帯のあとに何も描かれていないか。")
    out.append("- 簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-1.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
