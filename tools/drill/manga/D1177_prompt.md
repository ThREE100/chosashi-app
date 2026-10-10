# D1177 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1177（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H28-Q15ウ）。正解＝〇（正しい記述。表題登記がない建物の所有者又は表題登記がある建物の表題部所有者の一方が単独で申請できる）。誤解しやすい肢。
- 記事：`note-articles/h28-mondai/q15-gattai.md` H28-Q15ウ（表題登記のない建物との合体でも、AまたはBの一方が単独で申請できる。法49条1項1号。表示に関する登記には共同申請の定め〈法60条〉がない）を軸に、H21-Q18イ（所有権の登記名義人が異なる建物の合体でも、全員の共同申請ではない）を対比
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『Ａ又はＢが単独で申請することができる』と、申請の場面なのに『単独で』と言い切る。持ち主が別々で、しかも一方は表題登記もない建物なので、『別々の持ち主なら、2人がそろって共同して申請するはず』と読ませる。権利に関する登記は登記権利者と登記義務者が共同して申請する（法60条）という原則の記憶に引かれやすい。
- 【受験者の勘違い・定着していない点】（以下はすべて推測。肢の言い回しと、同じ問の兄弟肢、記事の『ここが違う』から立てた、受験者が一般にしやすい勘違い）①権利に関する登記の共同申請の原則（法60条）を、表示に関する登記である合体による登記等にも当てはめ、『持ち主が別々なら共同申請』と考える。②ＡとＢは共有者ではないので、『共有者の1人が保存行為として単独で申請できる』という整理（民法252条5項）では説明がつかず、『共有でもないのに単独は変だ』と感じる。③『合体による登記等』が、合体後の建物の表題登記と合体前の建物の表題部の登記の抹消の2つであり、表題登記がない甲建物のＡが乙建物の分まで申請してよいのか不安になる。④条文の『又は』を『それぞれが自分の建物の分を』と読み、『一方が全部を単独で』と読めていない。
- 【対比する制度】「権利に関する登記」⇔「合体による登記等」：権利に関する登記は、法令に別段の定めがない限り登記権利者と登記義務者が共同してする（法60条）／合体による登記等は、共同申請の定めがなく、法49条1項1号が定める『表題登記がない建物の所有者又は表題登記がある建物の表題部所有者』のうちの一方が単独でできる（結論が逆になる点）。同じ問の肢D0497（H21-Q18イ。名義人が別々の建物の合体を全員が共同してしなければならない、は×）とは同じ向きの結論で、矛盾しない。
- 【型の選び方】型：型3（第三案・理由説明）。理由…同じ誤りを繰り返しやすい肢なので、『単独でできる』という結論の暗記ではなく、なぜ共同申請でなくてよいのか（報告的登記で、共同申請の定めは権利に関する登記のもの）の理由が読み取れる構成にした。壁（初見の読者が引っかかる理解の壁）＝持ち主が別々の建物の合体なのに、なぜ片方だけで申請できるのかが見えない。コマ2に型1の対比（共同申請か単独か）を左右のカードで入れた混成。
- 記事の範囲：H28-Q15ウ（合体による登記等は既に生じた事実をそのまま登記に反映させる報告的登記。法49条1項1号。表示に関する登記には共同申請の定め〈法60条〉がない。ＡとＢは共有者ではないので民法252条5項の問題ではない。Ａだけの判断でもＢだけの判断でも申請できる）。法49条1項1号の文言と法60条の文言は、法令DB（note-articles/laws/fudousan-touki-hou.md）で原文を確認した。
- extra_refs：兄弟の肢D0497（note-articles/h21-mondai/q18-gattai-touki.md イ。名義人が異なる建物の合体でも、申請する資格のある者のうち誰か一人が申請すれば足りる）は、コマ4のチェック欄で肢IDつきで触れるだけで、新しい整理は足していない。法60条の『権利に関する登記の申請は、法令に別段の定めがある場合を除き、登記権利者及び登記義務者が共同してしなければならない』は、法令DBの原文。いずれも肢の記事（H28-Q15ウ）が引く範囲。
- 同じ問の肢で今回は図に入れない肢：D1175（ア。所有権の登記名義人となった者の1か月以内の申請義務〈法49条4項〉。〇）、D1176（イ。抵当権の内容が同一なら持分の記載を省略できる。〇）、D1178（エ。賃借権は存続登記の対象でなく移記されない。×）、D1179（オ。主たる建物と附属建物の合体は合体による登記等ではなく表題部の変更登記。×）。法49条1項の他の号（2号・4号・6号は所有権の登記も併せて申請）は、肢の記事にないので図に入れない。
- 登場人物：Ａ（表題登記がない甲建物の所有者）とＢ（乙建物の表題部所有者）の2人だけ。コマ1で人型タグ付きで紹介してから使う。合体後の建物は『合体後の建物』のラベル。
- 矢印の意味：矢印はコマ1の『工事』（2棟が1棟になる出来事）の1本だけ。申請や取引の矢印はない。コマ2・3・4は矢印なし。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は左（ＡとＢが共同して申請する）＝赤✕1つ、右（ＡかＢの一方が単独で申請できる）＝青✓1つ。この✓✕は『申請のしかたとして正しいか』の意味で、肢の〇×とは別（肢は〇。正解はコマ4に示す）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボン・帯は濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央）、コマ2＝none（共同申請と単独申請の左右のカードと、法49条1項1号の帯）、コマ3＝faces（左に2枚のカードとリボンと例、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝両方（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1177～H28-Q15ウ～

## note記事の冒頭文

表題登記がない甲建物の所有者Ａと、乙建物の表題部所有者Ｂがいて、この2棟が合体しました。合体による登記等の申請は、ＡかＢのどちらか一方だけでできるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成28年度　第15問　ウ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 合体による登記等は、一方だけで申請できる | 「一方だけで申請できる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 甲建物 / 乙建物 / 表題登記なし / 表題登記あり / Ａ / 所有者 / Ｂ / 表題部所有者 / 工事 / 合体後の建物 / 合体による登記等 / 合体後の建物の表題登記と、合体前の建物の表題部の登記の抹消 / 申請できるのは誰？ | — |
| コマ1 | 藍子（左・先に話す） | 持ち主が別々なら、2人そろって申請ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。申請できる人を条文で見るのよ | 「申請できる人」 |
| コマ2 見出し | ラベル | ②　共同申請か、単独か | — |
| コマ2 図 | 図・カード | 出題者のねらい / 共同申請と、単独で申請できる場合を見分ける / 権利に関する登記 / 法60条 / 登記権利者と登記義務者が、 / 共同して申請する / 合体による登記等 / 法49条1項1号 / 理由：生じた事実を反映する報告的登記 / 申請できる者の一方が、単独で申請できる / 法49条1項1号：表題登記がない建物の所有者又は表題登記がある建物の表題部所有者 | — |
| コマ3 見出し | ラベル | ③　なぜ単独でいいの？ | — |
| コマ3 図 | 図・カード | よくある勘違い / 持ち主が違うから、ＡとＢが共同して申請する / 正しい整理 / ＡかＢの一方が、単独で申請できる / ひっかけ：単独で申請することができる、という言い方 / たとえば：Ａの未登記の倉庫とＢが表題部所有者の乙建物が合体したら、Ａだけの判断でも、Ｂだけの判断でも申請できる | — |
| コマ3 | 藍子（左・1番目） | 持ち主が違うのに、単独でいいんですか？ | — |
| コマ3 | トリ先生（右・2番目） | そこが罠。共同申請と混ぜたわね | 「共同申請」 |
| コマ3 | 藍子（左・3番目） | 合体の登記は、なぜ単独でいいんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 生じた事実を反映する報告的登記だからよ | 「報告的登記」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 単独でできる、は〇なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。共同申請と混ぜないことよ | 「共同申請と混ぜない」 |
| コマ4 チェック欄 | 3項目（青✓） | 合体による登記等は、ＡかＢの一方が単独で申請できる / 理由：既に生じた事実を反映する報告的登記 / 持ち主が別々でも全員の共同申請ではない（肢D0497は×） | — |
| 結論帯 | 1行目 | 合体による登記等は、一方だけで申請できる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1177　正解〇（H28-Q15ウ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ Ｂ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ, Ｂ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「合体による登記等は、一方だけで申請できる」 in large bold letters; the part 「一方だけで申請できる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A before-and-after diagram in the center of the panel, left to right.
- On the left, two flat house icons side by side labeled 「甲建物」 and 「乙建物」. Under 「甲建物」 a small tag 「表題登記なし」, and under 「乙建物」 a small tag 「表題登記あり」. Each house has a faceless owner pictogram in the same light gray-blue color: a tag 「Ａ」 beside the left house with the small label 「所有者」, and a tag 「Ｂ」 beside the right house with the small label 「表題部所有者」.
- A dark navy arrow (this arrow means a construction event, not a sale or an application) labeled 「工事」 points to the right, where ONE larger merged house icon is drawn, labeled 「合体後の建物」.
- Under the merged house, a card with heading 「合体による登記等」 and body 「合体後の建物の表題登記と、合体前の建物の表題部の登記の抹消」.
- A small question badge 「申請できるのは誰？」 sits above the card (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「持ち主が別々なら、
2人そろって
申請ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
申請できる人を
条文で見るのよ」 with the part 「申請できる人」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　共同申請か、単独か」
- A full-width concept diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「共同申請と、単独で申請できる場合を見分ける」.
- Two large cards side by side, both exactly the same size and top-aligned, with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card. Left card, heading 「権利に関する登記」, small tag 「法60条」, two body lines: 「登記権利者と登記義務者が、」, 「共同して申請する」. Right card, heading 「合体による登記等」, small tag 「法49条1項1号」, two body lines: 「理由：生じた事実を反映する報告的登記」, 「申請できる者の一方が、単独で申請できる」.
- At the bottom, one wide dark navy band with white text 「法49条1項1号：表題登記がない建物の所有者又は表題登記がある建物の表題部所有者」.
- There is no check mark and no cross anywhere in this panel.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ単独でいいの？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two cards side by side, both exactly the same size and top-aligned, with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card.
- Left card, heading 「よくある勘違い」, body 「持ち主が違うから、ＡとＢが共同して申請する」, with ONE red cross only (no check mark on this card).
- Right card, heading 「正しい整理」, body 「ＡかＢの一方が、単独で申請できる」, with ONE blue check mark only (no cross on this card).
- Under the two cards, one dark navy ribbon with large white text 「ひっかけ：単独で申請することができる、という言い方」.
- Under the ribbon, one wide example strip with the same pale gray fill and a dark navy outline and dark navy text: 「たとえば：Ａの未登記の倉庫とＢが表題部所有者の乙建物が合体したら、Ａだけの判断でも、Ｂだけの判断でも申請できる」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「持ち主が違うのに、
単独でいいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「そこが罠。
共同申請と
混ぜたわね」 with the part 「共同申請」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「合体の登記は、
なぜ単独で
いいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「生じた事実を反映する
報告的登記だからよ」 with the part 「報告的登記」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「単独でできる、は
〇なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
共同申請と
混ぜないことよ」 with the part 「共同申請と混ぜない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「合体による登記等は、ＡかＢの一方が単独で申請できる」, 「理由：既に生じた事実を反映する報告的登記」, 「持ち主が別々でも全員の共同申請ではない（肢D0497は×）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「合体による登記等は、一方だけで申請できる」 with a yellow highlighter marker.
- Line 2: 「問題D1177　正解〇（H28-Q15ウ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 建, 所, 権, 物, 登, 肢, 解, 記, 請, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the word 「合体」 is spelled exactly like this everywhere (never 「合併」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the faceless pictograms Ａ, Ｂ are all drawn in exactly the same single light gray-blue color, the same shade for every one of them (they differ only by their letter tags); confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 表題登記なしの建物と合体 | 薄い黄色のマーカー |
| タイトル2行目 | どちらが申請できる？ | 「どちらが申請できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1177　H28-Q15ウ | — |

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
表題登記なしの建物と合体
Line 2 is larger; the phrase どちらが申請できる？ is red-orange and the rest is dark navy:
どちらが申請できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1177　H28-Q15ウ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: two small houses standing side by side, one of them drawn with a dashed outline, and a construction crane behind
Right side: a blank registry sheet with a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 表, 題, 登, 記, 建, 物, 合, 体, 申, 請, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1177～H28-Q15ウ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1177～H28-Q15ウ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1177～H28-Q15ウ～_v01.png ／ 4コマ解説図解D1177～H28-Q15ウ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1177_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、甲建物（表題登記なし・所有者Ａ）と乙建物（表題登記あり・表題部所有者Ｂ）が合体した場面で、合体による登記等の申請人が問われていると言える。コマ2で、権利に関する登記は共同申請（法60条）、合体による登記等は法49条1項1号の者の一方が単独で、と言える。コマ3で、共同申請と混ぜたことが罠で、理由は報告的登記だからと言える
- [ ] 工程C：肝の確認：①権利に関する登記（共同申請）と合体による登記等（一方が単独）で結論が逆 ②理由は、生じた事実を反映する報告的登記で、共同申請の定めは権利に関する登記のもの ③肢の『Ａ又はＢが単独で申請することができる』は〇
- [ ] 工程C：構成表の全文言を記事（H28-Q15ウ）と突き合わせ：『表題登記がない建物の所有者又は表題登記がある建物の表題部所有者』『既に生じた事実をそのまま登記に反映させる報告的登記』『共同申請の定め（法60条）がない』『Ａだけの判断でも、Ｂだけの判断でも』。民法252条5項は図に入れず、設計メモの勘違い②にだけ書いた
- [ ] 工程C：コマ1・2に印がなく、コマ3は左赤✕・右青✓、コマ4だけ青✓の暗記3点。コマの使い方が隣り合うコマで同じにならない（side→none→faces→両方）。コマ4のチェックに肢D0497（×）を別に示し、本肢（〇）と結論の向きが矛盾しない

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

- 2026-10-10 v01：新規作成（型3。権利に関する登記の共同申請〈法60条〉と合体による登記等〈法49条1項1号〉の対比。D0497〈名義人が別々の建物の合体は全員の共同申請ではない・×〉と結論の向きが一致することを確認）
