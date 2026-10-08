#!/usr/bin/env python3
"""記述式解説漫画 パイロット：R7/Q21 第2章（問1 D点は「時計回り」で出す）のページ構成表（文言の正本）の設計データ。
使い方: python3 tools/drill/manga/kijutsu_pilot/r7_q21_ch02.py   → R7-Q21-ch02_page_spec.json と R7-Q21-ch02_kouseihyou.md を生成
検査:   python3 tools/drill/manga/kijutsu_pilot/check_pages.py tools/drill/manga/kijutsu_pilot/R7-Q21-ch02_page_spec.json
決定事項（2026-10-08、ユーザー）：合成方式は A′（キャラ・吹き出し・背景はChatGPT、図と計算カードはコードで合成）／電卓操作は漫画に入れない
（計算は式・表示・答えだけ）／セリフは記事の文言のまま分割（言い換えない）／図は用意済みのzu/のPNGをそのまま使う／
赤はUIでは「誤り・訂正の箇所」だけに使う（図の中の赤は制限しない）。"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ARTICLE = "note-articles-Kijyutsu/R7/Q21/note_R7_dai21mon_tochi_kaiwa_kaisetsu.md"
ZU = "note-articles-Kijyutsu/R7/Q21/zu/"

# ---------------------------------------------------------------- 記事の第2章から、セリフの正本を取り出す
def chapter_turns():
    txt = (ROOT / ARTICLE).read_text(encoding="utf8")
    ch = re.search(r"^## 第2章：.*?(?=^## 第3章)", txt, re.S | re.M).group(0)
    turns = []
    for m in re.finditer(r"^\*\*(トリ先生|藍子)\*\*  \n「(.*?)」\s*$", ch, re.S | re.M):
        turns.append((m.group(1), m.group(2)))
    return ch, turns

CH, TURNS = chapter_turns()
assert len(TURNS) == 12, len(TURNS)
TURN_IDS = ["T1", "A1", "T2", "A2", "T3", "T4", "A3", "T5", "A4", "T6", "A5", "T7"]
for tid, (who, _) in zip(TURN_IDS, TURNS):
    assert (tid[0] == "T") == (who == "トリ先生"), tid

# ---------------------------------------------------------------- セリフの分割（正本）。結合すると記事の文言（空白を除く）と一致すること
SPLIT = {
 "T1": ["D点はT2に器械を据えて、", "T1を後視して観測しているわ。", "観測角325°06′51″、水平距離25.81m。", "藍子、どう計算する？"],
 "A1": ["T2からT1の方向角を出して、", "そこから観測角を……", "325°は大きいので、", "反時計回りに35°くらい戻す", "イメージで引き算します！"],
 "T2": ["――ちょっと待ちなさい。観測値の表の注1を読んだ？", "『観測角は、時計回りの角度を示す』", "って書いてあるでしょう。引いたらどこに出るか、", "やってごらんなさい"],
 "A2": ["えっと……方向角から325°06′51″を引いて", "25.81m進むと……", "（172.27, 112.17）。", "あれ、A点やE点（X＝184.31）より", "12mも南です。甲土地の外に出ちゃいました……"],
 "T3": ["でしょう。", "時計回りの観測角は、足すのよ。", "この座標の置き方なら、", "複素平面の反時計回りが", "地図の時計回りと一致するから、", "足すだけで正しい向きになるの。", "式で書くとこう"],
 "T4": ["ちなみに途中の arg(T1 − T2)、", "つまりT2→T1の方向角は", "94°21′21.94″。", "これに325°06′51″を足すと", "419°を超えるけど、", "電卓は360°を引いたのと同じ向き", "（59°28′12.94″）で計算してくれるから",
        "気にしなくていいわ。", "座標は問題文の注3で", "小数第3位を四捨五入。", "丸めた値を打ち直して", "記憶しておきなさい"],
 "A3": ["D点の杭は、花子さんと二郎さんの説明が", "食い違っていたところですよね。", "花子さんは最初『甲土地と乙土地の境は", "C点とE点を結ぶ直線』って言っていて……"],
 "T5": ["そこが今年の最大のわなよ。二郎さんは", "『自宅と畑を分けている生垣の間に", "コンクリート杭がある』と聞いていた。", "探したらD点に杭があって、", "合成図の曲がり点とも一致した。", "だから筆界はC→D→Eと折れているの。", "CとEの直線だと思い込んだら、", "乙土地の面積もK点も全部ずれるわ"],
 "A4": ["でも先生、", "本当にDが筆界点だって、", "計算で確かめる方法は", "ありますか？"],
 "T6": ["いい質問ね。", "甲土地（206番）はN町三丁目にあって、", "不動産登記法第14条第1項の地図が", "備え付けられている土地よ。", "求めたD点で甲土地の面積を出して、", "登記記録の559㎡と比べてごらんなさい。", "A・B・C・D・Eの座標を記憶して、", "倍面積の式で一気に計算するの"],
 "A5": ["iの係数の絶対値を2で割って……", "559.8503㎡。", "畑の地積は1㎡未満を切り捨てるので、", "559㎡！", "登記記録とぴったりです！"],
 "T7": ["そう。", "CとEの直線で計算すると587.25㎡になって、", "28㎡も合わないのよ。", "筆界点の判断を座標で裏付けるときは、", "隣の土地の登記記録の地積との", "一致も使えるの。", "覚えておきなさい"],
}
for tid, (_, inner) in zip(TURN_IDS, TURNS):
    a = re.sub(r"\s+", "", inner); b = re.sub(r"\s+", "", "".join(SPLIT[tid]))
    assert a == b, f"{tid}: 分割を結合しても記事と一致しない\n{a}\n{b}"

def bub(tid, lo, hi, hl=None):
    """tid の SPLIT[lo:hi]（1始まりでなく0始まり）を吹き出しにする。強調語 hl は {番号: 語} の辞書"""
    who = "トリ先生" if tid[0] == "T" else "藍子"
    out = []
    for k in range(lo, hi):
        d = {"id": f"{tid}-{k+1}", "speaker": who, "text": SPLIT[tid][k]}
        if hl and (k + 1) in hl: d["highlight"] = hl[k + 1]
        out.append(d)
    return out

# ---------------------------------------------------------------- 全体の決め事
GLOBAL = {
  "canvas": {"w": 1080, "h": 1920, "background": "淡いクリーム（完全に不透明）"},
  "production_mode": "A′：キャラクター・吹き出し・背景・ページ枠はChatGPTで生成。図・計算カード・答えバナー・整理カードは、ChatGPTには『空の枠（仮枠）』だけを描かせ、後からコードで正確な内容を貼って合成する。",
  "placeholder_instruction": "仮枠（frame）は、指定の位置・大きさの『何も書かれていない薄い灰色（#E6E6E6）の長方形』として描く。枠線の飾り・文字・図形・影を入れない。キャラクターと吹き出しは仮枠に重ねない。",
  "bubble_font_note": "吹き出しの文字は正本のとおり（崩れやすい語は最終確認で確認）。ChatGPTが描くので、生成後に文言を一字一句照合する（OCR可）。",
  "colors": {
    "bubble": "白地＋濃紺の細い枠＋濃紺の文字（藍子・トリ先生とも同じ）",
    "card": "薄い灰色の地＋濃紺の枠＋濃紺の文字（コードで描く）",
    "answer_banner": "濃紺の地＋白い文字（答えは赤にしない。赤は誤り・訂正の箇所だけ）",
    "highlight": "黄色マーカー（強調語だけ）",
    "red_rule": "漫画のUI部品（吹き出し・カード・タグ・帯）で赤を使うのは、誤り・訂正の箇所（誤答の座標、誤りのラベル）だけ。青✓は正しい整理。図（zu/のPNG）の中の赤は制限しない（そのまま使う）。",
    "forbidden": "ピンク・緑・オレンジ。人物・領域・バーを意味のない色で塗り分けない"
  },
  "character_sizes_px": {"FULL": "全身または上半身で高さ約440〜520px", "MID": "上半身で高さ約300px", "SMALL": "全身で約110px", "FACES": "顔アイコン直径約80px（体・手は描かない）"},
  "silent_reaction": "セリフが記事にない（その人が話さない）場面でも、表情だけで反応させてよい。言葉・吹き出しは足さない（セリフは記事の文言のまま）。",
  "no_calculator_keys": "電卓操作（キー列、[ALPHA]・[SHIFT]・[STO]など）は漫画に入れない。式・表示・答えだけを出す。",
  "emotion_ids": {"A1": "自信満々", "A2": "固まる・青ざめ", "A3": "ひらめき", "A4": "確かめる・考える", "A5": "安堵・達成", "T1": "呆れ・叱る（愛あり）", "T2": "指し示す", "T3": "感心", "T4": "どや・念押し"},
}

FIG = {
  "zu02": {"file": ZU + "R7_dai21mon_zu02_D_housha.png", "size": [1600, 1200], "marker_index": 1, "recommended_class": "F-half"},
  "zu03": {"file": ZU + "R7_dai21mon_zu03_hikkai_D.png", "size": [1600, 1200], "marker_index": 2, "recommended_class": "F-half"},
}

def zone(zid, typ, y, h, **kw):
    d = {"zone_id": zid, "type": typ, "y": y, "h": h}; d.update(kw); return d

PAGES = []
def page(pid, template, beat, one_point, zones, **kw):
    d = {"page_id": pid, "template": template, "beat": beat, "one_point": one_point, "zones": zones}; d.update(kw); PAGES.append(d)

TAB = "第2章：問1 D点は「時計回り」で出す"

# ---- P01 章扉（B1）
page("R7-Q21-02-01", "T01 章扉", "B1", "D点は観測角を『足して』求める。（引き算の誤りを予告）",
  [zone("z1", "chapter_header", 0, 200, text=TAB, note="章扉の見出し。章番号と見出しを大きく。背景は章扉らしい淡い帯"),
   zone("z2", "obs_card", 200, 420, frame={"x": 40, "w": 1000}, card_title="観測", card_lines=["T2に器械を据えて", "T1を後視して観測", "観測角325°06′51″", "水平距離25.81m"], rendered_by="code"),
   zone("z3", "dialogue", 620, 1300, chars=[
        {"who": "トリ先生", "mode": "FULL", "emotion": "T2", "side": "right", "note": "指し棒で上のカードを指す"},
        {"who": "藍子", "mode": "FULL", "emotion": "A1", "side": "left", "hands": "片手は胸、もう片手はクリップボード（手は2本）"}],
        bubbles=bub("T1", 0, 4, {3: "観測角325°06′51″"}) + bub("A1", 0, 5, {5: "引き算します！"}),
        reading_order="トリ先生（右上）→ 藍子（左下）の順に、上から下へ")],
  chapter_goal=TAB, hook="藍子の『引き算します！』で終え、次ページで止める",
  source_refs={"turns": ["T1", "A1"], "article": "第2章 冒頭"})

# ---- P02 誤答の寸劇（B3）
page("R7-Q21-02-02", "T04 誤答の寸劇", "B3", "観測角を引くと、D点は甲土地の外（南）へ出てしまう",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 640, chars=[{"who": "トリ先生", "mode": "FULL", "emotion": "T1", "side": "right"}],
        bubbles=bub("T2", 0, 4, {1: "注1", 2: "『観測角は、時計回りの角度を示す』"})),
   zone("z3", "note_card", 710, 240, frame={"x": 40, "w": 1000}, card_title="観測値の表の注1", card_lines=["観測角は、時計回りの角度を示す"], rendered_by="code"),
   zone("z4", "dialogue", 950, 620, chars=[{"who": "藍子", "mode": "FULL", "emotion": "A2", "side": "left", "hands": "片手を口元、もう片手は下ろす（手は2本）"}],
        bubbles=bub("A2", 0, 5, {3: "（172.27, 112.17）"})),
   zone("z5", "wrong_card", 1570, 350, frame={"x": 40, "w": 1000}, card_title="誤り", card_lines=["方向角から325°06′51″を引いて", "（172.27, 112.17）", "A点やE点（X＝184.31）より12mも南です"],
        red_parts=["誤り", "（172.27, 112.17）"], rendered_by="code", note="『誤り』の見出しと誤答の座標だけ赤。ほかは濃紺")],
  hook="トリ先生『やってごらんなさい』→藍子が固まる。答えは次ページ",
  continuity="藍子の服・髪型は前ページと同じ。誤答の座標を赤で示す",
  source_refs={"turns": ["T2", "A2"]})

# ---- P03 訂正と式（B4+B5）
page("R7-Q21-02-03", "T05 計算ページ", "B4+B5", "時計回りの観測角は足す。式は D ＝ T2 ＋ 25.81∠( arg(T1 − T2) ＋ 325°06′51″ )",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 930, chars=[
        {"who": "トリ先生", "mode": "MID", "emotion": "T2", "side": "right"},
        {"who": "藍子", "mode": "FACES", "emotion": "A3", "side": "left", "note": "藍子は話さない（ひらめきの表情だけ。silent_reaction）"}],
        bubbles=bub("T3", 0, 7, {2: "足すのよ", 6: "足すだけで正しい向きになるの"})),
   zone("z3", "calc_card", 1000, 370, frame={"x": 40, "w": 1000}, card_title="式（点名）", card_lines=["D ＝ T2 ＋ 25.81∠( arg(T1 − T2) ＋ 325°06′51″ )"], rendered_by="code"),
   zone("z4", "calc_card", 1370, 190, frame={"x": 40, "w": 1000}, card_title="表示", card_lines=["201.7111… ＋ 114.4118…i"], rendered_by="code"),
   zone("z5", "reaction", 1560, 360, chars=[{"who": "藍子", "mode": "MID", "emotion": "A3", "side": "left", "hands": "片手で指を立てる、もう片手は胸（手は2本）"}, {"who": "トリ先生", "mode": "SMALL", "emotion": "T3", "side": "right"}], bubbles=[], note="吹き出しなし。藍子の『なるほど』の表情を大きく見せる")],
  hook="次ページ：途中の方向角と丸めの補足", continuity="式カード・表示カードの枠は次ページの方向角カードと同じ幅",
  source_refs={"turns": ["T3"], "article": "式（点名）、表示（電卓操作は入れない）"})

# ---- P04 補足（方向角と360°）
page("R7-Q21-02-04", "T07 会話ラリー", "B4", "足すと419°を超えるが、電卓は360°を引いたのと同じ向きで計算してくれる",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 1050, chars=[
        {"who": "トリ先生", "mode": "FACES", "emotion": "T2", "side": "right"},
        {"who": "藍子", "mode": "FACES", "emotion": "A4", "side": "left", "note": "藍子は話さない（確かめる表情だけ）"}],
        bubbles=bub("T4", 0, 7, {3: "94°21′21.94″", 6: "360°を引いたのと同じ向き"})),
   zone("z3", "point_card", 1120, 800, frame={"x": 40, "w": 1000}, card_title="途中の方向角", card_lines=["T2→T1の方向角は 94°21′21.94″", "これに325°06′51″を足すと419°を超える", "360°を引いたのと同じ向き（59°28′12.94″）"], rendered_by="code")],
  hook="次ページ：座標の丸め（注3）と答え", source_refs={"turns": ["T4"], "pieces": "1〜7"})

# ---- P05 丸めと答え＋図2
page("R7-Q21-02-05", "T03 全面図（図2）", "B5", "答えは D点（201.71, 114.41）。図2で位置を確かめる",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 650, chars=[
        {"who": "トリ先生", "mode": "FACES", "emotion": "T2", "side": "right"},
        {"who": "藍子", "mode": "FACES", "emotion": "A4", "side": "left", "note": "藍子は話さない"}],
        bubbles=bub("T4", 7, 12, {9: "注3", 10: "小数第3位を四捨五入"})),
   zone("z3", "answer_banner", 720, 200, frame={"x": 40, "w": 1000}, card_lines=["▶ D点（201.71, 114.41）"], rendered_by="code", note="濃紺の地に白い文字。赤にしない"),
   zone("z4", "figure", 920, 800, figure_ref="zu02", frame={"x": 40, "w": 1000, "h": 750, "y": 945}, fit="contain", rendered_by="code",
        note="図2（T2からの放射）をそのまま。切らない・縦横比を変えない・描き直さない"),
   zone("z5", "reaction", 1720, 200, chars=[{"who": "藍子", "mode": "FACES", "emotion": "A3", "side": "left", "note": "silent"}, {"who": "トリ先生", "mode": "FACES", "emotion": "T3", "side": "right", "note": "silent"}], bubbles=[])],
  hook="次ページ：藍子『D点の杭は…』", source_refs={"turns": ["T4"], "pieces": "8〜12", "marker": 1})

# ---- P06 最大のわな（B3→B4）
page("R7-Q21-02-06", "T04 誤答の寸劇（問いと力説）", "B3+B4", "筆界はC→D→Eと折れている。CとEの直線だと思い込むと、面積もK点もずれる",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 470, chars=[{"who": "藍子", "mode": "MID", "emotion": "A4", "side": "left", "hands": "片手をあごに、もう片手はクリップボード（手は2本）"}],
        bubbles=bub("A3", 0, 4, {4: "C点とE点を結ぶ直線"})),
   zone("z3", "dialogue", 540, 900, chars=[{"who": "トリ先生", "mode": "FULL", "emotion": "T4", "side": "right"}, {"who": "藍子", "mode": "SMALL", "emotion": "A2", "side": "left", "hands": "両手を体の前で下ろす（手は2本）", "note": "silent"}],
        bubbles=bub("T5", 0, 8, {1: "最大のわな", 6: "筆界はC→D→Eと折れている"})),
   zone("z4", "point_card", 1440, 480, frame={"x": 40, "w": 1000}, card_title="今年の最大のわな", card_lines=["筆界はC→D→Eと折れている", "CとEの直線だと思い込んだら"], rendered_by="code")],
  hook="藍子『本当にDが筆界点だって、計算で確かめる方法は…』へ", continuity="図2・図3と同じ点名（C・D・E）",
  source_refs={"turns": ["A3", "T5"]})

# ---- P07 確かめる方法を問う（B4）
page("R7-Q21-02-07", "T07 会話ラリー", "B4", "Dが筆界点か、甲土地の面積と登記記録の559㎡の一致で確かめる",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 420, chars=[{"who": "藍子", "mode": "FACES", "emotion": "A4", "side": "left"}, {"who": "トリ先生", "mode": "FACES", "emotion": "T3", "side": "right", "note": "silent（感心の表情）"}],
        bubbles=bub("A4", 0, 4, {3: "計算で確かめる方法"})),
   zone("z3", "dialogue", 490, 1030, chars=[{"who": "トリ先生", "mode": "FACES", "emotion": "T3", "side": "right"}, {"who": "藍子", "mode": "FACES", "emotion": "A4", "side": "left", "note": "silent"}],
        bubbles=bub("T6", 0, 6, {6: "登記記録の559㎡と比べて"})),
   zone("z4", "point_card", 1520, 400, frame={"x": 40, "w": 1000}, card_title="確かめる", card_lines=["甲土地（206番）", "不動産登記法第14条第1項の地図", "登記記録の559㎡"], rendered_by="code")],
  hook="次ページ：倍面積の式", source_refs={"turns": ["A4", "T6"], "pieces": "T6の1〜6"})

# ---- P08 倍面積の式と答え（B5+B6）
page("R7-Q21-02-08", "T05 計算ページ", "B5+B6", "甲土地の面積は559.8503㎡→559㎡で、登記記録の559㎡とぴったり合う",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 340, chars=[{"who": "トリ先生", "mode": "FACES", "emotion": "T2", "side": "right"}], bubbles=bub("T6", 6, 8, {8: "倍面積の式"})),
   zone("z3", "calc_card", 410, 420, frame={"x": 40, "w": 1000}, card_title="式（点名）",
        card_lines=["甲土地の倍面積 ＝ A・Conjg(B) ＋ B・Conjg(C) ＋ C・Conjg(D)", "＋ D・Conjg(E) ＋ E・Conjg(A)"], rendered_by="code"),
   zone("z4", "calc_card", 830, 170, frame={"x": 40, "w": 1000}, card_title="表示", card_lines=["（実部）− 1119.7006i"], rendered_by="code"),
   zone("z5", "dialogue", 1000, 620, chars=[{"who": "藍子", "mode": "MID", "emotion": "A5", "side": "left", "hands": "両手を小さくガッツポーズ（手は2本）"}, {"who": "トリ先生", "mode": "SMALL", "emotion": "T3", "side": "right", "note": "silent"}],
        bubbles=bub("A5", 0, 5, {2: "559.8503㎡", 4: "559㎡！", 5: "登記記録とぴったり"})),
   zone("z6", "answer_banner", 1620, 300, frame={"x": 40, "w": 1000}, card_lines=["559.8503㎡", "畑の地積は1㎡未満を切り捨てる", "559㎡", "登記記録とぴったりです！"], rendered_by="code", note="4行を縦に。濃紺の地に白い文字")],
  hook="次ページ：CとEの直線だと587.25㎡で28㎡も合わない（図3）", source_refs={"turns": ["T6", "A5"], "pieces": "T6の7〜8"})

# ---- P09 比較図3と章末（B6+B7）
page("R7-Q21-02-09", "T06 検算の比較（図3）＋章末", "B6+B7", "CとEの直線は587.25㎡で28㎡も合わない。隣の土地の地積との一致で筆界点を裏付ける",
  [zone("z1", "tab", 0, 70, text=TAB),
   zone("z2", "dialogue", 70, 920, chars=[{"who": "トリ先生", "mode": "MID", "emotion": "T4", "side": "right"}, {"who": "藍子", "mode": "FACES", "emotion": "A5", "side": "left", "note": "silent（納得の表情）"}],
        bubbles=bub("T7", 0, 7, {2: "587.25㎡", 3: "28㎡も合わない", 6: "一致も使える"})),
   zone("z3", "figure", 990, 800, figure_ref="zu03", frame={"x": 40, "w": 1000, "h": 750, "y": 1015}, fit="contain", rendered_by="code",
        note="図3（花子の説明のCとEの直線と、杭Dを通す場合の比較）をそのまま"),
   zone("z4", "next_chapter_tag", 1790, 130, frame={"x": 40, "w": 1000}, card_lines=["第3章：問1 K点は「実測の面積」で2等分"], rendered_by="code", note="次章の予告。章見出しの文字列そのまま。小さな帯")],
  hook="次章へ。章末の一言は記事の『覚えておきなさい』で終える", source_refs={"turns": ["T7"], "marker": 2})

SPEC = {
  "meta": {"id": "R7-Q21-ch02", "title": "令和7年度 問題21（土地） 第2章 問1 D点は「時計回り」で出す", "status": "draft-pilot", "created": "2026-10-08",
           "article": ARTICLE, "decisions": {"production": "A′", "calculator_keys": "漫画に入れない", "dialogue": "記事の文言のまま分割", "red": "UIでは誤り・訂正の箇所だけ（図の赤は制限しない）"}},
  "global": GLOBAL, "figures": FIG, "turns": [{"turn_id": t, "speaker": w, "text": s, "pieces": SPLIT[t]} for t, (w, s) in zip(TURN_IDS, TURNS)],
  "pages": PAGES,
}

def kouseihyou():
    L = ["# R7/Q21 第2章 学習漫画 ページ構成表（パイロット・文言の正本）", "",
         f"- 章：{TAB}（9ページ）　キャンバス 1080×1920px　合成方式 A′（図・計算カード・答えバナーは仮枠にコードで合成）",
         "- セリフは記事の文言のまま分割（結合すると記事と一致。`check_pages.py` で照合）　電卓操作は入れない",
         "- 赤は誤り・訂正の箇所だけ（UI）。答えは濃紺の帯。図の赤は制限しない", ""]
    for p in PAGES:
        L += [f"## {p['page_id']}　{p['template']}（{p['beat']}）", f"**このページの1点**：{p['one_point']}", ""]
        L += ["| 区画 | y〜h(px) | 種類 | 内容（正本） |", "|---|---|---|---|"]
        for z in p["zones"]:
            c = []
            if z.get("text"): c.append(z["text"])
            if z.get("card_title"): c.append(f"【{z['card_title']}】")
            if z.get("card_lines"): c.append(" ／ ".join(z["card_lines"]))
            if z.get("figure_ref"): c.append(f"図 {z['figure_ref']}（{FIG[z['figure_ref']]['file'].split('/')[-1]}）")
            if z.get("chars"): c.append("キャラ：" + "、".join(f"{x['who']}{x['mode']}({x['emotion']})" for x in z["chars"]))
            if z.get("bubbles"):
                c.append("<br>".join(f"{b['id']} {b['speaker']}：「{b['text']}」" + (f"〔強調：{b['highlight']}〕" if b.get('highlight') else "") for b in z["bubbles"]))
            L.append(f"| {z['zone_id']} | {z['y']}＋{z['h']} | {z['type']} | " + "<br>".join(c) + " |")
        L += ["", f"- 引き：{p.get('hook', '—')}", ""]
    return "\n".join(L)

if __name__ == "__main__":
    (HERE / "R7-Q21-ch02_page_spec.json").write_text(json.dumps(SPEC, ensure_ascii=False, indent=2), encoding="utf8")
    (HERE / "R7-Q21-ch02_kouseihyou.md").write_text(kouseihyou(), encoding="utf8")
    print("generated", len(PAGES), "pages")
