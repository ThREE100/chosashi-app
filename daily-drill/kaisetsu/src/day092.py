def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '地図の縮尺は、', '地域ごとに違う？', '不動産登記規則　地図と訂正の申出'
_cards = [
    dict(h='山林や原野は千分の一か二千五百分の一',
         ill='an isometric map sheet of a mountain and meadow area with a few trees. Two small scale-bar tags sit at the corner of the map, one labeled 「千分の一」 and the other labeled 「二千五百分の一」. A green check mark sits beside the tags.',
         words=['千分の一', '二千五百分の一'], tag='地域ごとに縮尺が違う'),
    dict(h='農地の地図は精度区分乙一まで',
         ill='an isometric map sheet of a farming village with rice paddies and fields. A measuring tape lies along one field, and a small ruler tag labeled 「乙一」 sits beside it. A green check mark sits beside the ruler tag.',
         words=['乙一'], tag='村落や農耕地の誤差の限度'),
    dict(h='相続人も地図の訂正を申し出られる',
         ill='an isometric scene: a map sheet with one plot circled in red pencil, and a figure standing in front of it who carries a name tag labeled 「相続人」 and holds a form. A green check mark sits beside the figure.',
         words=['相続人'], tag='相続を証する情報を添える'),
    dict(h='地積に錯誤があれば更正と同時に',
         ill='an isometric land plot with a measuring tape, and two forms laid side by side: one form labeled 「地積更正」 and another form for the map correction. A paper clip joins the two forms together. A green check mark sits beside the paper clip.',
         words=['地積更正'], tag='申出と更正をセットで'),
    dict(h='他の土地の区画まで動くなら却下',
         ill='an isometric map sheet with a target plot in the middle. A neighboring plot beside it would also have to move, drawn with dotted arrows. A round stamp labeled 「却下」 sits on the correction form. A green check mark sits beside the stamp.',
         words=['却下'], tag='申出に係る土地以外'),
]

D = dict(
    catch='地図の縮尺と、訂正の申出の決まり',
    intro='地図の縮尺や誤差の限度、地図に準ずる図面、そして地図の訂正の申出について問う問題です（不動産登記規則10条・16条）。この問題は、誤っているものの組合せを選びます。\n\nこの記事では、地域ごとに決まっている縮尺と誤差の限度、そして「だれが」「どんなときに」地図の訂正を申し出られるのかを、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('山林・原野地域の地図の縮尺は、千分の一又は二千五百分の一',
               '山林・原野地域の地図の縮尺は、千分の一又は二千五百分の一です（不動産登記規則10条2項3号）。五百分の一又は千分の一は、村落・農耕地域の縮尺です（同項2号）。\n\n問題文は、山林・原野地域を「五百分の一又は千分の一」としているので、本肢は誤りです。\n\n**たとえば**、山林や原野が広がる地域の地図は、千分の一か二千五百分の一です。田や畑の多い村落・農耕地域の地図は、五百分の一か千分の一です。数字を取り違えないようにしましょう。'),
        'イ': ('村落・農耕地域の誤差の限度は、精度区分乙一まで',
               '地図を作るための一筆地測量と地積測定における誤差の限度は、地域ごとに決まっています。村落・農耕地域は、精度区分乙一までです（不動産登記規則10条4項2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、田や畑が多い地域で地図を作るための測量をするときは、精度区分乙一までの誤差が認められます。市街地地域は甲二まで、山林・原野地域は乙三までです。'),
        'ウ': ('地図の区画に誤りがあるときは、所有権の登記名義人の相続人も訂正を申し出られる',
               '地図に表示された土地の区画又は地番に誤りがあるときは、表題部所有者や所有権の登記名義人のほか、これらの相続人その他の一般承継人も、訂正の申出をすることができます（不動産登記規則16条1項）。相続人が申し出るときは、相続があったことを証する情報も提供します（同条5項3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の所有権の登記名義人Aさんが亡くなった場合でも、相続人のBさんは、甲土地の区画の誤りについて、地図の訂正を申し出ることができます。'),
        'エ': ('地積に錯誤があるときは、地図に準ずる図面の訂正の申出は、地積の更正の登記と併せてする',
               '地図や地図に準ずる図面の訂正の申出をする場合に、その土地の登記記録の地積にも錯誤があるときは、申出は、地積に関する更正の登記の申請と併せてしなければなりません（不動産登記規則16条1項後段・2項）。\n\n問題文は、地積の更正の登記を申請せずに、訂正の申出のみをすることができるとしているので、本肢は誤りです。\n\n**たとえば**、乙土地の実際の形が図面と違い、しかも登記記録の面積も実際と違っていた場合は、面積の更正の登記を申請するのと同時に、図面の訂正を申し出ます。'),
        'オ': ('ほかの土地の区画まで訂正することになるときは、申出を却下する',
               '登記官は、地図又は地図に準ずる図面を訂正することによって、申出に係る土地以外の土地の区画又は位置若しくは形状を訂正すべきこととなるときは、理由を付した決定で、申出を却下しなければなりません（不動産登記規則16条13項6号）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の区画を訂正すると、隣の丙土地の区画も動かさなければならなくなる場合、甲土地の所有者の申出は、却下されます。'),
    },
    summary=[
        ('ア', '誤', '山林・原野地域の地図の縮尺は、千分の一又は二千五百分の一（五百分の一又は千分の一は村落・農耕地域）'),
        ('イ', '正', '村落・農耕地域の誤差の限度は、精度区分乙一まで'),
        ('ウ', '正', '地図の区画に誤りがあるときは、所有権の登記名義人の相続人も訂正を申し出られる'),
        ('エ', '誤', '地積に錯誤があるときは、訂正の申出は、地積の更正の登記の申請と併せてしなければならない'),
        ('オ', '正', '申出に係る土地以外の土地の区画も訂正することになるときは、申出は却下される'),
    ],
    summary_tail='アは地域ごとの縮尺の数字、エは「地積の更正の登記と併せてする」という手続の組合せを入れ替えた出題です。縮尺と誤差の限度は、地域ごとの表で覚えましょう。',
    supplements=[
        '### 補足説明（ア）：地図の縮尺と誤差の限度は、地域ごとに決まっている\n\n地図の縮尺（規則10条2項）と、測量・地積測定の誤差の限度（規則10条4項）は、地域の種類ごとに決まっています。\n\n| 地域 | 縮尺 | 誤差の限度 |\n|---|---|---|\n| 市街地地域 | 二百五十分の一又は五百分の一 | 精度区分甲二まで |\n| 村落・農耕地域 | 五百分の一又は千分の一 | 精度区分乙一まで |\n| 山林・原野地域 | 千分の一又は二千五百分の一 | 精度区分乙三まで |\n\n**たとえば**、五百分の一は、市街地地域と村落・農耕地域に出てきます。山林・原野地域にはありません。「五百分の一又は千分の一」と書かれていたら、村落・農耕地域の縮尺です。',
        '### 補足説明（エ）：地図の訂正の申出は、場面ごとに結論が決まっている\n\n地図等の訂正の申出（規則16条）は、場面ごとの結論を整理すると覚えやすくなります。\n\n| 場面 | 結論 |\n|---|---|\n| 区画に誤りがあるが、地積は合っている | 訂正の申出のみでよい |\n| 区画（位置・形状）に誤りがあり、地積にも錯誤がある | 地積の更正の登記の申請と併せて申し出る（2項） |\n| 申出人が所有権の登記名義人の相続人 | 相続があったことを証する情報も提供する（5項3号） |\n| 訂正すると、申出に係る土地以外の区画も訂正することになる | 却下（13項6号） |\n\n**たとえば**、地積は合っていて、図面に写った形だけが実際と違うなら、訂正の申出だけで足ります。面積も違っていたら、面積の更正の登記と一緒に申請します。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第92日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則10条2項・4項、16条1項・2項・5項・13項は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの縮尺は、規則10条2項各号の数字を地域ごとに並べたもので、縮尺が定められた理由は条文には書かれていないため、記事では説明していません。',
        'エの補足説明の表の「区画に誤りがあるが、地積は合っている場合は訂正の申出のみでよい」は、規則16条2項（地積に錯誤があるときに併せてする）の裏返しとしての一般的な整理です。',
    ],
    phrases=['山林や原野は千分の一か二千五百分の一', '農地の地図は精度区分乙一までです', '相続人も訂正を申し出られます', '地積に錯誤なら更正と併せて申請です', 'ほかの土地の区画を動かすなら却下です'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='地図と地図の訂正の申出を、「縮尺と誤差の限度」（グループA：ア・イ）と「訂正の申出」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地図と訂正の申出を整理', sub='不動産登記規則 第10条・第16条（毎日ドリル 第92日）',
        col_a='縮尺と誤差の限度', col_b='訂正の申出', n_a=2,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '地図と訂正の申出を整理縮尺と誤差の限度訂正の申出', n=24)),
    nb_label='ア・エ肢', nb_intro='ア・エの補足説明に合わせた2枚です。1枚目は、地域ごとの縮尺と誤差の限度を表で示します。2枚目は、地図の訂正の申出の場面ごとの結論を表で整理します。',
    notebooks=[
        dict(name='地域ごとの縮尺と誤差の限度', args=dict(
            title='地域ごとの縮尺と誤差の限度', sub='不動産登記規則10条（毎日ドリル 第92日 ア）',
            req='a three-row table',
            layout="""IMPORTANT: the three area names are different strings: 「市街地地域」, 「村落・農耕地域」 and 「山林・原野地域」. Draw each area name in its own accent color (blue, green, orange) so the rows can never be confused. Several scale words look alike (for example 「五百分の一」 appears in two rows, and 「千分の一」 appears in two rows) so copy each row exactly as written.

--- TABLE ---
A table with three rows and three columns (area, scale, limit of error). A small icon of a city, a farm village, and a mountain sits beside each area name.
Row 1: 市街地地域 | 二百五十分の一又は五百分の一 | 精度区分甲二まで
Row 2: 村落・農耕地域 | 五百分の一又は千分の一 | 精度区分乙一まで
Row 3: 山林・原野地域 | 千分の一又は二千五百分の一 | 精度区分乙三まで""",
            callout='五百分の一は、市街地地域と村落・農耕地域に出てきますが、山林・原野地域にはありません。\n「五百分の一又は千分の一」は、村落・農耕地域の縮尺です。',
            footer='不動産登記規則10条2項、4項',
            kanji='・'.join(_k('市街地地域村落農耕山林原野縮尺二百五十分五千二精度区分甲乙誤差限度不動産登記規則')), what='table',
            check='confirm the three area names are different strings drawn in three different accent colors and that the scale and limit text of each row is copied verbatim, ')),
        dict(name='地図の訂正の申出の結論', args=dict(
            title='訂正の申出の場面ごとの結論', sub='不動産登記規則16条（毎日ドリル 第92日 エ）',
            req='a four-row table',
            layout="""--- TABLE ---
A table with four rows. Each row has a scene on the left and the conclusion on the right, connected by a thin arrow. The four conclusion boxes are drawn in four different accent colors (blue, green, orange, purple).
Row 1: scene 「区画に誤りがあるが、地積は合っている」 (a map sheet with one plot circled) → 訂正の申出のみでよい
Row 2: scene 「区画に誤りがあり、地積にも錯誤がある」 (a map sheet and a measuring tape) → 地積の更正の登記の申請と併せて申し出る
Row 3: scene 「申出人が、所有権の登記名義人の相続人」 (a figure with a name tag 「相続人」) → 相続があったことを証する情報も提供する
Row 4: scene 「訂正すると、ほかの土地の区画も訂正することになる」 (two neighboring plots moving) → 却下
Do not use check marks or crosses.""",
            callout='地積にも錯誤があるときは、訂正の申出だけでは足りず、地積の更正の登記の申請と併せてしなければなりません。\nほかの土地の区画まで訂正することになるときは、申出は却下されます。',
            footer='不動産登記規則16条1項、2項、5項、13項',
            kanji='・'.join(_k('訂正申出区画誤地積合錯誤更正登記申請併相続名義人証情報提供却下他土地不動産登記規則')), what='table',
            check='confirm the four conclusion boxes are drawn in four different accent colors and that each row is copied verbatim, ')),
    ],
)
