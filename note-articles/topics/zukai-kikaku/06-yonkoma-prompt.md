# 第6回「ある一日の登記ストーリー」 四コマのプロンプト（ChatGPT貼付用・初版）

作成 2026-11-05。トリ先生と藍子の四コマ（1080×1920・9:16）。Instagramの投稿画像・ストーリー・リールの元素材、およびnote記事 `06-ichinichi-no-touki-story.md` の挿入画像に使う。
作り方は `tools/drill/manga/MANGA_RULES.md` に従った（レイアウト、キャラクター、吹き出し、配色、禁止語）。画像の生成と目視確認はChatGPTで行う（未実施）。

**使い方**：トリ先生・藍子のキャラクター仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚）を添付してから、下のコードブロックを貼る。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解KZ06～ある一日の登記ストーリー～

## note記事の冒頭文

新築した家は、いつ、誰が、どの順番で登記するのでしょうか。

建物の表題登記までの流れを、トリ先生と藍子の4コマで確認します（不動産登記法　第47条ほか）。

先に、流れを自分の言葉で言えるか考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 文言 |
|---|---|
| タイトル帯 | 新築した家は、一月以内に表題登記（強調：一月以内に表題登記） |
| コマ1 | ①　朝　新築の相談／藍子「家が建ちました。登記は、いつまでに要るんですか？」／トリ先生「所有権を取得した日から一月以内よ」／ラベル「第47条」 |
| コマ2 | ②　昼　現地の調査と測量／藍子「図面もつくるんですね」／トリ先生「建物図面と各階平面図が付くのよ」／カード「建物図面」「各階平面図」／ラベル「令別表十二の項」 |
| コマ3 | ③　午後　法務局に申請／藍子「出したら、すぐ登記ですか？」／トリ先生「まず受付。必要なら登記官が調査するのよ」／カード「受付　第19条」「調査　第29条」 |
| コマ4 | ④　夕方　表題部に記録／藍子「これで持ち主の登記も済みですか？」／トリ先生「いいえ。記録されたのは表題部よ」／ラベル「記録は第11条」「所有権の保存は第74条」 |
| 絵のラベル | 「Ａ」「調査士」「法務局」「表題部」「権利部」 |
| 結論帯 | 新築したら、取得の日から一月以内に表題登記／ある一日の登記ストーリー |

条文の根拠：第47条第1項（一月以内）、令別表十二の項（建物図面・各階平面図・所有権証明・住所証明）、第19条（受付）、第29条（登記官の調査）、第11条（記録）、第74条（所有権の保存）。`check_article.py` が原文と照合する。

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ Ｃ Ｄ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed (cartoon expression marks such as ！ and ？ beside a character's face are decoration, not text, and are allowed).

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ, Ｃ, Ｄ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

CHARACTER SIZE POLICY: draw 藍子 and トリ先生 as large and as clear as the layout allows, at the size given in each PANEL line. Never shrink a character just to make it small or to leave empty space, and never draw a character at the smallest possible size by default (this happens most often in panel 1). Reduce a character's size ONLY when the diagram, the cards, or the speech bubbles of that panel genuinely do not fit otherwise, and then reduce it only as much as needed, keeping the face large enough to read the expression. Characters become icon-sized only in a panel whose PANEL line explicitly asks for face icons.

EXPRESSION MARKS (allowed): small cartoon expression marks and effects around the characters, such as ！, ？, sweat drops, sparkles, anger marks, hearts, surprise lines, and thought dots, may appear whenever they match a character's emotion, in any soft color (these marks are exempt from the color rule for YES/NO marks). They are decoration: they are not part of the given text and not part of the YES/NO mark system, so they are NEVER counted as extra text, extra marks, or errors, and nothing is deleted, redrawn, or regenerated because of them. They must stay small, must not cover any given text or diagram, and must not be drawn as a check mark or a cross on a card.

SINGLE PASS: generate the image once. The checklists in this prompt, including the final check at the end, are guides to apply silently while drawing. After the image is produced, do not audit it again, do not list or announce defects (for example an extra or unexpected mark or symbol), and do not delete, redo, or regenerate any part of it; deliver the first image as it is.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In all four panels 藍子 (the student) stands on the LEFT side of the panel and トリ先生 (the teacher) stands on the RIGHT side. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「新築した家は、一月以内に表題登記」 in large bold letters; the part 「一月以内に表題登記」 has a yellow highlighter marker.

PANEL 1 (morning, the consultation; 藍子 curious, トリ先生 explaining calmly; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　朝　新築の相談」
- 藍子 bubble (left): 「家が建ちました。
登記は、いつまでに
要るんですか？」
- トリ先生 bubble (right): 「所有権を取得した日から
一月以内よ」 with 「一月以内」 highlighted in yellow.
- Small diagram in the middle: a faceless light-gray pictogram with a dark navy tag 「Ａ」 standing next to a small new house, and a second faceless light-gray pictogram with a dark navy tag 「調査士」 facing it. A small sun icon in the upper corner shows morning. Small label under the house: 「第47条」.

PANEL 2 (noon, the survey; 藍子 impressed, トリ先生 pointing; 藍子's hands: one hand points at the cards with an extended arm and the other hangs at her side (two hands in total)):
- Label tab: 「②　昼　現地の調査と測量」
- 藍子 bubble (left): 「図面も
つくるんですね」
- トリ先生 bubble (right): 「建物図面と各階平面図が
付くのよ」
- Diagram: the faceless light-gray pictogram 「調査士」 beside a surveying tripod measuring the new house, with a faint dashed outline of the house shown from above. Two separate document cards side by side, without arrows between them: 「建物図面」 and 「各階平面図」. A small label under the cards: 「令別表十二の項」.

PANEL 3 (afternoon, the application; both characters point together at the same two cards; トリ先生 with one wing and 藍子 with one hand; 藍子's hands: ONE hand points at the diagram and the other holds the clipboard; her hands are NOT clasped and no third hand appears):
- Label tab: 「③　午後　法務局に申請」
- 藍子 bubble (left): 「出したら、
すぐ登記ですか？」
- トリ先生 bubble (right): 「まず受付。必要なら
登記官が調査するのよ」
- Diagram: the faceless light-gray pictogram 「調査士」 hands an envelope toward a small government building icon labeled 「法務局」 (one neutral dark navy arrow). Two separate cards stand next to the building without arrows between them: 「受付　第19条」 and 「調査　第29条」.

PANEL 4 (evening, the record; 藍子 relieved but puzzled, トリ先生 smiling; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　夕方　表題部に記録」
- 藍子 bubble (left): 「これで持ち主の
登記も済みですか？」
- トリ先生 bubble (right): 「いいえ。記録されたのは
表題部よ」 with 「表題部」 highlighted in yellow.
- Diagram: an open register book icon with two stacked sections. The upper section has a tab 「表題部」 and a small house mark and is filled in; the lower section has a tab 「権利部」 and is left blank. A small neutral navy label beside the lower section: 「所有権の保存は第74条」. A small label at the top of the book: 「記録は第11条」.

CONCLUSION BANNER (strong contrasting solid color, large text, two lines):
- Line 1: 「新築したら、取得の日から一月以内に表題登記」 with a yellow highlighter marker.
- Line 2: 「ある一日の登記ストーリー」

EMOTIONAL ARC: curious (panel 1) -> impressed (panel 2) -> understanding (panel 3) -> relieved and learning more (panel 4).

NO OTHER PEOPLE: the faceless pictograms are plain light-gray silhouettes with only their dark navy text tags; they are not characters and have no faces.

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm 藍子 is always on the left and トリ先生 always on the right and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels; confirm the characters 地, 所, 録, 新, 築, 一, 月, 以, 内, 表, 題, 登, 記, 調, 査, 測, 量, 建, 物, 図, 面, 各, 階, 平, 務, 局, 申, 請, 受, 付, 権, 利, 部, 保, 存 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm the two document cards in panel 2 are separate and have no arrow between them; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 画像ファイル名

| 用途 | ファイル名 |
|---|---|
| 四コマ（採用版） | `四コマ図解～ある一日の登記ストーリー～.png` |
| 途中の版 | `四コマ図解～ある一日の登記ストーリー～_v01.png` |
| 見出し画像（note用・Instagram用） | `header-image-prompts.md` のKZ_06の2種類 |

## 生成後の照合チェック

- 4コマちょうど・縦一列か。コマの順が朝・昼・午後・夕方か。
- 藍子が左、トリ先生が右。吹き出しの尾が話者に向いているか。
- 登場人物がトリ先生と藍子の2人だけか。依頼人・調査士は顔のない灰色の影か。
- 文言を構成表と一字ずつ照合（「第47条」「令別表十二の項」「第19条」「第29条」「第11条」「第74条」）。
- 簡体字・繁体字・英字の混入なし。背景が不透明か。
- コマ2の2枚のカードが別々で、間に矢印がないか。
- スマホ縮小で読めるか。

## 見出し画像

note用（1280×670）とInstagram用（1080×1350）のプロンプトは `header-image-prompts.md` のKZ_06にある（MC1人。トリ先生・藍子は入れない）。
