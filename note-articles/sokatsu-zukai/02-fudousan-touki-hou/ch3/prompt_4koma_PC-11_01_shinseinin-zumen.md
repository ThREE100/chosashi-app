# D0485・D0369 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」の第3章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md`）の、論点【PC-11】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PC-11_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0485・D0369（不動産登記法／筆界特定・境界、出典 H21-Q15オ／H20-Q12イ）。正解＝D0485＝×（誤った記述）／D0369＝×（誤った記述）。
- 記事：`note-articles/h21-mondai/q15-hikkai-kyakka.md` オ（H21：一筆の土地の一部の所有権を取得した者の申請は、取得した部分以外の筆界についても却下されない。規則207条2項4号・209条1項5号。記事は『制度趣旨・実務上の取扱い』に基づく判断と注記）。ほか、エ（同じ問：対象土地の抵当権者の申請は却下される。法131条1項・123条5号・132条1項2号）、H20-Q12イ（h20-mondai/q12-hikkai-tokutei.md：対象土地の状況は『図面を利用する等の方法』で明示すればよい。規則207条2項7号・4項）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch3.md 【PC-11】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D0485は『取得した部分以外の土地部分の筆界についてする…申請は、却下される』と、取得した部分とそれ以外とを切り分けて却下と言い切る。D0369は『図面によりその内容を明らかにして申請しなければならない』と、申請情報の書き方を図面に限る。どちらも、条文にない限定（部分に限る、図面に限る）を肢の側から足している。
- 【受験者の勘違い・定着していない点】（推測）①一部取得者は『自分が取得した部分』の所有者にすぎないから、取得した部分以外の筆界を申請する資格はないと考え、申請人の範囲を狭く読む（申請人が誰かは、取得した部分かどうかではなく、所有権登記名義人等か、一部取得者として申請情報にその旨を書き取得を証する情報を添えているか、で決まる）。②対象土地の状況の明示は、図面を作って出すことと思い込み、規則207条4項の『図面を利用する等の方法』の『等』を読み落とす。
- 【対比する制度】「一部取得者の申請」⇔「抵当権者の申請」：一部取得者の申請は、申請情報にその旨を書き（規則207条2項4号）、取得を証する情報を添えれば（規則209条1項5号）、取得した部分以外の筆界でも却下されない（記事は実務の取扱いと整理）／抵当権者は所有権登記名義人等に含まれず（法123条5号・131条1項）、申請の権限を有しない者の申請として却下される（法132条1項2号）（結論が逆になる点）。あわせて「図面により」⇔「図面を利用する等の方法」：肢は『図面により…しなければならない』と図面に限るが、規則207条4項は『図面を利用する等の方法』で足り、図面に限られない。
- 【型の選び方】型：型1（思い込み→押さえどころ→違い→結論）。理由：壁＝『条文にない限定を足して読む』という2つの肢に共通の思い込み。誤解の型がはっきりしているので、コマ1で藍子の思い込み（部分に限る、図面に限る）を2肢まとめて出し、コマ2で申請人の資格を『一部取得者は申請できる／抵当権者は却下』の左右のカードで対比し、コマ3で肢D0369の言い分（図面に限る）と規則の文言（図面を利用する等の方法）を上下で対比し、コマ4で暗記3点にした。同じ論点の既存の4コマ（D1996。型3と型2）は『表題登記がない土地の所有者は、所有権を有することを証する情報』の理由と読み方で、今回の2肢とは観点が違う。
- コマごとに読者が言えること：コマ1＝一部取得者の申請は取得部分以外だと却下されるか、状況は図面で出さなければならないか、の2つの問い。コマ2＝一部取得者は申請でき、抵当権者は所有権登記名義人等でないので却下される。コマ3＝状況の明示は『図面を利用する等の方法』で、図面に限られない。コマ4＝D0485は×、D0369は×。
- 記事の範囲：H21-Q15オ（規則207条2項4号は申請人が一筆の土地の一部の所有権を取得した者であるときはその旨を申請情報とし、209条1項5号は取得したことを証する情報の提供を求める。取得した部分以外の筆界の申請も、そのことを理由に却下されるものではないとされる。記事は条文の明文というより制度趣旨・実務上の取扱いに基づく判断と注記しているので、図では断定せず『整理（実務の取扱い）』と添える）。H21-Q15エ（抵当権者の申請は却下）。H20-Q12イ（規則207条2項7号の対象土地の状況は申請情報の内容だが、明示の方法は同条4項の『図面を利用する等の方法』で、図面に限られない。例：図面のほか写真や記載でも伝えられる）。
- extra_refs：不動産登記法123条5号（所有権登記名義人等）・131条1項（土地の所有権登記名義人等は筆界特定の申請ができる）・132条1項2号（申請の権限を有しない者の申請は却下）、不動産登記規則207条2項4号・7号・4項、209条1項5号は、法令DB note-articles/laws/fudousan-touki-hou.md と fudousan-touki-kisoku-2.md で原文を確認。抵当権者の対比（コマ2）は章の記事【PC-11】にはなく、D0485と同じ問の記事（H21-Q15エ）による。
- 同じ論点の他の肢（図には肢として載せない）：D1996（表題登記がない甲土地の所有者は、所有権を有することを証する情報を提供する。〇。規則209条1項4号）は既存の4コマ（D1996_prompt.md、2案）があるので、今回は扱わない。コマ2の一部取得者のカードの『取得を証する情報』は、D1996の『所有権を有することを証する情報』と別の号（5号と4号）であることだけ、規則の号の表示（209条）にとどめた。
- 登場人物：当事者の人型は使わず、申請人の種類・書類は文字のカードで示す。事例の当事者は出さない。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカードと帯、コマ3は上下のカードと会話4往復。
- 配色：コマ1・2は印（✓✕）を付けない（コマ2の左右はどちらも結論の整理で、〇×の対比ではなく『申請できる／却下』の文字で示す）。コマ3の左は上＝赤✕、下＝青✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 筆界特定の申請に、条文にない限定は足さない | 「限定は足さない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　部分に限る？　図面に限る？ | — |
| コマ1 図 | 図・カード | 却下される？　図面が必要？ / 肢D0485 / 取得部分以外の筆界の申請は、却下される / 肢D0369 / 状況は、図面により明らかにして申請する | — |
| コマ1 | 藍子（左・先に話す） | 取得部分以外は却下。状況は図面ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。条文にない限定の足しすぎよ | 「条文にない限定」 |
| コマ2 見出し | ラベル | ②　申請できる人かどうかが分かれ目 | — |
| コマ2 図 | 図・カード | 法131条1項 / 申請人の資格が分かれ目 / 一部取得者の申請 / 規則207条・209条 / 申請情報に、その旨を書く / 取得を証する情報を添える / 取得部分以外の筆界でも申請できる / 抵当権者の申請 / 法131条・132条 / 所有権登記名義人等ではない / 申請の権限がなく、却下される / 一部取得者の申請可は、整理（実務の取扱い） | — |
| コマ3 見出し | ラベル | ③　状況の明示は、図面に限られない | — |
| コマ3 図 | 図・カード | 図面により明らかにして申請 / 肢D0369の言い分 / 図面を利用する等の方法 / 図面に限られない（規則207条4項） | — |
| コマ3 | 藍子（左・1番目） | 状況は、図面で出さないとだめ？ | — |
| コマ3 | トリ先生（右・2番目） | 図面を利用する等の方法、と書いてあるわ | 「図面を利用する等の方法」 |
| コマ3 | 藍子（左・3番目） | 図面以外でもいいんですか？ | — |
| コマ3 | トリ先生（右・4番目） | いいわ。図面は方法の一つよ | 「方法の一つ」 |
| コマ4 見出し | ラベル | ④　結論は×と× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | どちらも、条文より絞って読んでいました！ | — |
| コマ4 | トリ先生（右・答える） | そう。条文にない限定は足さないの | 「条文にない限定」 |
| コマ4 チェック欄 | 3項目（青✓） | 一部取得者は、取得部分以外の筆界でも却下されない（肢D0485は×） / 対象土地の状況は「図面を利用する等の方法」で足り、図面に限られない（肢D0369は×） / 抵当権者は所有権登記名義人等でなく、申請の権限がないので却下される | — |
| 結論帯 | 1行目 | 部分に限る・図面に限る、は足しすぎ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0485・D0369　正解×・×（出典 H21-Q15オ／H20-Q12イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法123条5号・131条1項・132条1項2号、不動産登記規則207条2項4号・7号・4項、209条1項5号（筆界特定の申請人と申請情報・添付情報）。法令DB note-articles/laws/fudousan-touki-hou.md・fudousan-touki-kisoku-2.md と照合済み。抵当権者の対比はH21-Q15エの記事による

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

TITLE BANNER: text 「筆界特定の申請に、条文にない限定は足さない」 in large bold letters; the part 「限定は足さない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　部分に限る？　図面に限る？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「却下される？　図面が必要？」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left and one dark navy text line (each text at least 24 px high).
- Card 1: tag 「肢D0485」, text 「取得部分以外の筆界の申請は、却下される」.
- Card 2: tag 「肢D0369」, text 「状況は、図面により明らかにして申請する」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「取得部分以外は却下。
状況は図面ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
条文にない限定の
足しすぎよ」 with the part 「条文にない限定」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　申請できる人かどうかが分かれ目」
- A small dark navy tag 「法131条1項」 at the top left, with one line beside it: 「申請人の資格が分かれ目」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「一部取得者の申請」, a small tag 「規則207条・209条」, three body lines: 「申請情報に、その旨を書く」, 「取得を証する情報を添える」, 「取得部分以外の筆界でも申請できる」.
- Right card, heading 「抵当権者の申請」, a small tag 「法131条・132条」, two body lines: 「所有権登記名義人等ではない」, 「申請の権限がなく、却下される」, with the heading highlighted with a yellow marker.
- Under the two cards, one wide dark navy band with large white text 「一部取得者の申請可は、整理（実務の取扱い）」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　状況の明示は、図面に限られない」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.
- Top card, heading 「図面により明らかにして申請」, body 「肢D0369の言い分」, and ONE red cross only at the bottom of this card (no check mark on this card).
- Bottom card, heading 「図面を利用する等の方法」, body 「図面に限られない（規則207条4項）」, and ONE blue check mark only at the bottom of this card (no cross on this card).
- The left cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「状況は、図面で
出さないとだめ？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「図面を利用する
等の方法、と
書いてあるわ」 with the part 「図面を利用する等の方法」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「図面以外でも
いいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「いいわ。
図面は
方法の一つよ」 with the part 「方法の一つ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と×」
- 藍子 bubble (left, spoken first): 「どちらも、条文より
絞って読んで
いました！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
条文にない限定は
足さないの」 with the part 「条文にない限定」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「一部取得者は、取得部分以外の筆界でも却下されない（肢D0485は×）」, 「対象土地の状況は「図面を利用する等の方法」で足り、図面に限られない（肢D0369は×）」, 「抵当権者は所有権登記名義人等でなく、申請の権限がないので却下される」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「部分に限る・図面に限る、は足しすぎ」 with a yellow highlighter marker.
- Line 2: 「問題D0485・D0369　正解×・×（出典 H21-Q15オ／H20-Q12イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 対, 当, 所, 抵, 権, 登, 肢, 規, 解, 記, 証, 請 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panels 1 and 2 contain no check mark and no cross anywhere, that panel 3 has exactly one red cross (top card) and one blue check mark (bottom card), and that the only other blue check marks in the whole image are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「一部取得者の申請」 and the right card has the heading 「抵当権者の申請」, never swapped; confirm that the top card of panel 3 has the heading 「図面により明らかにして申請」 and the bottom card has the heading 「図面を利用する等の方法」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不登法第3章_4コマ11_筆界特定の申請に、条文にない限定は足さない.png`
- 途中の版・不採用の版：`不登法第3章_4コマ11_筆界特定の申請に、条文にない限定は足さない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch3/prompt_4koma_PC-11_01_shinseinin-zumen.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『部分に限る』『図面に限る』の2つの思い込みを問う肢だと分かり、コマ2で一部取得者は申請でき抵当権者は却下されること、コマ3で状況の明示は図面に限られないことが言える
- [ ] 工程C：構成表の全文言を記事（H21-Q15オ・エ、H20-Q12イ）・法令DB（法123条5号・131条1項・132条1項2号、規則207条2項4号・7号・4項、209条1項5号）に突き合わせ済み。一部取得者が取得部分以外でも申請できる点は記事が実務の取扱いと注記しているので、図には『整理（実務の取扱い）』と添えた
- [ ] 工程C：コマ1・2に印がなく、コマ3の左は上＝赤✕・下＝青✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない。肢D1996は肢として扱っていない（既存の4コマあり）
- [ ] 工程C：肝の確認：①一部取得者は申請情報にその旨を書き取得を証する情報を添えて申請でき、取得した部分以外の筆界でも却下されない（実務の取扱い）②抵当権者は所有権登記名義人等でなく、申請の権限がないので却下③対象土地の状況は『図面を利用する等の方法』で明示すればよく、図面に限られない④D0485は×、D0369は×

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

## 改訂履歴（このファイルは `src/spec_4koma_PC-11_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第3章【PC-11】用。型1。一部取得者は申請でき抵当権者は却下される対比と、対象土地の状況の明示が『図面を利用する等の方法』で図面に限られない対比を組んだ。既存の4コマ（D1996）とは別の肢）
