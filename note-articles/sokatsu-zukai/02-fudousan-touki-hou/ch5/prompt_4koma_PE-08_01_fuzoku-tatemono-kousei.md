# D1687 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）の、論点【PE-8】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PE-08_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1687（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 R03-Q15ウ）。正解＝D1687＝〇（正しい記述）。
- 記事：`note-articles/r3-mondai/q15-tatemono-henkou-kousei.md` ウ（R03：甲建物の附属建物の床面積についての表題部の更正の登記をするときは、附属建物の表示に関する表題部に附属建物の種類、構造及び更正後の床面積の全部を記録し、符号を除いた従前の登記事項の全部を抹消する。不動産登記事務取扱手続準則94条1項。床面積だけの更正でも、数字だけ書き換えるのではなく、その附属建物の種類・構造・更正後の床面積をひとまとまりで書き直し、符号を残して古い記録の一式を消す）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md 【PE-8】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『附属建物の種類、構造及び更正後の床面積の全部を記録し』『符号を除いた従前の登記事項の全部を抹消する』と、『全部』を2回重ねる。甲建物の附属建物の『床面積』の更正と明示してあるので、誤りは床面積だけのはずなのに『全部』を記録・抹消するのは言い過ぎだ、と読ませて×にさせる。
- 【受験者の勘違い・定着していない点】（推測）①更正は誤りの箇所だけを直すものと考え、床面積の更正なら床面積の数字だけを書き換えると想像する。②附属建物の表示は、種類・構造・床面積がひとまとまりの一式として記録される、という登記記録の見方が定着していない。③『符号を除く』の意味が分からず、符号まで消えるのか、残るのかが曖昧になる。
- 【対比する制度】「数字だけ書き換える」⇔「ブロックごと書き換える」：誤っていた箇所だけを直すのではなく（受験者の想像）、附属建物の種類・構造・更正後の床面積の全部を記録し、符号を除く従前の登記事項の全部を抹消する（準則94条1項。更正でも変更でも同じ記録のしかた）。誤りが一か所でも、結論の書き方が逆になる点。
- 【型の選び方】型：型1（思い込み→押さえどころ→違い→結論）。理由：壁＝『更正は誤った箇所だけ直す』という感覚。誤解の型がはっきりしているので、コマ1で藍子の思い込みを出し、コマ2で『数字だけ書き換える』と『ブロックごと書き換える』を左右のカードで対比し、コマ3で記録するもの・抹消するもの・残るもの（符号）の3枚で中身を示し、コマ4で暗記3点にした。『なぜ一式を書き直すのか』の理由は、準則の文言も記事も定めるだけで理由を述べていないので、図には入れていない（型3にしなかった理由）。同じ論点の既存の4コマ（変更の登記が要る範囲）は型3の対比（登記事項が変わるか）で、扱う肢も壁も違う。
- コマごとに読者が言えること：コマ1＝この肢は、附属建物の床面積の更正の登記を、表題部にどう記録するかを問うている。コマ2＝数字だけ書き換えるのではなく、ブロックごと書き換える。コマ3＝更正後の種類・構造・床面積の全部を記録し、従前の事項は符号を除いて全部抹消する。コマ4＝この肢は〇。
- 記事の範囲：R03-Q15ウ（準則94条1項。『附属建物の床面積だけを更正する場合でも、床面積の数字だけ書き換えるのではなく、その附属建物の種類・構造・更正後の床面積をひとまとまりで書き直し、符号を残して古い記録の一式を消す』）。同じ記事のア（附属建物の新築の年月日の更正は表題部所有者も申請できる）・イ（変更と更正が混在するときの登記の目的）は図に入れていない。
- extra_refs：不動産登記事務取扱手続準則94条1項・3項（法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md の第94条で原文を確認。1項『附属建物の種類、構造又は床面積に関する変更の登記又は更正の登記をする場合において、表題部に附属建物に関する記録をするときは、当該附属建物の変更後又は更正後の種類、構造及び床面積の全部を記録し、従前の登記事項（符号を除く。）の全部を抹消するものとする。』）。3項（符号欄に従前の符号を記録）は図に番号を出さず、『符号を残す』という記事の言い方にそろえた。
- 同じ論点の他の肢（図に入れない理由）：D0333（改修でも登記事項が変わらなければ不要・×）は既存の4コマ（変更の範囲）が扱う。D0334（増築部分の帰属・付合）、D1371（非区分建物に接続した区分建物の新築）、D1779（再築）、D1576（附属建物の所有権証明情報）、D1959（共有建物の変更の単独申請）は、壁がそれぞれ別（付合、一括申請、滅失と新築、添付情報、保存行為）で、この対比と同居させると焦点がぼけるので入れていない。
- 登場人物：当事者の人型は使わず、登記記録の表示は文字のカードで示す。数値の例は入れず、種類・構造・床面積の項目名だけで示す。
- 矢印の意味：矢印は使わない。コマ1は縦のカード、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（コマ2の左は受験者の想像の説明で、〇×の対比ではなく書き方の対比）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 附属建物の更正は、一式を書き直す | 「一式を書き直す」を黄色マーカー |
| コマ1 見出し | ラベル | ①　床面積の更正は、どう記録する？ | — |
| コマ1 図 | 図・カード | 甲建物の附属建物 / 床面積が、登記のときから間違っていた / 更正後の種類、構造、床面積の全部を記録するとする / 肢D1687：附属建物の床面積の更正は、どう記録する？ | — |
| コマ1 | 藍子（左・先に話す） | 床面積だけ直すなら、数字だけ書き換えですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。直す箇所だけとは限らないの | 「直す箇所だけ」 |
| コマ2 見出し | ラベル | ②　数字だけか、ブロックごとか | — |
| コマ2 図 | 図・カード | 附属建物の更正の登記 / 記録のしかたが決まっている / 数字だけ書き換える / 受験者の想像 / 誤っていた床面積だけを直す / 種類と構造は、そのまま / ブロックごと書き換える / 準則94条1項 / その附属建物の一式を書き直す / 更正でも、変更でも同じ / 肢D1687は、右の話 | — |
| コマ3 見出し | ラベル | ③　何を記録し、何を消すのか | — |
| コマ3 図 | 図・カード | 記録するもの / 更正後の種類、構造 / 更正後の床面積 / 抹消するもの / ひっかけ：直す箇所だけ書き換える / 従前の登記事項の全部 / ただし、符号を除く / 残るもの / 符号 / 附属建物を見分ける番号は、そのまま | — |
| コマ3 | 藍子（左・1番目） | 直すのは床面積だけなのに、全部ですか？ | — |
| コマ3 | トリ先生（右・2番目） | そう。種類と構造も、書き直すのよ | 「書き直す」 |
| コマ3 | 藍子（左・3番目） | 古い記録は、どうなるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 符号以外は、全部抹消するの | 「符号以外」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 一か所の誤りでも、一式を書き直すんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。残るのは、符号だけよ | 「符号だけ」 |
| コマ4 チェック欄 | 3項目（青✓） | 附属建物の更正は、更正後の種類、構造及び床面積の全部を記録する（肢D1687は〇） / 従前の登記事項は、符号を除いて全部抹消する / 変更の登記でも、同じ記録のしかた（準則94条1項） | — |
| 結論帯 | 1行目 | 附属建物の更正は、一式を書き直す | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1687　正解〇（R03-Q15ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記事務取扱手続準則94条1項（附属建物の種類、構造又は床面積に関する変更の登記又は更正の登記をする場合の記録方法）。法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md の第94条で原文と照合済み。記事（R03-Q15ウ）が94条1項を引いている

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed (cartoon expression marks such as ！ and ？ beside a character's face are decoration, not text, and are allowed).

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

CHARACTER SIZE POLICY: draw 藍子 and トリ先生 as large and as clear as the layout allows, at the size given in each PANEL line. Never shrink a character just to make it small or to leave empty space, and never draw a character at the smallest possible size by default (this happens most often in panel 1). Reduce a character's size ONLY when the diagram, the cards, or the speech bubbles of that panel genuinely do not fit otherwise, and then reduce it only as much as needed, keeping the face large enough to read the expression. Characters become icon-sized only in a panel whose PANEL line explicitly asks for face icons.

EXPRESSION MARKS (allowed): small cartoon expression marks and effects around the characters, such as ！, ？, sweat drops, sparkles, anger marks, hearts, surprise lines, and thought dots, may appear whenever they match a character's emotion, in any soft color (these marks are exempt from the color rule for YES/NO marks). They are decoration: they are not part of the given text and not part of the YES/NO mark system, so they are NEVER counted as extra text, extra marks, or errors, and nothing is deleted, redrawn, or regenerated because of them. They must stay small, must not cover any given text or diagram, and must not be drawn as a check mark or a cross on a card.

SINGLE PASS: generate the image once. The checklists in this prompt, including the final check at the end, are guides to apply silently while drawing. After the image is produced, do not audit it again, do not list or announce defects (for example an extra or unexpected mark or symbol), and do not delete, redo, or regenerate any part of it; deliver the first image as it is.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both smaller than normal; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「附属建物の更正は、一式を書き直す」 in large bold letters; the part 「一式を書き直す」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　床面積の更正は、どう記録する？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「甲建物の附属建物」. Card 2: 「床面積が、登記のときから間違っていた」. Card 3: 「更正後の種類、構造、床面積の全部を記録するとする」.
- At the top, a small question badge in a gray fill with dark navy text 「肢D1687：附属建物の床面積の更正は、どう記録する？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「床面積だけ直すなら、
数字だけ
書き換えですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
直す箇所だけとは
限らないの」 with the part 「直す箇所だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　数字だけか、ブロックごとか」
- A small dark navy tag 「附属建物の更正の登記」 at the top left, with one line beside it: 「記録のしかたが決まっている」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「数字だけ書き換える」, a small tag 「受験者の想像」, two body lines: 「誤っていた床面積だけを直す」, 「種類と構造は、そのまま」.
- Right card, heading 「ブロックごと書き換える」, a small tag 「準則94条1項」, two body lines: 「その附属建物の一式を書き直す」, 「更正でも、変更でも同じ」, with the heading highlighted with a yellow marker.
- Under the two cards, one wide dark navy band with large white text 「肢D1687は、右の話」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　何を記録し、何を消すのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「記録するもの」, two body lines 「更正後の種類、構造」 and 「更正後の床面積」, with the heading highlighted with a yellow marker.
- Card 2, heading 「抹消するもの」, a dark navy ribbon tag with large white text 「ひっかけ：直す箇所だけ書き換える」, two body lines 「従前の登記事項の全部」 and 「ただし、符号を除く」.
- Card 3, heading 「残るもの」, two body lines 「符号」 and 「附属建物を見分ける番号は、そのまま」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「直すのは床面積だけ
なのに、全部ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「そう。
種類と構造も、
書き直すのよ」 with the part 「書き直す」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「古い記録は、
どうなるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「符号以外は、
全部抹消するの」 with the part 「符号以外」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「一か所の誤りでも、
一式を書き直すんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
残るのは、
符号だけよ」 with the part 「符号だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「附属建物の更正は、更正後の種類、構造及び床面積の全部を記録する（肢D1687は〇）」, 「従前の登記事項は、符号を除いて全部抹消する」, 「変更の登記でも、同じ記録のしかた（準則94条1項）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「附属建物の更正は、一式を書き直す」 with a yellow highlighter marker.
- Line 2: 「問題D1687　正解〇（R03-Q15ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 建, 所, 物, 番, 登, 肢, 解, 記, 違, 録, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「数字だけ書き換える」 and the right card has the heading 「ブロックごと書き換える」, never swapped; confirm that the three cards of panel 3 are in the order 記録するもの, 抹消するもの, 残るもの, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編⑤_4コマ8_附属建物の更正は、一式を書き直す.png`
- 途中の版・不採用の版：`不動産登記法編⑤_4コマ8_附属建物の更正は、一式を書き直す_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/prompt_4koma_PE-08_01_fuzoku-tatemono-kousei.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『附属建物の床面積の更正を表題部にどう記録するか』を問う肢だと分かり、コマ2で数字だけ書き換えるのではなくブロックごと書き換えること、コマ3で何を記録し何を抹消し何が残るかが言える
- [ ] 工程C：構成表の全文言を記事（R03-Q15ウ）と法令DB（準則94条1項）に突き合わせ済み。『なぜ一式を書き直すのか』の理由づけは図に入れていない（準則にも記事にも明記がない）。準則94条2項（原因欄の欄番号）と3項（符号欄）は図に番号を出していない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない。既存の4コマ（D0333の変更の範囲）とは肢・壁・対比が違う
- [ ] 工程C：肝の確認：①附属建物の更正は、誤りが床面積だけでも、更正後の種類・構造・床面積の全部を記録する ②従前の登記事項は符号を除いて全部抹消し、符号は残る ③更正でも変更でも同じ記録のしかた ④この肢は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PE-08_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第5章【PE-8】用。型1。附属建物の更正は、誤りが床面積だけでも、更正後の種類・構造・床面積の全部を記録し符号を除く従前の事項を全部抹消する、という取扱いと、数字だけ書き換えるという想像の対比を組んだ。既存の4コマ〈変更の範囲・D0333〉とは別の肢）
