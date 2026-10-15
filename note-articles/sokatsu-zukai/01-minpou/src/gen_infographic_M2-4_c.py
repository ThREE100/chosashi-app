# 【M2-4】占有の訴えの相手方と、本権との関係：追加の図解（占有の訴えと本権の訴えは別の土俵）1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M2-4.py＝4つの場面の早見表）では行の文章になっている、占有の訴えと本権の訴えの関係（民法202条）と、所有者でも実力で排除できない点を、4枚のカードで描く。
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

PERSON = "All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags)."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    cards = [
        ("占有の訴えと本権の訴えは別物",
         "Two document sheets side by side with a plain dark navy double-headed arrow between them; the left sheet is labeled " + q("占有の訴え") + " and the right sheet is labeled " + q("本権の訴え") + "; a small dark navy tag " + q("民法202条1項") + " under the arrow.",
         "互いに妨げない"),
        ("占有の訴えで所有権を主張しても",
         "A court building icon. Beside it a faceless pictogram tagged " + q("被告") + " holding a speech tag " + q("私の所有地だ") + " that stops at a plain dark navy shield icon labeled " + q("判断の材料にならない") + "; a small dark navy tag " + q("民法202条2項") + ".",
         "防御方法にならない"),
        ("所有者でも実力では排除できない",
         "A flat house icon with a faceless pictogram tagged " + q("不法占拠者") + " standing inside, and outside a heavy machine (excavator) icon with a dark navy caution triangle sign in front of it; on the right a small document sheet labeled " + q("占有保全の訴え") + " with the small label " + q("解体の予防を請求") + ".",
         "自力救済は原則不可"),
        ("所有権を争うなら",
         "A faceless pictogram tagged " + q("所有者") + " holding a document sheet labeled " + q("本権の訴え") + " and walking toward a court building icon, with a small light-gray label " + q("別に起こす") + ".",
         "別に本権の訴えを起こす"),
    ]
    body = [lead("1080x2500", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. " + PERSON + " The only arrows are the ones described in the illustrations."] + \
           header("占有の訴えと本権の訴え", "別々の土俵で争う", "民法 第199条・第202条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to {len(cards)} in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that card 2 shows the speech tag 私の所有地だ stopped by the shield and card 4 shows the 所有者 pictogram holding a document sheet labeled 本権の訴え, confirm that the last element is card 4, and confirm that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "占有の訴えと本権の訴え（別々の土俵で争う）", "カードポスター型（4枚）", "1080×2500", "民法編2_M2-4_追加_占有の訴えと本権の訴え", "【M2-4】の「たとえば」の直後", img1)]

def build_doc():
    out = ["# 【M2-4】占有の訴えの相手方と、本権との関係はどうなっているのか　追加の図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-4】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-4.md`＝4つの場面の早見表）は変更せず、"
               "表では行の文章になっている「占有の訴えと本権の訴えは別物であること」「占有の訴えで所有権を持ち出せないこと」「所有者でも実力で排除できないこと」「所有権を争うには別に本権の訴えを起こすこと」を、記事の「たとえば」（不法占拠の小屋を所有者が重機で解体しようとする例）に沿って4枚のカードで補います。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図は、はい／いいえの分岐ではないため、青・赤は使いません。画像の中には、図の番号・問題番号・個人の演習結果を入れません。\n")
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
    out += ["- カードがちょうど4枚で、1〜4の番号が順に付き、最後のカードのあとに何も描かれていないか。",
            "- カード2：「私の所有地だ」の吹き出しが盾で止まっているか。カード4：所有者が「本権の訴え」の書類を持って裁判所へ向かっているか。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「占有」「本権」「妨」「防御」「所有」「排除」「保全」「予防」が簡体字・別字になっていない）。",
            "- 青・赤・○×の印がどこにもない。人物はすべて同じ色の顔なしピクトグラム。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- 民法202条1項（占有の訴えは本権の訴えを妨げず、本権の訴えは占有の訴えを妨げない）・2項（占有の訴えについては、本権に関する理由に基づいて裁判をすることができない）、199条（占有保全の訴え：占有を妨害されるおそれがあるときは、妨害の予防又は損害賠償の担保を請求できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。",
            "- 「自力救済は原則不可」は、記事の中身の整理（不法占拠者でも占有は保護され、相手が真の所有者でも、自力救済は原則として許されません）による。自力救済の禁止そのものを明記した条文はなく、判例・通説の整理である。図では『原則』と添え、断定を避けた。",
            "- 「不法占拠者」の小屋の解体を占有保全の訴えで予防できる点は、記事の『たとえば』と肢の判定による。『被告』の『私の所有地だ』という吹き出しは、記事の『Bが『この土地は私の所有だ』と言って反論しても、占有の訴えの中では決め手になりません』に合わせた。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-4_c.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
