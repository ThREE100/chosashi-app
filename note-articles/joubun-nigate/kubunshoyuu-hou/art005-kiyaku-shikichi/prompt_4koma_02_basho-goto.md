# D0375・D1577・D1578・D1579 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、区分所有法 第5条（規約敷地）の記事に差し込む4コマ（2本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0375・D1577・D1578・D1579（不動産登記法／区分建物・敷地権・共用部分、出典 H20-Q13ウ／R02-Q14ア・エ・オ）。正解＝D0375・D1578・D1579＝×（誤った記述）／D1577＝〇。
- 記事：`note-articles/r2-mondai/q14-shikichiken.md` ア（規約敷地の分筆に規約の証明は要らない）・エ（分離処分可能規約で敷地権とならない表題登記は、規約の定めの証明が要る）・オ（割合を合算するだけの合体は、割合の規約の証明が要らない）と、H20-Q13ウ（売るための分筆に分離処分可能規約の証明は要らない）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】4つの肢のどれにも『規約』『敷地権』という同じ言葉が出る。分筆（規約敷地の分筆・売るための分筆）、表題登記（敷地権とならないとき）、合体（割合を足すだけ）の場面を並べ、『要しない』『しなければならない』を入れ替えて、登記の種類を見ずに言葉の雰囲気で要否を決めさせる（記事 R02-Q14ア・エ・オ、H20-Q13ウ）。
- 【受験者の勘違い・定着していない点】規約を証する情報が要るかを、登記の種類で決めず、『規約の話だから要る』（または『敷地権にならないから要らない』）と雰囲気で決める。実際は、規約で敷地権の有無や割合が決まる登記（区分建物の表題登記〈令別表12項〉、敷地権の発生・消滅を原因とする変更〈令別表15項〉）には要り、土地の分筆（令別表8項に挙がっていない）と、割合を足すだけの合体（令別表13項ヘのかっこ書）には要らない。分離処分を可能とする規約の証明を『売るための分筆に付ける』と考えるのも、同じ取り違えである。
- 【対比する制度】「規約の証明が要る」⇔「規約の証明は要らない」：規約で敷地権の有無や割合が決まる登記（建物の表題登記・敷地権の変更の登記）は要る／土地の分筆と、割合を足すだけの合体は要らない（結論が逆になる点）。
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由）。理由：4つの肢が『要る登記』と『要らない登記』に分かれるのに、同じ言葉で並んでいて分かれ目が見えないことが壁。コマ1で4つの肢の言い分を並べ、コマ2で『要る／要らない』の2枚のカードと分かれ目（規約で敷地権の有無や割合が決まる登記か）を示し、コマ3で登記の種類ごとの理由（表題登記・分筆・合体）を3枚のカードにした。肢単位の公開版（規約敷地の分筆の管轄違い、敷地権とならない事由）とは、4肢を1本の物差しで並べ直す点で切り口が違う。
- 記事の範囲：部品3（登記に出てくる3種類の規約。敷地権を生じさせる側か、消す・生じさせない側か）、部品6（添付情報の当てはめ。区分建物の表題登記〈令別表12項〉、敷地権が生じる・消える変更の登記〈同15項〉、合体・分筆〈同13項ヘのかっこ書・同8項〉）、ポイント2（登記の種類ごとに令別表で決まっている）。R02-Q14オは『割合が足し算で導けて、あらためて規約を設定したものとはいえない』、H20-Q13ウは『規約を証する情報を提供するのは、分筆の登記ではなく敷地権を消す建物の変更の登記のとき』（令別表15項添付情報欄ハ）。
- extra_refs：①令別表8項（分筆。添付情報は分筆後の地積測量図と、承役地の分筆で地役権設定の範囲が分筆後の一部であるときの情報・地役権図面で、規約を証する情報は掲げられていない）、令別表12項添付情報欄ホ・ヘ、13項添付情報欄ヘ（かっこ書）、15項添付情報欄イ〜ホは、法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md で原文を確認した。②『規約で敷地権の有無や割合が決まる登記に要る』という1本の言い方は、記事の部品3（規約の3種類は敷地権を生じさせる側か消す・生じさせない側か）と部品6の当てはめをまとめた整理で、記事にこの一文はない（ユーザーに伝える）。個々の結論と理由づけ（分筆は令別表8項に挙がっていない、合体は足し算で導ける、分離処分の規約は敷地権を消す変更に要る）は記事の文言による。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。土地・建物・書類は文字ラベルのカードで示す。
- 矢印の意味：矢印は使わない（取引も手続も流れもない）。コマ1は縦4枚の別カード、コマ2は左右のカードと帯、コマ3は縦3枚の理由カード。
- 配色：コマ1〜3は印（✓✕）を付けない（要る・要らないは文字で書く。肢の〇×とも重なって紛らわしくなる）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラの大きさ）：コマ1＝side（通常サイズのキャラが左右の端、図は中央に縦4枚のカード。1枚は見出し1行＋本文1行の短さなので、小さくする必要がない）、コマ2＝none（図が主役。左右のカードと帯）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び。カードと会話の量が多いので顔アイコン）、コマ4＝既定（通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 規約の証明が要るのは、規約で敷地権が決まる登記 | 「規約で敷地権が決まる登記」を黄色マーカー |
| コマ1 見出し | ラベル | ①　4つの肢の言い分 | — |
| コマ1 図 | 図・カード | 規約敷地の分筆 / 別の登記所でも、規約の証明は要らない / 売るための分筆（法定敷地） / 分離処分の規約の証明が要る / 敷地権とならない表題登記 / 規約の定めの証明は要らない / 割合を足すだけの合体 / 割合の規約の証明が要る / 肢の言い分は、正しい？ | — |
| コマ1 | 藍子（左・先に話す） | 規約の話なら、証明は要りますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。要る登記を見分けなさい | 「要る登記」 |
| コマ2 見出し | ラベル | ②　要る登記と、要らない登記 | — |
| コマ2 図 | 図・カード | 出題者のねらい / 要る登記と要らない登記を、入れ替えて並べる / 規約の証明が要る / 令別表12項・15項 / 建物の表題登記 / 敷地権の変更の登記 / 規約の証明は要らない / 令別表8項・13項ヘのかっこ書 / 土地の分筆 / 割合を足すだけの合体 / 分かれ目：規約で敷地権の有無や / 割合が決まる登記かどうか | — |
| コマ3 見出し | ラベル | ③　なぜ、要る登記と要らない登記に分かれる？ | — |
| コマ3 図 | 図・カード | 表題登記：事由は規約で決まる / 分離処分の規約が、敷地権とならない事由 / だから、その規約の証明が要る / 分筆：令別表8項に規約の証明はない / 売るための分離処分の規約の証明は / 敷地権を消す建物の変更に要る / 合体：割合は足し算で出る / あらためて規約を設定したとはいえない / だから、割合の規約の証明は要らない | — |
| コマ3 | 藍子（左・1番目） | 売るための分筆に、規約は要りますよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。要るのは建物の変更よ | 「建物の変更」 |
| コマ3 | 藍子（左・3番目） | 合体で割合を足すだけなら、どうです？ | — |
| コマ3 | トリ先生（右・4番目） | 足し算で出るから、証明は要らないの | 「足し算で出る」 |
| コマ4 見出し | ラベル | ④　結論 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 規約で決まる登記かを見ればいいんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。4つの肢にも当てはめなさい | 「当てはめなさい」 |
| コマ4 チェック欄 | 3項目（青✓） | 土地の分筆に、規約の証明は要らない（令別表8項） / 敷地権とならない表題登記と、敷地権を消す変更には要る（令別表12項・15項） / 割合を足すだけの合体に、割合の規約の証明は要らない（令別表13項ヘのかっこ書） | — |
| 結論帯 | 1行目 | 規約の証明は、規約で敷地権が決まる登記に要る | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0375・D1577・D1578・D1579　D1577＝〇、ほか× | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記令別表8項・12項添付情報欄ホ・ヘ・13項添付情報欄ヘ（かっこ書）・15項添付情報欄イ〜ホ（法令DB note-articles/laws/fudousan-touki-rei-betsuhyou.md）：8項は分筆後の土地の地積測量図などで規約を証する情報は掲げられていない。12項ホは敷地権とならない事由を証する情報、ヘは規約敷地・割合の規約を設定したことを証する情報など。13項ヘのかっこ書は、合体前の二以上の建物がいずれも敷地権付き区分建物で合体後も敷地権付き、かつ割合を合算した割合が合体後の割合となるときは不要。15項イは規約の設定、ロは規約の廃止、ハは分離処分可能規約の別段の定めその他の事由を証する情報。
- 『規約で敷地権の有無や割合が決まる登記に要る』：記事の部品3（規約は敷地権を生じさせる側か、消す・生じさせない側か）と部品6の当てはめをまとめた整理。記事にこの一文はない。

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

TITLE BANNER: text 「規約の証明が要るのは、規約で敷地権が決まる登記」 in large bold letters; the part 「規約で敷地権が決まる登記」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　4つの肢の言い分」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: four SEPARATE cards stacked from top to bottom, all exactly the same size, each with the same pale gray fill and a dark navy outline, a dark navy heading line INSIDE the card, and one dark navy body line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap. Every text in the cards is at least 24 px high.
- Card 1: heading 「規約敷地の分筆」, body 「別の登記所でも、規約の証明は要らない」.
- Card 2: heading 「売るための分筆（法定敷地）」, body 「分離処分の規約の証明が要る」.
- Card 3: heading 「敷地権とならない表題登記」, body 「規約の定めの証明は要らない」.
- Card 4: heading 「割合を足すだけの合体」, body 「割合の規約の証明が要る」.
- At the top, a small question badge in a gray fill with dark navy text 「肢の言い分は、正しい？」 (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel. The four cards have clearly different texts; copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「規約の話なら、
証明は要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
要る登記を
見分けなさい」 with the part 「要る登記」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　要る登記と、要らない登記」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「要る登記と要らない登記を、入れ替えて並べる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「規約の証明が要る」, a small dark navy tag 「令別表12項・15項」, two body lines: 「建物の表題登記」, 「敷地権の変更の登記」.
- Right card, heading 「規約の証明は要らない」, a small dark navy tag 「令別表8項・13項ヘのかっこ書」, two body lines: 「土地の分筆」, 「割合を足すだけの合体」.
- Under the two cards, one wide dark navy band with white text in two lines: 「分かれ目：規約で敷地権の有無や」 and 「割合が決まる登記かどうか」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、要る登記と要らない登記に分かれる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap. Every text in the cards is at least 24 px high.
- Card 1, heading 「表題登記：事由は規約で決まる」, body 「分離処分の規約が、敷地権とならない事由」 and 「だから、その規約の証明が要る」.
- Card 2, heading 「分筆：令別表8項に規約の証明はない」, body 「売るための分離処分の規約の証明は」 and 「敷地権を消す建物の変更に要る」.
- Card 3, heading 「合体：割合は足し算で出る」, body 「あらためて規約を設定したとはいえない」 and 「だから、割合の規約の証明は要らない」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「売るための分筆に、
規約は要りますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
要るのは建物の変更よ」 with the part 「建物の変更」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「合体で割合を
足すだけなら、どうです？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「足し算で出るから、
証明は要らないの」 with the part 「足し算で出る」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論」
- 藍子 bubble (left, spoken first): 「規約で決まる登記かを
見ればいいんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
4つの肢にも
当てはめなさい」 with the part 「当てはめなさい」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「土地の分筆に、規約の証明は要らない（令別表8項）」, 「敷地権とならない表題登記と、敷地権を消す変更には要る（令別表12項・15項）」, 「割合を足すだけの合体に、割合の規約の証明は要らない（令別表13項ヘのかっこ書）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「規約の証明は、規約で敷地権が決まる登記に要る」 with a yellow highlighter marker.
- Line 2: 「問題D0375・D1577・D1578・D1579　D1577＝〇、ほか×」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 売, 建, 当, 所, 権, 無, 物, 登, 肢, 規, 記, 証 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the word 「合体」 is spelled exactly like this everywhere (never 「合併」); confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ2_規約の証明は登記の種類ごと.png`
- 途中の版・不採用の版：`4コマ2_規約の証明は登記の種類ごと_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0375-D1577-D1578-D1579_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『4つの肢が、どの登記について規約の証明が要る・要らないと言っているか』、コマ2で『要るのは建物の表題登記・敷地権の変更、要らないのは土地の分筆と割合を足すだけの合体。分かれ目は規約で敷地権の有無や割合が決まる登記か』、コマ3で『表題登記は事由が規約で決まるので要る／分筆は令別表8項になく、分離処分の規約は敷地権を消す変更に要る／合体は割合が足し算で出る』が言える
- [ ] 工程C：肝の確認：①区分建物の表題登記で分離処分可能規約により敷地権とならないときは、その規約の定めの証明が要る（令別表12項ホ） ②土地の分筆に規約の証明は要らない（令別表8項。規約敷地の分筆も、売るための分筆も同じ）。分離処分の規約の証明は、敷地権を消す変更の登記に要る（令別表15項ハ） ③割合を足すだけの合体で、割合の規約の証明は要らない（令別表13項ヘのかっこ書） ④D1577＝〇、D0375・D1578・D1579＝×
- [ ] 工程C：構成表の全文言を記事・令別表の原文と突き合わせ：『規約で敷地権の有無や割合が決まる』（記事にない言い方の整理。extra_refs②）、『あらためて規約を設定したとはいえない』（記事 R02-Q14オ）、『敷地権を消す建物の変更』（記事 部品6・H20-Q13ウ）。条文番号は令別表8項・12項・13項ヘのかっこ書・15項だけ
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは図や会話が入らないコマだけ顔アイコンにしている

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズの規約敷地用。場面ごとの規約の証明の要否を問う4肢を1本にまとめた）
- 2026-10-11 v02：最新ルールで作り直し。登記の種類ごとに3枚のカードを並べる構成を、『規約で敷地権の有無や割合が決まる登記に要る』という1本の物差しと、登記の種類別の理由カード（表題登記・分筆・合体）に組み直した。肢単位の公開版（D1577、D1578-D0198-D1085）と重ならないよう、4肢を同じ物差しで並べる切り口にした。図には周辺情報（他の肢のID・個人の履歴）を載せていない
