# 【M1-4】錯誤・詐欺による取消し：追加の図解「詐欺の取消しと第三者（取り消せるか、対抗できるか）」1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-4.py）はカード4枚の個別の整理で、「第三者が取消しの前に現れる」という時の流れと、取消しの可否・対抗の可否の2つの問いを1枚で見られる関係図がないため補う。
# 実行: python3 gen_infographic_M1-4_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2200", "This is a timeline-and-relationship poster: a horizontal timeline with three milestones, two result cards side by side, one note card and one closing band."),
            TEXTREQ, BGREQ, NOCOLOR] + \
           header("取り消せるか、対抗できるか", "詐欺では二つの問いを分ける", "民法 第96条") + \
           ["--- TIMELINE (a wide rounded white panel directly below the header, dark navy outline) ---",
            "A single horizontal dark navy arrow runs left to right across the panel, with exactly three round milestone dots on it, each with a one-line label under the dot, in this order from left to right: " + q("詐欺による売買") + ", " + q("転売") + ", " + q("取消し") + ".",
            "Above the first milestone: two faceless person pictograms side by side with the dark navy name tags " + q("だまされた売主") + " and " + q("だました買主") + ".",
            "Above the second milestone: one faceless person pictogram holding a small shield, with the dark navy name tag " + q("善意でかつ過失のない第三者") + " and a small gray tag " + q("転得者・抵当権者など") + " under the name tag.",
            "Above the third milestone: a rubber stamp icon labeled " + q("取消し") + ".",
            "--- TWO RESULT CARDS (directly below the timeline, side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "Left card: a small dark navy tag " + q("売主と買主の間では") + ", the heading (bold) " + q("取り消せる") + ", and a small gray tag " + q("96条1項") + ".",
            "Right card: a small dark navy tag " + q("第三者に対しては") + ", the heading (bold) " + q("対抗できない") + ", a small gray tag " + q("96条3項") + ", and one body line " + q("第三者は、登記がなくても守られる（判例）") + ".",
            "The two cards have clearly different texts; the texts are NOT identical, so copy each exactly as given.",
            "--- NOTE CARD (a wide rounded card below the two result cards, pale gray fill, dark navy outline, with NO arrow) ---",
            "Heading (bold, ONE line): " + q("錯誤による取消しも、第三者の保護は同じ") + ".",
            "Body (ONE line): " + q("善意でかつ過失がない第三者に対抗できない") + " with the small gray tag " + q("95条4項") + ".",
            "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the note card) ---",
            q("取消しができることと、") + " on the first line and " + q("第三者に対抗できないことは別の問い") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the timeline has exactly 3 milestones in the order 詐欺による売買, 転売, 取消し, that the third-party pictogram is above the second milestone (before the cancellation), that there are exactly 2 result cards side by side, exactly 1 note card and exactly 1 closing band in this order, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band.")

META = [(1, "取り消せるか、対抗できるか（詐欺の取消しと第三者の関係図）", "関係図型（時の流れ＋結果カード2枚）", "1080×2200", "民法編1_M1-4_追加_取り消せるか対抗できるか", "【M1-4】の「たとえば」の直後", img1)]

def build_doc():
    out = ["# 【M1-4】錯誤・詐欺による取消し：追加の図解「取り消せるか、対抗できるか」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-4】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-4.md`）はカード4枚の個別の整理なので、第三者が取消しの前に現れるという時の流れと、「取消しの可否」「第三者への対抗の可否」の2つの問いを、1枚の関係図で補います。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
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
    out.append("- 時の流れの上の里程標が3つ（詐欺による売買・転売・取消し）で、第三者の人物が「転売」の上（取消しより前）に描かれているか。")
    out.append("- 結果のカードが左右2枚（取り消せる／対抗できない）で、右のカードに「第三者は、登記がなくても守られる（判例）」があるか。条番号（96条1項・96条3項・95条4項）が指定どおりか。")
    out.append("- 注記のカード1枚、濃紺の帯1つの順で終わり、そのあとに何も描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-4_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
