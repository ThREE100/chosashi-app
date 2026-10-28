def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='更正に期限はなく、分筆と一括できる',
    intro='地積に関する更正の登記について、誤差の限度の基準、申請の期間、一の申請情報での申請、地積の端数の切り捨てを問う問題です（不動産登記法37条・38条、不動産登記規則35条・100条、不動産登記事務取扱手続準則70条・72条）。\n\nこの記事では、「何を基準に比べるのか」「変更と更正で何が違うのか」を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('申請した地積を基準に、誤差の限度内なら相当と認められる',
               '申請情報の内容とした地積と、登記官の実地調査の結果による地積との差が、申請情報の内容とした地積を基準にして地積測量図の誤差の限度内であるときは、申請情報の内容とした地積を相当と認めて差し支えないとされています。\n\nこれは土地の表示に関する登記の申請についての扱いです（不動産登記事務取扱手続準則70条）。\n\n本肢は正しいといえます。\n\n**たとえば**、Aさんが「面積は200.00平方メートルです」と申請し、登記官が現地を調べたら少し違う値だったとします。\n\nその差が、申請した200.00平方メートルを基準にした誤差の限度内なら、登記官は、Aさんが申請した地積を相当と認めてよいことになります。'),
        'イ': ('分筆では、分筆前の地積を基準に誤差の限度を見る',
               '分筆の登記を申請する場合に、分筆前の地積と分筆後の地積の差が、分筆前の地積を基準にして地積測量図の誤差の限度内であるときは、地積に関する更正の登記の申請は要りません（不動産登記事務取扱手続準則72条1項）。\n\n問題文は、分筆後の地積を基準にするとしているので、本肢は誤りです。\n\n**たとえば**、登記記録の面積が500平方メートルの土地を2筆に分筆するとき、分筆後の2筆の地積の合計と500平方メートルの差を、分筆前の500平方メートルを基準にした誤差の限度と比べます。'),
        'ウ': ('更正の登記には、一月以内という申請の期間がない',
               '一月以内の申請義務があるのは、地積の変更の登記です（不動産登記法37条1項）。地積の更正の登記には、申請の期間の定めがありません（同法38条）。また、過料の対象にも挙げられていません（同法164条1項）。\n\n問題文は、知った日から一月以内に更正の登記を申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、測量したら、登記記録の地積が最初から間違っていたと分かった場合、Aさんに「いつまでに更正の登記をしなければならない」という期限はありません。\n\n一方、土地の一部が川に削られて面積が実際に減ったときは、変更の登記を、変更の日から一月以内に申請しなければなりません。'),
        'エ': ('地積の更正と分筆は、一の申請情報で申請できる',
               '同一の不動産について申請する二以上の登記が、表題部の登記事項に関する変更の登記又は更正の登記と、土地の分筆の登記であるときは、一の申請情報によって申請できます（不動産登記規則35条7号）。\n\n本肢は正しいといえます。\n\n**たとえば**、土地の一部を売るために分筆しようとして測量したところ、登記記録の地積が間違っていたと分かったとします。Aさんは、地積の更正の登記と分筆の登記を、1つの申請書でまとめて申請できます。'),
        'オ': ('宅地の地積は、100分の1平方メートル未満を切り捨てる',
               '地積は、水平投影面積により、平方メートルを単位として定めます。1平方メートルの100分の1未満の端数は切り捨てます。ただし、宅地及び鉱泉地以外の土地で10平方メートルを超えるものは、1平方メートル未満の端数を切り捨てます（不動産登記規則100条）。\n\n乙土地の地目は宅地なので、150.456平方メートルは、150.45平方メートルと記録されます。問題文は150平方メートルとしているので、本肢は誤りです。\n\n**たとえば**、同じ150.456平方メートルでも、地目が山林なら、1平方メートル未満を切り捨てて150平方メートルと記録されます。宅地は小数第2位まで記録するので、150.45平方メートルです。'),
    },
    summary=[
        ('ア', '正', '申請した地積と実地調査の地積の差が、申請した地積を基準にして誤差の限度内なら、申請した地積を相当と認めてよい'),
        ('イ', '誤', '分筆では、分筆前の地積を基準に誤差の限度を見る（分筆後の地積ではない）'),
        ('ウ', '誤', '地積の更正の登記には、一月以内という申請の期間の定めがない'),
        ('エ', '正', '地積の更正の登記と分筆の登記は、一の申請情報で申請できる'),
        ('オ', '誤', '宅地の地積は1平方メートルの100分の1未満を切り捨てるので、150.456は150.45になる'),
    ],
    summary_tail='イは「基準になる地積」、ウは「変更と更正」、オは「地目による端数処理」をすり替えた出題です。何を基準に比べるか、期間があるのはどちらか、地目で端数が変わることを分けて覚えましょう。',
    supplements=[
        '### 補足説明（イ）：誤差の限度は、何を基準にするか\n\n誤差の限度を見るときは、場面によって基準にする地積が決まっています。\n\n- 申請した地積と、実地調査の地積を比べる場面：申請情報の内容とした地積が基準（準則70条）。\n- 分筆前と分筆後の地積を比べる場面：分筆前の地積が基準（準則72条1項）。\n\n**たとえば**、登記記録の面積が500平方メートルの土地を分筆する場合は、分筆後の面積ではなく、分筆前の500平方メートルを基準にして、誤差の限度を計算します。',
        '### 補足説明（オ）：地目で変わる、地積の端数の切り捨て\n\n地積は、地目によって、切り捨てる位が違います（不動産登記規則100条）。\n\n- 宅地と鉱泉地：1平方メートルの100分の1未満を切り捨てる。\n- 宅地と鉱泉地以外の土地で10平方メートルを超えるもの：1平方メートル未満を切り捨てる。\n\n**たとえば**、測量の結果が150.456平方メートルだった場合、宅地なら150.45平方メートル、山林なら150平方メートルと記録されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第98日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法37条・38条・164条1項、不動産登記規則35条7号・100条、不動産登記事務取扱手続準則70条・72条1項は、`note-articles/laws/` 配下の原文で確認しました。',
        'イの具体例は、準則72条1項の「分筆後の地積」を、分筆後の各筆の地積の合計として説明した、一般的な整理です。',
        '具体例の人物と場面（川に削られた土地、土地の一部を売るための分筆など）は、理解のために設けた架空の例です。',
    ],
    phrases=['申請した地積が誤差の基準になります', '分筆では分筆前の地積が基準です', '更正の登記に申請の期限はありません', '更正と分筆は一つの申請でできます', '宅地は百分の一未満を切り捨てます'],
    header=dict(t1='地積の直し方、', t2='何がカギ？', topic='不動産登記法　地積の更正', kanji=''),
    poster_intro='地積の更正を、「誤差の限度と申請」（グループA：ア・イ・ウ）と「一括申請と端数」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地積の更正を整理', sub='不動産登記法 第37条と第38条、規則 第35条と第100条（毎日ドリル 第98日）',
        col_a='誤差の限度と申請', col_b='一括申請と端数', n_a=3,
        cards=[
            dict(h='申請の地積を基準に誤差の限度を見る',
                 ill='an isometric land plot sheet labeled 「申請」 with a measuring band drawn around it, and a surveyor figure comparing it with a second plot sheet. A green check mark sits beside the first sheet.',
                 words=['申請'], tag='申請の地積が基準'),
            dict(h='分筆では分筆前の地積が基準',
                 ill='a large land plot on the left labeled 「分筆前」 with a green bracket around it, and an arrow to two smaller plots on the right drawn in gray. A green check mark sits beside the bracket.',
                 words=['分筆前'], tag='分筆前の地積が基準'),
            dict(h='更正の登記に申請の期限はない',
                 ill='a calendar page with no date circled, and a record sheet with one line corrected by a pencil beside it. A tag on the record sheet is labeled 「更正」. No check mark and no cross mark on this card.',
                 words=['更正'], tag='期間の定めなし'),
            dict(h='更正と分筆は一つの申請でできる',
                 ill='two forms, one labeled 「更正」 and one labeled 「分筆」, placed together into a single folder. A green check mark sits beside the folder.',
                 words=['更正', '分筆'], tag='一の申請情報'),
            dict(h='宅地は小数第二位まで記録する',
                 ill='an isometric house plot labeled 「宅地」 with a measuring tape running along it; a pair of scissors cuts off the end of the tape. A green check mark sits beside the plot.',
                 words=['宅地'], tag='百分の一未満は切捨て'),
        ],
        kanji=[]),
    nb_label='イ・オ肢', nb_intro='イ・オの補足説明に合わせた2枚です。1枚目は、誤差の限度の基準になる地積を左右の対比で示します。2枚目は、地目による端数の切り捨てを表で整理します。',
    notebooks=[
        dict(name='誤差の限度の基準になる地積', args=dict(
            title='誤差の限度は何を基準に見る？', sub='準則70条と72条（毎日ドリル 第98日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「申請と実地調査」 on the left and 「分筆前と分筆後」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 申請と実地調査
Scene: a land plot sheet and a surveyor figure comparing it with an on-site measurement, with a bracket drawn around the sheet.
Label under the scene: 基準は申請情報の地積

RIGHT PANEL (orange accent):
Panel header: 分筆前と分筆後
Scene: a large land plot split into two smaller plots, with a bracket drawn around the large plot.
Label under the scene: 基準は分筆前の地積
Use exactly these strings, and no others, for the labels.""",
            callout='誤差の限度は、場面によって基準になる地積が違います。\n分筆の場面では、分筆後ではなく、分筆前の地積を基準にします。',
            footer='不動産登記事務取扱手続準則70条・72条1項', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (申請と実地調査 on the left and 分筆前と分筆後 on the right) drawn in different accent colors, ')),
        dict(name='地目で変わる端数の切り捨て', args=dict(
            title='地積の端数の切り捨て', sub='地目で変わる位（毎日ドリル 第98日 オ）',
            req='a two-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and two data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 地目 | 切り捨てる端数 | 150.456平方メートルの場合
Row 1: 宅地と鉱泉地 | 一平方メートルの百分の一未満 | 150.45平方メートル
Row 2: 宅地と鉱泉地以外で十平方メートルを超える土地 | 一平方メートル未満 | 150平方メートル
Next to each row, draw a small icon: row 1 shows a house plot, row 2 shows a forest plot with trees.""",
            callout='宅地は、百分の一平方メートル未満を切り捨てます。\n宅地以外の土地で十平方メートルを超えるものは、一平方メートル未満を切り捨てます。',
            footer='不動産登記規則100条', kanji=[], what='table',
            check='confirm the table has exactly three columns and two data rows with the given strings, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
