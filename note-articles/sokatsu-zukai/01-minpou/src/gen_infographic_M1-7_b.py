# 【M1-7】時効の援用・更新・完成猶予：追加の図解「更新はやり直し、完成猶予は先延ばし」1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 既存の図解（gen_infographic_M1-7.py）は6枚のカードの並びで、論点の題である「承認と猶予は何を変えるのか」＝更新と完成猶予の効果の違いを、時間軸で対比する図がないため補う。
# 実行: python3 gen_infographic_M1-7_b.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, final

NOCOLOR = "Draw no check mark and no cross mark, and use no blue or red anywhere in this image (this poster has no YES/NO meaning); use only dark navy, pale gray, white, and the pale yellow highlighter."

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    body = [lead("1080x2200", "This is a comparison poster: two cards side by side, each with a small timeline picture, followed by one wide card and one closing band."),
            TEXTREQ, BGREQ, NOCOLOR] + \
           header("更新と完成猶予の違い", "承認と猶予は何を変えるのか", "民法 第147条・第152条・第158条") + \
           ["--- TWO CARDS (side by side, exactly the same size, top-aligned, same pale gray fill, dark navy outline, each heading placed fully INSIDE the card) ---",
            "LEFT CARD: a small dark navy tag " + q("更新") + " and the heading (bold) " + q("時効が、新たに進行する") + ".",
            "  - Timeline picture: a horizontal bar that is filled with dark navy up to a vertical dashed line, then restarts as an empty bar from that line; a small rubber stamp icon sits on the dashed line, and the small label " + q("やり直し") + " is written under the empty part.",
            "  - Item lines (each with a small dark navy dot at its left end, NO number on the dots): " + q("承認") + " with the small gray tag " + q("152条1項") + "; " + q("一部弁済（残りの債務の承認）") + "; " + q("確定判決で権利が確定した裁判上の請求") + " with the small gray tag " + q("147条2項") + ".",
            "RIGHT CARD: a small dark navy tag " + q("完成猶予") + " and the heading (bold) " + q("その間は、時効が完成しない") + ".",
            "  - Timeline picture: a horizontal bar that is filled with dark navy and ends at a small flag; a second light-gray bar extends beyond the flag to the right with a bracket labeled " + q("6か月") + ", showing that the end is pushed back.",
            "  - Item lines (each with a small dark navy dot at its left end, NO number on the dots): " + q("訴えの取下げ → 終了の時から6か月") + " with the small gray tag " + q("147条1項") + "; " + q("法定代理人のいない成年被後見人 → 就職の時などから6か月") + " with the small gray tag " + q("158条1項") + ".",
            "The two cards have clearly different texts; the texts are NOT identical, so copy each exactly as given.",
            "--- WIDE CARD (a wide rounded card below the two cards, pale gray fill, dark navy outline, with NO arrow) ---",
            "Heading (bold, ONE line): " + q("時効の完成のあとに承認したら") + ".",
            "Body (ONE line): " + q("更新も猶予もなく、援用できない") + " with the small gray tag " + q("判例") + ".",
            "Under the body, a small dotted-outline tag (no check mark, no cross): " + q("完成を知らなくても同じ") + ".",
            "--- CLOSING BAND (the LAST element of the poster: one wide dark navy band with white text, placed directly below the wide card) ---",
            q("更新はやり直し、") + " on the first line and " + q("完成猶予は先延ばし") + " on the second line."]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm there are exactly 2 cards side by side, exactly 1 wide card and exactly 1 closing band in this order, that the left card has exactly 3 item lines and the right card has exactly 2 item lines, that the left timeline picture shows an empty bar restarting after the dashed line and the right timeline picture shows the end pushed back by a 6か月 bracket, that no check mark, cross mark, blue or red appears anywhere, and that nothing is drawn below the closing band.")

META = [(1, "更新と完成猶予の違い（承認と猶予は何を変えるのか）", "対比型（カード2枚＋カード1枚＋帯）", "1080×2200", "民法編1_M1-7_追加_更新と完成猶予の違い", "【M1-7】の「中身の整理」の直後（図解の次）", img1)]

def build_doc():
    out = ["# 【M1-7】時効の援用・更新・完成猶予：追加の図解「更新と完成猶予の違い」　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou-ch1.md`（民法編 第1章）の論点【M1-7】に追加で差し込む図解のプロンプトです。既存の図解（`prompt_infographic_M1-7.md`）は6枚のカードの並びなので、論点の題である「承認と猶予は何を変えるのか」＝更新（やり直し）と完成猶予（先延ばし）の効果の違いを、時間軸の絵で対比します。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "この図ははい／いいえの分岐ではないため、青・赤は使わず、濃紺・薄い灰色・薄い黄色のマーカーで描きます。画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
    for n, t, typ, size, fn, pos, _ in META:
        out.append(f"- 図解{n}：{t}")
        out.append(f"  - 型：{typ}　／　サイズ：{size}　／　保存名：`{fn}.png`")
        out.append(f"  - 記事の挿入位置：{pos}")
    out.append("")
    out.append("画像の使い方：ChatGPTに、下のコードブロックを貼って生成します（キャラクターは描かないので、参照画像は不要です）。サイズが1080幅で出せないときは、最も近い縦長で構いません。"
               "生成後は、プロンプトの文言と画像の文字を一字ずつ突き合わせ、簡体字・余計な文字・透過がないことを確かめてください。\n")
    for n, t, typ, size, fn, pos, fnc in META:
        out.append(f"## 図解{n}：{t}\n")
        out.append("```text\n" + fnc() + "\n```\n")
        out.append(f"保存名：`{fn}.png`\n")
    out.append("## 検品チェック\n")
    out.append("- 上段が左右2枚のカード（更新／完成猶予）で、左は項目が3行（承認・一部弁済・確定判決で権利が確定した裁判上の請求）、右は2行（訴えの取下げ・成年被後見人）か。")
    out.append("- 左の絵は空の棒が破線から再スタート（やり直し）、右の絵は終点が「6か月」の括弧で後ろへ延びている（先延ばし）か。")
    out.append("- 条番号（152条1項・147条2項・147条1項・158条1項）と「判例」の札が指定どおりか。濃紺の帯が最後に1つだけで、そのあとに何も描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-7_b.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
