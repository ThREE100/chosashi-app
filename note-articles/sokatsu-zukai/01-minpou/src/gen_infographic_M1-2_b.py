# 【M1-2】制限行為能力者：追加の図解「追認できるのは、いつか」の判定フロー1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-2.py）のカード3は、原則と「同意を得た追認」の2行だけで、法定代理人・保佐人・補助人が自ら追認する場合（124条2項1号）と成年被後見人の除外が図にないため補う。
# 実行: python3 gen_infographic_M1-2_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2300", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
           header("追認できるのは、いつ？", "だれが追認するかで分かれる", "民法 第124条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, SMALL NOTE, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, with at least 60 px of empty space between each diamond and its box so that the arrow label stays visible. The wide note card sits at the very bottom. All arrows are straight or have at most one right-angle bend and never cross each other. Do not draw any arrow that returns to an earlier node.",
            "NODE START (rounded pill, dark navy): " + q("取り消すことができる行為を追認する"),
            "NODE SMALL NOTE (a small gray card directly below START, with no arrow of its own): " + q("状況とは、取消しの原因となっていた状況のこと") + ".",
            "NODE DIAMOND 1: " + q("追認するのは、法定代理人・保佐人・補助人か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
            "NODE DIAMOND 2: " + q("同意を得て追認する、成年被後見人以外の制限行為能力者か？") + " The text is placed inside the diamond on 4 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow right to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow down to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (blue box): " + q("状況の消滅後でなくてよい") + " on the first line and " + q("法定代理人らが自ら追認する場合") + " on the next line, with the small gray tag " + q("124条2項1号") + " under the text.",
            "NODE RESULT 2 (blue box): " + q("状況の消滅後でなくてよい") + " on the first line and " + q("同意を得た追認は、成年前でもできる") + " on the next two lines, with the small gray tag " + q("124条2項2号") + " under the text.",
            "NODE RESULT 3 (red box): " + q("原則どおり") + " on the first line and " + q("状況が消え、取消権を知った後でなければ追認できない") + " on the next three lines, with the small gray tag " + q("124条1項") + " under the text.",
            "Counts: 1 start node, 1 small note, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The first lines of RESULT 1 and RESULT 2 are the same string on purpose; the second lines of the three result boxes are NOT identical, so copy each exactly as given.",
            "--- NOTE CARD AT THE BOTTOM (one wide separate card below RESULT 3, pale gray fill, dark navy outline, neutral dark navy text, with NO arrow) ---",
            "Heading (bold, ONE line): " + q("成年被後見人は、同意を得ても例外にならない") + ".",
            "Body (ONE line): " + q("どの場合も、取消権を有することを知った後であることは必要") + ", with the small gray tag " + q("124条") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 1 small note, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 on the arrow to the right and a red 「いいえ」 on the arrow going down, that RESULT 1 and RESULT 2 are blue and RESULT 3 is red, that no text overflows its box, that no arrow label is hidden, and that the note card at the bottom is one separate card with no arrow.")

META = [(1, "追認できるのは、いつか（だれが追認するかで分かれる判定フロー）", "フローチャート型", "1080×2300", "民法編1_M1-2_追加_追認はいつできるか", "【M1-2】の「判断のしかた」の直後", img1)]

def build_doc():
    out = ["# 【M1-2】制限行為能力者：追加の図解「追認できるのは、いつか」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-2】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-2.md`）のカード3が原則と「同意を得た追認」の2行だけなので、法定代理人・保佐人・補助人が自ら追認する場合と成年被後見人の除外を、判定の流れ図で補います。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、はい＝青、いいえ＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
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
    out.append("- 開始の楕円が1つ、その下に灰色の小さな注記が1つ、ひし形が2つ、結果の箱が3つ（青2・赤1）か。ひし形ごとに青の「はい」（右向き）と赤の「いいえ」（下向き）が付いているか。")
    out.append("- 結果1と結果2の1行目が同じ文字列（状況の消滅後でなくてよい）で、2行目が別の文言か。条番号（124条2項1号・124条2項2号・124条1項・124条）が指定どおりか。")
    out.append("- 結果の箱のあとに矢印が出ていないか。下の注記のカードが1枚だけで、矢印でつながれていないか。")
    out.append("- 簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-2_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
