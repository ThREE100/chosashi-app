# 【M1-3】心裡留保・虚偽表示：善意の第三者は何を満たせば守られるのか：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 実行: python3 gen_infographic_M1-3.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2500", "This is a flowchart poster (判定フロー) followed by one note card."), TEXTREQ, BGREQ, COLOR] + \
           header("善意の第三者は守られる？", "上から順に確かめる", "民法 総則（意思表示）") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, DIAMOND 3. Every red result box (RESULT 1 and RESULT 2) sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The two final blue result boxes sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 3. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy): " + q("無効や取消しを、第三者に対抗できるか"),
            "NODE DIAMOND 1: " + q("その人は、新たに取引に入った第三者か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box): " + q("第三者に当たらない") + " on the first line and " + q("当事者・包括承継人（相続人）は守られない") + " on the next two lines.",
            "NODE DIAMOND 2: " + q("その第三者は、善意か？") + " The text is placed inside the diamond on 2 lines.",
            "  - Arrow down to DIAMOND 3 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (red box): " + q("善意でないと守られない") + " on the first line and " + q("無効や取消しを対抗できる") + " on the second line.",
            "NODE DIAMOND 3: " + q("原因は、心裡留保・虚偽表示か、詐欺・錯誤か？") + " This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red); do not draw the strings 「はい」 or 「いいえ」 on these two arrows. The text is placed inside the diamond on 3 lines.",
            "  - Arrow down-left with the label " + q("心裡留保・虚偽表示") + " to RESULT 3.",
            "  - Arrow down-right with the label " + q("詐欺・錯誤") + " to RESULT 4.",
            "NODE RESULT 3 (blue box): " + q("善意だけで守られる") + " on the first line and " + q("過失があってもよい") + " on the second line, with the small gray tag " + q("93条2項・94条2項") + ".",
            "NODE RESULT 4 (blue box): " + q("善意でかつ過失がないとき守られる") + " on the first two lines, with the small gray tag " + q("96条3項・95条4項") + ".",
            "Counts: 1 start node, 3 diamonds, 4 result boxes (RESULT 1 and RESULT 2 red, RESULT 3 and RESULT 4 blue), 4 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The two blue result boxes have different texts (the strings " + q("善意だけで守られる") + " and " + q("善意でかつ過失がないとき守られる") + " are NOT identical); do not copy one into the other.",
            "--- NOTE CARD (a wide rounded card directly below the flowchart, pale gray fill, dark navy outline, with NO arrow connecting it to any node, and no blue or red) ---",
            "Heading (bold, ONE line): " + q("虚偽表示の第三者は"),
            "Body (ONE line): " + q("登記がなくても守られる（判例）") + ".",
            "Under the body, a small dark navy tag: " + q("相続人は、善意でも第三者でない") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 3 diamonds and 4 result boxes, that DIAMOND 1 and DIAMOND 2 each show a blue 「はい」 and a red 「いいえ」, that DIAMOND 3 shows only the two navy labels 「心裡留保・虚偽表示」 and 「詐欺・錯誤」, that RESULT 1 and RESULT 2 are red and RESULT 3 and RESULT 4 are blue, that there is exactly one note card below the flowchart and it is not connected by any arrow, that no text overflows its box, and that no arrow label is hidden. Confirm that the second character of 心裡留保 is drawn exactly as 裡 (clothing radical on the left, 里 on the right) everywhere it appears.")

META = [(1, "善意の第三者は守られるかの判定フロー", "フローチャート型", "1080×2500", "図解1_善意の第三者は守られるかの判定フロー", "【M1-3】の「判断のしかた」の直後", img1)]

def build_doc():
    out = ["# 【M1-3】心裡留保・虚偽表示：善意の第三者は何を満たせば守られるのか　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-3】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
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
    out.append("- 開始の楕円が1つ、ひし形が3つ、結果の箱が4つ（赤2・青2）か。ひし形1・2にだけ、青の「はい」と赤の「いいえ」が付いているか。")
    out.append("- ひし形3の出口が、濃紺の「心裡留保・虚偽表示」と「詐欺・錯誤」の2つだけで、青・赤の矢印やラベルになっていないか。")
    out.append("- 結果の箱のあとに矢印が出ていないか。注記のカードが1枚だけで、矢印でつながれていないか。")
    out.append("- 条番号（93条2項・94条2項・96条3項・95条4項）と、「虚偽表示の第三者は登記がなくても守られる（判例）」が指定どおりか。")
    out.append("- 簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-3.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
