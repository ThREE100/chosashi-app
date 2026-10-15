# 【M1-4】錯誤・詐欺による取消し：だれが取り消せて、いつ取り消せないのか：図解インフォグラフィック1枚のプロンプトを組み立てる（共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
# 実行: python3 gen_infographic_M1-4.py
import sys, pathlib
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[3] / "joubun-nigate" / "common"))
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    cards = [
        ("取り消せるのは、だれ？",
         "Three faceless person pictograms in one row inside ONE rounded frame, with the dark navy name tags " + q("表意者") + ", " + q("代理人") + " and " + q("承継人") + ", and outside the frame at the right one more person pictogram drawn with a thin dotted outline and the name tag " + q("相手方") + ".",
         "相手方は取り消せない"),
        ("表意者に重過失があるときは？",
         "A document sheet labeled " + q("錯誤") + " with a small dark navy tag " + q("表意者に重大な過失") + " on its corner, and to its right two small rounded cards stacked top and bottom under one small gray tag " + q("例外") + ": the top card " + q("相手方が知っていた・重過失で知らなかった") + " and the bottom card " + q("相手方も同じ錯誤だった") + ".",
         "原則は不可。例外が2つ"),
        ("詐欺の取消しは？",
         "A contract document sheet labeled " + q("詐欺") + " with a rubber stamp icon labeled " + q("取消し") + " pressed on it, and a faceless person pictogram with the name tag " + q("当事者") + " beside it.",
         "取消し自体はできる"),
        ("第三者には対抗できる？",
         "A faceless person pictogram with the name tag " + q("第三者") + " holding a shield labeled " + q("善意でかつ過失がない") + ", with two small gray tags " + q("錯誤") + " and " + q("詐欺") + " on the shield's upper edge, and a small registry ledger icon labeled " + q("詐欺：登記は要らない（判例）") + " beside the person.",
         "対抗できない"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with four numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR,
            "Draw no check mark and no cross mark anywhere in this poster, and use no blue or red; use dark navy outlines, badges and headings only, and the pale yellow banner only for the conclusion tags."] + \
           header("錯誤・詐欺の取消し", "4つの点で整理する", "民法 総則（意思表示）")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 4 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 4 exactly, numbered 1 to 4 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, confirm that no card contains a full sentence of explanatory prose, and confirm that no check mark, cross mark, blue or red appears anywhere.")

META = [(1, "錯誤・詐欺の取消し：4つの点で整理する", "カードポスター型", "1080×2300", "図解1_錯誤・詐欺の取消しを4つの点で整理する", "【M1-4】の「中身の整理」の直後", img1)]

def build_doc():
    out = ["# 【M1-4】錯誤・詐欺による取消し：だれが取り消せて、いつ取り消せないのか　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("総合記事 `note-articles/column/sokatsu-01-minpou.md`（民法編）の論点【M1-4】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
               "作成のルールは `note-articles/infographic-prompt-template.md`（文字化け・簡体字対策、背景の不透明化、アウトロブロック禁止）に従いました。"
               "画像の中には、図の番号・問題番号・年度・演習結果を入れません（カードの通し番号1〜4は図の部品です）。キャラクターは描きません。\n")
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
    out.append("- カードがちょうど4枚で、通し番号1〜4が順に並び、見出し・結論タグ（相手方は取り消せない／原則は不可。例外が2つ／取消し自体はできる／対抗できない）が指定どおりか。")
    out.append("- カード1の「相手方」だけが点線の輪郭か。カード2の例外が2つ（相手方が知っていた・重過失で知らなかった／相手方も同じ錯誤だった）か。")
    out.append("- 導入のイラスト・文章の段落・まとめの帯が、カードの前後に描かれていないか。")
    out.append("- 青・赤・チェック・×が一つもないか。簡体字・余計な文字・透過・図番がないか。")
    return "\n".join(out)

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parents[1] / "infographic" / "prompt_infographic_M1-4.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
