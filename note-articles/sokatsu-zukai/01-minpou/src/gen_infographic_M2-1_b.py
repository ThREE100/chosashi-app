# 【M2-1】共有者の一人は、単独で何ができ、何ができないのか：追加の図解（場面図）1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M2-1.py＝判定の流れ）に足りない、持分3分の1ずつの共有者と相手方の「当事者の位置関係」と損害90万円→30万円の分け方を描く。
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

PERSON = "All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags)."
NEUTRAL = "Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. " + PERSON

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    cards = [
        ("見知らぬ人が居座ったとき",
         "A flat land plot icon. On its left side three faceless person pictograms stand in a row, each tagged " + q("共有者") + " and each with the small label " + q("3分の1") + ". On its right side, inside the plot, one faceless pictogram tagged " + q("居座る人") + ". One dark navy arrow runs from the first of the three " + q("共有者") + " pictograms to the " + q("居座る人") + " pictogram, carrying the label " + q("明渡しの請求") + ". A small light-gray tag under the plot: " + q("保存行為（民法252条5項）") + ".",
         "一人で全部を請求できる"),
        ("損害の賠償を求めるとき",
         "On the left, a circle divided into three equal slices (a pie without numbers) with the label " + q("損害90万円") + " above it. One slice has a pale yellow highlighter fill and the label " + q("30万円") + "; the other two slices are light gray and each carries the small label " + q("ほかの共有者の分") + ". On the right, one faceless pictogram tagged " + q("共有者") + " with the small label " + q("3分の1") + ", joined to the yellow slice by a thin plain dark navy line with no arrowhead.",
         "請求できるのは持分の分だけ"),
        ("共有者の一人が住んでいるとき",
         "A flat house icon. Inside it one faceless pictogram tagged " + q("住んでいる共有者") + " with the small light-gray note " + q("使う権原がある") + ". Outside the door two faceless pictograms standing side by side tagged " + q("ほかの共有者") + ", with one bracket over both labeled " + q("持分の合計3分の2") + ". One dark navy arrow runs from the two outside pictograms to the pictogram inside, carrying the label " + q("明渡しの請求") + ".",
         "過半数でも直ちには不可"),
    ]
    body = [lead("1080x2300", "This is a scene poster with three numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR, NEUTRAL + " The only arrows on this poster are the dark navy arrows in cards 1 and 3, and each means one thing: a request made against the person at the arrowhead."] + \
           header("共有地で起きる3つの場面", "誰が・誰に・何を請求するか", "民法 第249条・第252条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    body += ["Under the cards, one wide dark navy band with large white text " + q("第三者には、明渡しは単独で、お金は持分まで") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, confirm that card 1 shows three 共有者 pictograms and one 居座る人 pictogram, that card 2 shows a three-slice pie with exactly one pale yellow slice labeled 30万円, that card 3 shows one pictogram inside the house and two outside, that the only arrows are the two dark navy arrows in cards 1 and 3, that the dark navy band is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "共有地で起きる3つの場面（誰が・誰に・何を請求するか）", "場面図型（カードポスター）", "1080×2300", "民法編2_M2-1_追加_共有地で起きる3つの場面", "【M2-1】の「たとえば」の直後", img1)]

def build_doc():
    out = ["# 【M2-1】共有者の一人は、単独で何ができ、何ができないのか　追加の図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-1】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-1.md`＝相手と請求の中身で分かれる判定の流れ）は変更せず、"
               "そこに描かれていない「3人が3分の1ずつ持つ共有地で、誰が誰にどの請求をしているのか」という当事者の位置関係と、損害90万円を持分で分ける様子を、記事の「たとえば」に沿った3つの場面で補います。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。当事者はラテン文字を使わず、役割（共有者・居座る人）で書きます。\n")
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
    out += ["- カードがちょうど3枚で、1〜3の番号が順に付いているか。カード1は共有者3人と居座る人1人、カード2は3つに分けた円（黄色は1切れだけで30万円）、カード3は家の中に1人と外に2人か。",
            "- 矢印はカード1とカード3の濃紺の2本だけで、どちらも「明渡しの請求」の矢印か。いちばん下の濃紺の帯のあとに何も描かれていないか。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「共」「賠」「償」「権」「渡」「居座」が簡体字・別字になっていない）。",
            "- 青・赤・○×の印がどこにもない。人物はすべて同じ色の顔なしピクトグラム。",
            "- 図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- カード1・2・3は、記事【M2-1】の「たとえば」（持分3分の1ずつの共有地に見知らぬ人が居座る例、損害90万円なら30万円まで、共有建物に一人だけが住んでいる例）と「中身の整理」による。",
            "- 民法249条1項（各共有者は共有物の全部についてその持分に応じた使用ができる）、252条1項（管理は持分の価格の過半数）・3項（特別の影響を及ぼすべきときは承諾）・5項（保存行為は各共有者が単独でできる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。",
            "- カード1の「保存行為（民法252条5項）」と、不法占有者への明渡請求が保存行為にあたり共有物の全部を求められる点、カード2の損害賠償請求権が持分に応じて分かれる点は、記事が「判例」として示す整理である。条文は保存行為の存在を定めるのみで、これらの当てはめは判例による。図では条文の語に限って添えた。",
            "- カード3の「使う権原がある」は、記事の「単独で占有している共有者も、自分の持分に基づく使用の権原を持っています」による。過半数の決定があっても、特別の影響を及ぼすときは承諾が要る（252条3項）が、図には入れず既存の図解のタグに任せた。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-1_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
