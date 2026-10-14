# D1097 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-12】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-12_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1097（不動産登記法／登記制度・総則（登記官・図面・保存期間・管轄・通知）、出典 H27-Q18エ）。正解＝D1097＝〇（正しい記述）。
- 記事：`note-articles/h27-mondai/q18-hozon-kikan.md` エ（H27：閉鎖した土地所在図は、申請書類つづり込み帳につづり込まれたものを除き、閉鎖した日から30年間保存される。不動産登記規則28条13号。申請書類つづり込み帳につづり込まれた書類は受付の日から30年間〔同条9号〕で、電磁的記録に記録して保存したものはその保存した日から30年間〔同号かっこ書〕）。イ（閉鎖した建物所在図は閉鎖しても永久。同条3号）。章の記事 note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md 【PB-12】
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】肢は『閉鎖した土地所在図は…閉鎖した日から30年間』と言い、かっこ書で『申請書類つづり込み帳につづり込まれたものを除き』と添える。同じ問のイ（閉鎖した建物所在図は50年間）が示すとおり、所在図は『閉鎖しても永久』と覚えた受験者は、土地所在図の肢を『永久のはずだ』と読んで×にする。かっこ書の除外も、読む前から身構えさせる。
- 【受験者の勘違い・定着していない点】（推測）①『所在図は閉鎖しても永久』を、建物所在図だけでなく土地所在図にも広げる。永久のまま残るのは地図・地図に準ずる図面・建物所在図で、土地所在図は地積測量図・建物図面・各階平面図と同じ組（13号）で、閉鎖すると30年になることが定着していない。②『つづり込み帳につづり込まれたものを除く』の意味が分からず、除かれたものは別の号で、数え始めの日が違うこと（受付の日など）に結びつかない。
- 【対比する制度】「土地所在図」⇔「建物所在図」：閉鎖した土地所在図は閉鎖した日から30年間（規則28条13号。閉鎖するまでは永久）／閉鎖した建物所在図は閉鎖したものを含めて永久（同条3号。地図・地図に準ずる図面も同じで2号）。名前が似た『所在図』なのに、閉鎖後の扱いが逆になる（結論が逆になる点）。
- 【型の選び方】型：型1（思い込み→押さえどころ→違い→結論）。理由：壁＝『所在図は閉鎖しても永久』という一括りと、かっこ書の除外への不安。誤解の型がはっきりしているので、コマ1で藍子の思い込みを出し、コマ2で2つの所在図の閉鎖後の扱いを左右のカードで対比し、コマ3で肢のかっこ書（除外）の中身を『数え始めの日が違う』2枚のカードで示し、コマ4で暗記3点にした。『なぜ建物所在図だけ永久か』の理由は、条文は号ごとに定めるだけで記事にも書かれていないので、図には入れていない（型3にしなかった理由）。
- コマごとに読者が言えること：コマ1＝閉鎖した土地所在図の保存期間を問う肢で、『所在図は永久』と思い込みやすい。コマ2＝建物所在図は閉鎖しても永久、土地所在図は閉鎖すると30年。コマ3＝除かれる申請書類つづり込み帳の書類は別の号で、数え始めの日も違う。コマ4＝閉鎖した土地所在図は閉鎖の日から30年、この肢は〇。
- 記事の範囲：H27-Q18エ（規則28条13号。閉鎖した土地所在図は閉鎖した日から30年間。申請書類つづり込み帳につづり込まれた書類は受付の日から30年間〔9号〕で、電磁的記録に記録して保存したものは保存した日から30年間〔9号かっこ書〕）。H27-Q18イ（閉鎖した建物所在図は永久。2号・3号）。同じ記事に、建物所在図・地図は閉鎖後も永久、との記述がある。地積測量図・建物図面・各階平面図も13号で土地所在図と同じ組であることは、原文（規則28条13号）で確かめた。
- extra_refs：不動産登記規則28条2号・3号・9号・13号は、法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第二十八条で原文を確認（2号『地図及び地図に準ずる図面（閉鎖したものを含む。）　永久』、3号『建物所在図（閉鎖したものを含む。）　永久』、9号『…申請書類つづり込み帳につづり込まれた書類に記載されたものを含む。…受付の日から三十年間（…電磁的記録に記録して保存した日から三十年間）』、13号『土地所在図、地積測量図、建物図面及び各階平面図（…申請書類つづり込み帳につづり込まれたものを除く。）　永久（閉鎖したものにあっては、閉鎖した日から三十年間）』）。
- 同じ論点の他の肢（図には肢として載せない）：D2027（閉鎖した地積測量図は永久ではなく30年。×）はコマ2のカードに『地積測量図・建物図面・各階平面図も同じ』と同じ組の図面として載せるにとどめ、肢のタグは付けない（条文別シリーズに既存の4コマ）。D1731（書面申請の申請書は受付の日から30年。〇）・D1728（法定相続情報一覧図つづり込み帳は翌年から5年。×）にも既存の4コマがあり、今回は扱わない。
- 登場人物：当事者の人型は使わず、図面・帳簿は文字のカードで示す。事例の当事者は出さない。
- 矢印の意味：矢印は使わない。コマ1は縦2枚のカード、コマ2は左右のカード、コマ3は上下のカードとリボン。
- 配色：コマ1〜3は印（✓✕）を付けない（保存期間は文字で書く。コマ3の2枚はどちらも正しい取扱いで、〇×の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝side（通常サイズのキャラが左右の端、図は中央）、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカードとリボン、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 閉鎖した土地所在図は、閉鎖から30年 | 「閉鎖から30年」を黄色マーカー |
| コマ1 見出し | ラベル | ①　閉鎖した所在図は、何年？ | — |
| コマ1 図 | 図・カード | 肢D1097：閉鎖した土地所在図は、閉鎖の日から30年？ / 土地所在図 / 新しい図面に差し替えられた / 古い土地所在図は閉鎖された / 保存期間 / 閉鎖した土地所在図は、いつまで？ / 申請書類つづり込み帳のものを除く | — |
| コマ1 | 藍子（左・先に話す） | 所在図は、閉鎖しても永久ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。建物所在図との混同よ | 「建物所在図との混同」 |
| コマ2 見出し | ラベル | ②　所在図でも、閉鎖後の扱いが違う | — |
| コマ2 図 | 図・カード | 規則28条 / 閉鎖後の扱いが分かれる / 建物所在図は、閉鎖しても永久 / 3号 / 閉鎖したものを含む / 地図・地図に準ずる図面も同じ / 土地所在図は、閉鎖すると30年 / 13号 / 閉鎖するまでは永久 / 地積測量図・建物図面・各階平面図も同じ | — |
| コマ3 見出し | ラベル | ③　除かれるものは、別の号で数える | — |
| コマ3 図 | 図・カード | 13号 / 閉鎖した土地所在図 / 閉鎖した日から30年間 / つづり込み帳のものを除く / 9号 / つづり込み帳に綴じた書類 / 受付の日から30年間 / 書面の図面は、電磁的記録に保存した日から / ひっかけ：所在図は、閉鎖しても永久 / 閉鎖しても永久 | — |
| コマ3 | 藍子（左・1番目） | つづり込み帳のものを除く、とは？ | — |
| コマ3 | トリ先生（右・2番目） | 別の号で、30年を数えるのよ | 「別の号」 |
| コマ3 | 藍子（左・3番目） | 数え始めの日も同じですか？ | — |
| コマ3 | トリ先生（右・4番目） | 違うわ。受付の日などからよ | 「違うわ」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 閉鎖後に30年なのは、土地所在図なんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。永久なのは、建物所在図の方よ | 「建物所在図の方」 |
| コマ4 チェック欄 | 3項目（青✓） | 閉鎖した土地所在図は、閉鎖した日から30年間（肢D1097は〇） / 閉鎖しても永久なのは、地図・地図に準ずる図面・建物所在図 / つづり込み帳に綴じた書類は、別の号（9号）で数える | — |
| 結論帯 | 1行目 | 閉鎖した土地所在図は、閉鎖から30年 | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1097　正解〇（H27-Q18エ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則28条2号・3号・9号・13号。法令DB note-articles/laws/fudousan-touki-kisoku-1.md の第二十八条で原文と照合済み。記事（H27-Q18エ・イ・R07-Q05イ）が2号・3号・9号・13号を引いている

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

TITLE BANNER: text 「閉鎖した土地所在図は、閉鎖から30年」 in large bold letters; the part 「閉鎖から30年」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　閉鎖した所在図は、何年？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: a small question badge 「肢D1097：閉鎖した土地所在図は、閉鎖の日から30年？」 at the top (a question badge only, with no check mark and no cross), and under it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, with no check mark, no cross, and no arrow anywhere. The two cards are separated only by a small empty gap, with nothing drawn between them.
- Each card has a small dark navy tag at its top left, one bold dark navy heading line, and one body line (each text at least 24 px high).
- Card 1: tag 「土地所在図」, heading 「新しい図面に差し替えられた」, body 「古い土地所在図は閉鎖された」.
- Card 2: tag 「保存期間」, heading 「閉鎖した土地所在図は、いつまで？」, body 「申請書類つづり込み帳のものを除く」.
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「所在図は、
閉鎖しても
永久ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
建物所在図との
混同よ」 with the part 「建物所在図との混同」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　所在図でも、閉鎖後の扱いが違う」
- A small dark navy tag 「規則28条」 at the top left, with one line beside it: 「閉鎖後の扱いが分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「建物所在図は、閉鎖しても永久」, a small tag 「3号」, two body lines: 「閉鎖したものを含む」, 「地図・地図に準ずる図面も同じ」.
- Right card, heading 「土地所在図は、閉鎖すると30年」, a small tag 「13号」, two body lines: 「閉鎖するまでは永久」, 「地積測量図・建物図面・各階平面図も同じ」, with the heading highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　除かれるものは、別の号で数える」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a small dark navy tag at its top left and a dark navy heading placed INSIDE the card, with no check mark, no cross, no arrow, and no connector. The cards are separated only by a small empty gap.
- Top card, tag 「13号」, heading 「閉鎖した土地所在図」, two body lines: 「閉鎖した日から30年間」, 「つづり込み帳のものを除く」.
- Bottom card, tag 「9号」, heading 「つづり込み帳に綴じた書類」, two body lines: 「受付の日から30年間」, 「書面の図面は、電磁的記録に保存した日から」.
- Under the two cards, one dark navy ribbon with white text 「ひっかけ：所在図は、閉鎖しても永久」, with the text 「閉鎖しても永久」 highlighted with a yellow marker.
- The two cards have clearly different texts; the texts are NOT identical, and the dark navy ribbon below them stays in the left column.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「つづり込み帳の
ものを除く、とは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「別の号で、
30年を
数えるのよ」 with the part 「別の号」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「数え始めの日も
同じですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「違うわ。
受付の日などからよ」 with the part 「違うわ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「閉鎖後に30年なのは、
土地所在図
なんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。永久なのは、
建物所在図の方よ」 with the part 「建物所在図の方」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「閉鎖した土地所在図は、閉鎖した日から30年間（肢D1097は〇）」, 「閉鎖しても永久なのは、地図・地図に準ずる図面・建物所在図」, 「つづり込み帳に綴じた書類は、別の号（9号）で数える」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「閉鎖した土地所在図は、閉鎖から30年」 with a yellow highlighter marker.
- Line 2: 「問題D1097　正解〇（H27-Q18エ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 保, 号, 地, 建, 所, 物, 肢, 規, 解, 記, 請, 違, 録, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panels 1, 2 and 3 contain no check mark and no cross anywhere, that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the left card of panel 2 has the heading 「建物所在図は、閉鎖しても永久」 and the right card has the heading 「土地所在図は、閉鎖すると30年」, never swapped; confirm that the top card of panel 3 has the tag 「13号」 and the bottom card has the tag 「9号」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ12_閉鎖した土地所在図は、閉鎖から30年.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ12_閉鎖した土地所在図は、閉鎖から30年_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-12_01_tojita-shozaizu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『閉鎖した土地所在図は何年保存か』を問う肢だと分かり、コマ2で建物所在図と土地所在図の閉鎖後の扱いの違い、コマ3でかっこ書の除外が別の号で数え始めの日も違うことが言える
- [ ] 工程C：構成表の全文言を記事（H27-Q18エ・イ）と法令DB（規則28条2号・3号・9号・13号）に突き合わせ済み。『なぜ建物所在図だけ永久か』の理由づけは図に入れていない（条文・記事に明記がない）
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない。肢D2027は肢として扱わず、コマ2のカードに地積測量図などを同じ組として載せるにとどめた
- [ ] 工程C：肝の確認：①閉鎖した土地所在図は閉鎖した日から30年間（閉鎖するまでは永久）②閉鎖した建物所在図・地図・地図に準ずる図面は永久③除かれる申請書類つづり込み帳の書類は別の号（9号）で、受付の日などから30年間④この肢は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-12_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-14 v01：新規作成（総合記事②不動産登記法編 第2章【PB-12】用。型1。建物所在図は閉鎖しても永久／土地所在図は閉鎖すると30年の対比と、肢のかっこ書（申請書類つづり込み帳のものを除く）が別の号で数え始めの日も違うことを組んだ）
