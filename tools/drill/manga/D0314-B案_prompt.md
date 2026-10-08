# D0314 4コマ解説図解 プロンプト（ChatGPT貼付用・B案v01）

- 肢：D0314（民法／用益権・担保物権、出典 H20-Q01イ）。正解＝×（誤った記述）。誤解未習得2回（？が2回連続）。
- 記事：`note-articles/h20-mondai/q01-fudousan-shichi.md` イ「不動産質でも、設定者の承諾なく転質ができる」（B案：しくみの図解と、間違えないための押さえどころで組む）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【B案の位置づけ】A案（`D0314_prompt.md`）は定型の「ひっかけと勘違い」のコマで組んだが、画像を見たユーザーから「不動産質権・転質のしくみそのものが分かりにくい」との指摘があり（2026-10-09）、定型を外して組み直した別パターン。ねらいは、『D0314をもう間違えないために、どこを押さえればいいか』が1枚で伝わること。A案とは別ファイル・別の採用版名（`_B案`）で試作し、採用するほうを後で決める。
- 【定型からの変更点】①「ひっかけと勘違い」の対比カード（赤✕・青✓の左右カード）を使わない。②コマ1を「出題の事案」ではなく、転質の「しくみ」を2段の関係図で見せるコマにする（質権の設定①→転質②。誰が誰に何をするかを先に分からせる）。③コマ2を「承諾と責任はセット」の押さえどころカードにする（承諾はいらない、そのかわり責任は重い）。④コマ3を「本番での読み方3ステップ」にして、問題文のどこを見て判断するかを示す。⑤コマ4は暗記3点と結論。
- 押さえどころ（記事の範囲）：(1) 転質は、質権者が、質権の存続期間内に、自己の責任で、質物にさらに質権を設定すること（民法348条、責任転質）。(2) 設定者の承諾は不要。(3) そのかわり、転質で生じた損失は不可抗力によるものまで質権者が責任を負う。(4) 記事のまとめ：『承諾がいる／いらない』を問う肢（イ・ウ）が、両方とも『いらない』側に倒れるのがこの問題の急所。
- 記事の具体例を使う：Ａが別荘に質権を設定してＢからお金を借りている（ウの例：賃貸アパートに質権を設定してお金を借りる、と同じ型）。Ｂが、自分がＣからお金を借りるとき、Ａに断らなくても、その別荘の質権をＣへの担保に使える（イの例）。
- 登場人物：Ａ（設定者・別荘の持ち主）・Ｂ（質権者）・Ｃ（Ｂにお金を貸す人）を、コマ1で人型タグ付きで左から順に紹介する。
- 矢印の意味：コマ1の2本の矢印は、どちらも『担保として質権を設定する』という同じ意味（①ＡからＢへ、②ＢからＣへ）。売買・お金の動き・申請の矢印はない。コマ2・3は矢印を使わない。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。人物は全員同じ薄い灰青、カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝small（2段の関係図を大きく）、コマ2＝none（承諾と責任のセットカードだけ）、コマ3＝faces（顔アイコンの会話＋3ステップのカード）、コマ4＝両方。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0314～H20-Q01イ～

## note記事の冒頭文

不動産質権を持つ質権者が、その不動産についてさらに転質をしたいと考えています。転質をするには、設定者の承諾を得なければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成20年度　第1問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 転質は承諾いらず。そのかわり責任は重い | 「そのかわり責任は重い」を黄色マーカー |
| コマ1 見出し | ラベル | ①　転質のしくみ | — |
| コマ1 図 | 図・カード | Ａ / 設定者（別荘の持ち主） / Ｂ / 質権者 / Ｃ / Ｂにお金を貸す人 / Ａの別荘 / Ｂの質権 / ①　質権の設定 / ②　転質（さらに質権を設定） / Ａは別荘に質権を設定して、Ｂからお金を借りる / Ｂは、自分がＣからお金を借りるとき、その別荘の質権をＣへの担保に使う / ②に、Ａの承諾は要る？ | — |
| コマ1 | 藍子（左・先に話す） | 転質って、誰が誰に何をするんですか？ | — |
| コマ1 | トリ先生（右・答える） | Ｂが自分の質権を使って、Ｃから借りるのよ | 「Ｃから借りる」 |
| コマ2 見出し | ラベル | ②　承諾と責任はセット | — |
| コマ2 図 | 図・カード | 押さえどころ / 承諾は不要。引き換えに、責任が重くなる / 責任が重くなる / セット / できること / 民法348条 / Ａの承諾なしで、転質ができる（責任転質） / 負う責任 / 転質で生じた損失について、不可抗力によるものまで責任を負う / 質権の存続期間内に、自己の責任で、質物にさらに質権を設定する | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　転質の場面か / 質権者が、質物にさらに質権を設定している / ステップ2　承諾の文言を見る / 承諾を得なければ、と書かれていたら、不動産質では要らない側。この問のイもウも、要らない / ステップ3　責任の文言を見る / 責任の肢は、質権者が不可抗力まで負う、が正しい内容 | — |
| コマ3 | 藍子（左・1番目） | 要る・要らないは、どう見分けますか？ | — |
| コマ3 | トリ先生（右・2番目） | 不動産質は、転質も使用収益も要らないの | 「要らない」 |
| コマ3 | 藍子（左・3番目） | 転質に、歯止めはないんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 不可抗力まで、質権者が責任を負うのよ | 「不可抗力まで」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 承諾なしで転質できる、と覚えます！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。ただし責任は不可抗力まで重いわよ | 「不可抗力まで」 |
| コマ4 チェック欄 | 3項目（青✓） | 転質は、質権者が自己の責任で、質物にさらに質権を設定すること（民法348条） / 転質に、設定者の承諾は不要 / 損失は、不可抗力によるものまで質権者が責任を負う | — |
| 結論帯 | 1行目 | 転質は承諾いらず。そのかわり責任は重い | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0314　正解×（H20-Q01イ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, or show both very small; in that case follow the PANEL line, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character is only a small face icon and the bubbles form a rally of short alternating lines. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「転質は承諾いらず。そのかわり責任は重い」 in large bold letters; the part 「そのかわり責任は重い」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear VERY SMALL (each about 110 px tall in total, clearly smaller than the full-size characters in the other panels, never more than one third of the panel height), 藍子 at the lower left corner and トリ先生 at the lower right corner, so that the diagram or the items to memorize fill the panel; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　転質のしくみ」
- A large two-step relation diagram fills the panel, laid out ONE row from left to right: three faceless pictogram tags in the same light gray-blue color with dark navy tags: 「Ａ」 (small label 「設定者（別荘の持ち主）」), 「Ｂ」 (small label 「質権者」), 「Ｃ」 (small label 「Ｂにお金を貸す人」).
- Above the row, between Ａ and Ｂ, stands one flat villa icon labeled 「Ａの別荘」 carrying a dark navy ribbon with white text 「Ｂの質権」 (the same dark navy ribbon in every panel).
- Two dark navy arrows with the SAME meaning (each arrow means setting up a pledge as security, not a sale and not a payment): arrow ① from Ａ to Ｂ labeled 「①　質権の設定」, and arrow ② from Ｂ to Ｃ labeled 「②　転質（さらに質権を設定）」.
- Under arrow ①, a white card with a dark navy outline: 「Ａは別荘に質権を設定して、Ｂからお金を借りる」. Under arrow ②, a white card with a dark navy outline: 「Ｂは、自分がＣからお金を借りるとき、その別荘の質権をＣへの担保に使う」.
- A small question badge 「②に、Ａの承諾は要る？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「転質って、
誰が誰に何を
するんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「Ｂが自分の質権を使って、
Ｃから借りるのよ」 with the part 「Ｃから借りる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　承諾と責任はセット」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「押さえどころ」 at the top left and a line beside it: 「承諾は不要。引き換えに、責任が重くなる」, with the part 「責任が重くなる」 in a yellow highlighter marker.
- Two large cards side by side, both with the same pale gray fill, a dark navy outline, and a dark navy heading, joined in the middle by a small plain dark navy label 「セット」 (a label only, no arrow). Left card, heading 「できること」, small tag 「民法348条」, body 「Ａの承諾なしで、転質ができる（責任転質）」. Right card, heading 「負う責任」, body 「転質で生じた損失について、不可抗力によるものまで責任を負う」.
- At the bottom, one wide dark navy band with white text 「質権の存続期間内に、自己の責任で、質物にさらに質権を設定する」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as very small round face icons (heads only, each about 80 px across, never larger than one fifth of the panel height, no bodies and no hands): the face icon of 藍子 sits at the left edge and the face icon of トリ先生 at the right edge of the panel; each speech bubble tail points to the face icon of its own speaker, and the bubbles form a rally of short alternating lines stacked from top to bottom (藍子 first), so that the large diagram or the large explanation card fills the panel):
- Label tab: 「③　本番での読み方3ステップ」
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross.
- Step card 1: heading 「ステップ1　転質の場面か」, body 「質権者が、質物にさらに質権を設定している」.
- Step card 2: heading 「ステップ2　承諾の文言を見る」, body 「承諾を得なければ、と書かれていたら、不動産質では要らない側。この問のイもウも、要らない」.
- Step card 3: heading 「ステップ3　責任の文言を見る」, body 「責任の肢は、質権者が不可抗力まで負う、が正しい内容」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, rally 1 of 4): 「要る・要らないは、
どう見分けますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, rally 2 of 4): 「不動産質は、転質も
使用収益も要らないの」 with the part 「要らない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, rally 3 of 4): 「転質に、歯止めは
ないんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, rally 4 of 4): 「不可抗力まで、
質権者が責任を負うのよ」 with the part 「不可抗力まで」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「承諾なしで転質できる、
と覚えます！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
ただし責任は
不可抗力まで重いわよ」 with the part 「不可抗力まで」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark: 「転質は、質権者が自己の責任で、質物にさらに質権を設定すること（民法348条）」, 「転質に、設定者の承諾は不要」, 「損失は、不可抗力によるものまで質権者が責任を負う」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「転質は承諾いらず。そのかわり責任は重い」 with a yellow highlighter marker.
- Line 2: 「問題D0314　正解×（H20-Q01イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 承, 抗, 押, 権, 物, 番, 肢, 解, 諾, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the face icons and the very small characters are drawn at the specified small sizes (they must not grow and squeeze the diagram) and that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 不動産質の質権者が転質 | 薄い黄色のマーカー |
| タイトル2行目 | 設定者の承諾は要る？ | 「承諾は要る？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0314　H20-Q01イ | — |

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
不動産質の質権者が転質
Line 2 is larger; the phrase 承諾は要る？ is red-orange and the rest is dark navy:
設定者の承諾は要る？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0314　H20-Q01イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small villa house with a plain ribbon tag and a faceless silhouette beside it
Right side: two blank document sheets passing from one hand to another hand

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 不, 動, 産, 質, 権, 者, 転, 設, 定, 承, 諾, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0314～H20-Q01イ～_B案.png |
| 見出し画像（採用版） | 4コマ解説図解D0314～H20-Q01イ～_B案_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0314～H20-Q01イ～_B案_v01.png ／ 4コマ解説図解D0314～H20-Q01イ～_B案_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0314-B案_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の2本の矢印がどちらも『担保として質権を設定する』で、Ａ→Ｂ→Ｃの2段になっている。この図だけで、転質は『Ｂが自分の質権をＣへの担保に使うこと』と言える
- [ ] 工程C：押さえどころ4つ（転質の意味・承諾不要・責任は不可抗力まで・承諾の肢は『いらない』側）が、コマ1・2・3・4のどこかに図か文言で必ずある
- [ ] 工程C：構成表の全文言を記事（H20-Q01イ）と突き合わせ：「民法348条」「責任転質」「自己の責任で」「不可抗力によるものまで」「イ・ウが両方いらない側」
- [ ] 工程C：コマ3の3ステップが、本番の問題文の読み方（転質の場面か→承諾の文言→責任の文言）として、順番に使える。結論は×（承諾を得なければ転質できないという記述が誤り）

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

## B案v01：新規作成（2026-10-09）。A案の画像を見たユーザーから「不動産質権・転質のしくみが分かりにくい。『ひっかけと勘違い』を使うことにこだわらず、この問題をもう間違えないために押さえるところが伝わる構成にしてほしい」との指示を受けて作成。定型（事案→ねらい→ひっかけ・勘違い→結論）を外し、しくみの図解→承諾と責任のセット→本番での読み方3ステップ→暗記3点、で組んだ。ChatGPTでの画像生成・検品はまだ（ユーザーが試作する）。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-09 B案v01：初版（D0314のA案と別パターンの構成表・プロンプト本体2）
