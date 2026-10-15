# 【M3-3_c】他人物売買で所有権が移る時点の時間軸：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-3_c.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-3_c"
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

TOPIC = "【M3-3】順次譲渡（甲→乙→丙）で、相続人・債権者・他人物売買をどう扱うか"
SCOPE = "【M3-3】の「中身の整理」の直後（他人物売買で所有権が買主に移る時点の時間軸）"
DIFF = "既存の図解（三つの場面の対比表）との違い：既存の図解は、他人物売買で『買主に所有権が移るのは、いつか』を表の1マスで示すだけです。この図解は、誤りの多い『元の所有者から売主への移転登記の時点』と『売主が所有権を取得した時』を、3つの時点の時間軸で見分けます。"

def img1():
    steps = [
        ("売主が、元の所有者の土地を買主に売る",
         "An isometric small house on a plot of land with a dark navy name tag " + q("所有者：元の所有者") + ". Beside it, two faceless pictograms in the same light gray-blue color tagged " + q("売主") + " and " + q("買主") + " exchanging a document sheet labeled " + q("売買契約") + ".",
         ["他人の物の売買も、契約は有効", "売主は、取得して買主に移す義務を負う"], "契約の時点"),
        ("売主が、元の所有者から買い受ける",
         "The same isometric house; its name tag now reads " + q("所有者：買主") + ". Three faceless pictograms in a row tagged " + q("元の所有者") + ", " + q("売主") + " and " + q("買主") + ", with a dark navy arrow labeled " + q("取得") + " from 元の所有者 to 売主 and a short dark navy arrow labeled " + q("そのまま移る") + " from 売主 on to 買主.",
         ["売主が、所有権を取得した", "その時に、買主に移る"], "ここで移る"),
        ("売主への移転登記をする",
         "The same isometric house with the name tag " + q("所有者：買主") + " unchanged. Beside it, a registry ledger with a small rubber stamp labeled " + q("売主への移転登記") + ".",
         ["登記の時点で、初めて移るのではない", "移る時期は、取得した時"], "登記は別"),
    ]
    body = [lead("1080x2100", "This is a vertical timeline poster with three numbered cards (時間軸); it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + \
           header("他人物売買で、いつ買主に移る？", "売主が取得した時に移る", "民法　第561条")
    for i, (h, ill, items, tag) in enumerate(steps, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 3 in order). Cards are joined by short straight dark navy arrows pointing down (no labels on those arrows).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Item lines (two short lines of dark navy text beside the illustration, each with a small dark navy dot at its left end, NO number on the dots):"] + [q(x) for x in items] + \
                ["Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    body += ["Under the last card, one wide dark navy band with large white text " + q("移るのは、売主が取得した時") + ".",
             "Counts: 3 cards. The house name tag reads 「所有者：元の所有者」 only in card 1, and 「所有者：買主」 in cards 2 and 3. The three conclusion tags are different strings."]
    return finish(body, "Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, that the house name tag reads 所有者：元の所有者 in card 1 and 所有者：買主 in cards 2 and 3, that the registry ledger with the stamp 売主への移転登記 appears only in card 3, that the dark navy band is the last element, that no check mark, cross mark, blue, or red appears anywhere, and that all person names are role names with no Latin letters.")

META = [(1, "他人物売買で、いつ買主に移る？（3つの時点の時間軸）", "時間軸カード型（3枚）", "1080×2100", "民法編3_3_追加_他人物売買で所有権が移る時点", "【M3-3】の「中身の整理」の直後", img1)]

CHECKS = ["カードがちょうど3枚で番号が1〜3の順。家の名札が、カード1だけ『所有者：元の所有者』、カード2・3は『所有者：買主』",
          "カード3だけに、登記簿と『売主への移転登記』の印がある。最後の要素が濃紺の帯『移るのは、売主が取得した時』",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない。人型の名札が役割名（英字なし）"]
NOTES = ["他人物売買：民法561条『他人の権利を売買の目的としたときは、売主は、その権利を取得して買主に移転する義務を負う』（`note-articles/laws/minpou-2-saiken.md` で原文確認済み）。契約が有効で、売主が取得した時に買主に移り、売主への移転登記の時点とは限らない、という記事【M3-3】の中身の整理に合わせた",
         "カード2の『そのまま移る』：記事の結論（売主が取得した時点で買主に移る）。民法561条は売主の義務を定める規定で、移転の時期そのものを明記した条文ではない（判例・通説の整理）",
         "カード3の『登記は別』：記事の『売主への移転登記の時点とは限りません』を図にしたもの。登記の対抗の問題（民法177条）とは別の問い"]


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
