def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='家屋番号は不要、番号の提供で省略可',
    intro='登記の申請で提供する、申請情報の内容と添付情報について、記載すべき事項、共通する添付情報の扱い、相続人が申請するとき、法人の証明、住所の証明の省略を問う問題です（不動産登記令3条・7条・9条、不動産登記規則36条・37条）。\n\nこの記事では、「何を書くのか」「何を添えるのか」「何を省略できるのか」を、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('建物の表題登記では、申請情報に家屋番号を書かない',
               '建物の表示に関する登記を申請するときは、申請情報の内容として家屋番号を記載するのが原則ですが、建物の表題登記を申請する場合は除かれています（不動産登記令3条8号ロ）。家屋番号は、登記所が一個の建物ごとに付すものだからです（不動産登記法45条）。\n\n問題文は、甲建物の家屋番号を記載しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、新築した家の表題登記を申請するとき、その家にはまだ家屋番号が付いていません。申請人は、家屋番号を書く必要がありません。'),
        'イ': ('共通する添付情報を併せて提供したら、その旨を他の申請に書く',
               '同一の登記所に同時に二以上の申請をする場合に、各申請に共通する添付情報があるときは、一の申請の申請情報と併せて提供すれば足ります（不動産登記規則37条1項）。\n\nただし、その場合は、添付情報を併せて提供した旨を、他の申請の申請情報の内容としなければなりません（同条2項）。問題文は、その旨を記載する必要はないとしているので、本肢は誤りです。\n\n**たとえば**、Aさんが土地家屋調査士に頼んで、分筆と地目の変更を同時に申請する場合、委任状は1通を添えれば足ります。ただし、もう一方の申請書には、「委任状は、他の申請に添付した」という旨を書きます。'),
        'ウ': ('相続人が申請するときは、相続人である旨と相続を証する情報',
               '表題部所有者の相続人が、法30条の規定により表示に関する登記を申請するときは、申請情報の内容として、申請人が相続人その他の一般承継人である旨を記載します（不動産登記令3条10号）。\n\n添付情報としては、相続その他の一般承継があったことを証する、市町村長、登記官その他の公務員が職務上作成した情報を提供します（同令7条1項4号）。本肢は正しいといえます。\n\n**たとえば**、表題部所有者のBさんが亡くなった後、相続人のCさんが土地の地目の変更の登記を申請するなら、申請書に「申請人はBさんの相続人である」と書き、相続を証する戸籍謄本などを添えます。'),
        'エ': ('登記事項証明書は、作成後3月以内のもの',
               '会社法人等番号の提供に代えて、代表者の資格を証する登記事項証明書を提供して申請する場合、その登記事項証明書は、作成後3月以内のものでなければなりません（不動産登記規則36条1項・2項）。\n\n問題文は「作成後一月以内」としているので、本肢は誤りです。\n\n**たとえば**、株式会社が、取得してから2か月たった登記事項証明書を添えて申請する場合でも、作成後3月以内なので、期間の点では使うことができます。'),
        'オ': ('住民票コードを提供すれば、住所を証する情報は省略できる',
               '申請情報と併せて住所を証する情報を提供しなければならない場合でも、法務省令で定める情報を提供したときは、住所を証する情報の提供は要りません（不動産登記令9条）。\n\n法務省令で定める情報は、住民票コード又は会社法人等番号です（不動産登記規則36条4項）。本肢は正しいといえます。\n\n**たとえば**、Eさんが新築した家の表題登記を、自分を表題部所有者として申請するとき、申請情報にEさんの住民票コードを書いておけば、住民票の写しなどの住所を証する書類を添える必要はありません。'),
    },
    summary=[
        ('ア', '誤', '建物の表題登記では、申請情報の内容として家屋番号を記載しない（登記所が付す）'),
        ('イ', '誤', '共通する添付情報を一の申請と併せて提供したときは、その旨を他の申請の申請情報の内容とする'),
        ('ウ', '正', '相続人が申請するときは、相続人である旨を記載し、相続を証する公務員作成の情報を提供する'),
        ('エ', '誤', '会社法人等番号に代えて提供する登記事項証明書は、作成後3月以内のもの'),
        ('オ', '正', '住民票コードを提供すれば、住所を証する情報の提供は要らない'),
    ],
    summary_tail='アは「書く事項」、イは「旨の記載」、エは「期間」をすり替えた出題です。原則と例外、省略するときに必要なひと手間、期間の数字を分けて覚えましょう。',
    supplements=[
        '### 補足説明（ア）：建物の表題登記と、ほかの登記の違い\n\n建物の登記では、家屋番号を申請情報に書くかどうかが、登記の種類で変わります。\n\n- 建物の表題登記：家屋番号は申請情報の内容にしない（不動産登記令3条8号ロ）。\n- 建物のほかの登記（表題部の変更の登記など）：家屋番号を申請情報の内容とする。\n\n**たとえば**、新築した家の表題登記では、家屋番号は登記所が付けるので書きません。その後、増築して表題部の変更の登記をするときは、すでに付いている家屋番号を申請情報に書きます。',
        '### 補足説明（イ・エ）：「旨の記載」と「3月以内」\n\n添付情報の提供には、細かい決まりがあります。数字と、ひと手間を整理しておきましょう。\n\n- 共通する添付情報：一の申請と併せて提供すれば足りるが、その旨を他の申請の申請情報に書く（規則37条）。\n- 登記事項証明書：会社法人等番号に代えて提供するときは、作成後3月以内（規則36条）。\n\n**たとえば**、同時に2件の申請をして、委任状を1通だけ添えたなら、もう一方の申請書に「委任状は他の申請に添付した」旨を書きます。法人の登記事項証明書は、取得から3月以内のものを使います。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第99日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法45条、不動産登記令3条8号ロ・10号、7条1項4号、9条、不動産登記規則36条・37条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの「新築した家にはまだ家屋番号が付いていない」という説明は、法45条（登記所が一個の建物ごとに家屋番号を付す）からの一般的な整理です。',
        '具体例の人物と場面は、理解のために設けた架空の例です。条文にない事実は断定していません。',
    ],
    phrases=['建物の表題登記に家屋番号は書きません', '共通の添付は旨を書いて一度で足ります', '相続人が申請するときは相続を証する情報です', '登記事項証明書は三月以内のものです', '住民票コードで住所の証明は省略できます'],
    header=dict(t1='申請情報と添付、', t2='何が必要？', topic='不動産登記令　申請情報と添付情報', kanji=''),
    poster_intro='申請情報と添付情報を、「書く事項と添える情報」（グループA：ア・イ・ウ）と「法人と住所の証明」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='申請情報と添付情報を整理', sub='不動産登記令と不動産登記規則（毎日ドリル 第99日）',
        col_a='書く事項と添える情報', col_b='法人と住所の証明', n_a=3,
        cards=[
            dict(h='建物の表題登記に家屋番号は書かない',
                 ill='a new isometric house and an application form beside it. The form has a blank line labeled 「家屋番号」 drawn in faded gray, and a registry office clerk figure holds a number tag. A green check mark sits beside the clerk.',
                 words=['家屋番号'], tag='登記所が付ける'),
            dict(h='共通の添付は一度でよく、旨を書く',
                 ill='two application forms sharing one attached document labeled 「委任状」, with a small arrow pointing from the second form to the document and a note mark on the second form. A green check mark sits beside the document.',
                 words=['委任状'], tag='提供した旨を記載'),
            dict(h='相続人が申請するときは相続の証明',
                 ill='an heir figure holding an application form and a family-register document labeled 「戸籍」, standing beside a faded gray portrait frame. A green check mark sits beside the document.',
                 words=['戸籍'], tag='相続を証する情報'),
            dict(h='登記事項証明書は三月以内のもの',
                 ill='a company building, a certificate sheet beside it, and a calendar page labeled 「三月」 with a green bracket. A tag on the certificate is labeled 「登記事項証明書」. A green check mark sits beside the calendar.',
                 words=['登記事項証明書', '三月'], tag='作成後三月以内'),
            dict(h='住民票コードで住所の証明は省略できる',
                 ill='a person figure holding an identification card labeled 「住民票コード」, with a faded gray residence-certificate sheet set aside on the table. A green check mark sits beside the card.',
                 words=['住民票コード'], tag='住所の証明を省略'),
        ],
        kanji=[]),
    nb_label='ア・イ・エ肢', nb_intro='ア・イ・エの補足説明に合わせた2枚です。1枚目は、建物の表題登記とほかの登記の違いを左右の対比で示します。2枚目は、添付情報の細かい決まりを表で整理します。',
    notebooks=[
        dict(name='建物の表題登記と、ほかの登記の違い', args=dict(
            title='家屋番号を書く登記、書かない登記', sub='建物の申請情報（毎日ドリル 第99日 ア）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers are different strings: 「建物の表題登記」 on the left and 「表題部の変更の登記」 on the right. Draw them large and in different accent colors (blue on the left, orange on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 建物の表題登記
Scene: a newly built house and an application form whose house number line is blank.
Label under the scene: 家屋番号は申請情報に書かない

RIGHT PANEL (orange accent):
Panel header: 表題部の変更の登記
Scene: a house with an extension and an application form whose house number line is filled in with a small number tag.
Label under the scene: 家屋番号を申請情報に書く
Use exactly these strings, and no others, for the labels.""",
            callout='建物の表題登記では、家屋番号は登記所が付けるので、申請情報に書きません。\n表題部の変更の登記などでは、すでに付いている家屋番号を書きます。',
            footer='不動産登記令3条8号ロ', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (建物の表題登記 on the left and 表題部の変更の登記 on the right) drawn in different accent colors, ')),
        dict(name='旨の記載と、3月以内', args=dict(
            title='添付情報の細かい決まり', sub='共通の添付と登記事項証明書（毎日ドリル 第99日 イ・エ）',
            req='a two-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and two data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 場面 | 決まり | 根拠
Row 1: 共通する添付情報 | 併せて提供し、その旨を他の申請の申請情報に書く | 規則37条
Row 2: 登記事項証明書 | 会社法人等番号に代えて提供するときは作成後三月以内 | 規則36条
Next to each row, draw a small icon: row 1 shows two forms sharing one document, row 2 shows a certificate with a calendar page.""",
            callout='共通する添付情報は、一度の提供で足りますが、その旨を他の申請に書きます。\n登記事項証明書は、作成後三月以内のものを使います。',
            footer='不動産登記規則36条・37条', kanji=[], what='table',
            check='confirm the table has exactly three columns and two data rows with the given strings, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
