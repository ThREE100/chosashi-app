# 【M2-0】総合記事（民法編）第2章「物権」の全体図：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 論点6つの関係・読む順番・この章で分かれる「問い」の整理。画像の中に、図の番号・問題番号・個人の演習結果は入れない。
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def card_list(cards):
    """番号つきカードを縦に並べるポスター用。cards=(見出し, 絵の指示, [項目行], タグ)。"""
    out = []
    for i, (h, ill, items, tag) in enumerate(cards, 1):
        out += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                "Item lines (two or three short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
               ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    return out

def img1():
    cards = [
        ("共有者の一人にできること",
         "A flat land plot icon with three faceless person pictograms standing in a row on it, each with a small tag " + q("3分の1") + ".",
         ["相手は、第三者か共有者か", "請求は、守る請求かお金か"], "共有"),
        ("占有の善意・悪意と移転",
         "A short horizontal timeline with three small markers, and under it three faceless person pictograms in a row joined by two plain dark navy arrows pointing right, no text.",
         ["悪意とみなすのは、いつからか", "善意・悪意の基準は、誰か", "指図の承諾をするのは、誰か"], "占有の基準"),
        ("占有回収の訴えを起こせる人",
         "A flat house icon with one faceless person pictogram outside the closed door and a second pictogram drawn with a thin dotted outline standing behind it, no text.",
         ["占有者のほかに、誰が起こせるか", "転貸人は起こせるか", "代表者個人は起こせるか"], "占有回収の訴え"),
        ("占有の訴えの相手方と本権",
         "Two document sheets side by side with a plain dark navy double-headed arrow between them, the left sheet labeled " + q("占有の訴え") + " and the right sheet labeled " + q("本権の訴え") + ".",
         ["奪った者が貸しただけなら、誰が相手か", "所有権は、防御方法になるか"], "相手方と本権"),
        ("所有権に基づく返還請求",
         "A flat house icon with a faceless person pictogram tagged " + q("所有者") + " beside it and a second pictogram tagged " + q("不法占有者") + " standing in the doorway.",
         ["誰が、誰に、請求できるか", "登記がなくても請求できるか", "所有権は、いつ移るか"], "物権的請求権"),
        ("袋地の通行権と付合の償金",
         "A flat land plot icon completely surrounded by other land plots, with a short dotted dark navy path leading out to a road strip at the edge, and a small young tree planted on a plot at the side, no text.",
         ["袋地ができた原因は、何か", "通行権の主張に、登記は要るか", "付合で失った者は、償金を請求できるか"], "通行権と償金"),
    ]
    body = [lead("1080x3300", "This is a quick-reference poster with six numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading, two or three short item lines, and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, NOCOLOR] + header("物権の肢は、誰が・誰に、で読む", "共有・占有・所有権・通行権の6つ", "民法 物権（共有・占有・物権的請求権・通行権）") + \
           ["One thin pale-yellow banner under the header with the text " + q("共有、占有、所有権、隣の土地の順に読む") + "."] + \
           card_list(cards) + \
           ["Under the cards, one wide dark navy band with large white text " + q("どの肢も、誰が・誰に・何を、を先に書き出す") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 6 exactly, numbered 1 to 6 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that each card has two or three item lines and exactly one conclusion tag, confirm that the thin pale-yellow banner is under the header and the dark navy band is the last element, and confirm that no card contains a full sentence of explanatory prose and that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "物権の肢は、誰が・誰に、で読む（第2章の6つの論点と、分かれる問い）", "カードポスター型（俯瞰）", "1080×3300", "民法編2_全体図_物権の肢を読む順", "章の冒頭（「この章の誤りの傾向」の直後、【M2-1】の見出しの直前）", img1)]

def build_doc():
    out = ["# 【M2-0】第2章（物権）の全体図　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の冒頭に差し込む、章全体の図解のプロンプトです。論点【M2-1】〜【M2-6】の関係（共有→占有→所有権→隣の土地の読む順）と、各論点で分かれる「問い」（誰が・誰に・何を）を1枚で俯瞰します。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "分類・カードの図は、はい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・個人の演習結果（誤りの回数など）を入れません。キャラクターは描きません。\n")
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
    out += ["- カードがちょうど6枚で、1〜6の番号が順に付き、各カードに見出し1行・項目2〜3行・黄色い結論タグが1つあるか。",
            "- 見出し直下の黄色い薄い帯が1本、いちばん下の濃紺の帯が1本で、そのあとに何も描かれていないか。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「占有」「回収」「償」「袋」「付合」「承諾」が簡体字・別字になっていない）。",
            "- 青・赤・○×の印がどこにもない。人物はすべて同じ色の顔なしピクトグラム。",
            "- 図の番号・問題番号・個人の演習結果が画像の中にない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- 6枚のカードの順序と見出しは、第2章の論点【M2-1】〜【M2-6】の見出し・「判断のしかた」に合わせた。カードの項目行は、各論点の「判断のしかた」で最初に確かめる問いを短くしたもの。",
            "- 「共有、占有、所有権、隣の土地の順に読む」は、章の並び（共有〔M2-1〕→占有〔M2-2〜M2-4〕→所有権に基づく請求〔M2-5〕→袋地の通行権・付合〔M2-6〕）を言葉にした整理で、条文に直接の根拠のある語ではない。",
            "- 項目行は問いの形にとどめ、結論は書いていない（結論は各論点の本文と、論点ごとの図解で示す）。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-0_zentai.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
