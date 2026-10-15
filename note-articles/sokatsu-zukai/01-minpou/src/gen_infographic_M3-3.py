# 民法編・総合記事【M3-3】順次譲渡で、相続人・債権者・他人物売買をどう扱うか：図解インフォグラフィック1枚のプロンプトを組み立てる
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
import pathlib, sys

_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

M = "M3-3"


def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]


def img1():
    body = [lead("1080x2000", "This is a comparison table poster with three scene columns (対比表型)."), TEXTREQ, BGREQ, COLOR] + \
        header("売主の周りに出てくる三つの場面", "場面ごとに、見る点が違う", "民法 第177条・第423条・第561条") + \
        ["--- STRIP (directly below the header, one row, no paragraph) ---",
         "A short horizontal strip with three faceless flat person pictograms in exactly the same single light gray-blue color, from left to right, each with a dark navy name tag: " + q("元の所有者") + ", " + q("売主") + ", " + q("買主") +
         ". Between the pictograms are two plain thin dark navy arrows, each with a small label " + q("譲渡") + " (both arrows mean the same thing). Under the strip, one small light-gray tag: " + q("登記は、元の所有者の名義のまま") + ".",
         "--- TABLE ---",
         "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 4 columns (one row-label column and three scene columns) and exactly 4 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
         "Header row (dark navy cells with white text), from left to right, with a small light-gray tag under each of the three scene headers: the first cell is empty; the second header " + q("売主の相続人が出てきた") + " with the tag " + q("民法177条") +
         "; the third header " + q("売主の債権者が出てきた") + " with the tag " + q("民法423条") + "; the fourth header " + q("他人物売買だった") + " with the tag " + q("民法561条") + ".",
         "The three scene headers are NOT identical; copy each one exactly as given.",
         "Data row 1 (row label cell, dark navy, white text: " + q("問われること") + "): second column " + q("買主は、相続人に登記なしで主張できるか") + "; third column " + q("合意をしても、債権者は代位できるか") + "; fourth column " + q("買主に所有権が移るのは、いつか") + ".",
         "Data row 2 (row label cell, dark navy, white text: " + q("引かれやすい言葉") + "): second column " + q("登記名義人が元の所有者のまま") + "; third column " + q("直接登記名義を移転する旨の合意") + "; fourth column " + q("売主への所有権の移転の登記がされた時点") + ".",
         "Data row 3 (row label cell, dark navy, white text: " + q("見る点") + "): second column " + q("相続人は、売主の権利義務を包括的に承継する") + "; third column " + q("合意は、登記を移す経路の取決めにとどまる") + "; fourth column " + q("他人の物の売買も、債権契約としては有効") + ".",
         "Data row 4 (row label cell, dark navy, white text: " + q("答え") + "; every cell of this row has a pale yellow highlighter marker behind its text): second column " + q("登記なしで主張できる") +
         "; third column " + q("売主の登記請求権は消えず、債権者は代位できる") + "; fourth column " + q("売主が所有権を取得した時に移る") + ".",
         "At the bottom, one small light-gray tag centered across the table: " + q("中間省略登記の扱いは、判例の整理による"),
         "Every cell has its own text exactly as given; no two cells share the same text."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 4 columns and exactly 4 data rows, that the three scene headers read 売主の相続人が出てきた, 売主の債権者が出てきた and 他人物売買だった in this order, that every cell reads exactly as given, that the strip above the table has three pictograms and two arrows labeled 譲渡, and that no check mark, cross mark, blue or red appears anywhere.")


META = [
    (1, "売主の周りに出てくる三つの場面（相続人・債権者・他人物売買）", "対比表型（3列・4行）", "1080×2000", "図解1_売主の周りに出てくる三つの場面", "【M3-3】の『中身の整理』の直後", img1),
]


def build_doc():
    out = [f"# 【{M}】順次譲渡（A→B→C）で、相続人・債権者・他人物売買をどう扱うか　図解インフォグラフィック プロンプト（{len(META)}枚）\n"]
    out.append("民法編の総合記事（`note-articles/column/sokatsu-01-minpou.md`）の【M3-3】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一していますが、この図解は対比表なので、○×・青・赤は使いません。画像の中には、図の番号を入れません。"
               "4コマ（`4koma/prompt_4koma_M3-3_D0722-D0723-D1209.md`）が3つの肢を並べ直す形なのに対し、この図解は、場面ごとに『問われること・引かれやすい言葉・見る点・答え』を1枚で見比べる早見表です。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}")
        out.append(f"  - サイズ：{size}")
        out.append(f"  - 保存名：{fn}.png")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("## 検品チェック（生成後）\n")
    for c in ["表が4列（行の見出し＋3つの場面）・4行で、場面の見出しが左から『売主の相続人が出てきた』『売主の債権者が出てきた』『他人物売買だった』の順になっている",
              "各セルの文字がプロンプトと一字一句同じ（『登記なしで主張できる』『売主の登記請求権は消えず、債権者は代位できる』『売主が所有権を取得した時に移る』など）",
              "上の帯に人型が3つ（元の所有者・売主・買主）と矢印2本（どちらも『譲渡』）がある。人型は全部同じ色",
              "『答え』の行の文字だけに黄色のマーカーがある。○×・青・赤が一つもない",
              "簡体字・繁体字・英字・ハングルの混入がない。背景が不透明（透過・チェッカーボードなし）",
              "表の下に、まとめのパネル・トロフィー・追加の文章がない"]:
        out.append(f"- [ ] {c}")
    out.append("")
    out.append("## 記事・条文との照合（設計メモ）\n")
    for c in ["相続人は包括承継人で、177条の『第三者』ではない（記事【M3-3】中身の整理、H24-Q03イ）",
              "中間省略登記の合意があってもBの登記請求権は消えず、債権者は民法423条1項で代位できる（記事が『個別の判例の番号までは確認できていない』と注記しているため、図の下に『判例の整理による』の小さな札を付けた）",
              "他人物売買は契約として有効で、売主が取得した時点で買主に移る（民法561条：売主は、その権利を取得して買主に移転する義務を負う。法令DB `note-articles/laws/minpou-2-saiken.md` で確認）",
              "『引かれやすい言葉』は、元の肢の問題文からの引用（H24-Q03イ・ウ、H29-Q02ア）"]:
        out.append(f"- {c}")
    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    doc = build_doc()
    dest = _here.parents[1] / "infographic" / f"prompt_infographic_{M}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf8")
    print(dest, len(doc))
