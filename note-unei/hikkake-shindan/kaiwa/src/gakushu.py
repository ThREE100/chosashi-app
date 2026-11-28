"""学習まんが版（コマ割りが解説の進行で変わる）の共通部品。
データは gNN.py（ITEM）。1ページ＝1枚の画像（縦 1024×1536）。ページ数・コマ数は話の必要に合わせて決める。
肢の文・正誤は一問一答バンクから取る。話し手は名前で呼ばず、絵と吹き出しのしっぽで見分ける。
既存の作品の画風・キャラクター・道具はまねない（構成の型だけを学習まんがから借りる）。
"""
import os
from common import bank, strip_tags, nendo, TYPES, OUT

W, H = 1024, 1536
TEACHER = ("THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, "
           "blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.")
STUDENT = ("THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, "
           "outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly "
           "the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look "
           "like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big "
           "(confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, "
           "two hands with five fingers each.")

def _bubble(sp, t):
    who = 'STUDENT' if sp == 'S' else 'TEACHER'
    return f"      - speech bubble from the {who} (tail points at the {who.lower()}): 「{t}」"

def page_prompt(it, k, page):
    n = len(it['pages'])
    L = [f"Draw page {k} of {n} of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly {W}x{H} "
         "pixels (2:3 portrait), full color, fully opaque background.", "",
         "## 1. Art style and characters",
         "Clean, warm, friendly flat digital illustration in the same style as the bird teacher's character sheets: simple outlines, soft pastel "
         "colors, expressive manga reactions (sweat drops, sparkle eyes, speed lines) used lightly. Do not imitate any existing manga series, "
         "its characters, gadgets, or logos.",
         TEACHER, STUDENT,
         "Only these two characters appear. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ) are NOT characters: draw them as small "
         "faceless flat pictograms in one light gray-blue, each with a small round tag holding its letter. They never speak in speech bubbles.",
         "NO NAMES: never write any character's name or role word anywhere (no トリ先生, no 先生, no 生徒, no 藍子, no name tags). Who speaks is "
         "shown only by the character and the tail of the bubble.", "",
         "## 2. Page layout",
         "Reading order: left to right, top to bottom (horizontal Japanese text). Panel borders are dark navy, with clear white gutters. "
         + page['layout'], ""]
    L.append("## 3. Panels")
    for j, p in enumerate(page['panels'], 1):
        L.append(f"PANEL {j} ({p['size']}): {p['art']}")
        if p.get('chars'):
            L.append(f"      characters: {p['chars']}")
        if p.get('narration'):
            L.append(f"      narration box (rectangular, cream fill, dark navy text, top-left corner of the panel): 「{p['narration']}」")
        for sp, t in p.get('talk', []):
            L.append(_bubble(sp, t))
        if p.get('words'):
            L.append("      words inside the drawing (exactly these, nothing else): " + "、".join(f"「{w}」" for w in p['words']))
    L += ["", "## 4. Text rules",
          "The only text on the page is the strings in section 3, each reproduced exactly, character for character, in clear horizontal "
          "Japanese lettering large enough to read on a smartphone. No other words, numbers, letters, sound effects written as text, or "
          "signs. Cartoon marks ！ and ？ beside faces are decoration. Standard Japanese (Jōyō) kanji forms only, never Simplified or Traditional "
          "Chinese variants. Bubbles in one panel are read top to bottom in the listed order. Color meaning: check marks and correct = BLUE, "
          "crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.", "",
          "## 5. Quality check (apply silently while drawing)",
          f"Exactly {len(page['panels'])} panels in the described layout; every string exactly as written and nothing else; no name or role word; "
          "every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; "
          "she has exactly two arms and two hands; pictograms have no faces; fully opaque. Deliver the first image as it is."]
    return "\n".join(L)

def header_prompt(it, w, h, kind):
    t1, t2, sub = it['header']
    return "\n".join([
        f"Create a {kind} header image for a Japanese educational comic article, exactly {w}x{h} pixels, fully opaque.", "",
        f"TEXT (only these three strings, exactly): line 1 on a pale yellow marker band 「{t1}」; line 2 large, the key word in reddish orange "
        f"「{t2}」; subtitle in a light-blue rounded band 「{sub}」. No other words, digits, or Latin letters.", "",
        "CHARACTERS: exactly two. " + TEACHER + " Place him lower right of center. " + STUDENT + " Place her lower left of center. "
        "Free, natural poses that fit the topic, different each time; both fully visible, faces clear of the title. "
        "No names or role words anywhere.", "",
        f"STYLE: the bird teacher's flat pastel style; the topic scene ({it['header_scene']}) fades softly into the left and right edges with "
        "no text in it. Do not imitate any existing manga series.", "",
        "Final check: only the three strings; standard Japanese kanji; exactly two characters; fully opaque. Deliver the first image as it is."])

def build(it, B):
    x = B[it['id']]
    stem = strip_tags(x['statement'])
    ans = '○（正しい）' if x['truth'] else '×（誤り）'
    no = f"{it['no']:02d}"
    title = f"【土地家屋調査士試験】ひっかけ診断ノート_{no}～{it['catch']}～"
    md = [f"## {title}", "", f"**出題：{nendo(it['q'], it['label'])}**", "", it['intro'], "",
          "### 本試験の肢", "", f"> {stem}", "",
          "正しいと思えば「○」、誤りだと思えば「×」、自信がなければ「？」を、紙に書いてから漫画を読んでください。", "", "---", ""]
    for k, page in enumerate(it['pages'], 1):
        md += [f"> 【画像挿入】{k}ページ目：{page['caption']}", ""]
    md += ["---", "", "### 答えと型（文字で確かめたい人へ）", "", f"- 答え：**{ans}**",
           f"- ひっかけの型：**{it['type']}：{TYPES[it['type']]}**", f"- 決め手：{it['key']}", ""]
    md += [f"- {m}" for m in it['memo']]
    md += ["", f"根拠：{it['basis']}", "", it['outro'], ""]
    pr = [f"# ひっかけ診断ノート_{no}（{it['id']}・{it['q']}{it['label']}）学習まんが版の画像プロンプト", "",
          "記事：`" + f"{no}-{it['slug']}.md" + f"`。全{len(it['pages'])}ページ、1ページ＝1枚（{W}×{H}）。",
          "ChatGPTでは、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付し、「鳥が先生、女性が生徒です。名前は画像に書かないでください」と添えてから、1ページずつ貼る。2ページ目からは同じチャットで続ける。", "",
          f"ファイル名：`ひっかけ診断ノート_{no}_p01.png`〜`_p{len(it['pages']):02d}.png`、見出し画像 `ひっかけ診断ノート_{no}_見出し_note.png`／`_見出し_IG.png`。", ""]
    for k, page in enumerate(it['pages'], 1):
        pr += [f"## {k}ページ目：{page['caption']}", "", f"ねらい：{page['aim']}", "", "```", page_prompt(it, k, page), "```", ""]
    pr += ["## 見出し画像（note用 1280×670）", "", "```", header_prompt(it, 1280, 670, 'landscape note.com'), "```", "",
           "## 見出し画像（Instagram用 1080×1440）", "", "```", header_prompt(it, 1080, 1440, 'portrait Instagram (3:4)'), "```", ""]
    return title, "\n".join(md), "\n".join(pr), stem, x['truth']
