# 土地家屋調査士試験 note解説記事

土地家屋調査士試験の過去問（択一式、ア〜オの5肢問題）を、note投稿用に初学者向けに解説した記事一式です。Claude Codeとの対話の中で、法務省公表の試験問題原本・正答資料、条文、実務解説サイトを都度確認しながら作成しています。

## フォルダ構成

```
note-articles/
├── README.md               このファイル
├── format-template.md      note記事の執筆フォーマット(固定テンプレート)
├── generate-prompt.md      新しい問題の記事を生成するためのプロンプトテンプレート
├── tools/
│   └── md_to_mt.py         note.comインポート用(MT形式)への一括変換スクリプト
├── exports/                md_to_mt.pyで変換済みのnote.comインポート用ファイル
│   ├── r6-mondai.mt.txt
│   ├── r7-mondai.mt.txt
│   └── h27-mondai.mt.txt
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
└── h27-mondai/             平成27年度 午後の部の解説記事(問題ごとに1ファイル、第1問〜第20問すべて作成済み)
    ├── q01-sagi-kyouhaku.md           第1問 詐欺又は強迫による意思表示
    ├── q02-kyouyuu.md                 第2問 共有
    ├── q03-igon.md                    第3問 遺言
    ├── q04-shinsei-jouhou.md          第4問 申請情報の内容
    ├── q05-hyoudaibu-shoyuusha.md     第5問 表題部所有者の登記
    ├── q06-tochi-hyouji-tenpu.md      第6問 土地の表示登記の申請情報又は添付情報
    ├── q07-tochi-hyoudai.md           第7問 土地の表題登記
    ├── q08-chiban.md                  第8問 土地の地番又は地番区域
    ├── q09-gappitsu.md                第9問 合筆の登記
    ├── q10-chizu-teisei.md            第10問 地図の訂正
    ├── q11-daii-shinsei.md            第11問 登記の代位申請
    ├── q12-kankatsu-toukisho.md       第12問 建物の管轄登記所
    ├── q13-tatemono-nintei.md         第13問 建物の認定
    ├── q14-tatemono-hyoudai.md        第14問 建物の表題登記
    ├── q15-kubun-tatemono.md          第15問 区分建物の表示に関する登記
    ├── q16-shikichiken.md             第16問 敷地権
    ├── q17-kyouyoububun.md            第17問 共用部分である旨の登記
    ├── q18-hozon-kikan.md             第18問 登記所に保存される情報の保存期間
    ├── q19-chousashihou-kyoukai.md    第19問 境界紛争（対話形式）
    └── q20-chousashihou-gyoumu.md     第20問 土地家屋調査士又は調査士法人の業務
```

令和7年度分は第1問は本シリーズでは未作成です（作業を第2問から開始したため）。令和6年度分・平成27年度分は第1問〜第20問すべて作成済みです。

## 令和6年度分の情報ソースについて

令和6年度分（r6-mondai）は、法務省公表資料に加えて、ユーザーが過去に構築した土地家屋調査士試験対策アプリのデータベースを主要な一次情報源として作成しました。

- `takuitsu.json`（問題文・肢・正解・explanationフィールドの詳細な条文根拠解説）を各記事の法的根拠の一次情報源とした。
- `kaisetsu_plus.json`（approach/pitfalls/keyPointsの補足解説）を初学者向けの具体例作成のヒントとして参照した。
- ローカルに保存されているアガルートの教材（`土地家屋調査士_アガルート`フォルダ）も確認したが、択一式については講義動画のチャプター一覧（対照表PDF）のみで、個別問題のテキスト解説は含まれていなかったため、参照できなかった。
- 全20記事について、作成後に法務省公式の正解表（PDF）と条文（e-Gov法令検索等）を用いた独立したダブルチェックを実施し、正解番号・各肢の正誤判定に誤りがないことを確認済み。

## 平成27年度分の情報ソースについて

平成27年度分（h27-mondai）は、r6-mondaiと同じくアプリの検証済みデータベース（`takuitsu.json`のexplanationフィールド、`kaisetsu_plus.json`のapproach/pitfalls/keyPointsフィールド）を主要な一次情報源として作成しました。

- 全20記事について、正解番号・各肢（ア〜オ）の正誤判定を`takuitsu.json`のcorrectAnswer・combosフィールドおよびexplanationフィールド中の「○/×」表記と突き合わせ、記事本文・まとめ表・正解表記の間で矛盾がないことをプログラムで機械的に検証済みです。
- データベース内に、同じ問題について`explanation`フィールドと`kaisetsu_plus`フィールドの記載が食い違う箇所が3問（第12問・第17問・第20問）で見つかりました。いずれも、条文・先例番号を明示している`explanation`フィールドの記載を優先して採用し、食い違いがあった旨を該当記事の確認事項ブロックに明記しています。
- **今回のセッションでは、環境のネットワーク制限により法務省公式サイト・外部の過去問解説サイトへのアクセスができず（すべて403エラー）、r6-mondaiで実施したような法務省公式PDF・e-Gov法令検索を用いた外部からの独立したダブルチェックは実施できていません。** 正解番号・各肢の正誤判定は、アプリの検証済みデータベース内での整合性確認にとどまります。将来的にネットワークアクセスが可能なセッションで、法務省公式の正解表・条文との照合を追加で行うことを推奨します。
- ローカルのアガルート教材PDF・テキストファイルについては、リポジトリ内を検索しましたが該当フォルダは見つからず、参照できませんでした（`takuitsu.json`のexplanationフィールド自体がアガルート教材のOCRテキストに由来するとみられる内容を含んでいます）。

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

## note.comへのインポート方法

各年度フォルダの記事をまとめてnote.comに下書きとしてインポートしたい場合は、`tools/md_to_mt.py` を使用します。

```
python tools/md_to_mt.py <記事フォルダ> [出力ファイル]
# 例: python tools/md_to_mt.py h27-mondai exports/h27-mondai.mt.txt
```

- 出力はMT(Movable Type)形式のテキストファイルで、note.comのインポート機能にそのまま読み込めます。
- 「このまま使える点／使う前に確認したい点」ブロック(確認事項ブロック・重複出題チェックのメモを含む)は執筆時の内部メモのため、出力からは除外されます。読者向けの本文には含まれません。
- インポートされた記事はすべて下書き(Draft)状態になります。内容を確認したうえで、note.com側で公開操作をしてください。
- 新しい年度のフォルダができたら、同じスクリプトをそのまま再利用できます。`exports/` フォルダに変換済みファイルを追加し、上記のフォルダ構成にも追記してください。
