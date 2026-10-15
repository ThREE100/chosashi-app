# 【M3-4_b】遺産分割と特定遺贈の場面の関係図：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-4_b.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-4_b"
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
SCOPE = "【M3-4】の「たとえば」の直後（遺産分割と特定遺贈の場面を登場人物の図で）"
DIFF = "既存の図解（承継と対抗の対比表）との違い：既存の図解は、取得の原因ごとに『承継』と『対抗』を表で比べます。この図解は、記事の例（遺産分割で単独取得したあと持分が譲渡された場合）と特定遺贈の場面を、登場人物と順番の図で見せます。"

def panel(heading, diagram, steps, result, extra=None):
    out = ["--- PANEL ---", "Panel heading bar (dark navy with white bold text, ONE line):", q(heading), "Diagram: " + diagram,
           "Step strip directly under the diagram: three small rounded boxes in a row from left to right, each with a small dark navy circle containing a number (1, 2, 3 in order) and a short label: "
           + ", ".join(f"({i}) " + q(s) for i, s in enumerate(steps, 1)) + ".",
           "Result banner (a wide pale-yellow banner with dark navy text, directly below the step strip): " + q(result) + "."]
    if extra:
        out.append("Under the banner, one small light-gray tag: " + q(extra) + ".")
    return out

def img1():
    body = [lead("1080x2000", "This is a poster of two stacked scene panels, each a small relationship diagram of people with a three-step strip (関係図); it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + \
           header("分割・遺贈のあと、第三者が出た", "登記がないと対抗できない", "民法　第177条・第899条の2・第909条")
    body += panel("遺産分割で、一人が単独で取得した",
                  "Three " + PERSON + " in a row from left to right: " + q("取得した相続人") + " with a small light-gray tag " + q("未登記") + ", " + q("もう一人の相続人") + " and " + q("持分を買った人") + ". "
                  "A dark navy arrow from もう一人の相続人 to 持分を買った人 labeled " + q("持分を譲渡") + ", with a small rubber-stamp icon labeled " + q("登記") + " beside 持分を買った人.",
                  ["相続が始まる", "協議で、一人が単独取得", "持分が譲渡され、登記"], "超える部分は、登記がないと対抗できない", "遺産分割は相続開始にさかのぼるが、第三者の権利は害せない")
    body += panel("特定遺贈を受けた",
                  "Three " + PERSON + " in a row from left to right: " + q("遺贈を受けた人") + " with a small light-gray tag " + q("未登記") + ", " + q("相続人") + " and " + q("相続人の債権者") + ". "
                  "Under 相続人, a small isometric house with a dark navy name tag " + q("名義：相続人") + ". A dotted two-headed dark navy line between 遺贈を受けた人 and 相続人の債権者 labeled " + q("対抗できる？") + ".",
                  ["遺言で、特定の不動産を遺贈", "相続が始まる", "相続人の債権者が出てくる"], "登記がないと、債権者に対抗できない", "特定遺贈は、遺言による個別の権利移転")
    body += ["Counts: 2 panels, each with exactly 3 pictograms and exactly 3 numbered step boxes; the rubber-stamp icon appears once in panel 1 and never in panel 2; the light-gray tag " + q("未登記") + " appears once in each panel. The two result banners have different texts; do not copy one into the other. Draw no check mark, no cross mark, and no blue or red anywhere."]
    return finish(body, "Confirm there are exactly 2 panels with 3 pictograms and 3 numbered step boxes each, that the 登記 stamp appears once in panel 1 and never in panel 2, that the dotted two-headed line labeled 対抗できる？ appears only in panel 2, that the two result banners read 超える部分は、登記がないと対抗できない and 登記がないと、債権者に対抗できない in this order, that no text overflows its box, and that all person names are role names with no Latin letters.")

META = [(1, "分割・遺贈のあと、第三者が出てきたら（遺産分割と特定遺贈の登場人物）", "関係図ポスター型（2場面＋3ステップ帯）", "1080×2000", "民法編3_4_追加_遺産分割と特定遺贈の場面", "【M3-4】の「たとえば」の直後", img1)]

CHECKS = ["場面パネルがちょうど2つで、人型が各3体、番号つきのステップの箱が各3つ。登記の印は場面1に1つ（持分を買った人）、場面2にはない。『未登記』の札が各場面に1つ",
          "点線の両方向の線『対抗できる？』が場面2だけにある。結果の帯が『超える部分は、登記がないと対抗できない』『登記がないと、債権者に対抗できない』の順",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない。人型の名札が役割名（英字なし）"]
NOTES = ["場面1：記事【M3-4】の『たとえば』（共同相続人2人のうち一人が単独取得する協議、登記前にもう一人が持分を譲渡し登記）。民法899条の2第1項（法定相続分を超える部分は、遺産分割によるかどうかにかかわらず、対抗要件を備えなければ第三者に対抗できない）、民法909条ただし書（第三者の権利を害することはできない）：`note-articles/laws/minpou-3-shinzoku-souzoku.md` で原文確認済み",
         "場面2：記事の中身の整理（特定遺贈は、遺言という意思表示による個別の権利移転なので、受遺者が登記なしでは、相続人の債権者に対抗できない）。債権者の差押えなど具体的な手続は記事に書かれていないため、図にも描いていない",
         "数字（相続分の割合）は、記事にないため図に入れていない"]


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
