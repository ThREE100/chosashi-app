# D1605 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

- 肢：D1605（不動産登記法／登録免許税、出典 R02-Q19ア）。正解＝〇（正しい記述）。誤解回答履歴は×・×・〇・×（誤解3回）。2026-10-03と10-11は×、10-05だけ〇。
- 記事：`note-articles/r2-mondai/q19-touroku-menkyozei.md` R02-Q19ア（合筆は合筆後の個数×1,000円。墓地になった部分の分筆は法5条10号で非課税のため、一部地目変更と分筆でも1,000円）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】第1欄・第2欄の2つの登記を並べ、『いずれも合計1,000円』と言い切る。第2欄は『2筆にする分筆』なので、分筆後の2筆をそのまま数えて2,000円と読ませる（問題文の『当該土地を2筆にする分筆』の語）。さらに『一部地目変更』という別の登記名が付くので、その分の税も上乗せして考えさせる。
- 【受験者の勘違い・定着していない点】推測（回答履歴は×・×・〇・×で、×が3回）：①分筆の税は『分筆後の個数×1,000円』だけを覚えていて、『墓地になった部分は非課税』という引く部分が結びつかず、2筆分の2,000円と考える。②肢イ・肢オのように『ふつうの分筆は2筆なら2,000円』と結論で覚えているため、同じ『2筆にする分筆』の字面でも墓地の分が入ると1,000円になるとは読めない。③一部地目変更の登記そのものに税がかかるかどうかが定着していない（別表第一に掲げられていない課税の外）。④第1欄の合筆を、合筆前の2筆分と数える取り違えも考えられるが、×の向きだけでは区別できない（回答履歴からの推測）。
- 【対比する制度】「ふつうの分筆」⇔「墓地を分ける分筆」：ふつうの分筆は分筆後の個数×1,000円で、2筆なら2,000円（肢D1606の国との共有地、肢D1609の宗教法人の土地でも同じ）。墓地になった部分を分ける分筆は、その墓地の部分が法5条10号で非課税のため、残る1筆の1,000円だけになる（結論が逆になる点。分筆後の個数は同じ2筆でも税額が違う）。
- 【型の選び方】型：型3（＋型2の当てはめ）。理由：初見の読者が引っかかる壁は『分筆は後の個数なのに、なぜ2筆の分筆が1,000円になるのか』という理由の欠落。結論の暗記（1,000円）では肢イ・オに崩れるので、コマ2で3つの数え方を並べ、コマ3で『なぜ墓地の分を引くのか』の理由（法5条10号）と『一部地目変更は課税の外』をカードにした。誤答が3回続いた肢なので、型3の理由コマを優先した。
- 記事の範囲：R02-Q19ア（合筆は『合筆又は合併後の不動産の個数』に1個1,000円で、合筆後は1筆なので1,000円〔別表第一（十三）ロ〕。一部地目変更＋2筆にする分筆は、墓地になった部分の土地が法5条10号〔墳墓地に関する登記〕により非課税で、もう一方の分筆後の土地に1,000円が課されるため合計1,000円〔先例による〕。一部地目変更の登記そのものは別表第一に掲げられておらず課税範囲外）。同じ記事の兄弟肢：イ＝再区分・共有地の分筆は2,000円（国の持分があっても通常どおり課税）、オ＝宗教法人の土地の分筆は2,000円（宗教法人でも非課税にならない）。
- extra_refs：①登録免許税法別表第一（十三）ロ（合筆又は合併後の不動産の個数に1個につき千円）、同イ（分筆又は分割若しくは区分後の不動産の個数に1個につき千円）、法2条（別表第一に掲げる登記等について課する）、法5条10号（墳墓地に関する登記は登録免許税を課さない）は、法令DB note-articles/laws/touroku-menkyozei-hou.md の原文で確認した。②法令DBには、地目の変更の登記が別表第一に登場しないこと（課税範囲外）も、同ファイルの整理として載っている。③『墓地になった部分の分筆のうち、墓地の部分が非課税になる』という具体的な当てはめは、記事が『先例による』と書く点で、先例番号は法令DBでは確認できなかった（記事の別の箇所に昭42.10.2民甲2680号とあるが、法令DBにはない）。図には先例番号を入れず、『法5条10号で非課税』と記事の言い方にとどめる。④不動産登記規則35条7号（表題部の変更の登記と分筆の登記は、同一の不動産なら一の申請情報にできる）は法令DB fudousan-touki-kisoku-1.md で確認した。肢文の『最も低額となるように申請する場合』との関係は、『一部地目変更が課税の外なので、一の申請情報にしても別々にしても税額は同じ』という推測で、記事には書いていない。図には入れない。⑤肢D1606・D1609の結論（分筆後の2筆で2,000円）は同じ記事のイ・オから取った。記事にない整理はなし。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。土地は平らな区画のアイコンと文字ラベルで示す。
- 矢印の意味：矢印は使わない。コマ1は2枚のカードと小さな土地アイコン、コマ2は3枚のカード、コマ3は3枚のカードとリボン。
- 配色：コマ1〜3は印（✓✕）を付けない（課税される・されないは文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、土地アイコンは同じ薄い灰色、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（3枚のカードだけ）、コマ3＝faces（左に3枚のカード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1605～R02-Q19ア～

## note記事の冒頭文

所有権の登記のある2筆の土地の合筆の登記と、土地の一部が墓地になったためにする一部地目変更とその土地を2筆にする分筆の登記を申請します。登録免許税は、どちらも1,000円で済むのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和2年度　第19問　ア）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 合筆も、墓地を分ける分筆も、1,000円 | 「墓地を分ける分筆も、1,000円」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの登記を並べる | — |
| コマ1 図 | 図・カード | どちらも1,000円？ / 第1欄 / 所有権の登記のある2筆を合筆 / 2筆の土地が、1筆になる / 第2欄 / 一部地目変更と分筆 / 土地の一部が墓地になり、2筆に分ける / 墓地 / 残る土地 | — |
| コマ1 | 藍子（左・先に話す） | 分筆は2筆だから、2,000円ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。分筆後の数だけ見る癖 | 「分筆後の数だけ見る」 |
| コマ2 見出し | ラベル | ②　3つの数え方 | — |
| コマ2 図 | 図・カード | 合筆 / 合筆後の個数は1個 / 1個×1,000円＝1,000円 / ふつうの分筆 / 国との共有地・宗教法人の土地も / 分筆後の個数は2個 / 2個×1,000円＝2,000円 / 墓地を分ける分筆 / 墓地の部分は非課税。残る1筆だけ課税 | — |
| コマ3 見出し | ラベル | ③　なぜ墓地の分を引くのか | — |
| コマ3 図 | 図・カード | 個数の数え方 / 合筆後・分筆後の個数に、1個1,000円 / 墓地の部分は非課税 / ひっかけ：分筆後の2筆をそのまま数える / 墳墓地に関する登記は、法5条10号で非課税 / 一部地目変更は課税の外 / 別表第一に掲げられていない | — |
| コマ3 | 藍子（左・1番目） | 2筆にする分筆でも、1,000円？ | — |
| コマ3 | トリ先生（右・2番目） | 数えるのは分筆後の個数。ただ墓地は非課税 | 「墓地は非課税」 |
| コマ3 | 藍子（左・3番目） | 地目を変える登記の税は別ですか？ | — |
| コマ3 | トリ先生（右・4番目） | 別表第一にないから課税の外よ | 「課税の外」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 後の個数から、墓地の分を引くんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。引く部分を忘れないことよ | 「引く部分」 |
| コマ4 チェック欄 | 3項目（青✓） | 合筆は、合筆後の個数1個で、1,000円 / 分筆は分筆後の個数だが、墓地の部分は非課税 / 一部地目変更そのものは、課税の外。D1605は〇 | — |
| 結論帯 | 1行目 | 合筆も、墓地を分ける分筆も、1,000円 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1605　正解〇（R02-Q19ア） | — |

## プロンプト本体

```text
Create ONE complete vertical Japanese study infographic in the form of a four-panel comic, in a single image. Canvas: 1080x1920 px portrait (9:16). If exactly 9:16 is impossible, use the closest portrait size and keep the same layout proportions.

CRITICAL TEXT REQUIREMENT: All text must be Japanese only, using standard Japanese kanji (joyo kanji), hiragana, katakana, Arabic numerals, circled numbers. Never use simplified Chinese characters, traditional Chinese characters, Latin-alphabet words, Korean, or pseudo-text. Render every text string verbatim, exactly as given between the quotation marks 「」. Do not paraphrase, shorten, add, reorder, or translate any text. Do not add any text that is not listed.

BACKGROUND REQUIREMENT: The whole image has a fully opaque background (solid or subtly textured light cream). No transparency, no alpha channel, no checkerboard, no transparent areas anywhere.

CHARACTERS: The attached character-specification images are the single authoritative reference for two recurring characters, and you must reproduce them faithfully in every panel: same face, body shape, clothing, colors, proportions, and drawing style, including the same hairstyle for 藍子 in all four panels. Only expression, gaze, hand position, and posture may change. (1) 「トリ先生」 is the TEACHER: a plump, round bird character who knows the exam inside out; sharp-tongued but full of love for beginners (exasperated, scolding-yet-caring expressions; wings used as hands). (2) 「藍子」 is the STUDENT: a serious, straightforward young woman exam-taker in a collared light-blue blouse with thin blue pinstripes (sleeves rolled up) and a navy pencil skirt with navy pumps, no jacket, often holding a navy clipboard and a pencil; earnest and headstrong (confident, startled, realizing, relieved expressions). Do not redesign either character and do not add any other character. Organizations and buildings in the diagrams are NOT characters: draw them only as simple, faceless, flat icons with the exact text labels given below.

CHARACTER SIZE POLICY: draw 藍子 and トリ先生 as large and as clear as the layout allows, at the size given in each PANEL line. Never shrink a character just to make it small or to leave empty space, and never draw a character at the smallest possible size by default (this happens most often in panel 1). Reduce a character's size ONLY when the diagram, the cards, or the speech bubbles of that panel genuinely do not fit otherwise, and then reduce it only as much as needed, keeping the face large enough to read the expression. Characters become icon-sized only in a panel whose PANEL line explicitly asks for face icons.

ANATOMY (critical, 藍子): keep her human anatomy strictly correct in every panel: exactly one head, one torso, exactly two arms (one left, one right) and exactly two hands in total. Never draw extra arms, extra hands, extra fingers, floating hands, duplicated hands, arms that do not grow from the shoulders, or fused hands. Each hand has exactly five fingers. Check that every shoulder, elbow, and wrist connects naturally. HAND COUNT RULE: before drawing each panel, assign both of 藍子's hands a job (for example, one hand points while the other hand holds the clipboard or hangs at her side; or one hand touches her chin while the other holds the clipboard; or both hands are raised in a small cheer). When she points, only ONE arm points; her other hand must not be clasped, raised, or clenched at the same time, so there are never three hands in a panel. POSE: change 藍子's pose from panel to panel (for example standing, sitting, leaning forward, resting a hand on her chin) and use a different set of poses each time this image is generated. CONTENT: in each panel, express through the diagram, labels, and scene the elements a reader needs in order to understand this article's content and pass the land and building surveyor exam, without adding any text beyond the given strings.

FIXED POSITIONS AND SPEECH BUBBLES: In every panel in which a character appears, 藍子 (the student) stands on the LEFT side and トリ先生 (the teacher) stands on the RIGHT side. A panel does not have to show both characters: when the diagram, the flowchart, or the items to memorize need more space, the PANEL line may show only one of the two characters, show both at the normal size at the two outer edges, show both as small face icons in a vertical conversation column, or show both smaller than normal; in that case follow the PANEL line and its LAYOUT lines, and a character who is not drawn has no speech bubble; in a panel marked as face icons, each character appears only as a small round face icon inside the vertical conversation column described in the LAYOUT lines, with exactly one face icon for each speech bubble and never more face icons than bubbles. Every speech bubble is placed in the upper area on the SAME SIDE as its speaker, and its tail points directly at that speaker's mouth. Never point a tail at the other character and never place a bubble on the opposite side from its speaker. Each bubble is short, with large, high-contrast, mobile-readable Japanese text (character height at least 40 px). Reading order is top to bottom, 藍子 first, then トリ先生. 藍子 asks or voices the misconception and トリ先生 answers or corrects, so 藍子's line is always the first one read in a panel.

STYLE: clean, warm, trustworthy flat digital illustration for a Japanese study column; simple outlines, soft pastel colors, readable silhouettes. Emphasis color: use a yellow highlighter marker only on the strings marked as emphasized. Color rule: affirmative marks, check marks, and the YES branch arrows and result boxes of any flowchart are BLUE. Negative marks, crosses, and the NO branch arrows and result boxes of any flowchart are RED. Use only these two colors for YES/NO meaning; use dark navy for neutral arrows, outlines, and stamps. Keep every stamp, arrow, and label fully inside its own card or panel frame with clear margins; nothing overlaps a frame edge or a character's pointing wing.

CONTINUITY: any object, label, ribbon, tag, or figure that appears in more than one panel keeps the same look, the same color, and the same label text in every panel in which it appears (for example, a ribbon on a plot of land does not disappear after a step of the diagram), unless that panel's own description says that it changes. Every speech bubble's line breaks follow phrase boundaries as written inside its quotation marks; never split a word across lines.

LAYOUT (top to bottom, one column, exactly four panels, no side-by-side panels):
- Title banner (about 190 px tall).
- Panel 1 (about 395 px), Panel 2 (about 395 px), Panel 3 (about 395 px), Panel 4 (about 395 px), separated by thin frame lines and about 14 px gaps.
- Conclusion banner at the bottom (about 110 px tall).

TITLE BANNER: text 「合筆も、墓地を分ける分筆も、1,000円」 in large bold letters; the part 「墓地を分ける分筆も、1,000円」 has a yellow highlighter marker.

PANEL 1 (curious, confident mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの登記を並べる」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A flat concept diagram placed only in the central column of the panel, about 56% of the panel width, drawn large, with a small question badge 「どちらも1,000円？」 at the top (a question badge only, with no check mark and no cross).
- Under the badge, two cards stacked from top to bottom, both exactly the same size, with the same pale gray fill and a dark navy outline, each with its dark navy heading placed fully INSIDE the card, and with no check mark and no cross.
- Top card: a small dark navy tag 「第1欄」, heading 「所有権の登記のある2筆を合筆」, one body line 「2筆の土地が、1筆になる」, and a small flat illustration of two land plots merging into one land plot, all plots in the same pale gray fill.
- Bottom card: a small dark navy tag 「第2欄」, heading 「一部地目変更と分筆」, one body line 「土地の一部が墓地になり、2筆に分ける」, and a small flat illustration of one land plot divided by a dotted line into a part labeled 「墓地」 and a part labeled 「残る土地」, both parts in the same pale gray fill.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「分筆は2筆だから、
2,000円ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
分筆後の数だけ
見る癖」 with the part 「分筆後の数だけ見る」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　3つの数え方」
- Three wide cards stacked from top to bottom in the center of the panel, all exactly the same size and aligned, each with the same pale gray fill and a dark navy outline, with its dark navy heading placed fully INSIDE the card, and with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「合筆」, two body lines: 「合筆後の個数は1個」, 「1個×1,000円＝1,000円」.
- Card 2, heading 「ふつうの分筆」, small tag 「国との共有地・宗教法人の土地も」, two body lines: 「分筆後の個数は2個」, 「2個×1,000円＝2,000円」.
- Card 3, heading 「墓地を分ける分筆」, two body lines: 「墓地の部分は非課税。残る1筆だけ課税」, 「1個×1,000円＝1,000円」.
- The three cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given. There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ墓地の分を引くのか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「個数の数え方」, body 「合筆後・分筆後の個数に、1個1,000円」.
- Card 2, heading 「墓地の部分は非課税」, a dark navy ribbon tag with large white text 「ひっかけ：分筆後の2筆をそのまま数える」, body 「墳墓地に関する登記は、法5条10号で非課税」.
- Card 3, heading 「一部地目変更は課税の外」, body 「別表第一に掲げられていない」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「2筆にする分筆でも、
1,000円？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「数えるのは分筆後の個数。
ただ墓地は非課税」 with the part 「墓地は非課税」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「地目を変える登記の
税は別ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「別表第一にないから
課税の外よ」 with the part 「課税の外」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「後の個数から、
墓地の分を
引くんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
引く部分を
忘れないことよ」 with the part 「引く部分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「合筆は、合筆後の個数1個で、1,000円」, 「分筆は分筆後の個数だが、墓地の部分は非課税」, 「一部地目変更そのものは、課税の外。D1605は〇」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「合筆も、墓地を分ける分筆も、1,000円」 with a yellow highlighter marker.
- Line 2: 「問題D1605　正解〇（R02-Q19ア）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 所, 権, 登, 解, 記 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 合筆と墓地の分筆 | 薄い黄色のマーカー |
| タイトル2行目 | どちらも1,000円？ | 「1,000円？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1605　R02-Q19ア | — |

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
合筆と墓地の分筆
Line 2 is larger; the phrase 1,000円？ is red-orange and the rest is dark navy:
どちらも1,000円？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1605　R02-Q19ア
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: two adjoining plots of land being joined, with a small signpost board
Right side: a plot of land with a small gravestone corner and a dotted dividing line, beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 合, 筆, 墓, 地, 分, 円, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1605～R02-Q19ア～.png |
| 見出し画像（採用版） | 4コマ解説図解D1605～R02-Q19ア～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1605～R02-Q19ア～_v01.png ／ 4コマ解説図解D1605～R02-Q19ア～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1605_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で、第1欄の合筆と第2欄の一部地目変更＋分筆が別の登記だと分かり、コマ2で『合筆は1個、ふつうの分筆は2個、墓地を分ける分筆は墓地の部分が非課税』の3つの数え方が並んで読める
- [ ] 工程C：肝の確認：①合筆は合筆後の1個×1,000円 ②分筆は分筆後の個数だが、墓地になった部分は法5条10号で非課税 ③一部地目変更そのものは課税の外 ④だから第1欄も第2欄も1,000円で、肢D1605は〇
- [ ] 工程C：構成表の全文言を記事と突き合わせ：『合筆後の個数』『分筆後の個数』『墓地の部分』『法5条10号』『墳墓地に関する登記』『別表第一に掲げられていない』『課税の外』（記事は『課税範囲外』と書く。同義で図は『課税の外』）。先例番号と規則35条7号は図に入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。肢D1606・D1609のタグは、ふつうの分筆のカードに載せた

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

## v01：新規作成（2026-10-11）。一問一答で誤解が3回になった肢（回答履歴は×・×・〇・×）。型3（理由コマ）に型2の当てはめを混ぜ、ふつうの分筆との対比で『墓地の分を引く』理由を示した。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-11 v01：初版（v2ルール：吹き出しの改行、コマ間の継続、人体構造・手の割り当てを適用。一発合格ルール適用）
