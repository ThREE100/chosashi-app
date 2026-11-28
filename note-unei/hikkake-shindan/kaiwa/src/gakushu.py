"""学習まんが版（コマ割りが解説の進行で変わる）の共通部品。
データは gNN.py（ITEM）。1ページ＝1枚の画像（縦 1024×1536）。ページ数・コマ数は話の必要に合わせて決める。
肢の文・正誤は一問一答バンクから取る。話し手は名前で呼ばず、絵と吹き出しのしっぽで見分ける。
既存の作品の画風・キャラクター・道具はまねない（構成の型だけを学習まんがから借りる）。
"""
import os
from common import bank, strip_tags, nendo, TYPES, OUT
from claims import CLAIM

# ○×の決まり（2026-11-28 ユーザー指示。毎日ドリル朝と同じ）：○×・はんこ・チェックは最後のまとめのページだけ。
# ○＝肢の記述が正しい、×＝肢の記述が誤り。印は肢の記述（claims.py）の横に付け、正しい内容は「正しくは」に分けて書く。
LEGEND = '○＝肢の記述が正しい　×＝肢の記述が誤り'
NOMARK = ("NO JUDGEMENT MARKS ON THIS PAGE (critical): do not draw any circle mark ○, cross mark ×, check mark, tick, X, stamp, seal, "
          "thumbs-up icon, or red/blue judgement symbol anywhere, not even as decoration; whether an option is right or wrong is shown only "
          "on the last page. Color meaning: emphasis = yellow highlighter, neutral = dark navy, the key word may be reddish orange.")
MARKCOLOR = ("Color meaning on this last page only: the ○ mark is BLUE, the × mark is RED, emphasis = yellow highlighter, neutral = dark navy. "
             "Use ○ or × exactly once, only in the row 「この肢の記述」; the legend line explains the marks. No other check marks or stamps.")

W, H = 1024, 1536
TEACHER = ("THE TEACHER: the plump, round bird teacher in the attached sheets キャラクターシート_トリ先生_01, _02, _03 (round red glasses, "
           "blue shirt, red neckerchief, wings used as hands). Sharp-tongued but caring: exasperated, scolding-yet-warm expressions.")
STUDENT = ("THE STUDENT: the young woman in the attached sheets キャラクターシート_I-01, I-02, I-03. Copy her face, hairstyle, hair color, "
           "outfit, and proportions from those three sheets exactly; never use the look of any other student character. Redraw her in exactly "
           "the same art style as the bird teacher's sheets (same line weight, same flat pastel coloring, same head-to-body ratio) so both look "
           "like they come from one comic. Earnest, straightforward, and lively; she falls into the exam writer's traps and reacts big "
           "(confident, startled, sweating, realizing, relieved). Correct anatomy: one head, one torso, exactly one left arm and one right arm, "
           "two hands with five fingers each.")

import re as _re
_JP = _re.compile(r'[0-9０-９,，]*[一-龥ぁ-んァ-ヶーＡ-Ｚ０-９々][一-龥ぁ-んァ-ヶーＡ-Ｚ０-９0-9,，・（）「」々㎡]*')

def art_labels(art):
    out = []
    for r in _JP.findall(art):
        r = r.strip('、。,，・')
        if r.count('（') != r.count('）'): r = r.strip('（）')
        if r.count('「') != r.count('」'): r = r.replace('「', '').replace('」', '')
        if r and r not in out: out.append(r)
    return out

def normalize(it):
    """絵の指示に出てくる日本語の札・ラベルを、そのコマの「文字の指定」に足す（文字の決まりと食い違わないように）。"""
    for page in it['pages']:
        for p in page['panels']:
            have = '｜'.join(p.get('words', []) + ([p['narration']] if p.get('narration') else []))
            add = [w for w in art_labels(p['art']) if w not in have]
            if add: p['words'] = p.get('words', []) + add

def finalize(it, B):
    """最後のページ（kata.matome の印）を、バンクの truth から○×を付けたまとめのページに作る。ほかのページには nomark を付ける。"""
    last = it['pages'][-1]
    if last.get('kind') != 'matome': raise ValueError(f"{it['id']}: 最後のページが matome ではない")
    truth = B[it['id']]['truth']; mark = '○' if truth else '×'
    head = 'ポイント' if truth else '正しくは'
    words = [LEGEND, 'この肢の記述', f"{mark}　{CLAIM[it['id']]}", head, *last['lines'], f"ひっかけの型：{last['typ']}"]
    art = ("A large summary board. At the very top, a small legend line in dark navy. Below it, a row labeled この肢の記述 with the limb's claim, "
           f"and in front of the claim one large {'BLUE ○ mark' if truth else 'RED × mark'} (the only judgement mark on the page). A thin divider, then a "
           f"section headed {head} with a plain bulleted list using small navy dots (no check marks). At the bottom of the board, a rounded label for the trap type.")
    for p in it['pages'][:-1]: p['nomark'] = True
    it['pages'][-1] = dict(caption=f'まとめ：この肢は{mark}', aim='○×はこのページだけ。凡例を添え、肢の記述の横に印、正しい内容は分けて書く。生徒が自分の言葉で言い直す。',
        layout='Two panels: one large panel filling the top two thirds, and one wide panel at the bottom.',
        panels=[dict(size='large, top two thirds', art=art, words=words),
                dict(size='wide, bottom', art='The student, relieved and determined, holds her pencil up; the teacher smiles warmly with wings on hips.',
                     chars='student left, teacher right', talk=[('S', last['s_end']), ('T', last['t_end'])])])

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
          "Chinese variants. Bubbles in one panel are read top to bottom in the listed order.",
          NOMARK if page.get('nomark') else MARKCOLOR, "",
          "## 5. Quality check (apply silently while drawing)",
          f"Exactly {len(page['panels'])} panels in the described layout; every string exactly as written and nothing else; no name or role word; "
          + ("no ○, ×, check mark, cross mark, or stamp anywhere on the page; " if page.get('nomark') else "○ or × appears only once, in the row この肢の記述; ") +
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
    if it['pages'][-1].get('kind') == 'matome': finalize(it, B)
    normalize(it)
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

REPO = 'https://github.com/ThREE100/chosashi-app/blob/main/note-unei/hikkake-shindan/kaiwa/'

def instructions(it):
    """Codex用・ChatGPT（GitHub接続）用の貼り付け文。"""
    no = f"{it['no']:02d}"; n = len(it['pages']); pf = f"{no}-{it['slug']}_prompts.md"
    heads = [f"## {k}ページ目：{p['caption']}" for k, p in enumerate(it['pages'], 1)]
    cx = [f"# Codexに貼る指示文（第{it['no']}回 学習まんが版・全{n}ページ＋見出し画像2枚）", "",
          "使い方：「ここから」〜「ここまで」をそのまま OpenAI Codex に貼り、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付する（シートはリポジトリにない）。", "",
          "---ここから---", "",
          "GitHub のリポジトリ ThREE100/chosashi-app（https://github.com/ThREE100/chosashi-app 、ブランチ main）にある学習まんがのプロンプトで、画像を作ってください。", "",
          "## 対象（ここから読む）", f"- プロンプト：{REPO}{pf}", f"- 構成の型（確認用）：{REPO}02-gakushu-manga-no-kata.md", "",
          "## 手順", "1. リポジトリを clone する（手元にあれば git pull origin main）。", "   git clone https://github.com/ThREE100/chosashi-app.git && cd chosashi-app",
          f"2. プロンプトのファイルの「## 1ページ目」〜「## {n}ページ目」と「## 見出し画像（note用 1280×670）」「## 見出し画像（Instagram用 1080×1440）」の見出しの下にある ``` で囲まれたプロンプトを読む。コードブロックの中身を1文字も変えずに使う（要約・翻訳・言い換えをしない）。",
          "3. 添付した6枚を参照画像として渡し、プロンプト1つにつき1枚ずつ生成する。「キャラクターシート_トリ先生_01, _02, _03」は鳥の3枚、「キャラクターシート_I-01, I-02, I-03」は女性の3枚。鳥が先生、女性が生徒。",
          f"4. 画像を「ひっかけ診断ノート_{no}_p01.png」〜「ひっかけ診断ノート_{no}_p{n:02d}.png」「ひっかけ診断ノート_{no}_見出し_note.png」「ひっかけ診断ノート_{no}_見出し_IG.png」の名前で、リポジトリの外の作業フォルダ（例：~/hikkake-manga/{no}/）に PNG で保存する。指定の大きさでなければ、縦横比を保って拡大・縮小し全体を覆ってから中央で切り取る（歪ませない。余白を足さない。透明の部分を残さず RGB）。",
          "5. 各ページを確かめ、問題があればそのページだけ同じプロンプトで1回作り直す（2回目も直らなければ、そのまま渡して何が直らなかったかを報告する）。",
          "   - コマの数と配置がプロンプトの「## 2. Page layout」のとおり",
          "   - 文字がプロンプトの文字列と一字一句同じで、ほかの文字がない。漢字が中国の字体になっていない",
          "   - 名前・役割名（トリ先生・先生・生徒など）がどこにもない。吹き出しのしっぽが話し手を指している",
          "   - 生徒は I-01〜03 の顔・髪型・服装のままで、鳥の先生と同じ画風。腕は左右1本ずつ、手は2つで指は5本ずつ",
          "   - Ａ・Ｂ・Ｃは顔のないピクトグラム。既存の漫画作品に似た画風・キャラクターになっていない。背景が端まで塗られている",
          "6. すべての画像と、手順5の確認結果（ページごとに、できた点・崩れた点を具体的に）を報告する。", "",
          "## してはいけないこと", "- リポジトリのファイルを書き換えない。リポジトリの中に画像を置かない。git の commit・push はしない。", "", "---ここまで---", ""]
    gp = [f"# ChatGPTに貼る指示文（GitHubから直接読み込ませる形・第{it['no']}回 学習まんが版）", "",
          f"使い方：GitHubと接続したChatGPTに、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付し、「ここから」〜「ここまで」を貼る。1回の返事で1ページだけ作らせ、2ページ目からは同じチャットで下の1行を送る（全{n}ページ＋見出し画像2枚）。",
          f"ChatGPTがリポジトリを読めなかったときは、`{pf}` の該当ページのコードブロックの中身を、そのまま全文貼る（6枚の添付と一言はそのまま）。", "",
          "---ここから---", "", "接続しているGitHubのリポジトリ ThREE100/chosashi-app（ブランチ main）から、次のファイルを読んでください。", f"{REPO}{pf}", "",
          f"このファイルの見出し「{heads[0]}」の下にある ``` で囲まれたプロンプトを、1文字も変えずに（要約・翻訳・言い換えをせずに）使って、画像を1枚作ってください。コードブロックの外の説明文と、ほかの見出しのプロンプトは使いません。", "",
          "- 添付した6枚のうち、鳥の3枚（キャラクターシート_トリ先生_01〜03）が先生、女性の3枚（キャラクターシート_I-01〜03）が生徒です。",
          "- 名前・役割名は画像のどこにも書かないでください。話し手は、絵と吹き出しのしっぽで見分けます。",
          "- 大きさは 1024×1536（縦長）。作るのはこの1ページだけです。",
          f"- 作る前に、読み込んだプロンプトの最初の1行（「Draw page 1 of {n} …」で始まる行）をそのまま返事に書いて、正しいプロンプトを読めたことを示してから画像を作ってください。読めなかったときは、画像を作らずに「読めなかった」と答えてください。", "",
          "---ここまで---", "", "2ページ目以降は、同じチャットで次の1行だけを送る（○に数字）。",
          "「同じファイルの『## ○ページ目：…』の見出しの下のプロンプトで、同じやり方で次の1枚を作ってください。最初の1行を書いてから作ってください。」", "",
          "見出し画像は、次の1行を送る（大きさはプロンプトのとおり）。",
          "「同じファイルの『## 見出し画像（note用 1280×670）』の見出しの下のプロンプトで、同じやり方で1枚作ってください。最初の1行を書いてから作ってください。」（Instagram用は見出しを『## 見出し画像（Instagram用 1080×1440）』に替える）", "",
          "ページの見出し一覧（コピー用）：", ""] + [f"- {h}" for h in heads]
    return "\n".join(cx), "\n".join(gp)
