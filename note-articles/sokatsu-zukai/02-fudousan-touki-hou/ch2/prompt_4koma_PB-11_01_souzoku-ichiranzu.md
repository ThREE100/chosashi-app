# D1897・D1898 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 総合記事②「直前期の苦手論点つぶし 不動産登記法編」第2章（`note-articles/column/sokatsu-02-fudousan-touki-hou-ch2.md`）の、論点【PB-11】に差し込む4コマのプロンプトです。単独のnote記事にする場合の節（記事タイトル・冒頭文・見出し画像）は外してあり、生成元は `src/spec_4koma_PB-11_01.py` です。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`）に従い、生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-13）。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D1897・D1898（不動産登記法／申請総論（申請情報・添付情報・代理・却下取下・還付・電子申請・登記識別情報）、出典 R05-Q19ア／R05-Q19イ）。正解＝D1897＝×（誤った記述）／D1898＝〇（正しい記述）。
- 記事：`note-articles/r5-mondai/q19-houtei-souzoku.md` ア（R05：資格者代理人が申し出るには、委任状に加えて資格を示す身分証明書の写しなどを提供する。規則247条2項2号・3項7号）・イ（申出人の住所地を管轄する登記所にも申出ができる。規則247条1項）。ほか、同章の記事（sokatsu-02-fudousan-touki-hou-ch2.md 【PB-11】）の整理
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】D1897は『委任を受けた土地家屋調査士が』『代理人の権限を証する書面として、委任状以外の書面を添付する必要はない』と、資格者なら委任状だけで足りるように見せる。D1898は正しい記述だが、申出先を被相続人の本籍地などに限ると思い込んでいると、『申出人の住所地を管轄する登記所』を誤りに感じさせる。
- 【受験者の勘違い・定着していない点】（推測）①申出先は、被相続人の本籍地・最後の住所地・不動産の所在地といった被相続人の側だけと考え、申出人の住所地も選べることを見落とす（規則247条1項は4つを並べる）。②土地家屋調査士は有資格者だから、委任状だけで足りると軽く考え、代理人が親族以外なら資格を示す書面も提供することを見落とす。
- 【対比する制度】「本人が申し出る」⇔「調査士が代理して申し出る」：本人の申出には代理人がいないので、代理人の権限を証する書面は要らない／調査士が代理して申し出るなら、委任状（代理人の権限を証する書面）に加えて、資格を示す書面（身分証明書の写しなど）も提供する（提供する書面が増える点）。
- 【型の選び方】型：型4（複数肢の対比。コマ1は比較表）。理由：2肢は場面が別々（調査士の代理の申出、申出人の住所地の登記所）で、共通の日付がなく、一方が×、他方が〇。読者は、どの場面でどの書面や登記所が問われるのかを自分で並べ直せない。コマ1＝2肢の比較表（肢／場面／肢の言い分）、コマ2＝本人の申出と調査士の代理の申出の左右のカード、コマ3＝2肢の言い分を正しい整理に直す理由のカード（申出先は4つのどれでもよい・調査士の代理は委任状だけでは足りない）、コマ4＝×と〇の整理。壁＝『申出先は被相続人の側だけ』『有資格者なら委任状だけで足りる』という思い込み。
- コマごとに読者が言えること：コマ1＝2肢は、調査士が代理して写しの交付を申し出る場合と、申出先を問う。コマ2＝調査士が代理して申し出るなら、委任状だけでは足りず、資格を示す書面も提供する。コマ3＝申出先は4つのどれでもよく、申出人の住所地も選べる。コマ4＝D1897は×、D1898は〇。
- 記事の範囲：R05-Q19ア・イ（記事 r5-mondai/q19-houtei-souzoku.md）と、同章の記事【PB-11】の整理。保管の期間と再交付（D2087）、住所入りの写しの兼用（D1487）は、図解16と別の肢なので入れない。保存期間は同章のPB-12の4コマと重ねない。
- extra_refs：不動産登記規則247条1項（申出先：被相続人の本籍地若しくは最後の住所地、申出人の住所地又は被相続人を表題部所有者若しくは所有権の登記名義人とする不動産の所在地を管轄する登記所）、同条2項2号（代理人は、申出人の法定代理人又はその委任による代理人にあってはその親族若しくは戸籍法第十条の二第三項に掲げる者に限る）、同条3項7号（代理人によって申出をするときは、当該代理人の権限を証する書面）は、法令DB note-articles/laws/fudousan-touki-kisoku-2.md で原文を確認した。資格を示す身分証明書の写しの提供は、条文に明記がなく、先例に基づく取扱いなので、図では『実務の取扱い』と添えた。戸籍法第10条の2第3項は法令DBにないため、記事の記述（弁護士・司法書士・土地家屋調査士・税理士など）に従った。
- 登場人物：人型は使わず、申出先・書類は文字のカードで示す。
- 矢印の意味：矢印は使わない。コマ1は表、コマ2は左右のカード、コマ3は縦のカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、帯・リボンは濃紺（白文字）、強調は黄色マーカーだけ。
- コマの使い方（キャラは不必要に小さくしない）：コマ1＝small（表が横いっぱいに要るので、キャラは小さく。約150px）、コマ2＝none（図が主役）、コマ3＝faces（左に理由のカード2枚、右に会話4つの縦並び）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 一覧図の申出は、申出先を選べる | 「申出先を」を黄色マーカー |
| コマ1 見出し | ラベル | ①　2つの肢は、申出の場面を問う | — |
| コマ1 図 | 図・カード | 肢 / 場面 / 肢の言い分 / 肢D1897 / 土地家屋調査士が代理して、写しの交付を申し出る / 委任状以外の書面は、添付する必要はない / 肢D1898 / 法定相続情報一覧図の保管を申し出る / 申出人の住所地を管轄する登記所にできる | — |
| コマ1 | 藍子（左・先に話す） | 申出先は、被相続人の側だけですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。選べる先は、もっと広いのよ | 「もっと広い」 |
| コマ2 見出し | ラベル | ②　本人の申出と、調査士の代理の申出 | — |
| コマ2 図 | 図・カード | 規則247条 / 代理人が付くと、提供する書面が増える / 本人が申し出る / 代理人がいない / 代理人がいないので、 / 代理人の権限を証する書面は要らない / 調査士が代理して申し出る / 肢D1897は、こちらの場面 / 委任状（代理人の権限を証する書面）を提供 / 資格を示す書面も提供（実務の取扱い） / 調査士の代理は、委任状だけでは足りない | — |
| コマ3 見出し | ラベル | ③　2つの言い分を、直す | — |
| コマ3 図 | 図・カード | 申出先は、被相続人の側だけ？ / 被相続人の本籍地、最後の住所地 / 申出人の住所地、被相続人名義の不動産の所在地 / （4つのどれでもよい） / 肢D1898の言い分 / ひっかけ：委任状だけで足りる / 調査士なら、委任状だけで足りる？ / 委任状に加えて、 / 資格を示す書面も提供する / 肢D1897の言い分 | — |
| コマ3 | 藍子（左・1番目） | 申出人の住所地でも、いいんですか？ | — |
| コマ3 | トリ先生（右・2番目） | ええ。4つのどれでもいいのよ | 「4つのどれでも」 |
| コマ3 | 藍子（左・3番目） | 調査士なら、委任状だけで足りますか？ | — |
| コマ3 | トリ先生（右・4番目） | 足りないわ。資格を示す書面も要るの | 「足りない」 |
| コマ4 見出し | ラベル | ④　結論は×と〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 申出先は選べて、代理は書面が増えるんですね！ | — |
| コマ4 | トリ先生（右・答える） | そう。選べる先と書面を、分けて覚えてね | 「分けて」 |
| コマ4 チェック欄 | 3項目（青✓） | 申出先は、被相続人の本籍地・最後の住所地、申出人の住所地、不動産の所在地のどれでもよい（肢D1898は〇） / 調査士が代理するなら、委任状に加えて資格を示す書面も提供する（肢D1897は×） / 委任による代理人は、親族か戸籍法10条の2第3項に掲げる者に限る | — |
| 結論帯 | 1行目 | 一覧図の申出先は選べ、調査士の代理は委任状だけでは足りない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1897・D1898　正解×・〇（R05-Q19ア／R05-Q19イ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記規則247条1項（申出先）・2項2号（代理人）・3項7号（代理人の権限を証する書面）。法令DB note-articles/laws/fudousan-touki-kisoku-2.md と照合済み。資格を示す書面の提供は条文に明記がなく、実務の取扱い（先例）

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

TITLE BANNER: text 「一覧図の申出は、申出先を選べる」 in large bold letters; the part 「申出先を」 has a yellow highlighter marker.

PANEL 1 (curious, puzzled mood; both characters appear SMALLER than in the other panels, only because this panel's diagram or text needs the room (each about 150 px tall; never below 110 px and never more than one third of the panel height; use the largest size in this range that still lets the diagram fill the panel), 藍子 at the lower left corner and トリ先生 at the lower right corner; 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　2つの肢は、申出の場面を問う」
- A wide table that fills the full panel width. The header row is dark navy with white text and has three columns: 「肢」, 「場面」, 「肢の言い分」. The two body rows have the same pale gray fill and a dark navy outline, each text at least 22 px high, with no check mark, no cross, and no arrow.
- Body row 1: 「肢D1897」, 「土地家屋調査士が代理して、写しの交付を申し出る」, 「委任状以外の書面は、添付する必要はない」.
- Body row 2: 「肢D1898」, 「法定相続情報一覧図の保管を申し出る」, 「申出人の住所地を管轄する登記所にできる」.
- The two rows have clearly different texts; the texts are NOT identical, so copy each character exactly as given.
- 藍子 bubble (left, spoken first): 「申出先は、
被相続人の側だけ
ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
選べる先は、
もっと広いのよ」 with the part 「もっと広い」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　本人の申出と、調査士の代理の申出」
- A small dark navy tag 「規則247条」 at the top left, with one line beside it: 「代理人が付くと、提供する書面が増える」.
- Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.
- Left card, heading 「本人が申し出る」, a small tag 「代理人がいない」, two body lines: 「代理人がいないので、」, 「代理人の権限を証する書面は要らない」.
- Right card, heading 「調査士が代理して申し出る」, a small tag 「肢D1897は、こちらの場面」, two body lines: 「委任状（代理人の権限を証する書面）を提供」, 「資格を示す書面も提供（実務の取扱い）」.
- Under the two cards, one wide dark navy band with large white text 「調査士の代理は、委任状だけでは足りない」.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　2つの言い分を、直す」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Two cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill, a dark navy outline, and a dark navy heading placed INSIDE the card, with no check mark and no cross. The cards are separated only by a small empty gap, with nothing drawn between them.
- Card 1, heading 「申出先は、被相続人の側だけ？」, three body lines 「被相続人の本籍地、最後の住所地」, 「申出人の住所地、被相続人名義の不動産の所在地」, 「（4つのどれでもよい）」, and at the bottom a small tag 「肢D1898の言い分」.
- Card 2, a dark navy ribbon tag with large white text 「ひっかけ：委任状だけで足りる」, heading 「調査士なら、委任状だけで足りる？」, two body lines 「委任状に加えて、」 and 「資格を示す書面も提供する」, and at the bottom a small tag 「肢D1897の言い分」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「申出人の住所地でも、
いいんですか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「ええ。
4つのどれでも
いいのよ」 with the part 「4つのどれでも」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「調査士なら、
委任状だけで
足りますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「足りないわ。
資格を示す書面も
要るの」 with the part 「足りない」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は×と〇」
- 藍子 bubble (left, spoken first): 「申出先は選べて、
代理は書面が
増えるんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。
選べる先と書面を、
分けて覚えてね」 with the part 「分けて」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「申出先は、被相続人の本籍地・最後の住所地、申出人の住所地、不動産の所在地のどれでもよい（肢D1898は〇）」, 「調査士が代理するなら、委任状に加えて資格を示す書面も提供する（肢D1897は×）」, 「委任による代理人は、親族か戸籍法10条の2第3項に掲げる者に限る」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「一覧図の申出先は選べ、調査士の代理は委任状だけでは足りない」 with a yellow highlighter marker.
- Line 2: 「問題D1897・D1898　正解×・〇（R05-Q19ア／R05-Q19イ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 保, 地, 所, 権, 登, 肢, 規, 解, 記, 証 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the smaller characters are drawn within the specified size range (they must not grow and squeeze the diagram, and must not be shrunk below the range) and that nothing but the given text appears above the heads of the pictograms; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that the conclusion banner is pale yellow with dark navy text; confirm that panel 1, panel 2 and panel 3 contain no check mark and no cross anywhere, and that the only blue check marks in the whole image are the three in the checklist of panel 4; confirm that the two rows of the table in panel 1 are in the order 肢D1897, 肢D1898, never swapped; confirm that the left card of panel 2 has the heading 「本人が申し出る」 and the right card has the heading 「調査士が代理して申し出る」, never swapped; confirm that card 1 of panel 3 is the one tagged 「肢D1898の言い分」 and card 2 is the one tagged 「肢D1897の言い分」, never swapped confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`不動産登記法編2章_4コマ9_一覧図の申出は、申出先を選べる.png`
- 途中の版・不採用の版：`不動産登記法編2章_4コマ9_一覧図の申出は、申出先を選べる_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py note-articles/sokatsu-zukai/02-fudousan-touki-hou/ch2/prompt_4koma_PB-11_01_souzoku-ichiranzu.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1で2肢の場面と言い分、コマ2で本人の申出と調査士の代理の申出で提供する書面が違うこと、コマ3で申出先が4つのどれでもよいことが言える
- [ ] 工程C：構成表の全文言を記事（R05-Q19ア・イ）・法令DB（不動産登記規則247条1項・2項2号・3項7号）と突き合わせ済み。資格を示す書面は『実務の取扱い』と添えた
- [ ] 工程C：コマ1〜3に印がなく、コマ4だけ青✓。コマの使い方は small→none→faces→既定 で隣り合うコマが同じにならない
- [ ] 工程C：肝の確認：①申出先は、被相続人の本籍地・最後の住所地、申出人の住所地、被相続人名義の不動産の所在地のどれでもよい（規則247条1項） ②代理人にできるのは、法定代理人か、親族または戸籍法10条の2第3項に掲げる者（同条2項2号） ③調査士が代理するなら、委任状に加えて資格を示す書面も提供する（実務の取扱い） ④D1897は×、D1898は〇

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

## 改訂履歴（このファイルは `src/spec_4koma_PB-11_01.py` から `src/build_4koma.py` で生成。直すときは設計データを直して再生成する）

- 2026-10-13 v01：新規作成（総合記事②不動産登記法編 第2章【PB-11】用。型4（複数肢の対比。コマ1は比較表）。本人の申出と調査士の代理の申出の対比と、申出先は4つのどれでもよいことに絞った）
