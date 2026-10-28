def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='所有権の登記の有無と代位で決まる',
    intro='表示に関する登記の登録免許税について、課税されるものとされないもの、税額の数え方を問う問題です（登録免許税法5条・別表第一）。この問題は、誤っている記述を選ぶ形式です。\n\nこの記事では、「そもそも課税されるのか」「課税されるなら個数をどう数えるのか」を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('表題部の登記の抹消には、登録免許税が課されない',
               '登記の抹消には登録免許税が課されますが、土地又は建物の表題部の登記の抹消は除かれています（登録免許税法別表第一の一（十五））。\n\n合筆の登記は表題部の登記なので、その抹消に登録免許税は課されません。本肢は正しい記述です。\n\n**たとえば**、2筆の土地を合筆したものの、あとで合筆の登記に錯誤があったと分かった場合、その合筆の登記の抹消には、登録免許税はかかりません。'),
        'イ': ('所有権の登記がない土地の分筆には、登録免許税が課されない',
               '分筆などの登記に登録免許税が課されるのは、所有権の登記のある不動産の場合です。分筆後の不動産の個数1個につき、1,000円となります（登録免許税法別表第一の一（十三）イ）。\n\n丙土地は、所有権の登記がなく、表題部所有者だけが記録されています。この分筆の登記には、登録免許税は課されないので、3,000円としている本肢は誤りです。\n\n**たとえば**、表題登記だけがされていて、所有権の登記がまだない土地を3筆に分筆しても、登録免許税はかかりません。所有権の登記がある土地なら、3筆に分筆すると3,000円です。'),
        'ウ': ('地方公共団体が代位してする登記は、登録免許税が課されない',
               '国又は別表第二に掲げる者が、これらの者以外の者に代わってする登記は、登録免許税が課されません（登録免許税法5条1号）。市などの地方公共団体は、別表第二に掲げられています。\n\nB市が私人Cに代位して分筆の登記を嘱託する場合は、この非課税に当たります。分筆後が2筆でも課されないので、2,000円としている本肢は誤りです。\n\n**たとえば**、市が道路用地として買った土地の一部を、売主に代わって分筆する登記を嘱託する場合、その登記に登録免許税はかかりません。課税されるかどうかは、代わって申請する人が地方公共団体かどうかで決まります。'),
        'エ': ('区分の登記は、区分後の個数1個につき1,000円',
               '建物の区分による登記事項の変更の登記には、区分後の不動産の個数1個につき、1,000円が課されます（登録免許税法別表第一の一（十三）イ）。\n\n1個の区分建物を区分して2個にするので、2個で2,000円です。本肢は正しい記述です。\n\n**たとえば**、1つの店舗（区分建物）を壁で仕切って、2つの区分建物に分ける登記は、区分後の2個分で2,000円です。区分前の1個ではなく、区分後の個数で数えます。'),
        'オ': ('分割と合併を一括で申請するときは、甲建物と乙建物の2個で数える',
               '建物の分割による登記事項の変更の登記と、建物の合併による登記事項の変更の登記には、それぞれ後の個数1個につき1,000円が課されます（登録免許税法別表第一の一（十三）イ・ロ）。\n\n附属建物を分割して乙建物の附属建物とする場合、切り離した附属建物は独立した1個として残らないので、課税の対象は甲建物と乙建物の2個で、2,000円とされています。本肢は正しい記述です。\n\n**たとえば**、甲建物の附属建物の納屋を切り離して、乙建物の附属建物にする場合、納屋を1個と数えて3,000円になるのではなく、甲建物と乙建物の2個分で2,000円です。'),
    },
    summary=[
        ('ア', '正', '土地又は建物の表題部の登記の抹消には、登録免許税が課されない'),
        ('イ', '誤', '所有権の登記がない土地の分筆の登記には、登録免許税が課されない（3,000円ではない）'),
        ('ウ', '誤', '地方公共団体が私人に代位してする登記は非課税で、2,000円ではない'),
        ('エ', '正', '区分の登記は、区分後の個数1個につき1,000円なので、2個に区分すると2,000円'),
        ('オ', '正', '分割と合併を一の申請情報で申請するときは、甲建物と乙建物の2個で2,000円とされる'),
    ],
    summary_tail='イは「所有権の登記の有無」、ウは「代位する人」を見落とした出題です。課税されるかどうかは、登記の種類、所有権の登記の有無、申請する人の順に確かめましょう。',
    supplements=[
        '### 補足説明（イ・ウ）：課税されるかどうかの見分け方\n\n表示に関する登記の登録免許税は、次の順に確かめると整理できます。\n\n- 登記の種類：表題登記や滅失の登記などの多くは、別表第一に掲げられておらず、課税されない。\n- 所有権の登記の有無：分筆、分割、区分、合筆、合併は、所有権の登記のある不動産だけが課税される（別表第一の一（十三））。\n- 申請する人：国や地方公共団体が私人に代位してする登記は、非課税（5条1号）。\n\n**たとえば**、所有権の登記がない土地の分筆は、そもそも課税されません。所有権の登記がある土地でも、市が代位して嘱託するなら非課税です。',
        '### 補足説明（オ）：税額は、変更後の個数で数える\n\n課税される登記は、1個につき1,000円で、数える個数は登記の種類で決まります。\n\n- 分筆、分割、区分：分筆後、分割後、区分後の不動産の個数。\n- 合筆、合併：合筆後、合併後の不動産の個数。\n- 分割と合併を一の申請情報で申請するとき：切り離した附属建物は独立した1個として残らないので、甲建物と乙建物の2個。\n\n**たとえば**、土地を3筆に分筆すれば3,000円、区分建物を2個に区分すれば2,000円です。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第101日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、登録免許税法5条1号、別表第一の一（十三）・（十五）は、`note-articles/laws/` 配下の原文で確認しました。別表第二（地方公共団体が掲げられていること）は、手元の法令ファイルに収録がないため、原文は未確認です。',
        'オの「切り離した附属建物は独立した1個として残らないので2個」という数え方は、条文の文言から直接出るものではなく、取扱いからの整理です。',
        '「表題登記や滅失の登記などの多くは別表第一に掲げられていない」という説明は、別表第一の構成からの一般的な整理です。具体例の人物と場面は、理解のために設けた架空の例です。',
    ],
    phrases=['表題部の登記の抹消は課税されません', '所有権の登記がなければ分筆も課税なしです', '地方公共団体が代位する登記は非課税です', '区分は区分後の個数で数えます', '分割と合併の一括は二個で数えます'],
    header=dict(t1='表示の登記の税、', t2='かかる？かからない？', topic='登録免許税法　表示に関する登記', kanji=''),
    poster_intro='表示に関する登記の登録免許税を、「課税されない登記」（グループA：ア・イ・ウ）と「課税される個数の数え方」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='表示に関する登記の登録免許税', sub='登録免許税法 第5条と別表第一（毎日ドリル 第101日）',
        col_a='課税されない登記', col_b='課税される個数', n_a=3,
        cards=[
            dict(h='表題部の登記の抹消は課税されない',
                 ill='a record sheet showing two merged land plots, with a round stamp labeled 「抹消」 over the merged line. A green check mark sits beside the stamp.',
                 words=['抹消'], tag='課税の対象外'),
            dict(h='所有権の登記がない土地の分筆は課税なし',
                 ill='a land plot split into three parts, with a record sheet beside it. The ownership section of the record sheet is empty and drawn in faded gray; only a title-section owner line is filled in. A tag on the plot is labeled 「分筆」. A green check mark sits beside the record sheet.',
                 words=['分筆'], tag='所有権の登記が前提'),
            dict(h='地方公共団体の代位による登記は非課税',
                 ill='a city hall building figure holding a form, standing behind a private owner figure, with a thin arrow between them. A tag on the form is labeled 「代位」. A green check mark sits beside the form.',
                 words=['代位'], tag='非課税登記'),
            dict(h='区分は区分後の個数で数える',
                 ill='one condominium unit on the left splitting into two units on the right, with a tag on the arrow labeled 「区分」. A green check mark sits beside the two units.',
                 words=['区分'], tag='二個で二千円'),
            dict(h='分割と合併の一括は二個で数える',
                 ill='building A with an annex on the left; an arrow moves the annex to building B on the right. Two tags are placed on the arrow, labeled 「分割」 and 「合併」. A green check mark sits beside the two buildings.',
                 words=['分割', '合併'], tag='二個で二千円'),
        ],
        kanji=[]),
    nb_label='イ・ウ・オ肢', nb_intro='イ・ウ・オの補足説明に合わせた2枚です。1枚目は、課税されるかどうかを確かめる順番を流れで示します。2枚目は、課税される登記の個数の数え方を表で整理します。',
    notebooks=[
        dict(name='課税されるかどうかの見分け方', args=dict(
            title='課税されるかを確かめる順番', sub='表示に関する登記の登録免許税（毎日ドリル 第101日 イ・ウ）',
            req='a vertical flow diagram',
            layout="""--- FLOW ---
Render as a clean flat-design vertical flow of three steps connected by small downward arrows with no text. Do not number the steps. Do not use any check mark or cross mark. Use exactly these strings, and no others.
Step 1 (blue accent), step header: 登記の種類. Text: 表題登記や滅失の登記などの多くは課税されない. Icon: a record sheet.
Step 2 (green accent), step header: 所有権の登記の有無. Text: 分筆、分割、区分、合筆、合併は、所有権の登記のある不動産だけが課税される. Icon: a land plot split into parts.
Step 3 (orange accent), step header: 申請する人. Text: 国や地方公共団体が私人に代位してする登記は非課税. Icon: a city hall building figure.""",
            callout='課税されるかは、登記の種類、所有権の登記の有無、申請する人の順に確かめます。\n所有権の登記がない土地の分筆や、地方公共団体が代位してする登記は、課税されません。',
            footer='登録免許税法5条1号、別表第一の一（十三）', kanji=[], what='steps',
            check='confirm there are exactly three steps with the given headers and texts, ')),
        dict(name='課税される個数の数え方', args=dict(
            title='税額は何個で数える？', sub='分筆と区分と分割と合併（毎日ドリル 第101日 オ）',
            req='a three-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and three data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 登記 | 数える個数 | 税額
Row 1: 土地を三筆に分筆 | 分筆後の三個 | 三千円
Row 2: 区分建物を二個に区分 | 区分後の二個 | 二千円
Row 3: 分割と合併を一の申請情報で申請 | 甲建物と乙建物の二個 | 二千円
Next to each row, draw a small icon: row 1 shows a land plot split into three parts, row 2 shows a condominium unit split in two, row 3 shows an annex moving from one building to another.""",
            callout='税額は、一個につき千円で、変更後の個数で数えます。\n分割と合併を一括で申請するときは、切り離した附属建物は数えず、甲建物と乙建物の二個です。',
            footer='登録免許税法別表第一の一（十三）', kanji=[], what='table',
            check='confirm the table has exactly three columns and three data rows with the given strings, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
