# 【M3-1_b】二重に買われたら誰が勝つか（登場人物と登記の関係図）：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-1_b.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-1_b"
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

TOPIC = "【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか"
SCOPE = "【M3-1】の「たとえば」の直後（登場人物と登記の動きの図）"
DIFF = "既存の図解（判定の流れ図）との違い：既存の図解は、上から順に答えにたどり着く流れ図です。この図解は、同じ二重売買の登場人物（元の所有者・先の買主・あとの買主・転得者）を3つの場面で並べ、誰が登記をしていて誰が勝つのかを見せる関係図です。"

def panel(n, heading, diagram, result, extra=None):
    out = [f"--- PANEL {n} ---", "Panel heading bar (dark navy with white bold text, ONE line):", q(heading), "Diagram: " + diagram, "Result banner directly below the diagram: " + result]
    if extra:
        out.append(extra)
    return out

def img1():
    body = [lead("1080x2400", "This is a poster of three stacked scene panels, each a small relationship diagram of people (関係図); it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, COLOR] + \
           header("二重に買われたら、誰が勝つ？", "あとの買主の中身で決まる", "民法　第177条")
    base = ("On the left, one pictogram tagged " + q("元の所有者") + ". Two dark navy arrows leave it to the right, both labeled " + q("売る") + " (both arrows mean the same thing). "
            "The upper arrow ends at a pictogram tagged " + q("先の買主") + " with a small light-gray tag " + q("未登記") + " beside it. ")
    body += panel(1, "あとの買主が、知っていただけの悪意者",
                  base + "The lower arrow ends at a pictogram tagged " + q("あとの買主") + " with a small rubber-stamp icon labeled " + q("登記") + " beside it and a small light-gray tag " + q("知っていただけ") + " under it. Three pictograms in total in this panel.",
                  "a RED box with the text " + q("先の買主は、登記がないと負ける") + ".")
    body += panel(2, "あとの買主が、害する目的の背信的悪意者",
                  base + "The lower arrow ends at a pictogram tagged " + q("あとの買主") + " with a small rubber-stamp icon labeled " + q("登記") + " beside it and a small light-gray tag " + q("もっぱら害する目的") + " under it. Three pictograms in total in this panel.",
                  "a BLUE box with the text " + q("先の買主は、登記なしで勝てる") + ".")
    body += panel(3, "背信的悪意者から買った転得者が出てきた",
                  base + "The lower arrow ends at a pictogram tagged " + q("あとの買主") + " with a small rubber-stamp icon labeled " + q("登記") + " beside it and a small light-gray tag " + q("背信的悪意者") + " under it. "
                  "From the pictogram " + q("あとの買主") + ", a third dark navy arrow labeled " + q("転売") + " leads further to the right to a fourth pictogram tagged " + q("転得者") + " with a small rubber-stamp icon labeled " + q("登記") + " beside it and a small light-gray tag " + q("自身は背信的でない") + " under it. Four pictograms in total in this panel.",
                  "a RED box with the text " + q("先の買主は、転得者には負ける") + ".",
                  "Under the red box, one small light-gray tag: " + q("転得者自身が背信的悪意者なら、勝てる") + ".")
    body += ["Counts: 3 panels, with 3, 3 and 4 pictograms; the pictogram " + q("先の買主") + " never has a rubber-stamp icon; the rubber-stamp icon appears once in panel 1, once in panel 2 and twice in panel 3. The three result banners have different texts; do not copy one into another."]
    return finish(body, "Confirm there are exactly 3 panels, that panel 1 and panel 2 have 3 pictograms and panel 3 has 4 pictograms, that the pictogram 先の買主 never carries a 登記 stamp, that the banner of panel 1 is red, the banner of panel 2 is blue and the banner of panel 3 is red, that the arrows are dark navy and carry no はい or いいえ, that no text overflows its box, and that all person names are role names with no Latin letters.")

META = [(1, "二重に買われたら、誰が勝つ？（登場人物と登記の関係図）", "関係図ポスター型（3場面）", "1080×2400", "民法編3_1_追加_二重に買われたら誰が勝つ", "【M3-1】の「たとえば」の直後", img1)]

CHECKS = ["場面パネルがちょうど3つで、人型が3体・3体・4体。『先の買主』には登記の印がない（登記の印は、場面1に1つ、場面2に1つ、場面3に2つ）",
          "結果の箱は、場面1が赤『先の買主は、登記がないと負ける』、場面2が青『先の買主は、登記なしで勝てる』、場面3が赤『先の買主は、転得者には負ける』（3つの文言が別々）",
          "矢印は濃紺で『売る』『転売』だけ。『はい』『いいえ』が矢印にない。人型は全員同じ色で、役割名の名札（英字なし）",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。文字が箱からはみ出していない"]
NOTES = ["場面1・2：民法177条。単純悪意者も第三者に含まれ、害する目的の背信的悪意者本人は第三者から外れる（記事【M3-1】の結論・中身の整理）。背信的悪意かどうかを人ごとに判断する扱い（相対的構成）は判例の考え方で、条文に直接の定めはない",
         "場面3：記事の『たとえば』（嫌がらせ目的で買って登記した者から、事情を知らない者が転得し登記）と『判断のしかた』3（転得者自身が背信的かを見る）。小さな札『転得者自身が背信的悪意者なら、勝てる』は、判断のしかた3と既存の判定の流れ図（ひし形1）の裏返し",
         "『登記』の印が先の買主にないこと：先の買主が『登記をしていない人』という記事の前提（結論の冒頭）"]


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
