def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='滅失は一月以内、解体移転は滅失と新築',
    intro='建物の滅失の登記について、申請の期間、申請できる人、主たる建物だけがなくなった場合、建物を動かした場合の扱いを問う問題です（不動産登記法30条・57条、不動産登記事務取扱手続準則85条・102条）。\n\nこの記事では、「建物そのものがなくなったのか」「建物が動いただけなのか」という見分け方を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('滅失の登記の申請は、滅失の日から一月以内',
               '建物が滅失したときは、表題部所有者又は所有権の登記名義人は、その滅失の日から一月以内に、建物の滅失の登記を申請しなければなりません（不動産登記法57条）。\n\n問題文は「二月以内」としているので、本肢は誤りです。\n\n**たとえば**、令和8年6月1日に火災で家が全焼した場合、所有者のAさんは、6月1日から一月以内に滅失の登記を申請します。二月まで待つことはできません。\n\nこの申請を正当な理由なく怠ると、10万円以下の過料に処せられることがあります（同法164条1項）。'),
        'イ': ('相続人は、相続の登記をしなくても滅失の登記を申請できる',
               '所有権の登記名義人が表示に関する登記の申請人となることができる場合に、その人について相続があったときは、相続人は、その表示に関する登記を申請できます（不動産登記法30条）。\n\n本肢は正しいといえます。\n\n**たとえば**、Bさん名義の建物が、Bさんの死亡後に取り壊されたとします。相続人のCさんは、相続の登記をしないまま、申請情報に相続人であることを書き、相続があったことを証する戸籍謄本などを添えて、滅失の登記を申請できます。'),
        'ウ': ('主たる建物だけを取り壊しても、建物全体の滅失ではない',
               '附属建物がある主たる建物が滅失したときは、建物全体の滅失の登記ではなく、表題部の登記事項に関する変更の登記をします。\n\nこの登記では、主たる建物の滅失の原因を記録し、主たる建物となるべき附属建物の表示を、主たる建物の欄に記録します（不動産登記事務取扱手続準則102条）。\n\n問題文は、丙建物の滅失の登記を申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、母屋と離れの納屋が1つの建物として登記されていて、母屋だけを取り壊したとします。残る納屋が新しい主たる建物になるので、建物全体の滅失の登記ではなく、表題部を直す変更の登記になります。'),
        'エ': ('えい行移転は、所在の変更として扱われる',
               '建物をえい行移転した場合は、建物の所在の変更として取り扱います（不動産登記事務取扱手続準則85条2項）。滅失の登記と表題登記になるのは、解体移転の場合です（同条1項）。\n\n問題文は、えい行移転の場合に、滅失の登記と表題登記を申請するとしているので、本肢は誤りです。\n\n**たとえば**、建物を壊さずに、そのまま持ち上げて、同じ所有者の隣の土地へ動かしたとします。建物そのものは残っているので、建物の所在が変わった扱いとなり、滅失と新築の組合せにはなりません。'),
        'オ': ('解体移転は、滅失した建物と新築した建物として扱われる',
               '建物を解体移転した場合は、既存の建物が滅失し、新たな建物が建築されたものとして取り扱います（不動産登記事務取扱手続準則85条1項）。\n\nそのため、既存の建物については滅失の登記（不動産登記法57条）、新たな建物については表題登記（同法47条1項）を申請します。本肢は正しいといえます。\n\n**たとえば**、古い家を解体し、その材料を使って、別の土地に同じ形の家を建て直したとします。元の家は滅失、新しい家は新築として扱われ、元の家の滅失の登記と、新しい家の表題登記を申請します。'),
    },
    summary=[
        ('ア', '誤', '建物の滅失の登記は、滅失の日から一月以内に申請する'),
        ('イ', '正', '所有権の登記名義人が死亡したときは、相続人が相続の登記をしないで滅失の登記を申請できる'),
        ('ウ', '誤', '附属建物が残る場合に主たる建物だけを取り壊したときは、滅失の登記ではなく、表題部の変更の登記をする'),
        ('エ', '誤', 'えい行移転は建物の所在の変更として扱い、滅失の登記と表題登記は不要'),
        ('オ', '正', '解体移転は、既存の建物の滅失と新たな建物の新築として扱い、滅失の登記と表題登記を申請する'),
    ],
    summary_tail='アは「期間」、ウは「全部と一部」、エは「移転の種類」をすり替えた出題です。建物そのものがなくなったか、動いただけか、一部が残るかで見分けましょう。',
    supplements=[
        '### 補足説明（ウ）：建物全体がなくなったのか、一部が残るのか\n\n同じ「取り壊した」でも、残るものがあるかどうかで、登記が変わります。\n\n- 建物全体が滅失した場合：建物の滅失の登記（不動産登記法57条）。\n- 附属建物がある主たる建物だけが滅失した場合：表題部の変更の登記（不動産登記事務取扱手続準則102条）。\n\n**たとえば**、母屋も納屋も取り壊したなら、建物全体の滅失の登記です。母屋だけを取り壊し、納屋が残るなら、納屋が新しい主たる建物になる変更の登記です。',
        '### 補足説明（エ・オ）：解体移転とえい行移転の違い\n\n建物を別の場所へ移す方法には、2通りあります。扱いが違うので、登記も違います。\n\n- 解体移転：既存の建物の滅失と、新たな建物の建築として扱う。滅失の登記と表題登記を申請する。\n- えい行移転：建物の所在の変更として扱う。\n\n**たとえば**、建物を壊して、材料を使って別の土地に建て直すのが解体移転です。壊さずに、そのまま動かすのがえい行移転です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第97日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法30条、47条1項、57条、164条1項、不動産登記令3条10号・7条1項4号、不動産登記事務取扱手続準則85条・102条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの「建物全体の滅失ではない」という説明は、準則102条（附属建物がある主たる建物の滅失は、表題部の登記事項に関する変更の登記による）からの一般的な整理です。',
        'エの登記の方法（所在の変更として扱う）は準則85条2項の文言によります。具体例の人物と場面は、理解のために設けた架空の例です。',
    ],
    phrases=['滅失の登記は一月以内に申請します', '相続人は相続登記なしで申請できます', '主たる建物だけの取壊しは変更の登記です', 'えい行移転は所在の変更になります', '解体移転は滅失と新築の二つの登記です'],
    header=dict(t1='建物がなくなったら、', t2='どんな登記？', topic='不動産登記法　建物の滅失', kanji=''),
    poster_intro='建物の滅失と移転を、「滅失の登記の基本」（グループA：ア・イ・ウ）と「建物を動かすとき」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='建物の滅失と移転を整理', sub='不動産登記法 第57条（毎日ドリル 第97日）',
        col_a='滅失の登記の基本', col_b='建物を動かすとき', n_a=3,
        cards=[
            dict(h='滅失の日から一月以内に申請',
                 ill='an isometric house that has burned down, drawn as a blackened outline, with a calendar page labeled 「一月以内」 beside it. A green check mark sits beside the calendar.',
                 words=['一月以内'], tag='滅失の日から数える'),
            dict(h='相続人は相続の登記なしで申請できる',
                 ill='a faded gray portrait frame on the left and an heir figure on the right holding a form and a name tag labeled 「相続人」, standing in front of a demolished house outline. A green check mark sits beside the heir.',
                 words=['相続人'], tag='相続登記は不要'),
            dict(h='主たる建物だけの取壊しは変更の登記',
                 ill='a main building drawn as a dashed outline of a demolished building, and a small annex beside it that remains, highlighted with a green glow and labeled 「附属建物」. A green check mark sits beside the annex.',
                 words=['附属建物'], tag='表題部の変更'),
            dict(h='えい行移転は所在の変更',
                 ill='an isometric house lifted on rollers moving across to the adjacent land plot, with a thin arrow. A tag on the house is labeled 「えい行移転」. A green check mark sits beside the house.',
                 words=['えい行移転'], tag='所在が変わる'),
            dict(h='解体移転は滅失と新築',
                 ill='on the left a demolished house outline with a round stamp labeled 「滅失」, an arrow in the middle, and on the right a new house with a round stamp labeled 「新築」. A green check mark sits above the arrow.',
                 words=['滅失', '新築'], tag='二つの登記になる'),
        ],
        kanji=[]),
    nb_label='ウ・エ・オ肢', nb_intro='ウ・エ・オの補足説明に合わせた2枚です。1枚目は、建物全体がなくなる場合と主たる建物だけがなくなる場合を、左右の対比で示します。2枚目は、解体移転とえい行移転の違いを表で整理します。',
    notebooks=[
        dict(name='建物全体の滅失と、主たる建物だけの滅失', args=dict(
            title='全部がなくなるか、一部が残るか', sub='建物の滅失（毎日ドリル 第97日 ウ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「建物全体の滅失」 on the left and 「主たる建物だけの滅失」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 建物全体の滅失
Scene: a main building and an annex, both drawn as dashed outlines of demolished buildings.
Result badge: 建物の滅失の登記

RIGHT PANEL (orange accent):
Panel header: 主たる建物だけの滅失
Scene: a main building drawn as a dashed outline of a demolished building, and an annex that remains and is highlighted, with a small arrow from the annex to the empty place of the main building.
Result badge: 表題部の変更の登記
Use exactly these strings, and no others, for the labels.""",
            callout='建物全体がなくなったときは、滅失の登記をします。\n附属建物が残るときは、附属建物が主たる建物になるよう、表題部の変更の登記をします。',
            footer='不動産登記法57条、不動産登記事務取扱手続準則102条', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (建物全体の滅失 on the left and 主たる建物だけの滅失 on the right) drawn in different accent colors, ')),
        dict(name='解体移転とえい行移転の違い', args=dict(
            title='建物を移すときの登記', sub='解体移転とえい行移転（毎日ドリル 第97日 エ・オ）',
            req='a two-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and two data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 移し方 | 建物の扱い | 登記
Row 1: 解体移転 | 既存の建物の滅失と新たな建物の建築 | 滅失の登記と表題登記
Row 2: えい行移転 | 建物の所在の変更 | 表題部の変更
Next to each row, draw a small icon: row 1 shows a demolished house outline and a new house, row 2 shows a house lifted on rollers.""",
            callout='解体移転は、滅失と新築として扱います。\nえい行移転は、建物が残ったまま所在が変わった扱いです。',
            footer='不動産登記事務取扱手続準則85条', kanji=[], what='table',
            check='confirm the table has exactly three columns and two data rows with the given strings, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
