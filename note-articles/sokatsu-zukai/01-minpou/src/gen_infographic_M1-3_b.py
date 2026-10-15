# 【M1-3】心裡留保・虚偽表示：追加の図解「仮装売買の登場人物の関係図」1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-3.py）は判定の流れ図で、転得者と相続人が「元の所有者」「仮装の買主」とどういう関係にあるかの当事者関係図がないため補う。
# 実行: python3 gen_infographic_M1-3_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2100", "This is a relationship-diagram poster with two scenario cards stacked in one column and one closing band; every card draws three faceless person pictograms in a row."),
            TEXTREQ, BGREQ, NOCOLOR] + \
           header("仮装売買の登場人物", "だれが「第三者」になるか", "民法 第94条2項") + \
           ["--- SCENARIO CARD 1 (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number 1) ---",
            "Heading (bold, ONE line): " + q("仮装の買主が、他の人に転売した") + ".",
            "Diagram (three faceless person pictograms in one row, left to right):",
            "  - Left pictogram with the dark navy name tag " + q("元の所有者") + ".",
            "  - Middle pictogram with the dark navy name tag " + q("仮装の買主") + ". Between the left and middle pictograms, a dotted double-headed arrow with the label " + q("通じて仮装売買") + " and a small gray tag " + q("無効") + " under it.",
            "  - Right pictogram with the dark navy name tag " + q("転得者（善意）") + ", holding a small shield. A solid dark navy arrow runs from the middle pictogram to the right pictogram with the label " + q("転売") + ". Under the right pictogram, a small registry ledger icon with the label " + q("登記がなくても守られる（判例）") + ".",
            "Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence): " + q("第三者として守られる") + ", with the small gray tag " + q("94条2項") + " beside it.",
            "--- SCENARIO CARD 2 (a wide rounded card below scenario card 1, same style; badge: a filled dark navy circle containing the number 2) ---",
            "Heading (bold, ONE line): " + q("仮装の買主が死亡し、子が単独で相続した") + ".",
            "Diagram (three faceless person pictograms in one row, left to right):",
            "  - Left pictogram with the dark navy name tag " + q("元の所有者") + ".",
            "  - Middle pictogram drawn with a thin dotted outline (faded) with the dark navy name tag " + q("仮装の買主") + " and a small gray tag " + q("死亡") + ". Between the left and middle pictograms, a dotted double-headed arrow with the label " + q("通じて仮装売買") + ".",
            "  - Right pictogram with the dark navy name tag " + q("子（相続人）") + ". A solid dark navy arrow runs from the middle pictogram to the right pictogram with the label " + q("相続") + ". One thin dark navy bracket encloses the middle and right pictograms together, with the label " + q("買主の地位を、まるごと引き継ぐ") + ".",
            "Under the diagram, one small dotted-outline tag (no check mark, no cross): " + q("善意でも、第三者ではない") + ".",
            "Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence): " + q("第三者に当たらない") + ", with the small gray tag " + q("896条") + " beside it.",
            "The two scenario cards use the same three-pictogram layout and the same name tag " + q("元の所有者") + " on purpose, but their headings, the right-hand name tags and the conclusion tags are different texts; copy each exactly as given.",
            "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below scenario card 2) ---",
            q("新たに独立の利害関係をもった者だけが、") + " on the first line and " + q("善意の第三者として守られる") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 2 scenario cards followed by exactly 1 closing band, that each card has exactly 3 person pictograms in one row, that card 1 shows the right-hand name tag 転得者（善意） and card 2 shows the right-hand name tag 子（相続人）, that the middle pictogram of card 2 is faded with the tag 死亡, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band.")

META = [(1, "仮装売買の登場人物（だれが第三者になるか）", "関係図型（シナリオカード2枚＋帯）", "1080×2100", "民法編1_M1-3_追加_仮装売買の登場人物", "【M1-3】の「たとえば」の直後", img1)]

def build_doc():
    out = ["# 【M1-3】心裡留保・虚偽表示：追加の図解「仮装売買の登場人物」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-3】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-3.md`）は判定の流れ図なので、転得者と相続人が「元の所有者」「仮装の買主」とどういう関係にあるかを、当事者関係図で補います。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は関係図で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1・2は図の部品です）。キャラクターは描きません。\n")
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
    out.append("- シナリオのカードがちょうど2枚で、それぞれに人物のピクトグラムが3つ横に並んでいるか。カード1の右が「転得者（善意）」、カード2の右が「子（相続人）」か。")
    out.append("- カード2の中央（仮装の買主）が薄い点線の輪郭で「死亡」の札が付いているか。「相続」の矢印と、中央と右をまとめる括弧の文言（買主の地位を、まるごと引き継ぐ）があるか。")
    out.append("- 条番号（94条2項・896条）と、「登記がなくても守られる（判例）」が指定どおりか。濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-3_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
