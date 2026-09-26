## 【土地家屋調査士受験生向け】何度も同じところで間違える人へ〜苦手分析シリーズ②分筆・合筆・合併・合体、何が違う〜

**対象条文：不動産登記法40条・41条・49条・52条3項・56条、不動産登記規則102条・104条・105条・120条4項・131条・134条3項、民法252条5項**

この記事は、これまでの解答結果を分野別に振り返ったときに「一度ではなく複数の年度にわたって同じ論点で間違えている」と判明した分野を整理し直す苦手分析シリーズの第2回です。今回は、分筆・合筆・合併・合体という似た名前の4つの登記を混同しやすいという点を取り上げます。個別の過去問解説記事はすでに年度ごとに存在するため、この記事ではそれらを横断してつなぎ、「初見の問題でも迷わず判定できる形」に整理し直すことを目的にします。

---

似た名前の4つの登記は、対象（土地か建物か）と操作の向き（分けるかまとめるか）で整理できます。土地を分けるのが分筆、土地をまとめるのが合筆、建物をまとめるのが合併・合体です（建物を分ける「建物の分割」もありますが、試験で混同が起きやすいのは「まとめる」側の合筆・合併・合体の3つです）。この3つに分筆も加え、それぞれの性質を軸ごとに比較します。

- **対象**：分筆は土地1筆を複数筆に分ける登記です。合筆は土地の複数筆を1筆にまとめる登記です。合併は建物の複数個を1個にまとめる登記です（主・附属、または区分合併）。合体は物理的に一体化した複数の建物を1個の建物として記録する登記です。
- **実体的な成立要件**：分筆には特有の成立要件はありません。合筆には不動産登記法41条1〜6号という厳格な成立要件があります。合併にも不動産登記法56条1〜5号の成立要件があり、41条と骨格は共通しつつ要件は非対称です。合体は、現況をそのまま反映する登記です。
- **単独申請**：分筆は、共有地であれば保存行為として共有者の一人から申請できます。合筆は、表題部所有者または所有権の登記名義人でなければ申請できません。合併は、表示に関する登記であるため相続登記なしに相続人から申請できます（ただし住所の一致が前提です）。合体は、保存行為として共有者・相続人の一人から申請できます。
- **既存の他の権利の扱い**：分筆は原則として各土地に転写されますが、消滅承諾があれば一部の土地だけ権利を消滅させられます（分筆後の全部から消すことはできません）。合筆は消滅承諾書があっても認められず、内容が同一の担保権・信託登記等（不動産登記規則105条）と承役地側の地役権登記だけが例外的に存続を認められて合筆できます。合併も内容が同一の担保権・信託登記等（同規則131条）は例外的に存続を認められますが、共用部分である旨の登記があると合併できません（建物特有の制限です）。合体は、合体前の所有権以外の権利が持分上に移記されて存続します（同規則120条4項）。ただし賃借権のように持分になじまない権利は当然には移記されません。
- **登記原因及びその日付**：分筆は、一括申請の要件（同一管轄・同一目的・同一原因日付）はあるものの、分筆自体に特有の原因日付の問題は薄い登記です。合筆も同様に特有の原因日付の問題は薄い登記です。合併は、建物の種類変更等の表題部変更登記と一の申請情報で申請できます（同規則35条7号）。合体は「年月日新築、年月日新築、年月日合体」のように、各建物の新築日と合体日を並べて記録します。

### 分筆と抵当権の帰趨（繰り返し出題される最重要ポイント）

過去の間違いを振り返ると、「分筆時に抵当権者の承諾があるとどうなるか」という論点が複数の年度（平成26年度第10問、令和5年度第9問、令和7年度第11問）で繰り返し出題され、そのたびに間違えています。整理すると次のとおりです。

- 原則：分筆前の登記記録の権利登記は、分筆後の各土地に**転写**する（不動産登記規則102条1項）。
- 例外：権利者が「1筆を除いた他の土地」について権利の消滅を承諾する情報を提供すれば、その土地についてのみ権利を消滅させる登記ができる（不動産登記法40条、規則104条）。
- **落とし穴**：この承諾があっても、分筆後の**すべて**の土地から権利を消すことはできません。必ずどこかの土地には権利が残ります。地上権に抵当権が設定されている場合は、地上権者に加えその抵当権者の承諾も必要です（法40条括弧書）。

### 合筆と地役権の例外（同じ論点が複数年度で出題）

平成19年度第10問と令和2年度第10問は、どちらも「地役権が設定されている土地は合筆できるか」という同一の論点でした。不動産登記法41条6号は、所有権以外の権利の登記がある土地は原則として合筆できないとしますが、不動産登記規則105条1号により、**承役地**側の地役権登記は例外的に存続を認めて合筆できます。**要役地**側の地役権登記はこの例外に含まれず、原則どおり合筆の妨げになります。「承役地だけの例外」という非対称性が、繰り返し間違えているポイントです。

### 合筆・合併の対比（土地固有・建物固有の要件）

土地の合筆（41条）と建物の合併（56条）は、「名義人・持分が同一であること」「所有権登記の有無が一致すること」「他の権利の登記は原則不可（内容が同一なら例外あり）」という骨格が共通しています。一方で、**土地には「接続していること」「地目・地番区域が同一であること」という土地固有の要件があり、建物には「共用部分・団地共用部分の登記がないこと」という建物固有の要件があります**。この対比は`gappitsu-gappei-seigen.md`で号数レベルまで整理済みなので、詳細はそちらを参照してください。

### 合体の特殊性

合体は、複数の建物が物理的に一体化したという**現況をそのまま記録する登記**であり、共有物の保存行為（民法252条5項）として共有者・相続人の一人からでも単独申請できます。区分所有の意思を示した場合は「合体」ではなく非区分建物から区分建物への表題部変更登記（不動産登記法52条3項）として扱われる点、主である建物とその附属建物が一体化した場合はそもそも合体による登記等の対象にならない点も、合筆・合併とは別枠で押さえておくべき例外です。

### まとめ

分筆・合筆・合併・合体は、「対象が土地か建物か」「実体的な成立要件が厳格かどうか」「既存の権利がどう扱われるか」の3軸で区別すると混同しにくくなります。特に、分筆時の抵当権の帰趨（承諾があっても全部からは消せない）、合筆の地役権の例外（承役地側だけ）、合筆と合併の土地固有・建物固有の要件、合体だけが保存行為として単独申請できる現況記録型の登記であることの4点は、繰り返し間違えやすいポイントとして意識してください。

---

**確認事項**

- 分筆・合筆・合併・合体の対比は、`note-articles/h19-mondai/q12`、`note-articles/r3-mondai/q11`、`note-articles/r5-mondai/q09`、`note-articles/r7-mondai/q11`（分筆）、`note-articles/h27-mondai/q09`、`note-articles/r2-mondai/q10`、`note-articles/r4-mondai/q09`（合筆）、`note-articles/h28-mondai/q14`、`note-articles/r3-mondai/q16`（合併）、`note-articles/h28-mondai/q15`、`note-articles/r4-mondai/q15`、`note-articles/r5-mondai/q16`（合体）、`note-articles/column/bunpitsu-ikkatsu-gappitsu-chimoku.md`、`note-articles/topics/gappitsu-gappei-seigen.md`の内容に基づいています。
- 分筆・合筆・合併について「形成的登記」「報告的登記」という対概念そのものを明記した記述は、確認できた既存記事の範囲では見当たりませんでした。合体についてのみ「報告的登記」という明示的な記述が既存記事（`r5-mondai/q16`）にあったため、本記事でもその区別に沿って合体だけを「現況をそのまま記録する登記」と表現しています。
- `gappitsu-gappei-seigen.md`は当初「41条2号の地目は登記記録上の地目を基準とする」という誤った記述でしたが、令和6年度第9問イの公式正答と照合し、現況の地目を基準とする内容に訂正済みです。本記事の記述はこの訂正後の内容と整合しています。

---

## 見出し画像用フレーズ

- 分筆後の土地、全部から抵当権は消せないんです
- 承役地の地役権だけが合筆の例外なんです
- 合筆は土地の要件、合併は建物の要件、実は非対称なんです
- 合体だけは、共有者の一人からでも単独申請できるんです

---

## インフォグラフィック プロンプト

### 画像1：分筆・合筆・合併・合体の相互関係（系統図型）

```
Create a Japanese-language infographic, portrait layout, 1080x1600 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric land plots splitting
and merging, isometric buildings merging by registry vs merging by
physical fusion).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference
relationship diagram, NOT a text-heavy explainer document. There is NO
intro illustration and NO paragraph of prose anywhere on this poster — go
straight from the header to the diagram panels. Each panel must
communicate its point almost entirely through the illustration (icons,
arrows, small embedded labels) plus one short heading and one short
conclusion tag. Do NOT render any full-sentence explanation or legal
citation anywhere on the poster.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 分, 筆, 合, 併, 体,
記, 録 — do not draw these as Simplified or Traditional Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the panels — with a solid or illustrated opaque
background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
分筆・合筆・合併・合体、4つの関係

Subtitle (smaller, centered, 1行):
苦手分析シリーズ②対象と操作の向きで整理する

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL 1 ---
Badge: a filled circle in green containing the label "土地".
Heading (bold, ONE line, ~20 Japanese characters or fewer):
分筆と合筆は正反対の操作
Illustration: a single isometric land plot with an arrow labeled "分筆"
splitting it into two land plots, and a separate reverse arrow labeled
"合筆" merging two land plots back into one, drawn as a pair of opposite-
facing arrows so the inverse relationship is visually obvious.
Conclusion tag (green banner, 5-15 Japanese characters):
土地を分ける・まとめる

--- PANEL 2 ---
Badge: a filled circle in blue containing the label "建物・登記記録上".
Heading (bold, ONE line, ~20 Japanese characters or fewer):
合併は登記記録の上でまとめる
Illustration: two separate isometric building icons (each with its own
dashed registration-record border) merging into a single building icon
with one registration-record border, the dashed borders dissolving into
one, no physical wall change shown.
Conclusion tag (blue banner, 5-15 Japanese characters):
記録上1個にまとめる

--- PANEL 3 ---
Badge: a filled circle in blue containing the label "建物・物理的に".
Heading (bold, ONE line, ~20 Japanese characters or fewer):
合体は物理的に一体化した状態を記録
Illustration: two separate isometric building icons with a visible gap
between them, an arrow showing their outer walls physically joining into
a single continuous building silhouette (no gap, one roofline), then a
camera icon labeled "現況をそのまま記録" pointing at the fused building.
Conclusion tag (blue banner, 5-15 Japanese characters):
現況をそのまま記録

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
diagram has exactly 3 panels as described above, with no duplicated or
missing panels, confirm there is no intro illustration or paragraph block
between the header and the panels, confirm that no panel contains a full
sentence of explanatory prose, confirm nothing is rendered below the last
panel (no summary recap panel, no trophy or medal icon, and no additional
text block of any kind), and confirm the entire canvas, edge to edge, is
filled with a fully opaque background with no transparency or alpha
channel anywhere.
```

### 画像2：分筆・合筆・合併・合体の相互関係（早見表・1/2）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric land plots being
split/merged, isometric buildings being merged/fused).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the table. Each table row must communicate its point through a small
icon plus the short text specified for that row. Do NOT add any
explanation, illustration, or text beyond what is explicitly listed below.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 筆, 併, 体, 対, 象, 権,
記 — do not draw these as Simplified or Traditional Chinese variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the table — with a solid or illustrated opaque
background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
分筆・合筆・合併・合体、何が違う(1/2)

Subtitle (smaller, centered, 1行):
苦手分析シリーズ②対象・成立要件・単独申請

（タイトル・サブタイトルのすぐ下に表を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- TABLE ---
Render as a clean flat-design table with 4 data columns and alternating
row background colors (light green / white), Japanese sans-serif font, no
monospace font. Each row has a small isometric icon on the left.

Header row (5 columns, verbatim):
項目 ｜ 分筆 ｜ 合筆 ｜ 合併 ｜ 合体

Data rows (numbered 1-3 in this exact order; reproduce every row exactly
as written; do not omit, duplicate, merge, reorder, or paraphrase any
row):

1. 項目: 対象
   分筆: 土地1筆→複数筆
   合筆: 土地複数筆→1筆
   合併: 建物複数個→1個
   合体: 一体化した複数建物→1個
   Icon: an isometric land plot splitting into two, next to two land plots
   merging into one, next to two building icons merging into one.

2. 項目: 実体的な成立要件
   分筆: 特になし
   合筆: 不動産登記法41条1〜6号(厳格)
   合併: 不動産登記法56条1〜5号(41条と骨格は共通)
   合体: 現況をそのまま反映する登記
   Icon: a rule-book document icon with a large red "41" badge next to the
   合筆 column and "56" badge next to the 合併 column, and a small camera
   icon (「そのまま記録」の意味)next to the 合体 column.

3. 項目: 単独申請
   分筆: 共有地は保存行為として共有者の一人から可
   合筆: 表題部所有者又は所有権の登記名義人でなければ不可
   合併: 相続登記なしに相続人から可(住所の一致が前提)
   合体: 保存行為として共有者・相続人の一人から可
   Icon: a single person icon with a green checkmark for 分筆・合体 columns,
   and a group of people icon with a small lock for the 合筆 column.

Self-check instruction to embed in the image generation reasoning (not
rendered as visible text): confirm the table has exactly 3 data rows and 4
data columns (分筆・合筆・合併・合体) corresponding to the list above, in
the same order, with no row or column omitted, duplicated, merged, or
reworded.

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
table has exactly 3 data rows and 4 data columns exactly matching the list
above, with no duplicated or missing rows or columns, confirm there is no
intro illustration or paragraph block between the header and the table,
and confirm that no cell contains any text beyond what is specified for
that cell.
```

### 画像3：分筆・合筆・合併・合体の相互関係（早見表・2/2）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric mortgage document
stamps, chain-link icons, torn paper labels).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the table. Each table row must communicate its point through a small
icon plus the short text specified for that row. Do NOT add any
explanation, illustration, or text beyond what is explicitly listed below.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either. Reproduce the exact text strings
given below verbatim — do not paraphrase, translate, summarize, or
substitute any characters. Pay special attention to 転, 写, 権, 益, 筆,
併, 体, 移, 記 — do not draw these as Simplified or Traditional Chinese
variants.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas — including every
corner and margin outside the table — with a solid or illustrated opaque
background. There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 1行):
分筆・合筆・合併・合体、何が違う(2/2)

Subtitle (smaller, centered, 1行):
苦手分析シリーズ②既存の権利の扱い・登記原因

（タイトル・サブタイトルのすぐ下に表を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- TABLE ---
Render as a clean flat-design table with 4 data columns and alternating
row background colors (light green / white), Japanese sans-serif font, no
monospace font. Each row has a small isometric icon on the left.

Header row (5 columns, verbatim):
項目 ｜ 分筆 ｜ 合筆 ｜ 合併 ｜ 合体

Data rows (numbered 1-2 in this exact order; reproduce every row exactly
as written; do not omit, duplicate, merge, reorder, or paraphrase any
row):

1. 項目: 既存の他の権利の扱い
   分筆: 原則転写。消滅承諾で一部の土地だけ消滅可(全部からは消せない)
   合筆: 消滅承諾書では不可。内容同一の担保権・承役地の地役権は例外で存続
   合併: 内容同一の担保権等は例外で存続。共用部分の登記があると合併不可
   合体: 持分上に移記して存続(賃借権は当然には移記されない)
   Icon: a mortgage document icon split into two smaller stamped copies for
   分筆 column, a single mortgage document icon crossed out by a red ✕ for
   合筆 column, a mortgage document icon with a green checkmark for 合併
   column, and a document icon shrinking to fit a "持分" label for 合体
   column.

2. 項目: 登記原因及びその日付
   分筆: 一括申請時は同一原因日付が要件(規則の話)
   合筆: 特有の原因日付の問題は薄い
   合併: 表題部変更登記と一の申請情報で可
   合体: 「年月日新築、年月日新築、年月日合体」と並記
   Icon: a calendar/date-stamp icon with two identical dates linked by an
   "=" symbol for 分筆 column, a single blank calendar icon for 合筆
   column, two documents merging into one for 合併 column, and a timeline
   icon with three sequential date labels for 合体 column.

Self-check instruction to embed in the image generation reasoning (not
rendered as visible text): confirm the table has exactly 2 data rows and 4
data columns (分筆・合筆・合併・合体) corresponding to the list above, in
the same order, with no row or column omitted, duplicated, merged, or
reworded.

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Confirm the
table has exactly 2 data rows and 4 data columns exactly matching the list
above, with no duplicated or missing rows or columns, confirm there is no
intro illustration or paragraph block between the header and the table,
and confirm that no cell contains any text beyond what is specified for
that cell.
```

---

## 参考記事（この記事のもとになった過去問・既存記事）

- [合筆の登記の制限と建物の合併の登記の制限](../topics/gappitsu-gappei-seigen.md)
- [分筆の一括申請と合筆の地目制限](bunpitsu-ikkatsu-gappitsu-chimoku.md)
- [平成19年度午後の部第12問(分筆は保存行為)](../h19-mondai/q12-bunpitsu.md)
- [平成19年度午後の部第10問(承役地の合筆の例外)](../h19-mondai/q10-gappitsu.md)
- [平成26年度午後の部第10問(分筆と抵当権)](../h26-mondai/q10-bunpitsu.md)
- [平成27年度午後の部第9問(合筆の申請人)](../h27-mondai/q09-gappitsu.md)
- [平成28年度午後の部第10問(合筆の制限)](../h28-mondai/q10-gappitsu.md)
- [平成28年度午後の部第14問(建物の合併)](../h28-mondai/q14-tatemono-gappei.md)
- [平成28年度午後の部第15問(建物の合体)](../h28-mondai/q15-gattai.md)
- [令和2年度午後の部第10問(地役権と合筆の例外)](../r2-mondai/q10-gappitsu-seigen.md)
- [令和3年度午後の部第11問(共有地の分筆)](../r3-mondai/q11-bunpitsu.md)
- [令和3年度午後の部第16問(建物の分割・合併)](../r3-mondai/q16-tatemono-bunkatsu-gappei.md)
- [令和4年度午後の部第9問(合筆の登記)](../r4-mondai/q09-gappitsu.md)
- [令和4年度午後の部第15問(建物の合体)](../r4-mondai/q15-gattai-touki.md)
- [令和5年度午後の部第9問(分筆と抵当権)](../r5-mondai/q09-bunpitsu.md)
- [令和5年度午後の部第16問(合体か変更登記か)](../r5-mondai/q16-gattai.md)
- [令和7年度午後の部第11問(分筆で消える権利・残る権利)](../r7-mondai/q11-bunpitsu.md)
