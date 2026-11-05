"""各年度の択一式の図解の表紙（Instagram・3:4・1080x1440）の画像プロンプトを prompts/Instagram_<年度>_00.md に書き出す。
令和8年度〜平成17年度の22年度分。構成は令和8年度の見本画像（上にタイトル・下中央にMC1人・左右に薄い話題の絵）を踏襲する。
ポーズと表情は年度ごとに変える（POSES）。キャラクターシートは画像の生成時に添付して参照させる（SHEETS）。
使い方: python3 note-unei/instagram/make_ig_cover.py（手で直さず、ここを直して作り直す）"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'prompts')
SHEETS = ['MK-01', 'MK-02', 'MK-03', 'MK-04', 'MK-05', 'MK-06']   # 2026-10-30 に解説記事の見出し画像で採用したキャラクターシート

# (記号, 年度の表記)。令和元年度は「元」で書くので年度の数字は入らない。
YEARS = [('R8', '令和8年度'), ('R7', '令和7年度'), ('R6', '令和6年度'), ('R5', '令和5年度'), ('R4', '令和4年度'),
         ('R3', '令和3年度'), ('R2', '令和2年度'), ('R1', '令和元年度')] + \
        [(f'H{n}', f'平成{n}年度') for n in range(30, 16, -1)]

# 22通り。ポーズ（持ち物は文字のない無地の小道具だけ）と表情を、年度ごとに変える。
POSES = [
    'standing upright and smiling warmly while holding a small closed notebook in both hands in front of her chest',
    'giving a small friendly wave with her right hand while the left hand holds a closed notebook at her side; cheerful open smile',
    'tilting her head slightly with a curious, thoughtful smile, one finger lightly touching her chin, the other hand holding a closed notebook',
    'holding a closed notebook against her chest with both arms and smiling softly with her eyes gently closed, calm and reassured',
    'giving an encouraging thumbs-up with one hand, bright confident grin, the other hand relaxed at her side',
    'leaning forward slightly with both hands clasped in front, looking at the viewer with a sparkling, eager expression',
    'holding a plain pencil up beside her face with one hand and smiling as if she just had an idea, eyebrows raised happily',
    'standing with both hands behind her back, leaning a little, with a playful, relaxed smile',
    'pressing both fists lightly in front of her chest in a determined cheer pose, with a focused yet smiling expression',
    'holding a closed notebook in one hand and pointing upward with the other index finger, as if explaining, with a bright, assured smile',
    'resting one hand on her cheek with a gentle, pondering smile while the other arm holds a closed notebook',
    'holding a closed notebook out toward the viewer with both hands, offering it with a kind, welcoming smile',
    'tucking a strand of hair behind her ear with one hand, shy but happy smile, the other hand holding a closed notebook',
    'raising both hands slightly with open palms in a gentle "here we go" gesture, an excited, bright smile',
    'holding a plain clipboard with a blank sheet against her chest, a calm, professional, friendly smile',
    'making a small "OK" circle with one hand, the other hand holding a closed notebook, a relaxed and confident smile',
    'looking slightly to the side with a quiet, thoughtful smile, holding a closed notebook low in both hands',
    'laughing lightly with her eyes curved in joy, one hand lifted to her mouth, the other holding a closed notebook',
    'standing tall with a closed notebook tucked under one arm and the other hand on her hip, a confident, can-do smile',
    'holding a plain mug with both hands near her chest, taking a short break with a soft, relieved smile',
    'holding a closed notebook in her left hand and making a small victory fist with her right hand, a determined, hopeful smile',
    'bowing her head very slightly in a polite greeting while smiling, both hands holding a closed notebook in front of her',
]
assert len(POSES) == len(YEARS)

TEMPLATE = """Create an Instagram feed cover image, 3:4 portrait aspect ratio, 1080x1440 pixels.

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Fill the whole canvas with the pastel sky and soft clouds. Layout from top to bottom: the title block in the upper part, the single character in the lower center, and soft, slightly faded topic scenes along the left and right edges.

CHARACTERS (critical): this cover features ONE character only: the main character (MC) shown in the attached character-specification images ({sheets}). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached character sheets closely and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Place her at the bottom center, fully visible from about the waist up, with her face clear of the title text.
POSE AND EXPRESSION (changes every time): use the character sheets as the base, and vary the pose and facial expression from that base in every image of the series; do not copy the pose of the sheets or of another cover. Only the pose and expression change, never her design. For this image: {pose}. Any prop must be plain, with no letters or marks on it. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters anywhere in the image. The only digits allowed are the half-width Arabic digits that appear inside the title and subtitle strings (the year and the question numbers), written exactly as given; no other digit anywhere. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines in the upper part, centered, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it (about 100px tall letters):
{year}
Line 2 is larger (about 150px tall letters) and red-orange:
択一式の図解
Below the title, a light blue rounded pill-shaped subtitle band with navy text (about 50px tall letters):
第1問から第20問
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no account name, no hashtag, no web address, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the character):
Left side: a small stack of land registration documents, a rolled map, and a surveying tripod standing on a patch of green land with a boundary marker stone.
Right side: a small apartment-building model and a house model, a magnifying glass, and a sheet of paper with simple line drawings (shapes only, no letters).

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep ALL text and the character inside a safe area: at least 54px from the left and right edges and at least 72px from the top and bottom edges, so the image survives the center cropping that Instagram applies on the profile grid. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1080x1440 (3:4 portrait); confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written, with the year written exactly as {year}; scan every kanji glyph ({kanji}) and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm the MC character is the only character in the image (no トリ先生, no 藍子), that she matches the attached character sheets in face, hairstyle, and outfit, and that her pose and expression follow the POSE AND EXPRESSION line; confirm nothing important is within 54px of the left or right edge or within 72px of the top or bottom edge; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere."""


def kanji_of(year):
    base = '択一式図解第問'
    seen = []
    for ch in year + base:
        if '一' <= ch <= '鿿' and ch not in seen:
            seen.append(ch)
    return ''.join(seen)


def build(code, year, pose):
    name = f'Instagram_{code}_00'
    prompt = TEMPLATE.format(sheets=', '.join('キャラクターシート_' + s for s in SHEETS), pose=pose, year=year, kanji=kanji_of(year))
    return name, f"""# {year} 択一式の図解 表紙（Instagram・3:4）

画像のファイル名：**{name}**（.png／.webp など。`schedule.csv` に載せるときはこの名前）。
大きさは3:4（1080×1440px）。令和8年度の見本（上にタイトル、下中央にMC1人、左右に薄い話題の絵）の構成を踏襲している。
ChatGPTに `{'・'.join(SHEETS)}` のキャラクターシートを添付してから、下のコードブロックを貼る。ポーズと表情はシートをベースに、年度ごとに変えてある。
画像の中の数字は、タイトルの年度の数字だけ。アカウント名・URL・ハッシュタグ・「noteへ」などの案内は入れない。
画像の生成と目視確認は未実施。

```
{prompt}
```
"""


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for (code, year), pose in zip(YEARS, POSES):
        name, body = build(code, year, pose)
        open(os.path.join(OUT, name + '.md'), 'w', encoding='utf-8').write(body)
        print(name, year)
