# 【M2-6】袋地の通行権と付合の償金：図解インフォグラフィックのプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

# ---------------------------------------------------------------- 図解1：一般の袋地と分割・一部譲渡の袋地（対比表型・2列）
def img1():
    body = [lead("1080x1900", "This is a two-column comparison poster (対比表)."), TEXTREQ, BGREQ, COLOR] + \
           header("袋地の通行権", "一般の袋地と、分割の袋地", "民法 第210条・第213条") + \
           ["--- LEFT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("一般の袋地"),
            "--- RIGHT COLUMN HEADER (pill-shaped badge, dark navy) ---", q("分割・一部譲渡の袋地"),
            "The two columns are aligned: each row of the left column sits at exactly the same height as the same row of the right column. Each row is a rounded card with a small dark navy row label on its left edge. Use neutral dark navy outlines only; draw no check mark and no cross mark anywhere, and use no blue or red.",
            "--- ROW 1 (row label " + q("袋地ができた原因") + ") ---",
            "Left card: a land plot icon surrounded on all sides by other land plots, with the string " + q("分割・一部譲渡以外") + ".",
            "Right card: a land plot icon split into two by a boundary line, with the string " + q("一筆を分けて譲渡") + " and, under it, a small light-gray tag " + q("競売による場合も同じ") + ".",
            "--- ROW 2 (row label " + q("通れる土地") + ") ---",
            "Left card: a path icon running across the surrounding land plots, with the string " + q("囲んでいる他の土地") + ".",
            "Right card: a path icon running only across the one neighboring plot that was split off, with the string " + q("分けた相手の土地だけ") + " in a pale yellow highlighter marker.",
            "--- ROW 3 (row label " + q("償金") + ") ---",
            "Left card: a coin icon with the string " + q("償金を払う必要がある") + ".",
            "Right card: a coin icon with the string " + q("償金は払わなくてよい") + ".",
            "--- BOTTOM BAND (one wide dark navy band centered across both columns, white text) ---",
            q("どちらも、通行権の主張に所有権の移転の登記は要らない"),
            "The left and right cards of each row have clearly different texts; the texts are NOT identical."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 2 columns and exactly 3 rows of cards plus one bottom band, that the left and right texts of each row are different (especially 償金を払う必要がある on the left and 償金は払わなくてよい on the right, and 囲んでいる他の土地 on the left and 分けた相手の土地だけ on the right), and that no check mark or cross mark appears anywhere.")

# ---------------------------------------------------------------- 図解2：付合の償金（番号つきの流れ）
def img2():
    steps = [
        ("物が不動産に付合する",
         "A flat land plot icon with a small young tree planted on it, drawn so that the tree is fixed to the ground, with the small label " + q("従として付合した物") + ".",
         "不動産に従としてくっつく"),
        ("不動産の所有者が取得する",
         "A person pictogram with the name tag " + q("不動産の所有者") + " standing beside the land plot icon with the tree, and a small dark navy tag " + q("民法242条") + ".",
         "付合した物の所有権を取得"),
        ("所有権を失った者が出る",
         "A person pictogram with the name tag " + q("所有権を失った者") + " looking at the land plot, with a small light-gray label " + q("損失を受けた") + ".",
         "損をする人が生じる"),
        ("償金を請求できる",
         "The same person pictogram with the name tag " + q("所有権を失った者") + " handing a document sheet labeled " + q("償金の請求") + " to the pictogram " + q("不動産の所有者") + ", and a small dark navy tag " + q("民法248条") + ".",
         "不当利得の規定に従う"),
    ]
    body = [lead("1080x1900", "This is a step-by-step flow poster with four numbered cards in one column."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "Use neutral dark navy outlines only on this poster; draw no check mark and no cross mark anywhere, and use no blue or red. All person pictograms are faceless and drawn in ONE single identical light gray-blue color, the very same shade for every one of them (they differ only by their name tags). Between the cards draw small dark navy down-pointing arrows that all mean the same thing (the next step); draw no other arrows."] + \
           header("付合した物の所有権を失ったら", "償金の請求までの流れ", "民法 第242条・第248条・第703条")
    for i, (h, ill, tag) in enumerate(steps, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that all arrows between the cards point down and are dark navy, and confirm that no check mark or cross mark appears anywhere.")

META = [
    (1, "一般の袋地と、分割・一部譲渡の袋地", "対比表型（2列）", "1080×1900", "図解1_一般の袋地と分割の袋地", "「中身の整理」の末尾の対比の行の直後", img1),
    (2, "付合した物の所有権を失ったら、償金を請求できる", "番号つきの流れ（カードポスター型）", "1080×1900", "図解2_付合の償金", "「中身の整理」の付合の項目の直後", img2),
]

def build_doc():
    out = ["# 【M2-6】袋地の通行権と付合の償金　図解インフォグラフィック プロンプト（2枚）\n"]
    out.append("総合記事（民法編）`note-articles/column/sokatsu-01-minpou.md` の【M2-6】「袋地の通行権と付合の償金は、どんな場面で、どう認められるのか」に差し込む図解のプロンプトです。"
               "この論点は、袋地の通行権と付合の償金という別々の制度を扱うため、1枚に詰め込まず2枚に分けました。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "この図は、4コマ（`4koma/prompt_4koma_M2-6_D0523-D0524-D0525.md`）とは別の角度で、しくみと対比を俯瞰する図です。画像の中には、図の番号・問題番号・年度を入れません。\n")
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
    out += ["- 図解1：列がちょうど2つ、行がちょうど3つ（原因・通れる土地・償金）と下の帯1つ。左右の同じ行の文言が取り違えられていない（「囲んでいる他の土地」は左、「分けた相手の土地だけ」は右）。",
            "- 図解2：カードがちょうど4枚で、1から4の順に並び、カードの間の矢印がすべて下向きの濃紺である。",
            "- 見出し・タグの文字を、上のコードブロックの文言と一字ずつ突き合わせた（「償」「袋」「付合」「譲」「競」「損」が簡体字・別字になっていない）。",
            "- ○×・青・赤の印がどこにもない。人物はすべて同じ色の顔なしピクトグラム。",
            "- 図の番号・問題番号・年度・個人の演習結果が画像の中にない。背景は完全に不透明。"]
    out.append("")
    out.append("## 記事・条文との照合（作成者用）\n")
    out += ["- 図解1：総合記事M2-6の節の『中身の整理』と、最後の対比の行（一般の袋地〔210条〕＝囲んでいる土地を通れて償金が必要、分割・一部譲渡による袋地〔213条〕＝分割の相手方の土地のみ・償金不要）による。民法210条1項・213条1項2項を `note-articles/laws/minpou-1-soukyoku-bukken.md` の原文で確認（213条1項は『他の分割者の所有地のみを通行することができる。この場合においては、償金を支払うことを要しない』、2項は一部譲渡に準用）。",
            "- 図解1の『競売による場合も同じ』：『一筆の土地の一部に設定された抵当権が実行されて競落された場合も、一部譲渡に準じて扱われるのが判例の立場』（記事）。条文に明記はなく、判例の整理なので、断定を崩さず『同じ』と短く書いた。",
            "- 図解1の下の帯：『袋地の通行権は法律上当然に生じ、所有権の移転の登記がなくても主張できます（判例）』（記事）。",
            "- 図解2：中身の整理（民法242条＝不動産の所有者は従として付合した物の所有権を取得する、民法248条・703条＝損失を受けた者は不当利得の規定に従って償金を請求できる）。242条・248条・703条を `minpou-1-soukyoku-bukken.md`・`minpou-2-saiken.md` の原文で確認。242条ただし書（権原によって附属させた他人の権利を妨げない）は記事の範囲外なので図に入れていない。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    outp = _here.parents[1] / "infographic" / "prompt_infographic_M2-6.md"
    outp.write_text(doc, encoding="utf8")
    print(outp, len(doc))
