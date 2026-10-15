# 【M3-6】不動産質は、全部弁済まで全体に及び、転質も使用収益も承諾が要らない：図解インフォグラフィック1枚のプロンプトを組み立てる
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
else:
    sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    cards = [
        ("一部を返しても、全部に及ぶ",
         "An isometric vacation cottage wrapped by a dark navy ribbon labeled " + q("質権") + ". Beside it, a horizontal bar split into two segments: a short segment labeled " + q("返した100万円") + " and a longer segment labeled " + q("残り200万円") + ", under a small label " + q("借入れは300万円") + ".",
         "全部の弁済まで全部に"),
        ("転質に、設定者の承諾はいらない",
         "A person pictogram with the name tag " + q("質権者") + " standing beside a stack of two cards: the lower card labeled " + q("質権") + " and the upper card labeled " + q("転質") + ". Next to the stack, a document sheet with a dotted outline labeled " + q("設定者の承諾") + " with a small gray tag " + q("いらない") + ". Under the stack, a small note " + q("損失は不可抗力でも責任") + ".",
         "自己の責任で転質"),
        ("使用・収益にも、承諾はいらない",
         "An isometric vacation cottage with a person pictogram tagged " + q("質権者") + " at its door and a small pile of coins labeled " + q("収益") + " beside it. Next to the cottage, a document sheet with a dotted outline labeled " + q("設定者の承諾") + " with a small gray tag " + q("いらない") + ".",
         "用法に従って使う"),
        ("使える代わりに、負担がある",
         "Two items side by side: on the left an invoice sheet labeled " + q("管理の費用") + " with a small tag " + q("質権者が負担") + "; on the right a coin drawn with a dotted outline labeled " + q("利息") + " with a small tag " + q("請求できない") + ".",
         "費用は負担、利息は不可"),
        ("使用・負担・利息は、定めで変えられる",
         "A contract sheet labeled " + q("設定行為") + " with a rubber stamp, and three small tags lined up beside it: " + q("使用・収益") + ", " + q("管理の費用") + ", " + q("利息") + ". A small label on the sheet: " + q("別段の定め") + ".",
         "設定行為の別段の定め"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text. Draw no check mark and no cross mark anywhere, and use no blue or red anywhere on this poster.",
            TEXTREQ, BGREQ, COLOR] + header("不動産質の質権者にできること", "全部に及び、承諾は要らない", "民法 第348条・第350条・第356条・第357条・第358条・第359条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose, a check mark, or a cross mark.")

META = [(1, "不動産質の質権者にできること（全部に及ぶ・転質・使用収益・負担）", "カードポスター型（5枚）", "1080×2300", "不動産質の質権者にできること_M3-6", "総合記事【M3-6】の「結論」の直後（または「中身の整理」の終わり）", img1)]

def build_doc():
    out = ["# 【M3-6】図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の【M3-6】（不動産質は、全部弁済まで全体に及び、転質も使用収益も承諾が要らない）に差し込む図解のプロンプトです。"
               "画像は生成していません（ChatGPTなどで手動生成）。作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、○×・はい／いいえの配色、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・個人の演習結果を入れません。文言は記事（`h20-mondai/q01-fudousan-shichi.md`）と法令DB（`note-articles/laws/`）の範囲です。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"- 図解：{t}")
        out.append(f"- 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"- 記事の挿入位置：{pos}\n")
        out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせてください。\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append("検品チェック：")
        out.append("- 文字が日本語の常用漢字・ひらがな・カタカナ・数字・「」（）・：／だけで、簡体字・繁体字・余計な文字がない")
        out.append("- カードがちょうど5枚で、番号が1〜5の順。カードの中に文章（説明文）がない")
        out.append("- カード1の「返した100万円」と「残り200万円」の数字が入れ替わっていない（借入れは300万円）")
        out.append("- カード2・3の点線の書類（設定者の承諾）に「いらない」の札がある")
        out.append("- ✓・✕・青・赤がどこにもない／背景が透過でなく、最後のカードの下に追加のまとめがない\n")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M3-6.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
