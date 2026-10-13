# D1173 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第6章「建物の分割・分棟・合併」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch6.md`）の、論点【PF1-6】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PF1-06_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1173（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H28-Q14エ）。正解＝×（誤った記述）。
- 記事：`note-articles/h28-mondai/q14-tatemono-gappei.md` エ（H28：床面積に変更がなくても、合併後の各階平面図の添付は省略できない。令別表16の項添付情報イ）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『従来の各階平面図の床面積に変更がないため』という理由を付けて、『合併後の各階平面図を添付することを要しない』と結論づける。もっともらしい理由が付いていて、数字が変わらなければ図面も同じだから要らない、と思わせる。
- 【受験者の勘違い・定着していない点】（推測）①『変更がない部分は、手続もそのままでよい』と考える。②床面積という数値の変更の有無と、合併という登記記録の再編成に必要な図面を、別の話だと切り分けられない。③建物の分割・区分・合併の登記の添付情報（令別表16の項イ）が『分割後、区分後又は合併後の』図面だと定着していない。
- 【対比する制度】「床面積の数値は、変わらない」⇔「合併後の建物の図面は、要る」：床面積の数値が変わらなくても、合併は2つの登記記録を1つの新しい登記記録にまとめ直す登記で、合併後の建物は登記記録上新しく生まれた1個の建物なので、その姿を示す図面を改めて添付する（結論が逆になる点）。
- 【型の選び方】型：型3（理由説明）。理由：『合併後の各階平面図は要る』と結論だけ覚えても、『数字が変わらないから要らない』という理由づけがもっともらしく、別の肢で崩れる。なぜ要るか（合併は登記記録をまとめ直す登記で、合併後の建物は新しい1個の建物）と、付ける図面は何か（令別表16の項）を、コマ3の理由のカード3枚（印なし）に置いた。コマ1は思い込みを出す3枚のカード、コマ2は『床面積の数値』と『合併後の図面』の左右の対比。壁＝『数字が変わらないなら手続も変わらない』という思い込み。
- コマごとに読者が言えること：コマ1＝床面積の数値に変更がない合併で、合併後の各階平面図が要るかを問うている。コマ2＝床面積の数値は変わらなくても、合併後の建物の図面は要る。コマ3＝合併は登記記録をまとめ直す登記で、付けるのは合併後の建物図面及び各階平面図（令別表16の項）。コマ4＝D1173は×。
- 記事の範囲：H28-Q14エ（合併後の建物は新しい登記記録として作られるので、床面積に変動がなくても、合併後の各階平面図を改めて添付する。令別表16項添付情報イ）。『分割後、区分後又は合併後の建物図面及び各階平面図』という令別表16の項の添付情報イの文言は、法令DBで原文を確認した。登録免許税・登記識別情報は別の論点なので入れていない。
- extra_refs：令別表16の項（登記：建物の分割の登記、建物の区分の登記又は建物の合併の登記。添付情報イ：当該分割後、区分後又は合併後の建物図面及び各階平面図）は法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md で原文を確認。
- 登場人物：人型は使わず、建物・図面は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカードと疑問バッジ、コマ2は左右のカード、コマ3は縦3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 床面積が同じでも、合併後の図面は要る | 「合併後の図面は要る」を黄色マーカー |
| コマ1 見出し | ラベル | ①　数字が変わらない合併、図面は？ | — |
| コマ1 図 | 図・カード | 甲建物と乙建物を合併する / 従来の各階平面図の床面積に変更がない / 合併後の各階平面図を添付しなくてよい？ / 図面は、省略できる？ | — |
| コマ1 | 藍子（左・先に話す） | 数字が変わらないなら、図面も要りませんよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。数字と図面は別の話よ | 「別の話」 |
| コマ2 見出し | ラベル | ②　数字の話と、図面の話 | — |
| コマ2 図 | 図・カード | 合併の登記 / 2つの話を、分けて考える / 床面積の数値は、変わらない / 各階平面図の数字 / 甲建物と乙建物の床面積は / 合併しても同じ / 合併後の建物の図面は、要る / 令別表16の項 / 合併後の建物は、登記記録上 / 新しく生まれた1個の建物 / 数字が同じでも、図面は省略できない | — |
| コマ3 見出し | ラベル | ③　なぜ、図面が要るのか | — |
| コマ3 図 | 図・カード | 合併は、登記記録をまとめ直す / 甲建物と乙建物の登記記録を / 1つの登記記録にする / 合併後の建物は、新しい1個の建物 / ひっかけ：床面積が変わらないから省略 / その姿を示す図面を / 改めて添付する / 付ける図面は、令別表16の項 / 合併後の建物図面 / 合併後の各階平面図 | — |
| コマ3 | 藍子（左・1番目） | 床面積が同じなら、元の図面でいいのでは？ | — |
| コマ3 | トリ先生（右・2番目） | 合併は、登記記録をまとめ直す登記なのよ | 「まとめ直す」 |
| コマ3 | 藍子（左・3番目） | では、何の図面を付けるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 合併後の建物図面と各階平面図よ | 「合併後」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 数字が同じでも、図面は付けるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。合併後の姿を図面で示すのよ | 「合併後の姿」 |
| コマ4 チェック欄 | 3項目（青✓） | 合併の登記には、合併後の建物図面及び各階平面図を添付する（令別表16の項） / 床面積に変更がなくても、添付を省略できない / 床面積の数値の話と、登記記録をまとめ直す図面の話は別 | — |
| 結論帯 | 1行目 | 床面積が変わらなくても、合併後の各階平面図は要る | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1173　正解×（H28-Q14エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令 別表16の項（建物の分割の登記、建物の区分の登記又は建物の合併の登記）添付情報イ。法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md と照合済み。記事H28-Q14エの引用と一致

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

TITLE BANNER: text 「床面積が同じでも、合併後の図面は要る」 in large bold letters; the part 「合併後の図面は要る」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　数字が変わらない合併、図面は？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「甲建物と乙建物を合併する」. Card 2: 「従来の各階平面図の床面積に変更がない」. Card 3: 「合併後の各階平面図を添付しなくてよい？」.
- At the top, a small question badge in a gray fill with dark navy text 「図面は、省略できる？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「数字が変わらないなら、
図面も要りませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
数字と図面は
別の話よ」 with the part 「別の話」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　数字の話と、図面の話」
- A small dark navy tag 「合併の登記」 at the top left, with one line beside it: 「2つの話を、分けて考える」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「床面積の数値は、変わらない」, a small tag 「各階平面図の数字」, two body lines: 「甲建物と乙建物の床面積は」, 「合併しても同じ」.
- Right card, heading 「合併後の建物の図面は、要る」, a small tag 「令別表16の項」, two body lines: 「合併後の建物は、登記記録上」, 「新しく生まれた1個の建物」.
- Under the two cards, one wide dark navy band with large white text 「数字が同じでも、図面は省略できない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、図面が要るのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「合併は、登記記録をまとめ直す」, two body lines 「甲建物と乙建物の登記記録を」 and 「1つの登記記録にする」.
- Card 2, heading 「合併後の建物は、新しい1個の建物」, a dark navy ribbon tag with large white text 「ひっかけ：床面積が変わらないから省略」, two body lines 「その姿を示す図面を」 and 「改めて添付する」.
- Card 3, heading 「付ける図面は、令別表16の項」, two body lines 「合併後の建物図面」 and 「合併後の各階平面図」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「床面積が同じなら、
元の図面でいいのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「合併は、登記記録を
まとめ直す登記なのよ」 with the part 「まとめ直す」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、何の図面を
付けるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「合併後の建物図面と
各階平面図よ」 with the part 「合併後」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「数字が同じでも、
図面は付けるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
合併後の姿を
図面で示すのよ」 with the part 「合併後の姿」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「合併の登記には、合併後の建物図面及び各階平面図を添付する（令別表16の項）」, 「床面積に変更がなくても、添付を省略できない」, 「床面積の数値の話と、登記記録をまとめ直す図面の話は別」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「床面積が変わらなくても、合併後の各階平面図は要る」 with a yellow highlighter marker.
- Line 2: 「問題D1173　正解×（H28-Q14エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 建, 物, 登, 解, 記, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the three cards of panel 1 are in the order 合併する, 床面積に変更がない, 添付しなくてよい?, never reordered; confirm that the left card of panel 2 has the heading 「床面積の数値は、変わらない」 and the right card has the heading 「合併後の建物の図面は、要る」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法編6章_4コマ6_床面積が同じでも、合併後の図面は要る.png`
- 途中の版・不採用の版：`不登法編6章_4コマ6_床面積が同じでも、合併後の図面は要る_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch6/prompt_4koma_PF1-06_01_goppei-gokai-zumen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で問い（床面積に変更がない合併で、合併後の各階平面図は要るか）、コマ2で数字の話と図面の話は別であること、コマ3でなぜ要るか（新しい1個の建物の姿を示す）と付ける図面が言える
- [ ] 工程C：構成表の全文言を記事（H28-Q14エ）・法令DBと突き合わせ済み。出題当時と今の言い方の違いはない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①合併は2つの登記記録を1つにまとめ直す登記 ②合併後の建物は新しい1個の建物として扱われる ③付ける図面は合併後の建物図面及び各階平面図（令別表16の項添付情報イ）④床面積に変更がなくても省略できない ⑤D1173は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PF1-06_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第6章【PF1-6】用。型3（理由説明）。床面積の数値の話と、合併後の図面の話は別、合併は登記記録をまとめ直す登記、の順で組んだ）
