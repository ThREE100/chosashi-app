# D1712 4コマ解説図解 プロンプト（ChatGPT貼付用・v01）

> **このファイルについて**
>
> - 条文別『苦手克服』シリーズ（`note-articles/joubun-nigate/`）の、土地家屋調査士法 第22条・第41条第1項（依頼に応ずる義務と法人への準用）を主役にした4コマ（1本目）のプロンプトです。条文の中身が1枚で言えるように組み、構成表（文言の正本）を含みます。関連する肢（D1712）は、条文のどこで誤りやすいかを示す材料として使っています。
> - 構成・体裁は、4コマ解説図解のルール `MANGA_RULES.md`（ブランチ `claude/kind-bell-y3f106` の `tools/drill/manga/`）に従い、同ブランチの生成器 `gen_prompts.py` と機械チェック `check_prompt.py` で作りました（`check_prompt.py` は NG 0件・WARN 0件。2026-10-10）。下の「作成時の品質ゲート」にある `tools/drill/manga/` のパスは、そのブランチ上のパスです。設計データは `src/spec_4koma_01.py` にあります。
> - 画像は生成していません（ChatGPTでの生成・検品はまだ）。生成後は、下の「生成後の照合チェック」で検品してください。


- 肢：D1712（土地家屋調査士法／調査士会・資格・その他、出典 R03-Q20オ）。正解＝〇（正しい記述）。誤解しやすい点は、依頼応諾義務（法22条）が法41条1項で調査士法人にも準用されること。
- 記事：`note-articles/r3-mondai/q20-chousashihou.md` R03-Q20オ（調査士法人も、正当な事由がなければ登記代理の依頼を拒めない。依頼応諾義務の法22条を法41条1項が準用）を、法22条の本則・かっこ書・法41条1項の準用という条文の構造から整理する
- ルール：`MANGA_RULES.md`（品質ゲート 工程A〜D）
- 使い方：ChatGPTに **キャラ仕様書の参照画像（`CHATGPT_MANGA_WORKFLOW.md` §3の6枚。トリ先生・藍子の基準画像）** を添付し、どちらがトリ先生でどちらが藍子かを貼り付けの冒頭に一言添えて、下のコードブロックを貼る。サイズは 1080×1920（9:16）。

## 設計メモ（工程A）
- 【出題者のひっかけ】主語を『土地家屋調査士法人』に入れ替える。法22条の条文の主語は『調査士は』だけなので、法人には及ばないように見せる。さらに『正当な事由がある場合でなければ…拒むことはできない』という二重否定の言い回しで、〇か×かを迷わせる。肢の業務は『不動産の表示に関する登記の申請手続の代理』で、法22条のかっこ書で除かれる業務ではない（除かれる側に入れて読ませるのも罠）。
- 【受験者の勘違い・定着していない点】①『依頼応諾義務は調査士個人の義務で、会社のような法人は自由に断れる』と考える。②法22条の主語が『調査士は』なので、条文の側から法人に及ぶ道筋（法41条1項の準用）が見えない。③『拒むことはできない』の強い言い切りと二重否定に引かれて、×と判断する。④かっこ書で除かれる筆界特定の代理・相談と、除かれない登記の代理を混ぜて覚えている。
- 【対比する制度】「かっこ書の外」⇔「かっこ書で除かれる依頼」：かっこ書の外（登記の申請手続の代理など）は、正当な事由がある場合でなければ拒んではならない（法22条の本則）。かっこ書で除かれる依頼（筆界特定の代理・相談など）は、法22条の義務が及ばず拒める（ただし承諾しないときは、速やかに依頼者へ通知。規則25条2項）。同じ法22条の中で結論が逆になる。調査士（個人）と調査士法人の間は、法41条1項の準用により結論は同じ。
- 【型の選び方】型：型3（なぜそうなるかを条文の構造で示す。型2のしくみ図と読み方3ステップを混ぜる）。理由…先に作った肢中心の版は『法人にも及ぶ理由』が中心だったので、今回は法22条の本則・かっこ書・法41条1項の準用が、条文の側から1枚（コマ2）で言えるようにし、コマ3で受験者のひっかかりを『主語→かっこ書への当てはめ→二重否定』の順に当てはめる。壁（初見の読者が引っかかる点）＝『法22条は調査士は、としか書いていないのに、なぜ法人にも及ぶのか。かっこ書の外とは何か』。
- 記事の範囲：R03-Q20オ（法22条、法41条1項の準用、たとえば〔法人が『なんとなく気が進まない』で断れない／手が回らないなど正当な事由があれば断れる〕）。かっこ書で除かれる筆界特定の代理・相談との対比と規則25条2項は、同じ問のエ（兄弟肢D1711）の記事の整理による。民間紛争解決手続代理関係業務がかっこ書で除かれる点は、法22条の原文による（記事にない整理。extra_refs）。
- extra_refs：上の extra_refs に法令DBのファイル・条番号を記載した。図に入れた条番号は、法22条・法41条1項・法3条1項2号・規則25条2項のみ。英字の略称は図に入れない。罰則（法70条）と規則25条1項は図に入れていない。
- 先に作った肢中心の版（tools/drill/manga/D1712_prompt.md）との関係：主張は同じ（法人も拒めない・根拠は法41条1項の準用・筆界特定の代理・相談は拒める・通知は規則25条2項）。今回は、かっこ書の中身（筆界特定の代理・相談、民間紛争解決手続代理関係業務）と、法22条→かっこ書→法41条1項の並びを増やした。
- 登場人物：当事者の記号（Ａ〜Ｚ）は使わない。依頼者と調査士法人を、人型タグと建物のアイコン（文字ラベルつき）でコマ1に出す。
- 矢印の意味：矢印は使わない。コマ1は依頼者と調査士法人を細い線で結ぶ図、コマ2は積み重ねたカード（条文→かっこ書→準用）、コマ3は3枚のステップカード。
- 配色：コマ1〜3は印（✓✕）を付けない。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。
- コマの使い方：コマ1＝side（キャラは通常サイズで左右の端、図は中央）、コマ2＝none（条文の構造図）、コマ3＝faces（左に3ステップ、右に会話の縦並び。会話4つ＝顔4つ）、コマ4＝既定（暗記3点と結論）。

## 記事タイトル

【土地家屋調査士受験生向け】4コマ解説図解D1712～R03-Q20オ～

## note記事の冒頭文

土地家屋調査士法人が、不動産の表示に関する登記の申請手続の代理を頼まれました。法人は、正当な事由がなくても、この依頼を断ってよいのでしょうか。

択一式で間違えやすいこの論点を、トリ先生と藍子の4コマで確認します（令和3年度　第20問　オ）。

先に〇か×かを考えてから、読み進めてみてください。

## 構成表（文言の正本）

| 領域 | 話者・用途 | 正確な文言 | 強調 |
|---|---|---|---|
| タイトル帯 | — | 調査士法人も、正当な事由なく依頼は拒めない | 「正当な事由なく依頼は拒めない」を黄色マーカー |
| コマ1 見出し | ラベル | ①　問いの場面 | — |
| コマ1 図 | 図・カード | 法人は、正当な事由なく断ってよい？ / 依頼者 / 土地家屋調査士法人 / 代理を依頼 / 不動産の表示に関する登記の申請手続の代理 / 正当な事由がある場合でなければ、拒むことはできない / 肢D1712 | — |
| コマ1 | 藍子（左・先に話す） | 法人なら、自由に断れますよね？ | — |
| コマ1 | トリ先生（右・答える） | 出たわね。条文を読んでいくわよ | 「条文を読んでいく」 |
| コマ2 見出し | ラベル | ②　条文の仕組み | — |
| コマ2 図 | 図・カード | 出題者のねらい / 法人にも、この義務は及ぶか / 法22条　本則 / 正当な事由がある場合でなければ / 依頼を拒んではならない / かっこ書で除かれる依頼 / 筆界特定の代理・相談 / 民間紛争解決手続代理関係業務 / 拒める / 法41条1項　法22条を調査士法人に準用 / 調査士法人 / かっこ書の外の依頼は / 正当な事由がなければ拒めない | — |
| コマ3 見出し | ラベル | ③　本番での読み方3ステップ | — |
| コマ3 図 | 図・カード | ステップ1　主語を見る / ひっかけ：主語が調査士法人 / 法41条1項で、法人も法22条の対象 / ステップ2　かっこ書に当てはめる / 登記の代理（法3条1項2号）は、かっこ書の外 / だから拒めない / ステップ3　二重否定をほどく / 正当な事由がなければ拒めない＝正当な事由があれば断れる | — |
| コマ3 | 藍子（左・1番目） | 法22条は、調査士の規定ですよね？ | — |
| コマ3 | トリ先生（右・2番目） | 法41条1項で、法人にも準用よ | 「法人にも準用」 |
| コマ3 | 藍子（左・3番目） | 登記の代理は、除かれますか？ | — |
| コマ3 | トリ先生（右・4番目） | かっこ書の外。だから拒めないの | 「かっこ書の外」 |
| コマ4 見出し | ラベル | ④　結論は〇 | — |
| コマ4 図 | 図・カード |  | — |
| コマ4 | 藍子（左・先に話す） | 法人も、正当な事由なしには断れない！ | — |
| コマ4 | トリ先生（右・答える） | そう。肢は〇よ。根拠は法41条1項ね | 「法41条1項」 |
| コマ4 チェック欄 | 3項目（青✓） | 法22条：正当な事由がある場合でなければ、依頼を拒んではならない / かっこ書の筆界特定の代理・相談などは除く。承諾しないときは速やかに通知（規則25条2項） / 法41条1項で調査士法人に準用。法人も、登記の代理は拒めない | — |
| 結論帯 | 1行目 | 調査士法人も、正当な事由がなければ依頼を拒めない | 黄色マーカー |
| 結論帯 | 2行目 | 問題D1712　正解〇（R03-Q20オ） | — |

## 記事に無い条文（ユーザー指示で追加）

- 法令DB note-articles/laws/chousashi-hou.md 第22条（本則：正当な事由がある場合でなければ、依頼を拒んではならない。かっこ書：第三条第一項第四号及び第六号〔第四号に関する部分に限る〕に規定する業務並びに民間紛争解決手続代理関係業務に関する依頼を除く）
- 法令DB note-articles/laws/chousashi-hou.md 第3条第1項（第2号＝不動産の表示に関する登記の申請手続又は審査請求の手続の代理、第4号＝筆界特定の手続の代理、第6号＝前各号の事務についての相談〔第4号に関する部分が除外対象〕、第7号・第8号＝民間紛争解決手続代理関係業務）、同条第2項（第7号・第8号を民間紛争解決手続代理関係業務と定義）
- 法令DB note-articles/laws/chousashi-hou.md 第41条第1項（第一条、第二条、第二十条から第二十二条まで及び第二十四条の規定は、調査士法人について準用する）
- 法令DB note-articles/laws/chousashi-hou-sekourule.md 第25条第2項（かっこ書で除かれる業務の依頼を承諾しないときは速やかに依頼者へ通知）、第35条（第十九条から第二十八条までの規定を調査士法人に準用）
- （図に入れなかった確認事項）法令DB chousashi-hou.md 第70条第1項・第2項（22条違反は百万円以下の罰金。調査士法人が41条1項で準用する22条に違反したときは、違反行為をした社員又は使用人が同額の罰金）／同 規則第25条第1項（かっこ書の外の依頼を拒んだ場合に、依頼者の請求があるときは理由書を交付）

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

TITLE BANNER: text 「調査士法人も、正当な事由なく依頼は拒めない」 in large bold letters; the part 「正当な事由なく依頼は拒めない」 has a yellow highlighter marker.

PANEL 1 (curious, calm mood; both characters appear at the NORMAL size (each about 190 px tall, roughly half of the panel height, with the same full-body look as in the other panels): 藍子 at the left edge and トリ先生 at the right edge, both standing in the lower part of the panel (see the LAYOUT lines below); 藍子's hands: one hand holds the clipboard against her chest and the other touches her chin (two hands in total)):
- Label tab: 「①　問いの場面」
- LAYOUT (side characters): 藍子 stands at the left edge and トリ先生 at the right edge at the normal size, each taking only the outer 22% of the panel width, with their speech bubbles in the upper part above their own heads and never covering the diagram. The diagram described in the lines below is drawn large in the CENTER region only, between the two characters (about 56% of the panel width and the full panel height below the label tab); wherever a line below says the diagram fills the panel, it means this center region. The characters never overlap the diagram.
- A compact diagram in the center third of the panel, from top to bottom, all parts with the same pale gray fill and a dark navy outline, and with no check mark, no cross, and no arrow.
- Top: a small question badge 「法人は、正当な事由なく断ってよい？」 (a question badge only).
- Middle: on the left a simple faceless person pictogram in pale gray-blue with the dark navy tag 「依頼者」, on the right a simple building icon with the dark navy tag 「土地家屋調査士法人」, joined by one thin plain dark navy line (no arrowhead) with the small label 「代理を依頼」.
- Bottom: one wide card with the dark navy heading 「不動産の表示に関する登記の申請手続の代理」 and one body line 「正当な事由がある場合でなければ、拒むことはできない」, with a small tag 「肢D1712」.
- 藍子 bubble (left, spoken first): 「法人なら、自由に
断れますよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「出たわね。
条文を読んで
いくわよ」 with the part 「条文を読んでいく」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 2 (clear, calm infographic mood; NO character appears in this panel (a full-width diagram panel with no speech bubble): the whole panel is the diagram, the infographic, or the explanation cards, drawn large):
- Label tab: 「②　条文の仕組み」
- A tall stacked diagram fills the whole panel, with a small dark navy tag 「出題者のねらい」 at the top left and a line beside it: 「法人にも、この義務は及ぶか」.
- Below, four parts stacked from top to bottom, each full width, with only a small empty gap between them and nothing drawn in the gaps.
- Part 1, a card (pale gray fill, dark navy outline), dark navy heading 「法22条　本則」, two body lines: 「正当な事由がある場合でなければ」, 「依頼を拒んではならない」.
- Part 2, a card (pale gray fill, dark navy outline), dark navy heading 「かっこ書で除かれる依頼」, two body lines: 「筆界特定の代理・相談」, 「民間紛争解決手続代理関係業務」, and a small tag 「拒める」.
- Part 3, one dark navy band with large white text 「法41条1項　法22条を調査士法人に準用」.
- Part 4, a card (pale gray fill, dark navy outline), dark navy heading 「調査士法人」, two body lines: 「かっこ書の外の依頼は」, 「正当な事由がなければ拒めない」.
- There is no check mark and no cross anywhere in this panel.

PANEL 3 (thoughtful then confident mood; both characters appear ONLY as small round face icons (heads only, each about 72 px across, no bodies and no hands) inside a vertical conversation column on the right side of the panel, exactly one face icon for each speech bubble (see the LAYOUT lines below)):
- Label tab: 「③　本番での読み方3ステップ」
- LAYOUT (two columns, fixed): the panel below the label tab is divided into a LEFT column (about 56% of the panel width) and a RIGHT column (about 44%). The LEFT column holds ALL of the diagram, cards, and ribbons described in the lines below, drawn large; it has no face icon, no speech bubble, and no character. The RIGHT column is a vertical conversation of EXACTLY 4 rows stacked from top to bottom in the speaking order of the bubble lines below (row 1 at the top is the first line), each row about 82 px tall, all rows the same height, never overlapping. Each row contains EXACTLY ONE round face icon and EXACTLY ONE speech bubble that belongs to it: in a 藍子 row her face icon is at the LEFT end of the row and the bubble is to its right, with the tail pointing left at her face; in a トリ先生 row his face icon is at the RIGHT end of the row and the bubble is to its left, with the tail pointing right at his face. So the right column shows exactly 4 face icons and exactly 4 speech bubbles in total, one pair per row, and no other face, character, or bubble appears anywhere else in the panel. The text inside each bubble is at least 32 px high, written on 2 or 3 lines exactly as broken in the bubble lines below.
- Three step cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a dark navy number badge, and a dark navy heading, with no check mark and no cross. The step cards are separated only by a small empty gap, with nothing drawn between them.
- Step card 1: heading 「ステップ1　主語を見る」, a dark navy ribbon tag with large white text 「ひっかけ：主語が調査士法人」, body 「法41条1項で、法人も法22条の対象」.
- Step card 2: heading 「ステップ2　かっこ書に当てはめる」, two body lines: 「登記の代理（法3条1項2号）は、かっこ書の外」, 「だから拒めない」.
- Step card 3: heading 「ステップ3　二重否定をほどく」, body 「正当な事由がなければ拒めない＝正当な事由があれば断れる」.
- There is no check mark and no cross anywhere in this panel.
- 藍子 bubble (left, row 1 of 4 in the conversation column; face icon at the LEFT end of its own row): 「法22条は、
調査士の規定ですよね？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 2 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「法41条1項で、
法人にも準用よ」 with the part 「法人にも準用」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- 藍子 bubble (left, row 3 of 4 in the conversation column; face icon at the LEFT end of its own row): 「登記の代理は、
除かれますか？」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, row 4 of 4 in the conversation column; face icon at the RIGHT end of its own row): 「かっこ書の外。
だから拒めないの」 with the part 「かっこ書の外」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.

PANEL 4 (藍子 relieved, トリ先生 smiling proudly; 藍子's hands: both hands raised in a small cheering fist (two hands in total)):
- Label tab: 「④　結論は〇」
- 藍子 bubble (left, spoken first): 「法人も、正当な事由
なしには断れない！」. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- トリ先生 bubble (right, spoken as the answer): 「そう。肢は〇よ。
根拠は法41条1項ね」 with the part 「法41条1項」 highlighted in yellow. The line breaks inside the quotation marks are intentional: keep them exactly and never split a word across lines.
- A checklist card in the middle with exactly three items, each with a BLUE check mark and no other mark; each item is written on at most two lines with text at least 28 px high: 「法22条：正当な事由がある場合でなければ、依頼を拒んではならない」, 「かっこ書の筆界特定の代理・相談などは除く。承諾しないときは速やかに通知（規則25条2項）」, 「法41条1項で調査士法人に準用。法人も、登記の代理は拒めない」.

CONCLUSION BANNER (solid pale yellow fill with a thin dark navy outline and dark navy text; large text, two lines):
- Line 1: 「調査士法人も、正当な事由がなければ依頼を拒めない」 with a yellow highlighter marker.
- Line 2: 「問題D1712　正解〇（R03-Q20オ）」

EMOTIONAL ARC: confident (panel 1) -> puzzled (panel 2) -> realizing (panel 3) -> relieved and convinced (panel 4).

Final check before rendering: confirm there are exactly four panels in one vertical column; confirm every text string matches the given string exactly and no extra text exists anywhere (including backgrounds, signs, papers, and frames); confirm that wherever 藍子 appears she is on the left and wherever トリ先生 appears he is on the right, and that panels showing one character or two very small characters are drawn as specified and every bubble tail points at its own speaker; confirm both characters match the attached references in all panels and 藍子 has the same hairstyle in every panel; confirm the characters 代, 号, 地, 対, 当, 承, 番, 登, 肢, 規, 解, 記, 請, 諾, 間 are drawn as proper Japanese kanji forms and never as simplified or traditional Chinese variants; confirm every stamp, arrow, and label stays inside its own card or panel frame; confirm 藍子 has exactly two arms and two hands with five fingers each in every panel and her pose differs from panel to panel; confirm that the conversation column has exactly 4 face icons and exactly 4 speech bubbles, one pair per row in the speaking order from top to bottom, that each bubble tail points at the face icon in its own row, that no face, character, or bubble appears outside the right column, and that the diagram stays in the left column; confirm that in the panels marked as normal-size side characters the two characters are NOT shrunk, stand at the outer edges, and the diagram stays in the center region without being covered; confirm that nothing but the given text appears above the heads of the pictograms; confirm that every panel marked as having no character contains no character and no speech bubble; confirm that every question badge has a pale gray fill with a dark navy outline and dark navy text and carries no check mark or cross; confirm that no triangle, chevron, arrow, or connector is drawn between the stacked step cards; confirm that the conclusion banner is pale yellow with dark navy text; confirm the background is fully opaque with no transparency, alpha channel, or checkerboard.
```

## 見出し画像プロンプト（苦手分析シリーズと同じ構成・背景は水彩の空）

noteの見出し画像（アイキャッチ）用です。トリ先生と藍子を描きます（キャラ仕様書の参照画像を添付し、どちらがどちらかを一言添える）。サイズは1280×670px。構成は苦手分析シリーズと同じ（上中央にタイトル2行とサブタイトル、下中央にトリ先生と藍子、左右の端にテーマの場面）。背景は苦手分析シリーズ踏襲の水彩の空（2026-10-07、ユーザー採用）。

### 見出し画像の文言（正本）

| 領域 | 正確な文言 | 強調 |
|---|---|---|
| タイトル1行目 | 調査士法人への依頼 | 薄い黄色のマーカー |
| タイトル2行目 | 断ってよい？ | 「断ってよい？」を赤みのあるオレンジ |
| サブタイトル | 4コマ解説図解　D1712　R03-Q20オ | — |

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
調査士法人への依頼
Line 2 is larger; the phrase 断ってよい？ is red-orange and the rest is dark navy:
断ってよい？
Below the title, a light blue rounded pill-shaped subtitle band with navy text:
4コマ解説図解　D1712　R03-Q20オ
Do not write any other text anywhere in the image: no captions, no labels, no signs with letters, no watermark, no panel numbers.

TOPIC SCENES (illustration only, no text on any object; keep them soft and slightly faded so they never compete with the title or the characters):
Left side: a small office building with a plain signboard and a desk with a stack of blank forms
Right side: a blank clipboard, a rubber stamp and a closed door with an empty nameplate

LAYOUT: keep a clear, uncluttered zone behind the title and subtitle. Keep the characters and the title away from the extreme edges so the image survives center cropping. Do not draw any flowchart, diamond, arrow between boxes, or check mark or cross mark.

Final check before rendering: confirm the image is exactly 1280x670 landscape; confirm the only text in the whole image is the two title lines and the subtitle, reproduced exactly as written; scan every kanji glyph and confirm it is the standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional Chinese, paying special attention to the kanji 調, 査, 士, 法, 人, 依, 頼, 断, 解, 説, 図; if any character renders as a Chinese variant, redraw it in the correct Japanese form; confirm both characters match the attached references and 藍子 keeps the same hairstyle; and confirm the entire canvas, edge to edge, is filled with a fully opaque background with no transparency or alpha channel anywhere.
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
| 4コマ解説図解（本文用・採用版） | 4コマ解説図解D1712～R03-Q20オ～.png |
| 見出し画像（採用版） | 4コマ解説図解D1712～R03-Q20オ～_見出し.png |
| 途中の版・不採用の版（例：v01） | 4コマ解説図解D1712～R03-Q20オ～_v01.png ／ 4コマ解説図解D1712～R03-Q20オ～_見出し_v01.png |

## 作成時の品質ゲート（`MANGA_RULES.md`の工程A〜C）
- [x] 一発合格ルール（`MANGA_RULES.md`の「一発合格のための作成ルール」）適用済み
- [x] 4コマの目的（最優先。`MANGA_RULES.md`）適用済み：設計メモに【出題者のひっかけ】【受験者の勘違い・定着していない点】【対比する制度】の3行を書いた
- [ ] 工程B：`python3 tools/drill/manga/check_prompt.py tools/drill/manga/D1712_prompt.md` が NG 0件
- [ ] 工程C：初見の読者：①何が問われているか（調査士法人も、正当な事由がなければ登記代理の依頼を拒めないか）②どこで答えが分かれるか（法22条の本則とかっこ書、法人への準用）③罠（主語が法人／二重否定／かっこ書の外か中か）④正しい整理（本則＝正当な事由がなければ拒めない、かっこ書の依頼は除く、法41条1項で法人にも準用）を言える
- [ ] 工程C：肝の確認：法22条の本則（正当な事由がある場合でなければ拒んではならない）＋かっこ書（筆界特定の代理・相談、民間紛争解決手続代理関係業務は除く）＋法41条1項（調査士法人に準用）＝法人も、登記の代理は拒めない。肢は〇
- [ ] 工程C：構成表の全文言を記事（R03-Q20オ）と法令DB（法22条・法3条1項・法41条1項・規則25条2項）に突き合わせ済み。記事にない整理は、かっこ書の中身（民間紛争解決手続代理関係業務を含む）と法3条1項2号の引用
- [ ] 工程C：コマの使い方が隣り合うコマで同じにならない（side→none→faces→既定）。コマ1〜3に印がなく、コマ4だけ青✓

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

- 2026-10-10 v01：条文版を新規作成（法22条の本則・かっこ書・法41条1項の準用を1枚で言える構成。肢中心の先行版D1712_prompt.mdと主張は同じ）
