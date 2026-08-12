# CLAUDE.md

## 運用ルール(2026-07-15合意)

- 作業セッションごとにコミットする(まとめて1コミットにしない)
- 保留・着手しない案は削除せず、GitHub Issueとして記録する

## 作業ブランチの統一(2026-08-12合意)

- 土地家屋調査士試験のnote解説記事(note-articles/配下)に関する作業は、今後 `https://github.com/ThREE100/chosashi-app` の `main` ブランチに統一する。年度・問題番号ごとに個別のfeatureブランチ(`claude/surveyor-exam-*`等)を新設せず、`main`に直接コミット・pushする。
- 既存のfeatureブランチは削除せず保持するが、新規の作業・修正はmain側で行う。
- 別セッションが並行して同じリポジトリのmainを更新している場合があるため、pushの前に`git pull origin main`で最新化してから作業・pushすること。
- 例外：平成28年度午後の部の既存記事(note-articles/h28-mondai/配下)を修正する場合は、`main`に加えて`claude/surveyor-exam-afternoon-q1-20-5lehv0`ブランチにも同じ修正を反映する(2026-08-12合意)。同ブランチは他の複数年度(H23・H24・R3・R4等)のセッションからも参照されているため、当分の間はmainとの二重メンテナンスとする。
