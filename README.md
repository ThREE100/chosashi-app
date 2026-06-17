# 土地家屋調査士 トレーニング（Webアプリ）

択一過去問・暗記・書式（記述）・座標計算をまとめた学習Webアプリです。
択一の正答は **法務省の公式正答** と全問突合済み。学習記録はブラウザ内に自動保存されます。
上部タブで「択一 / 暗記 / 書式 / 計算」を切替。

## できること
**択一過去問（Phase 1・2）… 233問**
- 収録：平成24・26年＋平成27年〜令和6年（公式正答と全問一致）
- 年度別 / 分野別（民法・不動産登記法・調査士法）/ ランダム出題
- 組合せ1〜5の選択 → 正誤判定 → 解説表示
- **オリジナル解説**：解答時に「💡考え方・解き方／⚠️間違えやすいポイント／🎯覚えておくべきポイント」を表示（全233問。独立検証＋誤り修正済み）
- 正答率・解いた問題数の記録（自動保存）／間違えた問題だけの復習

**暗記（Phase 3）**
- ○× 一問一答 110問（章別／ランダム／間違い復習）
- 用語カード 44語（タップでめくり・章別）
- ※正答は解説の【正】【誤】から判定（元データの answer 欄は信頼できないため不使用）

**書式・記述（Phase 5）… 20問（建物10＋土地10）**
- 問題 → 模範解答 → 自己採点（◯解けた/△惜しい/✗）のレビュー型
- 令和6年・建物は**実際の問題用紙＋模範解答を図面画像つき**で収録（タップで拡大）
- 他年度は問題文＋模範解答テキスト（図面画像は今後追加可）
- ※作図は自動採点不可。紙に手書きで挑戦してから照合する方式

**計算（書式・Phase 4）**
- 座標求積：座標法による面積計算＋求積表（点を自由に増減）
- 距離・方向角：2点間の距離と方向角（度分秒）
- 座標系は X＝北・Y＝東、方向角は北から時計回り

## 起動のしかた（毎回これだけ）
1. このフォルダを開く
2. PowerShell で次を実行：
   ```
   npm run dev
   ```
3. 表示される `http://localhost:5173/` をブラウザで開く
4. 止めるときは PowerShell で `Ctrl + C`

> 初回や久しぶりのときに動かない場合は、先に `npm install` を一度だけ実行してください。

## フォルダの中身（ざっくり）
```
src/
  App.tsx              … 画面の切り替え（ホーム/演習/結果）
  components/
    Home.tsx           … トップ画面（出題の選択）
    Quiz.tsx           … 演習画面（1問ずつ）
    Result.tsx         … 結果画面
    OxQuiz.tsx         … ○×一問一答
    Flashcard.tsx      … 用語カード
    Kijutsu.tsx        … 書式レビュー（問題→模範解答→自己採点）
    Survey.tsx         … 計算（座標求積・距離方向角）
  lib/storage.ts       … 学習記録の保存（localStorage）
  data/takuitsu.json   … 択一データ（正本・233問）
  data/ankicards.json  … 暗記データ（○×110＋用語44）
  data/kijutsu.json    … 書式データ（建物10＋土地10）
  types.ts             … データの型
public/
  kijutsu/             … 書式の図面画像（例：R06-tatemono/q1.png 〜 a2.png）
tools/
  generate_takuitsu.py … 問題データを作り直すスクリプト（元データから再生成用）
```

## 問題データの作り直し（参考）
元データ（`...\chosashi_app\kakomon_data.json` と `official_answers.json`）から再生成する場合：
```
python tools/generate_takuitsu.py
```

## 今後の拡張メモ（ロードマップ）
- ~~Phase 1: 択一過去問（193問）~~ ✅ 完了
- ~~Phase 3: 暗記カード（○×110問＋用語44）~~ ✅ 完了
- ~~Phase 4: 書式（土地）座標計算・求積~~ ✅ 完了
- ~~Phase 5: 書式（建物）図面画像＋模範解答照合~~ ✅ 完了（R06建物に図面、他はテキスト）
- Phase 2: 旧年度の択一追加 … H24・H26を追加済（→ **233問**）。
  H21・H22・H23・H25 はOCRが断片的で保留（良質な元データが要る）。
  H17〜H20 は公式正答キーが無く形式も旧式のため対象外。
- Phase 6: 公開（**PWA化は完了**。公開手順は `DEPLOY.md` → 外出先のiPhoneで使える）
- 追加候補: 書式の図面画像を他年度にも展開（tools/ で年度のPDFページを描画して public/kijutsu/ へ）

### 公開（外出先のiPhoneから使う）
`DEPLOY.md` を参照。ざっくり：`npm run build` → `dist` を Netlify Drop か Cloudflare Pages
（`npm run deploy`）へ → 発行URLをiPhone Safariで開き「ホーム画面に追加」。

### データ生成スクリプト（元データは `...\chosashi_app\`）
- `tools/generate_takuitsu.py` … 択一233問（`takuitsu.json`）
- `tools/generate_ankicards.py` … ○×110問＋用語44（`ankicards.json`）
- `tools/generate_kijutsu.py` … 書式20問（`kijutsu.json`）。図面画像は別途PDFから描画して `public/kijutsu/` に配置
- `data/kaisetsu_plus.json` … 択一の考え方/落とし穴/暗記（全233問・問題IDで紐付け・reviewed/checkNote付き）。年度ごとに生成→独立検証→誤り修正の手順で作成

※ データが増えてビルドが重くなったら、`src/data/takuitsu.json` を `public/` へ移して
　実行時読み込み（fetch）に切り替える予定。
