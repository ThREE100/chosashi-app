# 【第1章 全体】総則の8つの論点を、3つの問いで整理する：章の冒頭の全体図1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 実行: python3 gen_infographic_M1-0_zentai.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

# (帯の文言, [(見出し, 絵の指示, [項目行], タグ), ...])
SECTIONS = [
    ("まず、何の制度かを見分ける", [
        ("無効と取消し", "Two small document sheets side by side, the left one with a faint crack line and the right one with a rubber stamp, no text on the sheets.",
         ["追認で有効になるのは取消しだけ", "だれでも主張できるのは無効"], "性質を両方に当てはめる"),
        ("制限行為能力者", "A small faceless child-size person pictogram standing beside a faceless adult pictogram who holds a paper sheet, no text.",
         ["同意が要るのは補助開始だけ", "詐術は、相手方が信じたときだけ"], "類型と要件を分ける"),
    ]),
    ("次に、だれの話かを確かめる", [
        ("心裡留保・虚偽表示", "Two faceless person pictograms shaking hands with a small theater mask icon between them, no text.",
         ["第三者の保護は、善意だけで足りる", "相続人は、第三者ではない"], "第三者かどうか"),
        ("錯誤・詐欺の取消し", "A document sheet with a magnifying glass and a rubber stamp pressed on it, no text.",
         ["取り消せるのは、表意者の側だけ", "取消しと第三者への対抗は別の問い"], "取消しと対抗は別"),
        ("代理権の濫用と無権代理の相続", "A faceless person pictogram handing a key to another faceless pictogram, with a third pictogram drawn with a thin dotted outline behind them, no text.",
         ["相手方が善意無過失なら有効", "単独相続すると追認を拒絶できない"], "地位が一人に集まるか"),
    ]),
    ("最後に、いつの話かを確かめる", [
        ("取得時効と登記", "A small house with a fence line and a calendar page, no text.",
         ["元の所有者には登記が要らない", "完成の前の第三者にも要らない"], "完成の前か後か"),
        ("時効の援用・更新・完成猶予", "A desk calendar with a circular arrow beside it, no text.",
         ["完成の前の承認は、更新", "完成の後の承認は、援用できない"], "承認の時点"),
        ("条件", "A door with a small hourglass beside it, no text.",
         ["効力が動くのは、成就の時", "契約の時にすでに成就なら扱いが変わる"], "成就の時と契約の時"),
    ]),
]

def img1():
    body = [lead("1080x3000", "This is a quick-reference overview poster with eight numbered cards in one column, grouped under three dark navy section bands; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the first section band. Every card is compact (about 250 px tall) and consists of one small icon at the left, one heading, two short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("総則は3つの問いで解く", "何の制度か・だれの話か・いつの話か", "民法 総則（意思表示・制限行為能力・代理・時効・条件）")
    n = 0
    total = sum(len(c) for _, c in SECTIONS)
    for si, (band, cards) in enumerate(SECTIONS, 1):
        body += [f"--- SECTION BAND {si} (a wide dark navy rounded band with large white text, placed directly above its cards) ---", q(band)]
        for h, ill, items, tag in cards:
            n += 1
            body += [f"--- CARD {n} ---", f"Badge: a filled dark navy circle containing the number {n} (numbers run 1 to {total} in order across all three sections and do not restart).",
                     "Heading (bold, ONE line):", q(h), "Icon at the left of the card: " + ill,
                     "Item lines (two short lines of dark navy text beside the icon, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                    ["Conclusion tag (a short pale-yellow banner directly below the item lines, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 3 section bands and exactly 8 cards, with the cards numbered 1 to 8 in order (2 cards under the first band, 3 under the second, 3 under the third), no duplicated or missing cards, that there is no intro illustration or paragraph block between the header and the first band, that no card contains a full sentence of explanatory prose, and that no check mark, cross mark, blue or red appears anywhere. Confirm that the second character of 心裡留保 is drawn exactly as 裡 (clothing radical on the left, 里 on the right) everywhere it appears.")

META = [(1, "総則は3つの問いで解く（8つの論点の全体図）", "カードポスター型（俯瞰。帯3本・カード8枚）", "1080×3000", "民法編1_全体_総則は3つの問いで解く", "章の冒頭（「この章の誤りの傾向」の直後、【M1-1】の前）", img1)]

def build_doc():
    out = ["# 【第1章 全体】総則は3つの問いで解く　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の冒頭に差し込む、8つの論点（【M1-1】〜【M1-8】）の全体図のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は分類の図で、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの通し番号1〜8は、記事の論点の順番です）。キャラクターは描きません。\n")
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
    out.append("- 濃紺の帯が3本（まず・次に・最後に）で、カードが8枚、番号が1〜8の順か（帯1の下に2枚、帯2の下に3枚、帯3の下に3枚）。")
    out.append("- カードの見出し・項目行・結論タグが指定どおりか（特に「心裡留保」の「裡」の字形）。")
    out.append("- 導入のイラスト・文章の段落が、ヘッダーと最初の帯の間に描かれていないか。最後のカードのあとに何も描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-0_zentai.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
