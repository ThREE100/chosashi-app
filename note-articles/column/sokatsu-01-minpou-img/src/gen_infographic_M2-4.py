# 民法編・総合記事【M2-4】占有の訴えの相手方と、本権との関係：図解インフォグラフィック1枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x1900", "This is a quick-reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, COLOR] + \
           header("占有の訴えの相手方と本権", "4つの場面を早見表で", "民法 第199条・第200条・第202条") + \
           ["--- KEY RULE STRIP ---",
            "Directly below the header and above the table, one wide dark navy band with white text: " + q("占有の訴えと本権の訴えは、互いに妨げない（民法202条1項）") + ". The words " + q("互いに妨げない") + " have a pale yellow highlighter marker.",
            "--- TABLE ---",
            "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns and exactly 4 data rows, no merged cells, every cell text at least 26 px high, row heights may differ so that all text stays inside its cell. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
            "Header row (dark navy cells with white text), from left to right: " + q("場面") + ", " + q("結論") + ", " + q("理由と条文") + ".",
            "Data row 1: first column " + q("不法占拠の建物を、所有者が重機で解体しようとする") + "; second column " + q("不法占拠者は、解体の予防を請求できる") + "; third column " + q("占有は本権の有無を問わず保護される（民法199条）") + ".",
            "Data row 2: first column " + q("占有の訴えに、被告が所有権を主張する") + "; second column " + q("防御方法にならない") + "; third column " + q("本権に関する理由で裁判できない（民法202条2項）") + ".",
            "Data row 3: first column " + q("占有を奪った者が、建物を他人に貸しただけ") + "; second column " + q("なお、奪った者に回収の訴えができる") + "; third column " + q("間接占有を保っている（民法181条）") + ".",
            "Data row 4: first column " + q("占有を奪った者が、占有を手放した") + "; second column " + q("承継人には原則提起できない") + " on the first line and " + q("侵奪を知っていればできる") + " on the second line; third column " + q("特定承継人への制限（民法200条2項）") + ".",
            "Every cell has its own text exactly as given; no two cells have the same text."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the table has exactly 3 columns and exactly 4 data rows, that every cell reads exactly as given, that the dark navy band above the table is the only element between the header and the table, and that no check mark, cross mark, blue or red appears anywhere.")

META = [
    (1, "占有の訴えの相手方と本権の関係（4つの場面の早見表）", "早見表型（3列・4行）", "1080×1900", "図解_M2-4_占有の訴えの相手方と本権", "【M2-4】の「中身の整理」の直後", img1),
]

def build_doc():
    out = ["# 【M2-4】占有の訴えの相手方と、本権との関係　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("民法編・総合記事（`note-articles/column/sokatsu-01-minpou.md`）の論点【M2-4】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "配色は、肯定＝青、否定＝赤、中立＝濃紺で統一しています（この図は、はい／いいえの分岐がないので、青・赤は使いません）。画像の中には、図の番号・問題番号・年度を入れません。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}")
        out.append(f"  - サイズ：{size}")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、各プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("## 検品チェック\n")
    out += ["- 表がちょうど3列・4行（見出し行を除く）で、各セルの文字がプロンプトの文言と一字ずつ一致しているか。",
            "- 「民法199条」「民法202条」「民法181条」「民法200条」の条番号と項番号が崩れていないか。",
            "- 見出しと表の間に、濃紺の帯のほかの要素がないか。",
            "- 青・赤・✓・×が使われていないか。",
            "- 表の下に、まとめのパネル・トロフィーなどが描き足されていないか。",
            "- 背景が不透明か（透過・チェッカーボードがないか）。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M2-4.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
