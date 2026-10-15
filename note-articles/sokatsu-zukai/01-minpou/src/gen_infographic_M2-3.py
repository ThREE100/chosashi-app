# 民法編・総合記事【M2-3】占有回収の訴えを起こせるのは誰か：図解インフォグラフィック1枚のプロンプトを組み立てる（標準ライブラリのみ。共通部品は note-articles/joubun-nigate/common/infographic_parts.py）
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

def header(t1, t2, sub):
    return ["--- HEADER ---", "Title (large, bold, 2 lines):", q(t1), q(t2), "Subtitle (smaller, centered, 1 line):", q(sub)]

def img1():
    cards = [
        ("占有を奪われたとき", "A flat house icon with a person pictogram tagged " + q("占有者") + " standing outside the closed door, and two small document sheets beside the door labeled " + q("物の返還") + " and " + q("損害の賠償") + ".", "占有回収の訴え（民法200条）"),
        ("訴えを起こせる人", "Two person pictograms side by side with dark navy name tags " + q("占有者") + " and " + q("他人のために占有をする者") + ", both holding a small document sheet labeled " + q("占有の訴え") + ".", "どちらも提起できる（民法197条）"),
        ("預かった物を管理する人", "A flat parking lot icon labeled " + q("預かった駐車場") + " with a small car icon parked on it and a person pictogram tagged " + q("管理会社") + " standing beside it.", "管理会社も提起できる"),
        ("転貸人は間接占有者", "Two person pictograms stacked in a column, the upper one tagged " + q("転貸人") + " and the lower one tagged " + q("転借人") + ", joined by a plain dark navy line labeled " + q("代理占有（民法181条）") + ", and a third small person pictogram at the side tagged " + q("奪った人") + ".", "転貸人も提起できる"),
        ("代表者には占有が2つ", "One person pictogram tagged " + q("代表者") + " holding two small tags, one on each side: " + q("機関としての占有") + " and " + q("個人としての占有") + ".", "個人としても提起できる"),
    ]
    body = [lead("1080x2300", "This is a quick-reference poster with five numbered cards in one column; it is NOT a text-heavy document."),
            "GLANCEABLE-POSTER REQUIREMENT (critical): There is no intro illustration and no paragraph of prose anywhere on this poster; go straight from the header to the cards. Every card communicates its point through the illustration plus one short heading and one short conclusion tag. Do NOT render any full-sentence explanation, legal citation, or paragraph of body text.",
            TEXTREQ, BGREQ, COLOR] + header("占有回収の訴えを起こせる人", "見る基準は、法律上の占有者", "民法 第181条・第197条・第200条")
    for i, (h, ill, tag) in enumerate(cards, 1):
        body += [f"--- CARD {i} ---", f"Badge: a filled dark navy circle containing the number {i} (numbers run 1 to 5 in order).",
                 "Heading (bold, ONE line):", q(h), "Illustration: " + ill,
                 "Conclusion tag (a short pale-yellow banner directly below the illustration, a keyword phrase, not a sentence):", q(tag)]
    txt = "\n".join(body)
    return txt + "\n--- FOOTER ---\n" + final(kanji_in(txt), "Confirm the number of cards equals 5 exactly, numbered 1 to 5 in order, with no duplicated or missing cards, confirm there is no intro illustration or paragraph block between the header and the cards, and confirm that no card contains a full sentence of explanatory prose.")

META = [
    (1, "占有回収の訴えを起こせる人（見る基準は法律上の占有者）", "カードポスター型（俯瞰）", "1080×2300", "図解_M2-3_占有回収の訴えを起こせる人", "【M2-3】の「中身の整理」の直後", img1),
]

def build_doc():
    out = ["# 【M2-3】占有回収の訴えを起こせるのは誰か　図解インフォグラフィック プロンプト（1枚）\n"]
    out.append("民法編・総合記事（`note-articles/column/sokatsu-01-minpou.md`）の論点【M2-3】に差し込む図解のプロンプトです。画像は生成していません（ChatGPTなどで手動生成）。"
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
    out += ["- カードがちょうど5枚で、1〜5の番号が順に付いているか。",
            "- 見出し・タグの文字が、プロンプトの文言と一字ずつ一致しているか（簡体字・余計な文字がないか）。",
            "- 「民法200条」「民法197条」「民法181条」の条番号が崩れていないか。",
            "- 青・赤が使われていないか（この図に、はい／いいえの分岐はない）。",
            "- 最後のカードの下に、まとめのパネル・トロフィーなどが描き足されていないか。",
            "- 背景が不透明か（透過・チェッカーボードがないか）。"]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    doc = build_doc()
    out = _here.parent.parent / "infographic" / "prompt_infographic_M2-3.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf8")
    print(out, len(doc))
