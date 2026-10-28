def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '点線か、朱書か、', '隣の地番は要る？', '不動産登記規則　図面の記録事項'
_cards = [
    dict(h='分筆後の土地に符号を付ける',
         ill='an isometric land plot divided into two parts by a clear dividing line. The left part carries a small tag labeled 「イ」 and the right part carries a small tag labeled 「ロ」. A green check mark sits beside the dividing line.',
         words=['イ', 'ロ'], tag='符号は適宜でよい'),
    dict(h='区分建物は一棟の一階を点線で',
         ill='an isometric apartment building with several floors. The floor plan of its ground floor is drawn below it with a dotted outline. A small flag labeled 「建物の存する部分」 marks the upper floors of the building. A green check mark sits beside the dotted outline.',
         words=['建物の存する部分'], tag='存する階層も記録'),
    dict(h='地下のみの建物は地下の形を朱書',
         ill='an isometric underground room drawn as a floor plan, with its outline traced in red ink. A small red pen lies beside the plan, and a label 「地下」 sits on the room. A green check mark sits beside the plan.',
         words=['地下'], tag='地下の形状は朱書'),
    dict(h='各階平面図は一階の位置を点線で',
         ill='an isometric stack of two floor plans. The upper plan shows a dotted outline marking the position of the lower floor below it. A label 「一階」 sits at the dotted outline. A green check mark sits beside the dotted outline.',
         words=['一階'], tag='一階以外を表示するとき'),
    dict(h='建物図面に隣接地の地番を記録',
         ill='an isometric site plan with a small building on the middle plot labeled 「六番」. The plot on the left is labeled 「五番」 and the plot on the right is labeled 「七番」. A compass mark sits in a corner. A green check mark sits beside the neighboring plots.',
         words=['五番', '六番', '七番'], tag='隣接地の地番も必要'),
]

D = dict(
    catch='地下のみは朱書、隣接地の地番も記録',
    intro='地積測量図、建物図面、各階平面図に、何をどのように書くのかを問う問題です（不動産登記規則78条・82条・83条、不動産登記事務取扱手続準則51条から53条）。この問題は、誤っているものの組合せを選びます。\n\nこの記事では、線の種類（点線・朱書・一点鎖線）の使い分けと、建物図面に書く事項を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('分筆後の各土地に付ける符号は、（イ）（ロ）でもよい',
               '分筆の登記を申請するときの地積測量図には、分筆前の土地を図示し、分筆線を明らかにして分筆後の各土地を表示し、符号を付けなければなりません（不動産登記規則78条）。\n\nこの符号は、①②③、（イ）（ロ）（ハ）、ＡＢＣなど、適宜の符号を用いて差し支えありません（不動産登記事務取扱手続準則51条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Aさんの1番の土地を2筆に分けるとき、図面の中で分けた片方を「（イ）」、もう片方を「（ロ）」と書いて区別して構いません。'),
        'イ': ('区分建物の建物図面には、一棟の建物の一階を点線で示し、存する階層を記録する',
               '区分建物の建物図面は、点線をもって、その建物が属する一棟の建物の一階の形状も明確にします。その建物が一階以外の部分に存するときは、その存する階層を「建物の存する部分　三階」のように記録します（不動産登記事務取扱手続準則52条2項）。\n\nなお、区分建物の建物図面では、地上の最低階の位置と形状を明確にします（不動産登記規則82条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、10階建てのマンションの3階と4階にまたがる部屋の建物図面には、マンション全体の一階の形を点線で描き、「建物の存する部分　三階、四階」と記録します。'),
        'ウ': ('地下のみの建物の建物図面は、地下の形を朱書する',
               '建物が地下のみの建物である場合の建物図面には、地下一階の形状を朱書します（不動産登記事務取扱手続準則52条1項）。\n\n問題文は「点線で表示する」としていますが、点線は、区分建物の一棟の建物の一階の形状などを示す方法です。本肢は誤りです。\n\n**たとえば**、地下一階だけの地下の店舗がある場合、その建物図面には、地下一階の形を赤い線で書きます。点線で書くのではありません。'),
        'エ': ('各階平面図で二階以上を表示するときは、一階の位置を点線で示す',
               '各階平面図に、一階以外の階層を表示するときは、一階の位置を点線をもって表示します（不動産登記規則83条1項、不動産登記事務取扱手続準則53条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、2階建ての建物の各階平面図で二階の形を示すときは、二階の形の下に、一階がどこにあるのかを点線で書き入れます。一階と二階の位置関係が一目でわかるようにするためです。'),
        'オ': ('建物図面には、隣接地の地番も記録する',
               '建物図面には、方位、縮尺、敷地の地番とその形状、隣接地の地番を記録します。附属建物があるときは、さらに主である建物又は附属建物の別と、附属建物の符号も記録します（不動産登記規則82条2項）。\n\n問題文は「隣接地の地番を記録することを要しない」としているので、本肢は誤りです。\n\n**たとえば**、Bさんの建物が6番の土地に建っていて、隣が5番と7番の土地なら、建物図面には、敷地の6番だけでなく、隣の5番と7番の地番も書きます。'),
    },
    summary=[
        ('ア', '正', '分筆後の各土地の符号は、①②③や（イ）（ロ）など、適宜の符号でよい'),
        ('イ', '正', '区分建物の建物図面には、一棟の建物の一階を点線で示し、存する階層を記録する'),
        ('ウ', '誤', '地下のみの建物の建物図面は、地下一階の形状を朱書する（点線ではない）'),
        ('エ', '正', '各階平面図で一階以外を表示するときは、一階の位置を点線で示す'),
        ('オ', '誤', '建物図面には、隣接地の地番も記録しなければならない'),
    ],
    summary_tail='ウは「朱書」と「点線」、オは「隣接地の地番」の有無を入れ替えた出題です。線の種類は場面ごとに決まっているので、表で整理して覚えましょう。',
    supplements=[
        '### 補足説明（ウ）：朱書・点線・一点鎖線の使い分け\n\n図面で使う線は、場面ごとに決まっています。\n\n| 場面 | 線の種類 | 根拠 |\n|---|---|---|\n| 地下のみの建物の建物図面 | 地下一階の形状を朱書 | 準則52条1項 |\n| 区分建物の建物図面（一棟の建物の一階） | 点線 | 準則52条2項 |\n| 区分建物の建物図面で、その建物の存する階層の形状が一棟の一階と異なるとき | 一点鎖線 | 準則52条3項 |\n| 各階平面図で一階以外を表示するとき（一階の位置） | 点線 | 準則53条1項 |\n\n**たとえば**、地下だけの建物の図面で「点線」と書いてしまうのは、区分建物の図面の約束を持ち込んだ間違いです。地下のみの建物は、地下一階の形を朱書します。',
        '### 補足説明（オ）：建物図面と各階平面図では、書く内容が違う\n\n建物図面は、建物が敷地のどこにあるかを示す図面です。各階平面図は、各階の形と広さを示す図面です。そのため、記録する事項が異なります。\n\n- 建物図面（規則82条2項）：方位、縮尺、敷地の地番とその形状、隣接地の地番、附属建物があるときは主である建物又は附属建物の別と附属建物の符号。\n- 各階平面図（規則83条1項）：縮尺、各階の別、各階の平面の形状、一階の位置、各階ごとの建物の周囲の長さ、床面積とその求積方法、附属建物があるときは主である建物又は附属建物の別と附属建物の符号。\n\n**たとえば**、隣の土地の地番は、建物が敷地のどこにあるかを示す建物図面に書きます。各階平面図には、隣接地の地番ではなく、各階の床面積とその求め方を書きます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第86日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記規則78条・82条・83条は `note-articles/laws/` 配下の規則の原文で、不動産登記事務取扱手続準則51条から53条は準則の原文で確認しました。',
        '準則52条の例示の図（実線・破線・一点鎖線の凡例と例の図）は、手元の原文では図の部分を文字として確認できていません。補足説明の線の種類は、準則52条・53条の本文で確認できる範囲で書いています。',
        'イの具体例（10階建ての3階と4階にまたがる部屋）は、準則52条2項の条文の言葉に沿って作った例です。',
    ],
    phrases=['分筆後の符号は適宜でよいです', '区分建物は一階を点線で示します', '地下のみの建物は朱書です', '各階平面図は一階を点線で示します', '建物図面に隣接地の地番を書きます'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='地積測量図・建物図面・各階平面図の書き方を、「符号と表示の方法」（グループA：ア・イ・ウ）と「各階平面図と建物図面」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='図面の書き方を整理', sub='不動産登記規則 第78条・第82条・第83条、準則 第51条から第53条（毎日ドリル 第86日）',
        col_a='符号と表示の方法', col_b='各階平面図と建物図面', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '図面の書き方を整理符号と表示の方法各階平面図と建物図面', n=24)),
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、朱書・点線・一点鎖線の使い分けを表で整理します。2枚目は、建物図面と各階平面図に記録する事項を左右の表で比べます。',
    notebooks=[
        dict(name='朱書・点線・一点鎖線の使い分け', args=dict(
            title='朱書・点線・一点鎖線の使い分け', sub='図面に使う線の種類（毎日ドリル 第86日 ウ）',
            req='a four-row table',
            layout="""IMPORTANT: the three line-type names are different strings: 「朱書」, 「点線」 and 「一点鎖線」. Draw each name in its own accent color (red for 朱書, blue for 点線, green for 一点鎖線) and draw a small sample line next to each name: a solid red line, a dotted blue line, and a dash-dot green line. The name 「点線」 must never be confused with 「一点鎖線」.

--- TABLE ---
A table with four rows. Each row has a scene on the left and the line type on the right, connected by a thin arrow.
Row 1: scene 「地下のみの建物の建物図面」 (a small underground floor plan icon) → 朱書
Row 2: scene 「区分建物の建物図面の一棟の一階」 (an apartment building icon with its ground floor outlined) → 点線
Row 3: scene 「区分建物で形が一棟の一階と異なる階」 (an apartment building icon with an odd-shaped upper floor) → 一点鎖線
Row 4: scene 「各階平面図の一階の位置」 (two stacked floor plans) → 点線""",
            callout='線の種類は、場面ごとに決まっています。地下のみの建物の建物図面は朱書、区分建物の一棟の一階や各階平面図の一階の位置は点線です。\n区分建物で形が一棟の一階と異なる階は、一点鎖線で示します。',
            footer='不動産登記事務取扱手続準則52条、53条',
            kanji='・'.join(_k('朱書点線一点鎖線地下建物図面区分建物一棟一階各階平面図位置形状異不動産登記事務取扱手続準則')), what='table',
            check='confirm the three line-type names (朱書, 点線, 一点鎖線) are different strings drawn in different accent colors and that 点線 and 一点鎖線 are never confused, ')),
        dict(name='建物図面と各階平面図の記録事項', args=dict(
            title='建物図面と各階平面図の違い', sub='図面に記録する事項（毎日ドリル 第86日 オ）',
            req='a two-column table',
            layout="""--- TWO-COLUMN TABLE ---
Two panels side by side (left and right), same height. The two panel headers are different strings; draw them in different accent colors (blue on the left, green on the right). Keep every item exactly as written. A few items appear in both panels on purpose.

LEFT PANEL (blue accent):
Panel header: 建物図面
Items (a plain list, one per row):
方位
縮尺
敷地の地番とその形状
隣接地の地番
主である建物又は附属建物の別と附属建物の符号
A highlighted row marker beside 「隣接地の地番」.

RIGHT PANEL (green accent):
Panel header: 各階平面図
Items (a plain list, one per row):
縮尺
各階の別
各階の平面の形状
一階の位置
各階ごとの建物の周囲の長さ
床面積とその求積方法
主である建物又は附属建物の別と附属建物の符号""",
            callout='建物図面は、建物が敷地のどこにあるかを示す図面なので、隣接地の地番も記録します。\n各階平面図は、各階の形と広さを示す図面なので、床面積とその求め方を記録します。',
            footer='不動産登記規則82条2項、83条1項',
            kanji='・'.join(_k('建物図面各階平面図方位縮尺敷地地番形状隣接地附属符号位置周囲長床面積求積方法不動産登記規則')), what='panels',
            check='confirm the two panel headers are different strings (建物図面 on the left and 各階平面図 on the right) and that both lists are copied verbatim, ')),
    ],
)
