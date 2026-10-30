# ハイライト「はじめに」の画像プロンプト（ChatGPT用・4枚）

ストーリーのハイライト「はじめに」（`stories.md`）の4枚（1080×1920）を、ChatGPTで作るためのプロンプト。2026-10-30。

## 使い方

1. 1枚ずつ、新しいチャットか同じチャットで、コードブロックをそのまま貼る。
2. **1枚目・2枚目・4枚目はトリ先生が出る**。ChatGPTに、トリ先生のキャラクターシート（`キャラクターシート_トリ先生_01〜03`）を添付してから貼る。3枚目はキャラクターが出ないので、添付は要らない。
3. 仕上がりを確かめる（下の「確かめること」）。直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。
4. ファイル名は `ig_story_hajimeni_01.png` 〜 `04.png`。ストーリーに続けて投稿し、全部をハイライト「はじめに」に入れる。

## 確かめること

- 大きさが1080×1920（9:16）か。上の約260px・下の約340pxに、文字や大事な絵が入っていないか。
- 文字が、下の文面と**1字ずつ**一致しているか（とくに、簡体字・繁体字の形になっていないか、余計な文字がないか）。
- 4枚で、空・色・文字の雰囲気がそろっているか。
- 2枚目：3つの場面が上から「電車の中」「お昼休み」「CMの間」の順か。トリ先生が3場面とも同じ見た目か。Latin文字が「CM」の2文字だけか。
- 4枚目：Latin文字が「note」の4文字だけか。サービスのロゴが描かれていないか。

文字が何度やっても崩れるときは、プロンプトの「TEXT」の部分を消して「No text at all」と書き換え、文字なしの背景と絵だけを作らせて、文字はCanvaなどで入れる。

## 01枚目：何のアカウントか（トリ先生が出る。キャラクターシートを添付）

```
Create a Japanese-language Instagram Story image, portrait layout, EXACTLY 1080x1920 pixels (9:16).
STYLE: soft Japanese watercolor-like illustration with a bright pastel morning sky (light blue, cream, pale yellow), gentle clouds, clean outlines, friendly flat explainer-graphic feel. Keep the same sky, colors (dark navy text, red-orange accent, pale yellow marker) and rounded bold Japanese font look as the other slides of this four-slide set.
SAFE ZONE (critical): Instagram covers the top and the bottom of a Story. Keep ALL text and ALL important drawings between y=260px and y=1580px. The top 260px and the bottom 340px contain only the soft sky background, nothing else.
TEXT RULES (critical): render the text strings below in standard Japanese only (hiragana, katakana, Jōyō kanji), verbatim, stroke-for-stroke. Do NOT use Simplified or Traditional Chinese character forms. Do not paraphrase, add, translate or omit any character. Do not add any other text anywhere: no extra labels, no pseudo-writing, no logos, no watermarks, no account name, no URL, no hashtags, no page numbers. Half-width Arabic digits are allowed ONLY where they appear in the given strings. Any prop (cards, phone screens, signs) that is not given a word must have a blank surface or an icon instead of writing.
BACKGROUND: fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.
CHARACTER (critical): draw only the owl teacher (トリ先生) shown in the attached character sheets (キャラクターシート_トリ先生_01〜03). Copy his face, body, glasses and outfit exactly; do not redesign him, and do not add any other character, person or animal. POSE IS NOT FIXED: ignore the poses in the sheets and give him a natural pose that fits the scene below. Human-like anatomy is not needed, but keep him anatomically consistent (no extra wings, hands or heads). Keep his face clear of the text.

TEXT (reproduce verbatim, nothing else), centered in the upper-middle area between y=300px and y=800px, bold rounded font, dark navy, over a soft white cloud-shaped glow so it reads clearly:
Line 1, very large, with a pale yellow marker stroke behind it:
土地家屋調査士試験
Line 2, large; the phrase 毎日3枚 in red-orange and the rest in dark navy:
過去問を図解で毎日3枚
Line 3, smaller, dark navy:
令和8年度の問1から、さかのぼっていきます
Check the kanji 土・地・家・屋・調・査・士・試・験・過・去・図・解・毎・令・和・度 are standard Japanese forms.

SCENE: below the text, the owl teacher stands at the center (about y=900px to y=1500px), pointing upward cheerfully with one wing. Three small poster cards with blank faces (rounded rectangles with simple colorful icons only, no writing) float around him, as if they were three pictures of infographics.
```

## 02枚目：いつでもどこでも、隙間時間で復習（トリ先生が出る。キャラクターシートを添付）

```
Create a Japanese-language Instagram Story image, portrait layout, EXACTLY 1080x1920 pixels (9:16).
STYLE: soft Japanese watercolor-like illustration with a bright pastel morning sky (light blue, cream, pale yellow), gentle clouds, clean outlines, friendly flat explainer-graphic feel. Keep the same sky, colors (dark navy text, red-orange accent, pale yellow marker) and rounded bold Japanese font look as the other slides of this four-slide set.
SAFE ZONE (critical): Instagram covers the top and the bottom of a Story. Keep ALL text and ALL important drawings between y=260px and y=1580px. The top 260px and the bottom 340px contain only the soft sky background, nothing else.
TEXT RULES (critical): render the text strings below in standard Japanese only (hiragana, katakana, Jōyō kanji), verbatim, stroke-for-stroke. Do NOT use Simplified or Traditional Chinese character forms. Do not paraphrase, add, translate or omit any character. Do not add any other text anywhere: no extra labels, no pseudo-writing, no logos, no watermarks, no account name, no URL, no hashtags, no page numbers. Half-width Arabic digits are allowed ONLY where they appear in the given strings. Any prop (cards, phone screens, signs) that is not given a word must have a blank surface or an icon instead of writing.
BACKGROUND: fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.
CHARACTER (critical): draw only the owl teacher (トリ先生) shown in the attached character sheets (キャラクターシート_トリ先生_01〜03). Copy his face, body, glasses and outfit exactly; do not redesign him, and do not add any other character, person or animal. POSE IS NOT FIXED: ignore the poses in the sheets and give him a natural pose that fits the scene below. Human-like anatomy is not needed, but keep him anatomically consistent (no extra wings, hands or heads). Keep his face clear of the text.

TEXT (reproduce verbatim, nothing else), bold rounded font, dark navy:
Heading at the top of the safe area, large, centered, two lines, with a pale yellow marker stroke; the phrase 隙間時間 in red-orange:
いつでもどこでも
隙間時間で復習
Three scene captions, one per panel, each in a small white rounded label (see the scene):
電車の中
お昼休み
CMの間
Check the kanji 隙・間・時・復・習・電・車・中・昼・休 are standard Japanese forms. The only digits and Latin letters allowed on the whole canvas: the three Latin letters C, M in the caption CMの間 (written exactly "CM"). No other Latin letter or digit anywhere.

SCENE (three horizontal panels stacked from top to bottom, between y=420px and y=1500px, each about 340px high, each a rounded-rectangle window with a soft pastel background; the same owl teacher appears in all three, looking at a smartphone held in his wing; the phone screen shows only a colorful infographic poster made of icons, no writing):
Panel 1 (top): inside a train, the owl sits on a seat holding the phone, with hanging straps and a window with a calm town view behind him. Caption label 「電車の中」 at the panel's upper left.
Panel 2 (middle): lunch break at a bright office cafeteria table, the owl holds the phone in one wing while the other wing holds a sandwich or a rice ball; a small mug on the table. Caption label 「お昼休み」 at the panel's upper left.
Panel 3 (bottom): a cozy living room, the owl sits on a sofa with the phone, while a TV in the background shows only a simple colorful cartoon-like commercial scene (no writing on the TV). Caption label 「CMの間」 at the panel's upper left.
Keep the owl's face clear of the captions. Soft sparkles around the phones to give a light mood.
```

## 03枚目：1枚で分かる（キャラクターなし）

```
Create a Japanese-language Instagram Story image, portrait layout, EXACTLY 1080x1920 pixels (9:16).
STYLE: soft Japanese watercolor-like illustration with a bright pastel morning sky (light blue, cream, pale yellow), gentle clouds, clean outlines, friendly flat explainer-graphic feel. Keep the same sky, colors (dark navy text, red-orange accent, pale yellow marker) and rounded bold Japanese font look as the other slides of this four-slide set.
SAFE ZONE (critical): Instagram covers the top and the bottom of a Story. Keep ALL text and ALL important drawings between y=260px and y=1580px. The top 260px and the bottom 340px contain only the soft sky background, nothing else.
TEXT RULES (critical): render the text strings below in standard Japanese only (hiragana, katakana, Jōyō kanji), verbatim, stroke-for-stroke. Do NOT use Simplified or Traditional Chinese character forms. Do not paraphrase, add, translate or omit any character. Do not add any other text anywhere: no extra labels, no pseudo-writing, no logos, no watermarks, no account name, no URL, no hashtags, no page numbers. Half-width Arabic digits are allowed ONLY where they appear in the given strings. Any prop (cards, phone screens, signs) that is not given a word must have a blank surface or an icon instead of writing.
BACKGROUND: fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.

No characters on this slide.

TEXT (reproduce verbatim, nothing else), centered, bold rounded font, dark navy over a soft white cloud-shaped glow:
Heading, large, two lines, with a pale yellow marker stroke; the phrase まず何を確認するか in red-orange:
1枚で「まず何を確認するか」
が分かる
Sub text, smaller, two lines:
問題文を読まなくても、どこが狙われるかが分かる図解です。
保存して、隙間時間に見返してください。
Check the kanji 問・題・読・確・認・狙・図・解・保・存・隙・間・時・見・返 are standard Japanese forms.

SCENE (below the text, y=950px to y=1500px, no writing anywhere in the drawing): a large smartphone in the center showing a colorful infographic card poster made of simple icons, checkmarks and arrows only. A magnifying glass with a checkmark over one icon, a bookmark (save) icon at the upper right of the phone, and a small clock icon at the lower left to suggest spare moments. Soft sparkles around.
```

## 04枚目：noteへの案内（トリ先生が出る。キャラクターシートを添付）

```
Create a Japanese-language Instagram Story image, portrait layout, EXACTLY 1080x1920 pixels (9:16).
STYLE: soft Japanese watercolor-like illustration with a bright pastel morning sky (light blue, cream, pale yellow), gentle clouds, clean outlines, friendly flat explainer-graphic feel. Keep the same sky, colors (dark navy text, red-orange accent, pale yellow marker) and rounded bold Japanese font look as the other slides of this four-slide set.
SAFE ZONE (critical): Instagram covers the top and the bottom of a Story. Keep ALL text and ALL important drawings between y=260px and y=1580px. The top 260px and the bottom 340px contain only the soft sky background, nothing else.
TEXT RULES (critical): render the text strings below in standard Japanese only (hiragana, katakana, Jōyō kanji), verbatim, stroke-for-stroke. Do NOT use Simplified or Traditional Chinese character forms. Do not paraphrase, add, translate or omit any character. Do not add any other text anywhere: no extra labels, no pseudo-writing, no logos, no watermarks, no account name, no URL, no hashtags, no page numbers. Half-width Arabic digits are allowed ONLY where they appear in the given strings. Any prop (cards, phone screens, signs) that is not given a word must have a blank surface or an icon instead of writing.
BACKGROUND: fully opaque from edge to edge; no transparency, no checkerboard, no unpainted edge.
CHARACTER (critical): draw only the owl teacher (トリ先生) shown in the attached character sheets (キャラクターシート_トリ先生_01〜03). Copy his face, body, glasses and outfit exactly; do not redesign him, and do not add any other character, person or animal. POSE IS NOT FIXED: ignore the poses in the sheets and give him a natural pose that fits the scene below. Human-like anatomy is not needed, but keep him anatomically consistent (no extra wings, hands or heads). Keep his face clear of the text.

TEXT (reproduce verbatim, nothing else), centered in the upper-middle area between y=300px and y=900px, bold rounded font, dark navy over a soft white cloud-shaped glow:
Heading, very large, with a pale yellow marker stroke; the word 解説 in red-orange. The four lowercase Latin letters n, o, t, e written exactly as "note" are the ONLY Latin letters allowed on the whole canvas:
くわしい解説はnoteで
Line 2, large:
プロフィールのリンクから
Line 3, smaller, two lines:
各肢の正誤は現行の法令で確かめ、
根拠の条文は原文と照合しています
Check the kanji 解・説・各・肢・正・誤・現・行・法・令・確・根・拠・条・文・原・照・合 are standard Japanese forms.

SCENE: below the text, the owl teacher at the center-left (about y=1000px to y=1500px), pointing UP with one wing toward the top of the image, as if pointing at the profile link. Beside him, a simple chain-link icon with a large upward arrow (no writing). No logo of any service.
```
