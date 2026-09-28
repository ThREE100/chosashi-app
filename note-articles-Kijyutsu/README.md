# note-articles-Kijyutsu

土地家屋調査士試験の**記述式**解説をnote記事にするための素材置き場です。択一式の `note-articles/` とは別体系にしています。

第21問（土地）と第22問（建物）で記事のスタイルが異なります。

- **第21問（土地）**：講師が語りかける解説プロース形式。計算は「式（点名）・電卓操作・表示」の3点セットで厳密に示す
- **第22問（建物）**：キャラクター「トリ先生」と「藍子」の会話形式（学習コミック風note記事）。計算は要所だけを対話の中で示す軽めのスタイル

保存先の階層構造、`qa-checklist-kijutsu.md` によるダブルチェック、`main` へのコミットという運用は両方共通です。

## フォルダ構成

```
note-articles-Kijyutsu/
├── README.md                                          このファイル
├── prompt_note-kijutsu_tochi_kyoutsu.md                共通：土地(第21問)の記述式 note記事執筆プロンプト（プロース形式）
├── prompt_note-kijutsu_tatemono_kyoutsu.md             共通：建物(第22問)の記述式 note記事執筆プロンプト（会話形式）
├── prompt_toukishinseisho-gazou_kihon-form.md          共通：登記申請書 画像作成プロンプト（土地・基本フォーム）
├── prompt_toukishinseisho-gazou_kihon-form_tatemono.md 共通：登記申請書 画像作成プロンプト（建物・基本フォーム）
├── prompt_kaisetsuzu-gazou_kihon-form_tatemono.md       共通：建物の解説用インフォグラフィック 画像作成プロンプト（基本フォーム）
├── qa-checklist-kijutsu.md                             共通：記事作成後のダブルチェック指示書（土地・建物共通＋固有、PDCAの改善記録つき）
├── tools/
│   ├── calc_helpers.py                                 F-789SGの計算を再現し、記事の表示値を生成・照合するヘルパー
│   └── lint_note_article.py                            note表記ルールの機械チェックと「表示：」行の一覧
├── R3/
│   └── Q22/
│       ├── note_R3_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R3_dai22mon_kaisetsuzu.md                   解説図7枚（区分の全体像・敷地辺長図・建物図面・壁心/内法の誤り比較図・1階/2階求積図・問2の求積図）作成プロンプト
│       ├── prompt_R3_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R3_dai22mon_toukishinseisho_machigai.md     登記申請書「区分した建物の表示」の原因欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R3_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R3_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R4/
│   └── Q22/
│       ├── note_R4_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R4_dai22mon_kaisetsuzu.md                   解説図6枚（工事前後比較図・敷地辺長図・建物図面・1階/2階求積図・車庫の誤り比較図）作成プロンプト
│       ├── prompt_R4_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R4_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R4_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R4_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R5/
│   └── Q22/
│       ├── note_R5_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R5_dai22mon_kaisetsuzu.md                   解説図6枚（敷地辺長図・建物図面・1階/2階求積図・誤り比較図・工事前後比較図）作成プロンプト
│       ├── prompt_R5_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。R5第22問の記入データ済み）
│       ├── prompt_R5_dai22mon_toukishinseisho_machigai.md     登記申請書「よくある間違い」の誤答→添削→正解の3コマ画像プロンプト
│       ├── prompt_R5_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R5_dai22mon.py                              記事の数値・求積の照合スクリプト
├── R6/
│   ├── Q21/
│   │   ├── note_R6_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文
│   │   ├── prompt_R6_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R6第21問の記入データ済み）
│   │   ├── prompt_R6_dai21mon_kaisetsuzu.md             解説図（筆界のずれ・B点D点・P点・地積測量図）作成プロンプト
│   │   └── verify_R6_dai21mon.py                        記事の数値・電卓表示の照合スクリプト
│   └── Q22/
│       ├── note_R6_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R6_dai22mon_kaisetsuzu.md                   解説図6枚（出入り経路図・敷地辺長図・建物図面・1階誤り比較図・1階/2階求積図）作成プロンプト
│       ├── prompt_R6_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R6_dai22mon_toukishinseisho_machigai.md     登記申請書「共有者」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R6_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R6_dai22mon.py                              記事・付属プロンプトの数値・求積の照合スクリプト
└── R7/
    ├── Q21/
    │   ├── note_R7_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文
    │   ├── prompt_R7_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R7第21問の記入データ済み）
    │   ├── prompt_R7_dai21mon_kaisetsuzu.md             解説図（K点・地積測量図・J点L点）作成プロンプト（R7第21問の座標入り）
    │   └── verify_R7_dai21mon.py                        記事の数値・電卓表示の照合スクリプト
    └── Q22/
        ├── note_R7_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
        ├── prompt_R7_dai22mon_kaisetsuzu.md                   解説図作成プロンプト
        ├── prompt_R7_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
        ├── prompt_R7_dai22mon_toukishinseisho_machigai.md     登記申請書「よくある間違い」の誤答→添削→正解の画像プロンプト
        ├── prompt_R7_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
        └── verify_R7_dai22mon.py                              記事の数値・求積の照合スクリプト
```

## 使い方

- **新しい年度・問題を追加するとき**は、直下の共通プロンプト（土地なら `..._tochi_kyoutsu.md` 系、建物なら `..._tatemono_...` 系）をコピーし、【令和○年度】や「記入データ」の部分だけをその年の問題に差し替えます。
- 直下の共通プロンプトそのものは、問題固有の数値を書き込まずに汎用のまま保つこと。
- 年度・問題ごとのフォルダ（`R7/Q21/` のように）には、その回の記事と、実際に埋めた値入りのプロンプト、照合スクリプトを保存します。
- 記事を書き終えたら、`qa-checklist-kijutsu.md` に従ってダブルチェックします。新しい種類の誤りが見つかったら、指示書末尾の改善記録に残し、指示書と執筆プロンプトの両方を更新します。

## 計算方法の前提

記述式の座標計算は、キヤノン F-789SG の複素数モードを前提に統一しています（詳細は共通プロンプト内）。

## 学習漫画（画像パネル形式）との違い

`CHATGPT_MANGA_WORKFLOW.md`（リポジトリ直下）は、キャラクターの立ち絵入り漫画**画像**をChatGPTの画像生成機能で1ページずつ作る別のワークフローで、素材・成果物はこのリポジトリの外（OneDrive）で管理している。本フォルダ（`note-articles-Kijyutsu/`）の記事は、画像パネルではなく**テキストのnote記事**（会話形式でも文章主体）であり、挿絵は本文中に生成箇所を明示するだけで、記事自体はこのリポジトリにそのままコミットする。
