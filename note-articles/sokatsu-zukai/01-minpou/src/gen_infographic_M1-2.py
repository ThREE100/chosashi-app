# 【M1-2】制限行為能力者：開始の審判・詐術・追認のルールは何か：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

ROWSTYLE = ("Each row is a rounded white mini-card with a dark navy outline: a left part with the situation text and a right part with the result text, separated by a thin vertical dark navy divider, with no arrow. "
            "Draw no check mark and no cross mark, and use no blue or red anywhere in this poster.")

def card(i, heading, icon, rows, tag, extra=""):
    out = [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 3 in order).",
           "Heading (bold, ONE line):", q(heading), "Small icon beside the heading: " + icon, ROWSTYLE + extra]
    for k, (l, r, small) in enumerate(rows, 1):
        s = f" Under the result text, a small gray tag {q(small)}." if small else ""
        out.append(f"Row {k}: left part {q(l)}; right part {q(r)}.{s}")
    out += ["Conclusion tag (a short pale-yellow banner directly below the rows, a keyword phrase, not a sentence):", q(tag)]
    return out

def img1():
    body = [lead("1080x2400", "This is a quick-reference poster with three numbered cards in one column; every card holds short rows, and it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card consists of one heading, a few short rows, and one short conclusion tag. Do NOT render any full-sentence explanation or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("制限行為能力者の三つのルール", "開始の審判・詐術・追認", "民法 総則（制限行為能力者）")
    body += card(1, "本人以外の請求で、同意がいるのは？", "A court gavel and a petition paper.",
                 [("後見開始", "同意は不要", "7条"), ("保佐開始", "同意は不要", "11条"), ("補助開始", "同意が必要", "15条2項")],
                 "同意がいるのは補助開始だけ",
                 " In row 3 the right part " + q("同意が必要") + " has a pale yellow highlighter marker. Rows 1 and 2 have the same right-part text on purpose; draw the same string in both.")
    body += card(2, "詐術を使うと、取り消せない？", "A small mask and a pair of eyes.",
                 [("相手方が行為能力者だと信じた", "取り消せない", "21条"), ("相手方が未成年者と知っていた", "取り消せる", "信じていないので21条は働かない")],
                 "相手方が信じたときだけ",
                 " In row 2 the left part " + q("相手方が未成年者と知っていた") + " has a pale yellow highlighter marker.")
    body += card(3, "追認できるのは、いつ？", "A signed paper sheet and a calendar.",
                 [("原則", "原因の状況が消え、取消権を知った後", "124条1項"), ("同意を得た追認（成年被後見人を除く）", "状況が消えた後でなくてよい", "124条2項2号")],
                 "同意を得れば、成年前でも追認できる",
                 " Row 2 is the exception row: draw the left part " + q("同意を得た追認（成年被後見人を除く）") + " on two lines.")
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 3 exactly, numbered 1 to 3 in order, with no duplicated or missing cards, that card 1 has exactly 3 rows, card 2 has exactly 2 rows and card 3 has exactly 2 rows, that the right parts of rows 1 and 2 in card 1 are the same string, that no check mark, cross mark, blue or red appears anywhere, that there is no intro illustration or paragraph block between the header and the cards, and that no card contains a full sentence of explanatory prose.")

META = [(1, "制限行為能力者の三つのルール（開始の審判・詐術・追認）", "カードポスター型（3枚のカード）", "1080×2400", "図解1_制限行為能力者の三つのルール", "【M1-2】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M1-2】制限行為能力者：開始の審判・詐術・追認のルールは何か　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-2】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・演習結果を入れません。キャラクターは描きません。\n")
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
    out.append("- カードは3枚で、番号が1〜3の順か。カード1は3行、カード2・カード3は各2行か。")
    out.append("- 条番号（7条・11条・15条2項・21条・124条1項・124条2項2号）が指定どおりか。")
    out.append("- 黄色のマーカーが、「同意が必要」と「相手方が未成年者と知っていた」の2か所だけか。青・赤・チェック・×が一つもないか。")
    out.append("- 最後のカードのあとに、まとめのパネルや文章ブロックが描かれていないか。")
    out.append("- 簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-2.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
