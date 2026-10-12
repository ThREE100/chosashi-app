# D1795 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1795（不動産登記法／区分建物・敷地権・共用部分、出典 R04-Q18ア）。正解＝×（誤った記述）。誤解敷地権は土地の全部の権利でなければならず、共有の持分は敷地権にならないと考える。
- 記事：`note-articles/r4-mondai/q18-shikichiken.md` ア（共有持分権を敷地権として、丁区分建物の表題登記を申請できる）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文が『甲土地及び乙土地のAの共有持分権を敷地権として』と、土地の全部ではなく持分だけを敷地権にすると書き、『申請することはできない』と言い切る。共有の持分は敷地権にならないと読ませる。前提条件に『分離処分可能規約はない』と書かれている点が、結論を決める。
- 【受験者の勘違い・定着していない点】（推測）①敷地権は土地の全部の権利（単独の所有権）でなければならず、共有の持分は敷地権にならないと考える。②敷地権になるための条件（敷地利用権であること・登記されていること・分離して処分できないこと）が結びついていない。③分離処分可能規約がないという前提が、結論を決める条件だと気づかない。
- 【対比する制度】「分離処分可能規約がない」⇔「分離処分可能規約がある」：規約がないときは、数人で有する敷地利用権（共有の持分も含む）は専有部分と分離して処分できないので、敷地権になる（区分所有法22条1項本文）／規約があるときは、分離して処分できるので、敷地権にならない（同項ただし書。同記事エ・オ）（結論が逆になる点）。
- 【型の選び方】型：型2（押さえどころ）＋型1の対比（規約の有無）。理由：壁は『共有の持分でも敷地権になる理由と、その条件が見えない』こと。コマ1で前提（A・B共有の土地、規約なし）を図にし、コマ2で敷地権になる3つの条件のカード、コマ3で『本番での読み方3ステップ』（ひっかけを1か所のリボン）にした。『一部の区分建物だけ規約を設定できる（エ）』や『分離処分の前提としての抹消（オ）』は肢アの結論を決めないので入れない。
- 記事の範囲：R04-Q18ア（敷地利用権が数人で有する登記された所有権・地上権・賃借権である場合は専有部分と一体化し、分離して処分できない〔区分所有法22条1項〕。甲・乙土地がA・B共有で所有権登記があるので、丁区分建物とAの共有持分権は一体化し、Aは共有持分権を敷地権として丁区分建物の表題登記を申請する）。同記事エ・オ（分離処分可能規約を設定し敷地権の登記を抹消して初めて分離できる）で規約ありの対比を補った。
- extra_refs：不動産登記法44条1項9号（法令DB note-articles/laws/fudousan-touki-hou.md 第44条）で、敷地権が『敷地利用権（登記されたものに限る。）であって、区分所有法22条1項本文により専有部分と分離して処分することができないもの』であることを確認した。この3つの条件は肢D1795の記事アにはないが、同じ分野のH30-Q11の記事〔⑥〕・D1366の4コマにある敷地権の定義と同じ。区分所有法22条1項（同 kubunshoyuu-hou.md）の本文・ただし書も確認した。
- 登場人物：Ａ・Ｂを、コマ1の図で顔なしの人型ピクトグラムとして紹介する。丁区分建物はＡ、戊区分建物はＢの所有。丙土地・集会・規約の決議（ウ・イ）は肢アの結論を決めないので図に入れない。
- 矢印の意味：矢印は使わない。コマ1は図、コマ2は縦の別カード、コマ3は上下の別カード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。人物は全員同じ薄い灰青のピクトグラム＋濃紺のタグ。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（キャラは通常サイズで左右の端、図は中央）、コマ2＝none（図が主役。縦のカード3枚）、コマ3＝faces（左に3ステップのカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1795～R04-Q18ア～

## note記事の冒頭文

甲土地と乙土地は、ＡとＢの共有で所有権の登記もされています。丁区分建物の表題登記を申請するとき、Ａは自分の共有持分権を敷地権にすることになるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和4年度　第18問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 共有の持分でも、敷地権になる | 「敷地権になる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　共有の持分は、敷地権になる？ | — |
| コマ1 図 | 図・カード | 甲土地・乙土地 / ＡとＢの共有（所有権の登記がある） / Ａ / Ｂ / 丁区分建物（Ａ） / 戊区分建物（Ｂ） / 分離処分可能規約はない / Ａの共有持分権を敷地権にして、丁区分建物の表題登記を申請できる？ | — |
| コマ1 | 藍子（左・先に話す） | 共有の持分は、敷地権にならないのでは？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。前提の規約を見なさい | 「前提の規約」 |
| コマ2 見出し | ラベル | ②　敷地権になる3つの条件 | — |
| コマ2 図 | 図・カード | 敷地権 / 3つの条件がそろえば、敷地権（法44条1項9号） / 敷地利用権である / 建物の敷地に関する権利（所有権・地上権・賃借権など） / 登記されている / 甲土地・乙土地には、ＡとＢの所有権の登記がある / 分離して処分できない / 数人で有する権利は、専有部分と分離処分できない（区分所有法22条1項本文） | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　どんな権利か / Ａの共有持分権も、敷地利用権になる / ステップ2　登記されているか / 所有権の登記があるので、登記されたもの / ステップ3　規約があるか / 分離処分可能規約がない（この肢）：敷地権になる / 分離処分可能規約がある：分離処分でき、敷地権にならない / ひっかけ：共有の持分だから敷地権にならない、と読ませる | — |
| コマ3 | 藍子（左・1番目） | 共有の持分だと、全体じゃないですよね？ | — |
| コマ3 | トリ先生（右・2番目） | そこが罠。数人で有する権利も一体よ | 「数人で有する権利も一体」 |
| コマ3 | 藍子（左・3番目） | 規約があったら、どうなりますか？ | — |
| コマ3 | トリ先生（右・4番目） | 分離して処分でき、敷地権にならないのよ | 「敷地権にならない」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 共有の持分でも、敷地権になるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。できないと書けば×よ | 「できないと書けば×」 |
| コマ4 チェック欄 | 3項目（青✓） | 数人で有する敷地利用権は、規約がなければ専有部分と分離処分できない（区分所有法22条1項本文） / 敷地権＝登記された敷地利用権で、分離処分できないもの（法44条1項9号） / 共有の持分でも敷地権になる。分離処分可能規約があれば、敷地権にならない | — |
| 結論帯 | 1行目 | 共有の持分でも、規約がなければ敷地権になる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1795　正解×（R04-Q18ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法44条1項9号（法令DB note-articles/laws/fudousan-touki-hou.md 第44条）：建物又は附属建物が区分建物である場合において、当該区分建物について区分所有法2条6項に規定する敷地利用権（登記されたものに限る。）であって、区分所有法22条1項本文（同条3項において準用する場合を含む。）の規定により区分所有者の有する専有部分と分離して処分することができないものがあるときは、その敷地権が登記事項になる。この3つの条件は肢D1795の記事アにはないが、同分野のH30-Q11の記事の敷地権の定義〔⑥〕と同じ
- 区分所有法22条1項（法令DB note-articles/laws/kubunshoyuu-hou.md 第22条）：敷地利用権が数人で有する所有権その他の権利である場合には、区分所有者は、その有する専有部分とその専有部分に係る敷地利用権とを分離して処分することができない。ただし、規約に別段の定めがあるときは、この限りでない。記事のアにも22条1項の引用がある
- 分離処分可能規約があるとき（本文の対比）：記事のエ・オによる（規約を設定し、敷地権の登記を抹消して初めて分離して処分できる）。肢アの前提条件は『分離処分可能規約はない』

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed (cartoon expression marks such as ！ and ？ beside a character's face are decoration, not text, and are allowed).

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

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

TITLE BANNER: text 「共有の持分でも、敷地権になる」 in large bold letters; the part 「敷地権になる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　共有の持分は、敷地権になる？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: one wide land block labeled 「甲土地・乙土地」, with the caption 「ＡとＢの共有（所有権の登記がある）」, and two faceless flat pictogram figures in exactly the same single light gray-blue color standing on it side by side, with dark navy tags 「Ａ」 (left) and 「Ｂ」 (right). Above the land block, two small building icons side by side labeled 「丁区分建物（Ａ）」 (left) and 「戊区分建物（Ｂ）」 (right). The shapes are joined only by plain thin lines, with no arrow anywhere.
- A small dark navy tag under the land block 「分離処分可能規約はない」.
- At the top, a small question badge in a gray fill with dark navy text 「Ａの共有持分権を敷地権にして、丁区分建物の表題登記を申請できる？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「共有の持分は、
敷地権にならないのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
前提の規約を
見なさい」 with the part 「前提の規約」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　敷地権になる3つの条件」
- A small dark navy tag 「敷地権」 at the top left, with one line beside it: 「3つの条件がそろえば、敷地権（法44条1項9号）」.
- Three SEPARATE cards stacked from top to bottom in the center, all exactly the same size, each with the same pale gray fill, a dark navy outline, a dark navy heading placed fully INSIDE the card and one short body line, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「敷地利用権である」, body 「建物の敷地に関する権利（所有権・地上権・賃借権など）」.
- Card 2, heading 「登記されている」, body 「甲土地・乙土地には、ＡとＢの所有権の登記がある」.
- Card 3, heading 「分離して処分できない」, body 「数人で有する権利は、専有部分と分離処分できない（区分所有法22条1項本文）」.
- The three cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked step cards from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge and a dark navy heading placed INSIDE the card, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Step card 1, heading 「ステップ1　どんな権利か」, body 「Ａの共有持分権も、敷地利用権になる」.
- Step card 2, heading 「ステップ2　登記されているか」, body 「所有権の登記があるので、登記されたもの」.
- Step card 3, heading 「ステップ3　規約があるか」, two body lines: 「分離処分可能規約がない（この肢）：敷地権になる」 and 「分離処分可能規約がある：分離処分でき、敷地権にならない」, and a dark navy ribbon tag with large white text 「ひっかけ：共有の持分だから敷地権にならない、と読ませる」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「共有の持分だと、
全体じゃないですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「そこが罠。数人で
有する権利も
一体よ」 with the part 「数人で有する権利も一体」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「規約があったら、
どうなりますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「分離して処分でき、
敷地権に
ならないのよ」 with the part 「敷地権にならない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「共有の持分でも、
敷地権になるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
できないと書けば×よ」 with the part 「できないと書けば×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「数人で有する敷地利用権は、規約がなければ専有部分と分離処分できない（区分所有法22条1項本文）」, 「敷地権＝登記された敷地利用権で、分離処分できないもの（法44条1項9号）」, 「共有の持分でも敷地権になる。分離処分可能規約があれば、敷地権にならない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「共有の持分でも、規約がなければ敷地権になる」 with a yellow highlighter marker.
- Line 2: 「問題D1795　正解×（R04-Q18ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 権, 物, 番, 登, 肢, 規, 解, 記, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the faceless pictograms Ａ, Ｂ are all drawn in exactly the same single light gray-blue color, the same shade for every one of them (they differ only by their letter tags); confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 共有の持分は | 薄い黄色のマーカー |
| タイトル2行目 | 敷地権になる？ | 「敷地権になる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1795　R04-Q18ア | — |

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
共有の持分は
Line 2 is larger; the phrase 敷地権になる？ is red-orange and the rest is dark navy:
敷地権になる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1795　R04-Q18ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a simple apartment building standing on a shared land plot, no text
Right side: two faceless figures standing on one land plot divided by a thin line, no text

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 共, 有, 持, 分, 敷, 地, 権, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1795～R04-Q18ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1795～R04-Q18ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1795～R04-Q18ア～_v01.png ／ 4コマ解説図解D1795～R04-Q18ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1795_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『甲・乙土地はＡ・Ｂの共有で所有権の登記があり、分離処分可能規約はない。Ａは自分の共有持分権を敷地権にして丁区分建物の表題登記を申請できるか』、コマ2で『敷地権になる条件は、敷地利用権であること・登記されていること・分離して処分できないこと』、コマ3で『共有の持分でも数人で有する権利は分離処分できない。規約があれば分離処分でき、敷地権にならない』が言える
- [ ] 工程C：肝の確認：①数人で有する敷地利用権（共有の持分を含む）は、規約がなければ専有部分と分離処分できない（区分所有法22条1項本文）②敷地権は、登記された敷地利用権で、分離処分できないもの（法44条1項9号）③規約があれば分離処分でき敷地権にならない（同項ただし書。記事エ・オ）④肢D1795は『できない』と書くので×
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『共有持分権』『敷地権』『分離処分可能規約』『区分所有法22条1項』『法44条1項9号』『登記されたもの』。出題当時と今の言い方の違い・集会の議事録の決議要件〈ウ〉は入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない

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

- 2026-10-12 v01：新規作成（型2の押さえどころ＋型1の対比。『共有の持分でも敷地権になる』理由を、敷地権の3つの条件〔法44条1項9号〕と、分離処分可能規約の有無〔区分所有法22条1項本文・ただし書〕の対比に絞った。ウ〔集会の議事録〕・イ〔1か月〕・エ・オは入れていない）
