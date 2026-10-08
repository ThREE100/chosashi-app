# D0026 4コマ解説図解 プロンプト（ChatGPT貼付用・v03）

- 肢：D0026（不動産登記法／土地の分筆・合筆・地積更正、出典 H17-Q06肢1）。正解＝×（誤った記述）。誤解4回。
- 記事：`note-articles/h17-mondai/q06-bunpitsu-shinsei.md` 1「仮差押があっても、分筆に債権者の承諾は不要」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 登場人物：Ａ（所有権の登記名義人）・Ｂ（仮差押債権者）をコマ1で紹介。登記官は人物ではなく「登記官」という文字ラベルの人型（コマ3）。
- 矢印の意味：コマ2の矢印は「分筆」という手続（物理的な区分）。コマ3の矢印は登記官による記録の引き継ぎ。取引の矢印はない。
- 会話順：藍子の誤解（承諾が要る）→分筆とは何か→仮差押えの行き先→結論（記述は×）。
- 配色：対比カードはなし。チェック欄は青。結論が×である旨はラベルと台詞の文字で示す。
- 記事の範囲：分筆は一筆を複数に区分する物理的な変更にすぎず権利内容を変更しない／仮差押えの効力は分筆後の各土地に当然に及ぶ／登記官が各土地の登記記録に引き継ぐ／承諾を証する情報は不要。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0026～H17-Q06肢1～

## note記事の冒頭文

仮差押えの登記がされている土地を、所有者が分筆しようとしています。仮差押えをした債権者の承諾は、必要なのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成17年度　第6問　肢1）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 仮差押えがあっても、分筆に債権者の承諾は不要 | 「債権者の承諾は不要」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | 仮差押え / Ａ / 分筆の申請 / Ｂ / 承諾は要る？ / Ａ（所有権の登記名義人）　Ｂ（仮差押債権者） | — |
| コマ1 | 藍子（左・先に話す） | 仮差押えがあるなら、Ｂの承諾が要りますよね？ | 「承諾が要りますよね？」 |
| コマ1 | トリ先生（右・答える） | 出たわね。承諾を証する情報が要ると思ったでしょ | — |
| コマ2 見出し | ラベル | ②　分筆とは | — |
| コマ2 図 | 図・カード | 一筆 / 仮差押え / 分筆 / 二筆 / 物理的に区分するだけ | — |
| コマ2 | 藍子（左・先に話す） | 分筆すると、仮差押えの内容まで変わるんですか？ | — |
| コマ2 | トリ先生（右・答える） | いいえ。一筆を複数に区分する物理的な変更にすぎないのよ | 「物理的な変更」 |
| コマ3 見出し | ラベル | ③　仮差押えの行き先 | — |
| コマ3 図 | 図・カード | 仮差押え / 登記官 / 各土地の登記記録に引き継ぐ（転写） | — |
| コマ3 | 藍子（左・先に話す） | 仮差押えは、分筆したらどうなるんですか？ | — |
| コマ3 | トリ先生（右・答える） | 分筆後の各土地に、当然に効力が及ぶのよ | 「当然に効力が及ぶ」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 債権者の承諾を証する情報は、提供しなくていいんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。承諾が必要という記述は×よ | 「承諾が必要という記述は×」 |
| コマ4 チェック欄 | 3項目（青✓） | 分筆は一筆を区分する物理的な変更 / 仮差押えは分筆後の各土地に及ぶ / 債権者の承諾を証する情報は不要 | — |
| 注記 | 小さな注記（コマ4の下） | 注）抵当権など所有権以外の権利を分筆後の一方の土地だけで消滅させるときは、権利者の承諾を証する情報が必要（不動産登記法40条） | — |
| 結論帯 | 1行目 | 仮差押えの効力は分筆後の各土地に及び、債権者の承諾は不要 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0026　正解×（H17-Q06肢1） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法40条

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall). Between panel 4 and the conclusion banner, a thin one-line note strip (about 50 px tall) with small text, as given in the NOTE LINE below.

TITLE BANNER: text 「仮差押えがあっても、分筆に債権者の承諾は不要」 in large bold letters; the part 「債権者の承諾は不要」 has a yellow highlighter marker.

PANEL 1 (藍子 confident, トリ先生 exasperated but caring; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　よくある思い込み」
- Small diagram in the middle: a flat plot-of-land block drawn as one rectangle with a diagonal ribbon labeled 「仮差押え」 across it. A faceless pictogram with tag 「Ａ」 stands at the left of the plot holding a small document labeled 「分筆の申請」. A faceless pictogram with tag 「Ｂ」 stands at the right with a small question badge 「承諾は要る？」 (a question badge only, with no check mark and no cross). Caption under the diagram: 「Ａ（所有権の登記名義人）　Ｂ（仮差押債権者）」.
- 藍子 bubble (left, spoken first): 「仮差押えがあるなら、Ｂの承諾が要りますよね？」 with the part 「承諾が要りますよね？」 highlighted in yellow.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。承諾を証する情報が要ると思ったでしょ」.

PANEL 2 (藍子 puzzled, トリ先生 explaining with a wing-pointer; 藍子's hands: one hand touches her chin and the other holds the clipboard at her side (two hands in total)):
- Label tab: 「②　分筆とは」
- On the left, one plot-of-land block labeled 「一筆」 with the diagonal ribbon 「仮差押え」. A navy arrow (this arrow means the procedure of dividing the land, not a sale) labeled 「分筆」 points to the right, where two plot blocks are drawn side by side and labeled 「二筆」; BOTH of the two blocks carry the same diagonal ribbon 「仮差押え」 as the original block (the ribbon must not disappear after the division).
- Under the arrow, a dark navy tag reads 「物理的に区分するだけ」.
- 藍子 bubble (left, spoken first): 「分筆すると、仮差押えの内容まで変わるんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「いいえ。
一筆を複数に区分する
物理的な変更にすぎないのよ」 with the part 「物理的な変更」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 3 (both characters point together at the same figure; 藍子 realizing; 藍子's hands: ONE hand points at the diagram with an extended arm and the other hand hangs at her side or holds the clipboard; her hands are NOT clasped and no third hand appears):
- Label tab: 「③　仮差押えの行き先」
- Two plot-of-land blocks side by side, each carrying its own diagonal ribbon 「仮差押え」.
- A faceless clerk pictogram labeled 「登記官」 stands above them, with a navy arrow to both blocks labeled 「各土地の登記記録に引き継ぐ（転写）」.
- 藍子 bubble (left, spoken first): 「仮差押えは、分筆したらどうなるんですか？」.
- トリ先生 bubble (right, spoken as the answer): 「分筆後の各土地に、当然に効力が及ぶのよ」 with the part 「当然に効力が及ぶ」 highlighted in yellow.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「債権者の承諾を証する情報は、提供しなくていいんですね！」.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。承諾が必要という記述は×よ」 with the part 「承諾が必要という記述は×」 highlighted in yellow.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「分筆は一筆を区分する物理的な変更」, 「仮差押えは分筆後の各土地に及ぶ」, 「債権者の承諾を証する情報は不要」.

NOTE LINE (small text on a thin strip between panel 4 and the conclusion banner, one line, fully legible): 「注）抵当権など所有権以外の権利を分筆後の一方の土地だけで消滅させるときは、権利者の承諾を証する情報が必要（不動産登記法40条）」

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「仮差押えの効力は分筆後の各土地に及び、債権者の承諾は不要」 with a yellow highlighter marker.
- Line 2: 「問題D0026　正解×（H17-Q06肢1）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 債, 効, 地, 当, 所, 承, 抵, 押, 権, 物, 登, 肢, 解, 記, 証, 請, 諾, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 仮差押えがある土地でも | 薄い黄色のマーカー |
| タイトル2行目 | 分筆に承諾は要る？ | 「承諾は要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0026　H17-Q06肢1 | — |

### 見出し画像プロンプト本体

```text
Create a note.com article header image (eyecatch thumbnail), 1280x670px
(1.91:1 landscape aspect ratio).

STYLE: soft Japanese watercolor-like illustration with a bright pastel sky (light blue, cream, and pale yellow), gentle clouds, clean outlines, consistent with the note.com explainer-column header images of the same series. Keep exactly the same overall layout: the title block at the top center, the two characters at the bottom center, and topic scenes fading softly into the left and right edges.
Fill the whole canvas with the pastel sky and soft clouds.

CHARACTERS (critical): follow the attached character-specification images exactly and do not redesign them. トリ先生 is the chubby bird teacher (round red glasses, blue shirt, red neckerchief), placed at the lower left of center. 藍子 is the young woman exam candidate (long wavy brown hair, pinstriped light-blue blouse with rolled sleeves, navy pencil skirt, no jacket), placed at the lower right of center. POSES ARE NOT FIXED: do not copy any pose from the attached images or from earlier header images; let each character take a free, natural pose of your own choosing that fits the topic and suits the character (for example standing, sitting, leaning, gesturing, or holding a small prop), and choose a different pose each time this image is generated. Keep both characters fully visible, with their faces clear of the title text, and keep 藍子's hairstyle exactly as in the attached images. Keep 藍子's human anatomy strictly correct: exactly one head, one torso, two arms (one left, one right) and two hands in total, each hand with exactly five fingers; never draw extra arms, hands, or fingers, floating or duplicated hands, arms not growing from the shoulders, or fused hands; check that every shoulder, elbow, and wrist connects naturally.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese only, using hiragana, katakana, Jōyō (regular Japanese) kanji, and the Arabic numeral 4; the only Latin letters and digits allowed are those in the subtitle exactly as written below. Do NOT use Simplified Chinese characters or Traditional Chinese characters; every glyph must match the standard Japanese Jōyō form exactly. Do NOT render any other non-Japanese script, and no stray or decorative glyphs of any kind, even as small background or texture elements. Reproduce the exact text strings given below verbatim; do not paraphrase, translate, summarize, or substitute any characters. Within this English prompt text, use half-width parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque from edge to edge. Do NOT generate a transparent or alpha-channel background under any circumstances, even if the output file format supports transparency. Fill the full canvas, including every corner and margin, with the opaque background described above. There must be no checkerboard pattern, no partially transparent area, and no unpainted canvas edge anywhere in the final image.

TEXT (reproduce verbatim, nothing else): a large, bold, rounded Japanese title in two lines at the top center, over a soft white cloud-shaped glow so it reads clearly. Line 1 is dark navy with a pale yellow marker stroke behind it:
仮差押えがある土地でも
Line 2 is larger; the phrase 承諾は要る？ is red-orange and the rest is dark navy:
分筆に承諾は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0026　H17-Q06肢1
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: one plot of land with a wide diagonal tape band across it (a plain seal tape with no writing), seen from a slight isometric angle
Right side: the same plot divided into two parts by a dotted boundary line, with a surveying tripod beside it

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 仮, 差, 押, 土, 地, 分, 筆, 承, 諾, 要, 解, 説, 図, 肢; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0026～H17-Q06肢1～.png |
| 見出し画像（採用版） | 4コマ解説図解D0026～H17-Q06肢1～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0026～H17-Q06肢1～_v01.png ／ 4コマ解説図解D0026～H17-Q06肢1～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0026_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：「仮差押え」のリボンがコマ2では分筆前の土地にだけ付き、コマ3で分筆後の2筆の両方に付くことが、ラベルで説明されている
- [ ] 工程C：構成表の全文言を記事（H17-Q06肢1）と突き合わせ：「物理的な変更」「当然に及ぶ」「登記官によって引き継がれる」
- [ ] 工程C：結論が×（承諾が必要という記述が誤り）であることが、コマ4のラベル・台詞・結論帯から読み取れる

## 生成後の照合チェック（文言の正本は上の構成表）
- [ ] 4コマ縦一列／タイトル帯・結論帯あり
- [ ] 全コマで藍子＝左・トリ先生＝右、全吹き出しの尾が話者へ向く。藍子の髪型が全コマで同じ
- [ ] タイトル・全セリフ・ラベルが構成表と一字一句一致
- [ ] スタンプ・矢印・ラベルが各カードの枠の内側に収まっている
- [ ] 色：はい・○＝青、いいえ・×＝赤、中立＝ネイビー。対比カードは左右で逆の極性
- [ ] 簡体字・英字なし、背景が不透明
- [ ] 記事の文言から外れていない（独自の理由づけなし）
- [ ] 顔アイコン・小さなキャラが指定の大きさ。キャラなしのコマにキャラ・吹き出しがない
- [ ] 図の部品（人物・バー・領域・タグ）の色が指定どおり（意味のない青・赤・緑・ピンクがない）。人物の頭の上に余計な印がない
- [ ] 台詞の綴りが一字一句正本どおり（特に「原則」「まとめて」など崩れやすい語）

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-07 v03：コマ3で藍子の手が3本になった（指さす腕＋胸の前で組んだ手）ため、各コマのPANEL行に藍子の手の割り当て（hands:）を追加し、人体構造の段落に「手の割り当てルール（指さすときは片腕だけ、もう一方の手は組む・上げる・握るをしない）」を加えた（全プロンプト共通）
- 2026-10-07 v02：①コマ2の「二筆」の両方に仮差押えのリボンを付ける（v01は消えていた）／②コマ2のトリ先生の吹き出しを3行（いいえ。／一筆を複数に区分する／物理的な変更にすぎないのよ）に固定／③コマ3の矢印を「各土地の登記記録に引き継ぐ（転写）」に併記／④コマ4の下に注記（抵当権など所有権以外の権利を消滅させるときは承諾が必要・法40条。ユーザー指示。法40条は記事に無いので「記事に無い条文」に記録）／⑤藍子の人体構造（腕2本・手2本・指5本）とコマごとのポーズ変更、記事内容の理解に必要な要素の表現を全プロンプトに追加
- 2026-10-07 v01：初版
