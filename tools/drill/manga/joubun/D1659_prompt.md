# D1659 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記事務取扱手続準則 第79条第3号（家屋番号の定め方）を主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D1659）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D1659（不動産登記法／土地の表題・地目・地積、出典 R03-Q09オ）。正解＝〇（正しい記述）。誤解の原因は、準則79条3号の本則（附属建物の有無で、主たる建物か床面積の多い部分かが分かれる）だけを覚え、同じ号のなお書き（管轄を異にするとき）を落とす。
- 記事：`note-articles/r3-mondai/q09-chiban-kaokubangou.md` R03-Q09オ（管轄を異にする土地にまたがる建物は、管轄指定を受けた登記所の管轄する土地の地番で家屋番号を定める。準則79条3号）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】問題文は『当該建物の床面積が多い部分の存する「5番1」』と、床面積の多い土地を先に出して、準則79条3号の本則（床面積の多い部分の存する敷地の地番）を呼び出す。その後ろに、『6番1』の土地は『登記の事務をつかさどる指定を受けたＢ登記所』の管轄、と小さく置く。読者を本則に引き寄せておいて、同じ号のなお書きで『6番1となる』と答えさせる。
- 【受験者の勘違い・定着していない点】①準則79条3号を『床面積の多い部分の存する敷地の地番』の一行で覚え、本則の中の場合分け（附属建物があるか、ないか）と、そのあとに続くなお書き（管轄を異にする土地にまたがるとき）を一つの号の中の順番として読めていない。②『管轄指定を受けた登記所』という語が、何を指定する話か（その建物の登記の事務をつかさどる登記所）と結びつかず、家屋番号に響く場面だと気づけない。③同じ問の別の肢（同じ地番に2個の建物＝支号。準則79条2号）と並べて、家屋番号の決め方を断片で覚えており、どの場面でどの決め方になるか区別できていない。
- 【対比する制度】「床面積の多い部分」⇔「管轄指定を受けた登記所」：管轄が分かれていない（附属建物がなければ）ときは、床面積の多い部分の存する敷地の地番。管轄を異にする土地にまたがるときは、床面積の多い部分ではなく、管轄指定を受けた登記所の管轄する土地の地番（結論が逆になる点：本肢は5番1ではなく6番1）。
- 【型の選び方】型：型2（＋型1の対比）。理由：初見の読者が引っかかる壁は『準則79条3号が、本則（附属建物の有無で二つに分かれる）と、なお書き（管轄を異にするとき）の三つの場合分けでできていることが見えず、一行の覚え方のまま問題文の床面積につられる』。壁を越えるには、条文の構造（誰が、どの場合に、どの土地の地番になるか）を先に1枚で見せ、そのあとで問題文のどこで場合が分かれるかを読む手順にするのがよい。そこでコマ2は条文の場合分けのカード、コマ3は本番での読み方3ステップ（ひっかけのリボンつき）にした。
- 記事の範囲：R03-Q09オ（1個の建物が複数の登記所の管轄にまたがるときは、法務大臣又は法務局・地方法務局の長が、その建物の登記の事務をつかさどる登記所を指定する。家屋番号は指定を受けた登記所が管轄する土地の地番と同一の番号。準則79条3号。床面積が多い方ではなく、担当に指定された登記所の地番で決まる）。
- extra_refs（記事にない整理の出典）：①準則79条3号の全文（本則：主たる建物〔附属建物の存する場合〕又は床面積の多い部分〔附属建物の存しない場合〕の存する敷地の地番と同一の番号。主たる建物が二筆以上の土地にまたがる場合は、床面積の多い部分の存する敷地の地番。なお書き：建物が管轄登記所を異にする土地にまたがって存する場合には、管轄指定を受けた登記所の管轄する土地の地番により定める）は、法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md の第79条3号で確認した。記事は本則の中身を書いていないので、本則の場合分け（附属建物の有無）は『記事にない整理』。②登記所の指定の根拠の不動産登記法6条2項（不動産が二以上の登記所の管轄区域にまたがる場合は、法務大臣又は法務局若しくは地方法務局の長が、当該不動産に関する登記の事務をつかさどる登記所を指定する）は、法令DB note-articles/laws/fudousan-touki-hou.md の第6条2項で確認した。記事は条番号を書かない。③本肢の建物に附属建物の記載がない点は、肢の文言からの整理（附属建物がない場合の本則＝床面積の多い部分で比べる場面）。
- 兄弟肢：D1655〜D1658（同じ問の別の肢）。D1658（同じ地番に2個の建物＝支号。準則79条2号）は、本肢とは結論が逆になる対比ではない。本肢は『他に登記された建物が存しない』ので支号は付かない、とだけコマ1の小カードに入れる。D1655〜D1657は地番の話で別の論点なので入れない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。問題文の『Ａ登記所』『Ｂ登記所』は、図では『別の登記所』『指定を受けた登記所』と書き分け、Ａ・Ｂの文字は図に入れない（lead1の問いかけだけ問題文どおり）。建物はアイコン、土地は『5番1』『6番1』の文字ラベル。
- 矢印の意味：矢印は使わない。コマ1は土地2枚の上に建物がまたがる図、コマ2は番号つきの別カード、コマ3は3ステップのカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常サイズで左右の端、図は中央）、コマ2＝none（条文の場合分けカードだけ。キャラも吹き出しもなし）、コマ3＝faces（左に3ステップとひっかけのリボン、右に会話4つの縦並び）、コマ4＝既定（両方）。隣り合うコマで同じ見せ方が続かない。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1659～R03-Q09オ～

## note記事の冒頭文

5番1と6番1の土地にまたがる建物があり、床面積が多い部分は5番1の土地にあります。登記の事務をつかさどる指定を受けたのは、6番1の土地を管轄するＢ登記所です。この建物の家屋番号は、どの番号になるのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和3年度　第9問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | またがる建物は、まず管轄が分かれるかを見る | 「まず管轄が分かれるか」を黄色マーカー |
| コマ1 見出し | ラベル | ①　5番1か、6番1か | — |
| コマ1 図 | 図・カード | 5番1 / 床面積が多い部分 / 別の登記所の管轄 / 6番1 / 指定を受けた登記所の管轄 / 登記の事務をつかさどる / この建物の家屋番号は？ / この土地の上に、他に登記された建物はない / 家屋番号は何番になる？ | — |
| コマ1 | 藍子（左・先に話す） | 床面積が多い5番1だから、5番1ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。その床面積が罠なのよ | 「床面積が罠」 |
| コマ2 見出し | ラベル | ②　準則79条3号の場合分け | — |
| コマ2 図 | 図・カード | 出題者のねらい / 床面積の多い方か、指定を受けた登記所の方かを見分けさせる / 準則79条3号　二筆以上の土地にまたがる一個の建物 / 家屋番号は、どの土地の地番と同じ番号にするか / ①　本則　附属建物があるとき / 主たる建物の存する敷地の地番 / ②　本則　附属建物がないとき / 床面積の多い部分の存する敷地の地番 / ③　なお書き　管轄を異にする土地にまたがるとき / 登記の事務をつかさどる登記所が指定される（法6条2項） / 管轄指定を受けた登記所の管轄する土地の地番 | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　管轄を見る / 管轄を異にする土地にまたがるか / ステップ2　同じなら本則 / 附属建物があれば主たる建物、なければ床面積の多い部分 / ステップ3　分かれるならなお書き / ひっかけ：床面積が多い5番1 / 指定を受けた登記所の管轄する6番1 | — |
| コマ3 | 藍子（左・1番目） | 床面積が多いのは5番1ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | それは本則。先に管轄を見るのよ | 「先に管轄」 |
| コマ3 | 藍子（左・3番目） | 管轄が分かれていたら、どうなるんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 指定を受けた登記所の土地の6番1よ | 「6番1」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 床面積より、管轄を先に見るんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。家屋番号は6番1で〇よ | 「6番1で〇」 |
| コマ4 チェック欄 | 3項目（青✓） | 本則は、附属建物があれば主たる建物、なければ床面積の多い部分の敷地の地番 / 管轄を異にする土地にまたがるなら、管轄指定を受けた登記所の管轄する土地の地番 / 本肢は管轄が分かれるので6番1で〇（準則79条3号） | — |
| 結論帯 | 1行目 | 本則の前に、管轄が分かれるかを見る | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1659　正解〇（R03-Q09オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記事務取扱手続準則79条3号（法令DB note-articles/laws/fudousan-touki-jimu-junsoku.md 第79条3号）：２筆以上の土地にまたがって１個の建物が存する場合には、主たる建物（附属建物の存する場合）又は床面積の多い部分（附属建物の存しない場合）の存する敷地の地番と同一の番号をもって、主たる建物が２筆以上の土地にまたがる場合には、床面積の多い部分の存する敷地の地番と同一の番号をもって定める。なお、建物が管轄登記所を異にする土地にまたがって存する場合には、管轄指定を受けた登記所の管轄する土地の地番により定める。
- 不動産登記法6条2項（法令DB note-articles/laws/fudousan-touki-hou.md 第6条2項）：不動産が二以上の登記所の管轄区域にまたがる場合は、法務省令で定めるところにより、法務大臣又は法務局若しくは地方法務局の長が、当該不動産に関する登記の事務をつかさどる登記所を指定する。

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

TITLE BANNER: text 「またがる建物は、まず管轄が分かれるかを見る」 in large bold letters; the part 「まず管轄が分かれるか」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　5番1か、6番1か」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two plot-of-land blocks side by side with the same pale gray fill and a dark navy outline.
- Left block, heading 「5番1」, with two small lines 「床面積が多い部分」 and 「別の登記所の管轄」. Right block, heading 「6番1」, with two small lines 「指定を受けた登記所の管轄」 and 「登記の事務をつかさどる」.
- One flat building icon lies across both blocks, with a white label 「この建物の家屋番号は？」 on it. Under the blocks, one small white card 「この土地の上に、他に登記された建物はない」.
- A small question badge at the top reads 「家屋番号は何番になる？」 (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「床面積が多い5番1だから、
5番1ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
その床面積が
罠なのよ」 with the part 「床面積が罠」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　準則79条3号の場合分け」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「床面積の多い方か、指定を受けた登記所の方かを見分けさせる」.
- One wide header card with the dark navy heading 「準則79条3号　二筆以上の土地にまたがる一個の建物」 and one body line 「家屋番号は、どの土地の地番と同じ番号にするか」.
- Under it, three SEPARATE numbered cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: heading 「①　本則　附属建物があるとき」, body 「主たる建物の存する敷地の地番」.
- Card 2: heading 「②　本則　附属建物がないとき」, body 「床面積の多い部分の存する敷地の地番」.
- Card 3: heading 「③　なお書き　管轄を異にする土地にまたがるとき」, two body lines: 「登記の事務をつかさどる登記所が指定される（法6条2項）」, 「管轄指定を受けた登記所の管轄する土地の地番」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　管轄を見る」, body 「管轄を異にする土地にまたがるか」.
- Step card 2: heading 「ステップ2　同じなら本則」, body 「附属建物があれば主たる建物、なければ床面積の多い部分」.
- Step card 3: heading 「ステップ3　分かれるならなお書き」, a dark navy ribbon tag with large white text 「ひっかけ：床面積が多い5番1」, body 「指定を受けた登記所の管轄する6番1」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「床面積が多いのは
5番1ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それは本則。
先に管轄を見るのよ」 with the part 「先に管轄」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「管轄が分かれて
いたら、どうなる
んですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「指定を受けた登記所の
土地の6番1よ」 with the part 「6番1」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「床面積より、
管轄を先に見る
んですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
家屋番号は
6番1で〇よ」 with the part 「6番1で〇」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「本則は、附属建物があれば主たる建物、なければ床面積の多い部分の敷地の地番」, 「管轄を異にする土地にまたがるなら、管轄指定を受けた登記所の管轄する土地の地番」, 「本肢は管轄が分かれるので6番1で〇（準則79条3号）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「本則の前に、管轄が分かれるかを見る」 with a yellow highlighter marker.
- Line 2: 「問題D1659　正解〇（R03-Q09オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 建, 所, 物, 番, 登, 肢, 解, 記 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 家屋番号のきめ方 | 薄い黄色のマーカー |
| タイトル2行目 | 管轄が分かれたら？ | 「管轄」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1659　R03-Q09オ | — |

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
家屋番号のきめ方
Line 2 is larger; the phrase 管轄 is red-orange and the rest is dark navy:
管轄が分かれたら？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1659　R03-Q09オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a single building standing across the boundary of two adjacent plots of land with two different small office signposts, no letters
Right side: two blank document sheets and a rubber stamp beside a small registry book

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 家, 屋, 番, 号, 方, 管, 轄, 分, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1659～R03-Q09オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1659～R03-Q09オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1659～R03-Q09オ～_v01.png ／ 4コマ解説図解D1659～R03-Q09オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1659_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の図で、建物が5番1（床面積が多い）と6番1（指定を受けた登記所の管轄）にまたがり、家屋番号が問われていることが言える
- [ ] 工程C：肝の確認：①準則79条3号の本則は、附属建物があれば主たる建物の存する敷地の地番、なければ床面積の多い部分の存する敷地の地番 ②建物が管轄登記所を異にする土地にまたがるときは、管轄指定を受けた登記所の管轄する土地の地番（なお書き） ③本肢は②なので6番1で〇（床面積の多い5番1と読むのがひっかけ）
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『主たる建物』『床面積の多い部分』『管轄を異にする土地にまたがる』『管轄指定を受けた登記所』『登記の事務をつかさどる登記所』『準則79条3号』『法6条2項』『家屋番号は6番1』
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない

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

- 2026-10-10 v01：新規作成（条文中心版。準則79条3号の本則と、管轄を異にするときのなお書きの場合分けを1枚で見せる。型2＋型1の対比）
