# note-articles-Kijyutsu

土地家屋調査士試験の**記述式**解説をnote記事にするための素材置き場です。択一式の `note-articles/` とは別体系にしています。

第21問（土地）と第22問（建物）で記事のスタイルが異なります。

- **第21問（土地）**：講師が語りかける解説プロース形式。計算は「式（点名）・電卓操作・表示」の3点セットで厳密に示す
- **第22問（建物）**：キャラクター「トリ先生」と「藍子」の会話形式（学習コミック風note記事）。計算は要所だけを対話の中で示す軽めのスタイル
- **第21問（土地）の会話形式（2026-09-29、R7/Q21から）**：第22問と同じキャラクター・体裁で、計算は土地の3点セット（式・電卓操作・表示）を会話の間に置いて省略しない。執筆は `prompt_note-kijutsu_tochi_kaiwa_kyoutsu.md`、別チャットへの依頼文は `irai-bun_tochi_shinki-nendo.md`。解説図は解答ごとに1枚、`prompt_kaisetsuzu-gazou_kihon-form_tochi.md` から作る

保存先の階層構造、`qa-checklist-kijutsu.md` によるダブルチェック、`main` へのコミットという運用は両方共通です。

## フォルダ構成

```
note-articles-Kijyutsu/
├── README.md                                          このファイル
├── prompt_note-kijutsu_tochi_kyoutsu.md                共通：土地(第21問)の記述式 note記事執筆プロンプト（プロース形式）
├── prompt_note-kijutsu_tochi_kaiwa_kyoutsu.md          共通：土地(第21問)の記述式 note記事執筆プロンプト（会話形式・各年度共通）
├── prompt_note-kijutsu_tatemono_kyoutsu.md             共通：建物(第22問)の記述式 note記事執筆プロンプト（会話形式）
├── prompt_toukishinseisho-gazou_kihon-form.md          共通：登記申請書 画像作成プロンプト（土地・基本フォーム）
├── prompt_toukishinseisho-gazou_kihon-form_tatemono.md 共通：登記申請書 画像作成プロンプト（建物・基本フォーム）
├── prompt_kaisetsuzu-gazou_kihon-form_tatemono.md       共通：建物の解説用インフォグラフィック 画像作成プロンプト（基本フォーム）
├── prompt_kaisetsuzu-gazou_kihon-form_tochi.md          共通：土地の解説用インフォグラフィック 作図プロンプト（基本フォーム。座標から作図、解答ごとに1枚、文字の重なり検査つき）
├── qa-checklist-kijutsu.md                             共通：記事作成後のダブルチェック指示書（土地・建物共通＋固有、PDCAの改善記録つき）
├── irai-bun_tatemono_shinki-nendo.md                  共通：新しい年度の第22問（建物）記事を別チャットで作らせるときに貼る依頼文（年度の1行だけ書き換えて使う）
├── irai-bun_tochi_shinki-nendo.md                     共通：新しい年度の第21問（土地）会話形式記事を別チャットで作らせるときに貼る依頼文（年度の1行だけ書き換えて使う）
├── tools/
│   ├── calc_helpers.py                                 F-789SGの計算を再現し、記事の表示値を生成・照合するヘルパー
│   ├── zu_helpers.py                                   土地の解説図の作図ヘルパー（座標どおりの作図、辺長・点名・座標の吹き出しの自動配置、重なりの自動検査）
│   └── lint_note_article.py                            note表記ルールの機械チェックと「表示：」行の一覧
├── H25/
│   └── Q22/
│       ├── note_H25_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた版〉と照合済み）
│       ├── prompt_H25_dai22mon_kaisetsuzu.md                  解説図8枚（時系列と3つの建物の行き先・敷地辺長図・所在の誤り比較図・建物図面・1階求積図・2階の誤り比較図・2階求積図・附属建物の増改築前後図）作成プロンプト
│       ├── prompt_H25_dai22mon_toukishinseisho_gazou.md       答案用紙の画像プロンプト（完成形3枚。第1欄・第2欄の登記申請書、第3欄の説明）
│       ├── prompt_H25_dai22mon_toukishinseisho_machigai.md    第2欄「所在」「申請人」の誤答→添削→正解の画像プロンプト
│       ├── prompt_H25_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H25_dai22mon.py                             記事・付属プロンプトの数値・求積・所在の判定・体裁の照合スクリプト
├── H26/
│   └── Q22/
│       ├── note_H26_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例〈改題版〉と照合済み）
│       ├── prompt_H26_dai22mon_kaisetsuzu.md                  解説図7枚（時系列図・主従比較図・敷地辺長図・建物図面・1階と附属の求積図・2階の誤り比較図・2階求積図）作成プロンプト
│       ├── prompt_H26_dai22mon_toukishinseisho_gazou.md       登記申請書等の画像プロンプト（完成形3枚。第1欄・第2欄、第4欄、第3欄）
│       ├── prompt_H26_dai22mon_toukishinseisho_machigai.md    第2欄「登記の目的」「登記原因及びその日付」の誤答→添削→正解の画像プロンプト
│       ├── prompt_H26_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H26_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── H27/
│   └── Q22/
│       ├── note_H27_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H27_dai22mon_kaisetsuzu.md                  解説図7枚（区分の全体像・敷地辺長図・建物図面・2階求積図・3階の誤り比較図・3階求積図・1階求積図）作成プロンプト
│       ├── prompt_H27_dai22mon_toukishinseisho_gazou.md       答案用紙（第1欄・第2欄）の画像プロンプト（完成形。区分した建物の表示（イ）（ロ）・敷地権の表示「記載不要」）
│       ├── prompt_H27_dai22mon_toukishinseisho_machigai.md    登記申請書「敷地権の表示」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_H27_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H27_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── H28/
│   └── Q22/
│       ├── note_H28_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H28_dai22mon_kaisetsuzu.md                  解説図7枚（出入り経路図・階の数え方の誤り比較図・敷地辺長図・建物図面・1階/2階/3階求積図）作成プロンプト
│       ├── prompt_H28_dai22mon_toukishinseisho_gazou.md       登記申請書画像プロンプト（完成形）
│       ├── prompt_H28_dai22mon_toukishinseisho_machigai.md    登記申請書「構造」「床面積」欄（渡廊下付き・1階の書き漏れ）の誤答→添削→正解の画像プロンプト
│       ├── prompt_H28_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H28_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── H29/
│   └── Q22/
│       ├── note_H29_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H29_dai22mon_kaisetsuzu.md                  解説図6枚（分割の前後比較図・敷地辺長図・建物図面・甲建物の求積図・丙建物の誤り比較図・丙建物の求積図）作成プロンプト
│       ├── prompt_H29_dai22mon_toukishinseisho_gazou.md       答案用紙の第1欄（問1）と登記申請書（第2欄）の画像プロンプト（完成形2枚）
│       ├── prompt_H29_dai22mon_toukishinseisho_machigai.md    登記申請書「所在」欄と附属建物の符号の誤答→添削→正解の画像プロンプト
│       ├── prompt_H29_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H29_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── H30/
│   └── Q22/
│       ├── note_H30_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H30_dai22mon_kaisetsuzu.md                  解説図6枚（工事前後比較図・敷地辺長図・建物図面・1階の誤り比較図・1階/2階求積図）作成プロンプト
│       ├── prompt_H30_dai22mon_toukishinseisho_gazou.md       登記申請書画像プロンプト（完成形。所有権登記の表示・存続登記の表を含む）
│       ├── prompt_H30_dai22mon_toukishinseisho_machigai.md    登記申請書「申請人」欄・存続登記「目的となる権利」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_H30_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H30_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R1/
│   └── Q22/
│       ├── note_R1_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R1_dai22mon_kaisetsuzu.md                   解説図6枚（構成図・敷地確認図・建物図面・甲の誤り比較図・甲の求積図・駐車場の誤り比較図）作成プロンプト
│       ├── prompt_R1_dai22mon_toukishinseisho_gazou.md        登記申請書（第1欄）・第2欄の画像プロンプト（完成形）
│       ├── prompt_R1_dai22mon_toukishinseisho_machigai.md     登記申請書「敷地権の表示」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R1_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R1_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R2/
│   ├── Q21/
│   │   ├── note_R2_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R2_dai21mon_kaiwa_kaisetsuzu.md       解説図7枚（全体図・B点の座標変換・G点H点の長方形・公差の判定・分合筆の流れ・登記識別情報の整理・地積測量図）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_R2_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地分合筆登記）
│   │   ├── prompt_R2_dai21mon_toukishinseisho_machigai.md  登記申請書「土地の表示」欄（（イ）107.68→107.73、合筆後156.53→156.12）の誤答→添削→正解の画像プロンプト
│   │   ├── prompt_R2_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R2_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図7枚のPNGと作図スクリプト draw_R2_dai21mon_kaisetsuzu.py
│   └── Q22/
│       ├── note_R2_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R2_dai22mon_kaisetsuzu.md                   解説図6枚作成プロンプト
│       ├── prompt_R2_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。第1欄の滅失登記・第3欄の表題登記）
│       ├── prompt_R2_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R2_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R2_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R3/
│   ├── Q21/
│   │   ├── note_R3_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み。相続人の1人が他の相続人に代位する分筆）
│   │   ├── prompt_R3_dai21mon_kaiwa_kaisetsuzu.md       解説図10枚（全体図・A点・C点・H点・L点・地図に準ずる図面・公差・分筆の地番・代位の関係図・地積測量図）作成プロンプト
│   │   ├── prompt_R3_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。答案用紙どおり登録免許税が申請人の枠より前）
│   │   ├── prompt_R3_dai21mon_toukishinseisho_machigai.md  登記申請書「添付書類」欄と申請人の枠（代位）の誤答→添削→正解の画像プロンプト
│   │   ├── prompt_R3_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R3_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図10枚のPNGと、作図スクリプト draw_R3_dai21mon_kaisetsuzu.py
│   └── Q22/
│       ├── note_R3_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R3_dai22mon_kaisetsuzu.md                   解説図7枚（区分の全体像・敷地辺長図・建物図面・壁心/内法の誤り比較図・1階/2階求積図・問2の求積図）作成プロンプト
│       ├── prompt_R3_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R3_dai22mon_toukishinseisho_machigai.md     登記申請書「区分した建物の表示」の原因欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R3_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R3_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R4/
│   ├── Q21/
│   │   ├── note_R4_dai21mon_tochi_kaiwa_kaisetsu.md      note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R4_dai21mon_kaiwa_kaisetsuzu.md        解説図10枚（全体図・AB線とEFGの比較・合成図の裏付け・P点・I点J点・筆界特定・公差・分筆と地番・地積測量図・本人確認情報）作成プロンプト
│   │   ├── prompt_R4_dai21mon_toukishinseisho_gazou.md   登記申請書画像プロンプト（完成形。土地一部地目変更・分筆登記）
│   │   ├── prompt_R4_dai21mon_toukishinseisho_machigai.md  登記申請書「登記の目的」と（イ）（ロ）の行の誤答→添削→正解の画像プロンプト
│   │   ├── prompt_R4_dai21mon_miidashi_gazou.md           note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R4_dai21mon_kaiwa.py                   記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                           解説図10枚のPNGと、作図スクリプト draw_R4_dai21mon_kaisetsuzu.py
│   └── Q22/
│       ├── note_R4_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R4_dai22mon_kaisetsuzu.md                   解説図6枚（工事前後比較図・敷地辺長図・建物図面・1階/2階求積図・車庫の誤り比較図）作成プロンプト
│       ├── prompt_R4_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R4_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R4_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R4_dai22mon.py                              記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── R5/
│   ├── Q21/
│   │   ├── note_R5_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R5_dai21mon_kaiwa_kaisetsuzu.md       解説図8枚（全体図・筆界点F/Jの比較・B点・H点・分筆の区画の比較・地積測量図・分合筆・職権の分合筆）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_R5_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。地目変更・分合筆）
│   │   ├── prompt_R5_dai21mon_toukishinseisho_machigai.md  登記申請書「添付書類」欄と分合筆後の1番1の行の誤答→添削→正解の画像プロンプト
│   │   ├── prompt_R5_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R5_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図8枚のPNGと、作図スクリプト draw_R5_dai21mon_kaisetsuzu.py
│   └── Q22/
│       ├── note_R5_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R5_dai22mon_kaisetsuzu.md                   解説図6枚（敷地辺長図・建物図面・1階/2階求積図・誤り比較図・工事前後比較図）作成プロンプト
│       ├── prompt_R5_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。R5第22問の記入データ済み）
│       ├── prompt_R5_dai22mon_toukishinseisho_machigai.md     登記申請書「よくある間違い」の誤答→添削→正解の3コマ画像プロンプト
│       ├── prompt_R5_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R5_dai22mon.py                              記事の数値・求積の照合スクリプト
├── R6/
│   ├── Q21/
│   │   ├── note_R6_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文（プロース形式。アガルート解答例と照合済み）
│   │   ├── note_R6_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み。筆界の判断・P点・乙土地の分筆・地図に準ずる図面の訂正）
│   │   ├── prompt_R6_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R6第21問の記入データ済み。プロース版・会話形式で共用）
│   │   ├── prompt_R6_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」欄と「土地の表示」1行目の誤答→添削→正解の画像プロンプト（会話形式用）
│   │   ├── prompt_R6_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（会話形式用、1280×670px）
│   │   ├── prompt_R6_dai21mon_kaisetsuzu.md             解説図（筆界のずれ・B点D点・P点・地積測量図）作成プロンプト（プロース版用）
│   │   ├── prompt_R6_dai21mon_kaiwa_kaisetsuzu.md       解説図9枚（全体図・B点・D点・筆界の判断・P点・必要な登記・分筆の地番・地積測量図・地図訂正の申出）作成プロンプト（会話形式用。土地の基本フォームの記入済み）
│   │   ├── verify_R6_dai21mon.py                        記事の数値・電卓表示の照合スクリプト（プロース版）
│   │   ├── verify_R6_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト（会話形式）
│   │   └── zu/                                          解説図9枚のPNGと、作図スクリプト draw_R6_dai21mon_kaisetsuzu.py
│   └── Q22/
│       ├── note_R6_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R6_dai22mon_kaisetsuzu.md                   解説図6枚（出入り経路図・敷地辺長図・建物図面・1階誤り比較図・1階/2階求積図）作成プロンプト
│       ├── prompt_R6_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R6_dai22mon_toukishinseisho_machigai.md     登記申請書「共有者」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R6_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_R6_dai22mon.py                              記事・付属プロンプトの数値・求積の照合スクリプト
└── R7/
    ├── Q21/
    │   ├── note_R7_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文（プロース形式。アガルート解答例と照合済み）
    │   ├── note_R7_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。答えはプロース版と同じ。L点は延長線の交点の相似で解く）
    │   ├── prompt_R7_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R7第21問の記入データ済み）
    │   ├── prompt_R7_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」「添付書類」欄の誤答→添削→正解の画像プロンプト（会話形式用）
    │   ├── prompt_R7_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（会話形式用、1280×670px）
    │   ├── prompt_R7_dai21mon_kaisetsuzu.md             解説図（K点・地積測量図・J点L点）作成プロンプト（プロース版用、R7第21問の座標入り）
    │   ├── prompt_R7_dai21mon_kaiwa_kaisetsuzu.md       解説図9枚（全体図・D点・筆界の比較・K点・公差・地積測量図・J点・L点・分筆の地番）作成プロンプト（会話形式用。土地の基本フォームの記入済み見本）
    │   ├── verify_R7_dai21mon.py                        記事の数値・電卓表示の照合スクリプト（プロース版）
    │   ├── verify_R7_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト（会話形式）
    │   └── zu/                                          解説図9枚のPNGと、作図の参照実装 draw_R7_dai21mon_kaisetsuzu.py
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
- **第22問（建物）の新しい年度を別チャットで作らせるとき**は、`irai-bun_tatemono_shinki-nendo.md` の依頼文を、冒頭の【対象年度】の1行だけ書き換えて貼り付けます。
- **第21問（土地）の会話形式の新しい年度を別チャットで作らせるとき**は、`irai-bun_tochi_shinki-nendo.md` の依頼文を、同じく【対象年度】の1行だけ書き換えて貼り付けます。
- 直下の共通プロンプトそのものは、問題固有の数値を書き込まずに汎用のまま保つこと。
- 年度・問題ごとのフォルダ（`R7/Q21/` のように）には、その回の記事と、実際に埋めた値入りのプロンプト、照合スクリプトを保存します。
- 記事を書き終えたら、`qa-checklist-kijutsu.md` に従ってダブルチェックします。新しい種類の誤りが見つかったら、指示書末尾の改善記録に残し、指示書と執筆プロンプトの両方を更新します。

## 計算方法の前提

記述式の座標計算は、キヤノン F-789SG の複素数モードを前提に統一しています（詳細は共通プロンプト内）。

## 学習漫画（画像パネル形式）との違い

`CHATGPT_MANGA_WORKFLOW.md`（リポジトリ直下）は、キャラクターの立ち絵入り漫画**画像**をChatGPTの画像生成機能で1ページずつ作る別のワークフローで、素材・成果物はこのリポジトリの外（OneDrive）で管理している。本フォルダ（`note-articles-Kijyutsu/`）の記事は、画像パネルではなく**テキストのnote記事**（会話形式でも文章主体）であり、挿絵は本文中に生成箇所を明示するだけで、記事自体はこのリポジトリにそのままコミットする。
