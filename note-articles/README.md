# 土地家屋調査士試験 note解説記事

土地家屋調査士試験の過去問（択一式、ア〜オの5肢問題）を、note投稿用に初学者向けに解説した記事一式です。Claude Codeとの対話の中で、法務省公表の試験問題原本・正答資料、条文、実務解説サイトを都度確認しながら作成しています。

## フォルダ構成

```
note-articles/
├── README.md               このファイル
├── format-template.md      note記事の執筆フォーマット(固定テンプレート)
├── generate-prompt.md      新しい問題の記事を生成するためのプロンプトテンプレート
├── tools/
│   └── md_to_mt.py         記事一式をnote.comインポート用MT形式に一括変換するスクリプト
├── exports/                md_to_mt.pyの変換結果(年度フォルダごとの.mt.txt)
│   ├── r6-mondai.mt.txt
│   ├── r7-mondai.mt.txt
│   └── h23-mondai.mt.txt
├── r7-mondai/              令和7年度 午後の部の解説記事(問題ごとに1ファイル)
│   ├── q02-senyuken.md            第2問 占有権
│   ├── q03-souzoku.md             第3問 相続の承認及び放棄
│   ├── q04-chizu-teisei.md        第4問 地図の訂正
│   ├── q05-hozonkikan.md          第5問 保存期間
│   ├── q06-shokutaku-touki.md     第6問 嘱託登記
│   ├── q07-ininjou.md             第7問 委任状・代理権
│   ├── q08-hyoudaibu-shoyuusha.md 第8問 表題部所有者
│   ├── q09-chisekisokuryouzu.md   第9問 地積測量図
│   ├── q10-tatemonozumen.md       第10問 建物図面及び各階平面図
│   ├── q11-bunpitsu.md            第11問 分筆の登記
│   ├── q12-tatemono-shurui.md     第12問 建物の種類
│   ├── q13-shikichiken.md         第13問 敷地権
│   ├── q14-tatemono-hyoudai.md    第14問 建物の表題登記
│   ├── q15-kyouyoububun.md        第15問 共用部分である旨の登記
│   ├── q16-hikkaitokutei.md       第16問 筆界特定
│   ├── q17-shinsaseikyuu.md       第17問 審査請求
│   ├── q18-houtei-souzoku.md      第18問 法定相続情報一覧図
│   ├── q19-touroku-menkyozei.md   第19問 登録免許税
│   └── q20-chousashihou.md        第20問 土地家屋調査士・調査士法人
└── r6-mondai/              令和6年度 午後の部の解説記事(問題ごとに1ファイル、第1問〜第20問すべて作成済み)
    ├── q01-koui-nouryoku.md           第1問 制限行為能力者の取消し
    ├── q02-taikouyouken.md            第2問 対抗要件(民法177条)
    ├── q03-daishuu-souzoku.md         第3問 代襲相続
    ├── q04-hyoudai-touki-tenpu.md     第4問 表題登記の添付情報
    ├── q05-chousashi-houkoku-houshiki.md 第5問 調査士報告方式
    ├── q06-chizu-teisei.md            第6問 地図等
    ├── q07-chiseki-kosei.md           第7問 地積に関する更正の登記
    ├── q08-bunpitsu-touki.md          第8問 土地の分筆の登記
    ├── q09-gappitsu-touki.md          第9問 合筆の登記
    ├── q10-chiekiken-zumen.md         第10問 地役権図面
    ├── q11-daii-ni-yoru-touki.md      第11問 代位による登記
    ├── q12-tatemono-nintei.md         第12問 建物の認定
    ├── q13-tatemono-shozai.md         第13問 建物の所在
    ├── q14-fuzoku-tatemono.md         第14問 附属建物
    ├── q15-tatemono-hyoji-touki.md    第15問 建物の表示に関する登記
    ├── q16-tatemono-bunkatsu-gappei.md 第16問 建物の分割又は合併の登記
    ├── q17-tatemono-messitsu.md       第17問 建物の滅失の登記
    ├── q18-kubun-tatemono.md          第18問 区分建物の登記
    ├── q19-hikkai-tokutei.md          第19問 筆界特定
    └── q20-chousashihou-gyoumu-kitei.md 第20問 土地家屋調査士法
└── h23-mondai/             平成23年度 午後の部の解説記事(第1問〜第20問すべて作成済み、r6-mondaiと同格の年度フォルダ)
    ├── q01-ishi-hyouji.md             第1問 意思表示
    ├── q02-jikou-engyo.md             第2問 時効の援用
    ├── q03-kyouyu.md                  第3問 共有
    ├── q04-touki-shikibetsu-jouhou.md 第4問 登記識別情報の通知
    ├── q05-chizu-teisei.md            第5問 地図の訂正
    ├── q06-bunpitsu.md                第6問 分筆の登記の申請
    ├── q07-chiban.md                  第7問 登記官が定める地番
    ├── q08-bunpitsu-gappitsu-kenri.md 第8問 所有権以外の権利のある土地の分筆及び合筆
    ├── q09-hikkai-shoyukenkai.md      第9問 筆界及び所有権界
    ├── q10-ichi-no-shinsei-jouhou.md  第10問 一の申請情報で申請する登記
    ├── q11-daii-shinsei.md            第11問 登記の代位申請
    ├── q12-hyoudaibu-kousei.md        第12問 表題部の更正の登記
    ├── q13-tatemono-messitsu.md       第13問 建物の滅失の登記
    ├── q14-kankatsu.md                第14問 登記所の管轄
    ├── q15-tatemonozumen-kaisuheimenzu.md 第15問 建物図面及び各階平面図
    ├── q16-hyouji-touki-gimu.md       第16問 不動産の表示に関する登記(申請義務)
    ├── q17-fuzoku-tatemono.md         第17問 附属建物
    ├── q18-tatemono-gattai.md         第18問 建物が合体した場合の登記の申請
    ├── q19-kubun-tatemono-hyoudai.md  第19問 建物の表題登記の申請(区分建物)
    └── q20-chousashihou.md            第20問 土地家屋調査士・調査士法人の業務制限
```

令和7年度分は第1問は本シリーズでは未作成です（作業を第2問から開始したため）。令和6年度分・平成23年度分はいずれも第1問〜第20問すべて作成済みです。

## 平成23年度分の情報ソースについて

平成23年度分（h23-mondai）は、`src/data/takuitsu.json`（全年度分の問題文・肢・正解を収録するアプリのマスターデータベース）を出題内容・正解番号の一次情報源としました。

- `missing_H23.json`・`kaisetsu_H23.json`（第2問〜第8問、第10問〜第19問の問題文・approach等の下書き解説）も参照しましたが、第1問・第9問・第20問はこれらのファイルに収録されておらず、`src/data/takuitsu.json`のみに全20問分のデータが存在したため、これをマスターソースとして採用しました。
- `kaisetsu_H23.json`の解説文（approach/pitfalls/keyPoints）は`reviewed:false`（未検証）の下書きであり、実際に第2問（時効の援用）で結論が誤っている（後順位抵当権者の援用可否についての判例解釈が逆）ことが判明したため、本シリーズでは各記事の法的根拠として採用せず、正解番号のみを参照した上で、条文・判例・実務先例から独立に法的根拠を再構成しました。
- `src/data/takuitsu.json`と`missing_H23.json`の正解番号は、両者が収録する17問（第2〜8問、第10〜19問）について完全に一致することを確認済みです（第2問についてのみ`kaisetsu_H23.json`のapproach文中の結論が両データベースの正解番号と食い違っていたため、データベースの正解番号を優先しました）。
- 第20問（土地家屋調査士法）の解説では、e-Gov法令検索・法務省サイトへの直接アクセスができなかったため、ウェブ検索結果の要約に基づいて条文構造（22条の2の業務制限とその例外）を整理しました。条文の項・号までの確定はできていない旨を、当該記事の確認事項ブロックに明記しています。
- 全20記事について、作成後に正解番号・各肢の正誤判定・まとめ表・正解表記の整合性を、データベースの正解番号と機械的に突き合わせる独立したダブルチェックを実施済みです。
- 平成23年度より後(平成24年度〜令和7年度)に同一・類似テーマの問題が再出題されていないかを`takuitsu.json`全体から検索し、重複出題チェックの結果を各記事の確認事項ブロックに記録しています。特に第5問(地図の訂正)・第11問(代位申請)・第13問(建物の滅失の登記)・第15問(建物図面及び各階平面図)・第19問(建物の表題登記)は、既にnote-articles配下に執筆済みのr6-mondai・r7-mondaiの記事と論点が強く重複するため、note投稿の際は書き分け・公開間隔に注意してください（詳細は各記事の確認事項ブロック参照）。

## 令和6年度分の情報ソースについて

令和6年度分（r6-mondai）は、法務省公表資料に加えて、ユーザーが過去に構築した土地家屋調査士試験対策アプリのデータベースを主要な一次情報源として作成しました。

- `takuitsu.json`（問題文・肢・正解・explanationフィールドの詳細な条文根拠解説）を各記事の法的根拠の一次情報源とした。
- `kaisetsu_plus.json`（approach/pitfalls/keyPointsの補足解説）を初学者向けの具体例作成のヒントとして参照した。
- ローカルに保存されているアガルートの教材（`土地家屋調査士_アガルート`フォルダ）も確認したが、択一式については講義動画のチャプター一覧（対照表PDF）のみで、個別問題のテキスト解説は含まれていなかったため、参照できなかった。
- 全20記事について、作成後に法務省公式の正解表（PDF）と条文（e-Gov法令検索等）を用いた独立したダブルチェックを実施し、正解番号・各肢の正誤判定に誤りがないことを確認済み。

## 各記事の構成

各記事は `format-template.md` の型に沿って以下の要素で統一されています。

1. タイトル（【土地家屋調査士受験生向け】＋一言キャッチ）
2. 出典（出題年度・午前/午後・問題番号）
3. 問題文の引用（ア〜オの肢＋選択肢の組合せを含む全文）
4. 各肢の解説（見出しは正しい結論を表すフレーズ、条文根拠、「たとえば」で始まる具体例）
5. まとめ表（肢・判定・ポイントの3列）
6. 正解（本文の最後に明記。冒頭での先出しはしない）
7. 「このまま使える点／使う前に確認したい点」の確認事項ブロック（出典・根拠の確認状況を正直に記載）
8. 見出し画像用フレーズ（語り口調のキャッチフレーズ、通常5つ）

## 正確性についての方針

- 出題年度・問題番号・正解番号は、法務省公表の試験問題原本(https://www.moj.go.jp/MINJI/minji05_00732.html 等)と正答資料(https://www.moj.go.jp/content/001450015.pdf 等)を直接確認したものです。
- 各肢の法的根拠は、条文(e-Gov法令検索等)・実務解説サイト・予備校教材を検索して確認していますが、確認できた根拠の確度は記事ごと・肢ごとに異なります。各記事末尾の確認事項ブロックに、根拠が条文レベルで確認済みか、一般原則からの推論にとどまるかを明記しています。
- 今後、内容の誤りが判明した場合は、該当ファイルを修正し、コミットメッセージに修正内容を明記してください。

## 新しい問題の記事を作成する方法

`generate-prompt.md` を参照してください。新しい年度・問題番号を指定してClaude Codeに投げれば、同じ形式の記事を生成できます。

## note.comインポート用ファイルの生成

`tools/md_to_mt.py` を使うと、年度フォルダ配下の記事一式を、note.comのインポート機能が受け付けるMT(Movable Type)形式のテキストファイルに一括変換できます。

```
python note-articles/tools/md_to_mt.py note-articles/h23-mondai note-articles/exports/h23-mondai.mt.txt
```

- まとめ表はnoteの本文エディタが表組みを描画できないため箇条書きに変換されます。
- 「このまま使える点／使う前に確認したい点」の確認事項ブロック（重複出題チェックのメモを含む）は執筆時の内部メモであり読者向けの本文ではないため、変換結果からは除外されます。重複出題の有無は、投稿前に必ずMarkdown側の確認事項ブロックを確認してください。
- インポートされた記事はすべて下書き(Draft)状態になるため、公開は手動で行ってください。
- 新しい年度フォルダができたら、同じスクリプトをそのフォルダパスに対して再実行するだけで変換できます。
