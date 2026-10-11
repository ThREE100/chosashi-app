# D0600・D0957 4コマ解説図解 プロンプト（ChatGPT貼付用・v02）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、不動産登記法 第40条の記事に差し込む4コマ（3本目）のプロンプトです。類似の誤解をまとめて、1本の4コマにしました。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（`tools/drill/manga/`（mainブランチ））に従い、同フォルダの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-09）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。

- 肢：D0600・D0957（不動産登記法／土地の分筆・合筆・地積更正、出典 H22-Q18オ／H26-Q10ア）。正解＝D0600＝×（誤った記述）／D0957＝〇。
- 記事：`note-articles/h22-mondai/q18-bunpitsu.md` オ「分筆手続の中で、もとの土地に『抵当権が消滅した旨の記録』はされない」。ほか、H26-Q10ア（q10-bunpitsu.md）
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【型の選び方】型：型4（複数肢の対比）＋型3（理由説明）。理由：壁は、同じ抵当権の分筆でも『どの土地について消す承諾か』で記録の書かれ方が逆になること（コマ2の左右のカード）と、両方の土地を消す承諾はなぜ成り立たないのか（コマ3で、条文の言い方が『いずれかの土地』であることを理由に示す）。2肢（D0600・D0957）の分かれ目が、承諾に係る土地が甲か、乙か、両方かの1点に集まるので、コマ2で2つの条文の効果を並べ、コマ3で両方の扱いを示した。
- 【出題者のひっかけ】D0600は『分筆後の甲土地及び乙土地の2筆の土地について抵当権者が抵当権の消滅を承諾した』と書き、そのうえで『甲土地には消滅した旨の記録、乙土地には転写されない』と結果を並べる。D0957は『分筆後の甲土地について消滅を承諾』と書く。どの土地について承諾したかの言い回し一つで、記録の書かれ方が変わる（記事 H22-Q18オ、H26-Q10ア）。
- 【受験者の勘違い・定着していない点】①承諾した土地が乙でも甲でも、同じ処理（もとの土地に消滅の記録、新しい土地には転写しない）だと思う。②両方の土地について消す承諾もできて、その場合も一方に記録して他方に転写しない、と考える。実際は、法40条は分筆後の『いずれかの土地』について消す承諾を定めていて、乙土地について消えるときは乙に転写せず甲に付記、甲土地について消えるときは甲に付記と抹消の記号で乙に転写される（規則104条2項・3項）。両方を消す承諾の処理を定めた規定はない（記事 H22-Q18オ）。
- 【対比する制度】「乙土地について消える」⇔「分筆後の甲土地について消える」：前者は乙土地に転写せず、甲土地の記録に付記登記で記録する（規則104条2項）／後者は甲土地の記録に付記登記と抹消の記号を記録し、乙土地には転写される（規則104条3項）。結論が逆になる点。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。土地は『甲土地』『乙土地』の文字タグで示す。
- 矢印の意味：矢印は使わない。コマ1は2筆に分ける図、コマ2は左右の別カード、コマ3は上下の別カード。
- 会話順：藍子の誤解（どの土地でも同じ処理）→トリ先生の訂正（承諾に係る土地を見る）→両方もできるかの質問→条文はいずれかの土地→甲で消すと乙は→乙に転写される。
- 配色：コマ1・2・3は印（✓✕）を付けない（コマ3は理由のカードで、説明であり正誤の対比ではない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- 記事の範囲：法40条（承諾に係る土地について消滅した旨を登記）／規則104条2項・3項（記録の方法。記事 H22-Q18オ）／甲土地について消滅し乙土地に転写される（記事 H26-Q10ア）。『両方の土地について消滅を承諾する処理を定めた規定はない』は、記事 H22-Q18オ が『両方の土地について承諾した場合の扱いを直接定めた条文は法令データベースでは確認できず、法40条の文言からの整理』と書いている範囲に限り、図にも『法40条の文言からの整理』と書く。
- コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央に2筆に分ける図と疑問バッジ。図の量が少ないので小さくする必要がない）、コマ2＝none（図が主役。左右のカードと帯）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 権利の消滅は、承諾に係る土地についてだけ登記する | 「承諾に係る土地」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの事案 | — |
| コマ1 図 | 図・カード | 甲土地（抵当権の登記がある） / 分筆後の甲土地 / 乙土地 / 抵当権者が、分筆後の甲土地について消すことを承諾 / 甲土地と乙土地の記録は、どうなる？ | — |
| コマ1 | 藍子（左・先に話す） | どの土地でも、同じ処理ですよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。承諾した土地を見なさい | 「承諾した土地」 |
| コマ2 見出し | ラベル | ②　出題者のねらい | — |
| コマ2 図 | 図・カード | 出題者のねらい / 消える土地によって、記録の書き方が変わる / 乙土地について消える / 乙土地には転写しない。甲土地の記録に、付記登記で乙土地について消滅と記録（規則104条2項） / 分筆後の甲土地について消える / 甲土地の記録に、付記登記で消滅と抹消の記号（規則104条3項）。乙土地には転写される | — |
| コマ3 見出し | ラベル | ③　なぜ、両方ではだめ？ | — |
| コマ3 図 | 図・カード | 法40条が定めるのは / 分筆後のいずれかの土地について / 消す承諾 / 両方の土地について消す承諾は / 定めた規定がない / （法40条の文言からの整理） / ひっかけ：2筆の土地について、と書いてある / たとえば / 乙だけ消す承諾なら、乙について消滅と登記 / 甲と乙の両方を消すのは、想定外 | — |
| コマ3 | 藍子（左・1番目） | 甲と乙の両方を消すこともできますか？ | — |
| コマ3 | トリ先生（右・2番目） | 条文は、いずれかの土地についてよ | 「いずれかの土地」 |
| コマ3 | 藍子（左・3番目） | 甲で消すと、乙はどうなりますか？ | — |
| コマ3 | トリ先生（右・4番目） | 乙には、抵当権が転写されるわ | 「転写される」 |
| コマ4 見出し | ラベル | ④　結論は承諾に係る土地 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 消える土地で、書き方が違うんですね！ | — |
| コマ4 | トリ先生（右・答える） | そのとおり。承諾に係る土地を見るのよ | 「承諾に係る土地」 |
| コマ4 チェック欄 | 3項目（青✓） | 消す承諾は、分筆後のいずれかの土地について（法40条） / 乙で消える：乙に転写せず、甲に付記登記（規則104条2項） / 甲で消える：甲に付記と抹消の記号（規則104条3項）、乙に転写 | — |
| 結論帯 | 1行目 | 消滅は、承諾に係る土地についてだけ登記する | 黄色マーカー |
| 結論帯 | 2行目 | 問題D0600・D0957　D0600＝×、D0957＝〇 | — |

## 記事に無い条文（ユーザー指示で追加）

- 不動産登記法40条・不動産登記規則104条2項・3項（法令DB note-articles/laws/fudousan-touki-hou.md 第40条、fudousan-touki-kisoku-1.md 第104条）で確認：40条＝承諾を証する情報が提供されたときは、承諾に係る土地について権利が消滅した旨を登記しなければならない（権利を『分筆後のいずれかの土地について』消滅させることの承諾）。104条2項＝乙土地について消滅するときは、分筆後の甲土地の登記記録の当該権利に関する登記についてする付記登記で記録し、乙土地には転写することを要しない。104条3項＝分筆後の甲土地について消滅するときは、付記登記で記録し、当該権利に関する登記を抹消する記号を記録する
- 規則102条1項（法令DB fudousan-touki-kisoku-1.md）：分筆のとき、乙土地の登記記録に甲土地の権利に関する登記を転写する。『甲土地について消えるときは乙土地に転写される』（記事 H26-Q10ア）の根拠。図では104条3項と併記せず、転写は記事の言い方（転写される）だけにした
- コマ3の『両方の土地について消す承諾は、定めた規定がない』：記事 H22-Q18オ が『両方の土地について承諾した場合の扱いを直接定めた条文は法令データベースでは確認できず、法40条の文言からの整理』と書く範囲。図にも『法40条の文言からの整理』と添えた

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

TITLE BANNER: text 「権利の消滅は、承諾に係る土地についてだけ登記する」 in large bold letters; the part 「承諾に係る土地」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel; do NOT make them smaller than this just to leave empty space, and reduce them by at most about 15% only if the speech bubbles or the diagram would otherwise not fit (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの事案」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A diagram is drawn large in the center region: a plot labeled 「甲土地（抵当権の登記がある）」 is divided into two plots side by side, with dark navy tags 「分筆後の甲土地」 and 「乙土地」.
- A white note card under the plots reads 「抵当権者が、分筆後の甲土地について消すことを承諾」.
- A small question badge 「甲土地と乙土地の記録は、どうなる？」 sits above the plots (a question badge only, with no check mark and no cross).
- 藍子 bubble (left, spoken first): 「どの土地でも、
同じ処理ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
承諾した土地を
見なさい」 with the part 「承諾した土地」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　出題者のねらい」
- A full-width explanation panel fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「消える土地によって、記録の書き方が変わる」.
- Two large white cards side by side with dark navy outlines (no arrows and no connectors). Left card, heading 「乙土地について消える」, body 「乙土地には転写しない。甲土地の記録に、付記登記で乙土地について消滅と記録（規則104条2項）」. Right card, heading 「分筆後の甲土地について消える」, body 「甲土地の記録に、付記登記で消滅と抹消の記号（規則104条3項）。乙土地には転写される」.
- There is no check mark and no cross anywhere in this panel.
- The two cards have clearly different texts; the texts are NOT identical.

PANEL 3 (surprised then convinced mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　なぜ、両方ではだめ？」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.
- Card 1, heading 「法40条が定めるのは」, body 「分筆後のいずれかの土地について」 and 「消す承諾」.
- Card 2, heading 「両方の土地について消す承諾は」, body 「定めた規定がない」 and 「（法40条の文言からの整理）」, and a dark navy ribbon tag with large white text 「ひっかけ：2筆の土地について、と書いてある」.
- Card 3, heading 「たとえば」, body 「乙だけ消す承諾なら、乙について消滅と登記」 and 「甲と乙の両方を消すのは、想定外」.
- There is no check mark and no cross anywhere in this panel.
- The three cards have clearly different texts; the texts are NOT identical.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「甲と乙の両方を
消すこともできますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「条文は、いずれかの
土地についてよ」 with the part 「いずれかの土地」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「甲で消すと、
乙はどうなりますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「乙には、抵当権が
転写されるわ」 with the part 「転写される」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (relieved and convinced mood; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は承諾に係る土地」
- 藍子 bubble (left, spoken first): 「消える土地で、
書き方が違うんですね！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そのとおり。
承諾に係る土地を
見るのよ」 with the part 「承諾に係る土地」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「消す承諾は、分筆後のいずれかの土地について（法40条）」, 「乙で消える：乙に転写せず、甲に付記登記（規則104条2項）」, 「甲で消える：甲に付記と抹消の記号（規則104条3項）、乙に転写」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「消滅は、承諾に係る土地についてだけ登記する」 with a yellow highlighter marker.
- Line 2: 「問題D0600・D0957　D0600＝×、D0957＝〇」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames; cartoon expression marks such as ！ and ？ beside the characters' faces are allowed and are not extra text); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two smaller characters are drawn as specified, and that no character is smaller than its PANEL line specifies and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 号, 地, 当, 承, 抵, 権, 登, 規, 記, 諾, 違, 録 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard. This list is only a guide for drawing: apply it silently while drawing, never audit the finished image against it, never announce a defect, and never delete, redo, or regenerate anything afterwards; deliver the first image as it is.
```

## 保存名

- 4コマ（採用版）：`4コマ3_消滅は承諾に係る土地だけ.png`
- 途中の版・不採用の版：`4コマ3_消滅は承諾に係る土地だけ_v01.png`

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D0600-D0957_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：コマ1の甲・乙の2筆（甲で消す承諾）と、コマ2の左右のカード（乙で消滅／甲で消滅）、コマ3の『いずれかの土地』と『両方は定めがない』が対応している
- [ ] 工程C：肝の確認：コマ2に規則104条2項・3項の記録の違い、コマ3に『両方の土地について』という言い回しが条文の『いずれかの土地』と違う点、コマ4の暗記3点に付記登記と抹消の記号が入っている。D0600＝×、D0957＝〇
- [ ] 工程C：出典の確認：法40条・規則104条2項・3項は法令DB（fudousan-touki-hou.md・fudousan-touki-kisoku-1.md）で確認済み。『両方の土地』の整理は記事の言い方にそろえ、『法40条の文言からの整理』と図にも書いた（条文に直接の規定がない）
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

- 2026-10-09 v01：初版（条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の第40条用。消滅の記録の書き方を問う2肢を1本にまとめた。ChatGPTでの生成・検品はまだ）
- 2026-10-11 v02：最新ルールで作り直し。コマ3を『勘違い／正しい整理』の左右カードから、『法40条の言い方はいずれかの土地』を理由とする上下3枚のカード（印なし）に変え、『両方は定めがない（法40条の文言からの整理）』を図に明記した。コマ4のチェック欄を短くし、転写の記述を規則104条3項の括弧の外に出した。コマ1のキャラは通常サイズ（side）
