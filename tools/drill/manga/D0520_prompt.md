# D0520 4コマ解説図解 プロンプト（ChatGPT貼付用・v04）

- 肢：D0520（民法／物権変動・対抗要件、出典 H22-Q02オ）。正解＝〇。誤解4回。
- 記事：`note-articles/h22-mondai/q02-taikou-youken-177.md` オ「未成年者の取消しは、その前に現れた善意の買主にも対抗できる」
- ルール：`MANGA_RULES.md`
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、下のコードブロックを貼る。トリ先生の参照画像と藍子の参照画像が別ファイルの場合は、どちらがどちらかを貼り付けの冒頭に一言添える。サイズは 1080×1920（9:16）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0520～H22-Q02オ～

## note記事の冒頭文

未成年者が親の同意なく売った土地が転売され、その後に親が売買を取り消しました。転売先が事情を知らなかったとき、売主の未成年者は、その人に土地の所有権を主張できるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成22年度　第2問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 未成年者の取消しは、取消し前の善意のＢにも対抗できる | 「取消し前の善意のＢにも対抗できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 | 藍子（左） | Ｂは未成年だと知らなかった。守られますよね？ | 「守られますよね？」 |
| コマ1 | トリ先生（右） | 出たわね、その思い込み。Ａが取り消す前にＢが買った場合よ | — |
| コマ1 | 図ラベル | Ａ（未成年者）→Ｄ→Ｂ（善意）／Ｃ（Ａの法定代理人）／矢印ラベル「Ｃの同意なし」 | — |
| コマ2 見出し | ラベル | ②　流れを整理 | — |
| コマ2 | 図（3つの別カード。取引の矢印はＡ→Ｄ、Ｄ→Ｂのみ） | ①ＡがＤに売却（Ｃの同意なし） / ②ＤがＢに売却（Ｂは善意） / ③Ｃが①の売買を取消し（スタンプ「取消し」） | — |
| コマ2 | 図ラベル | Ａの所有権が回復 | — |
| コマ2 | 図の矢印ラベル | 取消しは当初にさかのぼる | 黄色マーカー |
| コマ2 | 藍子（左・先に話す） | 取り消すと、どうなるんですか？ | — |
| コマ2 | トリ先生（右・答える） | 取消しの効果は、当初にさかのぼるのよ | 「当初にさかのぼる」 |
| コマ3 見出し | ラベル | ③　取消しの前と後の違い | — |
| コマ3 左カード | 見出し | 取消しの前にＢが買った | — |
| コマ3 左カード | 本文 | 善意のＢでも、Ａは主張できる | 青チェック✓ |
| コマ3 右カード | 見出し | 取消しの後にＢが買った | — |
| コマ3 右カード | 本文／タグ | 登記がなければＡは主張できない。先に登記した方が勝つ ／ 民法177条 | 赤✕ |
| コマ3 | 藍子（左・先に話す） | 取消しの後に買った人なら、どうなりますか？ | — |
| コマ3 | トリ先生（右・答える） | 前は守る規定がなくてＡの勝ち。後は登記の先後で決まるのよ | 「守る規定」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 | 藍子（左） | 取消し前のＢには、Ａは所有権を主張できるんですね！ | — |
| コマ4 | トリ先生（右） | そのとおり。取消し前に現れた善意の買主にも対抗できるのよ | 「対抗できる」 |
| コマ4 チェック欄 | 3項目（青✓） | 取消しは当初にさかのぼる ／ 取消し前の善意のＢにも、Ａは主張できる ／ 取消し後のＢとは、登記の先後で決まる | — |
| 結論帯 | 1行目 | 制限行為能力の取消しは、取消し前の善意の第三者に対抗できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0520　正解〇（H22-Q02オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 民法177条

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｄ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｄ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「未成年者の取消しは、取消し前の善意のＢにも対抗できる」 in large bold letters; the part 「取消し前の善意のＢにも対抗できる」 has a yellow highlighter marker.

PANEL 1 (the common misconception; 藍子 confident, トリ先生 exasperated but caring; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　よくある思い込み」
- 藍子 bubble (left): 「Ｂは未成年だと
知らなかった。
守られますよね？」 with the part 「守られますよね？」 highlighted in yellow.
- トリ先生 bubble (right): 「出たわね、その思い込み。
Ａが取り消す前に
Ｂが買った場合よ」
- Small diagram in the middle: three faceless pictograms in a row with arrows: a small young pictogram with tag 「Ａ」, then a pictogram with tag 「Ｄ」, then a pictogram with tag 「Ｂ」. The arrow from Ａ to Ｄ carries the small label 「Ｃの同意なし」. Standing right behind 「Ａ」 is a taller adult pictogram with tag 「Ｃ」 and the small label 「Ｃ（Ａの法定代理人）」, so that Ｃ is introduced here. Caption under the diagram: 「Ａ（未成年者）→Ｄ→Ｂ（善意）」.

PANEL 2 (the flow; 藍子 surprised, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　流れを整理」
- Three SEPARATE numbered cards in a row, left to right. Do NOT connect the cards with arrows, and do NOT draw any arrow from Ｂ to Ｃ. Arrows exist only inside card 1 (Ａ to Ｄ) and card 2 (Ｄ to Ｂ).
  - Card 1: pictograms 「Ａ」 and 「Ｄ」 with one arrow from Ａ to Ｄ; text 「①ＡがＤに売却（Ｃの同意なし）」.
  - Card 2: pictograms 「Ｄ」 and 「Ｂ」 with one arrow from Ｄ to Ｂ; text 「②ＤがＢに売却（Ｂは善意）」.
  - Card 3 (keep the round stamp fully inside this card's frame, smaller than the card, with clear space from トリ先生's pointer): NOT a sale. It shows the adult pictogram 「Ｃ」 holding a large dark navy round stamp that reads 「取消し」; text 「③Ｃが①の売買を取消し」.
- One curved dark navy arrow starts at the stamp in card 3 and points back to the Ａ-to-Ｄ arrow in card 1 (cancelling that sale). Its label 「取消しは当初にさかのぼる」 has a yellow highlighter marker. Next to the pictogram 「Ａ」 in card 1 add the small label 「Ａの所有権が回復」.
- 藍子 bubble (left, spoken first): 「取り消すと、
どうなるんですか？」
- トリ先生 bubble (right, spoken as the answer): 「取消しの効果は、
当初にさかのぼるのよ」 with 「当初にさかのぼる」 highlighted in yellow.

PANEL 3 (the contrast between before and after the cancellation; both characters point together at the same two comparison cards, トリ先生 pointing at the cards with one wing and 藍子 with one hand; 藍子's hands: ONE hand points at the diagram with an extended arm and the other hand hangs at her side or holds the clipboard; her hands are NOT clasped and no third hand appears):
- Label tab: 「③　取消しの前と後の違い」
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.
- Above the two cards, a thin horizontal timeline band with a vertical dark navy marker labeled 「取消し」 in the middle; the left card hangs under the part before the marker and the right card under the part after the marker.
- Left card, heading 「取消しの前にＢが買った」, body 「善意のＢでも、Ａは主張できる」, with ONE blue check mark only (no cross on this card).
- Right card, heading 「取消しの後にＢが買った」, body 「登記がなければＡは主張できない。先に登記した方が勝つ」, small tag 「民法177条」, with ONE red cross only (no check mark on this card).
- 藍子 bubble (left, spoken first): 「取消しの後に買った人なら、
どうなりますか？」
- トリ先生 bubble (right, spoken as the answer): 「前は守る規定が
なくてＡの勝ち。
後は登記の先後で決まるのよ」 with 「守る規定」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (the conclusion; 藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left): 「取消し前のＢには、
Ａは所有権を
主張できるんですね！」
- トリ先生 bubble (right): 「そのとおり。
取消し前に現れた善意の
買主にも対抗できるのよ」 with 「対抗できる」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「取消しは当初にさかのぼる」, 「取消し前の善意のＢにも、Ａは主張できる」, 「取消し後のＢとは、登記の先後で決まる」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「制限行為能力の取消しは、取消し前の善意の第三者に対抗できる」 with a yellow highlighter marker.
- Line 2: 「問題D0520　正解〇（H22-Q02オ）」

EMOTIONAL ARC: confident (panel 1) -> surprised (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels; confirm the characters 権, 所, 売, 買, 当, 初, 規, 対, 抗, 効, 張, 解, 違, 代, 登, 記 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm the left comparison card in panel 3 has only a blue check mark and the right card only a red cross; confirm the timeline marker 「取消し」 separates the left card (before) from the right card (after) in panel 3; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 未成年者が取り消したら | 薄い黄色のマーカー |
| タイトル2行目 | 転売先にも主張できる？ | 「主張できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0520　H22-Q02オ | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
未成年者が取り消したら
Line 2 is larger; the phrase 主張できる？ is red-orange and the rest is dark navy:
転売先にも主張できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0520　H22-Q02オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a school bag and a young person's silhouette standing beside a small plot of land
Right side: two small houses in a row, with a pink eraser and a calendar page with no writing

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 未, 成, 年, 者, 取, 消, 転, 売, 先, 主, 張, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 画像ファイル名（名づけルール）

ChatGPTで生成した画像は、保存するときに次の名前へ変更する（拡張子は生成された形式のまま：png・webp など）。`MANGA_RULES.md` の「画像ファイル名」に従う。

| 画像 | ファイル名 |
|---|---|
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0520～H22-Q02オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0520～H22-Q02オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0520～H22-Q02オ～_v01.png ／ 4コマ解説図解D0520～H22-Q02オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0520_prompt.md` が NG 0件・WARN 0件（2026-10-06）
- [x] 工程C：登場人物Ｃは1コマ目で紹介／取消しは売買の鎖の外（別カード）／藍子の質問→トリ先生の答えの順／青＝はい・赤＝いいえ・ネイビー＝中立

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く
- [ ] 2人の外見が添付画像どおり・全コマで同一
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致（Ａ〜Ｄの取り違えなし）
- [ ] コマ3：左＝青✓のみ、右＝赤✕のみ。カード文言が別々
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）

## v01の検品結果と修正（2026-10-06）
- v01（生成画像）の問題：①Ｃが初出なのにコマ2で突然登場し、Ｂ→Ｃの矢印で「ＢがＣに売った」ように見える。②赤い戻り矢印の起点がＣの人物で、「取消し」という出来事の矢印になっていない。③コマ1で藍子の吹き出しの文言が構成表と違った（表を現状の画像に合わせた）。④コマ2・3で藍子の反応が先に読まれ、トリ先生の説明より前に「気づき」が来る順序のずれ。⑤コマ2の「Ｂが買う前にもどる」は遡及の説明として不正確。
- 修正：Ｃをコマ1で「Ａの法定代理人」として登場させる。コマ2は3つの独立したカードにし、③は売買ではなく「取消し」のスタンプとして描く。藍子は質問、トリ先生は答えの順にする。

### ChatGPTへの修正依頼文（v01の画像を基準に貼る）
```text
直前に表示された最新版（v01）を基準に、以下の修正だけ行ってください。
1. コマ1：Ａ→Ｄの矢印に小さなラベル「Ｃの同意なし」を付ける。Ａの後ろに、背の高い大人のピクトグラム（タグ「Ｃ」）を立たせ、小さなラベル「Ｃ（Ａの法定代理人）」を付ける。
2. コマ2の流れ図を、矢印でつながない3つの別カードに描き直す。矢印はカード1の中のＡ→Ｄ、カード2の中のＤ→Ｂだけにし、Ｂ→Ｃの矢印は描かない。カード1「①ＡがＤに売却（Ｃの同意なし）」、カード2「②ＤがＢに売却（Ｂは善意）」、カード3は売買ではなく、ピクトグラム「Ｃ」がネイビーの丸い「取消し」のスタンプを持つ図にして、文言は「③Ｃが①の売買を取消し」。ネイビーの曲がった矢印はカード3のスタンプからカード1のＡ→Ｄの矢印へ戻し、ラベル「取消しは当初にさかのぼる」（黄色マーカー）を付ける。カード1のＡの横に小さなラベル「Ａの所有権が回復」を足す。
3. コマ2の藍子（左）の吹き出し全体を、「えっ、Ｂが買う前にもどるんですか？」から「取り消すと、
どうなるんですか？」へ変更する。
4. コマ3の藍子（左）の吹き出し全体を、「同じ取消しなのに、第三者の扱いが違うんですね」から「詐欺取消しだと、
第三者は守られるのに…」へ変更する。

変更しない箇所：上記以外のすべての文字・色・人物・表情・背景・吹き出しの位置と形、タイトル帯、コマ3の比較カード、コマ4、結論帯。
指定文言を一字ずつ正確に入れ、指定外の文字を追加しないでください。完成画像全体を1枚で表示してください。
```

## v02の検品結果（2026-10-06）→ 採用
採用版：`images/4コマ解説図解D0520～H22-Q02オ～.webp`（v01は不採用。画像は9:16の縦長）。
- 合格：①Ｃはコマ1で「Ｃ（Ａの法定代理人）」として登場し、コマ2では3つの独立カードになった（Ｂ→Ｃの矢印なし、③は「取消し」のスタンプ）。②藍子（左）の質問→トリ先生（右）の答えの順になり、尾は各話者を向いている。③コマ2の戻り矢印・スタンプはネイビー、コマ3は左＝青✓・右＝赤✕で極性が逆、コマ4のチェックは青。④タイトル・全セリフ・ラベル・結論帯は構成表と一致。簡体字・余計な文字なし、背景は不透明。⑤法的内容は記事（H22-Q02オ）の範囲内（民法96条3項は記事に記載あり）。
- 軽微（採用に影響しない）：(a) 「Ａ・Ｂ・Ｃ・Ｄ」が半角で描かれた（構成表は全角）。意味は同じなので許容とし、規則は全角・半角どちらも可に改めた。(b) コマ2の「取消し」スタンプがカードの右端からはみ出し、トリ先生の指し棒に近い。(c) コマ2の藍子の前髪が他のコマと少し違う。(d) コマ3でトリ先生がカードを指さしていない（藍子だけが指さす）。
- 次回以降のプロンプトに反映：スタンプ・矢印・ラベルは各カードの枠の内側に収める。
- 限定修正（v03）の依頼文：`D0520_v03_fix_request.md`（(b)(c)(d)の3点だけを直す。(a)は許容）。

## v04（2026-10-07）：取消しの前と後の比較を追加（ユーザー指示）
- 変更：コマ3を「詐欺取消しとの違い」から「取消しの前と後の違い」に変えた。左＝取消しの前にＢが買った（記事の範囲。善意でもＡは主張できる）、右＝取消しの後にＢが買った（登記の先後で決まる。民法177条）。タイムラインの帯の中央に「取消し」の目印を置き、前後を分ける。藍子が「取消しの後に買った人なら？」と聞き、トリ先生が「前は守る規定がなくてＡの勝ち。後は登記の先後で決まる」と答える。
- 取消し後の扱い（登記の先後。民法177条）は、このコマの元記事（H22-Q02オ）には書かれていない。苦手分析シリーズ⑰（`note-articles/column/nigate-17-*.md` の型B、「取消し・解除・時効の完成の後に現れた第三者：登記がなければ対抗できない」）の整理と一致するため、ユーザー指示で追加した。条文は「記事に無い条文」の節に記録した。
- 正確さのため、タイトル帯と結論帯に「取消し前の」を足した（取消し後は登記の先後なので、「善意の第三者にも対抗できる」だけでは取消し後まで含めて読めてしまう）。コマ4の藍子の台詞・チェック欄も、取消し前と後を分ける文言にした。
- 詐欺取消しとの違い（民法96条3項、第三者を守る規定の有無）のカードは、4コマに収まらないためコマ3から外した。「守る規定」はトリ先生の台詞に残している。
- v02の検品で見つかった軽微な点のうち、スタンプが枠からはみ出す問題（コマ2）と、トリ先生が翼で指さす構図（コマ3）を、プロンプトに織り込んだ（`D0520_v03_fix_request.md` の限定修正は、全面的に作り直すため不要。藍子の前髪のぶれは、共通ルールの髪型固定で対応）。
- 画像はv02の採用版のまま。v04のプロンプトで作り直した画像を、検品して差し替える（旧版は `_v02` を付けて残す）。
