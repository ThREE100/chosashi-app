#!/usr/bin/env python3
"""直前予想模試（択一式 問1〜問20）の解説記事を組み立てる（標準ライブラリのみ）。

使い方: python3 note-articles/chokuzen-yosou-moshi/src/build.py
入力 : ./q01.py 〜 ./q20.py（各問のデータ。変数 Q に辞書を入れる）
出力 : ../q01-xxx.md 〜 ../q20-xxx.md（記事。生成物は手で直さず、データ側を直して再生成する）

記事の書式は note-articles/format-template.md、総論インフォグラフィック（問題全体）は
note-articles/infographic-prompt-template.md の②、見出し画像は sokatsu-zukai/03-chousashi-hou/prompt_midashi_sokatsu03.md の書式による。
画像は生成しない（プロンプトまで）。
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
sys.path.insert(0, str(HERE))

# 簡体字との字形差が大きく、注意喚起に挙げる漢字（joubun-nigate/common/infographic_parts.py と同じ集合）
RISKY = set("号録権地番建物登記所請還売買当初詐欺規対抗無過効張説解間違肢承諾譲渡押債抵援認届款占帯証代保")
RISKY |= set("験隣竹枝境線続限産遺贈検査図訂測量閉鎖区画職権筆特定通知完了表題変更合併筆分割種類構造積算階体敷区共用調士連審")


def split_paragraph(text, limit=125):
    """1段落が長いとき、文の区切り（。）で、できるだけ均等な長さの段落に分ける（1文だけの長い段落はそのまま）。"""
    if len(text) <= limit:
        return [text]
    sents = [s for s in re.split(r"(?<=。)", text) if s]
    if len(sents) < 2:
        return [text]
    n = -(-len(text) // limit)
    target = len(text) / n
    out, cur = [], ""
    for i, s in enumerate(sents):
        if cur and len(cur) + len(s) > target * 1.15 and len(out) < n - 1:
            out.append(cur)
            cur = ""
        cur += s
    if cur:
        out.append(cur)
    return out


def jp_kanji(text):
    return sorted(RISKY & set(re.findall(r"[一-鿿]", text)))


def quote_block(q):
    """問題文の引用ブロック（各行の末尾に半角スペース2つ、行間は全角スペースだけの行）。"""
    lines = [q["stem"]] + q["items"]
    out = []
    for i, ln in enumerate(lines):
        out.append("> " + ln + "  ")
        out.append(">　  ")
    out.append("> " + q["choices"])
    return "\n".join(out)


def sections(q):
    out = []
    for s in q["sections"]:
        out.append(f"### {s['mark']}：{s['head']}")
        out.append("")
        for p in s["body"]:
            for pp in split_paragraph(p):
                out.append(pp)
                out.append("")
        for pp in split_paragraph(s["tatoeba"]):
            out.append(pp)
            out.append("")
        for p in s.get("after", []):
            for pp in split_paragraph(p):
                out.append(pp)
                out.append("")
    return "\n".join(out).rstrip("\n")


def summary(q):
    return "\n".join(f"- **{m}（{j}）**　{t}" for m, j, t in q["summary"])


def infographic(q):
    g = q["info"]
    cards = g["cards"]
    colA = [c for c in cards if c["col"] == "A"]
    colB = [c for c in cards if c["col"] == "B"]
    body = []
    body.append("Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,\n"
                "clean flat-design isometric illustration style with soft pastel colors\n"
                "(blue, green, beige, gray), rounded card sections, consistent with a\n"
                "modern explainer-graphic aesthetic (icons: isometric buildings, land\n"
                "plots, stamps, torn paper labels, etc. — adapt icon set to the topic).")
    body.append("")
    body.append("GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,\n"
                "NOT a text-heavy explainer document. There is NO intro illustration and NO\n"
                "paragraph of prose anywhere on this poster — go straight from the header\n"
                "to the cards. Every card must communicate its point almost entirely\n"
                "through the illustration (icons, X marks, checkmarks, small embedded\n"
                "labels) plus one short heading and one short conclusion tag. Do NOT render\n"
                "any full-sentence explanation, legal citation, or paragraph of body text\n"
                "anywhere on the poster. If a piece of information cannot be expressed as a\n"
                "short label (a few words) or drawn as an icon, leave it out rather than\n"
                "writing it as prose.")
    body.append("")
    all_text = g["title"] + g["col_a"] + g["col_b"] + "".join(c["head"] + c["tag"] + c["illus"] for c in cards)
    kj = "・".join(jp_kanji(all_text))
    body.append("CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese\n"
                "only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use\n"
                "Simplified Chinese characters (simplified hanzi) under any circumstances,\n"
                "even if a character looks similar. Do NOT use Traditional Chinese\n"
                "characters (traditional hanzi) either, even where a traditional-hanzi\n"
                "glyph looks close to the correct Japanese kanji form — every glyph must\n"
                "match the standard Japanese Jōyō form exactly, not the Chinese\n"
                "traditional variant. Do NOT render any character that is not standard\n"
                "Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —\n"
                "no Chinese-only characters, no Korean Hangul, no other non-Japanese\n"
                "script, and no stray or decorative glyphs of any kind, even as small\n"
                "background or texture elements. Every kanji must match standard Japanese\n"
                "orthography exactly as written below, stroke-for-stroke. Reproduce the\n"
                "exact text strings given below verbatim — do not paraphrase, translate,\n"
                "summarize, or substitute any characters. Pay special attention to the\n"
                f"kanji {kj} — these\n"
                "must be rendered in their standard Japanese forms, never as Simplified\n"
                "Chinese variants.")
    body.append("")
    body.append("BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque\n"
                "from edge to edge. Do NOT generate a transparent or alpha-channel\n"
                "background under any circumstances, even if the output file format\n"
                "supports transparency. Fill the full canvas — including every corner and\n"
                "margin outside the cards/columns — with a solid or illustrated opaque\n"
                "background (the pale beige/gray tone used elsewhere in this style is a\n"
                "good default). There must be no checkerboard pattern, no partially\n"
                "transparent area, and no unpainted canvas edge anywhere in the final\n"
                "image.")
    body.append("")
    body.append("--- HEADER ---\nTitle (large, bold, 1行):\n" + g["title"] + "\n\nSubtitle (smaller, centered, 1行):\n"
                + f"直前予想模試 第{q['no']}問" + "\n\n（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の\nブロックは置かない。）")
    n = 0
    for col, label, color, cs in (("A", g["col_a"], "green", colA), ("B", g["col_b"], "blue", colB)):
        if not cs:
            continue
        body.append("")
        body.append(f"--- COLUMN {col} HEADER (pill-shaped badge, color: {color}) ---\n{label}")
        for c in cs:
            n += 1
            body.append("")
            body.append(f"--- COLUMN {col}, CARD {n} ---\n"
                        f"Badge: a filled {color} circle containing the number {n}.\n"
                        "Heading (bold, ONE line, ~20 characters or fewer):\n"
                        f"{c['head']}\n"
                        f"Illustration: {c['illus']}\n"
                        f"Conclusion tag ({color} banner below the illustration, 5-15 characters):\n"
                        f"{c['tag']}")
    body.append("")
    cnt = f"{len(colA)} cards under 「{g['col_a']}」" + (f" and {len(colB)} cards under 「{g['col_b']}」" if colB else "")
    body.append("--- FOOTER ---\n\n"
                "Final check before rendering: scan every kanji glyph and confirm it is\n"
                "standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese. Also scan the entire canvas for any character that is not standard Japanese hiragana, katakana, or Jōyō kanji — including any Chinese-only character, Korean Hangul, other non-Japanese script, or stray decorative glyph — and remove or redraw it so that only standard Japanese text appears anywhere in the image. If any character\n"
                "renders as a Simplified or Traditional Chinese variant, redraw that character in the\n"
                f"correct Japanese form. Confirm the number of cards equals {len(cards)} exactly ({cnt}), with no duplicated or missing cards, that badge\n"
                f"numbers run 1-{len(cards)} continuously across the columns without resetting,\n"
                "confirm there is no intro illustration or paragraph block between the\n"
                "header and the cards, and confirm that no card contains a full sentence\n"
                "of explanatory prose — every card's takeaway must read as a short heading\n"
                "+ a short conclusion tag, at a glance. Confirm no card states a false\n"
                "(\"誤\"と判定された) rule — every card must show the legally correct rule\n"
                "only. Confirm nothing is rendered below the last card (no summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid of all 肢, and no additional text block of any kind — the image ends immediately after the last card). Confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.")
    return "\n".join(body)


def midashi(q):
    m = q["midashi"]
    kj = "、".join(jp_kanji(m["l1"] + m["l2"] + m["sub"]))
    l2 = m["l2"]
    hi = m["hi"]
    assert hi in l2, (q["no"], "見出しの強調語が2行目にない")
    return f"""Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
{m['l1']}
Line 2 is larger; the phrase {hi} is red-orange and the rest is dark navy:
{l2}
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
{m['sub']}
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: {m['left']}
Right side: {m['right']}

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji {kj}; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is."""


def render(q):
    no = q["no"]
    kaidai = q.get("kaidai")
    mark = "（改）" if kaidai else ""
    L = []
    L.append(f"## 【土地家屋調査士受験生向け】直前予想模試 第{no}問{mark}〜{q['catch']}〜")
    L.append("")
    L.append(f"**出題年度：直前予想模試　択一式　第{no}問{mark}**")
    L.append("")
    L.append(quote_block(q))
    L.append("")
    L.append("---")
    L.append("")
    for pp in split_paragraph(q["intro"]):
        L.append(pp)
        L.append("")
    if q.get("intro_list"):
        for it in q["intro_list"]:
            L.append("- " + it)
        L.append("")
    L.append(sections(q))
    L.append("")
    L.append("---")
    L.append("")
    L.append("### まとめ")
    L.append("")
    L.append(summary(q))
    L.append("")
    for pp in split_paragraph(q["closing"]):
        L.append(pp)
        L.append("")
    L.append(f"**正解：{q['answer']}**")
    L.append("")
    L.append("---")
    L.append("")
    if kaidai:
        L.append(kaidai)
        L.append("")
        L.append("---")
        L.append("")
    L.append("**このまま使える点／使う前に確認したい点**")
    L.append("")
    std = [
        "文章としてはこのままnoteに貼り付けて投稿できる内容です（問題文の引用部分の取り扱いは、次の項目を確認してください）。",
        f"本問は市販教材の直前予想模試であり、法務省が公表した試験問題ではありません。問題文・正解番号（{q['answer'].split('（')[1].rstrip('）')}）は、ユーザーから提供された資料（問題・採点基準・解答解説）で確認しました。公式の正答資料はありません。問題文を公開記事に全文引用する場合は、出題元の利用条件を事前に確認してください。",
    ]
    for b in std + q["kakunin"]:
        L.append("- " + b)
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 見出し画像用フレーズ")
    L.append("")
    for p in q["phrases"]:
        L.append("- " + p)
    L.append("")
    L.append("---")
    L.append("")
    L.append("## インフォグラフィック プロンプト（問題全体）")
    L.append("")
    L.append(q["info"]["lead"])
    L.append("")
    L.append("```")
    L.append(infographic(q))
    L.append("```")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 見出し画像 プロンプト（note見出し画像・1280×670px）")
    L.append("")
    L.append("ChatGPTに、キャラクターの参照画像（トリ先生と藍子の基準画像。リポジトリ直下の`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付し、"
             "どちらがトリ先生でどちらが藍子かを一言添えて、下のコードブロックを貼ります。画像は生成していません。")
    L.append("")
    m = q["midashi"]
    L.append(f"画像の文言（正本）：1行目「{m['l1']}」、2行目「{m['l2']}」（「{m['hi']}」を赤みのあるオレンジ）、サブタイトル「{m['sub']}」。"
             "結論は書かず、問いかけにしています。画像の中の数字は漢数字にしています（見出し画像は数字・英字を入れない決まりのため）。")
    L.append("")
    L.append("```text")
    L.append(midashi(q))
    L.append("```")
    L.append("")
    return "\n".join(L)


def main():
    made = []
    for n in range(1, 21):
        modname = f"q{n:02d}"
        if not (HERE / f"{modname}.py").exists():
            continue
        mod = importlib.import_module(modname)
        q = mod.Q
        assert q["no"] == n
        path = OUT / f"q{n:02d}-{q['slug']}.md"
        path.write_text(render(q), encoding="utf-8")
        made.append(path.name)
    print("generated:", len(made))
    for m in made:
        print(" ", m)


if __name__ == "__main__":
    main()
