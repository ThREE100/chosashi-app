# 【M2-1】共有者の一人は、単独で何ができ、何ができないのか：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2100", "This is a flowchart poster (判定フロー) read from top to bottom."), TEXTREQ, BGREQ, COLOR] + \
           header("共有者の一人にできること", "相手と請求の中身で決まる", "民法 第252条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 2. Every NO result box sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 sits on the center line directly below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy, white text): " + q("共有物をめぐる請求を考える"),
            "NODE DIAMOND 1: " + q("請求する相手は、第三者か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 1 (red box, at the right of DIAMOND 1): " + q("相手は、ほかの共有者") + " on the first line, " + q("相手にも持分に基づく使用の権原がある") + " on the second and third lines, and " + q("持分の過半数でも、直ちには明渡しを請求できない") + " on the next lines.",
            "Under RESULT 1, a small light-gray tag attached to the box: " + q("特別の影響を及ぼす決定には承諾が必要（252条3項）") + ".",
            "NODE DIAMOND 2: " + q("請求の中身は、守る請求（明渡し）か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box, on the center line below DIAMOND 2): " + q("保存行為（民法252条5項）") + " on the first line and " + q("各共有者が単独で、共有物の全部を請求できる") + " on the next two lines.",
            "NODE RESULT 3 (red box, at the right of DIAMOND 2): " + q("お金の請求（損害賠償）") + " on the first line, " + q("請求権は持分に応じて分かれる") + " on the second line, and " + q("請求できるのは自分の持分割合まで") + " on the next lines.",
            "Under RESULT 3, a small light-gray tag attached to the box: " + q("例：持分3分の1で損害90万円なら、30万円まで") + ".",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another. RESULT 2 is the last element of the poster."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that each diamond shows a blue 「はい」 and a red 「いいえ」, that RESULT 2 is blue and RESULT 1 and RESULT 3 are red, that the two small light-gray tags are attached to RESULT 1 and RESULT 3, that no text overflows its box, and that no arrow label is hidden.")

META = [(1, "共有者の一人にできること（相手と請求の中身で決まる）", "フローチャート型", "1080×2100", "図解1_共有者の一人にできること", "【M2-1】の「判断のしかた」の直後", img1)]

def build_doc():
    out = ["# 【M2-1】共有者の一人は、単独で何ができ、何ができないのか　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M2-1】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
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
    out.append("- ひし形が2つ（「請求する相手は、第三者か？」「請求の中身は、守る請求（明渡し）か？」）で、各ひし形に青の「はい」と赤の「いいえ」が付いているか。")
    out.append("- 結果の箱が3つ（青1つ＝保存行為、赤2つ＝相手が共有者、お金の請求）で、箱の文字が指定どおりか。小さな灰色のタグが赤い箱の2つに付いているか。")
    out.append("- 最後の要素（保存行為の青い箱）のあとに、まとめ・トロフィー・追加の文字ブロックが描かれていないか。")
    out.append("- 条番号は「252条3項」「民法252条5項」の2つだけか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-1.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
