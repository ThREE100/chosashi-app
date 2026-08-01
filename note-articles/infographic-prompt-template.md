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
3. **カードに落とし込む**：抽出した内容を、原則ごとに1枚の「カード」（見出し＋図解＋キャプション）にする。1カード＝1肢が基本だが、テーマが近い肢は1カードにまとめてもよい。カード数の目安は4〜6枚（肢の数と一致させる必要はない）。
4. **各カードに次の3要素を用意する**：
   - 見出し（1〜2行、太字、体言止めや「〜する」で結ぶ短い文）
   - 図解の説明（構図・アイコン・ラベルに使う文字列を具体的に指定する。誰が読んでも同じ絵になる粒度で書く）
   - キャプション（1〜2行、小さい文字での補足説明）
5. **下記「プロンプト雛形」に流し込み、プロンプト文を完成させる。**
6. **完成したプロンプト文だけをユーザーに提示する**（画像は生成しない）。

## プロンプト雛形（固定フォーマット）

```
Create a Japanese-language infographic, portrait layout, {SIZE_PX} pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric buildings, land
plots, stamps, torn paper labels, etc. — adapt icon set to the topic).

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

--- INTRO BLOCK (left: illustration; right: paragraph text) ---
Illustration: {INTRO_ILLUSTRATION_DESC}
{INTRO_TEXT}

--- COLUMN A HEADER (pill-shaped badge) ---
{COLUMN_A_LABEL}

--- COLUMN A, CARD 1 ---
Heading (bold):
{CARD_HEADING}
Illustration: {CARD_ILLUSTRATION_DESC}
Caption (small text below):
{CARD_CAPTION}

（…カードの数だけ繰り返し。列を分けない場合は「COLUMN」を省略して1列で並べる。）

--- FOOTER ---
Small credit text in the corner (optional, keep minimal).

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese. If any character
renders as a Simplified Chinese variant, redraw that character in the
correct Japanese form. Confirm the number of cards equals {CARD_COUNT}
exactly, with no duplicated or missing cards.
```

## 文字化け・簡体字対策（必須・厳守）

問9のインフォグラフィックで実際に発生した不具合（簡体字混入、用語の誤変換「公溜地（溜池）」「公園用地」、見出しの重複「墓地」、判読不能な文字列「/港口用用」）を再発させないため、以下を必ず守る。

1. プロンプトの冒頭と末尾の二重で「日本語のみ・常用漢字のみ・簡体字禁止」を明記する（雛形の CRITICAL TEXT REQUIREMENT と Final check の両方を必ず含める）。
2. カード見出し・キャプション・ラベルに使う文字列は、記事本文の表現をそのまま流用し、プロンプト側で言い換えない。プロンプト自体にも「verbatim（そのまま）・do not paraphrase」と明記する。
3. 列挙型の要素（種類の一覧など、項目数が決まっているもの）がある場合は、番号付きリストで全項目を一字一句明記し、「重複禁止・欠落禁止・言い換え禁止」を明記したうえで、生成後に個数と内容を自己検証させる一文を末尾に追加する。
4. 特に誤りやすい漢字（号・録・権・地・番・建・物・登・記・所など、簡体字との字形差が大きい字）がプロンプトに含まれる場合は、名指しで「簡体字にしない」よう注意喚起する一文を添える。
5. 生成後にユーザーが目視確認する前提だが、事前にこちらでも文字列の突き合わせ（記事本文とプロンプト中の文字列が一致しているか）を行ってから提示する。

## サイズ・アスペクト比

- 問題全体のインフォグラフィック（このドキュメントの対象）は、カード数が多く情報量が多いため**縦長ポートレート**を基本とする。目安は `1080×1920px`（9:16）だが、カード数が多い／少ないなど内容量に応じて `{SIZE_PX}` は調整してよい。ユーザーから明示的な指定があればそれを優先する。
- 肢ごとの見出し画像（①、このドキュメントの対象外）は `1280×670px` 横長固定。混同しないこと。

## スタイル（問9で確立した基準）

- カラー：淡いパステルカラー（青・緑・ベージュ・グレー）のフラットデザイン
- アイコン：アイソメトリック（斜め見下ろしの3D風）
- 構成：タイトル(上部) → サブタイトル → 導入文(図解+文章) → 複数カラムの原則カード群 → フッター
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
