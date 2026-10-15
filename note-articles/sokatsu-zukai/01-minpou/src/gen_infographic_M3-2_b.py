# 【M3-2_b】解除の前・解除のあと・時効完成の前の登記の動き：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-2_b.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-2_b"
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

TOPIC = "【M3-2】取消し・解除・時効と登記は、第三者がいつ現れたかで決まる"
SCOPE = "【M3-2】の「たとえば」の直後（解除の前・解除のあと・時効完成の前の登記の動き）"
DIFF = "既存の図解（時点カード5枚）との違い：既存の図解は、第三者が出てきた時点を5つの原因で見せる早見です。この図解は、解除の前・解除のあと・時効完成の前の3場面を取り出し、売主・買主・第三者のうち誰が登記をしたか、権利が動いた順番を登場人物の図で見せます（既存の図解にない『解除の前』を含みます）。"

def panel(heading, diagram, steps, result, extra=None):
    out = ["--- PANEL ---", "Panel heading bar (dark navy with white bold text, ONE line):", q(heading), "Diagram: " + diagram,
           "Step strip directly under the diagram: three small rounded boxes in a row from left to right, each with a small dark navy circle containing a number (1, 2, 3 in order) and a short label: "
           + ", ".join(f"({i}) " + q(s) for i, s in enumerate(steps, 1)) + ".",
           "Result banner (a wide pale-yellow banner with dark navy text, directly below the step strip): " + q(result) + "."]
    if extra:
        out.append("Under the banner, one small light-gray tag: " + q(extra) + ".")
    return out

def img1():
    body = [lead("1080x2600", "This is a poster of three stacked scene panels, each a small relationship diagram of people with a three-step strip (関係図); it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + \
           header("登記は、誰がいつ動かした？", "解除の前・解除のあと・時効の前", "民法　第177条・第545条")
    body += panel("解除の前に、第三者が買った",
                  "Three " + PERSON + " in a row from left to right: " + q("売主") + ", " + q("買主") + " and " + q("第三者") + ". A dark navy arrow from 売主 to 買主 labeled " + q("売る") + ", with a small rubber-stamp icon labeled " + q("登記") + " beside 買主. A dark navy arrow from 買主 to 第三者 labeled " + q("転売") + ".",
                  ["売買と登記", "転売", "解除"], "第三者の権利を害することはできない")
    body += panel("解除のあとに、第三者が買った",
                  "Three " + PERSON + " in a row from left to right: " + q("売主") + ", " + q("買主") + " and " + q("第三者") + ". A dark navy arrow from 売主 to 買主 labeled " + q("売る") + ", with a small rubber-stamp icon labeled " + q("登記") + " beside 買主. A dark navy arrow from 買主 to 第三者 labeled " + q("転売") + ", with a small rubber-stamp icon labeled " + q("登記") + " beside 第三者. "
                  "A dotted dark navy curved arrow from 買主 back to 売主 labeled " + q("復帰") + ".",
                  ["売買と登記", "解除", "転売と登記"], "先に登記をした方が勝つ", "売主が名義を戻していなければ、第三者が勝つ")
    body += panel("時効の完成の前に、第三者が登記を得た",
                  "Three " + PERSON + " in a row from left to right: " + q("元の所有者") + ", " + q("譲受人") + " and " + q("占有者") + ". A dark navy arrow from 元の所有者 to 譲受人 labeled " + q("売る") + ", with a small rubber-stamp icon labeled " + q("登記") + " beside 譲受人. A two-headed dark navy arrow between 譲受人 and 占有者 labeled " + q("主張") + ". A small isometric plot of land with a house under 占有者.",
                  ["占有を始める", "譲受人が買って登記", "時効が完成"], "占有者は、登記なしで主張できる", "譲受人は、時効取得の当事者に類する立場")
    body += ["Counts: 3 panels, each with exactly 3 pictograms and exactly 3 numbered step boxes; the rubber-stamp icon appears once in panel 1, twice in panel 2 and once in panel 3. The three result banners have different texts; do not copy one into another. Draw no check mark, no cross mark, and no blue or red anywhere."]
    return finish(body, "Confirm there are exactly 3 panels with 3 pictograms and 3 numbered step boxes each, that the stamp icons appear once, twice and once in panels 1, 2 and 3, that the dotted curved arrow labeled 復帰 appears only in panel 2, that the three result banners read 第三者の権利を害することはできない, 先に登記をした方が勝つ and 占有者は、登記なしで主張できる in this order, that no text overflows its box, and that all person names are role names with no Latin letters.")

META = [(1, "登記は、誰がいつ動かした？（解除の前・解除のあと・時効完成の前）", "関係図ポスター型（3場面＋3ステップ帯）", "1080×2600", "民法編3_2_追加_登記は誰がいつ動かしたか", "【M3-2】の「たとえば」の直後", img1)]

CHECKS = ["場面パネルがちょうど3つで、人型が各3体、番号つきのステップの箱が各3つ。登記の印は、場面1に1つ（買主）、場面2に2つ（買主と第三者）、場面3に1つ（譲受人）",
          "点線の曲がった矢印『復帰』が場面2だけにある。矢印は濃紺。✓・✕・青・赤がどこにもない",
          "結果の帯が上から『第三者の権利を害することはできない』『先に登記をした方が勝つ』『占有者は、登記なしで主張できる』（場面2・3の下に灰色の小さな札がある）",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。人型の名札が役割名（英字なし）"]
NOTES = ["場面1（解除の前）：民法545条1項ただし書『第三者の権利を害することはできない』（`note-articles/laws/minpou-2-saiken.md` で原文確認済み）。記事は『解除前の第三者は545条1項ただし書』（直前チェック）とだけ述べるため、第三者が保護を受ける要件（登記など）は図に書いていない",
         "場面2（解除のあと）：記事【M3-2】の『中身の整理』『たとえば』。復帰と転売を二重譲渡のように扱い、先に登記を備えた方が勝つ。これは判例の整理で、545条1項ただし書は解除『前』の第三者に関する規定",
         "場面3（時効完成の前）：記事【M3-2】の『中身の整理』（譲受人は時効取得の当事者に類する立場で、占有者は登記なしで主張できる）。時効の登記の要否は条文に明記がなく、判例の考え方",
         "ステップ帯の順番：場面1は売買と登記→転売→解除、場面2は売買と登記→解除→転売と登記、場面3は占有開始→譲受人の取得と登記→時効の完成。いずれも記事の例の時系列に合わせた"]


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
