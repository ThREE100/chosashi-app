# D1633 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1633（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 R03-Q04エ）。正解＝×（誤った記述。調査士報告方式なら、委任状原本の提示は省略できる）。誤解4回とも〇と答えて誤答（2026-10-05・10-08・10-09・10-10）。
- 記事：`note-articles/r3-mondai/q04-denshi-shinsei.md` R03-Q04エ（調査士報告方式なら、委任状原本の提示は省略できる。令13条2項の提示の原則に対する、通達による取扱い）を軸に、R06-Q05イ・エ・オ（報告方式の対象は委任状、対象外は承諾書）を対比
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『当該委任状原本の提示を省略することはできません』と言い切る。令13条2項（登記官が定めた相当の期間内に書面を提示する）という条文の原則を覚えている受験者に、『条文が提示を求めているのだから、省略できない』と読ませる。記事によると、省略の定めは条文になく、通達による取扱い（調査士報告方式）で認められている。
- 【受験者の勘違い・定着していない点】（以下はすべて推測。根拠は回答履歴：2026-10-05・10-08・10-09・10-10の4回とも〇、つまり『省略できない』を正しいと判断し続けている。誤りの向きが毎回同じなので、思い込みが固定している）①条文の原則（令13条2項の提示）と、条文にない通達による取扱い（報告方式）を区別できていない。②同じ問の補助者ウ（D1632。報告を付けず調査士の電子署名だけでは、申請人作成の委任状は添付情報にならない。〇）を先に解いて、『委任状は調査士の署名では足りない』と一般化し、エも『省略できない』と答える（ウは報告方式でない場合の話で、エは報告方式の場合の話）。③報告方式の対象かどうかが『承諾を証する書面か』で仕分けられ、委任状は承諾書と違って対象になる、という仕分けが定着していない。④『〜できない』と言い切る否定形を、厳しい側＝安全側と感じて〇と答えやすい。
- 【対比する制度】「委任状」⇔「承諾書」：委任状は代理人の権限を証する書面で、承諾を証するものではないので、調査士報告方式の対象（原本の提示は原則不要）／承諾書は第三者の承諾を証する書面なので、対象外（原本の提示が必要）（結論が逆になる点）。あわせて、条文の原則（令13条2項は提示）と報告方式（通達による取扱い。提示を原則として求めない）の対比も、コマ2で示す。
- 【型の選び方】型：型3（第三案・理由説明）。理由…4回とも同じ誤りなので、『省略できる』という結論の暗記ではなく、なぜ委任状は省略できて、承諾書はできないのか（承諾を証する書面かどうかで仕分けられる）の理由が読み取れる構成にした。壁（初見の読者が引っかかる理解の壁）＝条文は提示を求めているのに、なぜ委任状は省略できるのか、どの書面が省略できる側なのかが見えない。コマ2に型2の押さえどころカード（条文の原則と通達の取扱い）を入れた混成。
- 記事の範囲：R03-Q04エ（調査士報告方式の定義、令13条2項の提示の原則に対する法務省の通達による特例、条文に省略の定めはない）。R03-Q04ウ（申請人が作成した委任状の電磁的記録には申請人自身の電子署名が必要）は兄弟肢D1632で、コマ2の帯で『報告方式でない場合』として触れる。
- extra_refs：対比『委任状は対象、承諾書は対象外』と、判断の軸『第三者の許可・同意・承諾を証する情報かどうか』は、肢の記事（R03-Q04エ）になく、R06-Q05の記事（note-articles/r6-mondai/q05-chousashi-houkoku-houshiki.md。イ＝委任状は対象、エ・オ＝承諾書は対象外）から取った。報告方式の定義と『報告を付けない場合は調査士の電子署名だけでは添付情報にならない』は、note-articles/column/nigate-24-houjin-shikaku-shoumei-toikake-flow.md の手順5と兄弟肢D1632の記事。いずれも肢の記事にない整理で、ユーザーに『記事にない整理』と伝える。通達番号は記事間で表記が食い違い、原文も法令DBにないので、図には入れず『通達による取扱い』とだけ書く。
- 記事間の食い違いの疑い（図には入れない）：R06-Q05の記事が自ら指摘しているとおり、令13条1項の括弧書きは『申請人又はその代表者若しくは代理人が作成したもの』を除いており、委任状は一見この除外に当たるのに、通達の仕分けでは報告方式の対象とされる。この関係を説明する資料は確認できていない。図は通達の仕分け（承諾を証する書面かどうか）に従い、条文の根拠だとは書かない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。『申請人』『調査士』を人型タグ、『登記所』を建物アイコンでコマ1で紹介してから使う。『承諾書』『表題部所有者』『抵当権者』は書面と名称のラベルで、人物としては描かない。
- 矢印の意味：矢印はコマ1の1本だけ（調査士から登記所へ『電子申請で提供する』）。申請人と調査士の間は矢印のない細い線。コマ2は矢印なし（『特例』の小さなラベルのみ）、コマ3・4も矢印なし。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は左（承諾書：提示が必要）＝赤✕1つ、右（委任状：提示は原則不要）＝青✓1つ。この✓✕は『報告方式で原本の提示が要るか』の意味で、肢の〇×とは別（肢の〇×はコマ4で示す）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボン・帯は濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央）、コマ2＝none（条文の原則と通達の取扱いの図だけ）、コマ3＝faces（左に2枚のカードとリボン、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝両方（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1633～R03-Q04エ～

## note記事の冒頭文

調査士が代理人として、電子申請で土地の合筆の登記を申請します。委任状を確認してスキャンし、調査士の電子署名と調査に関する報告を添える調査士報告方式のとき、委任状の原本の提示は省略できないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和3年度　第4問　エ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 報告方式なら、委任状の原本の提示は省略できる | 「原本の提示は省略できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 申請人 / 調査士 / 登記所 / 委任状（原本） / ①　電子申請で提供する / スキャンした委任状、調査士の電子署名、調査に関する報告 / 委任状の原本の提示は、省略できない？ | — |
| コマ1 | 藍子（左・先に話す） | 原本は、提示しないとだめですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。報告方式かどうか見てごらん | 「報告方式」 |
| コマ2 見出し | ラベル | ②　条文の原則と通達の取扱い | — |
| コマ2 図 | 図・カード | 出題者のねらい / 条文の原則と、報告方式の取扱いを見分ける / 特例 / 令13条2項 / 条文の原則 / 登記官が定めた相当の期間内に、書面を提示する / 調査士報告方式 / 通達による取扱い / 電子署名と報告を添えれば、原本の提示を省略できる / 委任状は、報告方式でなく調査士の電子署名だけなら添付情報にならない（肢D1632） | — |
| コマ3 見出し | ラベル | ③　なぜ委任状は省略できるの？ | — |
| コマ3 図 | 図・カード | 承諾書 / 表題部所有者・抵当権者 / 第三者の承諾を証する書面。報告方式の対象外 / 提示が必要 / 委任状 / 代理人の権限を証する書面。承諾を証するものではない / 提示は原則不要 / ひっかけ：省略することはできない、という言い切り | — |
| コマ3 | 藍子（左・1番目） | 令13条2項は、提示とありますよね？ | — |
| コマ3 | トリ先生（右・2番目） | それは原則。報告方式は通達の取扱いよ | 「通達の取扱い」 |
| コマ3 | 藍子（左・3番目） | では、委任状もその対象なんですか？ | — |
| コマ3 | トリ先生（右・4番目） | ええ。承諾を証する書面ではないのよ | 「承諾を証する書面ではない」 |
| コマ4 見出し | ラベル | ④　結論は× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 省略できない、は×なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。承諾書とは分けて覚えるのよ | 「承諾書とは分けて」 |
| コマ4 チェック欄 | 3項目（青✓） | 調査士報告方式なら、委任状の原本の提示を省略できる / 令13条2項の提示の原則に対する、通達による取扱い / 委任状は承諾を証する書面でないので対象。承諾書は対象外で提示が必要 | — |
| 結論帯 | 1行目 | 報告方式なら、委任状の原本の提示は省略できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1633　正解×（R03-Q04エ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「報告方式なら、委任状の原本の提示は省略できる」 in large bold letters; the part 「原本の提示は省略できる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A relation diagram in the center of the panel, laid out ONE row from left to right: one faceless pictogram tag in light gray-blue labeled 「申請人」, one faceless pictogram tag in light gray-blue labeled 「調査士」, and one flat registry-office building icon labeled 「登記所」.
- Between 「申請人」 and 「調査士」, one plain thin dark navy line with no arrowhead and a small label 「委任状（原本）」.
- One dark navy arrow from 「調査士」 to 「登記所」 labeled 「①　電子申請で提供する」 (this arrow means submitting the application information, not a sale and not a payment).
- Under the arrow, a white card with a dark navy outline: 「スキャンした委任状、調査士の電子署名、調査に関する報告」.
- A small question badge 「委任状の原本の提示は、省略できない？」 sits at the top (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「原本は、提示しないと
だめですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
報告方式かどうか
見てごらん」 with the part 「報告方式」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　条文の原則と通達の取扱い」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「条文の原則と、報告方式の取扱いを見分ける」.
- Two large cards side by side, both with the same pale gray fill, a dark navy outline, and a dark navy heading, joined in the middle by a small plain dark navy label 「特例」 (a label only, no arrow). Left card, heading 「令13条2項」, small tag 「条文の原則」, body 「登記官が定めた相当の期間内に、書面を提示する」. Right card, heading 「調査士報告方式」, small tag 「通達による取扱い」, body 「電子署名と報告を添えれば、原本の提示を省略できる」.
- At the bottom, one wide dark navy band with white text 「委任状は、報告方式でなく調査士の電子署名だけなら添付情報にならない（肢D1632）」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ委任状は省略できるの？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two cards side by side, both exactly the same size and top-aligned, with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card.
- Left card, heading 「承諾書」, small tag 「表題部所有者・抵当権者」, body 「第三者の承諾を証する書面。報告方式の対象外」, then the line 「提示が必要」, with ONE red cross only (no check mark on this card).
- Right card, heading 「委任状」, body 「代理人の権限を証する書面。承諾を証するものではない」, then the line 「提示は原則不要」, with ONE blue check mark only (no cross on this card).
- Under the two cards, one dark navy ribbon with large white text 「ひっかけ：省略することはできない、という言い切り」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「令13条2項は、
提示とありますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それは原則。
報告方式は通達の
取扱いよ」 with the part 「通達の取扱い」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、委任状も
その対象なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。承諾を証する
書面ではないのよ」 with the part 「承諾を証する書面ではない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×」
- 藍子 bubble (left, spoken first): 「省略できない、は
×なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
承諾書とは分けて
覚えるのよ」 with the part 「承諾書とは分けて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「調査士報告方式なら、委任状の原本の提示を省略できる」, 「令13条2項の提示の原則に対する、通達による取扱い」, 「委任状は承諾を証する書面でないので対象。承諾書は対象外で提示が必要」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「報告方式なら、委任状の原本の提示は省略できる」 with a yellow highlighter marker.
- Line 2: 「問題D1633　正解×（R03-Q04エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 対, 当, 所, 承, 抵, 権, 登, 肢, 解, 記, 証, 請, 諾, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「原則」 is spelled exactly like this everywhere (never 「思則」); confirm that the word 「第三者」 is spelled exactly like this everywhere (never 「時三者」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 調査士報告方式で申請 | 薄い黄色のマーカー |
| タイトル2行目 | 委任状の原本は不要？ | 「不要？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1633　R03-Q04エ | — |

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
調査士報告方式で申請
Line 2 is larger; the phrase 不要？ is red-orange and the rest is dark navy:
委任状の原本は不要？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1633　R03-Q04エ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a laptop showing an online filing screen beside a small document scanner
Right side: a blank power-of-attorney sheet and a small report paper with a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 調, 査, 士, 報, 告, 方, 式, 申, 請, 委, 任, 状, 原, 本, 不, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1633～R03-Q04エ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1633～R03-Q04エ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1633～R03-Q04エ～_v01.png ／ 4コマ解説図解D1633～R03-Q04エ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1633_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、申請人・調査士・登記所の関係と、電子申請で何を提供するか（スキャンした委任状・電子署名・調査に関する報告）が言える。コマ2で、令13条2項（提示）は原則、報告方式は通達による取扱いで、提示を省略できる、と言える。コマ3で、委任状は承諾を証する書面でないので対象（提示は原則不要）、承諾書は対象外（提示が必要）と言える
- [ ] 工程C：肝の確認：①条文の原則（提示）と通達の取扱い（報告方式）で結論が逆 ②報告方式の中でも、委任状（対象）と承諾書（対象外）で結論が逆 ③肢の『省略することはできない』は、委任状が対象なので×
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『調査士報告方式』『令13条2項』『登記官が定めた相当の期間内に書面を提示する』『通達による取扱い』（R03-Q04エ）、『代理人の権限を証する書面』『承諾を証する書面』『第三者の承諾を証する書面』『対象外』（R06-Q05）。通達番号・令13条1項の括弧書きは図に入れていない
- [ ] 工程C：コマ1・2に印がなく、コマ3は左赤✕・右青✓、コマ4だけ青✓の暗記3点。コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）

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

- 2026-10-10 v01：新規作成（一問一答で4回とも〇と誤答した肢。型3。条文の原則と通達の取扱い、委任状と承諾書の対比。R06-Q05の記事から対比を足した）
