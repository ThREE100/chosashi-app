# 【M1-5】代理権の濫用と無権代理の相続：追加の図解「地位はだれに集まるか」（4つの場面の関係図）1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-5.py）の図解2は判定の流れ図で、「本人の地位」と「無権代理人の地位」がだれに移るかを示す関係図がなく、無権代理人の地位を共同相続した後に本人の地位を単独承継する場面は小さな注記だけなので補う。
# 実行: python3 gen_infographic_M1-5_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def card(i, heading, diagram, tag):
    return [f"--- SCENARIO CARD {i} (a wide rounded card, pale gray fill, dark navy outline; badge: a filled dark navy circle containing the number {i}, numbers run 1 to 4 in order) ---",
            "Heading (bold, ONE line):", q(heading), "Diagram: " + diagram,
            "Conclusion tag (a short pale-yellow banner directly below the diagram, a keyword phrase, not a sentence):", q(tag)]

def img1():
    body = [lead("1080x2600", "This is a relationship-diagram poster with four scenario cards stacked in one column, each drawing who inherits which position; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the person pictograms, arrows and short labels plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + \
           header("無権代理と相続", "地位はだれに集まるか", "民法 第113条1項（判例の考え方）")
    body += card(1, "無権代理人が、本人を単独で相続した",
                 "Two faceless person pictograms in one row. Left: a pictogram drawn with a thin dotted outline (faded) with the dark navy name tag " + q("本人") + " and a small gray tag " + q("死亡") + ". Right: a pictogram with the dark navy name tag " + q("無権代理人") + ". A solid dark navy arrow runs from the left to the right with the label " + q("相続") + ". Above the right pictogram, two small round badges are stacked together on the same person: " + q("本人の地位") + " and " + q("無権代理人の地位") + ".",
                 "二つの地位が融合する")
    body += card(2, "無権代理人が、他の相続人とともに本人を相続した",
                 "Three faceless person pictograms. Left: a faded pictogram (thin dotted outline) with the dark navy name tag " + q("本人") + " and a small gray tag " + q("死亡") + ". Right, one above the other: a pictogram with the dark navy name tag " + q("無権代理人") + " and a pictogram with the dark navy name tag " + q("他の相続人") + ". Two solid dark navy arrows run from the left pictogram to each of the two right pictograms with the label " + q("共同相続") + ". A thin bracket encloses the two right pictograms with the label " + q("追認は全員でする") + ".",
                 "全員で追認を拒絶できる")
    body += card(3, "本人が追認を拒絶したあとに、無権代理人が相続した",
                 "Two faceless person pictograms in one row. Left: a faded pictogram (thin dotted outline) with the dark navy name tag " + q("本人") + " and a small gray tag " + q("死亡") + "; in front of it a paper sheet labeled " + q("追認拒絶") + " with a closed padlock icon, placed before the arrow. Right: a pictogram with the dark navy name tag " + q("無権代理人") + ". A solid dark navy arrow runs from the left to the right with the label " + q("相続") + ".",
                 "拒絶は確定している")
    body += card(4, "無権代理人の地位を共同相続したあと、本人の地位も単独で承継した",
                 "Four faceless person pictograms. At the top left, a faded pictogram (thin dotted outline) with the dark navy name tag " + q("無権代理人") + " and a small gray tag " + q("死亡") + "; at the bottom left, a faded pictogram with the dark navy name tag " + q("本人") + " and a small gray tag " + q("死亡") + ". At the right, one above the other: a pictogram with the dark navy name tag " + q("承継した者") + " and a pictogram with the dark navy name tag " + q("他の共同相続人") + ". From the top-left faded pictogram, two solid arrows labeled " + q("共同相続") + " go to both right pictograms. From the bottom-left faded pictogram, one solid arrow labeled " + q("単独で承継") + " goes only to the " + q("承継した者") + " pictogram. Above the " + q("承継した者") + " pictogram, two small round badges are stacked together: " + q("無権代理人の地位") + " and " + q("本人の地位") + ".",
                 "両方の地位が一人に集まる")
    body += ["The four conclusion tags are four different texts; copy each exactly as given and do not copy one into another."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of scenario cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, that there is no intro illustration or paragraph block between the header and the cards, that no card contains a full sentence of explanatory prose, that the deceased persons are drawn faded with a thin dotted outline, and that no check mark, cross mark, blue or red appears anywhere.")

META = [(1, "無権代理と相続：地位はだれに集まるか（4つの場面の関係図）", "関係図型（シナリオカード4枚）", "1080×2600", "民法編1_M1-5_追加_地位はだれに集まるか", "【M1-5】の「たとえば」の直後（図解2の判定フローの次）", img1)]

def build_doc():
    out = ["# 【M1-5】代理権の濫用と無権代理の相続：追加の図解「地位はだれに集まるか」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-5】に追加で差し込む図解のプロンプトです。既存の図解2（`prompt_infographic_M1-5.md`）は判定の流れ図なので、「本人の地位」と「無権代理人の地位」がだれに移るかを、4つの場面の関係図で補います（無権代理人の地位を共同相続した後に本人の地位を単独承継する場面は、既存の図では小さな注記だけでした）。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は関係図で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの番号1〜4は図の部品です）。キャラクターは描きません。\n")
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
    out.append("- カードがちょうど4枚で、番号が1〜4の順か。死亡した人物が薄い点線の輪郭で描かれ、「死亡」の札が付いているか。")
    out.append("- カード1は「本人の地位」「無権代理人の地位」の2つの丸札が同じ人物に重なっているか。カード2は相続人が2人で、括弧の文言が「追認は全員でする」か。")
    out.append("- カード3は「追認拒絶」の札と南京錠が、相続の矢印の手前にあるか。カード4は「共同相続」の矢印が2本、「単独で承継」の矢印が1本（承継した者へだけ）か。")
    out.append("- 導入のイラスト・文章の段落・まとめの帯が、カードの前後に描かれていないか。青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-5_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
