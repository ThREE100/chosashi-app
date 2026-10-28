def kj(*ss, n=14):
    out = []
    for s in ss:
        for c in s:
            if '一' <= c <= '龥' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='一室の一部が低くても床面積に入る',
    intro='建物の床面積を、どう測り、どの部分を数えるのかを問う問題です（不動産登記規則115条、不動産登記事務取扱手続準則82条）。天井の低い部分、一棟の建物と専有部分の測り方の違い、壁で囲まれた駐車スペース、ダストシュート、屋上の階段室が登場します。\n\nこの記事では、「床面積に入るもの」と「入らないもの」の分かれ目を、具体的な場面で確認していきましょう。この問題は「正しいもの」の組合せを選ぶ形式です。',
    sections={
        'ア': ('一室の一部の天井が低くても、その部屋の面積に入る',
               '天井の高さが1.5メートル未満の地階や屋階（特殊階）は、床面積に算入しません。ただし、1室の一部が天井の高さ1.5メートル未満であっても、その部分は当該1室の面積に算入します（不動産登記事務取扱手続準則82条1号）。\n\n2階の洋室は、屋根の勾配のため一部の天井が1.2メートルしかありません。しかし、一つの部屋の一部ですから、その部分も洋室の面積に入ります。本肢は正しいといえます。\n\n**たとえば**、屋根の傾きに沿って天井が低くなっている部屋では、低い端の部分も含めて、部屋の床の面積全体を数えます。天井が低い端だけを除くことはしません。'),
        'イ': ('一棟の建物の床面積は、壁の中心線で測る',
               '建物の床面積は、各階ごとに壁その他の区画の中心線で囲まれた部分の水平投影面積により定めます。内側線で測るのは、区分建物の場合です（不動産登記規則115条かっこ書）。\n\n区分建物が属する一棟の建物は、それ自体が区分建物ではありません。壁の中心線で測ります。問題文は、専有部分と同様に内側線で測るとしているので、本肢は誤りです。\n\n**たとえば**、マンションの一棟全体の床面積は、外壁などの壁の中心線で囲んだ面積です。そのマンションの各部屋（専有部分）は、壁の内側の線で囲んだ面積で測ります。'),
        'ウ': ('三方が壁の駐車スペースは、前面が開いていても床面積に入る',
               '1階の駐車スペースが、三方を壁で囲まれていて、前面にはシャッターがなく常時開放されている場合でも、床面積に算入する扱いです。囲まれた三方の壁と上階の床によって、独立した空間として画されていると評価できるためです。\n\n本肢は正しいといえます。\n\n**たとえば**、家の1階をコの字形の壁でくり抜いて車庫にした場合、正面にシャッターを付けていなくても、その車庫の部分は建物の床面積に入ります。'),
        'エ': ('建物の内部にあるダストシュートは、外側に及んでいても全体を数える',
               '建物の内部に煙突やダストシュートがある場合には、その部分は各階の床面積に算入します。その一部が外側に及んでいるものも含みます。算入しないのは、外側にあるときです（不動産登記事務取扱手続準則82条10号）。\n\n問題文は、外側に及んでいる部分を算入しないとしています。かっこ書の「一部が外側に及んでいるものを含む」を見落としているので、本肢は誤りです。\n\n**たとえば**、事務所の内部に設けたダストシュートが、外壁の外に少しはみ出していても、はみ出した部分を含めて、ダストシュート全体が各階の床面積に入ります。'),
        'オ': ('屋上への出入口だけの階段室は、高さがあっても算入しない',
               '屋階にある、屋上への出入口のためだけに使われる階段室は、天井の高さが1.5メートル以上であっても、床面積に算入しない扱いです。1.5メートルという数字は、天井が低い特殊階を数えるかどうかの基準で、この階段室の判断には当てはまりません。\n\n問題文は、天井の高さが1.5メートル以上だから算入するとしているので、本肢は誤りです。\n\n**たとえば**、ビルの屋上に出るためだけに設けた小さな塔屋は、天井が2.2メートルあって高さが十分でも、床面積には入りません。'),
    },
    summary=[
        ('ア', '正', '1室の一部の天井が1.5メートル未満でも、その部分は当該1室の面積に算入する'),
        ('イ', '誤', '一棟の建物の床面積は壁の中心線で測り、内側線で測るのは区分建物（専有部分）'),
        ('ウ', '正', '三方が壁で囲まれた駐車スペースは、前面が常時開放でも床面積に算入する'),
        ('エ', '誤', '建物の内部にあるダストシュートは、一部が外側に及んでいても各階の床面積に算入する'),
        ('オ', '誤', '屋上への出入口だけの階段室は、天井の高さが1.5メートル以上でも算入しない'),
    ],
    summary_tail='アは「一室の一部」、エは「かっこ書き」、オは「1.5メートルの使いどころ」がひっかけでした。数字の基準は、どの場面のものかまでセットで覚えましょう。',
    supplements=[
        '### 補足説明（イ）：壁の中心線と内側線の使い分け\n\n床面積を測る線は、どの建物の床面積かによって違います（不動産登記規則115条）。\n\n| 床面積を測る対象 | 測る線 |\n|---|---|\n| 区分建物でない建物 | 壁その他の区画の中心線 |\n| 区分建物の専有部分 | 壁その他の区画の内側線 |\n| 区分建物が属する一棟の建物 | 壁その他の区画の中心線（区分建物ではないため） |\n\n**たとえば**、マンションの一棟全体の面積は外壁の中心線で測り、各部屋の面積は壁の内側で測ります。そのため、各部屋の面積を全部足しても、一棟全体の面積にはなりません。共用部分や壁の厚みの分が、足し合わせには含まれないからです。',
        '### 補足説明（エ・オ）：床面積に入る部分、入らない部分\n\n「入るか、入らないか」で迷いやすい部分を、場面ごとに整理します。\n\n| 部分 | 床面積 |\n|---|---|\n| 内部にあるダストシュート（一部が外側に及ぶものを含む） | 入る |\n| 外側にあるダストシュート | 入らない |\n| 建物に附属する屋外の階段 | 入らない |\n| 屋上への出入口だけの階段室（天井の高さ1.5メートル以上でも） | 入らない |\n| 吹抜になっている部分（上階の床面積として） | 入らない |\n\n**たとえば**、建物の中に収まるダストシュートは数えますが、外にあるものは数えません。同じように、外の階段や、屋上に出るだけの階段室も数えません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第79日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則115条、不動産登記事務取扱手続準則82条1号・7号・8号・10号は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウ（三方が壁の駐車スペース）とオ（屋上への出入口だけの階段室）は、準則に直接の号がなく、建物の認定（外気との分断性など）に沿った登記実務上の扱いに基づく説明です。取扱いの根拠となる通達・先例の原文は未確認です。特にオは、階段室を各階の床面積に算入するとする準則82条6号との関係を、手元の原文では確認できていません。',
        'イの「一棟の建物は壁の中心線で測る」は、規則115条のかっこ書が区分建物にのみ内側線を定めていることからの整理です。各具体例（屋根裏の洋室、コの字形の車庫、塔屋など）は条文を日常の場面にかみ砕いた説明です。',
    ],
    phrases=['一室の一部が低くても数えます', '一棟の建物は壁の中心で測ります', '三方が壁なら車庫は床面積です', '内部のダストシュートは数えます', '屋上の出入口だけの階段室は別です'],
    header=dict(t1='床面積に入る？', t2='入らない？', topic='不動産登記規則　建物の床面積',
                kanji='床・面・積・建・物・規・則・毎'),
    poster_intro='建物の床面積を、「測り方と天井の高さ」（グループA：ア・イ・ウ）と「入るもの・入らないもの」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の床面積を整理', sub='不動産登記規則 第115条と準則 第82条（毎日ドリル 第79日）',
        col_a='測り方と天井の高さ', col_b='入る部分と入らない部分', n_a=3,
        cards=[
            dict(h='一室の一部が低くても算入',
                 ill='a cross-section of a room with a sloped ceiling. The low corner part of the room is shaded green together with the rest of the floor of the room. A height marker is drawn near the low part without any number.',
                 words=[], tag='部屋全体で数える'),
            dict(h='一棟の建物は壁の中心で測る',
                 ill='a building floor plan with a dashed line along the center of the outer walls, and an arrow pointing to the dashed line labeled 「壁の中心」.',
                 words=['壁の中心'], tag='専有部分は内側線'),
            dict(h='三方が壁の車庫は算入',
                 ill='a ground floor plan in which a garage space is enclosed by walls on three sides and is open at the front with no shutter. The garage space is shaded green as part of the floor area.',
                 words=[], tag='前面が開放でも'),
            dict(h='内部のダストシュートは算入',
                 ill='a floor plan with a chute inside a wall, partly sticking out through the outer wall. The whole chute, including the part sticking out, is shaded green.',
                 words=[], tag='外に及んでも全体'),
            dict(h='屋上の出入口専用の階段室は算入しない',
                 ill='a building roof with a small stair house box on the rooftop. The stair house is covered with a pale gray shading to show it is not counted.',
                 words=[], tag='塔屋は数えない'),
        ],
        kanji=kj('一室低算入棟壁中心線三方車庫内部外側屋上出入口階段', n=24)),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、床面積を測る線を対象ごとに表で示します。2枚目は、床面積に入る部分と入らない部分を左右で対比します。',
    notebooks=[
        dict(name='壁の中心線と内側線の使い分け', args=dict(
            title='床面積は、どの線で測る？', sub='不動産登記規則115条（毎日ドリル 第79日 イ）',
            req='a comparison table',
            layout="""--- TABLE ---
Render as a clean flat-design table with a header row and three body rows, in rounded panel style. Each body row carries a small floor-plan icon at the left edge showing where the measuring line runs.
Header row (blue accent), two column headers: 床面積を測る対象 | 測る線
Row 1: 区分建物でない建物 | 壁の中心線
Row 2: 区分建物の専有部分 | 壁の内側線
Row 3: 区分建物が属する一棟の建物 | 壁の中心線
Draw 壁の中心線 in blue and 壁の内側線 in orange so they can never be confused. Use exactly these strings, and no others. Do not use check marks or cross marks.""",
            callout='区分建物の専有部分だけが、壁の内側線で測ります。\n一棟の建物は、区分建物ではないので、壁の中心線で測ります。',
            footer='不動産登記規則115条',
            kanji=kj('床面積測対象区分建物専有部分壁中心内側線', n=16), what='table',
            check='confirm the table has exactly three body rows and that the two kinds of line text are drawn in different colors, ')),
        dict(name='床面積に入る部分、入らない部分', args=dict(
            title='床面積に入る？入らない？', sub='準則82条の整理（毎日ドリル 第79日 エ・オ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「入る」 on the left and 「入らない」 on the right. Draw them large and in different accent colors (green on the left, gray on the right) so they can never be confused or duplicated. Do not use check marks or cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (green accent):
Panel header: 入る
Scene: an isometric office building with a chute inside the wall that sticks out a little.
Rows of text:
内部にあるダストシュート
外側に少し及んでいても全体

RIGHT PANEL (gray accent):
Panel header: 入らない
Scene: an isometric office building with an outdoor staircase attached and a small stair house on the roof.
Rows of text:
外側にあるダストシュート
建物に附属する屋外の階段
屋上への出入口だけの階段室""",
            callout='建物の内部にあるダストシュートは、外側に及んでいても全体が入ります。\n屋外の階段や、屋上への出入口だけの階段室は、床面積に入りません。',
            footer='不動産登記事務取扱手続準則82条',
            kanji=kj('入内部外側階段室屋上出口建物附属', n=14), what='panels',
            check='confirm the two panel headers are different strings (入る on the left and 入らない on the right) drawn in different accent colors, ')),
    ],
)
