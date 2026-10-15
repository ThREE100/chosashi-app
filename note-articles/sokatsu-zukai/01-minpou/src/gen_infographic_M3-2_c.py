# 【M3-2_c】未成年者の取消しと詐欺による取消しの比較：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-2_c.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-2_c"
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

TOPIC = "【M3-2】取消し・解除・時効と登記は、第三者がいつ現れたかで決まる"
SCOPE = "【M3-2】の「中身の整理」の直後（未成年者の取消しと詐欺による取消しの比較）"
DIFF = "既存の図解（時点カード5枚）との違い：既存の図解は、未成年者の取消しと詐欺による取消しを同じ時間軸のカードで並べ、結論だけを短い札で示します。この図解は、2つを比べて分かれる理由（第三者を保護する規定の有無）を、1枚の対比表で見せます。"

def img1():
    body = [lead("1080x1700", "This is a comparison table poster with two data columns (対比表)."), TEXTREQ, BGREQ, NOCOLOR] + \
           header("取消し前の第三者に、勝てる？", "保護する規定があるかで分かれる", "民法　第5条・第96条・第121条")
    body += ["One thin pale-yellow banner under the header with the text " + q("取り消された行為は、初めから無効とみなされる") + "."]
    body += ["--- TABLE ---",
             "Render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font. Exactly 3 columns (one row-label column and two data columns) and exactly 3 data rows, no merged cells. Draw no check mark and no cross mark, and use no blue or red anywhere in this table.",
             "Header row (dark navy cells with white text), from left to right: the first cell is empty; the second header " + q("未成年者の取消し") + "; the third header " + q("詐欺による取消し") + ". The two headers are NOT identical; copy each one exactly as given.",
             "Data row 1 (row label cell, dark navy, white text: " + q("取消しの根拠") + "): second column " + q("民法5条2項") + "; third column " + q("民法96条") + ".",
             "Data row 2 (row label cell, dark navy, white text: " + q("第三者を保護する規定") + "): second column " + q("ない") + "; third column " + q("ある（善意でかつ過失がない第三者）") + ".",
             "Data row 3 (row label cell, dark navy, white text: " + q("取消し前に買った、善意の第三者に") + "; every cell of this row has a pale yellow highlighter marker behind its text): second column " + q("善意でも、対抗できる") + "; third column " + q("善意でかつ過失がなければ、対抗できない") + ".",
             "The second-column and third-column cells of each data row have clearly different texts; the texts are NOT identical, so copy each cell exactly as given. In row 3 the two strings are similar on purpose but differ (対抗できる / 対抗できない); do not swap them.",
             "Under the table, one wide dark navy band with large white text " + q("詐欺の保護規定を、未成年者の取消しに広げない") + "."]
    return finish(body, "Confirm the table has exactly 3 columns and exactly 3 data rows, that the second header reads 未成年者の取消し and the third header reads 詐欺による取消し, that row 3 reads 善意でも、対抗できる on the left and 善意でかつ過失がなければ、対抗できない on the right and is not swapped, that only row 3 is highlighted, and that no check mark, cross mark, blue, or red appears anywhere.")

META = [(1, "取消し前の第三者に、勝てる？（未成年者の取消しと詐欺による取消しの比較）", "対比表型（2列・3行）", "1080×1700", "民法編3_2_追加_未成年者の取消しと詐欺取消しの比較", "【M3-2】の「中身の整理」の直後", img1)]

CHECKS = ["表が3列（行の見出し＋2つ）・3行で、見出しが左から『未成年者の取消し』『詐欺による取消し』の順。各セルの文字がプロンプトと一字一句同じ",
          "3行目の左右（『善意でも、対抗できる』と『善意でかつ過失がなければ、対抗できない』）が入れ替わっていない。黄色のマーカーは3行目だけ",
          "表の上に薄い黄色の細い帯、表の下に濃紺の帯がある。それ以外のまとめ・追加の文章がない",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない"]
NOTES = ["未成年者の取消し：民法5条2項（`note-articles/laws/minpou-1-soukyoku-bukken.md` で確認済み）。詐欺のような善意無過失の第三者を保護する規定がなく、取消し前の善意の転得者にも対抗できる（記事【M3-2】の中身の整理・肢の判定）",
         "詐欺による取消し：民法96条3項『善意でかつ過失がない第三者に対抗することができない』（同ファイルで原文確認済み）",
         "取り消された行為は初めから無効とみなされる：民法121条『取り消された行為は、初めから無効であったものとみなす』（同ファイルで原文確認済み）"]


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
