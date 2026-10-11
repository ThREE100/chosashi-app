# D0402・D0405 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、区分所有法 第5条（規約敷地）の記事に差し込む4コマ（1本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0402・D0405（不動産登記法／区分建物・敷地権・共用部分、出典 H20-Q19肢2・5）。正解＝×・×（どちらも誤った記述）。
- 記事：`note-articles/h20-mondai/q19-shikichiken.md` 2「他管轄の土地の登記事項証明書は敷地権発生の場合の添付情報」・5「規約設定証明に限らず、廃止証明・その他の事由証明でも足りる」
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】敷地権の消滅を原因とする変更登記の肢に、『規約』（D0405）や『他の登記所の管轄区域内にある土地の登記事項証明書』（D0402）という、敷地権が生じるときの添付情報と同じ言葉を出し、どの場面でも同じ書類が要るように見せる（記事 H20-Q19肢2・5、令別表15項）。
- 【受験者の勘違い・定着していない点】同じ『規約』という言葉に引かれて、何を定める規約を設定したのか、廃止したのかを読まずに、敷地権が生じるときの添付情報（イ・ホ）を消えるときにも出すと考える。敷地権が消えるのは、規約を廃止したか、分離処分を可能とする別段の定めなどで分離して処分できることになったときで、出すのは廃止または当該事由を証する情報（ロ・ハ）である。
- 【対比する制度】「敷地権が生じるとき」⇔「敷地権が消えるとき」：生じるときは、規約敷地を定める規約を設定したことを証する情報（令別表15項イ）と、土地が他の登記所の管轄なら、その土地の登記事項証明書（同ホ（２））／消えるときは、規約を廃止したことを証する情報（同ロ）、または分離処分できることとなった当該事由を証する情報（同ハ）。出す情報が逆になる点。
- 【型の選び方】型：型3（理由説明）＋型2（当てはめ表）。理由：公開済みの肢単位版は『原因→添付情報』の結論の当てはめが中心なので、条文の記事の4コマ1本目では、壁を『規約という同じ言葉に引かれて、規約の中身を読まない』に置いた。コマ1で3つの規約を並べて問い、コマ2で『規約の中身→生じるか消えるか→出す情報』の3行の表を示し、コマ3で『なぜ消えるときは廃止かその他の事由か（敷地権は分離して処分できないもの。できるようになれば敷地権でなくなる）』の理由を示す。
- 記事の範囲：区分所有法5条1項・22条1項ただし書、不動産登記法44条1項9号（敷地権は、登記された敷地利用権で、分離して処分できないもの）、不動産登記令別表15項のイ・ロ・ハ・ホ（note_art005 部品2・3・6、h20-mondai/q19-shikichiken.md 肢2・肢5）。D0402＝他の登記所の土地の登記事項証明書はホ（２）で、イ及びニの場合（敷地権が生じるとき）に限る。D0405＝消えるときの添付情報はロ（廃止）・ハ（その他の事由）で、イの規約を設定したことを証する情報ではない。
- extra_refs：①令別表15項（イ〜ホ）は法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md で確認（ホの冒頭『イ及びニの場合には』で、（１）規約で定められた割合の規約、（２）他の登記所の管轄の土地の登記事項証明書）。②不動産登記法44条1項9号は note_art005.md 部品2と法令DBで確認。③『規約の中身を読めば生じるか消えるかが決まる』という整理は、note_art005.md 部品3・ポイント1の見分け方にあり、h20の記事（肢2・5）には直接ない。④消えるときの事由（別段の定め）の証明に、規約そのものを示すことが含まれうるため、『規約を設定した証明は消えるときに要らない』とは言い切らず、『イは生じるときの項目、消えるときの項目はロ・ハ』という令別表の位置づけで書いた。
- 登場人物：当事者の記号は使わない。建物・規約はカードと文字ラベル。
- 矢印の意味：矢印は使わない（取引も手続も流れもない）。コマ1は縦3枚の別カード、コマ2は3行の表、コマ3は縦3枚の別カード。
- 配色：コマ1〜3は印（✓✕）を付けない（コマ3は理由のカードで正誤の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。『生じる』『消える』の語も濃紺で、青・赤にしない。
- コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央に縦3枚のカードと疑問バッジ。図の量が少ないので小さくする必要がない）、コマ2＝none（3行の表が主役で、台詞はない）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。
- 公開済みの肢単位版（D0402-D0405_prompt.md）との違い：向こうは『生じるとき⇔消えるとき』の左右カードと原因ごとの当てはめが中心。こちらは、コマ1で規約の3つの言い方を並べて『規約の中身を読む』が壁だと示し、コマ3で理由（敷地権の定義と分離処分）を足した。同じ問の別の肢の記述は入れていない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 規約の中身を読めば、出す情報が決まる | 「出す情報が決まる」を黄色マーカー |
| コマ1 見出し | ラベル | ①　同じ規約でも、中身が違う | — |
| コマ1 図 | 図・カード | 規約敷地を定める規約を設定した / その規約を廃止した / 分離処分を可能とする規約を設定した / どれも規約。出す情報は同じ？ | — |
| コマ1 | 藍子（左・先に話す） | どれも規約だから、規約の証明ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。規約の中身が違うのよ | 「規約の中身」 |
| コマ2 見出し | ラベル | ②　規約の中身と、出す情報 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 規約の中身で、出す情報が変わる / 生じる / 消える / 規約敷地を定める規約を設定した / 敷地権が生じるとき / その規約を設定したことを証する情報 / 他の登記所の土地なら、その登記事項証明書も / イ・ホ / その規約を廃止した / 敷地権が消えるとき / その規約を廃止したことを証する情報 / ロ / 分離処分を可能とする別段の定め / その事由を証する情報 / ハ / 不動産登記令別表15項 | — |
| コマ3 見出し | ラベル | ③　なぜ、消えるときは廃止か事由？ | — |
| コマ3 図 | 図・カード | 敷地権は、分離して処分できないもの / 分離して処分できれば、敷地権でなくなる / 法44条1項9号 / 廃止か別段の定めで、分離処分できる / 規約敷地の規約を廃止したとき / 分離処分を可能とする別段の定めがあるとき / 分かれ目：敷地権が生じるのか、消えるのか / だから、出すのは廃止か事由の証明 / 廃止したことを証する情報 / または、その事由を証する情報 | — |
| コマ3 | 藍子（左・1番目） | 規約と書いてあるから、設定の証明では？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。分離処分できれば敷地権は消えるのよ | 「敷地権は消える」 |
| コマ3 | 藍子（左・3番目） | では、土地の証明書は、消えるときも？ | — |
| コマ3 | トリ先生（右・4番目） | それは生じるときだけの添付情報よ | 「生じるときだけ」 |
| コマ4 見出し | ラベル | ④　結論はどちらも× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 規約の中身で、出す情報が決まるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。この2つの肢は、どちらも×よ | 「どちらも×」 |
| コマ4 チェック欄 | 3項目（青✓） | 令別表15項：規約を設定した証明（イ）は、生じるとき / 消えるとき：廃止（ロ）かその他の事由（ハ）の証明 / 他の登記所の土地の登記事項証明書は、生じるときだけ（ホ） | — |
| 結論帯 | 1行目 | 規約の中身を読めば、出す情報が決まる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0402・D0405　正解×・×（H20-Q19肢2・5） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令別表15項の添付情報欄イ・ロ・ハ・ホ（法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md の十五）：イ＝区分所有法第5条第1項の規約を設定したことにより敷地権が生じたときは、当該規約を設定したことを証する情報。ロ＝イの規約を廃止したことにより分離して処分することができることとなったときは、当該規約を廃止したことを証する情報。ハ＝区分所有法第22条第1項ただし書の規約における別段の定めがあることその他の事由により分離して処分することができることとなったときは、当該事由を証する情報。ホ＝イ及びニの場合に、（２）敷地権の目的である土地が他の登記所の管轄区域内にあるときは、当該土地の登記事項証明書。
- 不動産登記法44条1項9号（法令DB note-articles/laws/fudousan-touki-hou.md、note_art005.md 部品2）：敷地権＝登記された敷地利用権で、区分所有法22条1項本文により専有部分と分離して処分することができないもの。『分離して処分できれば敷地権でなくなる』は、この定義と令別表15項ロ・ハの『分離して処分することができることとなったとき』の文言からの整理。
- 『規約の中身を読めば、生じるか消えるかが決まる』：note_art005.md 部品3（規約敷地を定める規約は敷地権を生じさせる側、分離処分を可能とする規約は敷地権を消す側）とポイント1の見分け方。h20-mondai/q19-shikichiken.md（肢2・肢5）にはこの整理が直接はない。

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

TITLE BANNER: text 「規約の中身を読めば、出す情報が決まる」 in large bold letters; the part 「出す情報が決まる」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　同じ規約でも、中身が違う」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.
- Card 1: 「規約敷地を定める規約を設定した」. Card 2: 「その規約を廃止した」. Card 3: 「分離処分を可能とする規約を設定した」.
- At the top, a small question badge in a gray fill with dark navy text 「どれも規約。出す情報は同じ？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「どれも規約だから、
規約の証明ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
規約の中身が
違うのよ」 with the part 「規約の中身」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　規約の中身と、出す情報」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「規約の中身で、出す情報が変わる」.
- A table of exactly three rows in the center, all rows the same height and the same width, each row a wide card with the same pale gray fill and a dark navy outline, containing three cells from left to right (no arrows, no connectors, no check mark, no cross, and no header row): the left cell holds the rule, the middle cell is a white pill with dark navy text saying whether the land right arises or disappears (the words 「生じる」 and 「消える」 are dark navy, never blue and never red), and the right cell holds the information to submit.
- Row 1: left cell 「規約敷地を定める規約を設定した」, middle pill 「敷地権が生じるとき」, right cell 「その規約を設定したことを証する情報」 and a second smaller line 「他の登記所の土地なら、その登記事項証明書も」, and a small dark navy tag 「イ・ホ」 at the right end of the row.
- Row 2: left cell 「その規約を廃止した」, middle pill 「敷地権が消えるとき」, right cell 「その規約を廃止したことを証する情報」, and a small dark navy tag 「ロ」 at the right end of the row.
- Row 3: left cell 「分離処分を可能とする別段の定め」, middle pill 「敷地権が消えるとき」, right cell 「その事由を証する情報」, and a small dark navy tag 「ハ」 at the right end of the row.
- The three rows have clearly different texts; the texts are NOT identical.
- Under the table, one wide dark navy band with white text: 「不動産登記令別表15項」.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、消えるときは廃止か事由？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「敷地権は、分離して処分できないもの」, one body line 「分離して処分できれば、敷地権でなくなる」, and a small dark navy tag 「法44条1項9号」.
- Card 2, heading 「廃止か別段の定めで、分離処分できる」, body 「規約敷地の規約を廃止したとき」 and 「分離処分を可能とする別段の定めがあるとき」, and a dark navy ribbon tag with large white text 「分かれ目：敷地権が生じるのか、消えるのか」.
- Card 3, heading 「だから、出すのは廃止か事由の証明」, body 「廃止したことを証する情報」 and 「または、その事由を証する情報」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「規約と書いてあるから、
設定の証明では？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。分離処分できれば
敷地権は消えるのよ」 with the part 「敷地権は消える」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、土地の証明書は、
消えるときも？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それは生じるときだけの
添付情報よ」 with the part 「生じるときだけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論はどちらも×」
- 藍子 bubble (left, spoken first): 「規約の中身で、
出す情報が
決まるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。この2つの肢は、
どちらも×よ」 with the part 「どちらも×」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「令別表15項：規約を設定した証明（イ）は、生じるとき」, 「消えるとき：廃止（ロ）かその他の事由（ハ）の証明」, 「他の登記所の土地の登記事項証明書は、生じるときだけ（ホ）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「規約の中身を読めば、出す情報が決まる」 with a yellow highlighter marker.
- Line 2: 「問題D0402・D0405　正解×・×（H20-Q19肢2・5）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 所, 権, 登, 肢, 規, 解, 記, 証, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ1_発生と消滅は添付情報が違う.png`
- 途中の版・不採用の版：`4コマ1_発生と消滅は添付情報が違う_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0402-D0405_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『規約の3つの言い方。添付情報は同じか』、コマ2で『規約の中身で、生じるか消えるかが決まり、出す情報が変わる（イ・ホ／ロ／ハ）』、コマ3で『敷地権は分離して処分できないもの。できるようになれば消えるので、出すのは廃止または当該事由の証明』が言える
- [ ] 工程C：肝の確認：①規約敷地を定める規約を設定したら敷地権が生じ、規約を設定したことを証する情報と（他の登記所の土地なら）登記事項証明書を出す ②規約を廃止したら消え、廃止を証する情報 ③分離処分を可能とする別段の定めなどで消えるときは当該事由を証する情報 ④土地の登記事項証明書は生じるときだけ ⑤肢D0402・D0405はどちらも×
- [ ] 工程C：構成表の全文言を記事・令別表15項と突き合わせ：『規約敷地を定める規約』『規約を設定したことを証する情報』『規約を廃止したことを証する情報』『その事由を証する情報』『他の登記所の土地の登記事項証明書』『分離して処分できない』。出題当時と今の言い方の違いの説明、他の肢の記述は入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは、図や会話が入らないコマだけ小さくしている

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の規約敷地用。敷地権の発生と消滅の添付情報の違いを問う2肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
- 2026-10-11 v02：最新ルールで作り直し。決め手の対比（規約の中身→生じるか消えるか→令別表15項のイ・ホ／ロ／ハ）と理由（敷地権は分離して処分できないもの）に絞り、公開済みの肢単位版の当てはめ表と切り口を変えた。コマ1のキャラは通常サイズ（side）
