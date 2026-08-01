# 問題別インフォグラフィック プロンプト作成ルール（固定テンプレート）

## これは何か

`format-template.md` に沿って書いた1問1答の解説記事（例：`r3-mondai/q09-chiban-kaokubangou.md`）の内容をもとに、その問題全体（通常ア〜オの5肢）の要点を1枚で俯瞰できる**インフォグラフィック**を作るための、画像生成プロンプトを組み立てる手順を定める。

画像生成そのもの（ChatGPTのGPT Image 2等）はユーザーが手動で行う。このリポジトリ・このルールで作るのは**プロンプトの文章まで**であり、画像ファイルは生成しない。

## 対象と非対象（他のルールとの切り分け）

インフォグラフィック関連の成果物は3種類あり、混同しないこと。

| 種類 | 対応するルール | 内容 | スタイル | サイズ |
|---|---|---|---|---|
| ①肢ごとの note見出し画像 | このドキュメントの対象外（都度チャットで個別に作成） | 1つの肢(ア〜オのうち1つ)の結論を1シーンで表現 | モノクロ鉛筆画、女性キャラクター1人が資料を持つ構図 | 1280×670px 横長固定 |
| ②問題全体のインフォグラフィック | **このドキュメント** | その問題の5肢すべてを俯瞰する複数パネル構成 | カラー・フラットデザイン・アイソメトリック(斜め見下ろし)アイコン | 縦長ポートレート(下記「サイズ」参照) |
| ③分野別記事の設計メモ | `bunya-kaisetsu/format-template.md` の「インフォグラフィック設計メモ」 | 分野別・総合記事向けの構成案を**文章で**指定するのみ(プロンプト化はしない) | 記事ごとに都度検討 | 規定なし |

このドキュメントは②専用。①・③の依頼が来た場合は、それぞれ別の扱いをする（①はこれまで通り個別にプロンプトを作る、③は画像化せず設計メモのまま記事に残す）。

## 手順（問9で行った作業の再現）

1. **対象記事を読む**：`note-articles/{年度}-mondai/q{n}-*.md` を読み、以下を抽出する。
   - 記事タイトル・分野テーマ（例：「地番と家屋番号の基本ルール」）
   - 各肢（ア〜オ）の「まとめ表」の1行分（判定＋ポイント）と、本文の結論部分
   - 全体を貫く軸（例：「土地の地番に関する原則」と「建物の家屋番号に関する原則」で2系統に分かれる）があれば、それをレイアウトの列・グループ分けの基準にする
2. **正しい結論だけを図解する**：問題文の「誤っている記述」をそのまま図解しない。まとめ表で「誤」と判定された肢は、正しいルール（＝その肢が本当は何と言うべきだったか）に直して図解する。（例：問9のイ「登記官は地番を変更できない」は誤りの肢だが、インフォグラフィックには正しいルール「地番が錯雑している場合、登記官は職権で変更できる」として載せる。）
3. **カードに落とし込む**：抽出した内容を、原則ごとに1枚の「カード」（番号バッジ＋見出し＋図解＋結論タグ）にする。1カード＝1肢が基本だが、テーマが近い肢は1カードにまとめてもよい。カード数の目安は4〜6枚（肢の数と一致させる必要はない）。カードの番号は列ごとにリセットせず、1枚目から通し番号（1・2・3・4・5…）を振る。
4. **各カードに次の4要素を用意する**：
   - 番号バッジ（通し番号。列ごとに色を変える。例：列A＝緑の丸、列B＝青の丸。列見出しの色と揃える）
   - 見出し（1行、太字、体言止めまたは短い文で結ぶ。**20字前後を上限とする要約フレーズにする**。まとめ表のポイント欄をそのまま使わず、主語や条文番号を落としてさらに削ぎ落とす）
   - 図解の説明（構図・アイコン・ラベルに使う文字列を具体的に指定する。誰が読んでも同じ絵になる粒度で書く。○×マーク・チェックマーク・短いラベル札は図解の中に直接埋め込む）
   - **結論タグ**（図解の下に置く、色付きの帯・バッジに入れる**5〜15字程度の一言**。文章ではなく単語・短フレーズにする。例：「移転登記が先」「家庭裁判所の許可 不要」「承諾だけでは不可」「表示登記」「転写されないだけ」。条文番号や「〜であり、〜とされていない」のような説明文はここに入れない）
5. **下記「プロンプト雛形」に流し込み、プロンプト文を完成させる。**
6. **完成したプロンプト文だけをユーザーに提示する**（画像は生成しない）。

### 見出し・結論タグを「要約」する具体例（重要）

まとめ表のポイント欄や本文の結論は、条文根拠つきの1文になっていることが多い。これをそのままカードの見出し・結論タグに転記すると文字だらけになるため、**この段階で必ず圧縮する**。

| 元の文（まとめ表・本文） | 見出し（20字前後） | 結論タグ（5〜15字） |
|---|---|---|
| 分筆の登記を申請できるのは、表題部所有者または所有権の登記名義人に限られる（不動産登記法39条1項）。名義変更前の買主は単独では申請できない。 | 名義変更前の買主は申請不可 | 移転登記が先 |
| 分筆の登記は財産の現状を大きく変える処分行為ではなく管理行為的なものとされ、相続財産管理人による申請に家庭裁判所の許可を証する情報の提供は不要。 | 相続財産管理人は許可不要 | 家庭裁判所の許可 不要 |
| 分筆の登記は表示に関する登記であり、賃借権の登記名義人の承諾を証する情報は添付情報とされていない。 | 賃借権者の承諾は不要 | 表示登記 |

条文番号（「不動産登記法39条1項」等）は見出し・結論タグには含めない。根拠を残したい場合は、図解内のごく小さな注記（誰も読まなくても構成が崩れない程度の補助情報）にとどめ、主役にしない。

## プロンプト雛形（固定フォーマット）

```
Create a Japanese-language infographic, portrait layout, {SIZE_PX} pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric buildings, land
plots, stamps, torn paper labels, etc. — adapt icon set to the topic).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. Every card must communicate its point
almost entirely through the illustration (icons, X marks, checkmarks, small
embedded labels) plus one short heading and one short conclusion tag. Do
NOT render any full-sentence explanation, legal citation, or paragraph of
body text anywhere on the cards. If a piece of information cannot be
expressed as a short label (a few words) or drawn as an icon, leave it out
rather than writing it as prose.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Every kanji must match standard Japanese
orthography exactly as written below, stroke-for-stroke. Reproduce the
exact text strings given below verbatim — do not paraphrase, translate,
summarize, or substitute any characters.

--- HEADER ---
Title (large, bold, {N}行):
{TITLE}

Subtitle (smaller, centered, {N}行):
{SUBTITLE}

--- INTRO BLOCK (left: illustration; right: paragraph text — this is the
ONLY place in the whole poster where a short paragraph of prose is
allowed) ---
Illustration: {INTRO_ILLUSTRATION_DESC}
{INTRO_TEXT}

--- COLUMN A HEADER (pill-shaped badge, color: {COLUMN_A_COLOR}) ---
{COLUMN_A_LABEL}

--- COLUMN A, CARD {N} ---
Badge: a filled circle in {COLUMN_A_COLOR} containing the number {N} (numbers
run continuously across all columns — do not restart at 1 in column B).
Heading (bold, ONE line, ~20 Japanese characters or fewer — a compressed
takeaway phrase, not the original full sentence from the article):
{CARD_HEADING_SHORT}
Illustration: {CARD_ILLUSTRATION_DESC} (embed any ✕/✓ marks and short
name-tag labels directly inside the illustration itself, e.g. a crossed-out
document icon with a 2-4 character label next to it)
Conclusion tag (a short colored banner/pill directly below the illustration,
{COLUMN_A_COLOR}, 5-15 Japanese characters, a keyword phrase — NOT a
sentence, NOT a legal citation):
{CARD_CONCLUSION_TAG}

（…カードの数だけ繰り返し。列を分けない場合は「COLUMN」を省略して1列で並べ、
バッジ色は1色に統一する。）

--- FOOTER ---
Small credit text in the corner (optional, keep minimal).

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese. If any character
renders as a Simplified Chinese variant, redraw that character in the
correct Japanese form. Confirm the number of cards equals {CARD_COUNT}
exactly, with no duplicated or missing cards, and confirm that no card
(other than the intro block) contains a full sentence of explanatory
prose — every card's takeaway must read as a short heading + a short
conclusion tag, at a glance.
```

## 文字化け・簡体字対策（必須・厳守）

問9のインフォグラフィックで実際に発生した不具合（簡体字混入、用語の誤変換「公溜地（溜池）」「公園用地」、見出しの重複「墓地」、判読不能な文字列「/港口用用」）を再発させないため、以下を必ず守る。

1. プロンプトの冒頭と末尾の二重で「日本語のみ・常用漢字のみ・簡体字禁止」を明記する（雛形の CRITICAL TEXT REQUIREMENT と Final check の両方を必ず含める）。
2. カード見出し・結論タグ・ラベルに使う文字列は、圧縮後（上記「見出し・結論タグを『要約』する具体例」参照）に確定した文字列をプロンプト側でそれ以上言い換えない。プロンプト自体にも「verbatim（そのまま）・do not paraphrase」と明記する。
3. 列挙型の要素（種類の一覧など、項目数が決まっているもの）がある場合は、番号付きリストで全項目を一字一句明記し、「重複禁止・欠落禁止・言い換え禁止」を明記したうえで、生成後に個数と内容を自己検証させる一文を末尾に追加する。
4. 特に誤りやすい漢字（号・録・権・地・番・建・物・登・記・所など、簡体字との字形差が大きい字）がプロンプトに含まれる場合は、名指しで「簡体字にしない」よう注意喚起する一文を添える。
5. 生成後にユーザーが目視確認する前提だが、事前にこちらでも文字列の突き合わせ（記事本文とプロンプト中の文字列が一致しているか）を行ってから提示する。

## サイズ・アスペクト比

- 問題全体のインフォグラフィック（このドキュメントの対象）は、カード数が多く情報量が多いため**縦長ポートレート**を基本とする。目安は `1080×1920px`（9:16）だが、カード数が多い／少ないなど内容量に応じて `{SIZE_PX}` は調整してよい。ユーザーから明示的な指定があればそれを優先する。
- 肢ごとの見出し画像（①、このドキュメントの対象外）は `1280×670px` 横長固定。混同しないこと。

## スタイル（問9・問11で確立した基準）

- カラー：淡いパステルカラー（青・緑・ベージュ・グレー）のフラットデザイン
- アイコン：アイソメトリック（斜め見下ろしの3D風）
- 構成：タイトル(上部) → サブタイトル → 導入文(図解+文章、ポスター内で唯一まとまった文章が許される箇所) → 複数カラムの原則カード群 → フッター
- **カードは「読ませる」のではなく「見せる」**：各カードは通し番号バッジ＋短い見出し(1行)＋図解＋短い結論タグ(5〜15字)の4点のみで構成し、説明文・条文根拠を長文で書かない。図解の中の○×マークや短いラベル札で情報を伝える。
- 列ごとに色を割り当て（例：列A＝緑、列B＝青）、その列の見出しバッジ・カード番号バッジ・結論タグの色を統一する。
- 肢ごとの見出し画像（モノクロ鉛筆画・女性キャラクター）とは別のビジュアル言語であることを前提とする。同じ問題について両方作る場合でも、スタイルを混ぜない。

## 内容の正確性チェック

- インフォグラフィックに書く法的内容は、必ず元記事の「まとめ表」「各肢解説」と一致させる。独自解釈・誇張・簡略化しすぎた言い換えをしない。
- 元記事が後日修正された場合（例：R3午後第3問ウへの民法258条の2の追記）、インフォグラフィックのプロンプトも同じ内容に追従して更新する。
- 「誤っている肢」をそのまま図解しない（手順2を参照）。図解するのは常に「正しいルール」。

## 依頼を受けたときの実行手順（このルールの使い方）

「問{年度}{n}のインフォグラフィックのプロンプトを作って」と依頼されたら、次の順で対応する。

1. 対象記事（`note-articles/{年度}-mondai/q{n}-*.md`）を読み込む。
2. 上記「手順」1〜4に従い、カード内容を組み立てる。
3. 「プロンプト雛形」に流し込み、「文字化け・簡体字対策」を必ず適用する。
4. 画像は生成せず、完成したプロンプト文だけをチャットに提示する。
5. ユーザーから求められない限り、記事ファイル自体（`.md`）は変更しない（このプロンプトはあくまで別途手動生成する画像の設計図であり、記事本文の一部ではない）。
