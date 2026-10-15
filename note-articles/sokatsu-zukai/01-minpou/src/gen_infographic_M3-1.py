# 【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか：図解インフォグラフィック1枚のプロンプトを組み立てる
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2300", "This is a flowchart poster (判定フロー)."), TEXTREQ, BGREQ, COLOR] + \
        header("登記なしで勝てる相手は？", "上から順に確かめる", "民法　第177条") + \
        ["--- FLOWCHART ---",
         "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 and RESULT 3 sit at the bottom, one to the left and one to the right of the center line, below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
         "NODE START (rounded pill, dark navy): " + q("先に買って登記をしていない人が") + " on the first line and " + q("あとで買った人に主張する") + " on the second line. Next to it on the right, a small light-gray tag (no arrow attached): " + q("背信かどうかは、人ごとに判断する") + ".",
         "NODE DIAMOND 1: " + q("あとで買った人自身が、もっぱら害する目的で買ったか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
         "  - Arrow right to RESULT 1 with the BLUE label " + q("はい") + ".",
         "  - Arrow down to DIAMOND 2 with the RED label " + q("いいえ") + ".",
         "NODE RESULT 1 (blue box): " + q("登記なしで勝てる") + " on the first line and " + q("その人自身が第三者から除外される") + " on the next two lines.",
         "NODE DIAMOND 2: " + q("その人は、背信的悪意者から買った転得者か？") + " This diamond has TWO neutral branches whose arrows and labels are dark navy (NOT blue and NOT red) and carry the labels " + q("転得者") + " and " + q("二重に買った人") + "; do not draw the strings 「はい」 or 「いいえ」 on these two arrows. The text is placed inside the diamond on 3 lines.",
         "  - Arrow down-left with the label " + q("転得者") + " to RESULT 2.",
         "  - Arrow down-right with the label " + q("二重に買った人") + " to RESULT 3.",
         "NODE RESULT 2 (red box): " + q("登記がないと負ける") + " on the first line and " + q("転得者は独立の第三者") + " on the second line and " + q("背信性は引き継がれない") + " on the third line.",
         "NODE RESULT 3 (red box): " + q("登記がないと負ける") + " on the first line and " + q("二重に買った人は第三者") + " on the second line and " + q("知っていただけの悪意者も同じ") + " on the third line.",
         "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 2 and RESULT 3 start with the same first line on purpose, and their second and third lines are different; the strings " + q("転得者は独立の第三者") + " and " + q("二重に買った人は第三者") + " are NOT identical, so do not copy one into the other."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that DIAMOND 1 shows a blue 「はい」 and a red 「いいえ」, that DIAMOND 2 shows only the two navy labels 「転得者」 and 「二重に買った人」, that RESULT 1 is blue and RESULT 2 and RESULT 3 are red, that the light-gray tag next to START has no arrow attached, that no text overflows its box, and that no arrow label is hidden.")

META = [(1, "登記なしで勝てる相手は？の判定フロー", "フローチャート型", "1080×2300", "図解M3-1_登記なしで勝てる相手の判定フロー",
         "【M3-1】の「判断のしかた」の直後（結論と中身の整理の次）", img1)]

def build_doc():
    out = ["# 【M3-1】図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事『直前期の苦手論点つぶし総合記事①民法編』（`note-articles/column/sokatsu-01-minpou.md`）の【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか、に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。キャラクターは描かないので、参照画像は不要です。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}（型：{typ}／サイズ：{size}）")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    out.append("4コマ（D0214・D0322・D1911）との違い：4コマは3つの肢を『結論は同じなのに文末で〇×が分かれる』角度で見せます。この図解は、記事の「判断のしかた」を、上から順にたどる判定フローで一望するものです。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("### 検品チェック（生成後）\n")
        for c in ["開始ノード1・ひし形2・結果の箱3の数と並びが合っている（ひし形1の右に結果1、ひし形2の下の左に結果2、右に結果3）",
                  "ひし形1だけが青の「はい」・赤の「いいえ」。ひし形2の2本の矢印は濃紺で「転得者」「二重に買った人」。結果1は青、結果2・3は赤",
                  "結果2と結果3の2〜3行目が別の文言（コピーされていない）。START横の灰色タグに矢印が付いていない",
                  "簡体字・繁体字・英字・余計な文字がない。背景が不透明。文字が箱からはみ出していない",
                  "法的内容：害する目的の背信的悪意者本人は第三者から除外／転得者は本人が背信的悪意者でない限り第三者として保護／単純悪意者も第三者（記事【M3-1】と一致）"]:
            out.append(f"- [ ] {c}")
        out.append("")
        out.append("### 記事・条文との照合\n")
        for c in ["『もっぱら害する目的』『背信的悪意者』『転得者』『独立の第三者』『背信性は引き継がれない』『知っていただけの悪意者も同じ』：記事の【M3-1】の結論・中身の整理・判断のしかたと元記事（H19-Q02エ・H20-Q02オ・R06-Q02ア）の本文の範囲",
                  "『背信かどうかは、人ごとに判断する』：記事の「背信的悪意かどうかは個人ごとに判断します（相対的構成）」。判例の立場で、条文に直接の定めはない",
                  "民法第177条（サブタイトル）：note-articles/laws/minpou-1-soukyoku-bukken.md で原文確認済み（登記をしなければ第三者に対抗できない）"]:
            out.append(f"- {c}")
        out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).resolve().parent.parent.joinpath("infographic", "prompt_infographic_M3-1.md").write_text(doc, encoding="utf8")
    print(len(doc))
