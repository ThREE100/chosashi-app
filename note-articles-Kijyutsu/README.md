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
│   ├── zu_helpers.py                                   土地の解説図の作図ヘルパー（座標どおりの作図、境界標の記号〈コンクリート杭・金属標・石杭・基準点〉、辺長・点名・座標の吹き出しの自動配置、重なりの自動検査）
│   └── lint_note_article.py                            note表記ルールの機械チェックと「表示：」行の一覧
├── H24/
│   └── Q22/
│       ├── note_H24_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた改題版〉と照合済み。代位による区分建物表題登記・縦割りの内法・分有なら敷地権なし）
│       ├── prompt_H24_dai22mon_kaisetsuzu.md                  解説図9枚（全体像と代位の関係・敷地辺長図・建物図面・1階の誤り比較図・1階求積図・2階求積図・各階平面図の完成形・敷地権の比較図・本番で解く順番）作成プロンプト
│       ├── prompt_H24_dai22mon_toukishinseisho_gazou.md       登記申請書（第1欄。敷地権の目的である土地の表示に斜線が印刷済み）と第2欄の画像プロンプト
│       ├── prompt_H24_dai22mon_toukishinseisho_machigai.md    一棟の建物の表示「所在」の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│       ├── prompt_H24_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_H24_dai22mon.py                             記事・付属プロンプト・生成画像の数値・求積・所在の確認・解答例との一致・体裁の照合スクリプト
│       └── zu/                                                解説図9枚のPNGと作図スクリプト draw_H24_dai22mon_kaisetsuzu.py（fit(..., pad_aspect=True)）、登記申請書の完成形（縦長1200px）・第2欄の完成形・添削画像（縦3コマ）のPNG・HTMLと生成スクリプト make_H24_dai22mon_shinseisho_gazou.py
├── H25/
│   ├── Q21/
│   │   ├── note_H25_dai21mon_tochi_kaiwa_kaisetsu.md    note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた版〉と照合済み。B点の放射・F点の正弦定理・一部地目変更・分筆）
│   │   ├── prompt_H25_dai21mon_kaiwa_kaisetsuzu.md      解説図7枚（全体図・B点の放射・F点の正弦定理・C点とE点の裏付け・一筆に地目は一つ・分筆後の区画と地番・地積測量図）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H25_dai21mon_toukishinseisho_gazou.md 登記申請書画像プロンプト（完成形。土地一部地目変更・分筆登記）
│   │   ├── prompt_H25_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」欄と土地の表示（イ）（ロ）の行の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H25_dai21mon_miidashi_gazou.md         note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H25_dai21mon_kaiwa.py                 記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図7枚のPNGと作図スクリプト draw_H25_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削（縦長）のPNG・HTMLと生成スクリプト make_H25_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H25_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた版〉と照合済み）
│       ├── prompt_H25_dai22mon_kaisetsuzu.md                  解説図8枚（時系列と3つの建物の行き先・敷地辺長図・所在の誤り比較図・建物図面・1階求積図・2階の誤り比較図・2階求積図・附属建物の増改築前後図）作成プロンプト
│       ├── prompt_H25_dai22mon_toukishinseisho_gazou.md       答案用紙の画像プロンプト（完成形3枚。第1欄・第2欄の登記申請書、第3欄の説明）
│       ├── prompt_H25_dai22mon_toukishinseisho_machigai.md    第2欄「所在」「申請人」の誤答→添削→正解の画像プロンプト
│       ├── prompt_H25_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H25_dai22mon.py                             記事・付属プロンプトの数値・求積・所在の判定・体裁の照合スクリプト
├── H26/
│   ├── Q21/
│   │   ├── note_H26_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた改題版〉と照合済み。放射3点・直線上の点・地役権のある承役地の分合筆・100番5の甲区と乙区）
│   │   ├── prompt_H26_dai21mon_kaiwa_kaisetsuzu.md       解説図12枚（全体図・P点・D点・E点の放射・V点・W点・公差の判断・（イ）（ロ）の面積・分合筆の前後・甲区と乙区の整理図・地積測量図・本番で解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H26_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地分合筆登記。答案用紙どおり「添付情報（略）」・登録免許税が代理人の下・最下欄に地役権設定の範囲）
│   │   ├── prompt_H26_dai21mon_toukishinseisho_machigai.md  合筆後の100番5の行と最下欄（地役権設定の範囲）の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H26_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H26_dai21mon_kaiwa.py                  記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図12枚のPNGと作図スクリプト draw_H26_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削（縦長）のPNG・HTMLと生成スクリプト make_H26_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H26_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例〈改題版〉と照合済み）
│       ├── prompt_H26_dai22mon_kaisetsuzu.md                  解説図7枚（時系列図・主従比較図・敷地辺長図・建物図面・1階と附属の求積図・2階の誤り比較図・2階求積図）作成プロンプト
│       ├── prompt_H26_dai22mon_toukishinseisho_gazou.md       登記申請書等の画像プロンプト（完成形3枚。第1欄・第2欄、第4欄、第3欄）
│       ├── prompt_H26_dai22mon_toukishinseisho_machigai.md    第2欄「登記の目的」「登記原因及びその日付」の誤答→添削→正解の画像プロンプト
│       ├── prompt_H26_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       └── verify_H26_dai22mon.py                             記事・付属プロンプトの数値・求積・体裁の照合スクリプト
├── H27/
│   ├── Q21/
│   │   ├── note_H27_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例〈日付を平成30年に置き換えた改題版〉と照合済み）
│   │   ├── prompt_H27_dai21mon_kaiwa_kaisetsuzu.md       解説図11枚（全体図・A点の放射・K点・H点・登記の対象となる土地の整理図・分筆後の区画と地番・土地所在図兼地積測量図・注の仕分け・K点とH点の別解・（ロ）の対角線の別解・解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H27_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地一部地目変更・分筆登記。答案用紙どおり「添付情報」・所在2段）
│   │   ├── prompt_H27_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」欄と（ロ）の行の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H27_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H27_dai21mon_kaiwa.py                  記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図11枚のPNGと作図スクリプト draw_H27_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削（縦長）のPNG・HTMLと生成スクリプト make_H27_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H27_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H27_dai22mon_kaisetsuzu.md                  解説図9枚（区分の全体像・敷地辺長図・建物図面・2階求積図・3階の誤り比較図・3階求積図・1階求積図・各階平面図の完成形・本番で解く順番）作成プロンプト
│       ├── prompt_H27_dai22mon_toukishinseisho_gazou.md       第1欄の完成形と登記申請書（第2欄）の完成形の画像プロンプト（区分した建物の表示（イ）（ロ）・敷地権の表示「記載不要」。左の列→右の列を縦に積んだ縦長）
│       ├── prompt_H27_dai22mon_toukishinseisho_machigai.md    登記申請書「敷地権の表示」欄の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│       ├── prompt_H27_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_H27_dai22mon.py                             記事・付属プロンプト・生成画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図9枚のPNGと作図スクリプト draw_H27_dai22mon_kaisetsuzu.py、第1欄・登記申請書の完成形・添削（縦長）のPNG・HTMLと生成スクリプト make_H27_dai22mon_shinseisho_gazou.py
├── H28/
│   ├── Q21/
│   │   ├── note_H28_dai21mon_tochi_kaiwa_kaisetsu.md    note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_H28_dai21mon_kaiwa_kaisetsuzu.md      解説図11枚（全体図・D点の放射・J点の交点・筆界点の裏付けと（イ）（ロ）の面積・戊土地の2筆・取得原因と登記原因の整理図・分合筆の前後・地積測量図・J点の別解・注の仕分け・本番で解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H28_dai21mon_toukishinseisho_gazou.md 登記申請書画像プロンプト（完成形。土地分合筆登記。項目の順序は平成28年度の答案用紙どおり）
│   │   ├── prompt_H28_dai21mon_toukishinseisho_machigai.md  登記申請書「登録免許税」欄と合筆後の32番1の行の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H28_dai21mon_miidashi_gazou.md         note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H28_dai21mon_kaiwa.py                 記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                         解説図11枚のPNGと作図スクリプト draw_H28_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像のPNG・HTMLと生成スクリプト make_H28_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H28_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H28_dai22mon_kaisetsuzu.md                  解説図8枚（出入り経路図・階の数え方の誤り比較図・敷地辺長図・建物図面・1階/2階/3階求積図・本番で解く順番）作成プロンプト
│       ├── prompt_H28_dai22mon_toukishinseisho_gazou.md       登記申請書画像プロンプト（完成形。第2欄〈問2の記述〉の画像も）
│       ├── prompt_H28_dai22mon_toukishinseisho_machigai.md    登記申請書「構造」「床面積」欄（渡廊下付き・1階の書き漏れ）の誤答→添削→正解の画像プロンプト
│       ├── prompt_H28_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_H28_dai22mon.py                             記事・付属プロンプト・画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                画像（解説図8枚・登記申請書の完成形・添削・第2欄のPNGとHTML、作図・書き出しスクリプト）
├── H29/
│   ├── Q21/
│   │   ├── note_H29_dai21mon_tochi_kaiwa_kaisetsu.md    note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_H29_dai21mon_kaiwa_kaisetsuzu.md      解説図11枚（全体図・C点の放射・H点・I点〈直角に1.00m離れた平行線、拡大図つき〉・公差の判定・合筆後の分筆の区画・地積測量図・注の仕分け・H点とI点の別解〈FGからの離れの比例〉・（ロ）の対角線・本番で解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H29_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地地積更正・分筆登記、相続人2人による申請）
│   │   ├── prompt_H29_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」欄と分筆前の行の地積の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H29_dai21mon_miidashi_gazou.md         note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H29_dai21mon_kaiwa.py                  記事・付属プロンプト・生成済みの申請書画像の数値・体裁の照合スクリプト
│   │   └── zu/                                           解説図11枚のPNGと作図スクリプト draw_H29_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像のPNG・HTMLと生成スクリプト make_H29_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H29_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H29_dai22mon_kaisetsuzu.md                  解説図7枚（分割の前後比較図・敷地辺長図・建物図面・甲建物の求積図・丙建物の誤り比較図・丙建物の求積図・本番で解く順番）作成プロンプト
│       ├── prompt_H29_dai22mon_toukishinseisho_gazou.md       答案用紙の第1欄（問1）と登記申請書（第2欄）の画像プロンプト（完成形2枚）
│       ├── prompt_H29_dai22mon_toukishinseisho_machigai.md    登記申請書「所在」欄と附属建物の符号の誤答→添削→正解の画像プロンプト
│       ├── prompt_H29_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_H29_dai22mon.py                             記事・付属プロンプト・生成済みの画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図7枚（図7は本番で解く順番）のPNGと作図スクリプト draw_H29_dai22mon_kaisetsuzu.py（fit(..., pad_aspect=True)）、第1欄の完成形・登記申請書の完成形（縦長1200px）・添削（縦3コマ）のPNG・HTMLと生成スクリプト make_H29_dai22mon_shinseisho_gazou.py
├── H30/
│   ├── Q21/
│   │   ├── note_H30_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。2026-09-29に出題当初の試験問題の本文から作り直し、同日アガルートの解答例と直接照合済み。原点をずらした座標・放射のD点・延長線の交点のI点・筆界の定義〈エ＝意思〉・土地一部地目変更・分筆登記）
│   │   ├── prompt_H30_dai21mon_kaiwa_kaisetsuzu.md       解説図11枚（全体図・D点・I点・甲土地の面積の裏付け・筆界の定義・必要な登記の判断・公差・分筆後の区画と地番・地積測量図・帯の面積の別解〈対角線2本〉・本番の解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_H30_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。答案用紙どおり登録免許税が申請人より前、記入行4行）
│   │   ├── prompt_H30_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」欄と（イ）（ロ）の行の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_H30_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_H30_dai21mon_kaiwa.py                  記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図11枚のPNGと作図スクリプト draw_H30_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削（縦長）のPNG・HTMLと生成スクリプト make_H30_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_H30_dai22mon_tatemono_kaisetsu.md             note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_H30_dai22mon_kaisetsuzu.md                  解説図7枚（工事前後比較図・敷地辺長図・建物図面・1階の誤り比較図・1階/2階求積図・本番で解く順番）作成プロンプト
│       ├── prompt_H30_dai22mon_toukishinseisho_gazou.md       登記申請書画像プロンプト（完成形。所有権登記の表示・存続登記の表を含む。第1欄（その2）・第2欄は別の画像）
│       ├── prompt_H30_dai22mon_toukishinseisho_machigai.md    登記申請書「申請人」欄・存続登記「目的となる権利」欄の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│       ├── prompt_H30_dai22mon_miidashi_gazou.md               note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_H30_dai22mon.py                             記事・付属プロンプト・生成画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図7枚のPNGと作図スクリプト draw_H30_dai22mon_kaisetsuzu.py、登記申請書の完成形・第1欄（その2）・第2欄・添削（縦長）のPNG・HTMLと生成スクリプト make_H30_dai22mon_shinseisho_gazou.py
├── R1/
│   ├── Q21/
│   │   ├── note_R1_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み。地積更正・分筆、家庭菜園は宅地、筆界特定の対象土地・関係土地・関係人）
│   │   ├── prompt_R1_dai21mon_kaiwa_kaisetsuzu.md       解説図13枚（全体図・D点・G点〈垂線の足〉・対象土地と関係土地・関係人・分筆後の地積・公差・地目・地積測量図・G点の別解・対角線の別解・注の仕分け・解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_R1_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地地積更正・分筆登記。答案用紙どおり登録免許税・申請人が申請日より前）
│   │   ├── prompt_R1_dai21mon_toukishinseisho_machigai.md  登記申請書「登記の目的」と（イ）の行の誤答→添削→正解の画像プロンプト（3コマ縦積み）
│   │   ├── prompt_R1_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R1_dai21mon_kaiwa.py                  記事・付属プロンプト・生成画像の数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図13枚のPNGと作図スクリプト draw_R1_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像（PNG・HTML）と生成スクリプト make_R1_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R1_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R1_dai22mon_kaisetsuzu.md                   解説図7枚（構成図・敷地確認図・建物図面・甲の誤り比較図・甲の求積図・駐車場の誤り比較図・解く順番）作成プロンプト
│       ├── prompt_R1_dai22mon_toukishinseisho_gazou.md        登記申請書（第1欄）・第2欄の画像プロンプト（完成形）
│       ├── prompt_R1_dai22mon_toukishinseisho_machigai.md     登記申請書「敷地権の表示」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R1_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R1_dai22mon.py                              記事・付属プロンプト・生成画像の数値・求積・条文・体裁の照合スクリプト
│       └── zu/                                                解説図7枚のPNGと作図スクリプト draw_R1_dai22mon_kaisetsuzu.py、登記申請書の完成形（第1欄・第2欄）・添削（縦長）のPNG・HTMLと生成スクリプト make_R1_dai22mon_shinseisho_gazou.py
├── R2/
│   ├── Q21/
│   │   ├── note_R2_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R2_dai21mon_kaiwa_kaisetsuzu.md       解説図9枚（全体図・B点の座標変換・G点H点の長方形・公差の判定・分合筆の流れ・登記識別情報の整理・地積測量図・対角線で面積を出す別解・本番で解く順番）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_R2_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。土地分合筆登記）
│   │   ├── prompt_R2_dai21mon_toukishinseisho_machigai.md  登記申請書「土地の表示」欄（（イ）107.68→107.73、合筆後156.53→156.12）の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│   │   ├── prompt_R2_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R2_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図9枚のPNGと作図スクリプト draw_R2_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像のPNGとHTML（R2_dai21mon_toukishinseisho_kansei／_machigai）と生成スクリプト make_R2_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R2_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R2_dai22mon_kaisetsuzu.md                   解説図7枚（家屋番号の特定・敷地と建物の位置・建物図面・1階2階の求積・3階の誤り比較・3階の求積・本番で解く順番）作成プロンプト
│       ├── prompt_R2_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。第1欄の滅失登記・第3欄の表題登記、第2欄の完成形）
│       ├── prompt_R2_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」欄の誤答→添削→正解の画像プロンプト（3コマを縦に積んだ縦長）
│       ├── prompt_R2_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R2_dai22mon.py                              記事・付属プロンプト・画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図7枚（図7は本番で解く順番）のPNGと作図スクリプト draw_R2_dai22mon_kaisetsuzu.py（fit(..., pad_aspect=True)）。登記申請書の完成形2枚（第1欄・第3欄、縦長1200px）・第2欄の完成形・添削画像（縦3コマ）のPNG・HTMLと生成スクリプト make_R2_dai22mon_shinseisho_gazou.py
├── R3/
│   ├── Q21/
│   │   ├── note_R3_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み。相続人の1人が他の相続人に代位する分筆）
│   │   ├── prompt_R3_dai21mon_kaiwa_kaisetsuzu.md       解説図11枚（全体図・A点・C点・H点・L点・地図に準ずる図面・公差・分筆の地番・代位の関係図・地積測量図・解く順番）作成プロンプト
│   │   ├── prompt_R3_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。答案用紙どおり登録免許税が申請人の枠より前）
│   │   ├── prompt_R3_dai21mon_toukishinseisho_machigai.md  登記申請書「添付書類」欄と申請人の枠（代位）の誤答→添削→正解の画像プロンプト
│   │   ├── prompt_R3_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R3_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図11枚のPNGと作図スクリプト draw_R3_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像（縦長）のPNG・HTMLと生成スクリプト make_R3_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R3_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R3_dai22mon_kaisetsuzu.md                   解説図7枚（区分の全体像・敷地辺長図・建物図面・壁心/内法の誤り比較図・1階/2階求積図・問2の求積図）作成プロンプト
│       ├── prompt_R3_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。第1欄をA3横の答案用紙の左の列→右の列の順に縦に積む。第2欄の完成形も）
│       ├── prompt_R3_dai22mon_toukishinseisho_machigai.md     登記申請書「区分した建物の表示」の原因欄の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
│       ├── prompt_R3_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R3_dai22mon.py                              記事・付属プロンプト・画像・HTMLの数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図7枚のPNGと作図スクリプト draw_R3_dai22mon_kaisetsuzu.py（fit(..., pad_aspect=True)）。登記申請書の完成形（第1欄、縦長1200px）・第2欄の完成形・添削画像（縦3コマ）のPNG・HTMLと生成スクリプト make_R3_dai22mon_shinseisho_gazou.py
├── R4/
│   ├── Q21/
│   │   ├── note_R4_dai21mon_tochi_kaiwa_kaisetsu.md      note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R4_dai21mon_kaiwa_kaisetsuzu.md        解説図10枚（全体図・AB線とEFGの比較・合成図の裏付け・P点・I点J点・筆界特定・公差・分筆と地番・地積測量図・本人確認情報）作成プロンプト
│   │   ├── prompt_R4_dai21mon_toukishinseisho_gazou.md   登記申請書画像プロンプト（完成形。土地一部地目変更・分筆登記）
│   │   ├── prompt_R4_dai21mon_toukishinseisho_machigai.md  登記申請書「登記の目的」と（イ）（ロ）の行の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
│   │   ├── prompt_R4_dai21mon_miidashi_gazou.md           note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R4_dai21mon_kaiwa.py                   記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                           解説図10枚のPNGと、作図スクリプト draw_R4_dai21mon_kaisetsuzu.py（fit(..., pad_aspect=True)）。登記申請書の完成形・添削画像（R4_dai21mon_toukishinseisho_kansei／machigai の PNG・HTML、縦長1200px）と生成スクリプト make_R4_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R4_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R4_dai22mon_kaisetsuzu.md                   解説図6枚（工事前後比較図・敷地辺長図・建物図面・1階/2階求積図・車庫の誤り比較図）作成プロンプト
│       ├── prompt_R4_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R4_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」欄の誤答→添削→正解の画像プロンプト
│       ├── prompt_R4_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R4_dai22mon.py                              記事・付属プロンプト・画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                画像（解説図6枚・登記申請書の完成形・添削・第2欄・第3欄のPNGとHTML、作図・書き出しスクリプト）
├── R5/
│   ├── Q21/
│   │   ├── note_R5_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。アガルート解答例と照合済み）
│   │   ├── prompt_R5_dai21mon_kaiwa_kaisetsuzu.md       解説図8枚（全体図・筆界点F/Jの比較・B点・H点・分筆の区画の比較・地積測量図・分合筆・職権の分合筆）作成プロンプト（土地の基本フォームの記入済み）
│   │   ├── prompt_R5_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（完成形。地目変更・分合筆）
│   │   ├── prompt_R5_dai21mon_toukishinseisho_machigai.md  登記申請書「添付書類」欄と分合筆後の1番1の行の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
│   │   ├── prompt_R5_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（1280×670px）
│   │   ├── verify_R5_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト
│   │   └── zu/                                          解説図8枚のPNGと作図スクリプト draw_R5_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削画像（縦3コマ）のPNG・HTMLと生成スクリプト make_R5_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R5_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R5_dai22mon_kaisetsuzu.md                   解説図6枚（敷地辺長図・建物図面・誤り比較図・1階/2階求積図・工事前後比較図）作成プロンプト
│       ├── prompt_R5_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形。一棟の建物の表示・敷地権の目的である土地の表示・区分した建物の表示・敷地権の表示まで答案用紙の形どおり）
│       ├── prompt_R5_dai22mon_toukishinseisho_machigai.md     登記申請書「原因及びその日付」の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
│       ├── prompt_R5_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R5_dai22mon.py                              記事・付属プロンプト・画像の数値・求積・体裁の照合スクリプト
│       └── zu/                                                解説図6枚のPNGと作図スクリプト draw_R5_dai22mon_kaisetsuzu.py、登記申請書の完成形・添削画像（縦3コマ）のPNG・HTMLと生成スクリプト make_R5_dai22mon_shinseisho_gazou.py
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
│   │   └── zu/                                          解説図9枚のPNGと作図スクリプト draw_R6_dai21mon_kaisetsuzu.py、登記申請書の完成形・添削（3コマを縦に積んだ縦長）のPNG・HTMLと生成スクリプト make_R6_dai21mon_shinseisho_gazou.py
│   └── Q22/
│       ├── note_R6_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
│       ├── prompt_R6_dai22mon_kaisetsuzu.md                   解説図6枚（出入り経路図・敷地辺長図・建物図面・1階誤り比較図・1階/2階求積図）作成プロンプト
│       ├── prompt_R6_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（完成形）
│       ├── prompt_R6_dai22mon_toukishinseisho_machigai.md     登記申請書「共有者」欄の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
│       ├── prompt_R6_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
│       ├── verify_R6_dai22mon.py                              記事・付属プロンプト・生成画像（PNG・HTML）の数値・体裁の照合スクリプト
│       └── zu/                                                生成済みの画像
│           ├── draw_R6_dai22mon_kaisetsuzu.py                 解説図6枚の作図スクリプト（tools/zu_helpers.py を使用）
│           ├── make_R6_dai22mon_shinseisho_gazou.py           申請書の完成形1枚・添削1枚の生成スクリプト（HTML＋Playwright）
│           ├── R6_dai22mon_zu01〜zu06_*.png                   解説図6枚
│           └── R6_dai22mon_toukishinseisho_*.png / .html      申請書の完成形と「共有者」欄の添削
└── R7/
    ├── Q21/
    │   ├── note_R7_dai21mon_tochi_kijutsu_kaisetsu.md   note記事本文（プロース形式。アガルート解答例と照合済み）
    │   ├── note_R7_dai21mon_tochi_kaiwa_kaisetsu.md     note記事本文（会話形式。答えはプロース版と同じ。L点は延長線の交点の相似で解く）
    │   ├── prompt_R7_dai21mon_toukishinseisho_gazou.md  登記申請書画像プロンプト（R7第21問の記入データ済み）
    │   ├── prompt_R7_dai21mon_toukishinseisho_machigai.md  登記申請書「申請人」「添付書類」欄の誤答→添削→正解の画像プロンプト（会話形式用。3コマを縦に積んだ縦長）
    │   ├── prompt_R7_dai21mon_miidashi_gazou.md          note見出し画像（サムネイル）作成プロンプト（会話形式用、1280×670px）
    │   ├── prompt_R7_dai21mon_kaisetsuzu.md             解説図（K点・地積測量図・J点L点）作成プロンプト（プロース版用、R7第21問の座標入り）
    │   ├── prompt_R7_dai21mon_kaiwa_kaisetsuzu.md       解説図12枚（全体図・D点・筆界の比較・K点・公差・地積測量図・J点・L点・分筆の地番・K点の別解・10月の申請までの時系列・解く順番）作成プロンプト（会話形式用。土地の基本フォームの記入済み見本）
    │   ├── verify_R7_dai21mon.py                        記事の数値・電卓表示の照合スクリプト（プロース版）
    │   ├── verify_R7_dai21mon_kaiwa.py                  記事・付属プロンプトの数値・体裁の照合スクリプト（会話形式）
    │   └── zu/                                          解説図12枚のPNGと、作図の参照実装 draw_R7_dai21mon_kaisetsuzu.py（fit(..., pad_aspect=True)）。登記申請書の完成形・添削画像のPNGとHTML（R7_dai21mon_toukishinseisho_kansei／_machigai）と生成スクリプト make_R7_dai21mon_shinseisho_gazou.py
    └── Q22/
        ├── note_R7_dai22mon_tatemono_kaisetsu.md              note記事本文（会話形式。アガルート解答例と照合済み）
        ├── prompt_R7_dai22mon_kaisetsuzu.md                   解説図6枚（変遷図・符号2の一部取壊し・柱芯の誤り比較図・1階/2階求積図・本番で解く順番）作成プロンプト
        ├── prompt_R7_dai22mon_toukishinseisho_gazou.md        登記申請書画像プロンプト（問1・問2の完成形）
        ├── prompt_R7_dai22mon_toukishinseisho_machigai.md     登記申請書「符号」の誤答→添削→正解の画像プロンプト（3コマを縦に積む）
        ├── prompt_R7_dai22mon_miidashi_gazou.md                note見出し画像（サムネイル）作成プロンプト（1280×670px）
        ├── verify_R7_dai22mon.py                              記事・生成画像（PNG・HTML）の数値・体裁の照合スクリプト
        └── zu/                                                生成済みの画像（第22問で初めて実際に生成）
            ├── draw_R7_dai22mon_kaisetsuzu.py                 解説図6枚の作図スクリプト（tools/zu_helpers.py を使用）
            ├── make_R7_dai22mon_shinseisho_gazou.py           申請書の完成形2枚・添削1枚の生成スクリプト（HTML＋Playwright）
            ├── R7_dai22mon_zu01〜zu06_*.png                   解説図6枚
            └── R7_dai22mon_toukishinseisho_*.png / .html      申請書の完成形（問1・問2）と添削
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
