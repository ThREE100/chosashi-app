# 【M2-4】占有の訴えの相手方と、本権との関係：追加の図解（占有回収の訴えの相手方の分かれ道）1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M2-4.py＝4つの場面の早見表）では行の文章になっている、相手方が奪った者本人か特定承継人かの分かれ道を、判定の流れで描く。
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2300", "This is a flowchart poster (判定の流れ) read from top to bottom."), TEXTREQ, BGREQ, COLOR] + \
           header("占有回収の訴えの相手方", "奪った者か、その承継人か", "民法 第181条・第200条") + \
           ["--- FLOWCHART ---",
            "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 2. Every side result box (RESULT 1 and RESULT 3) sits to the RIGHT of its diamond on the same row, with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. RESULT 2 sits on the center line directly below DIAMOND 2. All arrows are straight or have at most one right-angle bend and never cross each other.",
            "NODE START (rounded pill, dark navy, white text): " + q("占有を奪われた。誰を相手にするか"),
            "NODE DIAMOND 1: " + q("相手は、奪った者本人か、特定承継人か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it. This diamond is NOT a yes/no question, so its two exits use NEUTRAL DARK NAVY arrows and dark navy labels (no blue and no red on this diamond).",
            "  - Arrow down to DIAMOND 2 with the dark navy label " + q("特定承継人") + ".",
            "  - Arrow right to RESULT 1 with the dark navy label " + q("本人") + ".",
            "NODE RESULT 1 (neutral box with a dark navy outline and a pale gray fill, NOT blue and NOT red, at the right of DIAMOND 1): " + q("奪った者本人には、回収の訴えを提起できる") + " on the first lines, and " + q("目的物を貸しただけでも、貸主として間接占有を続けている") + " on the next lines.",
            "Under RESULT 1, a small light-gray tag attached to the box: " + q("民法181条") + ".",
            "NODE DIAMOND 2: " + q("承継人は、侵奪の事実を知っていたか？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
            "  - Arrow down to RESULT 2 with the BLUE label " + q("はい") + ".",
            "  - Arrow right to RESULT 3 with the RED label " + q("いいえ") + ".",
            "NODE RESULT 2 (blue box, on the center line below DIAMOND 2): " + q("承継人にも提起できる") + " on the first line and " + q("ただし書：侵奪の事実を知っていたとき") + " on the next lines.",
            "NODE RESULT 3 (red box, at the right of DIAMOND 2): " + q("承継人には提起できない") + " on the first line and " + q("原則：特定承継人に対しては不可") + " on the next lines.",
            "Under RESULT 3, a small light-gray tag attached to the box: " + q("民法200条2項") + ".",
            "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. The three result boxes have different texts; do not copy one into another. RESULT 2 is the last element of the poster."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that DIAMOND 1 has dark navy labels 「特定承継人」 and 「本人」 and no blue or red, that DIAMOND 2 shows a blue 「はい」 and a red 「いいえ」, that RESULT 1 is a neutral dark navy outlined box, RESULT 2 is blue and RESULT 3 is red, that the two small light-gray tags are attached to RESULT 1 and RESULT 3, that no text overflows its box, and that no arrow label is hidden.")

META = [(1, "占有回収の訴えの相手方（奪った者か、その承継人か）", "フローチャート型", "1080×2300", "民法編2_M2-4_追加_占有回収の訴えの相手方の分かれ道", "【M2-4】の「判断のしかた」の直後", img1)]

def build_doc():
    out = ["# 【M2-4】占有の訴えの相手方と、本権との関係はどうなっているのか　追加の図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-4】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-4.md`＝4つの場面の早見表）は変更せず、"
               "表では文章の行になっている「占有回収の訴えの相手方は、奪った者本人か、特定承継人か。承継人なら侵奪の事実を知っていたか」という分かれ道を、記事の「判断のしかた」3（侵奪者が占有を失ったか、保ち続けているか）に沿って判定の流れで補います。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています。画像の中には、図の番号・問題番号・個人の演習結果を入れません。キャラクターは描きません。\n")
    out.append("| 番号 | 図解 | 型 | サイズ | 保存名 | 記事の挿入位置 |")
    out.append("|---|---|---|---|---|---|")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"| 図解{n} | {t} | {typ} | {size} | {fn}.png | {pos} |")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("## 検品チェック（生成後）\n")
    out += ["- ひし形が2つ。1つ目（「相手は、奪った者本人か、特定承継人か？」）は、はい／いいえではないので濃紺の「特定承継人」「本人」の矢印で、青・赤を使っていないか。2つ目（「承継人は、侵奪の事実を知っていたか？」）には青の「はい」と赤の「いいえ」が付いているか。",
            "- 結果の箱が3つ（濃紺の枠の中立の箱1つ＝奪った者本人、青1つ＝承継人にも提起できる、赤1つ＝承継人には提起できない）で、箱の文字が指定どおりか。小さな灰色のタグが中立の箱（民法181条）と赤い箱（民法200条2項）に付いているか。",
            "- 最後の要素（青い箱）のあとに、まとめ・トロフィー・追加の文字ブロックが描かれていないか。",
            "- 見出し・箱の文字を、上のコードブロックの文言と一字ずつ突き合わせた（「承継」「侵奪」「占有」「奪」「間接」「貸主」が簡体字・別字になっていない）。簡体字・余計な文字・透過・図番がない。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- 民法200条2項（占有回収の訴えは、占有を侵奪した者の特定承継人に対して提起することができない。ただし、その承継人が侵奪の事実を知っていたときは、この限りでない）、181条（占有権は代理人によって取得できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。",
            "- 「侵奪者が目的物を第三者に貸しただけなら、侵奪者は貸主として代理占有（間接占有）を続けており、なお相手方になる」は、記事の中身の整理・肢の判定による判例の整理で、条文に直接の記述はない（181条は代理占有の取得を定めるのみ）。図ではタグに民法181条とだけ添え、結論の断定は記事の範囲にとどめた。",
            "- 1つ目のひし形は「本人か、承継人か」という二択で、はい／いいえの分岐ではないため、濃紺の中立の矢印と箱にした（本人への提起は『できる』なので、赤い箱にすると『できない』と読み違えるおそれがある）。2つ目のひし形は「知っていたか」のはい／いいえなので、青・赤にした。",
            "- 占有を手放した場合（元の侵奪者が占有を失ったとき）の扱いは、記事の判断のしかたにある対比（手放した／貸しただけ）を、承継人の分岐として描いた。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-4_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
