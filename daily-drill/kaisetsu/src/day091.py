def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '分筆すると、', '地番と権利はどうなる？', '不動産登記法　分筆の登記'
_cards = [
    dict(h='支号のある土地の分筆は最終の次',
         ill='an isometric row of land plots labeled 「五番一」, 「五番二」 and 「五番三」, and a newly separated plot at the far right labeled 「五番四」 highlighted with a green glow. A green check mark sits beside the new plot.',
         words=['五番一', '五番二', '五番三', '五番四'], tag='支号の支号は使わない'),
    dict(h='乙土地の権利の消滅は甲土地に付記',
         ill='two record sheets side by side. The left sheet labeled 「甲土地」 carries a small sticky note labeled 「付記」 attached to one line. The right sheet labeled 「乙土地」 is clean with no copied line. A green check mark sits beside the sticky note.',
         words=['甲土地', '乙土地', '付記'], tag='乙土地には転写しない'),
    dict(h='地上権は乙土地にも転写される',
         ill='two record sheets side by side labeled 「甲土地」 and 「乙土地」. A line labeled 「地上権」 appears on the left sheet and is copied by a thin arrow onto the right sheet. A green check mark sits beside the copied line.',
         words=['甲土地', '乙土地', '地上権'], tag='共に目的である旨を記録'),
    dict(h='誤差の限度内なら更正は不要',
         ill='an isometric land plot with a measuring tape, split into two parts by a line. A small balance scale beside it holds the total of the two parts on one side and the original size on the other side, almost level. A tag labeled 「誤差の限度」 sits on the scale. A green check mark sits beside the scale.',
         words=['誤差の限度'], tag='分筆前後の地積の差で判断'),
    dict(h='転抵当権者の承諾も必要',
         ill='an isometric scene of three stacked document sheets: a mortgage sheet, and a second sheet labeled 「転抵当」 attached on top of it. Two figures stand at the sides, each holding a signed consent form. A green check mark sits beside the two signed forms.',
         words=['転抵当'], tag='第三者の承諾もそろえる'),
]

D = dict(
    catch='分筆後の地番と権利の移し方',
    intro='土地を分筆するときの、分筆後の地番の付け方、権利に関する登記の写し方と消し方、地積の更正が要るかどうかを問う問題です（不動産登記法40条、不動産登記規則102条・104条、不動産登記事務取扱手続準則67条・72条）。この問題は、正しいものの組合せを選びます。\n\nこの記事では、「どの土地に、何を、どう記録するか」という点を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('支号のある土地を分筆するときは、最終の支号の次の番号を付ける',
               '本番に支号のある土地を分筆する場合は、1筆に従来の地番を残し、他の筆には、本番の最終の支号を追って、順次支号を付けて地番を定めます。支号の支号は用いません（不動産登記事務取扱手続準則67条1項4号・9号）。\n\n問題文は、他の1筆を「5番1の1」としているので、本肢は誤りです。\n\n**たとえば**、5番1、5番2、5番3の土地がある地番区域で、5番1を2筆に分筆するとします。1筆は5番1のまま残し、もう1筆は、最終の支号の次の「5番4」とします。'),
        'イ': ('消滅する権利は、乙土地に転写せず、甲土地の登記に付記して記録する',
               '甲土地から乙土地を分筆する場合に、乙土地について権利が消滅した旨の登記をするときは、分筆後の甲土地の登記記録の当該権利の登記に付記登記をして、乙土地についてその権利が消滅した旨を記録します。\n\nこのとき、消滅した権利の登記を乙土地の登記記録に転写する必要はありません（不動産登記規則104条2項）。\n\n問題文は、乙土地に転写した上で消滅を記録するとしているので、本肢は誤りです。\n\n**たとえば**、抵当権の登記がある甲土地から乙土地を分筆し、乙土地について抵当権を消す場合、乙土地の登記記録に抵当権は写されません。甲土地の抵当権の登記に付記して、乙土地について消えたことを記録します。'),
        'ウ': ('地上権の登記は、乙土地に転写し、甲土地が共に目的である旨を記録する',
               '登記官は、乙土地の登記記録の権利部の相当区に、甲土地の登記記録から権利に関する登記を転写します。所有権と担保権以外の権利（地役権を除く）については、分筆後の甲土地が共にその権利の目的である旨も記録します（不動産登記規則102条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地全体にCさんの地上権が設定されていて、甲土地から乙土地を分筆したとします。乙土地にも地上権の登記が写され、甲土地も同じ地上権の目的であることが記録されます。'),
        'エ': ('分筆前後の地積の差が誤差の限度内なら、地積の更正の登記は要らない',
               '分筆前の地積と分筆後の地積の差が、分筆前の地積を基準にして、地積測量図の誤差の限度内であるときは、地積に関する更正の登記の申請は要りません（不動産登記事務取扱手続準則72条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、登記記録上300.00平方メートルの土地を測って分筆したところ、分筆後の2筆の合計が300.20平方メートルでした。この差が誤差の限度内なら、地積の更正の登記を別に申請する必要はありません。'),
        'オ': ('転抵当権者がいるときは、その承諾を証する情報も提供する',
               '権利を消滅させる登記をするには、権利の登記名義人が消滅を承諾したことを証する情報を提供します。\n\nその権利を目的とする第三者の権利に関する登記があるときは、その第三者が承諾したことを証する情報も提供しなければなりません（不動産登記法40条のかっこ書、不動産登記規則104条1項2号）。\n\n問題文は、抵当権者の承諾だけで足りるとしているので、本肢は誤りです。\n\n**たとえば**、Aさんの抵当権を目的として、Bさんの転抵当の登記があるとします。乙土地について抵当権を消すには、Aさんの承諾に加えて、Bさんの承諾も必要です。'),
    },
    summary=[
        ('ア', '誤', '支号のある土地を分筆するときは、最終の支号の次の番号を付ける（支号の支号は使わない）'),
        ('イ', '誤', '消滅する権利は乙土地に転写せず、甲土地の登記に付記して記録する'),
        ('ウ', '正', '地上権の登記は乙土地に転写し、甲土地が共に目的である旨を記録する'),
        ('エ', '正', '分筆前後の地積の差が誤差の限度内なら、地積の更正の登記は要らない'),
        ('オ', '誤', '転抵当権者がいるときは、転抵当権者の承諾を証する情報も提供しなければならない'),
    ],
    summary_tail='アは「5番4」と「5番1の1」、イは「転写の有無」、オは「承諾が必要な人の範囲」を入れ替えた出題です。分筆では、地番・権利・地積のそれぞれに決まりがあります。',
    supplements=[
        '### 補足説明（ア）：分筆後の地番の付け方\n\n分筆後の地番は、元の土地に支号があるかどうかで決まり方が変わります（準則67条1項4号・9号）。\n\n| 元の土地 | 分筆後の地番の決め方 | 例 |\n|---|---|---|\n| 支号のない土地（本番） | 分筆前の地番に支号を付けて各筆の地番を定める | 5番を分筆して、5番1と5番2 |\n| 支号のある土地 | 1筆は従来の地番を残し、他の筆は本番の最終の支号の次から順に付ける | 5番1、5番2、5番3がある区域で5番1を分筆して、5番1と5番4 |\n| どちらの場合も | 支号の支号は用いない | 「5番1の1」は使わない |\n\n**たとえば**、5番1を分筆して新しい筆に「5番1の1」と付けたくなりますが、支号の支号は使えません。すでに5番3まであるので、次の「5番4」になります。',
        '### 補足説明（イ・オ）：乙土地の権利を消すときの手順\n\n分筆に伴って、乙土地についてだけ権利を消すときは、次の手順になります（法40条、規則104条）。\n\n- 分筆の登記の申請と一緒に、権利の登記名義人が消滅を承諾したことを証する情報を提供する。\n- その権利を目的とする第三者の権利（転抵当など）の登記があるときは、その第三者の承諾を証する情報も提供する。\n- 登記官は、甲土地の登記記録の権利の登記に付記登記をして、乙土地について消滅した旨を記録する。乙土地には、その権利の登記を転写しない。\n\n**たとえば**、抵当権の登記がある甲土地から乙土地を分筆するとき、抵当権者の承諾書を付ければ、乙土地は抵当権のない土地になります。転抵当があれば、転抵当権者の承諾書も必要です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第91日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法40条、不動産登記規則102条1項・104条1項2号・2項、不動産登記事務取扱手続準則67条1項4号・9号・72条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの具体例の数値（300.00平方メートル、300.20平方メートル）は説明用の仮の数字で、実際の誤差の限度（地積測量図の誤差の限度を定めた規則77条5項）の具体的な値は、この記事では扱っていません。',
        'エの具体例のあとで、誤差の限度を超えるときは地積の更正の登記を併せて申請する、という流れになることは、準則72条1項の反対解釈による一般的な整理です。',
    ],
    phrases=['支号の分筆は最終の支号の次です', '消える権利は甲土地に付記します', '地上権は乙土地にも写します', '誤差の限度内なら更正は不要です', '転抵当権者の承諾も必要です'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='分筆の登記を、「地番と権利の移し方」（グループA：ア・イ・ウ）と「更正の要否と承諾」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='分筆の登記を整理', sub='不動産登記法 第40条、規則 第102条・第104条、準則 第67条・第72条（毎日ドリル 第91日）',
        col_a='地番と権利の移し方', col_b='更正の要否と承諾', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '分筆の登記を整理地番と権利の移し方更正の要否と承諾', n=24)),
    nb_label='ア・イ・オ肢', nb_intro='ア・イ・オの補足説明に合わせた2枚です。1枚目は、分筆後の地番の付け方を左右の対比で示します。2枚目は、乙土地の権利を消すときの手順を流れで示します。',
    notebooks=[
        dict(name='分筆後の地番の付け方', args=dict(
            title='分筆後の地番の付け方', sub='支号のない土地と、支号のある土地（毎日ドリル 第91日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「支号のない土地を分筆」 on the left and 「支号のある土地を分筆」 on the right; draw them in different accent colors (blue and green) so they can never be confused or duplicated. Do not use check marks or crosses.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 支号のない土地を分筆
Scene: one land plot labeled 「五番」 on top, an arrow down to two plots below labeled 「五番一」 and 「五番二」.
Rule text: 分筆前の地番に支号を付ける

RIGHT PANEL (green accent):
Panel header: 支号のある土地を分筆
Scene: three existing plots labeled 「五番一」, 「五番二」 and 「五番三」 in a row. The plot 「五番一」 is split by an arrow into two plots labeled 「五番一」 and 「五番四」.
Rule text: 1筆は従来の地番を残し、他の筆は最終の支号の次の番号
Small note text: 支号の支号は使わない""",
            callout='支号のある土地を分筆するときは、1筆に従来の地番を残し、他の筆には、最終の支号の次の番号を付けます。\n「五番一の一」のような、支号の支号は使えません。',
            footer='不動産登記事務取扱手続準則67条1項4号、9号',
            kanji='・'.join(_k('支号土地分筆地番五番一二三四最終次従来残他不動産登記事務取扱手続準則')), what='panels',
            check='confirm the two panel headers are different strings (支号のない土地を分筆 on the left and 支号のある土地を分筆 on the right) and that the plot labels 五番, 五番一, 五番二, 五番三 and 五番四 are copied verbatim, ')),
        dict(name='乙土地の権利を消すときの手順', args=dict(
            title='乙土地の権利を消す手順', sub='分筆に伴う権利の消滅（毎日ドリル 第91日 イ・オ）',
            req='a three-step flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow with three boxes connected by downward arrows. The three boxes are drawn in three different accent colors (blue, green, orange).
Box 1 (blue), label: 申請と同時に. Text: 権利の登記名義人が消滅を承諾したことを証する情報を提供する。
Box 2 (green), label: 第三者がいるとき. Text: 抵当権を目的とする転抵当などの登記があるときは、その第三者の承諾を証する情報も提供する。
Box 3 (orange), label: 登記の記録. Text: 甲土地の登記記録の権利の登記に付記して、乙土地について消滅した旨を記録する。乙土地には転写しない。
Beside box 3, two small record sheets labeled 「甲土地」 and 「乙土地」; the 「甲土地」 sheet carries a sticky note, the 「乙土地」 sheet is clean.
Do not use check marks or crosses.""",
            callout='乙土地の権利を消すには、権利の登記名義人の承諾が必要です。その権利を目的とする転抵当などの第三者の権利があるときは、その第三者の承諾も必要です。\n登記は、甲土地の登記記録の付記登記で行い、乙土地には転写しません。',
            footer='不動産登記法40条、不動産登記規則104条',
            kanji='・'.join(_k('乙土地権利消手順申請同時登記名義人承諾証情報提供第三者転抵当記録付記転写甲不動産登記法規則')), what='flow',
            check='confirm the three boxes are drawn in three different accent colors and that the labels (申請と同時に, 第三者がいるとき, 登記の記録) are copied verbatim, ')),
    ],
)
