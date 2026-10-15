# 【M2-5】所有権に基づく物権的請求権：図解インフォグラフィックのプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

# ---------------------------------------------------------------- 図解1：5つの確認ポイント（カードポスター型）
def img1():
    cards = [
        ("請求できるのは誰？",
         "A person pictogram with the name tag " + q("所有者") + " standing beside a flat house icon, with a small label " + q("買主を含む") + " under the pictogram.",
         "所有権を取得した人"),
        ("いつから所有者になる？",
         "A contract sheet icon labeled " + q("売買契約") + " beside a blank calendar page with no numbers on it, and a small label " + q("移転時期の特約なし") + ".",
         "特約がなければ契約と同時"),
        ("登記がないと請求できない？",
         "A person pictogram with the name tag " + q("不法占有者") + " standing in front of a house icon, and beside it a registry ledger icon drawn with a thin dotted outline and the label " + q("登記は売主の名義のまま") + ".",
         "不法占有者には登記は不要"),
        ("登記が要る相手は？",
         "A person pictogram with the name tag " + q("二重に買った人など") + " and under it the small label " + q("正当な利益を有する第三者") + ", beside a registry ledger icon with one rubber stamp on it.",
         "登記の先後で決まる"),
        ("請求先は誰？",
         "A house icon with two person pictograms below it side by side: the left one with the name tag " + q("借りて住む人") + " and the small label " + q("直接占有") + ", and the right one with the name tag " + q("権原のない貸した人") + " and the small label " + q("間接占有") + ".",
         "どちらにも請求できる"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags)."] + \
           header("所有権に基づく返還請求", "5つの確認ポイント", "民法 第176条・第177条・第181条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, confirm that card 3 shows the tag 不法占有者 and card 4 shows the tag 二重に買った人など (they are NOT identical), and confirm that no check mark or cross mark appears anywhere.")

META = [
    (1, "所有権に基づく返還請求：5つの確認ポイント", "カードポスター型（俯瞰）", "1080×2300", "図解1_所有権に基づく返還請求", "「中身の整理」の直後（判断のしかたの前）", img1),
]

def build_doc():
    out = ["# 【M2-5】所有権に基づく物権的請求権　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事（民法編）`note-articles/column/sokatsu-01-minpou.md` の【M2-5】「所有権に基づく物権的請求権は、誰が誰に、どんな条件で行使できるのか」に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "この図は、4コマ（`4koma/prompt_4koma_M2-5_D1414-D0913-D0916-D1815.md`）とは別の角度で、判断のポイントを俯瞰する早見の図です。画像の中には、図の番号・問題番号・年度を入れません。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}　／　サイズ：{size}")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("## 検品チェック（生成後）\n")
    out += ["- カードがちょうど5枚で、1から5の順に並んでいる。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「登記」「占有」「権原」「間接」「買主」などが簡体字・別字になっていない）。",
            "- カード3のタグ「不法占有者」とカード4のタグ「二重に買った人など」が取り違えられていない。",
            "- ○×・青・赤の印がどこにもない。人物はすべて同じ色の顔なしピクトグラム。",
            "- 図の番号・問題番号・年度・個人の演習結果が画像の中にない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- カード1：総合記事M2-5の結論（所有者は不法占有者に返還請求できる）。買主を含むのは、中身の整理（所有権を取得して登記を得ていない買主）による。",
            "- カード2：中身の整理4つ目。民法176条（物権の設定及び移転は、当事者の意思表示のみによって、その効力を生ずる）を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認。特定物の売買で特約がなければ契約と同時に移るのは判例の立場（記事の記述どおり）。",
            "- カード3：中身の整理1・2つ目。民法177条の第三者は、登記がないことを主張する正当な利益を有する者に限られ、不法占有者はあたらない。",
            "- カード4：同じ総合記事の串刺し1とM3-1の節（二重譲受人は登記の先後で決まる）。M2-5の節には明記がなく、記事の別の節から取った対比。",
            "- カード5：中身の整理3つ目。民法181条（占有権は、代理人によって取得することができる）を原文で確認。無権原の賃貸人は賃借人を通じて間接的に占有している、という記事の記述どおり。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    outp = _here.parents[1] / "infographic" / "prompt_infographic_M2-5.md"
    outp.write_text(doc, encoding="utf8")
    print(outp, len(doc))
