# 誤答の記録（個人の演習結果）

毎日ドリルを解いた結果を、ひっかけの型（`taxonomy.json` の朝 M1〜M10、夜 C1〜C14・A1〜A8・D1〜D5）で記録する場所。
**個人の演習結果なので、問題・解説・公開用の記事には転記しない。**

- `YYYYMMDD.jsonl`：その日に解いた記録（1回1行）。`python3 daily-drill/kiroku.py add …` が書き足す。手で直したら `python3 daily-drill/kiroku.py check`。
- `report.md`：自動生成の集計（ひっかけの型別の引っかかった率、問題の型・分野別の正答率、再演習の予定、弱い型を練習する問題）。

記録のしかた（解答ページの最後の「記録」の欄にも、その問のコマンドが印刷してある）：

```
python3 daily-drill/kiroku.py add PM-20 × A2 --item 添付情報 --min 18   # ×・△ は型を1つ以上
python3 daily-drill/kiroku.py add day20-pm △ A5                         # 第20日の夜（dayNN-am / dayNN-pm）でもよい
python3 daily-drill/kiroku.py add AM-003 ○                               # ○ は型を書かない
python3 daily-drill/kiroku.py add PM-82 × 他 --note "比の分子と分母を逆にした"   # 型に当てはまらないとき
python3 daily-drill/kiroku.py due                                         # 今日解き直す問題
```

再演習の間隔：最後の ×・△ から3日後 → その後 ○ なら7日後 → もう一度 ○ で卒業（また ×・△ なら最初から）。
日曜の「誤答の再演習」は `due` の一覧から解く。
