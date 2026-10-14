# D1381・D1967 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第5章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md`）の、論点【PE-5】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PE-05_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1381・D1967（不動産登記法／建物の認定・個数・種類構造床面積、出典 H30-Q14エ／R06-Q13ウ）。正解＝D1381＝×（誤った記述）／D1967＝〇（正しい記述）。
- 記事：`note-articles/h30-mondai/q14-fuzoku-tatemono.md` エ（H30：主である建物の土地の地番と附属建物の地下車庫の土地の地番が異なっても、附属建物の土地の地番は所在欄に後ろから記録される。準則88条2項は2筆以上にまたがる建物の記録順の定めで、附属建物の土地の地番を所在欄に記録する点を直接定めた条文は法令DBで確認できず、登記実務上の取扱い）。ほか、R06-Q13ウ（r6-mondai/q13-tatemono-shozai.md。仮換地上の建物の所在は、仮換地の場所に現に登記記録が存在する土地の現在の地番。予定地番の併記は任意）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch5.md 【PE-5】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1381は、肢が『附属建物である地下車庫が存在する土地の地番は、主である建物の表示欄の所在欄に記録されない』と言い切り、所在は主である建物の土地の地番だけと思い込ませる（実際は後ろに記録される。×）。D1967は『仮換地が指定された土地の上に』と始め、仮換地や従前の土地の地番を答えさせたくなるが、書くのは『現に存する土地の地番』である（〇）。どちらも、建物が現にどの土地にあるかを見落とさせる。
- 【受験者の勘違い・定着していない点】（推測）①建物の所在を『主である建物の土地の地番』と一つに決めてしまい、別の地番の土地にある地下車庫は所在欄に載らないと考える。②仮換地は、換地処分までは独自の地番を持つ土地ではなく、建物の下には底地という別の登記記録の土地があるため、予定地番や従前の土地の地番を所在にすると考える。③予定地番のかっこ書きを、書かなければならないものと取り違える。
- 【対比する制度】「現に存する土地の地番」⇔「仮換地の予定地番」：所在として必ず記録するのは建物が現に存する土地の地番（主である建物の土地が先、地下車庫の土地は後ろ、仮換地の上の建物は仮換地の場所に現に登記記録がある土地の地番）／仮換地の予定地番は、所在ではなく、かっこ書きで併記してもよいにとどまる（任意）（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は肢のカード）に型3（理由説明）を組み合わせる。理由：2肢は別々の場面（附属建物の地下車庫／仮換地の上の建物）で共通の日付がなく、『所在は主である建物の土地だけ』『仮換地なら予定地番』という別々の思い込みから出る。壁は『所在欄の地番は何を基準に書くか』という理由の欠落なので、コマ3で『現に存する土地かどうか』を理由に、地下車庫の土地と仮換地の場合を1つの整理にそろえた。コマ1＝2肢のカード（肢／場面／問い）、コマ2＝『現に存する土地の地番』と『仮換地の予定地番』の左右のカード、コマ3＝左は肢D1381の言い分（✕）と正しい整理（✓）、右は会話1往復と、所在欄の地番の決め方の整理カード、コマ4＝×・〇の整理。D1762（区分建物の非区分附属建物の所在は構造欄）のように区分建物の話にすると本論点の別の軸になるので入れていない。
- コマごとに読者が言えること：コマ1＝2肢は、附属建物の地下車庫が別の地番にあるとき、仮換地の上に新築したときに、所在欄にどの地番を書くかを問う。コマ2＝書くのは建物が現に存する土地の地番で、仮換地の予定地番は所在ではなく、併記は任意。コマ3＝地下車庫の土地の地番も所在欄に後ろから記録される。仮換地の上なら現に存する土地の地番。コマ4＝D1381は×、D1967は〇。
- 記事の範囲：H30-Q14エ（準則88条2項。附属建物の土地の地番を所在欄に記録する点は実務の取扱い）、R06-Q13ウ（法44条1項1号、仮換地の上の建物の所在、予定地番の併記は任意）。総合記事【PE-5】の結論・判断のしかた1・2。増築で隣地にまたがったときの変更登記（D1763）と、区分建物の非区分附属建物の所在（D1762）は、この図に入れない。
- extra_refs：法44条1項1号（建物の所在する市、区、郡、町、村、字及び土地の地番）・準則88条2項（2筆以上の土地にまたがる建物の所在は、床面積の多い部分又は主たる建物の所在する土地の地番を先に、他の土地の地番は後に記録）は法令DB note-articles/laws/fudousan-touki-hou.md・fudousan-touki-jimu-junsoku.md の原文で確認。準則の用語は『主たる建物』だが、図は記事の『主である建物』に合わせた。
- 同じ論点の他の肢（図には肢として載せない）：D1763（増築で隣接する土地にまたがったとき、地番を所在に加える変更登記ができる・×）は図解8が担当するので、この図には入れない。D1762（区分建物の非区分附属建物の所在は構造欄・〇）は既存の4コマ（D1762_prompt.md）があるので入れない。
- 登場人物：人型は使わず、建物と地番は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話1往復と整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 所在は、現に建つ土地の地番で書く | 「現に建つ土地」を黄色マーカー |
| コマ1 見出し | ラベル | ①　所在欄に、どの地番が載る？ | — |
| コマ1 図 | 図・カード | 肢D1381 / 地下車庫が、別の地番の土地にある / その地番は、所在欄に記録されない？ / 肢D1967 / 仮換地の上に、建物を新築した / 現に存する土地の地番を、所在とする？ / 所在欄に、どの地番が載る？ | — |
| コマ1 | 藍子（左・先に話す） | 所在は、主である建物の土地だけですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。現に建つ土地を見落とす癖よ | 「現に建つ土地」 |
| コマ2 見出し | ラベル | ②　現に存する土地と、予定地番 | — |
| コマ2 図 | 図・カード | 建物の所在 / どの地番が所在になるかを見る / 現に存する土地の地番 / 法44条1項1号 / 主である建物の土地が先、他は後ろ / 地下車庫の土地も後ろ（実務の取扱い） / 仮換地の上は、現に登記記録がある土地 / 仮換地の予定地番 / 実務の取扱い / かっこ書きで併記するかは、任意 / 所在は、予定地番でなく現にある土地 / 肢D1381・肢D1967は、どちらも左の話 | — |
| コマ3 見出し | ラベル | ③　所在は、現に建つ土地で決まる | — |
| コマ3 図 | 図・カード | 肢D1381の言い分 / 地下車庫の土地の地番は、所在欄に記録されない / 地下車庫の土地の地番も、後ろに記録される / 主である建物の土地が先（実務の取扱い） / 所在欄の地番の決め方 / 法44条1項1号 / 肢D1381　地下車庫の土地は、後ろに記録 / 肢D1967　仮換地の上は、現に存する土地 / 予定地番のかっこ書きは、併記が任意 / ひっかけ：主である建物の土地だけ / 主である建物の土地だけ | — |
| コマ3 | 藍子（左・1番目） | 仮換地なら、予定地番を所在にしますか？ | — |
| コマ3 | トリ先生（右・2番目） | いいえ。書くのは現に存する土地よ | 「現に存する土地」 |
| コマ4 見出し | ラベル | ④　結論は×と〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | どちらも、現に建つ土地を見るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。主の地番だけで決めつけないことよ | 「決めつけない」 |
| コマ4 チェック欄 | 3項目（青✓） | 附属建物の地下車庫の土地の地番も、所在欄に後ろから記録される（肢D1381は×） / 仮換地の上の建物は、現に存する土地の地番を所在とする（肢D1967は〇） / 仮換地の予定地番のかっこ書きの併記は、任意 | — |
| 結論帯 | 1行目 | 所在は、現に建つ土地の地番で書く | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1381・D1967　正解×・〇（H30-Q14エ／R06-Q13ウ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法44条1項1号、不動産登記事務取扱手続準則88条2項。法令DB note-articles/laws/fudousan-touki-hou.md・fudousan-touki-jimu-junsoku.md と照合済み。附属建物の地下車庫の土地の地番を所在欄に記録する点は直接定めた条文がなく、記事（H30-Q14エ）も登記実務上の取扱いとする。仮換地の予定地番の併記が任意であることは記事（R06-Q13ウ）の先例の要旨に基づき、図には『実務の取扱い』と添えた

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

TITLE BANNER: text 「所在は、現に建つ土地の地番で書く」 in large bold letters; the part 「現に建つ土地」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　所在欄に、どの地番が載る？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill, a dark navy outline, a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high). Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: tag 「肢D1381」, heading 「地下車庫が、別の地番の土地にある」, body 「その地番は、所在欄に記録されない？」.
- Card 2: tag 「肢D1967」, heading 「仮換地の上に、建物を新築した」, body 「現に存する土地の地番を、所在とする？」.
- At the top, a small question badge in a gray fill with dark navy text 「所在欄に、どの地番が載る？」 (a question badge only, with no check mark and no cross).
- The two cards have clearly different texts; the texts are NOT identical. There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「所在は、主である
建物の土地だけ
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
現に建つ土地を
見落とす癖よ」 with the part 「現に建つ土地」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　現に存する土地と、予定地番」
- A small dark navy tag 「建物の所在」 at the top left, with one line beside it: 「どの地番が所在になるかを見る」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「現に存する土地の地番」, a small tag 「法44条1項1号」, three body lines: 「主である建物の土地が先、他は後ろ」, 「地下車庫の土地も後ろ（実務の取扱い）」, 「仮換地の上は、現に登記記録がある土地」, with the heading highlighted with a yellow marker.
- Right card, heading 「仮換地の予定地番」, a small tag 「実務の取扱い」, two body lines: 「かっこ書きで併記するかは、任意」, 「所在は、予定地番でなく現にある土地」.
- Under the two cards, one wide dark navy band with large white text 「肢D1381・肢D1967は、どちらも左の話」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　所在は、現に建つ土地で決まる」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, a small tag 「肢D1381の言い分」, heading 「地下車庫の土地の地番は、所在欄に記録されない」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「地下車庫の土地の地番も、後ろに記録される」, body 「主である建物の土地が先（実務の取扱い）」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「所在欄の地番の決め方」 and a small dark navy tag 「法44条1項1号」 at its top right, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「肢D1381　地下車庫の土地は、後ろに記録」, 「肢D1967　仮換地の上は、現に存する土地」, 「予定地番のかっこ書きは、併記が任意」. Under the three rows, one small dark navy ribbon tag with white text 「ひっかけ：主である建物の土地だけ」, with the text 「主である建物の土地だけ」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「仮換地なら、
予定地番を
所在にしますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「いいえ。
書くのは
現に存する土地よ」 with the part 「現に存する土地」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と〇」
- 藍子 bubble (left, spoken first): 「どちらも、
現に建つ土地を
見るんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
主の地番だけで
決めつけないことよ」 with the part 「決めつけない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「附属建物の地下車庫の土地の地番も、所在欄に後ろから記録される（肢D1381は×）」, 「仮換地の上の建物は、現に存する土地の地番を所在とする（肢D1967は〇）」, 「仮換地の予定地番のかっこ書きの併記は、任意」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「所在は、現に建つ土地の地番で書く」 with a yellow highlighter marker.
- Line 2: 「問題D1381・D1967　正解×・〇（H30-Q14エ／R06-Q13ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 物, 番, 登, 肢, 解, 記, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that the left side of panel 3 has exactly one red cross (top card) and one blue check mark (bottom card), and that the only other blue check marks in the whole image are the three in the checklist of panel 4; confirm that the two cards of panel 1 are in the order 肢D1381, 肢D1967, never swapped; confirm that the left card of panel 2 has the heading 「現に存する土地の地番」 and the right card has the heading 「仮換地の予定地番」, never swapped; confirm that the list card of panel 3 has exactly three rows confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編⑤_4コマ5_所在は、現に建つ土地の地番で書く.png`
- 途中の版・不採用の版：`不動産登記法編⑤_4コマ5_所在は、現に建つ土地の地番で書く_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch5/prompt_4koma_PE-05_01_shozai-genni-sonsuru-tochi.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢が所在欄にどの地番を書くかを問うていること、コマ2で現に存する土地の地番が所在になり予定地番は任意と分かり、コマ3で地下車庫の土地も後ろに記録されることが言える
- [ ] 工程C：構成表の全文言を記事（H30-Q14エ、R06-Q13ウ）・総合記事【PE-5】・法令DB（法44条1項1号、準則88条2項）と突き合わせ済み。地下車庫の土地の地番を所在欄に記録する点は、条文に明記がないので『実務の取扱い』と添えた
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①所在欄には建物が現に存する土地の地番を書く（主である建物の土地が先、地下車庫の土地は後ろ。実務の取扱い） ②仮換地の上の建物は、仮換地の場所に現に登記記録がある土地の地番 ③予定地番のかっこ書きの併記は任意 ④D1381は×、D1967は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PE-05_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第5章【PE-5】用。型4（複数肢の対比。コマ1は肢のカード）に型3（理由説明）を組み合わせた。所在欄に書くのは現に存する土地の地番（主である建物の土地が先、地下車庫の土地は後ろ）で、仮換地の予定地番は併記が任意、という対比に絞った。D1762には既存の4コマ、D1763は図解8があるので扱わない）
