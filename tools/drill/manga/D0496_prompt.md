# D0496 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D0496（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H21-Q18ア）。正解＝〇（正しい記述）。誤解隔壁の取壊しで区分建物の要件を欠いたときの登記（合体と合併の違い、なぜ合体になるのか）。
- 記事：`note-articles/h21-mondai/q18-gattai-touki.md` ア（一棟の建物を区分した数個の建物が、隔壁部分の取壊しの工事で区分建物の要件を欠くこととなった場合は、合体による登記等を申請しなければならない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『隔壁部分の取壊しの工事』『区分建物の要件を欠くこととなった場合』と、壁を壊す工事の場面を前に出し、『合体による登記等を申請しなければならない』と言い切る。工事の話なので建物の変更や合併の登記に読ませ、区分建物の要件を欠く（隔壁がなくなる）と建物そのものが一個になる、という点を見えにくくしている。
- 【受験者の勘違い・定着していない点】（推測）①壁を壊しても建物は残るので、区分建物の表題部の変更か、合併の登記で足りると考える。②『一個の建物にする』と聞くと合併を思い浮かべ、合体（工事で現に一個になった）と合併（登記記録の上で一個にする）の区別が頭にない。③区分建物は隔壁などで構造上区分されているから区分建物であり、隔壁を取り壊すとその前提が崩れるという理由が結びついていない。
- 【対比する制度】「合体」⇔「合併」：どちらも二つの建物が一個になる話。合体は、工事で現に一個の建物になった場合に、合体後の建物の表題登記と合体前の建物の表題部の登記の抹消を申請しなければならない（法49条1項）。合併は、隔壁が残って別々の区分建物のまま、登記記録の上で一個にする登記（法54条1項3号。区分合併は接続している区分建物が対象）。結論が逆になるのは、隔壁を取り壊して区分建物の要件を欠いたか、隔壁が残るか。
- 【型の選び方】型：型3（理由説明）。理由：壁は『なぜ隔壁を取り壊しただけで合体と言えるのか、一個にする登記の合併とどこが違うのか』が見えないこと。結論の暗記ではなく、区分建物は構造上区分された部分（法2条22号）→隔壁を取り壊すと要件を欠く→二つの建物が一個になる→合体、という理由の流れをコマ3に置いた。コマ2に合体と合併の左右のカードを置いて対比を入れた（型3＋型1の対比の混成）。
- 記事の範囲：H21-Q18ア（一棟の建物を区分した数個の区分建物について、隔壁を取り壊して区分建物としての要件〈構造上の独立性〉を欠くこととなった場合は、複数の建物が一個の建物になったものとして、合体による登記等を申請しなければならない。たとえば、隣り合う二室の分譲マンションの間の壁をぶち抜いて一部屋にした場合）。
- extra_refs：①法49条1項柱書（二以上の建物が合体して一個の建物となった場合に、合体の日から一月以内に、合体後の建物の表題登記と合体前の建物の表題部の登記の抹消を申請しなければならない）と法2条22号（区分建物の定義＝一棟の建物の構造上区分された部分で独立して用途に供することができるもの）と法54条1項3号（建物の合併の登記。表題登記がある区分建物を、登記記録上これと接続する他の区分建物に合併して一個の建物とする登記）は、法令DB note-articles/laws/fudousan-touki-hou.md の原文で確認した。②規則133条1項（区分合併は、合併される乙建物が甲建物と接続する区分建物である場合に限る）は note-articles/laws/fudousan-touki-kisoku-1.md で確認した。③合併の側の整理（区分合併は接続のみが要件）は、同系統の肢の記事 note-articles/h17-mondai/q12-tatemono-gappei.md のエによる。④『現に一個になった事実を登記に反映する』は、H28-Q15ウの記事（note-articles/h28-mondai/q15-gattai.md）の『既に生じた事実をそのまま登記に反映させる報告的登記』の言い方による。
- 記事・条文の食い違いの疑い（図には入れていない）：法49条1項は『二以上の建物が合体して一個の建物となった場合』と定めるだけで、区分建物の隔壁を取り壊した場合がこれにあたるとは書いていない（note-articles/column/nigate-21-gattai-touki-toikake-flow.md も同じ注記）。図は『区分建物の要件を欠き、二つの建物が一個になった』という記事の整理に従い、条文が隔壁の取壊しを明記しているとは書かない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。甲区分建物・乙区分建物と隔壁は、建物のブロックと文字ラベルで示す。
- 矢印の意味：矢印はコマ1の『隔壁を取り壊す工事』という出来事の1本だけ（取引や申請の矢印ではない）。コマ2・3・4は矢印なし。
- 配色：コマ1〜3は印（✓✕）を付けない（合体と合併の違いは文字で書く。説明であり正誤の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボン・帯は濃紺の地に白文字、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（キャラは通常サイズで左右の端、図は中央に甲・乙の区分建物と隔壁、取壊し後）、コマ2＝none（合体と合併の左右のカードと帯。図が主役）、コマ3＝faces（左に理由の3枚のカードとリボン、右に会話4つ＝顔4つ＝4行）、コマ4＝既定（両方・通常サイズ。暗記3点と結論）。隣り合うコマで同じ見せ方が続かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0496～H21-Q18ア～

## note記事の冒頭文

隣り合う二つの区分建物の間の隔壁を取り壊す工事をして、区分建物の要件を欠くことになりました。この場合、合体による登記等を申請しなければならないのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成21年度　第18問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 隔壁を取り壊して要件を欠けば、合体の登記 | 「合体の登記」を黄色マーカー |
| コマ1 見出し | ラベル | ①　隔壁を取り壊したら | — |
| コマ1 図 | 図・カード | 隔壁を取り壊したら、何を申請する？ / 甲区分建物 / 隔壁 / 乙区分建物 / 隔壁を取り壊す工事 / 取壊し後 / 甲と乙が一つにつながる | — |
| コマ1 | 藍子（左・先に話す） | 壁を壊すだけなら、変更の登記では？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。壁がなくなる意味を見るのよ | 「壁がなくなる意味」 |
| コマ2 見出し | ラベル | ②　合体と合併 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 現に一個になったのか、登記の上で一個にするのか / 合体 / 法49条1項 / 工事で、現に一個の建物になった / 現況を登記に反映する / 合併 / 法54条1項3号 / 隔壁は残り、別々の区分建物のまま / 登記記録の上で一個にする / この肢は、隔壁を取り壊して区分建物の要件を欠いた場面 | — |
| コマ3 見出し | ラベル | ③　なぜ、合体になる？ | — |
| コマ3 図 | 図・カード | 区分建物とは / 法2条22号 / 構造上区分された部分 / 隔壁があるから別々の建物 / 隔壁を取り壊すと / 構造上の区分がなくなり / 区分建物の要件を欠く / ひっかけ：区分建物の要件を欠くこととなった場合には / 二つの建物が、一個の建物になる / 法49条1項 / 合体の日から1か月以内に / 合体による登記等を申請する | — |
| コマ3 | 藍子（左・1番目） | 壁を壊しても、建物は残りますよね？ | — |
| コマ3 | トリ先生（右・2番目） | 残るわ。でも区分建物の要件を欠くの | 「区分建物の要件を欠く」 |
| コマ3 | 藍子（左・3番目） | 要件を欠くと、なぜ合体なんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 二つの建物が一個になったからよ | 「一個になった」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 壁を取り壊したら、合体なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。壁が残るなら合体じゃないのよ | 「壁が残るなら合体じゃない」 |
| コマ4 チェック欄 | 3項目（青✓） | 隔壁を取り壊して要件を欠けば、合体による登記等 / 合体後の表題登記と、合体前の表題部の登記の抹消 / 隔壁が残るなら合体でなく、合併の話 | — |
| 結論帯 | 1行目 | 隔壁を取り壊して要件を欠けば、合体の登記 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0496　正解〇（H21-Q18ア） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法49条1項柱書・2条22号・54条1項3号（法令DB note-articles/laws/fudousan-touki-hou.md）：49条1項＝二以上の建物が合体して一個の建物となった場合に、合体の日から一月以内に、合体後の建物の表題登記と合体前の建物の表題部の登記の抹消（合体による登記等）を申請しなければならない。2条22号＝区分建物は、一棟の建物の構造上区分された部分で独立して住居、店舗、事務所又は倉庫その他建物としての用途に供することができるものであって、区分所有法2条3項の専有部分であるもの。54条1項3号＝建物の合併の登記（表題登記がある区分建物を登記記録上これと接続する他の区分建物に合併して一個の建物とする登記など）。
- 不動産登記規則133条1項（法令DB note-articles/laws/fudousan-touki-kisoku-1.md）：区分合併は、乙建物又は乙建物の附属建物が甲建物と接続する区分建物である場合に限る。合併の側の整理（区分合併に必要なのは接続のみ）は note-articles/h17-mondai/q12-tatemono-gappei.md のエ。
- 『現に一個になった事実を登記に反映する』：note-articles/h28-mondai/q15-gattai.md（H28-Q15ウ）の『既に生じた事実をそのまま登記に反映させる報告的登記』による。

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

TITLE BANNER: text 「隔壁を取り壊して要件を欠けば、合体の登記」 in large bold letters; the part 「合体の登記」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　隔壁を取り壊したら」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A before-and-after diagram in the center, about 56 percent of the panel width, top to bottom. At the top, a small question badge in a gray fill with dark navy text 「隔壁を取り壊したら、何を申請する？」 (a question badge only, with no check mark and no cross).
- Under the badge, three flat shapes in ONE row from left to right, all the same height: a building block labeled 「甲区分建物」, a thin dark navy vertical wall labeled 「隔壁」, and a building block labeled 「乙区分建物」. The two building blocks have the same pale gray fill and a dark navy outline. Do NOT draw any arrow between them.
- Below the row, ONE dark navy arrow pointing downward (this arrow means a construction event, not a sale or an application), labeled 「隔壁を取り壊す工事」.
- At the bottom, ONE wide building block with the same pale gray fill and a dark navy outline, with no wall inside, labeled 「取壊し後」 with a small tag 「甲と乙が一つにつながる」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「壁を壊すだけなら、
変更の登記では？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
壁がなくなる意味を
見るのよ」 with the part 「壁がなくなる意味」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　合体と合併」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「現に一個になったのか、登記の上で一個にするのか」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「合体」, a small tag 「法49条1項」, two body lines: 「工事で、現に一個の建物になった」, 「現況を登記に反映する」.
- Right card, heading 「合併」, a small tag 「法54条1項3号」, two body lines: 「隔壁は残り、別々の区分建物のまま」, 「登記記録の上で一個にする」.
- Under the two cards, one wide dark navy band with large white text 「この肢は、隔壁を取り壊して区分建物の要件を欠いた場面」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、合体になる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「区分建物とは」, a small tag 「法2条22号」, body 「構造上区分された部分」 and 「隔壁があるから別々の建物」.
- Card 2, heading 「隔壁を取り壊すと」, body 「構造上の区分がなくなり」 and 「区分建物の要件を欠く」, and a dark navy ribbon tag with large white text 「ひっかけ：区分建物の要件を欠くこととなった場合には」.
- Card 3, heading 「二つの建物が、一個の建物になる」, a small tag 「法49条1項」, body 「合体の日から1か月以内に」 and 「合体による登記等を申請する」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「壁を壊しても、
建物は残りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「残るわ。でも
区分建物の要件を
欠くの」 with the part 「区分建物の要件を欠く」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「要件を欠くと、
なぜ合体なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「二つの建物が
一個になったからよ」 with the part 「一個になった」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「壁を取り壊したら、
合体なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。壁が残るなら
合体じゃないのよ」 with the part 「壁が残るなら合体じゃない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「隔壁を取り壊して要件を欠けば、合体による登記等」, 「合体後の表題登記と、合体前の表題部の登記の抹消」, 「隔壁が残るなら合体でなく、合併の話」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「隔壁を取り壊して要件を欠けば、合体の登記」 with a yellow highlighter marker.
- Line 2: 「問題D0496　正解〇（H21-Q18ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 建, 物, 登, 肢, 解, 記, 請, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「合体」 is spelled exactly like this everywhere (never 「合併」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 隔壁を取り壊したら | 薄い黄色のマーカー |
| タイトル2行目 | 何の登記？ | 「何の登記？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0496　H21-Q18ア | — |

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
隔壁を取り壊したら
Line 2 is larger; the phrase 何の登記？ is red-orange and the rest is dark navy:
何の登記？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0496　H21-Q18ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: two small neighbouring apartment units with a thin dividing wall between them, no text
Right side: a cleared open room with a few pieces of rubble and a small rolled blueprint, no text

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 隔, 壁, 取, 壊, 何, 登, 記, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0496～H21-Q18ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D0496～H21-Q18ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0496～H21-Q18ア～_v01.png ／ 4コマ解説図解D0496～H21-Q18ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0496_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『隣り合う二つの区分建物の隔壁を取り壊した。何の登記？』、コマ2で『現に一個になれば合体、隔壁が残って登記記録の上で一個にするなら合併』、コマ3で『区分建物は構造上区分された部分→隔壁を取り壊すと要件を欠く→二つの建物が一個になる→合体』が言える
- [ ] 工程C：肝の確認：①隔壁を取り壊して区分建物の要件を欠けば、合体による登記等を申請しなければならない（法49条1項） ②合体は現に一個になった場合、合併は隔壁が残って登記記録の上で一個にする登記（法54条1項3号） ③合体の日から一月以内 ④肢D0496は〇
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『区分建物の要件』『構造上区分された部分』『合体の日から1か月以内』『合体後の建物の表題登記と合体前の建物の表題部の登記の抹消』『登記記録の上で一個にする』。条文が隔壁の取壊しを明記しているとは書いていない。他の肢のIDは図に入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは、図や会話が入らないコマだけ小さくする方針で、小さくしたコマはない

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

- 2026-10-11 v01：新規作成（型3。合体と合併の対比、区分建物は構造上区分された部分→隔壁を取り壊すと要件を欠く→二つの建物が一個になる、の理由の流れ。D0497・D1888・D1177と矛盾しないことを確認）
