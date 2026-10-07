# D2096 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D2096（土地家屋調査士法／調査士法人、出典 R07-Q20ア）。正解＝×（誤った記述）。誤解3回。
- 記事：`note-articles/r7-mondai/q20-chousashihou.md` ア「定款変更の届出先は、法務局ではなく所属の調査士会及び連合会」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の5枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。調査士法人・法務局・調査士会・連合会は、建物アイコンと文字ラベルで示す。
- 矢印の意味：すべて「届出」の矢印（実線のネイビー）。コマ1は誤った届出先（？バッジ）、コマ2で正しい届出先2か所、コマ3で比較。
- 会話順：藍子の誤解（法務局へ届け出る）→正しい届出先→法務局は届出先ではない→結論（記述は×）。
- 配色：コマ3の対比は、法務局＝赤✕（届出先ではない）、調査士会と連合会＝青✓（届出先）。逆の極性。
- 記事の範囲：土地家屋調査士法34条2項／変更の日から2週間以内／変更に係る事項を主たる事務所の所在地の土地家屋調査士会と日本土地家屋調査士会連合会の両方に届出／法務局又は地方法務局への届出ではない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D2096～R07-Q20ア～

## note記事の冒頭文

土地家屋調査士法人が、定款を変更しました。この変更は、どこへ、いつまでに届け出なければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和7年度　第20問　ア）。先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 調査士法人の定款変更の届出先は、法務局ではない | 「法務局ではない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | 調査士法人 / 定款を変更 / 法務局又は地方法務局 / 届出先？ | — |
| コマ1 | 藍子（左・先に話す） | 定款を変更したら、法務局に届け出ますよね？ | 「法務局に届け出ますよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。届出先は本当にそこかしら？ | — |
| コマ2 見出し | ラベル | ②　正しい届出先 | — |
| コマ2 図 | 図・カード | 調査士法人 / 変更に係る事項を届出 / 主たる事務所の所在地の土地家屋調査士会 / 日本土地家屋調査士会連合会 / 変更の日から2週間以内 / 土地家屋調査士法34条2項 | — |
| コマ2 | 藍子（左・先に話す） | 正しい届出先は、どこなんですか？ | — |
| コマ2 | トリ先生（右・答える） | 主たる事務所の所在地の調査士会と、連合会の両方よ | 「調査士会と、連合会の両方」 |
| コマ3 見出し | ラベル | ③　法務局は届出先ではない | — |
| コマ3 図 | 図・カード | 法務局又は地方法務局 / 届出先ではない / 調査士会と連合会（両方） / ここへ届け出る | — |
| コマ3 | 藍子（左・先に話す） | 法務局への届出は、いらないんですか？ | — |
| コマ3 | トリ先生（右・答える） | ええ。届出先は調査士会と連合会の両方よ | 「調査士会と連合会の両方」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 定款を変えたら、2週間以内に両方へ届け出るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。法務局への届出と書いてあれば×よ | 「法務局への届出と書いてあれば×」 |
| コマ4 チェック欄 | 3項目（青✓） | 変更の日から2週間以内 / 変更に係る事項を届け出る / 主たる事務所の所在地の調査士会と連合会の両方 | — |
| 結論帯 | 1行目 | 定款変更の届出先は、調査士会と連合会の両方 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D2096　正解×（R07-Q20ア） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a navy business suit over a blouse with thin blue vertical stripes; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「調査士法人の定款変更の届出先は、法務局ではない」 in large bold letters; the part 「法務局ではない」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: a flat building icon labeled 「調査士法人」 holding a small document labeled 「定款を変更」. A solid navy arrow points from it to a second building icon labeled 「法務局又は地方法務局」, with a small question badge 「届出先？」 (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「定款を変更したら、法務局に届け出ますよね？」 with the part 「法務局に届け出ますよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。届出先は本当にそこかしら？」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer):
- Label tab: 「②　正しい届出先」
- The building icon 「調査士法人」 on the left with two solid navy arrows, labeled 「変更に係る事項を届出」, pointing to two building icons on the right: 「主たる事務所の所在地の土地家屋調査士会」 and 「日本土地家屋調査士会連合会」.
- Two small tags: 「変更の日から2週間以内」 and 「土地家屋調査士法34条2項」.
- 藍子 bubble (left, spoken first): 「正しい届出先は、どこなんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「主たる事務所の所在地の調査士会と、連合会の両方よ」 with the part 「調査士会と、連合会の両方」 highlighted in yellow.

PANEL 3 (both characters point together at the same figure; 藍子 realizing):
- Label tab: 「③　法務局は届出先ではない」
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows a BLUE check mark; the right card shows a RED cross. Do not draw the same mark on both cards. The two cards also have clearly different texts; the two texts are NOT identical.
- Left card, heading 「法務局又は地方法務局」, body 「届出先ではない」, with ONE red cross only (no check mark on this card).
- Right card, heading 「調査士会と連合会（両方）」, body 「ここへ届け出る」, with ONE blue check mark only (no cross on this card).
- 藍子 bubble (left, spoken first): 「法務局への届出は、いらないんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「ええ。届出先は調査士会と連合会の両方よ」 with the part 「調査士会と連合会の両方」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「定款を変えたら、2週間以内に両方へ届け出るんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。法務局への届出と書いてあれば×よ」 with the part 「法務局への届出と書いてあれば×」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「変更の日から2週間以内」, 「変更に係る事項を届け出る」, 「主たる事務所の所在地の調査士会と連合会の両方」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「定款変更の届出先は、調査士会と連合会の両方」 with a yellow highlighter marker.
- Line 2: 「問題D2096　正解×（R07-Q20ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 届, 当, 所, 款, 解, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm the left comparison card has only a blue check mark and the right card only a red cross; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 調査士法人の定款変更 | 薄い黄色のマーカー |
| タイトル2行目 | 届出先はどこ？ | 「届出先はどこ？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D2096　R07-Q20ア | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief) standing at the lower left of center with one wing raised as if explaining. 藍子 is the young woman exam candidate (long wavy brown hair, blouse with thin blue vertical stripes, navy suit) at the lower right of center, resting her chin on one hand with a pen, looking up at トリ先生 with a curious smile, an open textbook on the desk in front of her. Keep both characters facing each other and fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
調査士法人の定款変更
Line 2 is larger; the phrase 届出先はどこ？ is red-orange and the rest is dark navy:
届出先はどこ？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D2096　R07-Q20ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small office building with an empty nameplate and a rolled charter scroll
Right side: two civic buildings side by side (a hall and a taller federation building) and a blank two-week calendar

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 調, 査, 士, 法, 人, 定, 款, 変, 更, 届, 出, 先, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
```

### 見出し画像の検品
- [ ] 画像内の文字は、タイトル2行とサブタイトルだけ。文言が上の表と一字一句一致、簡体字・余計な文字なし
- [ ] トリ先生が左下、藍子が右下で向き合い、顔がタイトルに重ならない。藍子の髪型が参照画像どおり
- [ ] 左右のテーマの場面に文字がなく、タイトル・キャラより目立たない
- [ ] 背景が不透明（透過・チェッカーボードなし）、中央でトリミングしても主要要素が切れない

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D2096_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：建物アイコンが4種（調査士法人、法務局又は地方法務局、土地家屋調査士会、日本土地家屋調査士会連合会）で、ラベルの取り違えがない
- [ ] 工程C：構成表の全文言を記事（R07-Q20ア）と突き合わせ：「2週間以内」「主たる事務所の所在地」「両方」「34条2項」
- [ ] 工程C：コマ3の左右のカードのマークが逆で、文言が別々（法務局＝届出先ではない／調査士会と連合会＝ここへ届け出る）

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
