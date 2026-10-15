# 【M3-4_c】登記が要るかの判定の流れ図：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-4_c.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-4_c"
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
PERSON = "faceless flat person pictograms in exactly the same single light gray-blue color, each with a dark navy name tag"
GLANCE = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the first element. "
          "Every element communicates its point through the illustration plus short labels. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text beyond the short strings listed below.")

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def table_block(cols, rows, hl, label_col=False):
    n = len(cols)
    out = ["--- TABLE ---",
           f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {len(rows)} data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
           "Header row (dark navy cells with white text): " + ", ".join(q(c) if c else "an empty cell" for c in cols) + ".",
           "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"]
    out += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    out.append(hl)
    return out

TOPIC = "【M3-4】遺贈・遺産分割・遺言による承継は、登記が要るか"
SCOPE = "【M3-4】の「判断のしかた」の直後（登記が要るかの判定の流れ図）"
DIFF = "既存の図解（承継と対抗の対比表）との違い：既存の図解は、取得の原因ごとに結論を横に並べる表です。この図解は、記事の『判断のしかた』（原因を確かめる→法定相続分を超えるかを見る）を、上から順にたどる判定の流れ図にしたものです。"

def img1():
    body = [lead("1080x2400", "This is a flowchart poster (判定の流れ)."), TEXTREQ, BGREQ, COLOR] + \
        header("登記が要るのは、どんなとき？", "原因と、取得した範囲で決まる", "民法　第177条・第899条の2") + \
        ["--- FLOWCHART ---",
         "Layout: one vertical center line down the middle of the canvas. Nodes are placed top to bottom on the center line in this order: START, DIAMOND 1, DIAMOND 2, RESULT 3. RESULT 1 sits to the RIGHT of DIAMOND 1 on the same row, and RESULT 2 sits to the RIGHT of DIAMOND 2 on the same row, each with at least 60 px of empty space between the diamond and the box so that the arrow label stays visible. The side note card sits at the bottom, below RESULT 3. All arrows are straight or have at most one right-angle bend and never cross each other.",
         "NODE START (rounded pill, dark navy): " + q("相続・遺産分割・遺言などで取得した不動産を") + " on the first line and " + q("第三者に主張する") + " on the second line.",
         "NODE DIAMOND 1: " + q("特定遺贈ではなく、相続による承継か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
         "  - Arrow down to DIAMOND 2 with the BLUE label " + q("はい") + ".",
         "  - Arrow right to RESULT 1 with the RED label " + q("いいえ") + ".",
         "NODE RESULT 1 (red box): " + q("登記が要る") + " on the first line, " + q("特定遺贈は個別の権利移転") + " on the second line and " + q("（民法177条）") + " on the third line.",
         "NODE DIAMOND 2: " + q("取得した部分は、法定相続分の範囲内か？") + " The text is placed inside the diamond on 3 lines; enlarge the diamond so that all text stays inside it.",
         "  - Arrow down to RESULT 3 with the BLUE label " + q("はい") + ".",
         "  - Arrow right to RESULT 2 with the RED label " + q("いいえ") + ".",
         "NODE RESULT 2 (red box): " + q("登記が要る") + " on the first line, " + q("遺産分割でも遺言でも") + " on the second line and " + q("（民法899条の2第1項）") + " on the third line.",
         "NODE RESULT 3 (blue box): " + q("登記なしで主張できる") + " on the first line and " + q("法定相続分の範囲内") + " on the second line.",
         "--- SIDE NOTE CARD (a wide card with a dashed dark navy outline at the bottom, neutral dark navy text, no arrow attached) ---",
         "Heading " + q("相続させる旨の遺言は、死亡と同時に承継される") + ", body " + q("承継の時期と、登記が要るかは、別の問い") + ".",
         "Counts: 1 start node, 2 diamonds, 3 result boxes, 3 distinct paths from the start to a result box. Every diamond has exactly two exits, and no arrow leaves a result box. RESULT 1 and RESULT 2 start with the same first line on purpose, and their second and third lines are different; the strings " + q("特定遺贈は個別の権利移転") + " and " + q("遺産分割でも遺言でも") + " are NOT identical, so do not copy one into the other."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 1 start node, 2 diamonds and 3 result boxes, that both diamonds show a blue 「はい」 and a red 「いいえ」, that RESULT 1 and RESULT 2 are red, that RESULT 3 is blue and sits directly below DIAMOND 2, that the side note card has no arrow attached and is the last element, that no text overflows its box, and that no arrow label is hidden.")

META = [(1, "登記が要るのは、どんなとき？（原因と取得した範囲の判定の流れ）", "フローチャート型", "1080×2400", "民法編3_4_追加_登記が要るかの判定の流れ", "【M3-4】の「判断のしかた」の直後", img1)]

CHECKS = ["開始ノード1・ひし形2・結果の箱3の数と並びが合っている（ひし形1の右に結果1、ひし形2の右に結果2、ひし形2の下に結果3）",
          "両方のひし形で、下向きが青の『はい』、右向きが赤の『いいえ』。結果1・2は赤、結果3は青",
          "結果1と結果2の2〜3行目が別の文言（コピーされていない）。下の破線の札に矢印が付いていない",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。文字が箱からはみ出していない"]
NOTES = ["特定遺贈は民法177条の問題（記事【M3-4】の中身の整理・肢の判定D0115）。法定相続分を超える部分は、遺産分割でも遺言でも対抗要件が必要（民法899条の2第1項、`note-articles/laws/minpou-3-shinzoku-souzoku.md` で原文確認済み）",
         "『法定相続分の範囲内は、登記なしで主張できる』：民法899条の2第1項が対抗要件を求めるのは『相続分を超える部分』なので、その反対の整理（条文に明記はなく、記事の判断のしかた2『法定相続分を超えるなら登記が必要』の裏返し）。図では、条文の根拠を結果の箱3に載せていない",
         "相続させる旨の遺言：記事の中身の整理（遺贈と解すべき特段の事情がなければ、遺産分割方法の指定と解され、死亡と同時に承継される）。承継の時期と対抗の要否を別の問いとして側注にした。法定相続分を超える部分は、この遺言でも結果2の経路（民法899条の2第1項）になる",
         "共有物分割と遺産分割の関係（民法258条の2）は、既存の図解（別の問いのカード）にあるため、この流れ図には入れていない"]


def build_doc():
    out = [f"# {TOPIC}　追加の図解インフォグラフィック プロンプト（{len(META)}枚）\n"]
    out.append("総合記事『直前期の苦手論点つぶし総合記事①民法編』の第3章（`note-articles/column/sokatsu-01-minpou-ch3.md`）の" + SCOPE + "に差し込む、追加の図解のプロンプトです。"
               "作成済みの図解（`infographic/prompt_infographic_M3-?.md`）は変えず、記事の要点のうち図がなかった部分を補います。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。当事者はラテン文字ではなく役割名で書いています。キャラクターは描かないので、参照画像は不要です。\n")
    out.append(DIFF + "\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}（型：{typ}／サイズ：{size}）")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("### 検品チェック（生成後）\n")
    for c in CHECKS:
        out.append(f"- [ ] {c}")
    out.append("")
    out.append("### 記事・条文との照合\n")
    for c in NOTES:
        out.append(f"- {c}")
    out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    dest = _here.parent.parent / "infographic" / f"prompt_infographic_{KEY}.md"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(doc, encoding="utf8")
    print(dest, len(doc))
