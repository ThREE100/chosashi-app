"""D0646・D0743 の4コマ解説図解の設計データ（SPEC）と見出し画像の設定（HEADER）。v02（2026-10-11、最新ルールでの作り直し）。
H23-Q08ア（抵当権を消すとき、転抵当権者の承諾も要る）とH24-Q07ウ（要役地の地役権を消すとき、土地の抵当権者の承諾も要る）。
v02：決め手の対比（本人の承諾だけ⇔第三者の承諾も併せて）と、その理由（消える権利で影響を受ける人がいる）に絞った。
抵当証券・土地の所有者は承諾しないという周辺情報は外した。"""


def B(who, text, hl=None, brk=None):
    return [who, text, hl, brk] if brk else [who, text, hl]


NOTE = "条文別『苦手克服』シリーズ（note-articles/joubun-nigate/）の第40条用。"

SPEC = dict(
    ippatsu=True, purpose=True,
    id="D0646・D0743", fid="D0646-D0743",
    topic="不動産登記法／土地の分筆・合筆・地積更正",
    src="H23-Q08ア／H24-Q07ウ",
    truth="D0646・D0743＝〇",
    miscon="承諾の情報の範囲（権利者本人だけで足りるか、第三者の承諾も要るか）",
    article="note-articles/h23-mondai/q08-bunpitsu-gappitsu-kenri.md",
    art_head="ア「抵当権を消すには、その上の第三者の承諾も要る」。ほか、H24-Q07ウ（q07-bunpitsu.md）",
    letters="",
    design=[
        "【型の選び方】型：型4（2肢の対比）＋型3（理由説明）。理由：壁は『本人の承諾だけでは足りないのはなぜか』と、抵当権の場面と要役地の地役権の場面で承諾する第三者が誰かが結びつかないこと。コマ2で『本人の承諾だけ』と『第三者の承諾も併せて』を左右に並べ、コマ3で『消える権利で影響を受ける人がいるから』という理由と、2つの場面の当てはめ（転抵当権者／土地の抵当権者）を示す。",
        "【出題者のひっかけ】どちらの肢も、『〜のほか、〜も提供しなければならない』と、本人の承諾の情報にもう一人分の承諾の情報を足す書き方をしている。権利を消すのは権利者本人の承諾で足りると考える受験者に、足りない分があることを見落とさせる（記事 H23-Q08ア、H24-Q07ウ）。",
        "【受験者の勘違い・定着していない点】（推測）①権利を消す承諾の情報は、消える権利の登記名義人（抵当権者・地役権者）の分だけで足りると考える。②第三者の承諾が要ることは覚えていても、なぜ要るのか（消える権利で影響を受ける人がいるから）と、誰の承諾なのか（抵当権なら転抵当権者、要役地の地役権なら土地の抵当権者）が結びついていない。",
        "【対比する制度】「本人の承諾だけ」⇔「第三者の承諾も併せて」：どちらも分筆で権利を消す承諾の情報の話。本人の承諾の情報だけでは足りず、その権利を目的とする第三者（抵当権では転抵当権者、要役地の地役権では土地の抵当権者）の承諾の情報も併せて提供する（法40条かっこ書、規則104条1項2号・6項）。結論が逆になるのは、本人だけで足りるか、第三者の分も要るか。",
        "記事の範囲：H23-Q08ア（法40条かっこ書、規則104条1項2号。抵当権の登記がある土地を分筆し乙土地の抵当権を消すとき、その抵当権を目的とする第三者の権利に関する登記があれば、抵当権者の承諾の情報のほか、その第三者の承諾の情報も提供する。第三者の権利も抵当権の消滅によって影響を受けるから。たとえば転抵当）とH24-Q07ウ（規則104条6項。要役地の地役権を消すとき、分筆前の土地に抵当権の登記があれば、地役権者が作成した情報のほか、抵当権者の承諾の情報も提供する。地役権は要役地の担保価値にも影響し、抵当権者の利益を保護する必要があるから）。",
        "extra_refs：①不動産登記法40条かっこ書・不動産登記規則104条1項2号・6項の原文は法令DB（note-articles/laws/fudousan-touki-hou.md・fudousan-touki-kisoku-1.md）で確認した。②コマ3の『消える権利で影響を受ける人がいる』という共通の言い方は、記事アの『第三者の権利も抵当権の消滅によって影響を受ける』とウの『地役権は要役地の担保価値にも影響するため、抵当権者の利益を保護する必要がある』を1つにまとめた整理で、記事にまとめた一文はない（ユーザーに伝える）。立法趣旨の断定はしていない。",
        "登場人物：当事者の記号（Ａ〜Ｚ）は使わない。人は文字ラベル（転抵当権者・土地の抵当権者）だけで示す。",
        "矢印の意味：矢印は使わない。コマ1は縦2枚の別カード、コマ2は左右のカード、コマ3は縦3枚の別カード。",
        "配色：コマ1〜3は印（✓✕）を付けない（コマ2の左右も、説明の対比であり正誤の印は付けない）。コマ4の暗記3点だけ青✓。カードは薄い灰色・濃紺の枠、強調は黄色マーカーだけ。",
        "コマの使い方（キャラの大きさ）：不必要に小さくしない。コマ1＝side（キャラは通常サイズで左右の端、図は中央のカード2枚と疑問バッジ。図の量が少ないので小さくする必要がない）、コマ2＝none（図が主役。左右のカードと帯）、コマ3＝faces（左に理由のカード3枚、右に会話4つの縦並び。カードと会話の量が多いので顔アイコンにして場所を確保）、コマ4＝既定（両方・通常サイズ）。隣り合うコマで同じ見せ方が続かない。",
    ],
    review=[
        "初見の読者：コマ1で『分筆して乙土地の権利を消す。抵当権に転抵当権があるとき／要役地の地役権を消すとき、承諾の情報はだれの分が要る？』、コマ2で『本人の承諾だけでは足りず、第三者の承諾も併せて要る（抵当権なら転抵当権者、地役権なら土地の抵当権者）』、コマ3で『消える権利で影響を受ける人がいるから、その人の承諾も要る』が言える",
        "肝の確認：①抵当権を消すとき：転抵当権者の承諾も要る（法40条かっこ書） ②要役地の地役権を消すとき：土地の抵当権者の承諾も要る（規則104条6項） ③理由：消える権利で影響を受ける人がいるから ④肢D0646・D0743はどちらも〇",
        "構成表の全文言を記事・法令DBと突き合わせ：『転抵当権者』『土地の抵当権者』『要役地の担保価値に影響』『抵当権者の利益を守る』『分筆の申請情報と併せて』。抵当証券・土地の所有者は承諾しないという周辺情報は入れていない",
        "コマ1〜3に印がなく、コマ4だけ青✓の暗記3点。コマの使い方は side→none→faces→既定 で隣り合うコマが同じにならない。キャラは、図や会話が入らないコマだけ小さくしている（小さくしたコマはない）",
    ],
    extra_refs=[
        "不動産登記法40条かっこ書（法令DB note-articles/laws/fudousan-touki-hou.md 第40条）：権利を目的とする第三者の権利に関する登記がある場合にあっては、当該第三者が承諾したことを証する情報が併せて提供されたときに限る。不動産登記規則104条1項2号・6項（同 fudousan-touki-kisoku-1.md 第104条）：1項2号＝前号の権利を目的とする第三者の権利に関する登記があるときは、当該第三者が承諾したことを証する情報。6項＝要役地の地役権を消滅させるとき、当該土地を目的とする第三者の権利に関する登記がある場合は、当該第三者が承諾したことを証する情報が併せて提供されたときに限る。1項2号は記事のア、6項は記事のウにある。",
        "『消える権利で影響を受ける人がいる』：記事アの『第三者の権利も抵当権の消滅によって影響を受ける』と、ウの『地役権は要役地の担保価値にも影響するため、抵当権者の利益を保護する必要がある』を1つにまとめた整理。記事にまとめた一文はない。立法趣旨としては断定しない",
    ],
    lead1="分筆した土地の権利を消すとき、抵当権に転抵当権があるときや、要役地の地役権を消すときに、承諾の情報は権利者本人の分だけで足りるのでしょうか。",
    title="権利を消すには、第三者の承諾の情報も併せて出す", title_hl="第三者の承諾の情報",
    panels=[
        dict(label="①　権利を消すとき、だれの承諾？", chars="side", mood="curious, calm mood",
             bubbles=[B("藍子", "権利者が承諾すれば、足りますよね？", None, "権利者が承諾すれば、\n足りますよね？"),
                      B("トリ先生", "出たわね。本人だけに目が行ったわね", "本人だけ", "出たわね。\n本人だけに\n目が行ったわね")],
             fig=["A diagram in the center, about 56 percent of the panel width: a small dark navy tag 「分筆して、乙土地の権利を消す」 at the top, and below it two SEPARATE cards stacked from top to bottom, both exactly the same size, each with the same pale gray fill, a dark navy outline, a dark navy heading placed fully INSIDE the card, and one dark navy body line. Do NOT draw any arrow anywhere in this panel and do NOT connect the cards; they are separated only by a small empty gap.",
                  "Card 1, heading 「抵当権を消す」, body 「その抵当権に転抵当権がある」. Card 2, heading 「要役地の地役権を消す」, body 「分筆前の土地に抵当権がある」.",
                  "At the bottom, a small question badge in a gray fill with dark navy text 「承諾の情報は、だれの分が要る？」 (a question badge only, with no check mark and no cross).",
                  "There is no check mark and no cross anywhere in this panel."]),
        dict(label="②　本人だけか、第三者も併せてか", chars="none", mood="clear, calm infographic mood",
             bubbles=[],
             fig=["A small dark navy tag 「どちらの場面でも」 at the top left, with one line beside it: 「承諾の情報は、本人の分で足りるか」.",
                  "Two large cards side by side in the center, both exactly the same size and top-aligned, each with its dark navy heading placed fully INSIDE the card, with the same pale gray fill and a dark navy outline, and with no check mark and no cross.",
                  "Left card, heading 「本人の承諾だけ」, two body lines: 「抵当権者や地役権者の分だけ」, 「これでは足りない」.",
                  "Right card, heading 「第三者の承諾も併せて」, two body lines: 「抵当権なら、転抵当権者の分」, 「地役権なら、土地の抵当権者の分」.",
                  "Under the two cards, one wide dark navy band with white text in two lines: 「本人の分に加えて、第三者の分も揃える」 and 「分筆の申請情報と併せて提供する」.",
                  "The two cards have clearly different texts; the texts are NOT identical."]),
        dict(label="③　なぜ、第三者の承諾が要る？", chars="faces", mood="thoughtful then confident mood",
             bubbles=[B("藍子", "なぜ、本人以外の承諾が要るんですか？", None, "なぜ、本人以外の\n承諾が要るんですか？"),
                      B("トリ先生", "消える権利に、影響を受ける人がいるの", "影響を受ける人", "消える権利に、\n影響を受ける人がいるの"),
                      B("藍子", "地役権の場合は、だれが影響を受けます？", None, "地役権の場合は、\nだれが影響を受けます？"),
                      B("トリ先生", "要役地に抵当権があれば、その人よ", "要役地に抵当権", "要役地に抵当権が\nあれば、その人よ")],
             fig=["Three stacked cards of the same size, from top to bottom, with the same pale gray fill and a dark navy outline, each with a dark navy heading placed INSIDE the card and two short body lines, with no arrow, no connector, no check mark, and no cross. The cards are separated only by a small empty gap.",
                  "Card 1, heading 「権利が消えると、影響を受ける人がいる」, body 「その人の承諾の情報も、併せて要る」, and a dark navy ribbon tag with large white text 「ひっかけ：本人の承諾にだけ目が行く」.",
                  "Card 2, heading 「抵当権を消すとき」, body 「抵当権が消えると」 and 「転抵当権者の権利に影響する」.",
                  "Card 3, heading 「要役地の地役権を消すとき」, body 「要役地の担保価値に影響する」 and 「抵当権者の利益を守るため」.",
                  "There is no check mark and no cross anywhere in this panel."]),
        dict(label="④　結論は第三者の分も併せて",
             bubbles=[B("藍子", "影響を受ける人の分も、揃えるんですね！", None, "影響を受ける人の分も、\n揃えるんですね！"),
                      B("トリ先生", "そのとおり。分筆の申請と併せて出すのよ", "併せて出す", "そのとおり。\n分筆の申請と\n併せて出すのよ")],
             fig=[],
             checklist=["抵当権を消すとき：転抵当権者の承諾も要る（法40条かっこ書）",
                        "要役地の地役権を消すとき：土地の抵当権者の承諾も要る（規則104条6項）",
                        "理由：消える権利で影響を受ける人の承諾も必要"]),
    ],
    band1="本人に加え、第三者の承諾も併せて出す", band2="問題D0646・D0743　正解どちらも〇",
    ver="v02",
    rev=["2026-10-09 v01：初版（" + NOTE + "承諾する人の範囲を問う2肢を1本にまとめた）",
         "2026-10-11 v02：最新ルールでの作り直し。決め手の対比（本人の承諾だけ⇔第三者の承諾も併せて）と理由（消える権利で影響を受ける人がいる）に絞り、抵当証券・土地の所有者は承諾しないという周辺情報を外した。コマ2を左右の対比カード、コマ3を理由の3枚カードにして、コマ1はキャラを通常サイズ（side）のまま"],
)

HEADER = dict(h1="権利を消す分筆", h2="だれの承諾が要る？", hkey="要る？",
              scene_l="a plot of land with a small bank building icon beside it and a boundary line, no text",
              scene_r="two blank paper sheets with signature lines and a rubber stamp, no text")
