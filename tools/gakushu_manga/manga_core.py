"""学習まんが（解説の進み方でコマ割りが変わる漫画）の共通部品。ひっかけ診断ノートで検証済みの書き方
（note-unei/hikkake-shindan/kaiwa/src/gakushu.py、2026-11-28 ユーザー評価「とても良好」）を、一枚まとめ・毎日ドリル（朝・夜）でも
使えるように切り出したもの。kaiwa/ のファイルは書き換えない（向こうはそのまま。こちらは図の差し込み枠などを足した版）。

台本の形（各仕組みの src/<ID>.py が作る）：
  page = dict(caption, aim, layout, panels=[panel, …], nomark=True?)
nomark=True のページには、○×・チェック・はんこなどの正誤の印を一切描かせない（毎日ドリル朝の肢ごとのページ。2026-11-28 ユーザー指示）。
  panel = dict(size, art, chars?, narration?, talk=[('S'|'T', 文), …]?, words=[…]?, fig=dict(name, rect=(x, y, w, h))?)
fig は「Claude が作った図の画像をそのまま置く枠」。rect はページ（1024×1536）の中の位置と大きさ（px）。
"""
W, H = 1024, 1536

TEACHER = ("THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, "
           "blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.")
STUDENT = ("THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, "
           "outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly "
           "the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look "
           "like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big "
           "(confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, "
           "two hands with five fingers each.")
NOMARK = ("NO JUDGEMENT MARKS ON THIS PAGE (critical): do not draw any circle mark ○, cross mark ×, check mark, tick, X, stamp, seal, "
          "thumbs-up icon, or red/blue judgement symbol anywhere, not even as decoration; whether an option is right or wrong is shown only on "
          "the last page. Color meaning: emphasis = yellow highlighter, neutral = dark navy, the key word may be reddish orange.")
SHEETS_NOTE = "ChatGPT・Codexには、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付する（シートはリポジトリにない）。"


def texts_of(panel):
    """コマに描かせる文字（吹き出し・ナレーション・絵の中の語）。図の画像の中の文字は含まない。"""
    return [t for _, t in panel.get('talk', [])] + list(panel.get('words', [])) + ([panel['narration']] if panel.get('narration') else [])


def figs_of(pages):
    """[(ページ番号, コマ番号, fig)]"""
    return [(k, j, p['fig']) for k, pg in enumerate(pages, 1) for j, p in enumerate(pg['panels'], 1) if p.get('fig')]


def _bubble(sp, t):
    who = 'STUDENT' if sp == 'S' else 'TEACHER'
    return f"      - speech bubble from the {who} (tail points at the {who.lower()}): 「{t}」"


def _fig_lines(fig, url):
    x, y, w, h = fig['rect']
    return [f"      FIGURE SLOT (critical): the attached image 「{fig['name']}.png」" + (f" (the same file is at {url})" if url else "") +
            f" is an exact figure made in advance. Inside this panel, keep a white rectangle exactly {w}x{h} pixels with its top-left corner at "
            f"x={x}, y={y} of the page, and place that image into the rectangle exactly as it is, scaled to fit the rectangle. Do NOT redraw, "
            "retrace, simplify, translate, recolor, crop, flip, or rotate it; keep every line, dot, letter, and number in it unchanged; add "
            "nothing inside the rectangle. Characters, bubbles, and narration boxes must stay outside the rectangle."]


def page_prompt(pages, k, page, url_of=None):
    """1ページ分のプロンプト（英語・5段）。url_of(fig) → 図のURL（なければ None）。"""
    n = len(pages)
    figs = [p['fig'] for p in page['panels'] if p.get('fig')]
    L = [f"Draw page {k} of {n} of a Japanese educational comic (gakushu manga) for adult exam learners. One page only, exactly {W}x{H} "
         "pixels (2:3 portrait), full color, fully opaque background.", ""]
    if figs:
        L += ["ATTACHED FIGURE(S) FOR THIS PAGE: " + "、".join(f"「{f['name']}.png」" for f in figs) +
              " (exact diagrams to be pasted in unchanged; they are not character sheets).", ""]
    L += ["## 1. Art style and characters",
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
          + page['layout'], "", "## 3. Panels"]
    for j, p in enumerate(page['panels'], 1):
        L.append(f"PANEL {j} ({p['size']}): {p['art']}")
        if p.get('chars'):
            L.append(f"      characters: {p['chars']}")
        if p.get('fig'):
            L += _fig_lines(p['fig'], url_of(p['fig']) if url_of else None)
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
          "Chinese variants. Bubbles in one panel are read top to bottom in the listed order. "
          + (NOMARK if page.get('nomark') else "Color meaning: check marks and correct = BLUE, crosses and wrong = RED, emphasis = yellow highlighter, neutral = dark navy.")
          + (" The text inside an attached figure image is part of that image: keep it exactly as it is and do not add to it." if figs else ""), "",
          "## 5. Quality check (apply silently while drawing)",
          f"Exactly {len(page['panels'])} panels in the described layout; every string exactly as written and nothing else; no name or role word; "
          "every bubble tail points at its own speaker; the student matches sheets I-01, I-02, I-03 and is drawn in the bird teacher's style; "
          "she has exactly two arms and two hands; pictograms have no faces; "
          + ("no ○, ×, check mark, cross, or stamp anywhere on the page; " if page.get('nomark') else "")
          + ("each attached figure sits unchanged in its rectangle with nothing drawn over it; " if figs else "")
          + "fully opaque. Deliver the first image as it is."]
    return "\n".join(L)


def header_prompt(header, scene, w, h, kind):
    """見出し画像（2人。ひっかけ診断ノートと同じ形）。header=(1行目, 2行目, 副題)。"""
    t1, t2, sub = header
    return "\n".join([
        f"Create a {kind} header image for a Japanese educational comic article, exactly {w}x{h} pixels, fully opaque.", "",
        f"TEXT (only these three strings, exactly): line 1 on a pale yellow marker band 「{t1}」; line 2 large, the key word in reddish orange "
        f"「{t2}」; subtitle in a light-blue rounded band 「{sub}」. No other words, digits, or Latin letters.", "",
        "CHARACTERS: exactly two. " + TEACHER + " Place him lower right of center. " + STUDENT + " Place her lower left of center. "
        "Free, natural poses that fit the topic, different each time; both fully visible, faces clear of the title. "
        "No names or role words anywhere.", "",
        f"STYLE: the bird teacher's flat pastel style; the topic scene ({scene}) fades softly into the left and right edges with "
        "no text in it. Do not imitate any existing manga series.", "",
        "Final check: only the three strings; standard Japanese kanji; exactly two characters; fully opaque. Deliver the first image as it is."])


def prompts_md(title, intro_lines, pages, file_prefix, header, scene, url_of=None):
    """プロンプトのファイル（md）。見出しの形は貼り付け文が参照するので変えない。"""
    n = len(pages)
    pr = [f"# {title}", ""] + intro_lines + ["", SHEETS_NOTE + "「鳥が先生、女性が生徒です。名前は画像に書かないでください」と添えてから、1ページずつ貼る。2ページ目からは同じチャットで続ける。", "",
          f"ファイル名：`{file_prefix}_p01.png`〜`_p{n:02d}.png`、見出し画像 `{file_prefix}_見出し_note.png`／`_見出し_IG.png`。", ""]
    fl = figs_of(pages)
    if fl:
        pr += ["## 差し込む図（Claudeが作った正確な図。描き直させない）", "",
               "| ページ | 図のファイル | 置く枠（x, y, 幅, 高さ px） | URL |", "|---|---|---|---|"]
        pr += [f"| {k} | `{f['name']}.png` | {f['rect'][0]}, {f['rect'][1]}, {f['rect'][2]}, {f['rect'][3]} | {url_of(f) if url_of else ''} |" for k, _, f in fl]
        pr += ["", "図のあるページは、その図のPNGも添付してから貼る。生成された画像で図が崩れたら、`tools/gakushu_manga/paste_fig.py` で正確な図を枠に貼り直す。", ""]
    for k, page in enumerate(pages, 1):
        pr += [f"## {k}ページ目：{page['caption']}", "", f"ねらい：{page['aim']}", "", "```", page_prompt(pages, k, page, url_of), "```", ""]
    pr += ["## 見出し画像（note用 1280×670）", "", "```", header_prompt(header, scene, 1280, 670, 'landscape note.com'), "```", "",
           "## 見出し画像（Instagram用 1080×1440）", "", "```", header_prompt(header, scene, 1080, 1440, 'portrait Instagram (3:4)'), "```", ""]
    return "\n".join(pr)
