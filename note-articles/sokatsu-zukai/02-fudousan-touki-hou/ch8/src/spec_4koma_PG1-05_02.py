"""D1588・D1589・D1501 の4コマ解説図解の設計データ（SPEC）と見出し画像の設定（HEADER）。v01（2026-10-13）。
総合記事②不動産登記法編 第8章【PG1-5】用（3本目）。R02-Q15オ（区分に伴い敷地権の割合が変わった場合の原因は『変更』・〇／『分割』・×）／R01-Q18エ（敷地権の地上権が存続期間満了で消えた場合の原因は『敷地権消滅』・〇）。
『割合が変わった→変更（分割ではない）』と『権利が消えた→敷地権消滅（非敷地権ではない）』の2つの混同に絞り、型4（別々の場面を比較表で並べる）に型5（整理カード併用）を組み合わせた。
『敷地権』と『新築』の混同（D1587）は既存の D1580・D1583・D1587 の4コマが扱う。"""

SPEC = dict(
    ippatsu=True, purpose=True,
    id="D1588・D1589・D1501", fid="D1588-D1589-D1501", topic="不動産登記法／区分建物・敷地権・共用部分",
    src="R02-Q15オ／R01-Q18エ",
    truth="D1588＝〇（正しい記述）／D1589＝×（誤った記述）／D1501＝〇（正しい記述）",
    miscon="区分に伴う割合の変更の原因を『分割』と書く、敷地権が消える場合の原因を『非敷地権』と書く、と取り違える（原因の文言が場面ごとに決まっていることが定着していない）",
    article="note-articles/r2-mondai/q15-touki-kiroku-anaume.md",
    art_head="オ（区分後の割合変更の原因は『年月日変更』）。ほか、R01-Q18エ（note-articles/r1-mondai/q18-kubun-tatemono.md。敷地権の地上権が存続期間満了で消えたら『年月日敷地権消滅』）",
    letters="",
    design=[
        "【出題者のひっかけ】D1589は、D1588と場面の説明を一字違わずに並べ、原因の文言だけを『分割』にする。区分登記なのだから『分割』と書きそう、と思わせる。D1501は『敷地権でなくなる』という点で、規約で外れたときの『非敷地権』と似た言葉を選ばせる。",
        "【受験者の勘違い・定着していない点】（推測）①区分して割合が変わるので、原因も『分割』と書くと考える。②敷地権が消える場合の原因が、地上権の期間満了なら『敷地権消滅』、規約で分離処分可能にしたなら『非敷地権』と、場面ごとに分かれることが定着していない。③原因の文言は条文に明記がなく、実務の書き方なので、理屈で導こうとして外す。",
        "【対比する制度】「変更」⇔「分割」：区分に伴って敷地権の割合が変わった場合の原因は『年月日変更』で、『分割』とは書かない（実務の取扱い）。「敷地権消滅」⇔「非敷地権」：敷地権の地上権が存続期間満了で消えた場合は『年月日敷地権消滅』、規約で分離処分可能にしたことで敷地権でなくなった場合は『年月日非敷地権』（書き分けが必要な点）。",
        "【型の選び方】型：型4（別々の場面を比較表で並べる）＋型5（整理カード併用）。理由：3肢は別々の場面（割合の変更、地上権の期間満了による消滅）で、共通の日付がないので、コマ1は場面と問いの比較、コマ2は『割合が変わった』と『権利が消えた』の左右の対比、コマ3の右側は会話1往復と、原因の文言4つの整理カード。壁＝『似た文言を場面と結びつけられない』。",
        "コマごとに読者が言えること：コマ1＝割合が変わったとき、地上権が期間満了で消えたとき、原因の欄に何と書くか。コマ2＝割合が変わったら『年月日変更』、権利が消えたら『年月日敷地権消滅』。コマ3＝原因の文言は4つ。『非敷地権』は規約で外れたとき。コマ4＝D1588・D1501は〇、D1589は×。",
        "記事の範囲：R02-Q15オ（実務の取扱いで『年月日変更』）、R01-Q18エ（記録の文言は条文に明記がなく、登記実務・先例の取扱い。『非敷地権』とは書き方が異なる）。整理カードの1行目（最初に生じたときは『年月日敷地権』）は R02-Q15エ（D1586・D1587）の記事の整理。",
        "登場人物：人型は使わず、場面と原因の言葉は文字のカードで示す。",
        "矢印の意味：矢印は使わない。コマ1は縦3枚のカード、コマ2は左右のカード、コマ3は上下のカードと整理カード。",
        "配色：コマ1・2は印（✓✕）を付けない。コマ3の左は上＝✕、下＝✓の1個ずつ。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。",
        "コマの使い方（キャラは不必要に小さくしない）：コマ1＝side、コマ2＝none（図が主役）、コマ3＝faces（左に上下2枚のカード、右に会話2つと整理カード）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。",
    ],
    review=[
        "初見の読者：コマ1で2つの場面（割合の変更、期間満了による消滅）と問い、コマ2で場面ごとの原因の文言の対比、コマ3で4つの文言の整理が言える",
        "構成表の全文言を記事（R02-Q15オ、R01-Q18エ）と突き合わせ済み。原因の文言は条文に明記がなく実務の取扱いであることを図に入れた（断定しない）",
        "コマ1・2に印がなく、コマ3の左は上＝✕・下＝✓の1個ずつ、コマ4だけ青✓。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラを小さくしたコマはない",
        "肝の確認：①区分で割合が変わった→年月日変更（分割ではない） ②地上権の存続期間満了で敷地権が消えた→年月日敷地権消滅 ③規約で分離処分可能にして敷地権でなくなった→年月日非敷地権 ④D1588・D1501は〇、D1589は×",
    ],
    extra_refs=[
        "原因の文言（年月日敷地権・年月日変更・年月日敷地権消滅・年月日非敷地権）は条文・規則に明記がなく、登記実務の取扱い（記事 R02-Q15オ・R01-Q18エ、R02-Q15エの整理）。敷地権の登記原因及びその日付を記録する根拠は不動産登記規則118条（法令DB note-articles/laws/fudousan-touki-kisoku-1.md で確認）。",
    ],
    lead1="区分登記に伴って、敷地権の割合が3分の1から6分の1に変わりました。敷地権の表示の原因及びその日付の欄には、どのような言葉を書くのでしょうか。",
    title="区分で割合が変わったら、原因は変更", title_hl="原因は変更",
    panels=[
        dict(label="①　原因の欄には、何と書く？", chars="side", mood="curious, calm mood",
             bubbles=[("藍子", "区分したから、原因は分割ですよね？", None, "区分したから、\n原因は分割\nですよね？"),
                      ("トリ先生", "出たわね。その言葉は書かないのよ", "書かない", "出たわね。\nその言葉は\n書かないのよ")],
             fig=["A diagram in the center, about 56 percent of the panel width: three SEPARATE cards stacked from top to bottom, all the same size, each with the same pale gray fill, a dark navy outline, a small dark navy dot at its left end (NO number, NO digit, NO letter on the dots, so that they cannot be confused with the circled panel numbers), and one dark navy text line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.",
                  "Card 1: 「区分で、割合が3分の1から6分の1に」. Card 2: 「地上権が、存続期間の満了で消えた」. Card 3: 「原因の欄に書く言葉は？」.",
                  "At the top, a small question badge in a gray fill with dark navy text 「場面ごとに、原因の言葉は違う？」 (a question badge only, with no check mark and no cross).",
                  "There is no check mark and no cross anywhere in this panel."]),
        dict(label="②　割合が変わる、権利が消える", chars="none", mood="clear, calm infographic mood",
             bubbles=[],
             fig=["A small dark navy tag 「敷地権の表示の原因」 at the top left, with one line beside it: 「場面で、言葉が決まる」.",
                  "Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.",
                  "Left card, heading 「割合が変わったとき」, a small tag 「割合の場面」, two body lines: 「年月日変更」, 「区分登記でも、分割とは書かない」.",
                  "Right card, heading 「敷地権が消えたとき」, a small tag 「消滅の場面」, two body lines: 「地上権の期間満了など」, 「年月日敷地権消滅」.",
                  "Under the two cards, one wide dark navy band with large white text 「割合の変更と、権利の消滅は別の言葉」.",
                  "The two cards have clearly different texts; the texts are NOT identical."]),
        dict(label="③　原因の言葉は4つ", chars="faces", opposite="lx", mood="thoughtful then confident mood",
             bubbles=[("藍子", "消えたときは、非敷地権ですか？", None, "消えたときは、\n非敷地権ですか？"),
                      ("トリ先生", "いいえ。期間満了なら敷地権消滅よ", "敷地権消滅", "いいえ。\n期間満了なら\n敷地権消滅よ")],
             fig=["LEFT SIDE: two stacked cards of the same size, top and bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card, with no arrow and no connector. The cards are separated only by a small empty gap.",
                  "Top card, heading 「割合の変更も、分割と書く」, body 「分割と書く言い方」, and ONE red cross only at the bottom of this card (no check mark on this card).",
                  "Bottom card, heading 「割合の変更は、年月日変更」, body 「変更と書く言い方」, and ONE blue check mark only at the bottom of this card (no cross on this card).",
                  "RIGHT SIDE, under the two speech bubbles (the two speech bubbles and their two faces stay at the top of the right side): one tall list card with a dark navy heading 「敷地権の表示の原因」, with the same pale gray fill and a dark navy outline, containing exactly four short rows, each with a small dark navy dot at its left end (NO digit and NO letter on the dots), with no arrow and no check mark and no cross: 「最初に生じた　年月日敷地権」, 「割合が変わった　年月日変更」, 「権利が消えた　年月日敷地権消滅」, 「規約で外れた　年月日非敷地権」, with the third row highlighted with a yellow marker. Under the four rows, one small dark navy ribbon tag with white text 「文言は条文になく、実務の取扱い」.",
                  "The list card is a part of the right side, and it is NOT a speech bubble. The left cards and the list card have clearly different texts; the texts are NOT identical."]),
        dict(label="④　結論は〇・×・〇",
             bubbles=[("藍子", "場面ごとに、言葉を覚えるんですね！", None, "場面ごとに、\n言葉を覚える\nんですね！"),
                      ("トリ先生", "そう。分割と非敷地権に注意よ", "分割と非敷地権", "そう。\n分割と非敷地権に\n注意よ")],
             fig=[], checklist=["区分に伴う割合の変更は、年月日変更。分割とは書かない", "地上権の期間満了で敷地権が消えたら、年月日敷地権消滅", "規約で分離処分可能にしたときは、年月日非敷地権"])
    ],
    band1="割合が変われば変更、権利が消えれば敷地権消滅", band2="問題D1588・D1589・D1501　正解〇・×・〇（R02-Q15オ／R01-Q18エ）",
    ver="v01",
    rev=["2026-10-13 v01：新規作成（総合記事②不動産登記法編 第8章【PG1-5】用。型4（場面を並べる）＋型5。割合の変更と権利の消滅で原因の文言が違う点に絞った）"],
)

HEADER = dict(h1="区分して割合が変わる", h2="原因は何と書く？", hkey="何と書く？",
              scene_l="a building ledger page with one blank line being filled by a pen, no text",
              scene_r="a pie chart that is divided into smaller slices, no text")
