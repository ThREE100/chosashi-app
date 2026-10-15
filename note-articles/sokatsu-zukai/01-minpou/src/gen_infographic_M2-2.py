# 【M2-2】占有の善意・悪意と占有の移転は、誰を基準に、いつから考えるのか：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2100", "This is a comparison table poster with three data columns (対比表) and an illustration row at the top of the table."), TEXTREQ, BGREQ, COLOR] + \
           header("占有の善意と悪意", "いつから・誰を・誰が", "民法 第189条・第184条") + \
           ["--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three data columns) and exactly 4 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("いつから悪意とみなす？") + "; the third header " + q("善意・悪意は誰を基準に？") + "; the fourth header " + q("承諾するのは誰？") + ".",
            "Data row 1 (row label cell, dark navy, white text: " + q("イメージ") + "): this row is taller than the others and holds one small flat illustration per column, drawn only with the labels given here.",
            "  - Second column illustration: a horizontal timeline with three markers from left to right labeled " + q("占有の開始") + ", " + q("訴えの提起") + " and " + q("敗訴") + "; the middle marker " + q("訴えの提起") + " has a pale yellow highlighter marker and a small tag " + q("ここから悪意") + " above it.",
            "  - Third column illustration: two faceless pictograms side by side in the same light gray-blue color with dark navy tags " + q("本人") + " and " + q("占有代理人") + "; under the first a small label " + q("善意") + " and under the second a small label " + q("悪意") + "; a small caption under both: " + q("悪意の占有として扱う") + ".",
            "  - Fourth column illustration: three faceless pictograms in a row in the same light gray-blue color with dark navy tags " + q("本人") + ", " + q("占有代理人") + " and " + q("第三者") + "; one dark navy arrow from the first to the second carrying the small label " + q("命じる") + ", and a small speech tag " + q("承諾") + " beside the third; under the third a small label " + q("占有権を取得") + ".",
            "Data row 2 (row label cell, dark navy, white text: " + q("答え") + "): second column " + q("訴えの提起の時から、悪意とみなす") + " with the part " + q("訴えの提起の時") + " in a pale yellow highlighter marker; third column " + q("占有代理人について決める") + " with the part " + q("占有代理人") + " in a pale yellow highlighter marker; fourth column " + q("第三者が承諾すると、第三者が占有権を取得する") + " with the part " + q("第三者が承諾") + " in a pale yellow highlighter marker.",
            "Data row 3 (row label cell, dark navy, white text: " + q("取り違えやすい点") + "): second column " + q("占有の開始の時と取り違える") + "; third column " + q("本人を基準にしてしまう") + "; fourth column " + q("占有代理人の承諾と取り違える") + ".",
            "Data row 4 (row label cell, dark navy, white text: " + q("根拠") + "): second column " + q("民法189条2項") + "; third column " + q("判例・通説の理解") + "; fourth column " + q("民法184条") + ". These three cells use a smaller font in a light-gray tag style.",
            "Every cell has its own text exactly as given; no two cells carry the same string. Exactly three strings are highlighted in pale yellow in data row 2, and one more in the timeline illustration.",
            "The table is the last element of the poster."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 4 data rows, that every cell reads exactly as given, that the illustration row uses only the labels listed, that no check mark, cross mark, blue, or red appears anywhere, and that the table is the last element of the poster.")

META = [(1, "占有の善意と悪意（いつから・誰を・誰が）", "対比表型（3列）＋イメージ行", "1080×2100", "図解1_占有の善意と悪意", "【M2-2】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M2-2】占有の善意・悪意と占有の移転は、誰を基準に、いつから考えるのか　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M2-2】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
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
    out.append("- 表は4列（行見出し・3つの問い）×データ4行で、各セルの文字が指定どおりか（民法189条2項・判例・通説の理解・民法184条）。")
    out.append("- 「イメージ」の行の3つの絵が、指定のラベルだけで描かれているか（時間軸の3つの印、本人と占有代理人の2人、本人・占有代理人・第三者の3人と「命じる」の矢印1本）。")
    out.append("- 黄色のマーカーが、「答え」の行の3か所と、時間軸の「訴えの提起」だけか。青・赤・チェック・×が一つもないか。")
    out.append("- 表のあとに、まとめ・帯・追加の文字ブロックが描かれていないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-2.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
