# D0649・D1850 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第40条の記事に差し込む4コマ（4本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0649・D1850（不動産登記法／土地の分筆・合筆・地積更正、出典 H23-Q08エ／R05-Q09ア）。正解＝×・×（どちらも誤った記述）。
- 記事：`note-articles/h23-mondai/q08-bunpitsu-gappitsu-kenri.md` H23-Q08エ（承諾の情報を提供して権利を消した分筆は、分筆錯誤だけでは抹消を申請できない）を軸に、R05-Q09ア（分筆前から付いていた抵当権が写っただけなら、錯誤を原因に分筆の登記を抹消できる）と対比する
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】2肢は言い切りの向きが逆。D0649は『承諾…を提供して分筆の登記がされた場合であっても…分筆錯誤を原因として…抹消を申請することができる』と、錯誤なら承諾で権利を消した分筆でも戻せるように書く。D1850は『抵当権の設定の登記がされた土地について分筆の登記がされた後は、錯誤を原因とする…抹消をすることはできない』と、抵当権があれば戻せないように書く。どちらも、分筆のときに権利を消したかどうかを見落とさせる。
- 【受験者の勘違い・定着していない点】推測：①錯誤による申請なら、分筆の登記はいつでも抹消できると考える（D0649の言い切りに乗る）。②抵当権の登記がある土地の分筆は、錯誤では抹消できないと決めつける（D1850の言い切りに乗る）。③どちらも、抵当権があるかどうかだけで答えを決め、分筆のときに承諾の情報で権利を消したかを確かめない。片方の言い切りだけを覚えると、逆向きの肢で迷う。
- 【対比する制度】「権利が写っただけ」⇔「承諾で権利を消した」：前者（分筆前から付いていた抵当権が分筆後の土地に写っただけ）は、錯誤を原因に分筆の登記を抹消できる（D1850の『できない』は誤り）。後者（承諾の情報を提供して、権利が消滅した旨の登記までされた）は、分筆錯誤だけでは抹消を申請できない（D0649の『できる』は誤り）。結論が逆になる点は、分筆のときに権利を消す登記までしたか。
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由）。理由：壁＝2肢が逆向きの言い切りなのに、どちらも×で、どこで分かれるかを自分で並べ直せないこと。コマ1＝2肢の言い分を並べる（別々の問題文なので時系列でなく2枚のカード）、コマ2＝『写っただけ』⇔『承諾で消した』の左右対比（各カードに、どちらの肢がその場面で誤りかのタグ）、コマ3＝対比の両側の理由（写っただけなら公示関係は複雑にならない／承諾で消したなら権利の消滅まで登記され、分筆だけ抹消しても消えた抵当権は復活しない）、コマ4＝2肢とも×の整理。是正の手続・出題当時の言い方は決め手でないので入れない。
- 記事の範囲：H23-Q08エ（承諾の情報を提供して分筆の登記がされた場合は、抵当権の消滅という権利変動を伴う。分筆錯誤を原因として単純に分筆の登記の抹消を申請することはできない。条文に明記はなく、登記実務の取扱いによる整理。分筆の登記だけを抹消しても、いったん消滅した抵当権が当然に復活するわけではない）、R05-Q09ア（分筆の登記の抹消ができなくなるのは、分筆と同時に消滅承諾の情報を添えて権利の登記を消滅させた場合で、公示関係が複雑になるため。分筆前から抵当権が設定されていたケースはそのような複雑化は生じず、錯誤を原因とする分筆登記の抹消ができる）。
- extra_refs：①不動産登記法40条（登記官は、承諾に係る土地について当該権利が消滅した旨を登記しなければならない）：note-articles/laws/fudousan-touki-hou.md の第40条で確認。D0649の記事のア（H23-Q08ア）の解説にも引用がある。②『写っただけなら錯誤で抹消できる』はR05-Q09アの記事（note-articles/r5-mondai/q09-bunpitsu.md）から取った。D0649の記事（H23-Q08エ）にはない対比。③コマ3の理由は両方の記事の文言（『複雑化は生じず』『公示関係が複雑になる』『当然に復活するわけではない』）のとおりで、条文に直接の根拠はなく、登記実務の整理。『権利を消したことまで錯誤とは限らない』という言い方は、2つの記事にはなく、条文別記事（note_art040.md）にだけあるので、図には入れない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。甲土地・乙土地も図に出さず、文字ラベルのカードで示す。
- 矢印の意味：矢印は使わない。コマ1は2枚のカード、コマ2は左右のカード、コマ3は3枚のカード。
- 配色：コマ1〜3は印（✓✕）を付けない（肢の〇×と印の向きが重なって紛らわしいため、可否は文字で書く）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、リボン・帯・タグは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央に2枚のカードと疑問バッジ。図が少ないので小さくする必要がない）、コマ2＝none（左右のカードと帯が主役）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。
- コマごとに読者が言えること：コマ1＝2肢は言い切りが逆（できる／できない）だが、どちらも×。コマ2＝分筆前から付いていた抵当権が写っただけなら抹消できる（D1850は誤り）。承諾で権利を消したなら分筆錯誤だけでは抹消を申請できない（D0649は誤り）。コマ3＝写っただけなら公示関係は複雑にならない。承諾で消すと権利の消滅まで登記され、分筆だけ抹消しても消えた抵当権は当然には復活しない。コマ4＝抵当権の有無ではなく、権利を消したかで決まる。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 錯誤で戻せるかは、権利を消したかで決まる | 「権利を消したか」を黄色マーカー |
| コマ1 見出し | ラベル | ①　逆の言い切り、両方×？ | — |
| コマ1 図 | 図・カード | 肢D0649の言い分 / 承諾の情報を出した分筆であっても / 錯誤で抹消を申請できる / 肢D1850の言い分 / 抵当権の登記がある土地の分筆の後は / 錯誤で抹消はできない / 錯誤で、分筆の登記を抹消できる？ | — |
| コマ1 | 藍子（左・先に話す） | 言い切りが逆なのに、両方×ですか？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。どちらも言い切りすぎなのよ | 「言い切りすぎ」 |
| コマ2 見出し | ラベル | ②　写っただけと、承諾で消した | — |
| コマ2 図 | 図・カード | 同じ分筆の錯誤でも / 分筆のときに何をしたかで、結論が分かれる / 権利が写っただけ / 分筆前から付いていた抵当権が写っただけ / 錯誤で、分筆の登記を抹消できる / 肢D1850は、この場面で誤り / 承諾で権利を消した / 権利が消滅した旨の登記もされた / 分筆錯誤だけでは、抹消を申請できない / 肢D0649は、この場面で誤り / 分筆のときに、権利を消す登記までしたか / ここが、錯誤で戻せるかの分かれ目 | — |
| コマ3 見出し | ラベル | ③　なぜ、そうなる？ | — |
| コマ3 図 | 図・カード | 写っただけの分筆なら / 消えた権利はない / 公示関係は複雑にならない / 承諾の情報を出した分筆なら / 登記官は、権利が消滅した旨を登記する / （法40条） / 分筆の登記だけを抹消しても / 消えた抵当権は、当然には復活しない / 公示関係が複雑になる | — |
| コマ3 | 藍子（左・1番目） | 抵当権があると、抹消できませんよね？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。写っただけなら抹消できるのよ | 「写っただけ」 |
| コマ3 | 藍子（左・3番目） | 承諾で消した後も、錯誤なら戻せませんか？ | — |
| コマ3 | トリ先生（右・4番目） | 消えた抵当権は、当然には復活しないのよ | 「当然には復活しない」 |
| コマ4 見出し | ラベル | ④　結論は両方× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 抵当権の有無ではなく、消したかですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。言い切りは危ないわよ | 「言い切り」 |
| コマ4 チェック欄 | 3項目（青✓） | 分筆前から付いていた抵当権が写っただけなら、錯誤で分筆の登記を抹消できる（肢D1850は×） / 承諾で権利を消したなら、分筆錯誤だけでは抹消を申請できない（肢D0649は×。条文に明記がなく、登記実務の整理） / 見分け方：抵当権があるかではなく、分筆のときに権利を消したかを見る | — |
| 結論帯 | 1行目 | 権利を消せば戻せず、写っただけなら戻せる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0649・D1850　どちらも×（誤った記述） | — |

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

TITLE BANNER: text 「錯誤で戻せるかは、権利を消したかで決まる」 in large bold letters; the part 「権利を消したか」 has a yellow highlighter marker.

PANEL 1 (puzzled, curious mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　逆の言い切り、両方×？」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill and a dark navy outline, a small dark navy tag fully inside the top of the card, and two short dark navy body lines, with only a small empty gap between them. Do NOT draw any arrow anywhere in this panel, do NOT connect the cards, and draw no check mark and no cross.
- Top card: tag 「肢D0649の言い分」, body lines 「承諾の情報を出した分筆であっても」 and 「錯誤で抹消を申請できる」.
- Bottom card: tag 「肢D1850の言い分」, body lines 「抵当権の登記がある土地の分筆の後は」 and 「錯誤で抹消はできない」.
- At the top, a small question badge in a gray fill with dark navy text 「錯誤で、分筆の登記を抹消できる？」 (a question badge only, with no check mark and no cross).
- The two cards have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「言い切りが逆なのに、
両方×ですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
どちらも
言い切りすぎなのよ」 with the part 「言い切りすぎ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　写っただけと、承諾で消した」
- A small dark navy tag 「同じ分筆の錯誤でも」 at the top left, with one line beside it: 「分筆のときに何をしたかで、結論が分かれる」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark, no cross, and no arrow anywhere in this panel. Only a small empty gap separates the two cards, with nothing drawn between them.
- Left card: heading 「権利が写っただけ」, two body lines 「分筆前から付いていた抵当権が写っただけ」 and 「錯誤で、分筆の登記を抹消できる」, and a small dark navy tag 「肢D1850は、この場面で誤り」.
- Right card: heading 「承諾で権利を消した」, two body lines 「権利が消滅した旨の登記もされた」 and 「分筆錯誤だけでは、抹消を申請できない」, and a small dark navy tag 「肢D0649は、この場面で誤り」.
- Under the two cards, one wide dark navy band with white text in two lines: 「分筆のときに、権利を消す登記までしたか」 and 「ここが、錯誤で戻せるかの分かれ目」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、そうなる？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「写っただけの分筆なら」, body 「消えた権利はない」 and 「公示関係は複雑にならない」.
- Card 2, heading 「承諾の情報を出した分筆なら」, body 「登記官は、権利が消滅した旨を登記する」 and 「（法40条）」.
- Card 3, heading 「分筆の登記だけを抹消しても」, body 「消えた抵当権は、当然には復活しない」 and 「公示関係が複雑になる」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「抵当権があると、
抹消できませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。写っただけなら
抹消できるのよ」 with the part 「写っただけ」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「承諾で消した後も、
錯誤なら戻せませんか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「消えた抵当権は、
当然には復活しないのよ」 with the part 「当然には復活しない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は両方×」
- 藍子 bubble (left, spoken first): 「抵当権の有無ではなく、
消したかですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
言い切りは
危ないわよ」 with the part 「言い切り」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「分筆前から付いていた抵当権が写っただけなら、錯誤で分筆の登記を抹消できる（肢D1850は×）」, 「承諾で権利を消したなら、分筆錯誤だけでは抹消を申請できない（肢D0649は×。条文に明記がなく、登記実務の整理）」, 「見分け方：抵当権があるかではなく、分筆のときに権利を消したかを見る」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「権利を消せば戻せず、写っただけなら戻せる」 with a yellow highlighter marker.
- Line 2: 「問題D0649・D1850　どちらも×（誤った記述）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 地, 当, 承, 抵, 権, 無, 登, 肢, 記, 請, 諾 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that in panel 1 the TOP card has the tag 「肢D0649の言い分」 and the BOTTOM card has the tag 「肢D1850の言い分」, never swapped; confirm that in panel 2 the LEFT card has the heading 「権利が写っただけ」 with the tag 「肢D1850は、この場面で誤り」 and the RIGHT card has the heading 「承諾で権利を消した」 with the tag 「肢D0649は、この場面で誤り」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ4_権利を消した分筆は錯誤で戻せない.png`
- 途中の版・不採用の版：`4コマ4_権利を消した分筆は錯誤で戻せない_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0649-D1850_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『抵当権の登記がある土地を分筆したあと、錯誤と分かった。D0649は〜でも抹消できる、D1850は〜抹消はできない、と逆に言い切る』、コマ2で『写っただけなら抹消できる／承諾で消したなら抹消を申請できない。D1850は左の場面で誤り、D0649は右の場面で誤り』、コマ3で『写っただけなら複雑にならない。承諾で消すと権利の消滅まで登記され、分筆だけ抹消しても復活しない』が言える
- [ ] 工程C：肝の確認：①写っただけなら錯誤で抹消できる（R05-Q09ア） ②承諾で権利を消したなら分筆錯誤だけでは抹消を申請できない（H23-Q08エ。条文に明記なく、登記実務の整理） ③承諾の情報があると、登記官は権利が消滅した旨を登記する（法40条） ④消えた抵当権は分筆の登記を抹消しても当然には復活しない ⑤D0649もD1850も×
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『分筆前から付いていた抵当権』『権利が消滅した旨を登記』『当然には復活しない』『公示関係が複雑』『条文に明記がなく、登記実務の整理』。是正の手続・出題当時の言い方・『権利を消したことまで錯誤とは限らない』は入れていない
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない

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

- 2026-10-11 v02：最新ルールで作り直し（型4＋型3。2肢を『言い切りが逆でどちらも×』の対比で1本にした。是正の手続（権利の登記を抹消→合筆→改めて設定）・『権利を消したことまで錯誤とは限らない』・タイトルの偏りを除き、理由をコマ3の3枚のカードに両側を入れた。コマ1をsideにした。ChatGPTでの生成・検品はまだ）
