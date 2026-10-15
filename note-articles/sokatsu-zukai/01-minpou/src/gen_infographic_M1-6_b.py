# 【M1-6】取得時効：追加の図解「時効取得と登記の時間軸」1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-6.py）は判定の流れ図と早見表で、「時効の完成」を境にした時間軸の上で、元の所有者・完成前の第三者・完成後の第三者がどこにいるかを示す図がないため補う。
# 実行: python3 gen_infographic_M1-6_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

MINI = ("Mini timeline at the left of the card: a short horizontal dark navy line with one small flag labeled " + q("完成") + " at its middle; ")

def card(i, heading, mini, items, tag, small=None):
    out = [f"--- CARD {i} (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number {i}, numbers run 1 to 3 in order) ---",
           "Heading (bold, ONE line):", q(heading), mini,
           "Item line (one short line of dark navy text with a small dark navy dot at its left end, NO number on the dot):", q(items),
           "Conclusion tag (a short pale-yellow banner directly below the item line, a keyword phrase, not a sentence):", q(tag)]
    if small:
        out.append("Small gray tag under the conclusion tag: " + q(small) + ".")
    return out

def img1():
    body = [lead("1080x2300", "This is a timeline poster: one wide timeline panel at the top followed by three numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the timeline panel. Every card has one heading, one mini timeline, one item line and one conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + \
           header("時効取得と登記", "時効の完成の前か後かで決まる", "民法 第162条（判例の考え方）") + \
           ["--- TIMELINE PANEL (a wide rounded white panel directly below the header, dark navy outline) ---",
            "A single horizontal dark navy arrow runs left to right across the panel with exactly three milestone flags on it, each with a one-line label under the flag, in this order: " + q("占有の開始") + ", " + q("時効の完成") + ", " + q("時効取得を主張する") + ".",
            "The segment between the first and second flags has the bracket label " + q("完成の前") + "; the segment between the second and third flags has the bracket label " + q("完成の後") + ".",
            "At the far left above the arrow: a faceless person pictogram with the dark navy name tag " + q("占有者") + ". Above the first segment: a small pin and a faceless person pictogram with the name tag " + q("第三者") + " and the label " + q("所有権を得た") + ". Above the second segment: another pin and a faceless person pictogram with the name tag " + q("第三者") + " and the label " + q("所有権を得た") + ". The two " + q("第三者") + " pictograms are the same text on purpose; draw the same string in both.",
            "Below the arrow, spanning its whole length (under all three flag labels, with at least 20 px of space), one thin dotted bracket with a faceless person pictogram at its left end with the dark navy name tag " + q("元の所有者") + "."]
    body += card(1, "元の所有者に対して",
                 MINI + "no pin on it, and one faceless person pictogram with the dark navy name tag " + q("元の所有者") + " beside the mini timeline.",
                 "時効の当事者で、対抗関係に立たない", "登記なしで主張できる")
    body += card(2, "完成の前の第三者に対して",
                 MINI + "a small pin is placed on the left of the 完成 flag.",
                 "元の所有者と同じ立場（当事者類似）", "登記なしで主張できる", "判例の考え方")
    body += card(3, "完成の後の第三者に対して",
                 MINI + "a small pin is placed on the right of the 完成 flag.",
                 "第三者との間で対抗関係に立つ", "登記の先後で決まる", "判例の考え方")
    body += ["The conclusion tag " + q("登記なしで主張できる") + " appears in both CARD 1 and CARD 2 on purpose; the headings, item lines and mini timelines of the three cards are different, so copy each exactly as given.",
             "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below card 3) ---",
             q("相手と、第三者が所有権を得た時点で") + " on the first line and " + q("登記が要るかが決まる") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the timeline panel has exactly 3 flags in the order 占有の開始, 時効の完成, 時効取得を主張する, with the labels 完成の前 and 完成の後 on the two segments, that there are exactly 3 numbered cards followed by exactly 1 closing band, that the mini timeline pin is absent in card 1, on the left of the flag in card 2 and on the right of the flag in card 3, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band.")

META = [(1, "時効取得と登記：完成の前か後かの時間軸", "時間軸型（時間軸パネル＋カード3枚＋帯）", "1080×2300", "民法編1_M1-6_追加_時効取得と登記の時間軸", "【M1-6】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M1-6】取得時効：追加の図解「時効取得と登記の時間軸」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-6】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-6.md`）は判定の流れ図と早見表なので、時効の完成を境にした時間軸の上で、元の所有者・完成の前の第三者・完成の後の第三者がどこにいるかを示します。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1〜3は図の部品です）。キャラクターは描きません。\n")
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
    out.append("- 時間軸パネルの旗が3つ（占有の開始・時効の完成・時効取得を主張する）で、2つの区間に「完成の前」「完成の後」の括弧があるか。第三者の人物が2人（区間ごとに1人）描かれているか。")
    out.append("- カードがちょうど3枚で、ミニ時間軸の目印（ピン）が、カード1はなし、カード2は完成の旗の左、カード3は右か。")
    out.append("- 「登記なしで主張できる」がカード1とカード2にあり、カード3は「登記の先後で決まる」か。カード2・3に「判例の考え方」の札があるか。")
    out.append("- 濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-6_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
