# D0686・D0772 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第51条第1項の記事に差し込む4コマ（4本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0686・D0772（不動産登記法／建物の分割・合併・合体・滅失・変更、出典 H23-Q16ア／H24-Q13イ）。正解＝×・×（どちらも誤った記述）。
- 記事：`note-articles/h23-mondai/q16-hyouji-touki-gimu.md` ア「増築登記の起算点は、工事が終わった日」。ほか、H24-Q13イ（q13-tatemono-hyouji-touki.md）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】アは、主語を『増築した当時の登記名義人』にしながら、起算点を後ろの日付（共用部分である旨の登記がされた日）に書いている点。イは、主語を『改築のあとに所有権を取得したＢ』にしながら、起算点を『改築工事が完了した日』という工事の日付に書いている点。どちらも、主語の人と起算点の日が合っていない（記事 H23-Q16ア、H24-Q13イ）。
- 【受験者の勘違い・定着していない点】肢に出てくる日付（工事が完了した日／共用部分である旨の登記がされた日／所有権の登記があった日）のうち、目についた日に引かれ、主語の人を先に読まない。実際は、変更のときの名義人は工事が完了した日（1項）、変更のあとに名義人になった者は自分の所有権の登記があった日（2項）、共用部分である旨の登記の日から数えるのは1項・2項の人を除く所有者（3項）。
- 【対比する制度】「工事のときの名義人（法51条1項）」⇔「工事のあとに名義人になった者（法51条2項）」：前者は変更があった日（工事が完了した日）から1か月／後者はその者に係る所有権の登記があった日から1か月。『共用部分である旨の登記の日』は3項の日で、1項・2項の人には使えない。主語が違うと起算点が変わり、同じ日付を当てはめると誤りになる。
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由説明）。理由：壁は、2肢を別々に見ると『主語によって起算点が変わる』という共通の仕組みが見えず、なぜその日が使えないのかも分からないこと。コマ1に2人の時系列（主語の違い）、コマ2に主語ごとの起算点（条文の対応）、コマ3に『なぜ共用部分の登記の日・工事完了の日が使えないのか』の理由のカード、コマ4に暗記3点を置いた。同じ論点を1肢で扱った単独版は『3項のかっこ書がなぜ1項の人の起算点を動かさないか』が中心で、この4コマは『主語→起算点の対応と、2肢の罠が同じ型であること』を1枚で見る別の切り口。
- 登場人物：当事者の記号は使わない（lead1だけ問題文どおり）。人物は『工事のときの名義人』『工事のあとに名義人になった者』という文字タグだけで示す。
- 矢印の意味：コマ1の矢印は『時間の流れ』だけ。コマ2・3は矢印を使わない。
- 会話順：藍子の誤解（どの人も、工事が終わった日から）→トリ先生の訂正（人によって違う）→藍子が共用部分の登記の日を言う→トリ先生が3項は1項の人を除くと答える→藍子が買った人を聞く→トリ先生が2項と答える。
- 配色：コマ1・2・3は印（✓✕）を付けない（コマ3は理由の説明であり、正誤の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方（キャラの大きさ）：コマ1＝side（キャラは通常サイズで左右の端、図は中央に2本の時系列。図の量が少ないので小さくする必要がない）、コマ2＝none（図が主役。2枚のカードと帯）、コマ3＝faces（左に理由のカード2枚、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。
- 記事の範囲：法51条1項（変更があった日）／同条2項（その者に係る所有権の登記があった日）／同条3項かっこ書（1項・2項の人を除く所有者。共用部分である旨の登記がされた日から）／1か月。記事 H23-Q16ア：3項は1項の人の起算点を後ろへずらす規定ではなく、1項の人の義務は、あとから共用部分である旨の登記がされても消えず、起算点も工事完了の日のまま。記事 H24-Q13イ：変更後に所有権を取得した者は、改築工事が完了した日からではなく、その者に係る所有権の登記があった日から。
- extra_refs：条文は法令DB note-articles/laws/fudousan-touki-hou.md の第51条1項〜3項で原文を確認した（1項＝変更があった日から一月、2項＝その者に係る所有権の登記があった日から一月、3項＝共用部分である旨の登記がされた日から一月で、前二項の規定により登記を申請しなければならない者を除く）。記事にない整理はない。
- 削った周辺情報：4項（共用部分の建物で変更のあとに所有権を取得した者。所有権の取得の日）、5項・6項（区分建物の特例）、過料（法164条）、土地の37条。この2肢を決める対比ではないため入れない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 変更の登記の1か月は、人ごとに違う日から数える | 「人ごとに違う日」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 時間の流れ / 工事のときの名義人 / 増築の工事が完了 / 共用部分である旨の登記がされる / 工事のあとに名義人になった者 / 改築の工事が完了 / その者の所有権の登記がされる / 1か月は、どこから数える？ | — |
| コマ1 | 藍子（左・先に話す） | どの人も、工事が終わった日からですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。人によって違うのよ | 「人によって違う」 |
| コマ2 見出し | ラベル | ②　主語の人で、数える日が決まる | — |
| コマ2 図 | 図・カード | 先に読む / 誰の1か月か / 工事のときの名義人（法51条1項） / 工事が完了した日から1か月 / 工事のあとに名義人になった者（法51条2項） / その者の所有権の登記があった日から1か月 / 共用部分の登記の日から数えるのは、1項・2項の人を除く所有者（法51条3項） | — |
| コマ3 見出し | ラベル | ③　なぜ、その日は使えない？ | — |
| コマ3 図 | 図・カード | 工事のときの名義人に、共用部分の登記の日は使えない / 義務は消えず、起算点も工事完了の日のまま / 3項のかっこ書が、1項の人を除いている / 買った人に、工事完了の日は使えない / 変更のあとに所有権を取得した者は、2項 / 自分の所有権の登記があった日から / 分かれ目：主語は誰か | — |
| コマ3 | 藍子（左・1番目） | 共用部分の登記の日からでは？ | — |
| コマ3 | トリ先生（右・2番目） | それが罠よ。3項は1項の人を除くの | 「3項は1項の人を除く」 |
| コマ3 | 藍子（左・3番目） | では、買った人はどうなりますか？ | — |
| コマ3 | トリ先生（右・4番目） | 2項で、自分の登記の日から数えるのよ | 「自分の登記の日」 |
| コマ4 見出し | ラベル | ④　結論は両方× | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 数え始めは、人ごとに違うんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。主語を見てから日を選ぶのよ | 「主語を見てから」 |
| コマ4 チェック欄 | 3項目（青✓） | 工事のときの名義人は、工事が完了した日から（法51条1項） / あとに名義人になった者は、自分の所有権の登記の日から（法51条2項） / 共用部分の登記の日は、3項の所有者の日（1項・2項の人は除く） | — |
| 結論帯 | 1行目 | 1か月は、主語の人を見てから起算点を選ぶ | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0686・D0772　どちらも×（誤った記述） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法第51条1項〜3項（法令DB note-articles/laws/fudousan-touki-hou.md）：1項＝第四十四条第一項各号（第二号及び第六号を除く。）の登記事項について変更があったときは、表題部所有者又は所有権の登記名義人は、当該変更があった日から一月以内に、変更の登記を申請しなければならない。2項＝変更があった後に表題部所有者又は所有権の登記名義人となった者は、その者に係る表題部所有者についての更正の登記又は所有権の登記があった日から一月以内。3項＝変更があった後に共用部分である旨の登記があったときは、所有者（前二項の規定により登記を申請しなければならない者を除く。）は、共用部分である旨の登記がされた日から一月以内。

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

TITLE BANNER: text 「変更の登記の1か月は、人ごとに違う日から数える」 in large bold letters; the part 「人ごとに違う日」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- Two short timelines are stacked in the center region, each a plain horizontal line with a plain dark navy arrow labeled 「時間の流れ」 (this arrow means only the passing of time, not an application or a transaction).
- Upper timeline with a dark navy tag 「工事のときの名義人」: two event cards in order, 「増築の工事が完了」 and then 「共用部分である旨の登記がされる」.
- Lower timeline with a dark navy tag 「工事のあとに名義人になった者」: two event cards in order, 「改築の工事が完了」 and then 「その者の所有権の登記がされる」.
- A small question badge 「1か月は、どこから数える？」 sits above the two timelines (a question badge only, with no check mark and no cross).
- The two first event cards have clearly different texts (増築 and 改築); the texts are NOT identical.
- 藍子 bubble (left, spoken first): 「どの人も、工事が
終わった日からですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
人によって
違うのよ」 with the part 「人によって違う」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　主語の人で、数える日が決まる」
- A full-width explanation panel fills the whole panel, with a small dark navy tag 「先に読む」 at the top left and a line beside it: 「誰の1か月か」.
- Two wide white cards stacked top and bottom, each with a dark navy outline and no arrow between them. The upper card has the heading 「工事のときの名義人（法51条1項）」 and the body 「工事が完了した日から1か月」. The lower card has the heading 「工事のあとに名義人になった者（法51条2項）」 and the body 「その者の所有権の登記があった日から1か月」.
- At the bottom, one wide dark navy band with white text: 「共用部分の登記の日から数えるのは、1項・2項の人を除く所有者（法51条3項）」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、その日は使えない？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two large cards stacked top and bottom, both exactly the same size, each with a pale gray fill and a dark navy outline, with its dark navy heading placed fully INSIDE the card, and with no arrow, no connector, no check mark, and no cross. They are separated only by a small empty gap.
- Upper card, heading 「工事のときの名義人に、共用部分の登記の日は使えない」, two body lines: 「義務は消えず、起算点も工事完了の日のまま」 and 「3項のかっこ書が、1項の人を除いている」.
- Lower card, heading 「買った人に、工事完了の日は使えない」, two body lines: 「変更のあとに所有権を取得した者は、2項」 and 「自分の所有権の登記があった日から」.
- A dark navy ribbon tag with large white text under the two cards: 「分かれ目：主語は誰か」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「共用部分の登記の
日からでは？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「それが罠よ。
3項は1項の人を
除くの」 with the part 「3項は1項の人を除く」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「では、買った人は
どうなりますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「2項で、自分の
登記の日から
数えるのよ」 with the part 「自分の登記の日」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は両方×」
- 藍子 bubble (left, spoken first): 「数え始めは、
人ごとに違うんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
主語を見てから
日を選ぶのよ」 with the part 「主語を見てから」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「工事のときの名義人は、工事が完了した日から（法51条1項）」, 「あとに名義人になった者は、自分の所有権の登記の日から（法51条2項）」, 「共用部分の登記の日は、3項の所有者の日（1項・2項の人は除く）」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「1か月は、主語の人を見てから起算点を選ぶ」 with a yellow highlighter marker.
- Line 2: 「問題D0686・D0772　どちらも×（誤った記述）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 所, 権, 登, 記, 買, 違, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ4_1か月は人ごとに違う日から.png`
- 途中の版・不採用の版：`4コマ4_1か月は人ごとに違う日から_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0686-D0772_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で『増築当時の人は共用部分の登記があり、別の建物では改築のあとに買った人がいる。1か月はどこから数える？』、コマ2で『工事のときの名義人は工事完了の日（1項）、あとに名義人になった者は自分の所有権の登記の日（2項）、共用部分の登記の日は1項・2項の人を除く所有者（3項）』、コマ3で『共用部分の登記の日が使えないのは3項が1項の人を除くから、工事完了の日が使えないのは買った人は2項だから』が言える
- [ ] 工程C：肝の確認：①1項＝工事が完了した日 ②2項＝自分の所有権の登記があった日 ③3項かっこ書＝1項・2項の人を除く ④どちらの肢も、主語と日が合っていないので×
- [ ] 工程C：構成表の全文言を記事・法令DBの第51条と突き合わせ：『変更があった日』『その者に係る所有権の登記があった日』『共用部分である旨の登記がされた日』『前二項の規定により登記を申請しなければならない者を除く』。4項・過料・区分建物の特例は入れていない
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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ 第51条第1項 用。起算点の取り違えを問う2肢を1本にまとめた）
- 2026-10-11 v02：最新の作成ルールで作り直し。コマ2を主語ごとの起算点の対応に、コマ3を『なぜ共用部分の登記の日・工事完了の日が使えないか』の理由のカード（印なし）に変え、コマ2とコマ3の重複を解消した。コマ1は通常サイズのキャラ（side）のまま
