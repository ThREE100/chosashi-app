# D0404・D0990・D1089 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、区分所有法 第5条（規約敷地）の記事に差し込む4コマ（6本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0404・D0990・D1089（不動産登記法／区分建物・敷地権・共用部分、出典 H20-Q19肢4／H26-Q16オ／H27-Q16オ）。正解＝すべて×（誤った記述）。
- 記事：`note-articles/h26-mondai/q16-kubuntatemono.md` H26-Q16オ（分離処分可能となる敷地権の変更の登記で、抵当権者の承諾の情報があれば、抵当権が消滅した旨が登記される）を軸に、H20-Q19肢4（建物の表題部に関する変更の登記を申請することはできるか）・H27-Q16オ（承諾に係る土地について消滅した旨を登記することはできるか）を同じ法55条1項の問いとしてまとめる
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】3肢とも、同じ場面（敷地権にも効力が及ぶ抵当権のある敷地権付き区分建物で、分離処分できることになって敷地権の変更の登記をする）で、承諾の情報を提供したとしても『申請することはできない』『消滅した旨の登記はされない』『登記することはできない』と言い切る（記事 H20-Q19肢4、H26-Q16オ、H27-Q16オ）。『承諾したことを証する情報を提供したとしても』という前置きで、承諾があっても消せない、と読ませる。
- 【受験者の勘違い・定着していない点】①分筆のときの承諾による消滅（法40条）は知っていても、敷地権の変更の登記の場面（法55条1項）には当てはめられない。②承諾書を出しただけでは抵当権は消えず、別に抹消の登記を申請しないといけないという一般的な感覚が先に立つ（記事 H26-Q16オの『ここが分かりにくいポイント』）。③『申請できる』『登記される』『登記できる』と問われ方が違っても、同じ条文の問いだと気づけない。
- 【対比する制度】「分筆するとき」⇔「分離処分できることになったとき」：どちらも承諾の情報を申請と併せて出せば、承諾に係る土地（または建物）について消滅した旨を登記する、同じ仕組みの場面違い（法40条／法55条1項）。結論が逆になる近接制度ではないが、受験者は法40条は知っていて法55条1項に結びつかない、という取り違えが肝になる。
- 【型の選び方】型：型3（理由説明）＋型4（3肢をまとめ、場面違いの2条文を並べる）。理由：壁は、『承諾書だけで消えるはずがない』という感覚と、条文（承諾の情報が申請と併せて提供されたときは、登記官が消滅した旨を登記しなければならない）が結びつかないこと。コマ2で2つの場面の条文を左右に並べ、コマ3で『承諾の情報の提供そのものが消滅の登記のきっかけになり、別に抹消の登記を申請する必要はない』という理由を示す。
- 記事の範囲：H26-Q16オ（法55条1項。特定登記のある敷地権付き区分建物で、分離処分できることになって敷地権の変更の登記をする場合に、特定登記に係る権利の登記名義人が変更の登記後の建物または土地についてその権利を消滅させることを承諾したことを証する情報が提供されたときは、承諾に係る建物または土地について消滅した旨を登記しなければならない。承諾を証する情報の提供そのものが引き金になる。たとえば、抵当権者が承諾する書類を出せば、敷地権の変更の登記とあわせて抵当権が消滅した旨が登記される）、H20-Q19肢4、H27-Q16オ（いずれも法55条1項）。シリーズ記事 note_art005.md ポイント6（40条と仕組みは同じで場面が違う）。
- extra_refs：①法55条1項・法40条の原文は法令DB note-articles/laws/fudousan-touki-hou.md の第55条・第40条で確認した（どちらも、申請情報と併せて承諾したことを証する情報が提供されたときは、承諾に係る土地〔55条は建物または土地〕について権利が消滅した旨を登記しなければならない）。②『別に抹消の登記を申請する必要はない』『承諾の情報の提供そのものが引き金』は、記事 H26-Q16オの本文（通常の抵当権抹消のように別途の申請行為を要するのではなく、承諾を証する情報が提供されたことそのものが引き金）による。法40条との対比は、シリーズ記事 note_art005.md の整理による。
- 削った周辺情報：特定登記の定義、抵当証券が発行されている場合、第三者の権利の登記がある場合の承諾（法55条1項かっこ書）、法55条2項以下、抹消する旨の登記の方法（規則）。いずれも結論を決める対比と理由ではないので入れない。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。建物・抵当権・書類はアイコンと文字ラベルで示す。
- 矢印の意味：矢印は使わない。コマ1は建物と書類のカード、コマ2は左右のカード、コマ3は左右のカードと帯。
- 配色：コマ1・2は印（✓✕）を付けない。コマ3は左（よくある勘違い）＝赤✕1つ、右（正しい整理）＝青✓1つ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央。図が小さく台詞が2つなので小さくする必要がない）、コマ2＝none（図が主役。左右のカード）、コマ3＝faces（左に比較カードと帯、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 承諾の情報があれば、抵当権が消滅した旨が登記される | 「消滅した旨が登記される」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 敷地権付き区分建物 / 敷地権にも効力が及ぶ抵当権 / 分離処分可能規約を設定。抵当権者が消滅を承諾 / 抵当権の登記は、どうなる？ | — |
| コマ1 | 藍子（左・先に話す） | 承諾の情報を出しても、消せませんよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。分筆のときは知っているのに | 「分筆のとき」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 承諾の情報で消せるのは、分筆のときだけではない / 分筆するとき / 法40条 / 分筆の申請と併せて、承諾の情報を出す / 分筆後の土地に、消滅した旨を登記 / 分離処分できることになったとき / 法55条1項 / 変更の登記と併せて、承諾の情報を出す / 承諾に係る建物または土地に、消滅を登記 | — |
| コマ3 見出し | ラベル | ③　ひっかけと勘違い | — |
| コマ3 図 | 図・カード | よくある勘違い / 承諾しても、別に抹消の登記が要る / ひっかけ：『承諾があっても、できない』という言い切り / 正しい整理 / 申請と併せて承諾の情報を出せば、登記官が消滅した旨を登記 / 理由：承諾の情報の提供そのものが、消滅の登記のきっかけ / たとえば：抵当権者の承諾書を出せば、その抵当権が消滅した旨が登記される | — |
| コマ3 | 藍子（左・1番目） | 承諾しても、できないのでは？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠。法55条1項があるの | 「法55条1項」 |
| コマ3 | 藍子（左・3番目） | 別に、抹消の登記は要らないんですか？ | — |
| コマ3 | トリ先生（右・4番目） | 要らない。申請と併せて出せば足りる | 「申請と併せて」 |
| コマ4 見出し | ラベル | ④　結論は消滅を登記 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 承諾の情報を、併せて出せばいいんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。申請と併せて出すのよ | 「併せて出す」 |
| コマ4 チェック欄 | 3項目（青✓） | 変更の登記の申請と併せて、承諾の情報を出す（法55条1項） / 承諾に係る建物または土地で、抵当権が消滅した旨が登記される / できない・されない、の言い切りは、3肢とも誤り | — |
| 結論帯 | 1行目 | 分離処分でも、承諾の情報で抵当権を消せる | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0404・D0990・D1089　すべて×（誤った記述） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法55条1項・40条（法令DB note-articles/laws/fudousan-touki-hou.md 第55条・第40条）：55条1項＝特定登記のある敷地権付き区分建物について、敷地利用権が専有部分と分離して処分することができるものとなったことにより敷地権の変更の登記をする場合において、申請情報と併せて特定登記に係る権利の登記名義人が変更の登記後の建物または土地について権利を消滅させることを承諾したことを証する情報が提供されたときは、承諾に係る建物または土地について権利が消滅した旨を登記しなければならない。40条＝分筆の登記の申請情報と併せて承諾したことを証する情報が提供されたときは、承諾に係る土地について権利が消滅した旨を登記しなければならない。
- 『承諾の情報の提供そのものが引き金。別に抹消の登記を申請する必要はない』：記事 note-articles/h26-mondai/q16-kubuntatemono.md オの『ここが分かりにくいポイント』（通常の抵当権抹消のように別途の申請行為を要するのではなく、承諾を証する情報が提供されたことそのものが引き金）による。法40条との場面違いの整理はシリーズ記事 note_art005.md ポイント6による

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

TITLE BANNER: text 「承諾の情報があれば、抵当権が消滅した旨が登記される」 in large bold letters; the part 「消滅した旨が登記される」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram in the center, about 56 percent of the panel width: one apartment building icon with a dark navy tag 「敷地権付き区分建物」 and, on it, a white card 「敷地権にも効力が及ぶ抵当権」.
- A white note card beside the building reads 「分離処分可能規約を設定。抵当権者が消滅を承諾」. A small question badge 「抵当権の登記は、どうなる？」 sits above the diagram (a question badge only, with no check mark and no cross).
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, spoken first): 「承諾の情報を出しても、
消せませんよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
分筆のときは
知っているのに」 with the part 「分筆のとき」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A small dark navy tag 「出題者のねらい」 at the top left, with one line beside it: 「承諾の情報で消せるのは、分筆のときだけではない」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross. There is no arrow and no connector between the cards.
- Left card, heading 「分筆するとき」, a small tag 「法40条」, two body lines: 「分筆の申請と併せて、承諾の情報を出す」, 「分筆後の土地に、消滅した旨を登記」.
- Right card, heading 「分離処分できることになったとき」, a small tag 「法55条1項」, two body lines: 「変更の登記と併せて、承諾の情報を出す」, 「承諾に係る建物または土地に、消滅を登記」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　ひっかけと勘違い」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- IMPORTANT: the two comparison cards must show OPPOSITE marks, not the same mark. The left card shows ONE RED cross only; the right card shows ONE BLUE check mark only. Do not draw the same mark on both cards and never draw a check mark on the left card or a cross on the right card. Place each mark in the empty space below the card's body text, never touching or overlapping the text. The two cards also have clearly different texts; the two texts are NOT identical.
- Two large cards side by side, with two strips under them: first a reason strip, then a wide example strip.
- Left card, heading 「よくある勘違い」, body 「承諾しても、別に抹消の登記が要る」, with ONE red cross only (no check mark on this card); a dark navy ribbon tag under the body, with large white text, reads 「ひっかけ：『承諾があっても、できない』という言い切り」.
- Right card, heading 「正しい整理」, body 「申請と併せて承諾の情報を出せば、登記官が消滅した旨を登記」, with ONE blue check mark only (no cross on this card).
- Reason strip (dark navy outline, pale gray fill) under the two cards: 「理由：承諾の情報の提供そのものが、消滅の登記のきっかけ」.
- Example strip under the reason strip: 「たとえば：抵当権者の承諾書を出せば、その抵当権が消滅した旨が登記される」.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「承諾しても、
できないのでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠。
法55条1項があるの」 with the part 「法55条1項」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「別に、抹消の登記は
要らないんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「要らない。申請と
併せて出せば足りる」 with the part 「申請と併せて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は消滅を登記」
- 藍子 bubble (left, spoken first): 「承諾の情報を、
併せて出せばいいんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
申請と
併せて出すのよ」 with the part 「併せて出す」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「変更の登記の申請と併せて、承諾の情報を出す（法55条1項）」, 「承諾に係る建物または土地で、抵当権が消滅した旨が登記される」, 「できない・されない、の言い切りは、3肢とも誤り」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「分離処分でも、承諾の情報で抵当権を消せる」 with a yellow highlighter marker.
- Line 2: 「問題D0404・D0990・D1089　すべて×（誤った記述）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 効, 地, 建, 当, 承, 抵, 権, 物, 登, 肢, 規, 記, 請, 諾, 違 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm the left comparison card has only a red cross and the right card only a blue check mark; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ6_分離処分でも承諾で抵当権を消せる.png`
- 途中の版・不採用の版：`4コマ6_分離処分でも承諾で抵当権を消せる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0404-D0990-D1089_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『抵当権のある敷地権付き区分建物で、分離処分できることになり、敷地権の変更の登記を申請。抵当権者が消滅を承諾した情報を出したら、抵当権は？』、コマ2で『承諾の情報で消せる場面は分筆（法40条）だけでなく、分離処分できることになったとき（法55条1項）もある』、コマ3で『承諾の情報の提供そのものがきっかけで、別に抹消の登記を申請しなくても、登記官が消滅した旨を登記する』が言える
- [ ] 工程C：肝の確認：①法55条1項は、変更の登記の申請と併せて承諾の情報が提供されたときは、承諾に係る建物または土地について消滅した旨を登記しなければならない ②分筆のとき（法40条）と同じ仕組み ③3肢とも、承諾があっても消せないと言い切るので×
- [ ] 工程C：構成表の全文言を記事・法令DBと突き合わせ：『分筆するとき』『分離処分できることになったとき』『承諾に係る建物または土地』『消滅した旨を登記』『併せて』。条文番号は法40条・法55条1項だけで、法令DBの原文で確認済み
- [ ] 工程C：コマ1・2に印がなく、コマ3は左＝赤✕・右＝青✓、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。個人の演習結果と他の肢のIDは図にも設計メモにも入れていない

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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の規約敷地用。分離処分できることになったときの抵当権の消滅を問う3肢を1本にまとめた）
- 2026-10-11 v02：最新ルールで作り直し。コマ2の『承諾で権利を消せる場面は、2つある』を『分筆のときだけではない』に直し（法55条2項以下などほかの場面もあるため、数の断定を外した）、コマ3に『なぜ消えるのか』の理由（承諾の情報の提供そのものが消滅の登記のきっかけ。別に抹消の登記を申請する必要はない）を足した。コマ4の3点目を、分筆の言及から3肢の言い切り（できない・されない）に直した。コマの使い方は side→none→faces→既定
