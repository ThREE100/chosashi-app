# CLAUDE.md

## 運用ルール(2026-07-15合意)

- 作業セッションごとにコミットする(まとめて1コミットにしない)
- 保留・着手しない案は削除せず、GitHub Issueとして記録する

## 作業ブランチの統一(2026-08-12合意、2026-08-12改訂)

- 土地家屋調査士試験のnote解説記事(note-articles/配下)に関する作業は、`claude/surveyor-exam-afternoon-q1-20-5lehv0`ブランチに統一する。年度・問題番号ごとに個別のfeatureブランチ(`claude/surveyor-exam-*`等)を新設せず、既存記事の修正・新規記事の作成とも、このブランチに直接コミット・pushする。
- 当初(2026-08-12)は`main`ブランチへの統一を合意していたが、`claude/surveyor-exam-afternoon-q1-20-5lehv0`ブランチ側に、年度を横断して統合済みのより完成度の高い正本(全年度分のnote-articles、ローカル法令データベース`laws/`等)が別途存在することが判明したため、同日中に方針を`claude/surveyor-exam-afternoon-q1-20-5lehv0`への統一に改めた。
- 既存の年度別featureブランチ(このブランチを含む)は削除せず保持するが、新規の作業・修正はすべて`claude/surveyor-exam-afternoon-q1-20-5lehv0`側で行う。年度別ブランチで先に作業してしまった場合は、`claude/surveyor-exam-afternoon-q1-20-5lehv0`側の該当記事とマージ前に必ず突き合わせ、後から作られた独自の改善(デザイン・検証方法等)を上書きしないよう内容を比較してから反映すること。
- 別セッションが並行して`claude/surveyor-exam-afternoon-q1-20-5lehv0`を更新している場合があるため、pushの前に`git pull origin claude/surveyor-exam-afternoon-q1-20-5lehv0`で最新化してから作業・pushすること。
- `main`ブランチのnote-articles/は当面そのまま保持するが、新規のメンテナンス対象ではない。
