def kj(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '鿿' and c not in out:
                out.append(c)
    return out[:n]


D = dict(
    catch='地図は永久、建物の閉鎖記録は三十年',
    intro='登記記録や図面の保存期間と、登記事項証明書の交付、附属書類の閲覧について問う問題です（不動産登記法119条・121条、不動産登記規則28条）。\n\nこの記事では、「閉鎖したあとも永久に残るもの」と「閉鎖すると期間が決まるもの」を中心に、具体的な場面で確認していきましょう。',
    sections={
        'ア': ('地図に準ずる図面は、閉鎖したものも永久に保存される',
               '地図及び地図に準ずる図面は、閉鎖したものを含めて、保存期間が永久です（不動産登記規則28条2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、ある地域の地図に準ずる図面が閉鎖されたとしても、その図面は、閉鎖したあとも廃棄されずに、永久に保存されます。'),
        'イ': ('建物の閉鎖登記記録は、閉鎖した日から30年間',
               '閉鎖した登記記録の保存期間は、土地と建物で違います。土地に関する閉鎖登記記録は、閉鎖した日から50年間です。建物に関する閉鎖登記記録は、閉鎖した日から30年間です（不動産登記規則28条4号・5号）。\n\n甲建物の閉鎖登記記録の保存期間は30年間なので、50年間としている本肢は誤りです。\n\n**たとえば**、土地の滅失の登記で登記記録を閉鎖したなら50年間、建物の滅失の登記で登記記録を閉鎖したなら30年間、保存されます。'),
        'ウ': ('登記を申請した人は、正当な理由がなくても附属書類を閲覧できる',
               '登記簿の附属書類（図面を除く）の閲覧は、だれでも、正当な理由があるときに請求できます（不動産登記法121条3項）。\n\nただし、登記を申請した人は、この規定にかかわらず、自己を申請人とする登記記録に係る附属書類の閲覧を請求できます（同条4項）。Aは、自分が申請した分筆の登記の附属書類なので、本肢は誤りです。\n\n**たとえば**、Aさんが自分で申請した分筆の登記の申請書や添付書類の内容を、あとで確かめたいとき、Aさんは、正当な理由を示さなくても、閲覧を請求できます。'),
        'エ': ('地積測量図は、閉鎖すると閉鎖した日から30年間になる',
               '土地所在図、地積測量図、建物図面及び各階平面図は、保存期間が永久です。ただし、閉鎖したものは、閉鎖した日から30年間です（不動産登記規則28条13号）。\n\n問題文は、閉鎖された後も永久に保存されるとしているので、本肢は誤りです。\n\n**たとえば**、乙土地の分筆の登記のときに提出された地積測量図は、閉鎖されるまでは永久に保存されます。しかし、閉鎖されると、閉鎖した日から30年間の保存になります。'),
        'オ': ('だれでも、他の登記所に登記事項証明書を請求できる',
               '何人も、手数料を納付して、登記事項証明書の交付を請求できます（不動産登記法119条1項）。この請求は、法務省令で定める場合を除き、不動産の所在地を管轄する登記所以外の登記所の登記官に対してもできます（同条5項）。\n\n本肢は正しいといえます。\n\n**たとえば**、隣の土地の様子を知りたい人が、利害関係がなくても、手数料を納めて、その土地の登記事項証明書の交付を請求できます。原則として、近くの登記所にも請求できます。'),
    },
    summary=[
        ('ア', '正', '地図及び地図に準ずる図面は、閉鎖したものも永久に保存される'),
        ('イ', '誤', '建物に関する閉鎖登記記録は、閉鎖した日から30年間（50年間は土地）'),
        ('ウ', '誤', '登記を申請した人は、正当な理由がなくても、自己を申請人とする登記の附属書類を閲覧できる'),
        ('エ', '誤', '地積測量図は永久保存だが、閉鎖したものは閉鎖した日から30年間'),
        ('オ', '正', '登記事項証明書は、だれでも、他の登記所の登記官にも請求できる'),
    ],
    summary_tail='イは「土地と建物」、エは「地図と地積測量図」を取り違えた出題です。閉鎖すると期間が決まるものと、閉鎖しても永久のものを、分けて覚えましょう。',
    supplements=[
        '### 補足説明（ア・エ）：閉鎖したあとの図面の保存期間\n\n同じ図面でも、閉鎖したあとの保存期間が違います（不動産登記規則28条）。\n\n- 地図及び地図に準ずる図面：閉鎖前も閉鎖後も、永久。\n- 地積測量図、建物図面など：閉鎖前は永久、閉鎖すると閉鎖した日から30年間。\n\n**たとえば**、地図に準ずる図面が閉鎖されても、永久に残ります。一方、分筆のときの地積測量図が閉鎖されると、閉鎖した日から30年で保存期間が終わります。',
        '### 補足説明（イ）：閉鎖登記記録は、土地と建物で期間が違う\n\n閉鎖した登記記録の保存期間は、土地と建物で違います（不動産登記規則28条4号・5号）。\n\n- 土地に関する閉鎖登記記録：閉鎖した日から50年間。\n- 建物に関する閉鎖登記記録：閉鎖した日から30年間。\n\n**たとえば**、土地の滅失で閉鎖された記録は50年、取り壊した建物の滅失で閉鎖された記録は30年、保存されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第102日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法119条1項・5項、121条3項・4項、不動産登記規則28条2号・4号・5号・13号は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「原則として、近くの登記所にも請求できる」は、119条5項の「法務省令で定める場合を除き」からの一般的な整理で、除外される場合の具体的な内容は確認していません。',
        '具体例の人物と場面は、理解のために設けた架空の例です。条文にない事実は断定していません。',
    ],
    phrases=['地図に準ずる図面は閉鎖しても永久です', '建物の閉鎖登記記録は三十年間です', '申請した人は附属書類を閲覧できます', '地積測量図は閉鎖すると三十年間です', '登記事項証明書はだれでも請求できます'],
    header=dict(t1='登記の記録は、', t2='いつまで残る？', topic='不動産登記規則　保存期間', kanji=''),
    poster_intro='登記記録等の公開と保存期間を、「保存期間（登記記録と地図）」（グループA：ア・イ）と「閲覧・図面・証明書」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='登記記録の保存と公開を整理', sub='不動産登記規則 第28条と不動産登記法 第119条と第121条（毎日ドリル 第102日）',
        col_a='登記記録と地図の保存', col_b='閲覧と図面と証明書', n_a=2,
        cards=[
            dict(h='地図に準ずる図面は閉鎖しても永久保存',
                 ill='a map sheet with a round stamp labeled 「閉鎖」 placed inside an archive shelf, with a long ribbon labeled 「永久」 wrapped around it. A green check mark sits beside the ribbon.',
                 words=['閉鎖', '永久'], tag='閉鎖後も永久'),
            dict(h='建物の閉鎖登記記録は三十年間',
                 ill='a record sheet of a demolished building placed on an archive shelf, with a calendar page labeled 「三十年」 beside it. A green check mark sits beside the calendar.',
                 words=['三十年'], tag='閉鎖した日から数える'),
            dict(h='申請した人は附属書類を閲覧できる',
                 ill='an applicant figure holding a folder labeled 「附属書類」 and looking at its pages at a counter. A green check mark sits beside the folder.',
                 words=['附属書類'], tag='正当な理由は不要'),
            dict(h='地積測量図は閉鎖後に三十年間',
                 ill='a survey drawing sheet with a round stamp labeled 「閉鎖」 and a calendar page labeled 「三十年」 beside it. A tag on the drawing is labeled 「地積測量図」. A green check mark sits beside the calendar.',
                 words=['閉鎖', '三十年', '地積測量図'], tag='閉鎖後は三十年間'),
            dict(h='だれでも登記事項証明書を請求できる',
                 ill='a person figure at a registry office counter holding a certificate sheet labeled 「登記事項証明書」, with a second registry office building in the background. A green check mark sits beside the certificate.',
                 words=['登記事項証明書'], tag='他の登記所にも請求'),
        ],
        kanji=[]),
    nb_label='ア・エ・イ肢', nb_intro='ア・エ・イの補足説明に合わせた2枚です。1枚目は、図面の保存期間が閉鎖の前後でどう違うかを表で整理します。2枚目は、土地と建物の閉鎖登記記録の保存期間を左右の対比で示します。',
    notebooks=[
        dict(name='閉鎖したあとの図面の保存期間', args=dict(
            title='図面の保存期間は？', sub='閉鎖の前と後（毎日ドリル 第102日 ア・エ）',
            req='a two-row table',
            layout="""--- TABLE ---
Render as a clean flat-design table with three columns and two data rows under a header row. Use exactly these strings, and no others. Do not use any check mark or cross mark.
Header row: 図面 | 閉鎖する前 | 閉鎖したあと
Row 1: 地図と地図に準ずる図面 | 永久 | 永久
Row 2: 地積測量図や建物図面など | 永久 | 閉鎖した日から三十年間
Next to each row, draw a small icon: row 1 shows a map sheet, row 2 shows a survey drawing with a calendar page.""",
            callout='地図と地図に準ずる図面は、閉鎖したあとも永久に保存されます。\n地積測量図などは、閉鎖すると、閉鎖した日から三十年間の保存になります。',
            footer='不動産登記規則28条2号・13号', kanji=[], what='table',
            check='confirm the table has exactly three columns and two data rows with the given strings, ')),
        dict(name='土地と建物の閉鎖登記記録', args=dict(
            title='閉鎖した登記記録の保存期間', sub='土地と建物の違い（毎日ドリル 第102日 イ）',
            req='a side-by-side comparison',
            layout="""IMPORTANT: the two panel headers differ by one word, 「土地」 on the left and 「建物」 on the right; they are NOT the same string. Draw 「土地」 and 「建物」 large and in different accent colors (green on the left, blue on the right) so they can never be confused or duplicated. Do not use any check mark or cross mark in this image.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (green accent):
Panel header: 土地の閉鎖登記記録
Scene: an isometric land plot with a closed record sheet and a calendar page.
Label under the scene: 閉鎖した日から五十年間

RIGHT PANEL (blue accent):
Panel header: 建物の閉鎖登記記録
Scene: an isometric house with a closed record sheet and a calendar page.
Label under the scene: 閉鎖した日から三十年間
Use exactly these strings, and no others, for the labels.""",
            callout='閉鎖した登記記録の保存期間は、土地と建物で違います。\n土地は閉鎖した日から五十年間、建物は閉鎖した日から三十年間です。',
            footer='不動産登記規則28条4号・5号', kanji=[], what='panels',
            check='confirm the two panel headers are different strings (土地の閉鎖登記記録 on the left and 建物の閉鎖登記記録 on the right) drawn in different accent colors, ')),
    ],
)

_p = D['poster']
_p['kanji'] = kj(_p['title'], _p['sub'], _p['col_a'], _p['col_b'], *[c['h'] + c['tag'] + ''.join(c['words']) for c in _p['cards']])
D['header']['kanji'] = '・'.join(kj(D['header']['t1'], D['header']['t2'], D['header']['topic']))
for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = kj(_a['title'], _a['sub'], _a['callout'], _a['footer'])
