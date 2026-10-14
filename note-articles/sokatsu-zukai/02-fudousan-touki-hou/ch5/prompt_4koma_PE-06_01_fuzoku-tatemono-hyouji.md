# D1778・D1382・D0979 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）の、論点【PE-6】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PE-06_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1778・D1382・D0979（不動産登記法／建物の認定・個数・種類構造床面積、出典 R04-Q14ウ／H30-Q14オ／H26-Q14エ）。正解＝D1778＝×（誤った記述）／D1382＝×（誤った記述）／D0979＝×（誤った記述）。
- 記事：`note-articles/r4-mondai/q14-fuzoku-tatemono.md` ウ（附属建物が別の一棟の区分建物なら、その一棟の所在地番を申請情報に書く）。ほか、H30-Q14オ（h30-mondai/q14-fuzoku-tatemono.md。同一の一棟に属する区分建物なら、一棟の表示の記録は不要）、H26-Q14エ（h26-mondai/q14-fuzoku-tatemono.md。同一の一棟でも、附属建物自体の構造・床面積の記載は省略できない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】3肢とも『要しない／要する』と、一棟の表示を書くかどうかを反対向きに言い切る。D1778は別の一棟なのに『要しない』、D1382は同一の一棟なのに『記録することを要する』、D0979は同一の一棟の省略（所在地番）に、附属建物自体の『構造及び床面積』を紛れ込ませる。
- 【受験者の勘違い・定着していない点】（推測）①『省略できるのは何か』を、附属建物自体の記載と一棟の表示の記載に分けていない。②準則89条は『同一の一棟に属するときの、一棟の表示の記録』の定めで、附属建物自体の構造・床面積を省略できる意味ではないことが定着していない。③別の一棟なら一棟の所在地番も要ることを落とす。
- 【対比する制度】「同じ一棟に属する」⇔「別の一棟に属する」：同じ一棟に属する附属建物は、一棟の所在・構造・床面積の記録を要しない（準則89条）／別の一棟に属する区分建物の附属建物は、その一棟の所在地番も申請情報に書く（法44条1項5号）（結論が逆になる点）。どちらでも、附属建物自体の種類・構造・床面積は省略できない。
- 【型の選び方】型：型5（整理カード併用。型1の思い込みと組み合わせ）。理由：結論の理由が『附属建物の表示で何を書き、何を省略できるか』という一覧の記憶なので、コマ2は『同じ一棟』と『別の一棟』の左右の対比、コマ3の右側は会話1往復と、附属建物の表示（所在・種類・構造・床面積）の整理カードにした。壁＝『一棟の表示』と『附属建物自体の表示』の取り違え。
- コマごとに読者が言えること：コマ1＝3つの肢は、附属建物が区分建物のときの『別の一棟』『同じ一棟の一棟の表示』『同じ一棟の附属建物自体』を問うている。コマ2＝同じ一棟なら一棟の表示は記録を要せず、別の一棟ならその一棟の所在地番も要る。コマ3＝附属建物自体の種類・構造・床面積は常に書く。コマ4＝D1778・D1382・D0979はいずれも×。
- 記事の範囲：R04-Q14ウ（法44条1項5号。別の一棟の所在地番が申請情報に必要）、H30-Q14オ（準則89条）、H26-Q14エ（法44条1項5号、令3条8号ホ、準則89条は登記官の記録方法の定め）。
- extra_refs：法44条1項5号（附属建物があるときの所在〔区分建物である附属建物にあっては、その附属建物が属する一棟の建物の所在〕並びに種類、構造及び床面積）、令3条8号ホ（申請情報）、準則89条（附属建物が主たる建物と同一の一棟の建物に属するときは、一棟の所在・地番並びに構造及び床面積を記録することを要しない）は法令DB note-articles/laws/ の原文で確認。準則の用語は『主たる建物』だが、図は記事の『主である建物』に合わせた。
- 登場人物：人型は使わず、建物と表示は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 同じ一棟のときだけ、一棟の表示を省ける | 「一棟の表示を省ける」を黄色マーカー |
| コマ1 見出し | ラベル | ①　附属建物の表示、どこまで省ける？ | — |
| コマ1 図 | 図・カード | 肢D1778 / 乙は、別の一棟に属する区分建物 / その一棟の所在地番を書く？ / 肢D1382 / 乙は、同じ一棟に属する区分建物 / 一棟の所在・構造・床面積を記録する？ / 肢D0979 / 同じ一棟の乙の、構造・床面積 / 乙自体の構造・床面積も書かなくてよい？ / 甲の附属建物に乙をする。何を書く？ | — |
| コマ1 | 藍子（左・先に話す） | 同じ一棟なら、全部省けますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。省けるのは一棟の表示だけよ | 「一棟の表示だけ」 |
| コマ2 見出し | ラベル | ②　同じ一棟と、別の一棟 | — |
| コマ2 図 | 図・カード | 附属建物が区分建物のとき / どの一棟に属するかを見る / 同じ一棟に属する / 準則89条 / 一棟の所在・構造・床面積は、 / 記録することを要しない / （主である建物に載っている） / 別の一棟に属する / 法44条1項5号 / その一棟の所在地番も、 / 申請情報に書く / （附属建物の構造欄に一棟の表示を記録） / 肢D1778は右の話、肢D1382は左の話 | — |
| コマ3 見出し | ラベル | ③　附属建物自体は省けない | — |
| コマ3 図 | 図・カード | 乙自体の構造・床面積も省ける / 肢D0979の言い分 / 乙自体の種類・構造・床面積は、常に書く / 省けるのは、一棟の表示だけ / 附属建物の表示 / 法44条1項5号 / 所在　別の一棟ならその地番 / 種類　省けない / 構造　省けない / 床面積　省けない / 省けるのは、同じ一棟の一棟の表示だけ / 同じ一棟 | — |
| コマ3 | 藍子（左・1番目） | 同じ一棟なら、構造も床面積も要らない？ | — |
| コマ3 | トリ先生（右・2番目） | いいえ。乙自体の表示は省けないの | 「乙自体の表示は省けない」 |
| コマ4 見出し | ラベル | ④　結論は×と×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 省けるのは、一棟の表示だけなんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。同じ一棟か、別の一棟かが分かれ目よ | 「同じ一棟か、別の一棟か」 |
| コマ4 チェック欄 | 3項目（青✓） | 同じ一棟の附属建物は、一棟の所在・構造・床面積を記録しない（肢D1382は×） / 別の一棟の附属建物は、その一棟の所在地番を申請情報に書く（肢D1778は×） / 附属建物自体の種類・構造・床面積は省けない（肢D0979は×） | — |
| 結論帯 | 1行目 | 省けるのは、同じ一棟のときの一棟の表示だけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1778・D1382・D0979　正解×・×・×（R04-Q14ウ／H30-Q14オ／H26-Q14エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法44条1項5号、不動産登記令3条8号ホ、不動産登記事務取扱手続準則89条。法令DB note-articles/laws/ と照合済み。同一の一棟の附属建物の所在地番を申請情報から省略できるかどうかを直接定めた条文はなく、準則89条の記録しないことに対応した取扱い（逆の結論の肢D1969の記事）。図には、申請情報の省略を断定する文言は入れていない

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

TITLE BANNER: text 「同じ一棟のときだけ、一棟の表示を省ける」 in large bold letters; the part 「一棟の表示を省ける」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　附属建物の表示、どこまで省ける？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high). Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: tag 「肢D1778」, heading 「乙は、別の一棟に属する区分建物」, body 「その一棟の所在地番を書く？」.
- Card 2: tag 「肢D1382」, heading 「乙は、同じ一棟に属する区分建物」, body 「一棟の所在・構造・床面積を記録する？」.
- Card 3: tag 「肢D0979」, heading 「同じ一棟の乙の、構造・床面積」, body 「乙自体の構造・床面積も書かなくてよい？」.
- At the top, a small question badge in a gray fill with dark navy text 「甲の附属建物に乙をする。何を書く？」 (a question badge only, with no check mark and no cross).
- The three cards have clearly different texts; the texts are NOT identical. There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「同じ一棟なら、
全部省けますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
省けるのは
一棟の表示だけよ」 with the part 「一棟の表示だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　同じ一棟と、別の一棟」
- A small dark navy tag 「附属建物が区分建物のとき」 at the top left, with one line beside it: 「どの一棟に属するかを見る」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「同じ一棟に属する」, a small tag 「準則89条」, three body lines: 「一棟の所在・構造・床面積は、」, 「記録することを要しない」, 「（主である建物に載っている）」.
- Right card, heading 「別の一棟に属する」, a small tag 「法44条1項5号」, three body lines: 「その一棟の所在地番も、」, 「申請情報に書く」, 「（附属建物の構造欄に一棟の表示を記録）」.
- Under the two cards, one wide dark navy band with large white text 「肢D1778は右の話、肢D1382は左の話」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　附属建物自体は省けない」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「乙自体の構造・床面積も省ける」, body 「肢D0979の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「乙自体の種類・構造・床面積は、常に書く」, body 「省けるのは、一棟の表示だけ」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「附属建物の表示」 and a small dark navy tag 「法44条1項5号」 at its top right, with the same pale gray fill and a dark navy outline, containing exactly four short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「所在　別の一棟ならその地番」, 「種類　省けない」, 「構造　省けない」, 「床面積　省けない」. Under the four rows, one small dark navy ribbon tag with white text 「省けるのは、同じ一棟の一棟の表示だけ」, with the text 「同じ一棟」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「同じ一棟なら、
構造も床面積も
要らない？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
乙自体の表示は
省けないの」 with the part 「乙自体の表示は省けない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と×と×」
- 藍子 bubble (left, spoken first): 「省けるのは、
一棟の表示だけ
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
同じ一棟か、別の一棟かが
分かれ目よ」 with the part 「同じ一棟か、別の一棟か」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「同じ一棟の附属建物は、一棟の所在・構造・床面積を記録しない（肢D1382は×）」, 「別の一棟の附属建物は、その一棟の所在地番を申請情報に書く（肢D1778は×）」, 「附属建物自体の種類・構造・床面積は省けない（肢D0979は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「省けるのは、同じ一棟のときの一棟の表示だけ」 with a yellow highlighter marker.
- Line 2: 「問題D1778・D1382・D0979　正解×・×・×（R04-Q14ウ／H30-Q14オ／H26-Q14エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 物, 番, 肢, 解, 記, 請, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that the left side of panel 3 has exactly one red cross (top card) and one blue check mark (bottom card), and that the only other blue check marks in the whole image are the three in the checklist of panel 4; confirm that the three cards of panel 1 are in the order 肢D1778, 肢D1382, 肢D0979, never swapped; confirm that the left card of panel 2 has the heading 「同じ一棟に属する」 and the right card has the heading 「別の一棟に属する」, never swapped; confirm that the list card of panel 3 has exactly four rows confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編⑤_4コマ6_同じ一棟のときだけ、一棟の表示を省ける.png`
- 途中の版・不採用の版：`不動産登記法編⑤_4コマ6_同じ一棟のときだけ、一棟の表示を省ける_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/prompt_4koma_PE-06_01_fuzoku-tatemono-hyouji.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で3つの問い（別の一棟／同じ一棟の一棟の表示／同じ一棟の附属建物自体）、コマ2で同じ一棟と別の一棟の違い、コマ3で附属建物自体の表示は省略できないことが言える
- [ ] 工程C：構成表の全文言を記事（R04-Q14ウ、H30-Q14オ、H26-Q14エ）・法令DB（法44条1項5号、準則89条）と突き合わせ済み。出題当時と今の言い方の違いは入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①附属建物自体の所在・種類・構造・床面積は書く（法44条1項5号） ②同じ一棟なら一棟の所在・構造・床面積の記録は要しない（準則89条）。これは登記官の記録方法の定めで、附属建物自体を省略できる意味ではない ③別の一棟ならその一棟の所在地番も要る ④D1778・D1382・D0979はいずれも×

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

## 改訂履歴（このファイルは `src/spec_4koma_PE-06_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第5章【PE-6】用。型5（整理カード併用）。同じ一棟と別の一棟の対比と、附属建物自体は省けないことの整理に絞った）
