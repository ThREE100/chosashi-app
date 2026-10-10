# D2016 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、民法 第921条第1号（法定単純承認）を主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D2016）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D2016（民法／相続・親族、出典 R07-Q03エ）。正解＝×（誤った記述）。誤解の原因は、条文の本文とただし書の取り違え（条文の側から作る版）。
- 記事：`note-articles/r7-mondai/q03-souzoku.md` R07-Q03エ（民法921条1号：本文＝処分したとき単純承認とみなす／ただし書＝保存行為・602条に定める期間を超えない賃貸は、この限りでない）を、条文の作りから1枚で言えるようにする
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は、民法921条1号の本文の言い回し『相続財産の全部又は一部を』をそのまま使い、本文で単純承認とみなす引き金になっている『処分』の位置に、ただし書で除かれている『保存行為』を入れ替えて置いている。条文の語が並んでいるので、条文どおりの正しい記述に見える（記事の『ここが分かりにくいポイント』）。
- 【受験者の勘違い・定着していない点】①『相続財産に何か手を付けた＝承認した』と、行為の中身（財産の価値を維持するのか、減らす・処分するのか）を見分けずに考える。②条文を『全部又は一部』という語の並びで覚えていて、本文（処分）とただし書（保存行為・602条に定める期間を超えない賃貸）のどちらの側の行為かを読まない。③ただし書が、本文の例外（みなさない場合）を定めた構造だと意識せず、1号を『行為をしたら承認』と1つの文として覚えてしまう。
- 【対比する制度】「処分」⇔「保存行為」：処分（家財を売り払う、預金を引き出して使う）は本文で単純承認とみなされる。保存行為（雨漏りの応急処置、鍵の交換）と602条に定める期間を超えない賃貸は、ただし書で『この限りでない』となり、単純承認とみなされない（同じ『相続財産に手を付けた』場面でも、結論が逆になる）。
- 【型の選び方】型：型2（しくみ図→押さえどころ→読み方3ステップ→暗記3点。条文の作りの当てはめ表）。理由：『初見の読者が引っかかる壁』は、1号が『本文（処分→みなす）』と『ただし書（保存行為・短期賃貸→みなさない）』の2層でできているのに、肢の文は条文の語を並べただけで、どちらの層の行為かが見えない点。先行版（肢中心）は処分と保存行為の入れ替えを見せたが、今回は条文の側から、1号の本文とただし書を『行為・条文の位置・結論』の表1枚で言えるようにし、コマ3は条文を読む順番の3ステップにした。
- 記事の範囲：R07-Q03エ（民法921条1号、ただし書で保存行為は除外、602条以内の短期賃貸、保存行為＝財産価値を維持する行為、処分行為＝家財を売り払う・預金を引き出して使う、雨漏りの応急処置・鍵の交換の例、本文＝処分／ただし書＝保存行為の構造）。1号の原文（note-articles/laws/minpou-3-shinzoku-souzoku.md の第921条）で、本文『相続人が相続財産の全部又は一部を処分したとき』、ただし書『保存行為及び第602条に定める期間を超えない賃貸をすることは、この限りでない』を確かめた。
- extra_refs（記事にない整理。法令DBで原文を確認）：①民法第602条（note-articles/laws/minpou-2-saiken.md）の『建物の賃貸借　三年』（コマ2の表の3行目『建物は3年まで』。第602条は『処分の権限を有しない者が賃貸借をする場合』の上限期間で、土地5年・山林10年・動産6箇月もある。図には建物の3年だけを例として入れ、他は入れない）。②民法第920条（minpou-3-shinzoku-souzoku.md）『相続人は、単純承認をしたときは、無限に被相続人の権利義務を承継する。』（コマ1の下の帯。単純承認とみなされると何が起きるかを示す背景）。ほかの関連条文：第915条第1項（3箇月以内に承認又は放棄）・第918条（承認・放棄の前の管理）は、図の主張に使わない（918条は兄弟肢D2014の論点。保存行為が承認から外れる理由として918条を結びつけると、条文にない理由づけになるので図に入れない）。
- 出題文の注意：肢の前半『自己のために相続が開始した事実を知りながら』は、民法第921条第1号の原文にない言い回しで、記事も扱っていないため、図の判断基準には入れない（図では肢の誤りを『保存行為』を引き金に置いた点に限る）。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。『相続人』を顔なしの人型タグ、『実家』を家のアイコンで、コマ1で紹介してから使う。
- 矢印の意味：矢印は使わない。コマ1は人型タグ・家・2枚の行為カード・帯、コマ2は表、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（みなす・みなさないは文字で書く）。コマ4の暗記3点だけ青✓。カードと表は薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝small（行為カードと帯を横いっぱいに置くので、キャラは極小）、コマ2＝none（条文の作りの表だけ）、コマ3＝faces（左に3枚のステップカード、右に会話4行）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D2016～R07-Q03エ～

## note記事の冒頭文

まだ承認も放棄も決めていない相続人が、相続財産の全部又は一部について、保存行為をしました。民法第921条第1号は、この行為を単純承認とみなすのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和7年度　第3問　エ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | みなす引き金は処分。保存行為は除かれる | 「保存行為は除かれる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの場面 | — |
| コマ1 図 | 図・カード | どの行為で、単純承認とみなされる？ / 相続人 / 承認も放棄も、まだ決めていない / 実家 / 家財を売り払う / 雨漏りの応急処置 / 相続財産への行為 / 単純承認の効力（920条） / 無限に被相続人の権利義務を承継する | — |
| コマ1 | 藍子（左・先に話す） | 手を付けたら、承認ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。引き金を条文で見るのよ | 「引き金を条文で見る」 |
| コマ2 見出し | ラベル | ②　民法921条1号の作り | — |
| コマ2 図 | 図・カード | 出題者のねらい / 引き金と除外が入れ替わっていないか / 民法921条1号 / 行為 / 条文の位置 / 単純承認 / 処分 / 家財を売り払う。預金を引き出して使う / 本文 / みなす / 保存行為 / 雨漏りの応急処置。鍵の交換 / ただし書 / みなさない / 602条に定める期間を超えない賃貸 / 期間は602条で決まる（建物は3年まで） | — |
| コマ3 見出し | ラベル | ③　条文を読む3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　行為の中身を見る / 価値を維持する → 保存行為 / 減らす・処分する → 処分 / ステップ2　ただし書を見る / 保存行為と、602条に定める期間を / 超えない賃貸は、この限りでない / ステップ3　引き金を確かめる / ひっかけ：処分の位置に、保存行為がある / 1号の引き金は、本文の処分 | — |
| コマ3 | 藍子（左・1番目） | 全部又は一部、とあるから〇です | — |
| コマ3 | トリ先生（右・2番目） | それが罠。引き金は処分なのよ | 「引き金は処分」 |
| コマ3 | 藍子（左・3番目） | 保存行為は、どうなるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | ただし書で、この限りでないのよ | 「ただし書」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | ただし書が、保存行為を外すんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。引き金は本文の処分よ | 「本文の処分」 |
| コマ4 チェック欄 | 3項目（青✓） | 1号の引き金は、本文の処分（相続財産の全部又は一部） / ただし書：保存行為と、602条に定める期間を超えない賃貸は、みなさない / 保存行為をして単純承認とみなされる、という記述は× | — |
| 結論帯 | 1行目 | 引き金は処分。保存行為はみなされない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D2016　正解×（R07-Q03エ） | — |

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

TITLE BANNER: text 「みなす引き金は処分。保存行為は除かれる」 in large bold letters; the part 「保存行為は除かれる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear VERY SMALL (each about 110 px tall in total, clearly smaller than the full-size characters in the other panels, never more than one third of the panel height), 藍子 at the lower left corner and トリ先生 at the lower right corner, so that the diagram or the items to memorize fill the panel; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの場面」
- A wide diagram that fills the full panel width. A wide question badge across the top: 「どの行為で、単純承認とみなされる？」 (a question badge only, with no check mark and no cross).
- Below it at the left, one faceless pictogram tag in a light gray-blue color with a dark navy tag 「相続人」 and a small label 「承認も放棄も、まだ決めていない」, standing beside a flat house icon labeled 「実家」.
- To the right of the house, two white cards with dark navy outlines side by side, each text at least 24 px high: left card 「家財を売り払う」, right card 「雨漏りの応急処置」, both under a small plain label 「相続財産への行為」.
- At the bottom, one wide pale gray card with a dark navy outline and a dark navy heading 「単純承認の効力（920条）」 and one body line 「無限に被相続人の権利義務を承継する」.
- 藍子 bubble (left, spoken first): 「手を付けたら、
承認ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。引き金を
条文で見るのよ」 with the part 「引き金を条文で見る」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　民法921条1号の作り」
- A full-width table diagram fills the whole panel. At the top left, a small dark navy tag 「出題者のねらい」 with a line beside it 「引き金と除外が入れ替わっていないか」, and at the top right a small tag 「民法921条1号」.
- Below, a table with a dark navy header row with white text and three columns: 「行為」, 「条文の位置」, 「単純承認」. Three body rows have the same pale gray fill and a dark navy outline, each main text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「処分」 in a yellow highlighter marker with a small line 「家財を売り払う。預金を引き出して使う」, then 「本文」, then 「みなす」.
- Body row 2: 「保存行為」 with a small line 「雨漏りの応急処置。鍵の交換」, then 「ただし書」, then 「みなさない」.
- Body row 3: 「602条に定める期間を超えない賃貸」 with a small line 「期間は602条で決まる（建物は3年まで）」, then 「ただし書」, then 「みなさない」.
- The three rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　条文を読む3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　行為の中身を見る」, two body lines 「価値を維持する → 保存行為」 and 「減らす・処分する → 処分」.
- Step card 2: heading 「ステップ2　ただし書を見る」, two body lines 「保存行為と、602条に定める期間を」 and 「超えない賃貸は、この限りでない」.
- Step card 3: heading 「ステップ3　引き金を確かめる」, a dark navy ribbon tag with large white text 「ひっかけ：処分の位置に、保存行為がある」, body 「1号の引き金は、本文の処分」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「全部又は一部、
とあるから〇です」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
引き金は処分なのよ」 with the part 「引き金は処分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「保存行為は、
どうなるんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ただし書で、
この限りでないのよ」 with the part 「ただし書」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「ただし書が、
保存行為を外す
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
引き金は本文の
処分よ」 with the part 「本文の処分」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「1号の引き金は、本文の処分（相続財産の全部又は一部）」, 「ただし書：保存行為と、602条に定める期間を超えない賃貸は、みなさない」, 「保存行為をして単純承認とみなされる、という記述は×」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「引き金は処分。保存行為はみなされない」 with a yellow highlighter marker.
- Line 2: 「問題D2016　正解×（R07-Q03エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 効, 号, 売, 建, 承, 権, 無, 物, 解, 記, 認, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the very small characters are drawn at the specified small sizes (they must not grow and squeeze the diagram) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 手を付けたら承認？ | 薄い黄色のマーカー |
| タイトル2行目 | 引き金はどの行為？ | 「どの行為？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D2016　R07-Q03エ | — |

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
手を付けたら承認？
Line 2 is larger; the phrase どの行為？ is red-orange and the rest is dark navy:
引き金はどの行為？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D2016　R07-Q03エ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: an old house with a ladder leaning on the roof and a small bucket beside it
Right side: a wooden cabinet and a few blank cardboard boxes beside a blank folder

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 手, 付, 承, 認, 引, 金, 行, 為, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D2016～R07-Q03エ～.png |
| 見出し画像（採用版） | 4コマ解説図解D2016～R07-Q03エ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D2016～R07-Q03エ～_v01.png ／ 4コマ解説図解D2016～R07-Q03エ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D2016_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『まだ決めていない相続人が、家財を売り払う・雨漏りの応急処置をした』場面と問い、コマ2で『処分→本文→みなす／保存行為→ただし書→みなさない／602条の期間内の賃貸→ただし書→みなさない』、コマ3で条文を読む3ステップ（行為の中身→ただし書→1号の引き金は処分）、コマ4で結論（×）が言える
- [ ] 工程C：肝の確認：①1号の引き金は本文の『処分』 ②ただし書で、保存行為と602条に定める期間を超えない賃貸は『この限りでない』 ③肢は引き金の位置に保存行為を置いているので×
- [ ] 工程C：構成表の全文言を記事と原文に突き合わせ：『処分』『保存行為』『602条に定める期間を超えない賃貸』『財産の価値を維持する』『家財を売り払う』『預金を引き出して使う』『雨漏りの応急処置』『鍵の交換』『無限に被相続人の権利義務を承継する』（920条）『建物は3年まで』（602条3号）。記事にない2点（602条の3年、920条）は法令DBで原文確認済みの旨を設計メモに書いてある
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（small→none→faces→既定）。コマ4の正解欄は×

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

## v01：新規作成（2026-10-10）。条文（民法921条1号）の側から作る版。型2（条文の作りの当てはめ表）。記事の範囲に、法令DBで原文確認した602条（建物3年）と920条を足した。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-10 v01：初版（条文を主役にした版。一発合格ルール適用）
