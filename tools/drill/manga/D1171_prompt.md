# D1171 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1171（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H28-Q14イ）。正解＝〇（正しい記述）。肢は合併について『住所の変更を証する情報を提供したとしても申請することができない』と述べており、これが正しい。誤解（ユーザー指示。合併と合体の違いを、理由つきで対比）。
- 記事：`note-articles/h28-mondai/q14-tatemono-gappei.md` イ（甲乙で住所が食い違ったままでは、住所変更を証する情報を出しても合併できない）を軸に、合体（R05-Q16オ・H26-Q17オ）と対比し、古い側が乙建物の場合（H22-Q05エ）も添える
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文の『住所の変更を証する情報を提供したとしても』。証する情報を出せば足りる合体の感覚に乗せ、『提供したのだから申請できる』と読ませて、『申請することができない』という結論を誤りと思わせる。長い事案（Ａが引っ越す→乙建物を取得して登記→甲建物の住所の変更の登記は未了）の中で、食い違っているのが甲建物と乙建物の登記記録の住所であることも見落とさせる。この肢は合併なので、証する情報を出しても申請できず、正しい（〇）。
- 【受験者の勘違い・定着していない点】①『住所の変更を証する情報を提供すれば足りる』を、合体（R05-Q16オ・H26-Q17オ）の扱いのまま合併にも広げる。②合併は表示に関する登記で、相続登記なしでも申請できるなど緩やかな面がある（同じ問のア）ので、住所もゆるく扱えると思う。③『なぜ合併だけ、証する情報では足りないのか』の理由（登記記録の上で同じ名義人か確かめる）が定着しておらず、結論だけを覚えているため、合体と合併の肢が並ぶと取り違える。（①〜③は、肢の言い回しと同じ問の兄弟肢から立てた推測。記事に書かれた誤解の型ではない）
- 【対比する制度】「合体」⇔「合併」：合体は住所の変更を証する情報を提供すれば、住所の変更の登記を経ずに申請できる。合併は、証する情報を出しても足りず、先に住所の変更の登記が要る（結論が逆）。理由は、合併は所有権の登記名義人が相互に異なる建物ではできず（法56条2号）、登記記録の上で同じ名義人か確かめる必要があるから（住所の一致を要件とする明文はなく、登記実務の取扱い）。合体は『住所が変わった事実』と『変更の登記』が別物で、事実を証する情報で示せば足りる（これも登記実務の取扱いで、条文は確認できていない）。
- 【型の選び方】型：型3（第三案・理由説明）。壁＝『住所の変更を証する情報を出せば足りる』は合体の話で、合併では足りない。その理由（合併は登記記録の上で同じ名義人か確かめる）が分からないと、合体と合併が並ぶたびに結論が崩れる。結論の暗記ではなく理由が読み取れるよう、型1の流れ（思い込み→手順→理由→結論）のコマ3を理由の説明コマにし、会話（faces）で『なぜ？では合体は？』の2問を聞く形にした。
- 記事の範囲：H28-Q14イ（所有権の登記名義人が相互に異なる建物の合併はできない〈法56条2号〉。登記記録上の氏名・住所が食い違うと、記録の上では同じ名義人と確認できないため、合併しようとする各建物の登記記録上の住所は一致している必要がある。住所の一致を要件とする明文はなく、登記実務の取扱い。証する情報を提供しても記録上の不一致は解消されず、先に住所の変更の登記が必要）。
- extra_refs：①法56条2号は法令DB（note-articles/laws/fudousan-touki-hou.md 第56条）で『表題部所有者又は所有権の登記名義人が相互に異なる建物の合併の登記』と確認した。②合体の側の理由と結論は、同系統の肢 D1888（R05-Q16オ、note-articles/r5-mondai/q16-gattai.md）と D0995（H26-Q17オ、note-articles/h26-mondai/q17-gattai-touki.md）の記事の整理：『変更があった事実』と『変更の登記を経ること』は別物で、前者を証する情報（住民票の写しなど）で示せれば、後者を省略できる場面がある（直接定めた条文は確認できず、登記実務の取扱い）。③古い住所の側が乙建物の場合（甲建物が新住所、乙建物が旧住所）も、先に変更登記が要ることは、対の肢 D0534（H22-Q05エ、note-articles/h22-mondai/q05-tatemono-gappei.md）の記事の整理。いずれも肢 D1171 の記事にない対比・整理で、ユーザーに『記事にない整理』と伝える。図には法56条2号以外の条文番号は入れない（不動産登記令第9条などは入れない）。
- 同じ問の兄弟肢（今回の図には入れない）：D1170（ア、相続登記なしで合併を申請できる、×）、D1172（ウ、区分合併は接続していれば足りる、〇）、D1173（エ、合併後の各階平面図は要る、×）、D1174（オ、表題部所有者は印鑑証明書不要、〇）。アは『合併は表示に関する登記で、登記名義人が死亡していても申請できる』という緩やかさの例で、本肢の住所（登記記録上の名義人の表示が一致していること）とは別の話。
- 登場人物：Ａ（甲建物・乙建物の所有権の登記名義人）をコマ1で顔なしのピクトグラム＋人型タグで紹介。建物は人物ではなく『甲建物』『乙建物』の文字ラベルの建物アイコン。
- 矢印の意味：矢印は使わない。コマ1は図と札、コマ2は番号つきの3つの別カード、コマ3は上下2枚の理由カード。
- 配色：コマ1〜3は印（✓✕）を付けない（証する情報で足りる／足りないは文字で書く。肢の〇×と印の向きが重なって三重に紛らわしくなるのを避ける）。コマ4の暗記3点だけ青✓。人物は全員同じ薄い灰青、カード・札は薄い灰色・濃紺の枠、リボン・帯は濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常の大きさ。図は中央）、コマ2＝none（3枚カードだけ）、コマ3＝faces（左に上下2枚の理由カード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。
- コマごとに読者が言えること：コマ1＝甲建物は旧住所・乙建物は新住所で食い違っていて、問われているのは『証する情報で合併できるか』。コマ2＝合併は、古い住所の建物の住所の変更の登記を先にして、住所をそろえてから申請する。コマ3＝合併は登記記録の上で同じ名義人か確かめるから証する情報では足りず、合体は事実を証する情報で足りる。コマ4＝この肢は合併について『できない』と述べているので〇。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1171～H28-Q14イ～

## note記事の冒頭文

Ａは引っ越した後に乙建物を取得して登記しましたが、甲建物の登記の住所は引っ越し前のままです。住所の変更を証する情報を提供すれば、乙建物を甲建物の附属建物とする合併の登記を申請できるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成28年度　第14問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 住所が食い違う合併は、先に変更登記が要る | 「先に変更登記が要る」を黄色マーカー |
| コマ1 見出し | ラベル | ①　よくある思い込み | — |
| コマ1 図 | 図・カード | Ａ / 甲建物 / 乙建物 / 登記の住所：旧住所 / 登記の住所：新住所 / Ａ（所有権の登記名義人）が引っ越した後、乙建物を取得して登記した / ひっかけ：証する情報を提供したとしても / 証する情報で、合併はできる？ | — |
| コマ1 | 藍子（左・先に話す） | 証する情報を出せば、合併できますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。甲乙の登記の住所を見なさい | 「登記の住所」 |
| コマ2 見出し | ラベル | ②　合併は、住所をそろえてから | — |
| コマ2 図 | 図・カード | ①　住所が食い違う / 甲建物は旧住所、乙建物は新住所 / ②　先に変更登記 / 古い住所の建物（ここでは甲建物）に、住所の変更の登記をする / 古い側が乙建物でも同じ（肢D0534） / ③　そろえてから合併 / 証する情報だけでは、合併の登記は申請できない / 合併は、登記の住所をそろえてから | — |
| コマ3 見出し | ラベル | ③　なぜ合併はだめなの？ | — |
| コマ3 図 | 図・カード | 合併：証する情報でも足りない / 住所の一致は登記実務の取扱い / 所有権の登記名義人が異なる建物は合併できない（法56条2号） / 住所が違うと、記録の上で同じ人と分からない / 証する情報では、記録の食い違いは直らない / 合体：証する情報で足りる / 合体前の建物の住所が古いとき（登記実務の取扱い） / 住所が変わった事実と、変更の登記は別物 / 事実を証する情報で示せば、変更登記は省ける | — |
| コマ3 | 藍子（左・1番目） | 証する情報を出しても、なぜだめなんですか？ | — |
| コマ3 | トリ先生（右・2番目） | 合併は、記録の上で同じ人か見るからよ | 「同じ人か」 |
| コマ3 | 藍子（左・3番目） | じゃあ、合体はどうなんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 合体は、事実を証する情報で足りるのよ | 「証する情報で足りる」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 合併は、先に変更登記が要るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。できないと書くこの肢は〇よ | 「この肢は〇」 |
| コマ4 チェック欄 | 3項目（青✓） | 合併は、証する情報を出しても、先に住所の変更登記が要る / 理由：合併は、記録の上で同じ名義人か確かめる / 合体は、証する情報で足りる（合併と混ぜない） | — |
| 結論帯 | 1行目 | 合併は、証する情報では足りず、先に変更登記 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1171　正解〇（H28-Q14イ） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers, and the full-width letters Ａ only where specified below. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. The legal parties Ａ are NOT characters: draw them only as small, faceless, flat pictogram figures, each with a small round label tag containing the full-width letter given in the text plan.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both very small; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「住所が食い違う合併は、先に変更登記が要る」 in large bold letters; the part 「先に変更登記が要る」 has a yellow highlighter marker.

PANEL 1 (curious, confident mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　よくある思い込み」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center of the panel, about 56 percent of the panel width. A faceless pictogram in a light gray-blue color with a dark navy tag 「Ａ」 stands at the top center.
- Below it, two small building icons side by side, labeled 「甲建物」 (left) and 「乙建物」 (right). Under 「甲建物」 hangs a small white plate with a dark navy outline reading 「登記の住所：旧住所」, and under 「乙建物」 a small white plate with a dark navy outline reading 「登記の住所：新住所」. The two plates have clearly different texts, so copy each character exactly as given.
- A caption under the diagram: 「Ａ（所有権の登記名義人）が引っ越した後、乙建物を取得して登記した」.
- A dark navy ribbon with large white text 「ひっかけ：証する情報を提供したとしても」, and a small question badge 「証する情報で、合併はできる？」 (a question badge only, with no check mark and no cross).
- There is no arrow anywhere in this panel.
- 藍子 bubble (left, spoken first): 「証する情報を出せば、
合併できますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
甲乙の登記の住所を
見なさい」 with the part 「登記の住所」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　合併は、住所をそろえてから」
- Three SEPARATE numbered cards in ONE row from left to right, all exactly the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading placed fully INSIDE the card, with no check mark and no cross. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards.
- Card 1, heading 「①　住所が食い違う」, body 「甲建物は旧住所、乙建物は新住所」.
- Card 2, heading 「②　先に変更登記」, body 「古い住所の建物（ここでは甲建物）に、住所の変更の登記をする」, and a small tag 「古い側が乙建物でも同じ（肢D0534）」.
- Card 3, heading 「③　そろえてから合併」, body 「証する情報だけでは、合併の登記は申請できない」.
- At the bottom, one wide dark navy band with white text 「合併は、登記の住所をそろえてから」.
- The three cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then understanding mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ合併はだめなの？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two stacked cards of the same size fill the whole left column, top and bottom, with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow, and nothing drawn between them except a small empty gap.
- Top card, with a dark navy heading 「合併：証する情報でも足りない」, a small tag 「住所の一致は登記実務の取扱い」, and three short lines of body text 「所有権の登記名義人が異なる建物は合併できない（法56条2号）」, 「住所が違うと、記録の上で同じ人と分からない」, 「証する情報では、記録の食い違いは直らない」.
- Bottom card, with a dark navy heading 「合体：証する情報で足りる」, a small tag 「合体前の建物の住所が古いとき（登記実務の取扱い）」, and two short lines of body text 「住所が変わった事実と、変更の登記は別物」, 「事実を証する情報で示せば、変更登記は省ける」.
- The two cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「証する情報を出しても、
なぜだめなんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「合併は、記録の上で
同じ人か見るからよ」 with the part 「同じ人か」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「じゃあ、合体は
どうなんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「合体は、事実を
証する情報で足りるのよ」 with the part 「証する情報で足りる」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「合併は、先に
変更登記が要るんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
できないと書く
この肢は〇よ」 with the part 「この肢は〇」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「合併は、証する情報を出しても、先に住所の変更登記が要る」, 「理由：合併は、記録の上で同じ名義人か確かめる」, 「合体は、証する情報で足りる（合併と混ぜない）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「合併は、証する情報では足りず、先に変更登記」 with a yellow highlighter marker.
- Line 2: 「問題D1171　正解〇（H28-Q14イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 建, 所, 権, 物, 登, 肢, 解, 記, 証, 請, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「合体」 is spelled exactly like this everywhere (never 「合併」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the faceless pictograms Ａ are all drawn in exactly the same single light gray-blue color, the same shade for every one of them (they differ only by their letter tags); confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that every 「合併」 in the image is spelled with 併 and every 「合体」 with 体, and that the two words are never swapped: in panel 3 the TOP card heading starts with 「合併」 and the BOTTOM card heading starts with 「合体」, and the first bubble of panel 1 and the question badge in panel 1 say 「合併」; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the two plates in panel 1 read 「登記の住所：旧住所」 under 「甲建物」 and 「登記の住所：新住所」 under 「乙建物」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 登記の住所が古いまま | 薄い黄色のマーカー |
| タイトル2行目 | 合併は申請できる？ | 「申請できる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1171　H28-Q14イ | — |

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
登記の住所が古いまま
Line 2 is larger; the phrase 申請できる？ is red-orange and the rest is dark navy:
合併は申請できる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1171　H28-Q14イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small house with an old weathered house-number plate beside its front door
Right side: a cardboard moving box and a few blank document sheets with a rubber stamp

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 登, 記, 住, 所, 古, 合, 併, 申, 請, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1171～H28-Q14イ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1171～H28-Q14イ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1171～H28-Q14イ～_v01.png ／ 4コマ解説図解D1171～H28-Q14イ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1171_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の図で、甲建物は旧住所・乙建物は新住所の登記になっていることと、『証する情報で合併できる？』が問われていることが言える。Ａはコマ1で人型タグ付きで紹介されている
- [ ] 工程C：肝の確認：①合併は、証する情報を出しても足りず、先に住所の変更の登記が要る（古い側が甲でも乙でも同じ） ②理由は、合併は登記記録の上で同じ名義人か確かめるから（法56条2号、住所の一致は登記実務の取扱い） ③合体は事実を証する情報で足りる ④この肢は『できない』と述べているので〇
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『住所の変更を証する情報を提供したとしても』『住所の変更の登記』『法56条2号』『記録の上で同じ人と分からない（記事は、記録のうえでは同じ名義人と確認できない）』『住所の一致は登記実務の取扱い』。合体の側（事実と変更の登記は別物）はD1888・D0995の記事、乙建物側が古い場合はD0534の記事で、extra_refsに記録した
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。肢の〇×は、コマ4の台詞と帯の『正解〇』で示す

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

- 2026-10-10 v01：新規作成（型3。コマ3を『なぜ合併はだめで、合体はよいのか』の理由の説明コマにした。合体の側と乙建物が古い場合は、D1888・D0995・D0534の記事から出典つきで足した）
