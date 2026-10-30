# Xの運用（note-unei/x）

戦略上の位置づけは `note-unei/senryaku.md` の「5. 入り口を増やす（SNS）」の①。

## 表示名（名前）

決定：`みもっさん@土地家屋調査士試験対策`（2026-10-30）。

表示名（太字で出る名前）は自由に書ける文字列で、`@` 以降も含めて無料のアカウントで設定できる。
「名前＠肩書き」の形は、表示名の中に `＠〜` を書いているだけで、ユーザー名（`@xxxx` のID）とは別物。
表示名は50文字まで。

案（noteの名前「みもっさん」に合わせる）：

- `みもっさん＠調査士試験 再挑戦中`
- `みもっさん＠毎朝の調査士ドリル`
- `みもっさん｜土地家屋調査士試験の受験生`

## プロフィールの各欄（2026-10-30 表示名は「みもっさん@土地家屋調査士試験対策」に決定。アイコンはトリ先生）

### 自己紹介（160文字まで。107文字。2026-10-30 掲載済み）

```
土地家屋調査士試験の受験生。令和8年度は夏前から挑戦するも太刀打ちできず、令和9年度の合格へ再スタート。毎朝、条文から作ったオリジナルの択一ドリルを出題、夜に記述式ドリルを投稿します。過去問の全肢解説はnoteで。
```

### 場所（30文字まで。2026-10-30 掲載済み）

住んでいる場所は書かず、毎日の投稿の中身を書いて「何が読めるか」を伝える。

```
毎朝ドリル1問 択一＋条文の空欄補充、午後 記述式ドリル
```

### ウェブサイト

noteのトップページのURL（`https://note.com/` の後ろにnoteのID）。

### ヘッダー画像（1500×500px）

ChatGPTに、アイコンのトリ先生の画像を添付して貼る。

```
Create a Twitter/X profile header image, EXACTLY 1500x500 pixels (3:1 landscape).
STYLE: soft Japanese watercolor-like illustration, bright pastel morning sky (light blue, cream, pale yellow), gentle clouds, clean outlines.
CHARACTER: draw only the owl teacher shown in the attached image (brown owl with round glasses and a blue shirt). Copy his look exactly; do not add any other person or animal. Place him on the right third, pointing up cheerfully.
SAFE ZONE (critical): the profile icon covers the bottom-left corner (about 400x400px from the left edge) and the right edge may be cropped on phones, so keep the left 30% and the bottom 25% free of text and the character's face.
TEXT (Japanese only, reproduce verbatim, nothing else), centered in the upper middle area, bold rounded font, dark navy over a soft white cloud glow:
毎朝1問　土地家屋調査士試験
Below it, smaller, red-orange:
条文から作るオリジナルの択一
The only digit allowed is the half-width Arabic digit 1 in 毎朝1問, written exactly as given. Do not render any other text, letters, digits, or decorative glyphs. Use standard Japanese Jōyō kanji only (no Simplified or Traditional Chinese forms).
BACKGROUND: fully opaque from edge to edge; no transparency, no checkerboard.
DECOR: faint land-survey motifs in the sky (a surveyor's tripod, a boundary stake, a folded map) drawn small and soft, without any writing on them.
```

## 固定する投稿（最初に1本。2026-10-30 文面を統一、280字に収まるよう短縮）

```
はじめまして。土地家屋調査士試験の受験生です。
令和8年度は太刀打ちできず、令和9年度合格へ再スタート。
朝は条文から作ったオリジナルの択一ドリル、夜は記述式ドリルを投稿します。
毎日一緒に続けましょう。
過去問の全肢解説はnoteで。
{noteのURL}
#土地家屋調査士 #調査士試験
```

## 毎日の投稿

- 投稿文は `make_x_posts.py` で作り、`posts.md` に全日分（第1日〜第120日）が入っている。手で直さず、直すときはスクリプトを直して作り直す。形は2026-10-30にユーザーが決めた。
  - 朝（択一ドリル）：テーマと「答えと解説はnoteで」。**問題の画像を添える**（`daily-drill/out/dayNNN-am.html` をブラウザで開き、問題文と選択肢の部分を画面写しにする）。
  - 返信（択一ドリルの答え）：朝の投稿への**返信**として投稿する（朝の問題と答えが1本につながる）。正解の番号と組合せ、解説記事のタイトルのひとことの要点、noteの解説記事のURL（`{URL}` を貼りかえる）。
  - 夜（記述式ドリル）：テーマと「解答・解説はnoteで」、その日の記述式ドリルのnoteの記事のURL。**問題の画像を添える**（`daily-drill/out/dayNNN-pm.html` の画面写し）。**返信はしない**。テーマは問題のタイトルから末尾の括弧書きを外したもの。
- スクリプトは、正解を問題データの各肢の正誤から計算し、解説記事の「正解：…（選択肢N番）」と一致することを確かめる。食い違うと止まる。
- Xの文字数（全角2・半角1・URL23で280以下）も確かめる。
- 投稿の時刻の目安：朝7時ごろ（択一と返信）・夜21時ごろ（記述式）。Xの予約投稿を使うと、前の晩にまとめて入れておける。

## 守ること

- 朝の投稿の本文には答えを書かない（答えは返信に書く）。
- 投稿の7〜8割は、投稿だけで役に立つ中身にする。noteへの案内は朝・返信の投稿と固定の投稿だけにとどめる。
- 予備校の教材（問題文・解説文）は載せない。
- 反応（いいね・返信・表示回数）が多かった日のテーマは、`note-unei/kpi-log.csv` の `memo` に残す。noteで深く書く候補にする。
