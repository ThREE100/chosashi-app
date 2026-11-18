# 「すきま時間の一枚まとめ」マガジン用 見出し画像のプロンプト（ChatGPT用）

2026-11-18 作成。noteのマガジンの見出し画像（1280×670）。年度別マガジン・「間違いノート」マガジンと同じ仕様で、**マガジンヘッダーとして実際に表示されるのは縦中央の帯（y=227〜443、高さ216px）だけ**。タイトルと女性のMCキャラクターの顔・上半身は、この帯の中に収める（タイトルの位置は既定の場所）。画像の生成と目視確認はChatGPTで行う（未実施）。マガジン用なので、Instagram用はない。

## 使い方
1. ChatGPTに、キャラクターシート `キャラクターシート_MC-01〜MC-04` の4枚を添付してから、下のコードブロックをそのまま貼る。
2. 1280×670が出ないときは、横長（約1.91:1）で生成させ、1280×670にリサイズ・トリミングする。帯は画像の高さの約33.9%〜66.1%。トリミング後に、帯の中で顔・文字が切れていないかを確かめる。
3. 直すときは、プロンプトの最後に「次の点だけを直して、ほかは変えない：…」と1文足して再生成する。

## 画像に入れる文字（正本）
| 位置 | 文字 | 強調 |
|---|---|---|
| 1行目（小さめ） | すきま時間の | なし |
| 2行目（大きく） | 一枚まとめ | 「一枚」を赤橙、「まとめ」を濃紺 |
| 小さな帯（丸い角） | 分野ごとの要点をスマホで | なし |

数字・英字は入れない。

## 確かめること
- 大きさが 1280×670 か。
- 文字が上の3つだけで、**1字ずつ**一致しているか（簡体字・繁体字の字形になっていないか、余計な文字・数字・英字がないか）。
- タイトル（3つの文字）と、MCの顔・上半身が、帯（y=227〜443）の中に収まっているか。帯の外側は文字も人物もなく、やわらかい背景だけか。
- キャラクターがMC1人だけか（トリ先生・藍子が入っていないか）。シートの髪型・服装と合っているか。手や腕の数が合っているか。
- 小道具（スマートフォン、縦長の紙、付せんなど）に文字・数字が入っていないか。
- 背景が不透明か。

文字が崩れるときは、「TEXT」の部分を「No text」に書き換えて文字なしの背景とキャラクターだけを作らせ、文字はCanvaなどで重ねる。

## プロンプト（1280×670）

```
Create a landscape magazine header image, EXACTLY 1280x670 pixels (1.91:1 landscape aspect ratio), for a note.com magazine of one-page quick-reference summaries for the Japanese 土地家屋調査士 (land and house surveyor) exam, to be read on a smartphone in spare moments.

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com header images of the same series. Fill the whole canvas with the pastel sky and soft clouds.

CANVAS SAFE-ZONE REQUIREMENT (critical): only the vertical center band from y=227px to y=443px (a 216px-tall horizontal strip across the full 1280px width) is visible when this image is shown as the magazine header. The title text and the main character's face and upper body MUST be fully contained inside this band. Everything above y=227px and below y=443px is a soft, low-contrast, low-detail decorative extension of the same sky scene (no text, no character, no important detail), but the whole 1280x670 canvas must still look complete and balanced.

CHARACTERS (critical): this image features ONE character only: the main character (MC) shown in the attached character-specification images (キャラクターシート_MC-01, MC-02, MC-03, MC-04). Do NOT draw トリ先生 (the bird teacher), 藍子, or any other character, person, or animal besides this one MC character. Follow the attached MC character sheets exactly and do not redesign her: copy her face, hairstyle, hair color, outfit, and proportions from the sheets, and do not invent or change any of them. Draw her from the waist up at the right side of the band (about x=1000px to x=1260px), with her whole head and both hands inside y=227-443px. POSE IS NOT FIXED: let her take a free, natural pose of your own choosing that fits the topic (for example holding up a smartphone, or holding a long sheet of paper), and choose a different pose each time this image is generated. Keep her face clear of the title ribbon. Keep her human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands.

CRITICAL TEXT REQUIREMENT: all text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and no Latin letters and no digits anywhere in the image. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters.

BACKGROUND REQUIREMENT (critical): the entire 1280x670 canvas must be fully opaque from edge to edge, including the decorative area above y=227px and below y=443px. Do NOT generate a transparent or alpha-channel background under any circumstances. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere.

TEXT (reproduce verbatim, nothing else), placed on a large, soft-white, rounded title ribbon with a thin warm-yellow border and a subtle drop shadow, spanning about x=140px to x=980px and sitting fully inside y=227-443px, with the text stacked and centered on the ribbon:
Line 1, smaller, bold, dark navy:
すきま時間の
Line 2, very large, bold, rounded Japanese letters; the phrase 一枚 is red-orange and the rest is dark navy:
一枚まとめ
Below line 2, a small light blue rounded pill-shaped band with navy text:
分野ごとの要点をスマホで
The title text must be crisp and large enough to read on a phone. Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no numbers, no logo, no watermark.

TOPIC SCENES (illustration only, no text and no numbers on any object; soft and slightly faded so they never compete with the title or the character): at the left edge inside the band (about x=0px to x=140px) a small smartphone showing a blank pale sheet; above and below the band, in the soft decorative area only, a few blank sticky notes, a long blank paper sheet floating among the clouds, and a small surveyor tripod. No writing on any of them.

LAYOUT: keep the title ribbon free of any overlap by the character's face. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the three strings すきま時間の / 一枚まとめ / 分野ごとの要点をスマホで, reproduced exactly as written, with no digits and no Latin letters; scan every kanji glyph, paying special attention to 時・間・一・枚・分・野・要・点, and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese; confirm the title ribbon, all the text, and the MC character's face and upper body are fully inside the y=227-443px band, with the title centered across the band area; confirm the area above y=227px and below y=443px holds only soft, low-detail background with no text and no character; confirm the MC character is the only character (no トリ先生, no 藍子), that she matches the attached MC character sheets, and that she has exactly two hands with five fingers each; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```
