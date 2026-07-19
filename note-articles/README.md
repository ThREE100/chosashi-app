# 土地家屋調査士試験 note解説記事

土地家屋調査士試験の過去問（択一式、ア〜オの5肢問題）を、note投稿用に初学者向けに解説した記事一式です。Claude Codeとの対話の中で、法務省公表の試験問題原本・正答資料、条文、実務解説サイトを都度確認しながら作成しています。

## フォルダ構成

```
note-articles/
├── README.md               このファイル
├── format-template.md      note記事の執筆フォーマット(固定テンプレート)
├── generate-prompt.md      新しい問題の記事を生成するためのプロンプトテンプレート
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
├── r6-mondai/              令和6年度 午後の部の解説記事(問題ごとに1ファイル、第1問〜第20問すべて作成済み)
│   ├── q01-koui-nouryoku.md           第1問 制限行為能力者の取消し
│   ├── q02-taikouyouken.md            第2問 対抗要件(民法177条)
│   ├── q03-daishuu-souzoku.md         第3問 代襲相続
│   ├── q04-hyoudai-touki-tenpu.md     第4問 表題登記の添付情報
│   ├── q05-chousashi-houkoku-houshiki.md 第5問 調査士報告方式
│   ├── q06-chizu-teisei.md            第6問 地図等
│   ├── q07-chiseki-kosei.md           第7問 地積に関する更正の登記
│   ├── q08-bunpitsu-touki.md          第8問 土地の分筆の登記
│   ├── q09-gappitsu-touki.md          第9問 合筆の登記
│   ├── q10-chiekiken-zumen.md         第10問 地役権図面
│   ├── q11-daii-ni-yoru-touki.md      第11問 代位による登記
│   ├── q12-tatemono-nintei.md         第12問 建物の認定
│   ├── q13-tatemono-shozai.md         第13問 建物の所在
│   ├── q14-fuzoku-tatemono.md         第14問 附属建物
│   ├── q15-tatemono-hyoji-touki.md    第15問 建物の表示に関する登記
│   ├── q16-tatemono-bunkatsu-gappei.md 第16問 建物の分割又は合併の登記
│   ├── q17-tatemono-messitsu.md       第17問 建物の滅失の登記
│   ├── q18-kubun-tatemono.md          第18問 区分建物の登記
│   ├── q19-hikkai-tokutei.md          第19問 筆界特定
│   └── q20-chousashihou-gyoumu-kitei.md 第20問 土地家屋調査士法
└── r1-mondai/              令和元年度 午後の部の解説記事(問題ごとに1ファイル、第1問〜第20問すべて作成済み)
    ├── q01-buttenteki-seikyu.md       第1問 物権的請求権
    ├── q02-kyouyuu.md                 第2問 共有
    ├── q03-igon.md                    第3問 遺言
    ├── q04-kankatsu-touki.md          第4問 管轄登記所
    ├── q05-chimoku.md                 第5問 地目
    ├── q06-tochi-messitsu.md          第6問 土地の滅失の登記
    ├── q07-chiseki-sokuryouzu.md      第7問 地積測量図
    ├── q08-shinsei-tenpu.md           第8問 土地の表示登記の申請情報・添付情報
    ├── q09-tatemono-kosuu.md          第9問 建物の個数
    ├── q10-tatemono-zumen.md          第10問 建物図面及び各階平面図
    ├── q11-ichi-no-shinsei.md         第11問 一の申請情報による申請
    ├── q12-tatemono-bunkatsu-gappei.md 第12問 建物の分割又は合併の登記
    ├── q13-tatemono-hyoudaibu.md      第13問 建物の表題部の登記
    ├── q14-daii-shinsei.md            第14問 登記の代位申請
    ├── q15-tatemono-tenpu.md          第15問 建物の表示登記の添付情報
    ├── q16-hyouji-touki-shinsei.md    第16問 不動産の表示登記の申請
    ├── q17-chizu-teisei.md            第17問 地図等の訂正
    ├── q18-kubun-tatemono.md          第18問 区分建物の登記
    ├── q19-touki-kiroku-yomitori.md   第19問 登記記録の読み取り(合筆・分筆の履歴)
    └── q20-chousashi-gimu.md          第20問 土地家屋調査士の義務
```

令和7年度分は第1問は本シリーズでは未作成です（作業を第2問から開始したため）。令和6年度分・令和元年度分は、いずれも第1問〜第20問すべて作成済みです。

## 令和元年度分の情報ソースについて

令和元年度分（r1-mondai）は、令和6年度分と同じく、ユーザーが過去に構築した土地家屋調査士試験対策アプリの検証済みデータベースを主要な一次情報源として作成しました。

- `src/data/takuitsu.json`（問題文・肢・正解・explanationフィールドの条文根拠解説）を各記事の問題文引用と法的根拠の一次情報源とした。R01の正解番号（correctAnswer）と各肢の正誤は、`kaisetsu_plus.json` のpitfalls（`reviewed=true`、2026-06-06に独立検証済み）と突き合わせて確定した。
- `src/data/kaisetsu_plus.json`（approach/pitfalls/keyPoints）を初学者向けの具体例・考え方のヒントとして参照した。なお `approach` は初期ドラフトであり、検証済みの `pitfalls`・正解番号と食い違う箇所（例：第11問の肢ア）は `pitfalls`・正解番号を優先した。
- 全20記事について、作成後に「設問の極性（正しいもの／誤っているもの）× 正解の組合せ」から各肢の○×を機械的に導いたアンサーキーと、各記事のまとめ表・本文の判定を1問ずつ突き合わせる独立ダブルチェックを実施し、正解番号・各肢の正誤判定に食い違いがないことを確認済み。第19問は登記記録の地積計算（5番＝180.05㎡、3番2＝45.01㎡、6番＝189.94㎡→6番＞5番）を再計算して肢オの判定を検証した。
- 法務省公表の正答PDF・条文原本はこの作業環境からは直接取得できなかった（moj.go.jp等がプロキシ経由で403となるため）。条文番号・先例番号のうち原本で確認しきれなかったものは、各記事末尾の確認事項ブロックにその旨を正直に明記している。ローカルのアガルート過去問PDF等の教材も、この作業環境には存在せず参照できなかった。

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
