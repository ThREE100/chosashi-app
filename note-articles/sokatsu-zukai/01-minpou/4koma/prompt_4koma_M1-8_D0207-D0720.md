# D0207・D0720 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事『直前期の苦手論点つぶし総合記事①民法編』（`note-articles/column/sokatsu-01-minpou.md`）の【M1-8】に対応する4コマ（1本）のプロンプトです。肢は、その論点の中で出題者のひっかけ・受験者の勘違いが最も出るものを選び、結論が逆になる対比で組みました。構成表（文言の正本）を含みます。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、`tools/drill/manga/render_spec.py` と `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。設計データは `../src/spec_4koma_M1-8.py`。直すときは設計データを直して再生成します（生成物を手で直さない）。
> - 末尾の「見出し画像プロンプト」は、この4コマを単独で投稿するとき用です。総合記事の見出し画像は `../prompt_midashi_sokatsu-01-minpou.md` です。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0207・D0720（民法／時効・条件期限、出典 H19-Q01イ／H24-Q02オ）。正解＝D0207＝〇・D0720＝〇（どちらも正しい記述）。誤解停止条件は成就するまで待つとだけ覚え、契約の時にすでに成就していた場合（既成条件）を考えない。効力が変わるのは成就した時なのに、当事者が成就を知った時と取り違える（推測）。
- 記事：`note-articles/h19-mondai/q01-joken.md／note-articles/h24-mondai/q02-jouken.md／note-articles/column/sokatsu-01-minpou.md（M1-8）` H19-Q01イ（契約の時にすでに成就していた停止条件は、無条件の契約として有効。131条1項）・H24-Q02オ（解除条件は、成就した時から当然に効力を失い、知らなくても支払義務を免れる。127条2項）を、停止条件と解除条件の対比として1枚に並べる
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0207は、停止条件の事実が契約の時にすでに発生していたのに『停止条件だから成就するまで効力がない』と思わせる（実は131条1項で無条件、つまり有効）。D0720は『Aが進級できなかったことを知らなくても』と、当事者の認識を入れて、知らなければ義務はまだ続くと思わせる（実は成就した時に当然、効力を失う）。
- 【受験者の勘違い・定着していない点】（推測）①停止条件は『成就したときから効力が生じる』とだけ覚え、契約の時にすでに成就していた場合（既成条件）に特則があることを知らない。②条件の効力が変わるのは成就した時なのに、当事者が成就を知った時や通知を受けた時と取り違える。③停止条件と解除条件の取り違え（効力が生じるのか、失われるのか）。
- 【対比する制度】「停止条件」⇔「解除条件」：停止条件は成就した時から効力を生じ（127条1項）、解除条件は成就した時から効力を失う（127条2項）。契約の時にすでに成就していた条件は、停止条件なら無条件（有効）、解除条件なら無効（131条1項）。同じ『すでに成就』でも、条件の種類で結論が逆になる。
- 【型の選び方】型：型4（＋型2の当てはめ表）。理由：2肢は別々の場面（共通の日付がない）なので、コマ1は『肢／条件の種類／場面／肢の言い分』の比較表の代わりに2枚の場面カード、コマ2は『条件の種類×成就の時期』の2×2の当てはめ表（結論が逆になる4マス）、コマ3は『読み方3ステップ』、コマ4は暗記3点。理解の壁は、停止条件と解除条件で効力の向きが逆になること、そして契約の時にすでに成就していた場合の特則が混ざっている点。
- 記事の範囲：H19-Q01イ（131条1項：条件が法律行為の時に既に成就していた場合、停止条件なら無条件、解除条件なら無効。たとえば、契約した時点ですでに雨が降り始めていた『雨が降ったら傘をあげる』の贈与は、無条件で最初から有効）、H24-Q02オ（127条2項：解除条件付法律行為は成就した時からその効力を失う。条件成就の効果は客観的な事実によって発生し、当事者が知っていたかどうかは効力発生に影響しない）、総合記事 M1-8（127条1項：停止条件は成就した時から効力を生ずる）。
- extra_refs：民法127条1項・2項、131条1項・2項の原文は法令DB note-articles/laws/minpou-1-soukyoku-bukken.md で確認した。131条2項（条件が成就しないことが契約の時にすでに確定していた場合は逆：停止条件は無効、解除条件は無条件）は総合記事 M1-8 の整理にあるが、2肢の元記事にはなく、肢の結論も決めないので図の中心にはせず、コマ4の暗記3点にも入れない（読者の混乱を避ける）。
- 兄弟肢：このグループの2肢だけ。両方とも正しい記述（〇）なので、コマ4の帯の正解欄は『〇・〇』にする。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。コマ1の場面カードは文字ラベル（『契約』『条件』『奨学金』）だけで示し、人物は描かない。
- 矢印の意味：矢印は使わない。コマ1は上下2枚のカード、コマ2は2×2の表、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない（結論は文字で書く）。コマ4の暗記3点だけ青✓。カードと表は薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（上下2枚の場面カードが中央、キャラは通常サイズで左右の端）、コマ2＝none（2×2の表が主役）、コマ3＝faces（左に3枚のステップカード、右に会話の縦並び。会話4つ＝顔4つ＝4行）、コマ4＝既定（暗記3点と結論）。
- コマごとに読者が言えること：コマ1＝2肢とも条件の話で、停止条件の『すでに成就』と、解除条件の『知らなくても』が問われている。コマ2＝停止条件は成就した時に効力が生じ、解除条件は成就した時に効力を失う。契約の時にすでに成就していたら、停止条件は無条件（有効）、解除条件は無効。コマ3＝条件の種類を見る→成就の時期を見る→当事者の認識は無関係。コマ4＝D0207は〇、D0720は〇。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D0207・D0720～H19-Q01イ／H24-Q02オ～

## note記事の冒頭文

停止条件を付けた契約の、その条件とした事実が、契約の時にすでに起きていました。この契約の効力は、いつ生じるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（平成19年度　第1問　イ／平成24年度　第2問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 成就した時に変わる。すでに成就なら別扱い | 「すでに成就なら別扱い」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの肢の場面 | — |
| コマ1 図 | 図・カード | 肢D0207　停止条件 / 条件とした事実が、契約の時にすでに発生 / 契約の効力は、どうなる？ / 肢D0720　解除条件 / 進級できなかったら、奨学金をやめる / 進級できなかったと知らなくても？ | — |
| コマ1 | 藍子（左・先に話す） | 条件なら、成就を待つんですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。契約の時の状態も見なさい | 「契約の時の状態」 |
| コマ2 見出し | ラベル | ②　条件の種類と、成就の時期 | — |
| コマ2 図 | 図・カード | 効力の変わり方 / 停止条件と解除条件で、向きが逆 / 向きが逆 / 停止条件 / 解除条件 / 成就した時 / その時から効力を生ずる / 127条1項 / その時から効力を失う / 127条2項 / 肢D0720 / 契約の時にすでに成就 / 無条件（有効） / 131条1項 / 肢D0207 / 無効 | — |
| コマ3 見出し | ラベル | ③　条件を読む3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　条件の種類を見る / 効力が生じる → 停止条件 / 効力を失う → 解除条件 / ステップ2　成就の時期を見る / 契約の後に成就 → 127条 / 契約の時にすでに成就 → 131条1項 / ステップ3　認識は関係ない / ひっかけ：知った時ではなく、成就した時 / 当事者が知っていたかは、効力に影響しない | — |
| コマ3 | 藍子（左・1番目） | 停止条件なら、成就するまで待つのでは？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。契約の時に成就済みなら待たないの | 「契約の時に成就済み」 |
| コマ3 | 藍子（左・3番目） | 知らなければ、まだ払うのでは？ | — |
| コマ3 | トリ先生（右・4番目） | 効力は成就した時に生じるの。知らなくても同じよ | 「成就した時」 |
| コマ4 見出し | ラベル | ④　これだけ覚える | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 種類と時期の2つを見るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。効力が変わるのは成就した時よ | 「成就した時」 |
| コマ4 チェック欄 | 3項目（青✓） | 停止条件は成就した時から効力を生じ、解除条件は成就した時から効力を失う / 契約の時にすでに成就していた条件は、停止条件なら無条件（有効）、解除条件なら無効（D0207は〇） / 効力が変わるのは成就した時。当事者が知った時ではない（D0720は〇） | — |
| 結論帯 | 1行目 | 効力が変わるのは成就した時。すでに成就なら別扱い | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0207・D0720　正解〇・〇（H19-Q01イ／H24-Q02オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 民法127条1項・2項、131条1項（法令DB note-articles/laws/minpou-1-soukyoku-bukken.md で原文確認）。127条1項と131条1項は肢D0207・D0720の元記事の解説にもある（127条1項は総合記事 M1-8 の整理）

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

TITLE BANNER: text 「成就した時に変わる。すでに成就なら別扱い」 in large bold letters; the part 「すでに成就なら別扱い」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの肢の場面」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both the same size, each with the same pale gray fill, a dark navy outline, a dark navy heading placed INSIDE the card, and two short body lines. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: heading 「肢D0207　停止条件」, body 「条件とした事実が、契約の時にすでに発生」 and 「契約の効力は、どうなる？」.
- Card 2: heading 「肢D0720　解除条件」, body 「進級できなかったら、奨学金をやめる」 and 「進級できなかったと知らなくても？」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「条件なら、
成就を待つんですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
契約の時の状態も
見なさい」 with the part 「契約の時の状態」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　条件の種類と、成就の時期」
- A small dark navy tag 「効力の変わり方」 at the top left, with one line beside it: 「停止条件と解除条件で、向きが逆」, with the part 「向きが逆」 in a yellow highlighter marker.
- Below, a table that fills the full panel width. The header row is dark navy with white text and has three columns: an empty first cell, 「停止条件」, and 「解除条件」. The two body rows have the same pale gray fill and a dark navy outline, each main text at least 24 px high, with no check mark, no cross, and no arrow, and the first cell of each body row is a dark navy cell with white text.
- Body row 1 (first cell 「成就した時」): second column 「その時から効力を生ずる」 with a small tag 「127条1項」; third column 「その時から効力を失う」 with a small tag 「127条2項」 and, in a yellow highlighter marker, a second small tag 「肢D0720」.
- Body row 2 (first cell 「契約の時にすでに成就」): second column 「無条件（有効）」 with a small tag 「131条1項」 and, in a yellow highlighter marker, a second small tag 「肢D0207」; third column 「無効」 with a small tag 「131条1項」.
- The four body cells have clearly different texts; the texts are NOT identical, so copy each character exactly as given.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　条件を読む3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　条件の種類を見る」, two body lines 「効力が生じる → 停止条件」 and 「効力を失う → 解除条件」.
- Step card 2: heading 「ステップ2　成就の時期を見る」, two body lines 「契約の後に成就 → 127条」 and 「契約の時にすでに成就 → 131条1項」.
- Step card 3: heading 「ステップ3　認識は関係ない」, a dark navy ribbon tag with large white text 「ひっかけ：知った時ではなく、成就した時」, body 「当事者が知っていたかは、効力に影響しない」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「停止条件なら、
成就するまで待つのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。契約の時に
成就済みなら待たないの」 with the part 「契約の時に成就済み」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「知らなければ、
まだ払うのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「効力は成就した時に
生じるの。知らなくても同じよ」 with the part 「成就した時」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　これだけ覚える」
- 藍子 bubble (left, spoken first): 「種類と時期の
2つを見るんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。効力が変わるのは
成就した時よ」 with the part 「成就した時」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「停止条件は成就した時から効力を生じ、解除条件は成就した時から効力を失う」, 「契約の時にすでに成就していた条件は、停止条件なら無条件（有効）、解除条件なら無効（D0207は〇）」, 「効力が変わるのは成就した時。当事者が知った時ではない（D0720は〇）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「効力が変わるのは成就した時。すでに成就なら別扱い」 with a yellow highlighter marker.
- Line 2: 「問題D0207・D0720　正解〇・〇（H19-Q01イ／H24-Q02オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 当, 無, 肢, 解, 認 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 条件の効力 | 薄い黄色のマーカー |
| タイトル2行目 | いつ変わる？ | 「いつ変わる？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D0207・D0720　H19-Q01イ／H24-Q02オ | — |

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
条件の効力
Line 2 is larger; the phrase いつ変わる？ is red-orange and the rest is dark navy:
いつ変わる？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D0207・D0720　H19-Q01イ／H24-Q02オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a blank contract sheet with a small padlock and a pen
Right side: a desk calendar with blank pages and a small stopwatch

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written (cartoon expression marks such as ！ and ？ beside the characters' faces are decoration, are allowed, and are not extra text); scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 条, 件, 効, 力, 変, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere. Never delete, redo, or regenerate anything because of an expression mark or a symbol beside a character; deliver the first image as it is.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D0207・D0720～H19-Q01イ／H24-Q02オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D0207・D0720～H19-Q01イ／H24-Q02オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D0207・D0720～H19-Q01イ／H24-Q02オ～_v01.png ／ 4コマ解説図解D0207・D0720～H19-Q01イ／H24-Q02オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0207-D0720_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢の場面（契約の時にすでに成就した停止条件／進級できなかった解除条件）が言える。コマ2の表で、停止条件と解除条件の効力の向きと、すでに成就していた場合の結論が言える。コマ3で、読む順番（種類→時期→認識は無関係）が言える。コマ4で、2肢の〇が言える
- [ ] 工程C：肝の確認：①停止条件は成就した時から効力を生じ、解除条件は成就した時から効力を失う ②契約の時にすでに成就していた条件は、停止条件なら無条件（有効）、解除条件なら無効 ③効力が変わるのは成就した時で、当事者が知った時ではない
- [ ] 工程C：構成表の全文言を記事と法令DBに突き合わせ：『成就した時から効力を生ずる』『成就した時から効力を失う』『無条件』『無効』『契約の時にすでに成就』『知った時ではない』『127条1項・2項』『131条1項』。131条2項は入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。コマ3の顔アイコンは会話の数と同じ4つ。コマ4の正解欄は〇・〇

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

## v01：新規作成（2026-10-13）。民法編の総合記事 M1-8 の論点全体の整理。型4（＋型2の当てはめ表）。ChatGPTでの画像生成・検品はまだ。

## 改訂履歴（このファイルは `manga_specs.py` から生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：初版（一発合格ルール適用）
