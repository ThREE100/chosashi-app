# 【M2-3】占有回収の訴えを起こせるのは誰か：追加の図解（法人の代表者の二つの占有）1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M2-3.py）のカード5は「個人としても提起できる」だけで、機関としての占有と個人としての占有が併存する条件（特段の事情）が見えない。それを描く。
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

PERSON = "All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags)."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2100", "This is a relationship-diagram poster with two big cards in one column and a bottom band; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Each card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. " + PERSON + " The only lines and arrows are the ones described below."] + \
           header("法人の代表者が建物を奪われたとき", "機関の占有と個人の占有は別に数える", "民法 第200条（判例）") + \
           ["--- CARD 1 ---", "Badge: a filled dark navy circle containing the number 1 (numbers run 1 to 2 in order).",
            "Heading (bold, ONE line):", q("代表者の占有は二つありうる"),
            "Illustration (a wide relationship diagram inside the card): a flat office building icon at the right. At the left, one faceless pictogram tagged " + q("代表者") + ", and above it a small company icon tagged " + q("法人") + ". Two dark navy lines run from the 代表者 pictogram to the building. The upper line carries the label " + q("機関としての占有") + " with the small light-gray label " + q("法人のため") + ". The lower line carries the label " + q("個人としての占有") + " with the small light-gray label " + q("特段の事情があるとき") + ". The two lines are drawn clearly separate and never merge.",
            "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q("両方の占有が併存する"),
            "--- CARD 2 ---", "Badge: a filled dark navy circle containing the number 2 (numbers run 1 to 2 in order).",
            "Heading (bold, ONE line):", q("占有を奪われたとき"),
            "Illustration: one faceless pictogram tagged " + q("代表者") + " holding a small document sheet labeled " + q("占有回収の訴え") + ", with a thin plain dark navy line from the sheet to a small badge labeled " + q("個人としての占有") + ", and a small light-gray label " + q("判例の立場") + " beside the sheet.",
            "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q("個人としても提起できる"),
            "Under the two cards, one wide dark navy band with large white text " + q("機関として持っていても、個人の占有は別にある") + "."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 2 exactly, numbered 1 and 2, that card 1 shows exactly two separate lines from the 代表者 pictogram to the building, one labeled 機関としての占有 and one labeled 個人としての占有, that card 2 shows the 代表者 pictogram holding a document sheet labeled 占有回収の訴え, that the dark navy band is the last element, and confirm that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "法人の代表者の二つの占有（機関としての占有と個人としての占有）", "関係図型（2枚のカード＋帯）", "1080×2100", "民法編2_M2-3_追加_法人の代表者の二つの占有", "【M2-3】の「判断のしかた」の直後", img1)]

def build_doc():
    out = ["# 【M2-3】占有回収の訴えを起こせるのは誰か　追加の図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch2.md`（民法編・第2章）の論点【M2-3】に差し込む、追加の図解のプロンプトです。既存の図解（`prompt_infographic_M2-3.md`＝5枚のカード）は変更せず、"
               "そのカード5（代表者）は「個人としても提起できる」の結論だけで、機関としての占有と個人としての占有が別々に数えられ、特段の事情があるときに併存することが見えないため、"
               "記事の中身の整理（法人の代表者が建物を法人の機関として占有しつつ、特段の事情により個人のためにも占有している場合）に沿って、2つの占有を1枚の関係図で補います。"
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
    out += ["- カードがちょうど2枚（番号1・2）で、いちばん下に濃紺の帯が1本あり、そのあとに何も描かれていないか。",
            "- カード1：代表者から建物へ向かう線がちょうど2本で、上が「機関としての占有（法人のため）」、下が「個人としての占有（特段の事情があるとき）」か。2本が1本に合流していないか。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「機関」「占有」「併存」「奪」「代表者」「法人」が簡体字・別字になっていない）。",
            "- 青・赤・○×の印がどこにもない。図の番号・問題番号・個人の演習結果がない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- 民法200条1項（占有者がその占有を奪われたときは占有回収の訴えにより物の返還及び損害の賠償を請求できる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。",
            "- 「機関としての占有と個人としての占有が併存し得る」「特段の事情により個人のためにも占有している場合」「個人として占有回収の訴えを提起できる」は、記事の中身の整理・結論による判例の整理で、条文に直接の記述はない。そのため図に小さく「判例の立場」と添え、断定を条文の効果のようには見せていない。",
            "- 記事は「機関としての占有とは別に個人としての占有があれば」と書き、機関としてのみ占有している場合の結論までは述べていない。図もその場合の結論（個人の占有はない等）は描かず、併存するときだけを描いた。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M2-3_c.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
