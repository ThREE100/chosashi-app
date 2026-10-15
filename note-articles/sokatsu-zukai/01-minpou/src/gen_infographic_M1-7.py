# 【M1-7】時効の援用・更新・完成猶予：承認と猶予は何を変えるのか。図解インフォグラフィック1枚のプロンプトを組み立てる。
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py。実行: python3 gen_infographic_M1-7.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

NAME = "M1-7"
TITLE = "時効の援用・更新・完成猶予：承認と猶予は何を変えるのか"

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def card(i, h, ill, tag):
    return [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 6 in order).",
            "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
            "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]

def img():
    cards = [
        (1, "だれが援用できる？",
         "One large person pictogram with the dark navy name tag " + q("債務者") + " at the left, and three smaller person pictograms in a row at the right with dark navy name tags " + q("保証人") + ", " + q("物上保証人") + " and " + q("第三取得者") + ". All four pictograms have faceless heads and the same light gray-blue color.",
         "当事者と、正当な利益を有する者"),
        (2, "承認すると、どうなる？",
         "A hand signing a paper sheet labeled " + q("承認") + ", and beside it a desk calendar whose day counter is restarting from the first day, with the small label " + q("時効期間のやり直し") + ".",
         "承認の時から新たに進行（更新）"),
        (3, "一部弁済は、どうなる？",
         "A small stack of coins being handed over, with the tag " + q("一部弁済") + ", and beside it a document sheet labeled " + q("残りの債務") + " with a signing hand on it.",
         "残りの債務の承認にあたる"),
        (4, "完成のあとに承認したら？",
         "A calendar page with a rubber stamp " + q("完成") + ", and to its right a signed paper sheet labeled " + q("承認") + " followed by a closed padlock icon with the label " + q("援用できない") + ". Below the illustration, one thin dotted-outline light-gray tag (with no check mark and no cross) reads " + q("完成を知っていたかは問わない") + ".",
         "その後は援用できなくなる"),
        (5, "更新の効力は、だれに及ぶ？",
         "Two person pictograms side by side with dark navy name tags " + q("債務者") + " and " + q("保証人") + ". A signed paper sheet labeled " + q("承認") + " lies in front of the " + q("保証人") + " pictogram only, enclosed by a thin dark navy bracket, with the small label " + q("自分の保証債務") + ". A small dotted-outline tag reads " + q("主債務の時効は援用できる") + ".",
         "更新の効力は当事者の間だけ"),
        (6, "完成が猶予されるのは？",
         "Two document sheets side by side. The left sheet is labeled " + q("訴えの取下げ") + " with a small calendar tag " + q("終了の時から6か月") + ". The right sheet is labeled " + q("法定代理人のいない成年被後見人") + " with a small label " + q("期間満了前6か月以内") + " and a small calendar tag " + q("就職の時などから6か月") + ".",
         "6か月と起算点をセットで"),
    ]
    body = [lead("1080x2700", "This is a quick-reference poster with six numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("時効の援用・更新・完成猶予", "承認と猶予は何を変えるか", "民法 第145条・第147条・第152条・第153条・第158条")
    for c in cards:
        body += card(*c)
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 6 exactly, numbered 1 to 6 in order, with no duplicated or missing cards; confirm there is no intro illustration or paragraph block between the header and the cards; confirm that no card contains a full sentence of explanatory prose; confirm that no check mark and no cross mark appears anywhere; and confirm that the text " + q("債務者") + " and " + q("保証人") + " are drawn exactly as given.")

META = [(1, TITLE, "カードポスター型（俯瞰。援用できる人→承認と更新→一部弁済→完成後の承認→更新の効力の範囲→完成猶予）", "1080×2700", "図解_M1-7_時効の援用・更新・完成猶予", "総合記事 sokatsu-01-minpou.md の【M1-7】の「中身の整理」の直後", img)]

def build_doc():
    out = [f"# 【{NAME}】{TITLE}　図解インフォグラフィック プロンプト（{len(META)}枚）\n"]
    out.append("民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M1-7】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。キャラクターは描かないので、参照画像は不要です。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}")
        out.append(f"  - サイズ：{size}")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append(f"保存名：`{fn}.png`\n")
        out.append("検品チェック：\n- カードが6枚で、番号が1〜6の順に並んでいる\n- 文字が簡体字・繁体字になっていない（特に 援・承・認・猶・予・債・保・証）\n- 背景が透過していない\n- 最後のカードの下に、まとめの枠・トロフィー・○×の再掲が描かれていない\n- カード4の点線の札と、カード5の点線の札に、チェックや×の印が付いていない\n- 画像の中に図の番号・問題番号・年度がない\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / f"prompt_infographic_{NAME}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
