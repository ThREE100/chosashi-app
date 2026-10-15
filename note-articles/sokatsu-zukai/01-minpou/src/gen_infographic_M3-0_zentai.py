# 【M3-0_zentai】第3章の全体図：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-0_zentai.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-0_zentai"
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

TOPIC = "【M3-0】第3章の全体図"
SCOPE = "冒頭（「この章の誤りの傾向」の次、【M3-1】の前）の全体図"
DIFF = "既存の図解（論点ごとの6枚）との違い：既存の図解は論点の中の判定や対比を見せます。この全体図は、6つの論点が『誰に』『いつ』『何を』『どこまで』のどの問いに答えるものかを、読む順に並べた地図です。"

def card(i, n, h, ill, items, tag):
    return [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {n} in order across the whole poster; the group bands do not take a number).",
            "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
            "Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
           ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]

def img1():
    cards = [
        ("あとの買主は、どんな人か",
         "Two faceless buyer pictograms in exactly the same light gray-blue color standing on either side of one small isometric house, with dark navy name tags " + q("先の買主") + " and " + q("あとの買主") + "; the right one holds a small rubber stamp.",
         ["知っていただけなら、登記が要る", "登記なしで勝てるのは、害する目的の本人だけ", "転得者は、自身が害する目的でなければ保護される"], "誰に"),
        ("第三者は、いつ現れたか",
         "A horizontal timeline arrow in dark navy with one large dot in the middle labeled " + q("取消し・解除・時効") + "; one faceless pictogram tagged " + q("第三者") + " above the left side of the dot and another one tagged " + q("第三者") + " above the right side, with small labels " + q("前") + " and " + q("後") + " under the two sides.",
         ["取消し・解除・時効の、前か後かを見る", "解除のあとは、登記の先後で決まる"], "いつ"),
        ("売主の周りの人は、誰か",
         "Three faceless pictograms in a row with dark navy name tags " + q("元の所有者") + ", " + q("売主") + " and " + q("買主") + ", and one smaller pictogram tagged " + q("売主の相続人") + " standing above the middle one.",
         ["相続人には、登記なしで主張できる", "合意をしても、債権者は代位できる", "他人物売買は、取得した時に移る"], "立場"),
        ("相続で、登記が要るのは何か",
         "One long horizontal bar: the left part labeled " + q("法定相続分まで") + " and a short extension at the right end labeled " + q("超える部分") + ", with a small rubber stamp icon placed only on the extension.",
         ["法定相続分を超える部分は、登記が要る", "特定遺贈も、登記が要る", "共有の解消は、遺産分割で"], "範囲"),
        ("地上権は、何が自由か",
         "An isometric plot of land with a small house standing on it and a small dark navy key tag labeled " + q("地上権") + " beside the house.",
         ["承諾なしで、譲渡も抵当権の設定もできる", "地代は、約束があって初めて生じる", "賃借権は、譲渡に承諾が要る"], "物権"),
        ("不動産質は、どこまでできるか",
         "An isometric vacation cottage wrapped by a dark navy ribbon labeled " + q("質権") + ".",
         ["全部の弁済まで、全体に権利が及ぶ", "転質も使用収益も、承諾は要らない", "利息は、請求できない"], "質権"),
    ]
    body = [lead("1080x3200", "This is a map-style quick-reference poster with six numbered cards in one column, split into two groups by two wide bands; it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + \
           header("第3章の地図：6つの問い", "いつ・誰に、で読み分ける", "民法 第177条・第899条の2・第265条・第356条")
    body += ["--- GROUP BAND 1 (placed directly below the header and above CARD 1) ---", "One wide dark navy band with large white text " + q("登記が要るか：誰に・いつ・何を") + "."]
    for i in range(4):
        body += card(i + 1, 6, *cards[i])
    body += ["--- GROUP BAND 2 (placed between CARD 4 and CARD 5) ---", "One wide dark navy band with large white text " + q("制度の中身：どこまで自由にできるか") + "."]
    for i in range(4, 6):
        body += card(i + 1, 6, *cards[i])
    body += ["Counts: 2 group bands and 6 cards. The six conclusion tags are all different strings; the six headings are all different strings."]
    return finish(body, "Confirm the number of cards equals 6 exactly, numbered 1 to 6 in order, that the dark navy band 「登記が要るか：誰に・いつ・何を」 sits above card 1, that the dark navy band 「制度の中身：どこまで自由にできるか」 sits between card 4 and card 5, that the bands carry no number, that there is no intro illustration or paragraph block, and that no card contains a full sentence of explanatory prose, a check mark, a cross mark, blue, or red.")

META = [(1, "第3章の地図：6つの問い（誰に・いつ・何を・どこまで）", "カードポスター型（俯瞰・6枚＋グループ帯2本）", "1080×3200", "民法編3_0_第3章の地図", "章の冒頭（「この章の誤りの傾向」の次、【M3-1】の前）", img1)]

CHECKS = ["カードがちょうど6枚で番号が1〜6の順。濃紺の帯が2本（カード1の上とカード4・5の間）で、帯に番号がない",
          "各カードの見出し・項目・結論タグ（誰に／いつ／立場／範囲／物権／質権）がプロンプトと一字一句同じ",
          "簡体字・繁体字・英字・ハングルの混入がない。背景が不透明。✓・✕・青・赤がどこにもない",
          "カードの中に説明文の段落がない。最後のカードの下に追加のまとめ・トロフィーがない"]
NOTES = ["カード1（M3-1）：民法177条。登記なしで勝てるのは害する目的の本人だけ／転得者は自身が背信的悪意者でない限り保護（記事【M3-1】の結論・判断のしかた）",
         "カード2（M3-2）：取消し・解除・時効の前後で登記の要否が変わる（記事【M3-2】）。解除のあとは対抗関係（先に登記をした方が勝つ）",
         "カード3（M3-3）：相続人は包括承継人で、登記なしで主張できる／中間省略登記の合意でも売主の登記請求権は消えず、債権者は代位できる（民法423条1項）／他人物売買は売主の取得時（民法561条）。中間省略登記の扱いは判例の整理で、条文に直接の定めはない",
         "カード4（M3-4）：民法899条の2第1項（法定相続分を超える部分は対抗要件が必要）、特定遺贈は民法177条、共有の解消は民法258条の2第1項（遺産分割による）",
         "カード5（M3-5）：地上権は承諾なしで譲渡でき抵当権も設定できる（民法369条2項）、地代は設定契約の定めで初めて生じる（民法266条1項の前提）、賃借権は賃貸人の承諾が必要（民法612条1項）",
         "カード6（M3-6）：不動産質は不可分性（民法350条・296条）、転質は承諾不要（民法348条）、使用及び収益ができ（民法356条）、利息は請求できない（民法358条）。いずれも設定行為の別段の定めで変えられる（民法359条）"]


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
