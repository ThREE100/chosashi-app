def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='土地を分筆したら、', t2='権利はどこへ？', topic='不動産登記法　分筆の登記')
_PT = '分筆の登記を整理'
_PS = '分筆に伴う権利と地番と申請人（毎日ドリル 第74日）'

_cards = [
    dict(h='乙土地の抵当権の消滅は甲土地に付記する',
         ill='two record sheets, the left labeled 「甲土地」 with a mortgage line and a small side-note line attached below it, and the right labeled 「乙土地」 with no mortgage line. A green check mark sits beside the side-note line.',
         words=['甲土地', '乙土地'], tag='乙土地には転写しない'),
    dict(h='抵当権者の承諾も併せて提供する',
         ill='a chain of three figures: a land owner, a ground-rights holder labeled 「地上権者」, and a bank figure labeled 「抵当権者」. Two signed consent papers pass from the holder and the bank to a registrar figure. A green check mark sits beside the papers.',
         words=['地上権者', '抵当権者'], tag='第三者の承諾も必要'),
    dict(h='支号のある土地の分筆は最終の支号の次',
         ill='a row of four land plots in a line and a fifth plot being split off at the end. The fifth plot has an empty address board. A land plot at the start of the row has a board labeled 「5番1」 and the new plot has a board labeled 「5番5」. A green check mark sits beside the new plot.',
         words=['5番1', '5番5'], tag='支号の支号は使わない'),
    dict(h='共有地の分筆は持分の過半数で申請できる',
         ill='three owner figures sharing one land plot, each holding a one-third piece of a round pie chart. Two of the owners hold forms while the third owner stands aside. A green check mark sits beside the two owners.',
         words=['過半数'], tag='三分の二で足りる'),
    dict(h='地役権は乙土地に及ぶときだけ転写する',
         ill='two land plots split from one, the left plot labeled 「甲土地」 and the right plot labeled 「乙土地」. A shaded strip crosses only the left plot and the boundary. A record sheet beside the right plot has an empty line. A green check mark sits beside the empty line.',
         words=['甲土地', '乙土地'], tag='存続しなければ転写しない'),
]

_nb1_layout = """--- FLOW ---
Render as a clean flat-design vertical flow in three steps connected by small downward arrows with no text.
Step 1 (blue accent), step header: 分筆前. Scene: a record sheet labeled 甲土地 with a mortgage line.
Step 2 (green accent), step header: 乙土地について消滅を承諾. Scene: a bank figure handing a consent paper to a registrar figure. Beside the scene, a small tag: 抵当権者の承諾を証する情報
Step 3 (orange accent), step header: 分筆後. Scene: two record sheets side by side: the left labeled 甲土地 shows the mortgage line with a small side-note line labeled 乙土地について消滅, and the right labeled 乙土地 has no mortgage line.
Use exactly these strings, and no others."""

_nb2_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and two data rows, with a small land-plot icon at the start of each row.

Header row: 分筆する土地 | 分筆した土地の地番

Row 1 (blue accent): 本番の5番（支号なし） | 5番1、5番2のように支号を付ける
Row 2 (green accent): 本番に支号のある5番1（最終の支号は5番4） | 一筆は5番1のまま、他は5番5

Below the table, a gray note with the label: 支号の支号は使わない
Use exactly these strings, and no others."""

D = dict(
    catch='分筆で消す権利は、甲土地に付記する',
    intro='土地の分筆の登記について、権利に関する登記の扱い、分筆後の地番、共有地の分筆の申請人を問う問題です（不動産登記法40条、不動産登記規則102条・104条、不動産登記事務取扱手続準則67条）。\n\nこの記事では、分筆に伴って権利が消滅するときの記録の仕方、新しい地番の付け方、共有者の一部でも申請できるかを、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('乙土地の抵当権の消滅は、甲土地の登記に付記する',
               '所有権の登記以外の権利に関する登記がある土地を分筆するときに、権利者が、その権利を分筆後のいずれかの土地について消滅させることを承諾したことを証する情報を提供すると、その土地について権利が消滅した旨が登記されます（不動産登記法40条）。\n\n甲土地から乙土地を分筆し、乙土地について消滅させる場合は、分筆後の甲土地の登記記録の抵当権の登記に、付記登記で消滅した旨を記録します。乙土地の登記記録には、転写しません（不動産登記規則104条2項）。本肢は正しいといえます。\n\n**たとえば**、甲土地に銀行の抵当権があり、そこから乙土地を分筆して、乙土地だけ抵当権を外すことを銀行が承諾したとします。乙土地の登記記録には抵当権が載らず、甲土地の抵当権の登記に、乙土地について消滅した旨が付記されます。'),
        'イ': ('地上権の消滅には、その地上権の抵当権者の承諾も必要',
               '消滅させる権利を目的とする第三者の権利に関する登記があるときは、その第三者が承諾したことを証する情報も、併せて提供しなければ、消滅の登記はされません（不動産登記法40条かっこ書）。\n\n問題文は、抵当権者の承諾を証する情報を提供しなくてもよいとしているので、本肢は誤りです。\n\n**たとえば**、甲土地の地上権に抵当権が設定されているとします。乙土地について地上権を消すには、地上権者の承諾だけでなく、その地上権を目的とする抵当権者の承諾も必要です。'),
        'ウ': ('支号のある土地の分筆では、支号の支号は使わない',
               '本番に支号のある土地を分筆するときは、一筆に従来の地番を残し、他の筆には、本番の最終の支号を追って順次支号を付けます（準則67条1項4号ただし書）。地番の支号には数字を用い、支号の支号は用いません（同項9号）。\n\n5番1を分筆する場合、本番5番の最終の支号は5番4なので、分筆した土地は5番5となります。問題文は「5番1の1」としているので、本肢は誤りです。\n\n**たとえば**、5番1の土地から1筆を分けたとき、元の土地は5番1のまま、新しい土地は5番4の次の5番5です。'),
        'エ': ('共有地の分筆は、持分の過半数を持つ共有者が申請できる',
               '共有物の管理に関する事項は、各共有者の持分の価格に従い、その過半数で決することができます（民法252条1項）。共有地の分筆は、共有物の形状や効用の著しい変更を伴わない軽微な変更として扱われ、持分の価格の過半数を持つ共有者だけで申請できるとされています。\n\n本肢は正しいといえます。\n\n**たとえば**、A・B・Cが各3分の1の持分で共有する甲土地で、AとBの持分の合計は3分の2です。AとBは、Cが申請人にならなくても、分筆の登記を申請することができます。'),
        'オ': ('地役権の登記は、乙土地に存続するときだけ転写する',
               '承役地についてする地役権の登記がある土地を分筆するときは、乙土地に地役権が存続することとなる場合に限り、地役権の登記を乙土地の登記記録に転写します（不動産登記規則102条1項かっこ書）。\n\n乙土地に地役権が存続しない場合は、乙土地に転写しません（同規則104条4項）。問題文は、存続しなくても転写されるとしているので、本肢は誤りです。\n\n**たとえば**、通行を認める地役権が、甲土地の分筆後の部分だけに及ぶとします。この場合、乙土地には地役権が存続しないので、その登記は乙土地の登記記録に転写されません。'),
    },
    summary=[
        ('ア', '正', '乙土地について消滅させる場合、甲土地の抵当権の登記に付記し、乙土地には転写しない'),
        ('イ', '誤', '地上権の消滅の登記には、その地上権を目的とする抵当権者の承諾を証する情報も必要'),
        ('ウ', '誤', '本番に支号のある5番1を分筆するときは、5番1と5番5になる。支号の支号は使わない'),
        ('エ', '正', '共有地の分筆は、持分の価格の過半数を持つ共有者が申請できる'),
        ('オ', '誤', '地役権の登記は、乙土地に地役権が存続する場合に限り、乙土地に転写する'),
    ],
    summary_tail='イは第三者の承諾の見落とし、ウは支号の付け方、オは転写の条件を入れ替えた出題です。分筆では、権利の行き先と地番の付け方を、条文の文言に沿って確かめましょう。',
    supplements=[
        '### 補足説明（ア・イ）：分筆に伴って権利を消滅させるとき\n\n分筆の際、分筆後のいずれかの土地について権利を消滅させるときの流れを整理します（不動産登記法40条、不動産登記規則104条）。\n\n1. 権利の登記名義人が、その権利を消滅させることを承諾する。\n2. その権利を目的とする第三者の権利の登記があるときは、その第三者の承諾も得る。\n3. 承諾を証する情報を、分筆の登記の申請情報と併せて提供する。\n4. 乙土地について消滅させる場合、甲土地の登記に付記して記録する。乙土地には転写しない。\n\n**たとえば**、地上権に抵当権がついているなら、地上権者と抵当権者の両方の承諾が要ります。片方だけでは、消滅の登記はされません。',
        '### 補足説明（ウ）：分筆した土地の地番の付け方\n\n分筆した土地の地番は、分筆前の地番に支号を付けて定めます（準則67条1項4号）。\n\n| 分筆する土地 | 分筆後の地番 |\n|---|---|\n| 本番に支号がない5番 | 5番1、5番2のように支号を付ける |\n| 本番に支号がある5番1（最終の支号は5番4） | 一筆は5番1のまま、他の筆は5番5 |\n\n支号の支号（5番1の1のような地番）は使いません（同項9号）。\n\n**たとえば**、5番1から分筆する土地に5番1の1と付けたくなりますが、正しくは本番の最終の支号の次の5番5です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第74日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法40条、不動産登記規則102条1項・104条1項から5項まで、不動産登記事務取扱手続準則67条1項4号・9号、民法252条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの「共有地の分筆は持分の価格の過半数を持つ共有者が申請できる」という取扱いは、民法の改正を受けた通達によるもので、手元の法令の原文では確認できていません（原文は未確認）。本文では、民法252条1項と、軽微な変更として扱われるという一般的な整理を書いています。',
        'ウの具体例（5番1から分筆した土地が5番5になる）は、準則67条1項4号ただし書と問題文の前提（本番5番の最終の支号は5番4）から導いたものです。',
    ],
    phrases=['乙土地の消滅は甲土地に付記します', '第三者の承諾も併せて提供します', '支号の支号は使いません', '共有地の分筆は持分の過半数で申請できます', '地役権は存続するときだけ転写します'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='分筆の登記を、「権利に関する登記の扱い」（グループA：ア・イ）と「地番と申請人と地役権」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='権利に関する登記の扱い', col_b='地番と申請人と地役権', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '権利に関する登記の扱い地番と申請人と地役権', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ア・イ・ウ肢', nb_intro='ア・イとウの補足説明に合わせた2枚です。1枚目は、分筆に伴って権利を消滅させるときの流れを示します。2枚目は、分筆した土地の地番の付け方を表で示します。',
    notebooks=[
        dict(name='分筆に伴って権利を消滅させるとき', args=dict(
            title='分筆で権利を消すには？', sub='分筆に伴う権利の消滅の登記（毎日ドリル 第74日 ア・イ）',
            req='a flow diagram',
            layout=_nb1_layout,
            callout='乙土地について権利を消滅させる場合、甲土地の登記に付記して記録します。乙土地には転写しません。\n消滅させる権利を目的とする第三者の権利があるときは、その第三者の承諾も必要です。',
            footer='不動産登記法40条、不動産登記規則104条2項',
            kanji=[], what='blocks',
            check='confirm there are exactly three steps connected by downward arrows with no text, ')),
        dict(name='分筆した土地の地番', args=dict(
            title='分筆した土地の地番は？', sub='支号の付け方（毎日ドリル 第74日 ウ）',
            req='a table',
            layout=_nb2_layout,
            callout='本番に支号のある土地を分筆するときは、一筆に従来の地番を残し、他の筆には本番の最終の支号の次を付けます。\n支号の支号は使いません。',
            footer='不動産登記事務取扱手続準則67条1項4号・9号',
            kanji=[], what='table',
            check='confirm there are exactly two data rows and a gray note below the table, ')),
    ],
)

for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = K(_a['title'], _a['sub'], _a['layout'], _a['callout'], _a['footer'])
