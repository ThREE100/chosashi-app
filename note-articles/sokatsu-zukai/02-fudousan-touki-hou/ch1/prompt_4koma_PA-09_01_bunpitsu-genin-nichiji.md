# D1036 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第1章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch1.md`）の、論点【PA-9】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PA-09_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1036（不動産登記法／申請総論（申請情報・登記原因及びその日付）、出典 H27-Q06イ）。正解＝D1036＝〇（正しい記述）。
- 記事：`note-articles/h27-mondai/q06-tochi-hyouji-tenpu.md` イ（H27：地積の変更の登記と分筆の登記を一の申請情報で申請するとき、登記原因とその日付を書くのは地積の変更の登記についてだけ。分筆は形成的な登記で、そもそも登記原因が存在しない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『地積の変更の登記についてのみ』と、原因と日付を書く登記を1つに絞って言い切る。『一の申請情報で二つの登記を申請するのだから、二つとも原因と日付を書くはず』と考えた受験者は、『のみ』を書き漏れの記述だと読み、×にしてしまう。
- 【受験者の勘違い・定着していない点】（推測）①登記原因とその日付は、どの登記の申請情報にも書くものだと一括りにする。②地積の変更は実際に起きた事実（例：一部海没）があるので日付も書くが、分筆は人為的に一筆を区切る登記で、原因の事実そのものがないことを区別できない。③一の申請情報にまとめても、登記ごとに書くことは変わらない点が結びつかない。
- 【対比する制度】「地積の変更の登記」⇔「分筆の登記」：地積の変更の登記は、変わった事実の原因とその日付を書き、登記記録にも実際の年月日が記録される（準則73条。結論が逆になる点）／分筆の登記は、人為的に一筆を区切る形成的な登記で、書くべき原因の事実と日付がなく、登記記録には『何番何、何番何に分筆』と記録される（準則74条）。
- 【型の選び方】型：型3（理由説明）。理由：『地積の変更には書く、分筆には書かない』と結論だけ覚えても、『どの登記にも原因を書く』という感覚が残ると崩れる。なぜ書かないのか（分筆は人が区切るだけで、記録すべき原因の事実がない）を、コマ3の理由のカードに置いた。コマ1は二つの登記の事案、コマ2は準則73条・74条の記録の仕方の左右の対比。壁＝『原因と日付はどの登記にも書く、という一括り』。
- コマごとに読者が言えること：コマ1＝一の申請情報で、地積の変更と分筆を申請するとき、原因と日付をどの登記に書くかを問うている。コマ2＝地積の変更は実際の年月日を書き、分筆は年月日を伴わない。コマ3＝地積の変更は事実を記録する登記、分筆は人が区切る形成的な登記だから、日付がない。コマ4＝地積の変更の登記についてだけ書く。この記述は〇。
- 記事の範囲：H27-Q06イ（分筆は形成的な登記で、そもそも登記原因が存在しない。準則74条の記録は『何番何、何番何に分筆』、準則73条の記録は『令和何年何月何日地目変更』のように実際の年月日を伴う）。総合記事②第1章【PA-9】の整理（形成的な登記には原因と日付を書かない）。『登記原因が存在しない』ことを直接定める条文は記事にもなく、準則の記録方法の違いからの裏付けと記事が説明している点は、図でも断定を避け、記事の言い方にそろえた。
- extra_refs：不動産登記事務取扱手続準則73条（地番、地目又は地積に関する変更の登記又は更正の登記をする場合の記録。例『②令和何年何月何日地目変更』）、74条（分筆の登記の記録方法。『①③何番何、何番何に分筆』『何番から分筆』）は、法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md で原文を確認。
- 登場人物：当事者の人型は使わず、二つの登記は文字のカードで示す。事例の当事者は出さない。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下のカードと理由のカード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと理由のカード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 分筆に、原因の日付は書かない | 「原因の日付」を黄色マーカー |
| コマ1 見出し | ラベル | ①　一の申請情報で、二つの登記 | — |
| コマ1 図 | 図・カード | 原因と日付は、どの登記に？ / 地積の変更の登記 / 崖崩れで海に沈み、地積が減った / 地積が変わった事実がある / 分筆の登記 / その土地を二つに分ける / 人が、一筆を区切る | — |
| コマ1 | 藍子（左・先に話す） | 原因と日付は、全部の登記に書きますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。全部に書く、は思い込みよ | 「全部に書く」 |
| コマ2 見出し | ラベル | ②　地積の変更と、分筆の記録 | — |
| コマ2 図 | 図・カード | 一の申請情報 / 原因と日付の扱いが分かれる / 地積の変更は、原因と日付を書く / 準則73条 / 例：令和○年○月○日一部海没 / 実際の年月日を記録する / 分筆は、原因と日付を書かない / 準則74条 / 「何番何、何番何に分筆 / 年月日は記録されない | — |
| コマ3 見出し | ラベル | ③　なぜ、分筆には書かないのか | — |
| コマ3 図 | 図・カード | 分筆にも、原因と日付を書く / どの登記にも書く、という思い込み / 書くのは、事実がある登記だけ / 分筆は、事実のない形成的な登記 / 原因と日付があるかどうか / 地積の変更：起きた事実を記録する / 分筆：人為的に区切る形成的な登記 / 記録すべき原因の日付がない / ひっかけ：どの登記にも原因を書く / どの登記にも | — |
| コマ3 | 藍子（左・1番目） | 分けた日を、書けばいいのでは？ | — |
| コマ3 | トリ先生（右・2番目） | 人が区切るだけで、事実がないの | 「事実がない」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 原因を書くのは、事実がある登記だけですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。分筆は、日付を書かないのよ | 「分筆は、日付を書かない」 |
| コマ4 チェック欄 | 3項目（青✓） | 地積の変更の登記には、原因とその日付を書く / 分筆の登記は形成的で、原因と日付を書かない / 一の申請情報でも、書くのは地積の変更だけ（この記述は〇） | — |
| 結論帯 | 1行目 | 原因と日付を書くのは、地積の変更だけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1036　正解〇（H27-Q06イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記事務取扱手続準則73条・74条。法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md と照合済み。記事（H27-Q06イ）が準則73条・74条を引いている

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

TITLE BANNER: text 「分筆に、原因の日付は書かない」 in large bold letters; the part 「原因の日付」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　一の申請情報で、二つの登記」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「原因と日付は、どの登記に？」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「地積の変更の登記」, heading 「崖崩れで海に沈み、地積が減った」, body 「地積が変わった事実がある」.
- Card 2: tag 「分筆の登記」, heading 「その土地を二つに分ける」, body 「人が、一筆を区切る」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「原因と日付は、
全部の登記に
書きますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
全部に書く、は
思い込みよ」 with the part 「全部に書く」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　地積の変更と、分筆の記録」
- A small dark navy tag 「一の申請情報」 at the top left, with one line beside it: 「原因と日付の扱いが分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「地積の変更は、原因と日付を書く」, a small tag 「準則73条」, two body lines: 「例：令和○年○月○日一部海没」, 「実際の年月日を記録する」, with the heading highlighted with a yellow marker.
- Right card, heading 「分筆は、原因と日付を書かない」, a small tag 「準則74条」, two body lines: 「「何番何、何番何に分筆」」, 「年月日は記録されない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、分筆には書かないのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「分筆にも、原因と日付を書く」, body 「どの登記にも書く、という思い込み」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「書くのは、事実がある登記だけ」, body 「分筆は、事実のない形成的な登記」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall card with a dark navy heading 「原因と日付があるかどうか」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「地積の変更：起きた事実を記録する」, 「分筆：人為的に区切る形成的な登記」, 「記録すべき原因の日付がない」. Under the three rows, one small dark navy ribbon tag with white text 「ひっかけ：どの登記にも原因を書く」, with the text 「どの登記にも」 highlighted with a yellow marker.
- The right card is a part of the right side, and it is NOT a speech bubble. The left cards and the right card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「分けた日を、
書けばいいのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「人が区切るだけで、
事実がないの」 with the part 「事実がない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「原因を書くのは、
事実がある登記
だけですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
分筆は、
日付を書かないのよ」 with the part 「分筆は、日付を書かない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「地積の変更の登記には、原因とその日付を書く」, 「分筆の登記は形成的で、原因と日付を書かない」, 「一の申請情報でも、書くのは地積の変更だけ（この記述は〇）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「原因と日付を書くのは、地積の変更だけ」 with a yellow highlighter marker.
- Line 2: 「問題D1036　正解〇（H27-Q06イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 番, 登, 解, 記, 請, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that the only red cross in the whole image is the one at the bottom of the top-left card of panel 3 and the only blue check marks are the one at the bottom of the bottom-left card of panel 3 and the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「地積の変更は、原因と日付を書く」 and the right card has the heading 「分筆は、原因と日付を書かない」, never swapped; confirm that the two cards of panel 1 are in the order 地積の変更の登記, 分筆の登記, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法編1_4コマ9_分筆に、原因の日付は書かない.png`
- 途中の版・不採用の版：`不登法編1_4コマ9_分筆に、原因の日付は書かない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch1/prompt_4koma_PA-09_01_bunpitsu-genin-nichiji.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で一の申請情報に二つの登記を入れていること、コマ2で地積の変更と分筆の記録の仕方の違い、コマ3で分筆に日付がない理由が言える
- [ ] 工程C：構成表の全文言を記事（H27-Q06イ）・法令DB（準則73条・74条）と突き合わせ済み。『分筆に原因が存在しない』は記事の整理にとどめ、条文で断定していない。令3条6号は図に入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①地積の変更の登記は、変わった事実の原因とその日付を書く ②分筆の登記は形成的な登記で、原因と日付を書かない ③一の申請情報にまとめても、書くのは地積の変更の登記についてだけ ④この記述は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PA-09_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第1章【PA-9】用。型3（理由説明）。地積の変更は原因と日付を書き分筆は書かない対比と、分筆には記録すべき事実がない理由を組んだ）
