# 【M3-2】取消し・解除・時効と登記は、第三者がいつ現れたかで決まる：図解インフォグラフィック1枚のプロンプトを組み立てる
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

def timeline(dots, who_above, who_tag):
    """3つの点の時間軸。第三者の人型を who_above 番目（1〜3）の点の上に置く。"""
    d1, d2, d3 = dots
    return ("A horizontal timeline with an arrowhead pointing to the right, drawn in dark navy, with exactly three small dots from left to right labeled "
            + q(d1) + ", " + q(d2) + " and " + q(d3) + " (labels under the dots). "
            "A small faceless person pictogram in a light gray-blue color, with a dark navy name tag " + q("第三者") + ", stands above dot number " + str(who_above)
            + ", and a small pale-yellow highlighter banner " + q(who_tag) + " sits right next to the pictogram. No other person is drawn.")

CARDS = [
    ("未成年者の取消し", timeline(("売買", "第三者が買う", "取消し"), 2, "取消しの前に現れた"), "善意の第三者にも対抗できる"),
    ("詐欺による取消し", timeline(("売買", "第三者が買う", "取消し"), 2, "取消しの前に現れた"), "善意無過失は保護される"),
    ("解除", timeline(("売買", "解除", "第三者が買う"), 3, "解除のあとに現れた"), "対抗関係（売主も登記が要る）"),
    ("時効：完成の前", timeline(("占有を始める", "第三者が登記を得る", "時効が完成"), 2, "完成の前に現れた"), "登記なしで主張できる"),
    ("時効：完成のあと", timeline(("占有を始める", "時効が完成", "第三者が買う"), 3, "完成のあとに現れた"), "対抗関係（登記の先後）"),
]

def img1():
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the timeline illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("第三者はいつ出てきた？", "取消し・解除・時効の早見", "民法　第177条")
    for i, (h, ill, tag) in enumerate(CARDS, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    body += ["Cards 1 and 2 have the same timeline on purpose (the same three dot labels and the same banner), and their headings and conclusion tags are different; do not copy a heading or a conclusion tag from one card to another. The five conclusion tags are all different strings."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that exactly one person pictogram appears in each card, and confirm that no card contains a full sentence of explanatory prose.")

META = [(1, "第三者はいつ出てきた？の早見", "カードポスター型（時点カード5枚）", "1080×2300", "図解M3-2_第三者はいつ出てきたかの早見",
         "【M3-2】の「判断のしかた」の直後（結論と中身の整理の次）", img1)]

def build_doc():
    out = ["# 【M3-2】図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事『直前期の苦手論点つぶし総合記事①民法編』（`note-articles/column/sokatsu-01-minpou.md`）の【M3-2】取消し・解除・時効と登記は、第三者がいつ現れたかで決まる、に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図には「はい／いいえ」の分岐がないため、青・赤は使わず、濃紺と薄い黄色の強調で統一しています。画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。キャラクターは描かないので、参照画像は不要です。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}（型：{typ}／サイズ：{size}）")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    out.append("4コマ（D1210・D1211）との違い：4コマは、解除のあとと時効完成の前の2肢を『第三者が出てきた時期』と理由で対比します。この図解は、取消し・解除・時効の3つの原因を、第三者の位置を時間軸に置いた5枚のカードで一望する早見です。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("### 検品チェック（生成後）\n")
        for c in ["カードがちょうど5枚で、1〜5の順。導入のイラストや文章のブロックが見出しとカードの間にない",
                  "各カードに時間軸（点が3つ、左から右の矢印）があり、第三者の人型が1人だけ、指定の点の上に立っている（カード1〜2は2番目、カード3は3番目、カード4は2番目、カード5は3番目）",
                  "カード1とカード2は時間軸と黄色の札が同じで、見出しと結論の札が別の文言（コピーされていない）。5つの結論の札がすべて別の文言",
                  "簡体字・繁体字・英字・余計な文字がない。背景が不透明。最後のカードの下に、まとめの帯やトロフィーがない",
                  "法的内容：未成年者の取消しは善意でも対抗できる／詐欺取消しは善意無過失の第三者が保護される／解除のあとは対抗関係で売主も登記が要る／時効完成の前は登記なしで主張できる／時効完成のあとは対抗関係（記事【M3-2】・【M1-6】と一致）"]:
            out.append(f"- [ ] {c}")
        out.append("")
        out.append("### 記事・条文との照合\n")
        for c in ["『善意の第三者にも対抗できる』『善意無過失は保護される』『対抗関係（売主も登記が要る）』『登記なしで主張できる』：記事の【M3-2】の結論・中身の整理と、串刺しチェックの「取消し前の第三者は、詐欺取消しなら善意無過失で保護、未成年者の取消しなら善意でも対抗できる」",
                  "『完成の前に現れた／完成のあとに現れた』『対抗関係（登記の先後）』：記事の【M1-6】（時効完成前の第三者は当事者類似で登記なしで主張できる、完成後の第三者とは対抗関係）。判例の立場で、条文に直接の定めはない",
                  "民法第177条（サブタイトル）：note-articles/laws/minpou-1-soukyoku-bukken.md で原文確認済み。民法121条・5条2項・96条3項は画像に条番号を入れていない（記事の本文で確認）"]:
            out.append(f"- {c}")
        out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    pathlib.Path(__file__).resolve().parent.parent.joinpath("infographic", "prompt_infographic_M3-2.md").write_text(doc, encoding="utf8")
    print(len(doc))
