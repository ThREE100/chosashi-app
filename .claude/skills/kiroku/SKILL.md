---
name: kiroku
description: 毎日ドリル（daily-drill の朝の択一・夜の記述式）を解いた結果を、ひっかけの型で記録し、集計・解き直しの予定を返す。ユーザーが「記録」「ドリルの結果」「第○日の朝／夜、×」「今日の解き直し」と言ったとき、または /kiroku で使う。一問一答ドリル（/drill）とは別。
---

# 毎日ドリルの誤答の記録

エンジンは `python3 daily-drill/kiroku.py`。記録は `daily-drill/log/YYYYMMDD.jsonl`、集計は `daily-drill/log/report.md`（自動生成）。説明は `daily-drill/log/README.md`。
**個人の演習結果なので、問題・解説・公開用の記事には転記しない。**

## 1. 記録する（「第20日の夜、×、添付情報を落とした」など）
1. 問題を決める：「第N日の朝／夜」は `dayN-am` / `dayN-pm`、IDなら `AM-003`・`PM-20`。どちらか分からなければ聞く。
2. 結果：○（全部できた）・△（一部まちがい）・×（まちがい）。
3. ×・△ のときは型を決める。**型は推測で決めず**、その問の想定の型（`daily-drill/registry.json` の traps、解答ページの「記録」の欄）を名前つきで示して選んでもらう。ユーザーの話から明らかなとき（「添付情報を落とした」→ A2 など）だけ、型を添えて「A2 でよいか」を確かめてから記録する。当てはまらなければ「他」と、メモ（--note）に中身を書く。
4. 実行：`python3 daily-drill/kiroku.py add <問題> <○|△|×> [型 …] [--item 欄・肢・点] [--min 分] [--note メモ]`（日付は今日。前の日の分は `--date YYYY-MM-DD`）。
   - 「想定のひっかけにない型」と出たら、その旨を一言伝える（問題の作りを見直す材料）。
5. 保存：`git -C /home/user/chosashi-app pull origin main` のあと、`daily-drill/log/` だけをコミットして `main` に push（記録だけの変更。コードや問題は一緒にしない）。

## 2. 返事の形（スマホ向けに短く）
- 記録した内容を1行（問題・結果・型）。
- `daily-drill/log/report.md` から、引っかかった回数の多い型の上位3つと、その型を練習する未演習の問題を1行ずつ。
- 今日の解き直しがあれば `kiroku.py due` の結果を添える。

## 3. 解き直し（「今日の解き直し」「日曜の復習」）
- `python3 daily-drill/kiroku.py due`（日付指定は `--date`）。一覧の問題の問題ページ（`daily-drill/out/dayNN-am.html`・`dayNN-pm.html`）を案内する。
- 間隔：最後の ×・△ から3日後 → ○ なら7日後 → もう一度 ○ で卒業（また ×・△ なら最初から）。

## 4. 決まり
- 正誤を判定するのはユーザー（自己採点）。こちらで答えを採点し直したり、結果を変えたりしない。採点の相談をされたら、解答ページ（`daily-drill/out/dayNN-*-ans.html`）の答えと根拠で答える。
- 記録を直す・消すときは、該当の `log/YYYYMMDD.jsonl` の行を直し、`python3 daily-drill/kiroku.py check` と `report` を実行する。
- 「他」が3回以上たまった中身は、新しい型として `daily-drill/taxonomy.json` に足すことを提案する（足すのはユーザーの了承を得てから）。
