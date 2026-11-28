# Codexに貼る指示文（毎日ドリル 第1日（夜） 学習まんが・全20ページ＋見出し画像2枚）

使い方：「ここから」〜「ここまで」をそのまま OpenAI Codex に貼り、キャラクターシート_トリ先生_01〜03 と キャラクターシート_I-01〜03 の6枚を添付する（シートはリポジトリにない）。

---ここから---

GitHub のリポジトリ ThREE100/chosashi-app（https://github.com/ThREE100/chosashi-app 、ブランチ main）にある学習まんがのプロンプトで、画像を作ってください。

## 対象（ここから読む）
- プロンプト：https://github.com/ThREE100/chosashi-app/blob/main/daily-drill/manga/pm/day001-pm-manga_prompts.md
- 構成の型（確認用）：https://github.com/ThREE100/chosashi-app/blob/main/daily-drill/manga/KATA.md
- 差し込む図（リポジトリの中の正確な図。描き直さずにそのまま使う）：
  - 2ページ目：PM-01_mondai.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_mondai.png
  - 4ページ目：PM-01_housha.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_housha.png
  - 7ページ目：PM-01_vector.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_vector.png
  - 13ページ目：PM-01_kouten.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kouten.png
  - 14ページ目：PM-01_zahyou.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_zahyou.png
  - 19ページ目：PM-01_kotae.png　https://raw.githubusercontent.com/ThREE100/chosashi-app/main/daily-drill/manga/pm/fig/PM-01_kotae.png

## 手順
1. リポジトリを clone する（手元にあれば git pull origin main）。
   git clone https://github.com/ThREE100/chosashi-app.git && cd chosashi-app
2. プロンプトのファイルの「## 1ページ目」〜「## 20ページ目」と「## 見出し画像（note用 1280×670）」「## 見出し画像（Instagram用 1080×1440）」の見出しの下にある ``` で囲まれたプロンプトを読む。コードブロックの中身を1文字も変えずに使う（要約・翻訳・言い換えをしない）。
3. 添付した6枚を参照画像として渡し、プロンプト1つにつき1枚ずつ生成する。「キャラクターシート_トリ先生_01, _02, _03」は鳥の3枚、「キャラクターシート_I-01, I-02, I-03」は女性の3枚。鳥が先生、女性が生徒。
   図のあるページは、リポジトリの図のPNGも参照画像として渡す。生成した後、`python3 tools/gakushu_manga/paste_fig.py <生成した画像> <プロンプトのファイル> <ページ番号>` を実行して、正確な図を枠に貼り直す（図が崩れていなくても必ず行う）。
4. 画像を「毎晩ドリル漫画_Day001_p01.png」〜「毎晩ドリル漫画_Day001_p20.png」「毎晩ドリル漫画_Day001_見出し_note.png」「毎晩ドリル漫画_Day001_見出し_IG.png」の名前で、リポジトリの外の作業フォルダに PNG で保存する。指定の大きさでなければ、縦横比を保って拡大・縮小し全体を覆ってから中央で切り取る（歪ませない。余白を足さない。透明の部分を残さず RGB）。
5. 各ページを確かめ、問題があればそのページだけ同じプロンプトで1回作り直す（2回目も直らなければ、そのまま渡して何が直らなかったかを報告する）。
   - コマの数と配置がプロンプトの「## 2. Page layout」のとおり
   - 文字がプロンプトの文字列と一字一句同じで、ほかの文字がない。漢字が中国の字体になっていない
   - 名前・役割名（トリ先生・先生・生徒など）がどこにもない。吹き出しのしっぽが話し手を指している
   - 生徒は I-01〜03 の顔・髪型・服装のままで、鳥の先生と同じ画風。腕は左右1本ずつ、手は2つで指は5本ずつ
   - Ａ・Ｂ・Ｃは顔のないピクトグラム。既存の漫画作品に似た画風・キャラクターになっていない。背景が端まで塗られている
   - 図の枠の中が、リポジトリの図と同じ（線・点・文字・数字が1つも変わっていない）。枠に人物・吹き出しが重なっていない
6. すべての画像と、手順5の確認結果（ページごとに、できた点・崩れた点を具体的に）を報告する。

## してはいけないこと
- リポジトリのファイルを書き換えない。リポジトリの中に画像を置かない。git の commit・push はしない。

---ここまで---
