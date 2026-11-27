# Codexに貼る一括指示文（第2回 見出し画像）

使い方：下の「ここから」〜「ここまで」をそのまま OpenAI Codex に貼り、キャラクターシート_I-01〜03 の3枚をチャットに添付する（シートはリポジトリに入っていない）。Codex が GitHub から記事とプロンプトを読み、画像の生成・ファイル名の付け直し・zip化まで行う。

---ここから---

GitHub のリポジトリ ThREE100/chosashi-app（https://github.com/ThREE100/chosashi-app 、ブランチ main）の記事「条文ランキングの続き（11位〜32位と、法令ごとの顔ぶれ）」の見出し画像を2枚作り、本文の図と一緒に zip にまとめてください。

## 対象（GitHub上のファイル。ここから読む）

- 記事フォルダ：https://github.com/ThREE100/chosashi-app/blob/main/note-unei/hitogara/02-joubun-ranking-30/
- 見出し画像のプロンプト：https://github.com/ThREE100/chosashi-app/blob/main/note-unei/hitogara/02-joubun-ranking-30/header-prompts.md
- 記事本文（画像のファイル名の確認用）：https://github.com/ThREE100/chosashi-app/blob/main/note-unei/hitogara/02-joubun-ranking-30/article.md
- zip化スクリプト：https://github.com/ThREE100/chosashi-app/blob/main/note-unei/hitogara/make_zip.sh

## 手順

1. リポジトリを clone する（すでに手元にあれば `git pull origin main` で最新にする）。
   `git clone https://github.com/ThREE100/chosashi-app.git && cd chosashi-app`
2. `note-unei/hitogara/02-joubun-ranking-30/header-prompts.md` を読む。見出し「## note用（1280×670）」と「## Instagram用（1080×1440）」の下に、それぞれ「ファイル名：`…png`」と、``` で囲まれたプロンプトがある。プロンプトはコードブロックの中身を**1文字も変えずに**使う（要約・翻訳・言い換えをしない。コードブロックの外の説明文は入れない）。
3. 2つのプロンプトで画像を1枚ずつ生成する。添付したキャラクターシート_I-01〜03 の3枚を、2枚とも参照画像として渡す。プロンプトの中の「main character」と「キャラクターシート_I-01, I-02, I-03」は、この添付した3枚とその人物のこと。
4. 生成した画像を、その見出しの「ファイル名：」の名前（`hitogara02_header_note.png`・`hitogara02_header_ig.png`）に付け直して、`note-unei/hitogara/02-joubun-ranking-30/` に PNG で保存する。寸法が見出しの（W×H）とちょうど同じでなければ、縦横比を保ったまま拡大・縮小して全体を覆い、中央で切り取ってぴったりにする（歪ませない。余白を足さない。透明の部分を残さず RGB で保存する）。
5. 2枚それぞれを確かめ、問題があればその画像だけ同じプロンプトで作り直す。
   - 寸法が見出しのとおり
   - 画像の中の文字が、プロンプトで指定したタイトル2行とサブタイトルだけで、一字一句同じ（数字・英字が入っていない。漢字が中国の字体になっていない）
   - 人物はキャラクターシート_I-01〜03 の人物1人だけで、シートと同じ髪型・服装。背景に胸像・彫像・肖像画など、ほかの人型が一つもない
   - 腕は左右1本ずつ（片側に2本ない）、手は2つで指は5本ずつ
   - 背景が、トリニティ・カレッジ図書館のロングルームを思わせる重厚な歴史的図書館の内装（書架・回廊・天井の装飾）になっている
   - 背景が端まで塗られていて、透明の部分がない
6. リポジトリの直下で次を実行して zip を作る。
   `bash note-unei/hitogara/make_zip.sh note-unei/hitogara/02-joubun-ranking-30`
   足りない画像・寸法の違う画像があると、その名前が表示されて zip はできない。表示された画像を直して、もう一度実行する。
7. できた `note-unei/hitogara/zip/02-joubun-ranking-30.zip` を渡し、手順5の確認結果と、zip に入ったファイルの一覧を報告する。

## してはいけないこと

- `article.md`・`header-prompts.md`・`make_zip.sh` など既存のファイルを書き換えない。
- 本文の図（`zu01_rank11_32_note.png`・`zu02_kamoku_note.png`・`zu01a_rank11_21_ig.png`・`zu01b_rank22_32_ig.png`・`zu02_kamoku_ig.png`）は作成済みなので、作り直さない・上書きしない。
- 見出し画像2枚と zip のほかにファイルを作らない。git の commit・push はしない。

---ここまで---
