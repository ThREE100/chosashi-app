# 【M3-1_c】第三者に当たる者・当たらない者の早見表：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-1_c.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-1_c"
NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."
PERSON = "faceless flat person pictograms in exactly the same single light gray-blue color, each with a dark navy name tag"
GLANCE = ("GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the first element. "
          "Every element communicates its point through the illustration plus short labels. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text beyond the short strings listed below.")

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def finish(body, extra):
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), extra)

def table_block(cols, rows, hl, label_col=False):
    n = len(cols)
    out = ["--- TABLE ---",
           f"Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly {n} columns and exactly {len(rows)} data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
           "Header row (dark navy cells with white text): " + ", ".join(q(c) if c else "an empty cell" for c in cols) + ".",
           "Data rows, one per line, in this order (" + " | ".join(f"column {i+1}" for i in range(n)) + "):"]
    out += [f"Row {i}: " + " | ".join(q(c) for c in r) for i, r in enumerate(rows, 1)]
    out.append(hl)
    return out

TOPIC = "【M3-1】単純悪意者や背信的悪意者の転得者に、登記なしで勝てるか"
SCOPE = "【M3-1】の「中身の整理」の直後（第三者に当たる者と当たらない者の早見表）"
DIFF = "既存の図解（判定の流れ図）との違い：既存の図解は、あとで買った人が背信的悪意者かどうかの流れを見せます。この図解は、記事の『中身の整理』にある、177条の『第三者』に当たる者と当たらない者を、1枚の早見表で並べ直したものです。"

def img1():
    rows = [("二重に買った人", "当たる", "登記の先後で決まる"),
            ("知っていただけの悪意者", "当たる", "知っていることと、信義則に反することは別"),
            ("背信的悪意者から買った転得者", "当たる", "転得者自身が背信的悪意者でない限り"),
            ("当事者", "当たらない", "売った人と、買った人の間"),
            ("包括承継人（相続人など）", "当たらない", "当事者の地位を、そのまま承継する"),
            ("前主・後主の関係にある者", "当たらない", "権利を渡した側と、受けた側"),
            ("不法占拠者", "当たらない", "登記がないことを主張する正当な利益がない"),
            ("背信的悪意者本人", "当たらない", "自由競争の範囲を逸脱し、もっぱら害する目的")]
    body = [lead("1080x2100", "This is a reference table poster with three columns (早見表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("第三者に当たるのは、誰？", "知っているだけでは外れない", "民法　第177条")
    body += table_block(["だれか", "第三者か", "見るポイント"], rows,
                        "Highlighting: the strings " + q("知っていただけの悪意者") + " in row 2 and " + q("背信的悪意者から買った転得者") + " in row 3 have a pale yellow highlighter marker; all other cells are plain. Copy each cell exactly as given. The strings " + q("当たる") + " and " + q("当たらない") + " repeat on purpose in the second column (3 rows and 5 rows), and the strings " + q("当たる") + " and " + q("当たらない") + " are NOT identical, so copy each exactly.")
    body += ["Under the table, one wide dark navy band with large white text " + q("知っているだけでは、第三者から外れない") + ".",
             "Under the band, one small light-gray tag: " + q("第三者の範囲は、判例による整理") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 8 data rows, that rows 1 to 3 read 当たる and rows 4 to 8 read 当たらない in the second column, that every cell reads exactly as given, that only the two cells in rows 2 and 3 of the first column are highlighted, and that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "第三者に当たるのは、誰？（当たる者・当たらない者の早見表）", "早見表型（3列・8行）", "1080×2100", "民法編3_1_追加_第三者に当たる者の早見表", "【M3-1】の「中身の整理」の直後", img1)]

CHECKS = ["表が3列・8行で、第2列が上から『当たる』3つ→『当たらない』5つ。各セルの文字がプロンプトと一字一句同じ",
          "黄色のマーカーは、1列目の2行目『知っていただけの悪意者』と3行目『背信的悪意者から買った転得者』だけ",
          "表の下に濃紺の帯『知っているだけでは、第三者から外れない』と灰色の小さな札。それ以外のまとめ・追加の文章がない",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない"]
NOTES = ["第三者に当たる者（二重譲受人・単純悪意者・背信的悪意者から買った転得者）と、外れる者（当事者・包括承継人・前主後主の関係にある者・不法占拠者・背信的悪意者）：記事【M3-1】の『中身の整理』の列挙のとおり",
         "『見るポイント』の列：行1〜3と行8は記事の本文（『知っていることと、信義則に反することは別です』『背信的悪意者本人でない限り保護』『自由競争の範囲を逸脱し、もっぱら相手を害する目的』）の範囲。行4〜6は定義的な言い換え、行7『登記がないことを主張する正当な利益がない』は、第三者を『登記の欠缺を主張する正当な利益を有する者』とする判例の一般的な説明で、記事に明記はない（図の下の札『第三者の範囲は、判例による整理』で添えた）",
         "民法177条の原文：`note-articles/laws/minpou-1-soukyoku-bukken.md` で確認済み（登記をしなければ、第三者に対抗することができない）。『第三者』の範囲は条文に定義がなく、判例による"]


def build_doc():
    out = [f"# {TOPIC}　追加の図解インフォグラフィック プロンプト（{len(META)}枚）\n"]
    out.append("総合記事『直前期の苦手論点つぶし総合記事①民法編』の第3章（`note-articles/column/sokatsu-01-minpou-ch3.md`）の" + SCOPE + "に差し込む、追加の図解のプロンプトです。"
               "作成済みの図解（`infographic/prompt_infographic_M3-?.md`）は変えず、記事の要点のうち図がなかった部分を補います。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・判例番号・個人の演習結果を入れません。当事者はラテン文字ではなく役割名で書いています。キャラクターは描かないので、参照画像は不要です。\n")
    out.append(DIFF + "\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}（型：{typ}／サイズ：{size}）")
        out.append(f"  - 保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("```text\n" + fnc() + "\n```\n")
    out.append("### 検品チェック（生成後）\n")
    for c in CHECKS:
        out.append(f"- [ ] {c}")
    out.append("")
    out.append("### 記事・条文との照合\n")
    for c in NOTES:
        out.append(f"- {c}")
    out.append("")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    dest = _here.parent.parent / "infographic" / f"prompt_infographic_{KEY}.md"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(doc, encoding="utf8")
    print(dest, len(doc))
