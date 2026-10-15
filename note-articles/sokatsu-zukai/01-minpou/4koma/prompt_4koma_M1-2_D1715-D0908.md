# D1715・D0908 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事『直前期の苦手論点つぶし総合記事①民法編』（`note-articles/column/sokatsu-01-minpou.md`）の【M1-2】に対応する4コマ（1本）のプロンプトです。肢は、その論点の中で出題者のひっかけ・受験者の勘違いが最も出るものを選び、結論が逆になる対比で組みました。構成表（文言の正本）を含みます。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、`tools/drill/manga/render_spec.py` と `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。設計データは `../src/spec_4koma_M1-2.py`。直すときは設計データを直して再生成します（生成物を手で直さない）。
> - 末尾の「見出し画像プロンプト」は、この4コマを単独で投稿するとき用です。総合記事の見出し画像は `../prompt_midashi_sokatsu-01-minpou.md` です。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1715・D0908（民法／意思表示・無効取消、出典 R04-Q01エ／H26-Q01イ）。正解＝D1715＝×・D0908＝×。本人以外の者の請求による審判で、本人の同意が必要なのは補助開始だけ。保佐開始（D1715）に本人の同意は不要。後見開始・保佐開始・補助開始のいずれも本人の同意が必要（D0908）とするのは誤り。誤解の原因は、後見・保佐・補助の3つを混同し、補助開始だけにある『本人の同意』を、保佐や『いずれの場合も』に広げてしまう点。
- 記事：`note-articles/r4-mondai/q01-seigen-koui-nouryoku.md` R04-Q01エ（本人以外の請求による保佐開始の審判に本人の同意はいらない）とH26-Q01イ（本人以外の請求による後見開始・保佐開始・補助開始のいずれも本人の同意が要る、は誤り）を、『同意がいるのは補助開始だけ』で1枚にする
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は、本人以外の請求による審判で、補助開始だけにある『本人の同意が必要』を、『保佐開始には』（D1715）、『後見開始、保佐開始又は補助開始のいずれの場合も』（D0908）と広げて書く。後見・保佐・補助が似た制度なので、一つの制度の特徴が三つに当てはまるように読めてしまう。
- 【受験者の勘違い・定着していない点】①後見・保佐・補助の3つを混同し、『本人以外の請求なら本人の同意が要る』と一般化する。②『いずれの場合も』『保佐開始も』という広げた文を、制度ごとに確かめずに〇にする。③補助だけ同意が要る理由（軽度で、本人の意思を特に尊重する制度であること）を知らず、丸暗記で覚えている。
- 【対比する制度】「後見開始」「保佐開始」⇔「補助開始」：後見開始（民法7条）・保佐開始（民法11条）は本人以外の請求でも本人の同意は不要。補助開始は本人以外の請求だと本人の同意が必要（民法15条2項）。同じ『本人以外の請求』の場面でも、同意の要否が逆になる。
- 【型の選び方】型：型2（＋型3の理由）。理由：『初見の読者が引っかかる壁』は、後見・保佐・補助のどれに本人の同意がいるのかを制度ごとに整理できていない点と、なぜ補助だけなのかが分からない点。コマ1で2つの肢の言い分と問い、コマ2で3つの審判の当てはめ表（印なし）、コマ3で『なぜ補助だけか』の理由カードと読み方、コマ4で暗記3点にした。同じ論点で、保佐だけを問う文（D1715）と、3つ全部を問う文（D0908）の2肢を1本にまとめた。
- 記事の範囲：R04-Q01エ・H26-Q01イ（本人以外の請求による審判で本人の同意が必要なのは、補助開始の審判だけ〔民法15条2項〕。補助は判断能力の低下が軽度な人を対象とする制度で、本人の意思を特に尊重する仕組みになっている。後見開始・保佐開始の審判では、本人の同意は要件になっていない）。総合記事【M1-2】の『中身の整理』と『判断のしかた』（同意が出てきたら補助だけと決める）に沿う。
- extra_refs：民法第7条・第11条・第15条の原文を note-articles/laws/minpou-1-soukyoku-bukken.md で確認した。表の『対象となる人』の列は条文の言い方（第7条『事理を弁識する能力を欠く常況にある者』、第11条『著しく不十分である者』、第15条『不十分である者』）にそろえ、補助の『軽度』は記事（H26-Q01イ）の言い方にそろえた。同じ論点の兄弟肢D1310（本人以外の請求による補助開始に本人の同意が必要）は、この4コマに入れていない。
- 今回の4コマに入れない関連肢（同じ総合記事の【M1-2】）：D0810（詐術を用いても、相手方が未成年と知っていれば取り消せる。民法21条）、D0811（未成年者は法定代理人の同意を得れば成年前でも追認できる。民法124条）。それぞれ別の論点（誤信の要件／追認の要件）で、言いたいことを1文に絞るため、この本にはまとめていない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。『本人』『家族』は顔なしの人型タグ（文字ラベル）にし、コマ1で紹介してから使う。肢のID（D####）は図に載せない（結論帯の問題番号だけ）。
- 矢印の意味：矢印は使わない。コマ1は人型タグと2枚のカード、コマ2は表、コマ3は理由カードとステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（『同意が必要』『同意は不要』は文字で書く）。コマ4の暗記3点だけ青✓。カードと表は薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（3列の当てはめ表が主役）、コマ3＝faces（左に2枚のカード、右に会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。
- コマごとに読者が言えること：コマ1＝家族の請求で審判をするとき、本人の同意が要るかが問われ、2肢は『保佐にも』『いずれにも』と広げている。コマ2＝同意が要るのは補助開始だけ。コマ3＝補助は軽度で本人の意思を尊重する制度だから。同意が出てきたら補助だけ。コマ4＝2肢とも×。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1715・D0908～R04-Q01エ／H26-Q01イ～

## note記事の冒頭文

家族など本人以外の者の請求で、後見開始、保佐開始、補助開始の審判をするとき、本人の同意はそれぞれ必要なのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和4年度　第1問　エ／平成26年度　第1問　イ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 本人の同意がいるのは、補助開始だけ | 「補助開始だけ」を黄色マーカー |
| コマ1 見出し | ラベル | ①　家族の請求で、同意は要る？ | — |
| コマ1 図 | 図・カード | 本人以外の請求で、本人の同意は要る？ / 家族（請求する人） / 本人 / 判断能力が落ちてきた / 保佐開始にも、本人の同意がいる / 後見・保佐・補助のどれも、本人の同意がいる | — |
| コマ1 | 藍子（左・先に話す） | 家族の請求なら、同意は必要ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。広げすぎよ | 「広げすぎ」 |
| コマ2 見出し | ラベル | ②　3つの審判の当てはめ | — |
| コマ2 図 | 図・カード | 出題者のねらい / 補助だけの特徴を、広げていないか / 審判 / 対象となる人 / 本人以外の請求 / 後見開始 / 能力を欠く常況の人 / 本人の同意は不要 / 保佐開始 / 著しく不十分な人 / 補助開始 / 不十分な人（軽度） / 本人の同意が必要 / 民法15条2項 | — |
| コマ3 見出し | ラベル | ③　なぜ補助だけか | — |
| コマ3 図 | 図・カード | なぜ、補助だけ？ / 補助は判断能力の低下が軽度な人の制度 / 本人の意思を特に尊重する / 読み方 / ひっかけ：いずれの場合も、保佐開始も / 同意と出たら、補助開始だけと決める | — |
| コマ3 | 藍子（左・1番目） | 保佐も、同意が要りそうです | — |
| コマ3 | トリ先生（右・2番目） | それが罠。同意は補助だけなのよ | 「同意は補助だけ」 |
| コマ3 | 藍子（左・3番目） | なぜ、補助だけなんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 軽度で、本人の意思を尊重するからよ | 「本人の意思を尊重」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 同意と出たら、補助だけですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。広げた文は×よ | 「広げた文は×」 |
| コマ4 チェック欄 | 3項目（青✓） | 本人以外の請求で本人の同意が必要なのは、補助開始だけ（民法15条2項） / 後見開始・保佐開始は、本人の同意が不要 / 保佐開始も、いずれの場合も、と広げた記述は× | — |
| 結論帯 | 1行目 | 本人の同意がいるのは、補助開始だけ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1715・D0908　正解×・×（R04-Q01エ／H26-Q01イ） | — |

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

TITLE BANNER: text 「本人の同意がいるのは、補助開始だけ」 in large bold letters; the part 「補助開始だけ」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　家族の請求で、同意は要る？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A question badge across the top, dark navy outline with a pale gray fill: 「本人以外の請求で、本人の同意は要る？」 (a question badge only, with no check mark and no cross).
- Below it, two faceless pictograms side by side in the same light gray-blue color, each with a dark navy name tag: the left one 「家族（請求する人）」 and the right one 「本人」 with the small label 「判断能力が落ちてきた」.
- At the bottom, two cards stacked from top to bottom, both the same size, each with the same pale gray fill and a dark navy outline, each text at least 24 px high, with no check mark, no cross, and no arrow, separated only by a small empty gap. Card 1: 「保佐開始にも、本人の同意がいる」. Card 2: 「後見・保佐・補助のどれも、本人の同意がいる」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「家族の請求なら、
同意は必要ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
広げすぎよ」 with the part 「広げすぎ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　3つの審判の当てはめ」
- A full-width table fills the whole panel. At the top left, a small dark navy tag 「出題者のねらい」 with a line beside it 「補助だけの特徴を、広げていないか」.
- Below, a table with a dark navy header row with white text and three columns: 「審判」, 「対象となる人」, 「本人以外の請求」. Three body rows have the same pale gray fill and a dark navy outline, each main text at least 24 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「後見開始」, 「能力を欠く常況の人」, 「本人の同意は不要」.
- Body row 2: 「保佐開始」, 「著しく不十分な人」, 「本人の同意は不要」.
- Body row 3: 「補助開始」, 「不十分な人（軽度）」, 「本人の同意が必要」 with the small line 「民法15条2項」. In this row the string 「本人の同意が必要」 is in a yellow highlighter marker.
- Rows 1 and 2 have the same text in the third column on purpose; draw the same string in both. Every other cell has its own text exactly as given.

PANEL 3 (surprised then understanding mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ補助だけか」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed fully INSIDE the card, with no check mark and no cross. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Top card: heading 「なぜ、補助だけ？」, two body lines 「補助は判断能力の低下が軽度な人の制度」 and 「本人の意思を特に尊重する」.
- Bottom card: heading 「読み方」, a dark navy ribbon tag with large white text 「ひっかけ：いずれの場合も、保佐開始も」, body 「同意と出たら、補助開始だけと決める」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「保佐も、同意が
要りそうです」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。同意は
補助だけなのよ」 with the part 「同意は補助だけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「なぜ、補助だけ
なんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「軽度で、本人の意思を
尊重するからよ」 with the part 「本人の意思を尊重」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「同意と出たら、
補助だけですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
広げた文は×よ」 with the part 「広げた文は×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「本人以外の請求で本人の同意が必要なのは、補助開始だけ（民法15条2項）」, 「後見開始・保佐開始は、本人の同意が不要」, 「保佐開始も、いずれの場合も、と広げた記述は×」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「本人の同意がいるのは、補助開始だけ」 with a yellow highlighter marker.
- Line 2: 「問題D1715・D0908　正解×・×（R04-Q01エ／H26-Q01イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 対, 当, 解, 記, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 本人以外の請求で | 薄い黄色のマーカー |
| タイトル2行目 | 同意が要るのは？ | 「同意が要るのは？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1715・D0908　R04-Q01エ／H26-Q01イ | — |

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
本人以外の請求で
Line 2 is larger; the phrase 同意が要るのは？ is red-orange and the rest is dark navy:
同意が要るのは？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1715・D0908　R04-Q01エ／H26-Q01イ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a blank petition paper with a small seal stamp beside it
Right side: a calm family sitting at a table with blank documents

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 本, 人, 以, 外, 請, 求, 同, 意, 要, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1715・D0908～R04-Q01エ／H26-Q01イ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1715・D0908～R04-Q01エ／H26-Q01イ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1715・D0908～R04-Q01エ／H26-Q01イ～_v01.png ／ 4コマ解説図解D1715・D0908～R04-Q01エ／H26-Q01イ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1715-D0908_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『家族が請求する場面で、本人の同意が要るか』が問いだと分かり、コマ2の表で3つの審判のうち同意が要るのは補助開始だけと言え、コマ3でその理由が言える
- [ ] 工程C：肝の確認：①本人以外の請求による審判で本人の同意が必要なのは補助開始のみ（民法15条2項） ②後見開始・保佐開始は同意不要 ③補助は軽度で本人の意思を特に尊重する制度 ④『保佐開始も』『いずれの場合も』と広げる文は×
- [ ] 工程C：構成表の全文言を記事（R04-Q01エ・H26-Q01イ）と突き合わせ：『本人以外の者の請求』『本人の同意』『補助開始の審判だけ』『判断能力の低下が軽度』『本人の意思を特に尊重』。条文（7条・11条・15条）は法令DBの原文で確認済み
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。コマ3の顔アイコンは会話の数と同じ4つ。コマ4の正解欄は×・×

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

## v01：新規作成（2026-10-13）。総合記事（民法編）【M1-2】の4コマ。保佐開始だけを問う肢と3つ全部を問う肢を1本にまとめた。詐術（D0810）・追認（D0811）は別論点なので入れていない。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：初版（型2＋型3の理由。一発合格ルール適用）
