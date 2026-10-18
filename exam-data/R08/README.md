# 令和8年度 土地家屋調査士試験 択一式 問題原文

令和8年度の択一式（第1問〜第20問）の問題文を、受験者が持ち帰った問題用紙の写真から文字起こししたデータ。

| ファイル | 内容 |
|---|---|
| `takuitsu_R08_questions.json` | 構造化データ。`src/data/takuitsu.json` の `questions` と同じ項目（`id`・`yearCode`・`stem`・`alts`・`combos`・`correctAnswer`・`explanation`）。第4問だけ、参考条文を `reference` に持つ |
| `takuitsu_R08_questions.md` | 読みやすい版 |

## 状態
- **正答は未入力**（`correctAnswer` は `null`）。法務省の公式正答が公表されたら入力する。
- `genre`（論点分類）は暫定。
- 転記は画像を読みながら行った。1肢ずつの再照合は未実施なので、公式の問題冊子と照らして誤字・脱字を確認すること。
- 受験者の手書きの書き込み（○×・下線など）と、写真そのもの（PDF）は、個人の記録なのでここには含めない。
- アプリ本体のデータ（`src/data/takuitsu.json`）には**まだ入れていない**。正答を入力してから、別の作業として統合する。
