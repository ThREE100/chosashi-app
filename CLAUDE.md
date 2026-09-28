# CLAUDE.md

## 記述式（第21問・第22問）学習漫画のChatGPT操作手順について

`note-articles/`（択一式）とは別に、記述式の学習漫画をChatGPTで生成・検品・ZIP化する
手順は`CHATGPT_MANGA_WORKFLOW.md`にまとめてある。記述式の作業に入るときはまずそちらを読む。

## 択一式・⑤作図ガイド型インフォグラフィックのChatGPT一括生成手順について(2026-09-19追加)

R7〜H17の問1〜問3（民法、全63記事）に埋め込まれている「⑤作図ガイド型」インフォグラフィック
プロンプトをChatGPTで一括生成・検品・リネーム・ZIP化する手順は`CHATGPT_INFOGRAPHIC_BATCH_WORKFLOW.md`
にまとめてある。ローカル環境（Chrome拡張「Claude in Chrome」が使える`claude --chrome`起動）でのみ
実行できる（クラウド上のリモートセッションでは実ブラウザ操作ができないため不可）。対象記事一覧・
プロンプト抽出には`note-articles/tools/list_gozu_guide_targets.py`を、生成後のZIP検品には
`note-articles/tools/verify_infographic_zip.py`を使う。

## ローカル環境でのClaude Code + Chrome拡張セットアップ手順について(2026-09-19追加)

「ローカルPCにClaude Code + Chrome拡張(Claude in Chrome)を用意し、実ブラウザでWEB版ツール
(ChatGPT等)を操作して大量のプロンプトを一括生成する」という仕組み自体は、上記2つの案件
(記述式学習漫画、択一式⑤作図ガイド型インフォグラフィック)に共通する汎用パターンである。
この環境構築・運用パターン（Windows特有の落とし穴を含む）は案件に依存しない内容として
`LOCAL_CLAUDE_CHROME_SETUP_GUIDE.md`にまとめてある。新しい案件で同じ仕組みを再現する場合は、
まずこのファイルを読む。案件固有の手順(何を・どんなプロンプトで生成するか)は、このファイルの
手順で立ち上げたローカルのClaude Codeに、案件ごとの`CHATGPT_*_WORKFLOW.md`を読み込ませて使う。

## 記述式note解説記事の作成とダブルチェックについて(2026-09-26追加)

記述式（第21問・土地）のnote解説記事は`note-articles-Kijyutsu/`に年度・問題番号別（例：`R6/Q21/`）で保存する。
執筆は`note-articles-Kijyutsu/prompt_note-kijutsu_tochi_kyoutsu.md`に従い、書き終えたら
`note-articles-Kijyutsu/qa-checklist-kijutsu.md`に従ってダブルチェックする（予備校の解答例は照合用のみ、説明文の流用禁止）。
チェックで新しい種類の誤りが見つかったら、同指示書末尾の改善記録に残し、指示書と執筆プロンプトの両方を更新する（PDCA）。

## 記述式（第22問・建物）会話形式note記事について(2026-09-28追加)

第21問（土地）とは別に、第22問（建物）の記述式は「トリ先生（毒舌だが愛のある教師役）」と「藍子（まじめだが罠にはまる生徒役）」の
会話形式（学習コミック風）でnote記事を作る。保存先・ダブルチェックの運用は土地と同じ`note-articles-Kijyutsu/`配下（例：`R5/Q22/`）だが、
文体は解説プロースではなく会話形式で、計算も要所（敷地の辺長、床面積の求積）だけを示す軽めのスタイルになる点が異なる。
執筆は`note-articles-Kijyutsu/prompt_note-kijutsu_tatemono_kyoutsu.md`に従う。解説図（インフォグラフィック）は
`note-articles-Kijyutsu/prompt_kaisetsuzu-gazou_kihon-form_tatemono.md`、登記申請書の画像は
`note-articles-Kijyutsu/prompt_toukishinseisho-gazou_kihon-form_tatemono.md`を使う。ダブルチェックは土地と共通の
`qa-checklist-kijutsu.md`だが、3章に建物固有の判断ポイント（合併/合体の別、床面積不算入部分、壁心/内法の切替など）を分けて記載してある。
令和5年度分（`R5/Q22/`）はアガルートの解答例・試験問題本文と照合済み（2026-09-28）。`verify_R5_dai22mon.py`で
表示値の一致を確認しており、挿入すべき画像（解説図6枚、登記申請書の完成形・誤り添削の計8枚＋note見出し画像）のプロンプトも
`R5/Q22/prompt_R5_dai22mon_kaisetsuzu.md`・`prompt_R5_dai22mon_toukishinseisho_gazou.md`・
`prompt_R5_dai22mon_toukishinseisho_machigai.md`に揃っており、会話形式ワークフローの完成した参考例として使える
（実際の画像生成・検品はまだ行っていない）。noteにそのまま貼り付けられる体裁（セリフの改行はハードブレーク、
画像挿入マーカーは引用形式で該当会話の直後に置く、区切り線の位置など）も確定済みで、
`prompt_note-kijutsu_tatemono_kyoutsu.md`の「note向けの体裁ルール」に理由つきで明記してある。
`qa-checklist-kijutsu.md`冒頭の「自動PDCA運用ルール」のとおり、内容の誤りだけでなく体裁修正も改善記録の対象とし、
年度ごとの記事が完成するたびに指示書・執筆プロンプト・図面プロンプトの改善余地を必ずレビューすること。
令和7年度分（`R7/Q22/`）はアガルートの解答例・答案用紙・試験問題本文と照合済み（2026-09-28）。`verify_R7_dai22mon.py`で
表示値の一致を確認しており、挿入すべき画像（解説図3枚、登記申請書の完成形・誤り添削の計3枚＋note見出し画像）のプロンプトも
`R7/Q22/prompt_R7_dai22mon_kaisetsuzu.md`・`prompt_R7_dai22mon_toukishinseisho_gazou.md`・
`prompt_R7_dai22mon_toukishinseisho_machigai.md`・`prompt_R7_dai22mon_miidashi_gazou.md`に揃っている
（実際の画像生成・検品はまだ行っていない）。本問は区分建物が関係せず、主である建物の全部取壊し＋附属建物の格上げ
（滅失登記ではなく表題部変更登記1本になる）と、附属建物の取壊し・再築による符号の付け替えが主な論点。
問題PDFの画像は`public/kijutsu/R07-tatemono/`にある（問題本文はユーザーから追加添付を受けた）。
令和6年度分（`R6/Q22/`）はアガルートの解答例・答案用紙・試験問題本文と照合済み（2026-09-28。問題PDFの後半に解答・解説と解答例が同じファイルで入っていた）。
`verify_R6_dai22mon.py`で記事と付属プロンプト（登記申請書・添削・見出し画像・解説図の頂点座標）の一致を確認しており（NG 0件）、
挿入すべき画像（解説図6枚、登記申請書の完成形・「共有者」欄の誤り添削の計2枚＋note見出し画像）のプロンプトも
`R6/Q22/prompt_R6_dai22mon_kaisetsuzu.md`・`prompt_R6_dai22mon_toukishinseisho_gazou.md`・
`prompt_R6_dai22mon_toukishinseisho_machigai.md`・`prompt_R6_dai22mon_miidashi_gazou.md`に揃っている
（実際の画像生成・検品はまだ行っていない）。本問は共有の新築建物の建物表題登記で、屋外廊下の先にある（あ）部分
（1階は周壁のない車庫、2階は洋室）が構造上の独立性はあるが利用上の独立性がないため1個の建物の一部になる点
（2階は床面積に算入、1階の車庫は不算入）、出窓の不算入、上下の寸法線の差に隠れた0.45の幅、71.685→71.68の切り捨て、
申請人（共有者の1人）と共有者欄（全員＋持分）の区別が主な論点。建物図面に2階の張り出しを点線で書くかは未検証
（解答例どおり1階の母屋の外形のみとした）。

## 運用ルール(2026-07-15合意)

- 作業セッションごとにコミットする(まとめて1コミットにしない)
- 保留・着手しない案は削除せず、GitHub Issueとして記録する

## 作業ブランチの統一(2026-08-12合意、2026-08-14最終改訂、2026-09-28に記述式へも明文化)

- 土地家屋調査士試験のnote解説記事(択一式`note-articles/`配下、記述式`note-articles-Kijyutsu/`配下の両方)に関する作業は、`main`ブランチに統一する。年度・問題番号ごとに個別のfeatureブランチ(`claude/surveyor-exam-*`等)を新設せず、既存記事の修正・新規記事の作成とも、`main`に直接コミット・pushする。
- 記述式（第21問・土地、第22問・建物）の解説note記事は、GitHubの https://github.com/ThREE100/chosashi-app/tree/main/note-articles-Kijyutsu に保存・記録する。作業場所は必ず`main`ブランチとし、他のfeatureブランチ上で作成・放置しない。セッション開始時に別ブランチへの作業を指示されている場合でも、note-articles-Kijyutsu配下の変更は`main`へ直接コミット・pushする（この指示は、そのための事前の明示的許可を兼ねる）。
- 経緯: 当初(2026-08-12)は`main`への統一を合意→同日中に、より完成度の高い正本が別途存在することが判明し`claude/surveyor-exam-afternoon-q1-20-5lehv0`ブランチへ統一を改訂→2026-08-14、同ブランチ(全年度分のnote-articles、ローカル法令データベース`laws/`等を含む)の内容がmainへ統合され、年度別featureブランチも含め旧ブランチはすべて`archived/`配下にアーカイブされたため、最終的に`main`への統一に戻った→2026-09-28、記述式(`note-articles-Kijyutsu/`)の会話形式ワークフロー整備作業がセッション指定のfeatureブランチにコミットされてしまったため、本ルールが択一式だけでなく記述式にも及ぶことを明文化した。
- 今後、新規の作業・修正はすべて`main`側で行う。旧ブランチ(`archived/claude/surveyor-exam-*`等)は参照専用のアーカイブであり、更新しない。
- 別セッションが並行して`main`を更新している場合があるため、pushの前に`git pull origin main`で最新化してから作業・pushすること。

## ルールの再確認(2026-08-16)

- 2026-08-16のセッションで、アーカイブ済みのはずの`claude/surveyor-exam-heisei26-afternoon-lmt0j0`および`claude/surveyor-exam-afternoon-q1-20-5lehv0`(同名の`archived/`配下ブランチが既に存在するにもかかわらず、非アーカイブ名で生き残っていた)に誤って作業・pushしてしまう事例が発生した。これを受けて、上記ルールを改めて明文化する。
- 土地家屋調査士試験のnote解説記事に関する更新・保存先は`main`のみとする。`claude/surveyor-exam-*`系のブランチ(archived配下・非archived配下を問わず)は今後一切使用しない。
- 未反映の作業: `claude/surveyor-exam-afternoon-q1-20-5lehv0`ブランチ上に、平成26年度Q1〜20の肢別解説の法令再検証・修正(コミット`58f1c5f`)およびQ6の保管期間補足(コミット`34488e5`)が、`main`未反映のまま残っている。同ブランチのH27午後等の記事は`main`より古く後退するため、単純な上書き・マージは行わず、該当ファイル(主に`note-articles/h26-mondai/`配下)を個別に差分確認したうえで`main`に反映すること。
