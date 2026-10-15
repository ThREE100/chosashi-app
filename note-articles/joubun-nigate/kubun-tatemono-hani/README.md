# 区分建物の範囲　苦手克服シリーズ（全9回）

択一式の一問一答で、復習・チェックの対象になっている区分建物の肢を、論点ごとの9つのグループにまとめた苦手克服の記事です（2026-10-15作成）。
敷地権や規約敷地は、出題文の状態そのものが頭に浮かびにくいのが弱点です。そこで各回の図解は、「①出題文の状態の絵 → ②正しいイメージ（青）→ ③誤ったイメージ（赤）」の順で、確かめる記述1つにつき1組の絵を並べる形にしました。文章の知識と絵をつなげるための図です。

## 構成

1. [区分建物とは何か・登記記録の読み方](01-kihon.md)　（肢13／図解5枚／見出し画像1枚。画像プロンプトは [01-kihon_prompts.md](01-kihon_prompts.md)）
2. [敷地権が成り立つ土地と権利](02-shikichi-seiritsu.md)　（肢10／図解6枚／見出し画像1枚。画像プロンプトは [02-shikichi-seiritsu_prompts.md](02-shikichi-seiritsu_prompts.md)）
3. [敷地権の登記の流れ・記録・原因の日付](03-shikichiken-kiroku.md)　（肢15／図解9枚／見出し画像1枚。画像プロンプトは [03-shikichiken-kiroku_prompts.md](03-shikichiken-kiroku_prompts.md)）
4. [分離処分可能規約と敷地権の消滅・抵当権](04-bunri-shobun.md)　（肢9／図解6枚／見出し画像1枚。画像プロンプトは [04-bunri-shobun_prompts.md](04-bunri-shobun_prompts.md)）
5. [敷地権のある土地の分筆・合筆・地目変更・移転](05-shikichi-no-tochi.md)　（肢6／図解5枚／見出し画像1枚。画像プロンプトは [05-shikichi-no-tochi_prompts.md](05-shikichi-no-tochi_prompts.md)）
6. [区分建物の表題登記を申請する人と組み合わせ](06-hyodai-shinsei.md)　（肢16／図解8枚／見出し画像1枚。画像プロンプトは [06-hyodai-shinsei_prompts.md](06-hyodai-shinsei_prompts.md)）
7. [区分・接続・合体・合併・分割](07-setsuzoku-gattai.md)　（肢17／図解11枚／見出し画像1枚。画像プロンプトは [07-setsuzoku-gattai_prompts.md](07-setsuzoku-gattai_prompts.md)）
8. [共用部分である旨の登記](08-kyoyobubun.md)　（肢11／図解6枚／見出し画像1枚。画像プロンプトは [08-kyoyobubun_prompts.md](08-kyoyobubun_prompts.md)）
9. [区分建物の変更・滅失・所在](09-henkou-messhitsu.md)　（肢6／図解4枚／見出し画像1枚。画像プロンプトは [09-henkou-messhitsu_prompts.md](09-henkou-messhitsu_prompts.md)）

合計：肢103、図解60枚（正誤を確かめる記述の組 101）、見出し画像9枚。

## 読み方・使い方

- 記事は、1回につき「前提（用語と条文）→ ポイントごとの整理（よくある勘違い／正しい整理／見分け方／たとえば）→ まとめ → 確認事項」の順です。ポイントのあとに「画像挿入」の指示があり、対応する図解のプロンプトが `NN-…_prompts.md` にあります。
- 図解の画像は、プロンプトをChatGPT（画像生成）に貼って作ります。画像の生成と目視確認は未実施です。
- 肢の番号と、どの肢がどのポイントに入っているかは、作業用の [grouping.md](grouping.md) にあります（記事・画像には載せていません）。
- 作り方：`src/build.py`（記事とプロンプトを生成）、`src/check_all.py`（機械チェック）、`parts/partN.py`（元データ）、`work/`（肢の抽出結果）。

## このシリーズの位置づけ

条文を主役にした「条文別『苦手克服』シリーズ」（`note-articles/joubun-nigate/`）の一つで、条文ではなく**区分建物の範囲**を主役にした回です。個別の条文（区分所有法第5条など）は、同シリーズの各回を参照してください。
