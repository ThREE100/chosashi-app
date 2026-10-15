# 【M3-3_b】中間省略登記の合意と債権者の代位：追加の図解インフォグラフィックのプロンプトを組み立てる（第3章の追加分）
# 共通部品は note-articles/joubun-nigate/common/infographic_parts.py（標準ライブラリのみ）。
# 生成物（infographic/prompt_infographic_M3-3_b.md）は手で直さず、ここを直して再生成する。
import pathlib, sys
_here = pathlib.Path(__file__).resolve()
for _p in _here.parents:
    if (_p / "joubun-nigate" / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "joubun-nigate" / "common")); break
    if (_p / "common" / "infographic_parts.py").exists():
        sys.path.insert(0, str(_p / "common")); break
from infographic_parts import q, kanji_in, lead, TEXTREQ, BGREQ, COLOR, final

KEY = "M3-3_b"
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
SCOPE = "【M3-3】の「たとえば」の直後（中間省略登記の合意と債権者の代位の関係図）"
DIFF = "既存の図解（三つの場面の対比表）との違い：既存の図解は、相続人・債権者・他人物売買の3場面を表で見比べる早見表です。この図解は、とくに誤りの多い中間省略登記の合意と債権者の代位について、登記を移す経路と、合意のあとも残るものを、登場人物の図で見せます。"

def img1():
    body = [lead("1080x2400", "This is a poster of two relationship-diagram cards and one three-step chain (関係図); it is NOT a text-heavy document."), GLANCE, TEXTREQ, BGREQ, NOCOLOR] + \
           header("中間省略の合意をしても", "売主の登記請求権は残る", "民法　第423条")
    body += ["--- CARD A (a wide rounded card, pale gray fill, dark navy outline) ---",
             "Card heading (dark navy, bold, ONE line): " + q("登記の移し方"),
             "Lane 1: a small light-gray tag at the left " + q("ふつう") + ", then three " + PERSON + " in a row from left to right: " + q("元の所有者") + ", " + q("売主") + " and " + q("買主") + ". Two dark navy arrows, one from 元の所有者 to 売主 and one from 売主 to 買主, each labeled " + q("移転登記") + " (both arrows mean the same thing).",
             "Lane 2: a small light-gray tag at the left " + q("中間省略") + ", then the same three pictograms in the same order, but the pictogram 売主 is drawn with a thin dotted outline. One long dark navy arch-shaped arrow goes from 元の所有者 over the dotted 売主 directly to 買主, labeled " + q("直接移す合意") + ".",
             "--- CARD B (a wide rounded card, pale gray fill, dark navy outline) ---",
             "Card heading (dark navy, bold, ONE line): " + q("合意のあとも、残るもの"),
             "Three " + PERSON + " in a row from left to right: " + q("売主の債権者") + ", " + q("売主") + " and " + q("元の所有者") + ". Under 売主, a document sheet drawn with a solid outline labeled " + q("売主の登記請求権") + " with a small light-gray tag " + q("消えない") + " beside it. "
             "One dark navy arch-shaped arrow goes from 売主の債権者 over 売主 to 元の所有者, labeled " + q("代位して請求") + ".",
             "--- THREE-STEP CHAIN (three small rounded boxes stacked top to bottom on the center line, joined by short straight dark navy arrows pointing down, no labels on the arrows) ---",
             "Box 1 with a dark navy circle containing 1: " + q("合意は、登記を移す経路の取決め") + ".",
             "Box 2 with a dark navy circle containing 2: " + q("売主の登記請求権は消えない") + ".",
             "Box 3 with a dark navy circle containing 3 (the text has a pale yellow highlighter marker): " + q("債権者は、代位して請求できる") + ".",
             "At the bottom, one small light-gray tag: " + q("中間省略登記の扱いは、判例の整理による") + ".",
             "Counts: 2 cards and 3 chain boxes; card A has 6 pictograms (3 in lane 1 and 3 in lane 2, one of them dotted) and card B has 3 pictograms. The three chain boxes have different texts."]
    return finish(body, "Confirm there are exactly 2 cards and 3 numbered chain boxes, that in card A the lane 1 has two arrows labeled 移転登記 and the lane 2 has one long arch arrow labeled 直接移す合意 over a dotted 売主, that in card B the arch arrow labeled 代位して請求 goes from 売主の債権者 to 元の所有者, that the document sheet 売主の登記請求権 has a solid outline, that no check mark, cross mark, blue, or red appears anywhere, and that all person names are role names with no Latin letters.")

META = [(1, "中間省略の合意をしても、売主の登記請求権は残る（登記の経路と債権者の代位）", "関係図ポスター型（カード2枚＋3ステップ）", "1080×2400", "民法編3_3_追加_中間省略登記と債権者の代位", "【M3-3】の「たとえば」の直後", img1)]

CHECKS = ["カードAに人型6体（ふつうの経路3体、中間省略3体のうち売主が点線）、カードBに人型3体。矢印は濃紺で、ふつうの経路に『移転登記』2本、中間省略に『直接移す合意』の弧の矢印1本、カードBに『代位して請求』の弧の矢印1本",
          "『売主の登記請求権』の書類が実線で、『消えない』の札がある（点線ではない）。点線なのは中間省略の売主の人型だけ",
          "下の3つの番号つきの箱が『合意は、登記を移す経路の取決め』『売主の登記請求権は消えない』『債権者は、代位して請求できる』の順。3つ目だけ黄色のマーカー",
          "簡体字・繁体字・英字・余計な文字がない。背景が不透明。✓・✕・青・赤がどこにもない。人型の名札が役割名（英字なし）"]
NOTES = ["中間省略登記：記事【M3-3】の中身の整理のとおり、合意があってもBの登記請求権は消えないと整理される。記事は個別の判例の番号までは確認できていないと注記しているため、図でも判例番号は載せず、小さな札『中間省略登記の扱いは、判例の整理による』を付けた（条文に直接の定めはない）",
         "債権者の代位：民法423条1項『債権者は、自己の債権を保全するため必要があるときは、債務者に属する権利を行使することができる』（`note-articles/laws/minpou-2-saiken.md` で原文確認済み）。売主の債権者が、売主に代わって元の所有者に売主への移転登記を請求する、という構図は既存の4コマ（`4koma/prompt_4koma_M3-3_D0722-D0723-D1209.md`）と同じ",
         "サブタイトルは民法423条のみ（図の中心が代位のため）。相続人と他人物売買は、既存の対比表と次の図解（他人物売買の時間軸）で扱う"]


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
