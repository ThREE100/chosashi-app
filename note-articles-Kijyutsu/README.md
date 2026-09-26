# note-articles-Kijyutsu

土地家屋調査士試験の**記述式**解説をnote記事にするための素材置き場です。択一式の `note-articles/` とは別体系にしています。

## フォルダ構成

```
note-articles-Kijyutsu/
├── README.md                                  このファイル
├── prompt_note-kijutsu_tochi_kyoutsu.md        共通：土地の記述式 note記事執筆プロンプト
├── prompt_toukishinseisho-gazou_kihon-form.md  共通：登記申請書 画像作成プロンプト（基本フォーム）
├── qa-checklist-kijutsu.md                    共通：記事作成後のダブルチェック指示書（PDCAの改善記録つき）
├── tools/
│   ├── calc_helpers.py                        F-789SGの計算を再現し、記事の表示値を生成・照合するヘルパー
│   └── lint_note_article.py                   note表記ルールの機械チェックと「表示：」行の一覧
├── R6/
│   └── Q21/
│       ├── note_R6_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文
│       ├── prompt_R6_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R6第21問の記入データ済み）
│       ├── prompt_R6_dai21mon_kaisetsuzu.md             解説図（筆界のずれ・B点D点・P点・地積測量図）作成プロンプト
│       └── verify_R6_dai21mon.py                        記事の数値・電卓表示の照合スクリプト
└── R7/
    └── Q21/
        ├── note_R7_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文
        ├── prompt_R7_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R7第21問の記入データ済み）
        ├── prompt_R7_dai21mon_kaisetsuzu.md             解説図（K点・地積測量図・J点L点）作成プロンプト（R7第21問の座標入り）
        └── verify_R7_dai21mon.py                        記事の数値・電卓表示の照合スクリプト
```

## 使い方

- **新しい年度・問題を追加するとき**は、直下の2本の共通プロンプトをコピーし、【令和○年度】や「記入データ」の部分だけをその年の問題に差し替えます。
- 直下の共通プロンプトそのものは、問題固有の数値を書き込まずに汎用のまま保つこと。
- 年度・問題ごとのフォルダ（`R7/Q21/` のように）には、その回の記事と、実際に埋めた値入りのプロンプト、照合スクリプトを保存します。
- 記事を書き終えたら、`qa-checklist-kijutsu.md` に従ってダブルチェックします。新しい種類の誤りが見つかったら、指示書末尾の改善記録に残し、指示書と執筆プロンプトの両方を更新します。

## 計算方法の前提

記述式の座標計算は、キヤノン F-789SG の複素数モードを前提に統一しています（詳細は共通プロンプト内）。
