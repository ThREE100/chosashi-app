# D1130 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-7】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-07_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1130（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 H28-Q05オ）。正解＝×（誤った記述）。
- 記事：`note-articles/h28-mondai/q05-tokureihoushiki.md` オ（特例方式でも、添付書面の原本の還付を請求することができる。規則附則24条2項が規則55条を準用する。還付を請求できない書面は、通常の書面申請と同じ）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢が『特例方式により提出された添付書面については、原本の還付を請求することができない』と、特例方式という特別な制度の名前を主語に出して、通常の書面申請とは別扱いに見せる。記事も『特例方式だから通常の申請と扱いが変わると思い込みやすい部分ほど、実は原則どおりの扱いが維持されている』と述べている。
- 【受験者の勘違い・定着していない点】（推測）①特例方式は電子申請の特例で、書面申請とは別の制度だから、書面申請の規定（原本還付）は及ばないと考える。②規則附則24条2項が、規則55条（添付書面の原本の還付請求）を特例方式による書面の提出に準用していることが定着していない。③還付を請求できない書面（印鑑に関する証明書、その申請のためにのみ作成された委任状その他の書面）と、特例方式であること自体を混同する。
- 【対比する制度】「書面申請の添付書面」⇔「特例方式で提出した書面」：書面申請の添付書面は、原本と相違ない旨を記載した謄本を提出して原本の還付を請求できる（規則55条）／特例方式で提出した書面にも規則55条が準用され（規則附則24条2項）、扱いは同じ。還付を請求できないのは、特例方式かどうかではなく、規則55条1項ただし書などに当たる書面である点。
- 【型の選び方】型：型5（整理カード併用。型1の思い込みと組み合わせ）。理由：結論の理由が『特例方式の書面は、還付されない書面の列挙に入っていない』という列挙の記憶なので、コマ3の右側は会話1往復と、『還付されない書面』の整理カードにした。コマ2は『書面申請の添付書面』と『特例方式で提出した書面』の左右の対比（準用）、コマ3の左は肢の言い分（✕）と正しい整理（✓）。壁＝『特例方式だから別扱い』という思い込み。
- コマごとに読者が言えること：コマ1＝電子申請で、添付書面を書面で提出する特例方式の書面は、原本の還付を請求できるかを問う肢。コマ2＝書面申請の添付書面は請求できる。特例方式の書面にも同じ規則が準用される。コマ3＝還付されない書面は3つ。特例方式の書面は入っていない。コマ4＝D1130は×。
- 記事の範囲：H28-Q05オ（規則附則24条2項・規則55条、規則55条1項ただし書）。還付を請求できない書面のうち『偽造などの疑いがある書面』は、規則55条5項（登記官は還付することができない）で、記事にも書かれている『偽造された書面その他不正な登記の申請のために用いられた疑いがある書面』にあたる。
- extra_refs：不動産登記規則55条1項（原本の還付の請求。ただし書：令16条2項・18条2項・19条2項などの印鑑に関する証明書、及び当該申請のためにのみ作成された委任状その他の書面は除く）、55条5項（偽造された書面その他の不正な登記の申請のために用いられた疑いがある書面は還付することができない）、規則附則24条2項（令附則5条1項の規定による書面の提出について、規則45条・49条・50条・55条を準用する。55条1項中『申請書の添付書面』は『当該書面』と読み替える）は、法令DB note-articles/laws/fudousan-touki-kisoku-1.md・fudousan-touki-kisoku-3.md で原文を確認した。
- 登場人物：人型は使わず、書面は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 特例方式でも、原本還付は請求できる | 「原本還付は」を黄色マーカー |
| コマ1 見出し | ラベル | ①　特例方式の書面は、返してもらえる？ | — |
| コマ1 図 | 図・カード | 原本の還付を請求できない？ / 電子申請で、申請情報を送った / 添付書面は、書面で登記所に提出した（特例方式） / その書面の原本の還付を、請求したい | — |
| コマ1 | 藍子（左・先に話す） | 特例方式の書面は、原本還付できませんよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。特例だから違う、と思う癖よ | 「特例だから違う」 |
| コマ2 見出し | ラベル | ②　書面申請と、同じ規則が及ぶ | — |
| コマ2 図 | 図・カード | 添付書面の原本の還付 / 特例方式は、書面申請と同じ扱い / 書面申請の添付書面 / 規則55条 / 原本の還付を請求できる / 原本と相違ない旨の謄本を提出する / 特例方式で提出した書面 / 規則附則24条2項 / 規則55条を準用する / だから、同じく請求できる / 特例方式でも、還付の扱いは同じ | — |
| コマ3 見出し | ラベル | ③　還付されない書面は、3つだけ | — |
| コマ3 図 | 図・カード | 特例方式の書面は、請求できない / 肢D1130の言い分 / 特例方式の書面も、請求できる / 規則附則24条2項が、規則55条を準用する / 還付されない書面（規則55条） / 印鑑に関する証明書 / その申請のためにのみ作成された委任状 / 偽造などの疑いがある書面 / 特例方式の書面は、この中にない / この中にない | — |
| コマ3 | 藍子（左・1番目） | 還付されない書面は、ないんですか？ | — |
| コマ3 | トリ先生（右・2番目） | あるわよ。この3つ。特例方式は入ってないの | 「特例方式は入ってない」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 特例方式でも、返してもらえるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。扱いは書面申請と同じよ | 「書面申請と同じ」 |
| コマ4 チェック欄 | 3項目（青✓） | 特例方式で提出した添付書面も、原本の還付を請求できる（規則附則24条2項） / 還付できないのは、印鑑に関する証明書やその申請のためにのみ作成された書面など / 特例方式だからといって、扱いは変わらない（肢D1130は×） | — |
| 結論帯 | 1行目 | 特例方式の添付書面も、原本の還付を請求できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1130　正解×（H28-Q05オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則55条1項（ただし書）・5項、規則附則24条2項。法令DB note-articles/laws/fudousan-touki-kisoku-1.md・fudousan-touki-kisoku-3.md と照合済み。特例方式は、令附則5条1項（電子申請の添付情報を書面を提出する方法で提供する特例）

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

TITLE BANNER: text 「特例方式でも、原本還付は請求できる」 in large bold letters; the part 「原本還付は」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　特例方式の書面は、返してもらえる？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「原本の還付を請求できない？」 at the top (a question badge only, with no check mark and no cross), and under it three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「電子申請で、申請情報を送った」. Card 2: 「添付書面は、書面で登記所に提出した（特例方式）」. Card 3: 「その書面の原本の還付を、請求したい」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「特例方式の書面は、
原本還付できません
よね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
特例だから違う、
と思う癖よ」 with the part 「特例だから違う」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　書面申請と、同じ規則が及ぶ」
- A small dark navy tag 「添付書面の原本の還付」 at the top left, with one line beside it: 「特例方式は、書面申請と同じ扱い」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「書面申請の添付書面」, a small tag 「規則55条」, two body lines: 「原本の還付を請求できる」, 「原本と相違ない旨の謄本を提出する」.
- Right card, heading 「特例方式で提出した書面」, a small tag 「規則附則24条2項」, two body lines: 「規則55条を準用する」, 「だから、同じく請求できる」.
- Under the two cards, one wide dark navy band with large white text 「特例方式でも、還付の扱いは同じ」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　還付されない書面は、3つだけ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 2 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 120 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 2 face icons and exactly 2 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「特例方式の書面は、請求できない」, body 「肢D1130の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「特例方式の書面も、請求できる」, body 「規則附則24条2項が、規則55条を準用する」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「還付されない書面（規則55条）」, with the same pale gray fill and a dark navy outline, containing exactly three short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「印鑑に関する証明書」, 「その申請のためにのみ作成された委任状」, 「偽造などの疑いがある書面」. Under the three rows, one small dark navy ribbon tag with white text 「特例方式の書面は、この中にない」, with the text 「この中にない」 highlighted with a yellow marker.
- The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 2 in the conversation column; face icon at the LEFT end of its own row): 「還付されない書面は、
ないんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 2 in the conversation column; face icon at the RIGHT end of its own row): 「あるわよ。この3つ。
特例方式は入ってないの」 with the part 「特例方式は入ってない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「特例方式でも、
返してもらえる
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
扱いは書面申請と
同じよ」 with the part 「書面申請と同じ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「特例方式で提出した添付書面も、原本の還付を請求できる（規則附則24条2項）」, 「還付できないのは、印鑑に関する証明書やその申請のためにのみ作成された書面など」, 「特例方式だからといって、扱いは変わらない（肢D1130は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「特例方式の添付書面も、原本の還付を請求できる」 with a yellow highlighter marker.
- Line 2: 「問題D1130　正解×（H28-Q05オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 所, 登, 肢, 規, 解, 記, 証, 請, 違, 還 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 2 face icons and exactly 2 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1 and panel 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (on the top-left card) and exactly one blue check mark (on the bottom-left card) and no other mark, and that the only blue check marks outside panel 3 are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「書面申請の添付書面」 and the right card has the heading 「特例方式で提出した書面」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ5_特例方式でも、原本還付は請求できる.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ5_特例方式でも、原本還付は請求できる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-07_01_tokurei-genpon-kanpu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で特例方式の書面の原本還付を問う肢、コマ2で書面申請と同じ規則が準用されること、コマ3で還付されない書面の3つが言える
- [ ] 工程C：構成表の全文言を記事（H28-Q05オ）・法令DB（規則55条、規則附則24条）と突き合わせ済み
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない
- [ ] 工程C：肝の確認：①書面申請の添付書面は、謄本を提出して原本の還付を請求できる（規則55条） ②特例方式で提出した書面にも規則55条が準用される（規則附則24条2項） ③還付されないのは、印鑑に関する証明書・その申請のためにのみ作成された書面・偽造などの疑いがある書面 ④D1130は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-07_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第2章【PB-7】用。型5（整理カード併用）。特例方式の書面も規則55条が準用されること、還付できない書面の整理に絞った）
