# D1939 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②不動産登記法編 第4章「土地の分筆・合筆・地積更正」（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch4.md`）の、論点【PD-11】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PD-11_02.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1939（不動産登記法／土地の分筆・合筆・地積更正、出典 R06-Q07オ）。正解＝×（誤った記述）。
- 記事：`note-articles/r6-mondai/q07-chiseki-kosei.md` オ（地積の更正の登記に、申請義務の期間制限はない。地目又は地積の変更の登記には変更があった日から1か月以内の申請義務がある）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文が『誤りが判明した後に所有権の登記名義人となった者は、その者に係る所有権の登記があった日から1か月以内に…申請しなければならない』と、地目・地積の『変更』の登記の義務（法37条）の言い回し（変更があった後に名義人となった者は、登記があった日から1か月以内）をそっくり使い、『変更』の語だけを『更正』に差し替える。見慣れた文型なので、そのまま正しいと読ませる。
- 【受験者の勘違い・定着していない点】（推測）①地積に関する登記なら、更正にも変更と同じ1か月以内の申請義務があると考える（変更と更正の混同）。②更正が最初から誤っていたものを直す登記で、いつ誤りが生じたか把握しにくいから義務がない、という理由が結びついていない。③更正について定めがあるのは、申請できる者（表題部所有者又は所有権の登記名義人。法38条）だけだと気づかない。
- 【対比する制度】「地積の変更の登記」⇔「地積の更正の登記」：地目又は地積の変更の登記は、変更があった日から1か月以内に申請しなければならない（法37条1項）／地積の更正の登記には、申請の期間制限も義務もない（結論が逆になる点）。
- 【型の選び方】型：型3（理由説明）＋型1の対比（変更⇔更正）。理由：結論（義務はない）だけ覚えても、『地積の登記は1か月以内』という感覚が残ると崩れる。なぜ更正に義務がないか（錯誤がいつ生じたかを把握するのは困難で、法は申請義務を定めていない）を、コマ3の左の3枚のカード（印なし）に置いた。コマ2は『変更の登記』と『更正の登記』の左右の対比。壁＝『地積に関する登記ならすべて1か月以内という思い込み』。
- コマごとに読者が言えること：コマ1＝地積の誤りが判明した後に名義人になった者に、1か月以内の更正の申請義務があるかを問う肢。コマ2＝変更は1か月以内の義務、更正は期限も義務もない。コマ3＝更正は錯誤を直す登記で、いつ生じたか把握しにくいため義務を定めていない。定めがあるのは申請できる者だけ。コマ4＝D1939は×。
- 記事の範囲：R06-Q07オ（更正の登記は錯誤によるもので、その錯誤がいつ生じたのかを把握するのは困難であることから、法は地積に関する更正の登記について申請義務を定めていない。地目又は地積の変更の登記には変更があった日から1か月以内の申請義務がある〔法37条1項〕。法38条は更正の登記を申請できる者を表題部所有者又は所有権の登記名義人に限定している）。
- extra_refs：問題文の言い回しの元になった『変更があった後に名義人となった者は、登記があった日から1か月以内』（法37条2項）は、法令DB note-articles/laws/fudousan-touki-hou.md 第37条で確認した。記事オには法37条1項しかないので、図には入れず、設計メモの説明にとどめた。
- 登場人物：人型は使わず、登記は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は左の縦3枚のカードと右の会話。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に縦3枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 地積の更正に、1か月の義務はない | 「1か月の義務はない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　地積の登記は、1か月以内？ | — |
| コマ1 図 | 図・カード | D1939 / 地積の誤りが判明した後に / 所有権の登記名義人となった / 所有権の登記の日から1か月以内に / 更正の登記を申請しなければならない？ / 更正にも、1か月の申請義務がある？ | — |
| コマ1 | 藍子（左・先に話す） | 地積の登記なら、1か月以内ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。変更と更正を混ぜないの | 「変更と更正」 |
| コマ2 見出し | ラベル | ②　変更の登記と、更正の登記 | — |
| コマ2 図 | 図・カード | 地積に関する登記 / 変更と更正で、申請の義務が違う / 地積の変更の登記 / 法37条1項 / 変更があった日から1か月以内 / 申請しなければならない / 地積の更正の登記 / 期間制限の規定なし / 申請の期限も、義務もない / 最初からの誤りを直す登記 / 期限も、義務もない | — |
| コマ3 見出し | ラベル | ③　なぜ、更正に義務がない？ | — |
| コマ3 図 | 図・カード | 更正は、錯誤による登記 / 錯誤がいつ生じたかを、把握するのは困難 / 法は、申請義務を定めていない / 期限も、義務もない / 定めがあるのは、申請できる者 / 表題部所有者又は所有権の登記名義人に限る（法38条） | — |
| コマ3 | 藍子（左・1番目） | 名義人になったら、義務ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | それは変更の話。更正は別よ | 「更正は別」 |
| コマ3 | 藍子（左・3番目） | 更正は、誰でも申請できますか？ | — |
| コマ3 | トリ先生（右・4番目） | いいえ。名義人に限られるのよ | 「名義人に限られる」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 変更は1か月、更正は期限なしですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。義務があると書けば×よ | 「義務があると書けば×」 |
| コマ4 チェック欄 | 3項目（青✓） | 地目又は地積の変更の登記は、変更があった日から1か月以内に申請しなければならない（法37条1項） / 地積の更正の登記には、申請の期限も義務もない（錯誤がいつ生じたか把握しにくい） / 更正を申請できるのは、表題部所有者又は所有権の登記名義人だけ（法38条） | — |
| 結論帯 | 1行目 | 地積の更正に、申請の期限も義務もない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1939　正解×（R06-Q07オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法37条2項（法令DB note-articles/laws/fudousan-touki-hou.md 第37条）：地目又は地積について変更があった後に表題部所有者又は所有権の登記名義人となった者は、その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内に、当該地目又は地積に関する変更の登記を申請しなければならない。問題文の言い回しの元。記事オには法37条1項しか書かれておらず、図には入れていない

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

TITLE BANNER: text 「地積の更正に、1か月の義務はない」 in large bold letters; the part 「1か月の義務はない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　地積の登記は、1か月以内？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and two short dark navy text lines. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1 with a small gray tag 「D1939」: 「地積の誤りが判明した後に」 and 「所有権の登記名義人となった」. Card 2: 「所有権の登記の日から1か月以内に」 and 「更正の登記を申請しなければならない？」.
- At the top, a small question badge in a gray fill with dark navy text 「更正にも、1か月の申請義務がある？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「地積の登記なら、
1か月以内
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
変更と更正を
混ぜないの」 with the part 「変更と更正」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　変更の登記と、更正の登記」
- A small dark navy tag 「地積に関する登記」 at the top left, with one line beside it: 「変更と更正で、申請の義務が違う」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「地積の変更の登記」, a small tag 「法37条1項」, two body lines: 「変更があった日から1か月以内」, 「申請しなければならない」.
- Right card, heading 「地積の更正の登記」, a small tag 「期間制限の規定なし」, two body lines: 「申請の期限も、義務もない」, 「最初からの誤りを直す登記」, with the text 「期限も、義務もない」 highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、更正に義務がない？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: three stacked reason cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and one short body line, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「更正は、錯誤による登記」, body 「錯誤がいつ生じたかを、把握するのは困難」.
- Card 2, heading 「法は、申請義務を定めていない」, body 「期限も、義務もない」.
- Card 3, heading 「定めがあるのは、申請できる者」, body 「表題部所有者又は所有権の登記名義人に限る（法38条）」.
- The three cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「名義人になったら、
義務ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それは変更の話。
更正は別よ」 with the part 「更正は別」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「更正は、誰でも
申請できますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
名義人に限られる
のよ」 with the part 「名義人に限られる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「変更は1か月、
更正は期限なし
ですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
義務があると
書けば×よ」 with the part 「義務があると書けば×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「地目又は地積の変更の登記は、変更があった日から1か月以内に申請しなければならない（法37条1項）」, 「地積の更正の登記には、申請の期限も義務もない（錯誤がいつ生じたか把握しにくい）」, 「更正を申請できるのは、表題部所有者又は所有権の登記名義人だけ（法38条）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「地積の更正に、申請の期限も義務もない」 with a yellow highlighter marker.
- Line 2: 「問題D1939　正解×（R06-Q07オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 初, 地, 所, 権, 登, 規, 解, 記, 請, 違, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編4章_4コマ6_地積の更正に、1か月の義務はない.png`
- 途中の版・不採用の版：`不動産登記法編4章_4コマ6_地積の更正に、1か月の義務はない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch4/prompt_4koma_PD-11_02_henkou-kousei.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で肢の問い、コマ2で変更の登記と更正の登記の対比、コマ3で更正に義務がない理由と申請できる者、が言える
- [ ] 工程C：構成表の全文言を記事（R06-Q07オ）・法令DB（法37条・38条）と突き合わせ済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①地目又は地積の変更の登記は変更があった日から1か月以内の申請義務（法37条1項）②地積の更正の登記に期間制限も義務もない③更正を申請できるのは表題部所有者又は所有権の登記名義人（法38条）④肢D1939は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PD-11_02.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第4章【PD-11】用。型3の理由説明＋型1の対比。変更の登記〔1か月以内〕と更正の登記〔義務なし〕の対比に絞った。D0443・D0441〔判決による代位〕は別の4コマ）
