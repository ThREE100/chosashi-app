"""ひっかけ診断・会話編（漫画）の共通部品。
各回のデータは dNN.py（ITEM）。肢の文・正誤は一問一答バンクから取り、ここやデータに書き写さない。
話し手は名前で呼ばない（吹き出しの向きと絵で見分ける）。個人の演習結果（回数など）は記事・画像に入れない。
"""
import json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
BANK = os.path.join(ROOT, 'tools', 'drill', 'data', 'items.json')
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TYPES = {
    'A': '数字・期間のすり替え', 'B': '主語のすり替え（誰が）', 'C': 'ないルールを足す',
    'D': '範囲のすり替え（全員・一部）', 'E': '似た手続の取り違え',
}
ERA = {'H': '平成', 'R': '令和'}
KANA = 'アイウエオ'

def bank():
    return {x['id']: x for x in json.load(open(BANK, encoding='utf-8'))['items']}

def strip_tags(s):
    s = re.sub(r'^〔[^〕]*〕', '', s)
    s = re.sub(r'【[^】]*】', '', s)
    return s.strip()

def nendo(q, label):
    m = re.match(r'([HR])(\d+)-Q(\d+)', q)
    y = int(m.group(2)); y = '元' if (m.group(1) == 'R' and y == 1) else str(y)
    return f"{ERA[m.group(1)]}{y}年度　第{int(m.group(3))}問　{label}"

TEACHER = ("THE TEACHER is the plump, round bird teacher shown in the attached sheets キャラクターシート_トリ先生_01, _02, _03 "
           "(round red glasses, blue shirt, red neckerchief, wings used as hands; sharp-tongued but full of love for beginners). "
           "He always stands on the RIGHT side of every panel.")
STUDENT = ("THE STUDENT is the young woman shown in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, "
           "hair color, outfit, and proportions from those three sheets exactly and do not invent or change any of them; do NOT use the "
           "look of any other student character. Redraw her in exactly the same art style as the bird teacher's sheets (same line weight, "
           "same flat pastel coloring, same head-to-body proportions), so the two look like characters from the same comic. She is earnest "
           "and straightforward and falls into the exam writer's traps. She always stands on the LEFT side of every panel. Her anatomy must be "
           "correct: one head, one torso, exactly one left arm and one right arm, two hands with five fingers each.")
NAMES_RULE = ("NO NAMES: never write any character's name or role word (no トリ先生, no 先生, no 生徒, no 藍子, no name tags, no captions "
              "saying who is speaking). Who is speaking is shown only by the position of the character and the tail of the speech bubble.")
STYLE = ("STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study comic, the same style as the bird teacher's "
         "character sheets; simple outlines, soft pastel colors. Color rule: check marks and YES are BLUE, crosses and NO are RED, neutral "
         "arrows and outlines are dark navy. Legal parties written as full-width letters (Ａ, Ｂ, Ｃ…) are NOT characters: draw them only as "
         "small faceless flat pictograms, all in the same light gray-blue, each with a small round tag holding its letter.")
TEXT_RULE = ("TEXT RULE: the only text in the image is the strings given below, reproduced exactly (cartoon marks ！ and ？ beside faces are "
             "decoration). Do not add any other words, numbers, or letters to backgrounds, papers, boards, or signs. Use standard Japanese "
             "(Jōyō) kanji forms only, never Simplified or Traditional Chinese variants.")

def page_prompt(it, k, page):
    lines = [f"Create one vertical Japanese study-comic page, exactly 1080x1920 pixels (9:16), with exactly {len(page['panels'])} panels "
             "stacked in one vertical column, read from top to bottom. Fully opaque background.", "",
             "CHARACTERS (critical): two recurring characters only. " + TEACHER + " " + STUDENT + " Do not add any other character.",
             "", NAMES_RULE, "", STYLE, "", TEXT_RULE, ""]
    for j, p in enumerate(page['panels'], 1):
        lines.append(f"PANEL {j}: mood: {p['mood']}")
        if p.get('fig'):
            lines.append(f"  Diagram in the middle of the panel: {p['fig']}")
            if p.get('words'):
                lines.append("  Words allowed inside this diagram (exactly these, nothing else): " + "、".join(f"「{w}」" for w in p['words']))
        for sp, t in p['talk']:
            who = 'the STUDENT (left)' if sp == 'S' else 'the TEACHER (right)'
            lines.append(f"  Speech bubble from {who}, tail pointing at {who.split(' ')[1].lower()}: 「{t}」")
        lines.append("")
    lines.append("Final check before rendering: exactly the panels listed; every string exactly as written and no other text; the student is "
                 "always on the left and the teacher always on the right; every bubble tail points at its own speaker; bubbles are read top to "
                 "bottom in the listed order within each panel; no name or role word anywhere; the student matches sheets I-01, I-02, I-03 and is "
                 "drawn in the same style as the bird teacher; she has exactly two arms and two hands; the background is fully opaque. Apply this "
                 "silently while drawing and deliver the first image as it is.")
    return "\n".join(lines)

def header_prompt(it, w, h, kind):
    t1, t2, sub = it['header']
    allowed = it.get('header_digits', '')
    return "\n".join([
        f"Create a {kind} header image for a Japanese study article, exactly {w}x{h} pixels, fully opaque background.", "",
        "TEXT (only these three strings, exactly as written): title line 1 (dark navy on a pale yellow marker band) 「" + t1 +
        "」; title line 2 (large, the emphasized word in reddish orange) 「" + t2 + "」; subtitle (in a light-blue rounded band) 「" + sub + "」. "
        + (f"The only digits allowed are {allowed}." if allowed else "Do not add any digits or Latin letters."), "",
        "CHARACTERS (critical): exactly two characters. " + TEACHER.replace('He always stands on the RIGHT side of every panel.', 'Place him at the lower right of center.')
        + " " + STUDENT.replace('She always stands on the LEFT side of every panel.', 'Place her at the lower left of center.')
        + " Poses are not fixed: choose free, natural poses that fit the topic, different each time. Keep both fully visible and their faces clear of the title.",
        "", NAMES_RULE, "",
        "STYLE: the same flat pastel style as the bird teacher's character sheets; soft study-room background with the topic scene "
        f"({it['header_scene']}) fading softly into the left and right edges, with no text in it.", "",
        "Final check: only the three strings above; standard Japanese kanji forms; exactly two characters; the student matches sheets I-01, I-02, "
        "I-03 and is drawn in the bird teacher's style; fully opaque. Deliver the first image as it is."])

def build(it, B):
    x = B[it['id']]
    src = next(s for s in x['sources'] if s['q'] == it['q'] and s['label'] == it['label'])
    stem = strip_tags(x['statement'])
    ans = '○（正しい）' if x['truth'] else '×（誤り）'
    no = f"{it['no']:02d}"
    title = f"【土地家屋調査士試験】ひっかけ診断ノート_{no}～{it['catch']}～"
    md = [f"## {title}", "", f"**出題：{nendo(it['q'], it['label'])}**", "", it['intro'], "",
          "### 本試験の肢", "", f"> {stem}", "",
          "正しいと思えば「○」、誤りだと思えば「×」、自信がなければ「？」を、紙に書いてから読み進めてください。", "", "---", ""]
    for k, page in enumerate(it['pages'], 1):
        md += [f"### {page['head']}", "", page['lead'], "", f"> 【画像挿入】漫画{k}：{page['caption']}", ""]
        if page.get('after'):
            md += [page['after'], ""]
    md += ["---", "", "### 答えと型", "", f"- 答え：**{ans}**", f"- ひっかけの型：**{it['type']}：{TYPES[it['type']]}**",
           f"- 決め手：{it['key']}", "", "### 覚えること", ""]
    md += [f"- {m}" for m in it['memo']]
    md += ["", f"根拠：{it['basis']}", "", it['outro'], ""]
    pr = [f"# ひっかけ診断ノート_{no}（{it['id']}・{it['q']}{it['label']}）の画像プロンプト", "",
          "記事：`" + f"{no}-{it['slug']}.md" + "`。ChatGPTに、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付し、"
          "「添付の6枚のうち、鳥のキャラクターが先生、女性が生徒です。名前は画像に書かないでください」と一言添えてから、下のコードブロックを1つずつ貼る。", "",
          f"漫画のファイル名：`ひっかけ診断ノート_{no}_漫画1.png` など。見出し画像：`ひっかけ診断ノート_{no}_見出し_note.png`／`_見出し_IG.png`。", ""]
    for k, page in enumerate(it['pages'], 1):
        pr += [f"## 漫画{k}：{page['caption']}", "", "```", page_prompt(it, k, page), "```", ""]
    pr += ["## 見出し画像（note用 1280×670）", "", "```", header_prompt(it, 1280, 670, 'landscape note.com'), "```", "",
           "## 見出し画像（Instagram用 1080×1440）", "", "```", header_prompt(it, 1080, 1440, 'portrait Instagram (3:4)'), "```", ""]
    return title, "\n".join(md), "\n".join(pr), stem, x['truth']
