def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='筆界特定を申請', t2='できるのは誰？', topic='不動産登記法　筆界特定')
_PT = '筆界特定の手続を整理'
_PS = '不動産登記法（毎日ドリル 第72日）'

_cards = [
    dict(h='相続登記前の相続人も申請できる',
         ill='an heir figure holding a form beside two neighboring land plots with a dotted boundary line. A faded outline of the former owner stands behind the heir, labeled 「相続」. A green check mark sits beside the heir.',
         words=['相続'], tag='一般承継人も含む'),
    dict(h='抵当権者は申請できない',
         ill='two neighboring land plots with a dotted boundary line. A bank figure with a name tag labeled 「抵当権者」 stands outside, drawn in faded gray, while an owner figure holds a form. No check mark and no cross mark on this card.',
         words=['抵当権者'], tag='申請人は所有者側'),
    dict(h='委員の質問には登記官の許可が必要',
         ill='a hearing scene with a registrar figure at the center and a survey committee figure beside the registrar. A permission slip labeled 「許可」 passes from the registrar to the committee figure. A green check mark sits beside the slip.',
         words=['許可'], tag='質問の前に許可'),
    dict(h='所有権の確認判決は却下事由にならない',
         ill='a courthouse building with a scroll labeled 「所有権確認」 beside a pair of neighboring plots. A form labeled 「筆界特定」 sits in front. A green check mark sits beside the form.',
         words=['所有権確認', '筆界特定'], tag='筆界確定訴訟だけ'),
    dict(h='申請人が一人ずつなら費用は等しく負担',
         ill='two neighboring owner figures each holding a coin, placing coins on the two sides of a balance scale that is level. A label on the scale reads 「等しい割合」. A green check mark sits beside the scale.',
         words=['等しい割合'], tag='一人ずつなら半分ずつ'),
]

_nb1_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and four data rows, with a small icon at the start of each row.

Header row: 土地の状態 | 筆界特定を申請できる人

Row 1 (blue accent): 所有権の登記がある | 所有権の登記名義人
Row 2 (blue accent): 所有権の登記がない | 表題部所有者
Row 3 (blue accent): 表題登記がない | 所有者
Row 4 (green accent): 上の人が亡くなっている | 相続人その他の一般承継人

Below the table, a small gray note with an icon of a mortgage document and the label: 抵当権者は含まれない
Use exactly these strings, and no others."""

_nb2_layout = """IMPORTANT: the two sides must show OPPOSITE results. The left side shows the case where the application is rejected, with a red cross; the right side shows the case where it is not rejected, with a green check mark. The two panel headers are different strings: 「筆界確定訴訟の判決が確定」 on the left and 「所有権確認訴訟の判決が確定」 on the right; draw them in different accent colors (orange and blue) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (orange accent):
Panel header: 筆界確定訴訟の判決が確定
Scene: a courthouse with a scroll, and two neighboring land plots with a dotted boundary line.
Result badge with a red cross: 筆界特定の申請は却下される

RIGHT PANEL (blue accent):
Panel header: 所有権確認訴訟の判決が確定
Scene: a courthouse with a scroll, and one land plot with a shaded area marked as owned.
Result badge with a green check mark: 却下されない"""

D = dict(
    catch='筆界特定の申請人は所有者とその承継人',
    intro='筆界特定の手続について、だれが申請できるのか、どんなときに申請が却下されるのか、費用はだれが負担するのかを問う問題です（不動産登記法123条・131条・132条・140条・146条）。\n\nこの記事では、筆界特定の申請人の範囲と、手続の細かな決まりを、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('相続の登記をしていない相続人も、申請できる',
               '土地の所有権登記名義人等は、筆界特定の申請をすることができます（不動産登記法131条1項）。所有権登記名義人等には、所有権の登記名義人又は表題部所有者の相続人その他の一般承継人も含まれます（同法123条5号）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の所有者Aが亡くなり、相続人のBが甲土地を相続したとします。相続による所有権の移転の登記をまだしていなくても、Bは、甲土地と乙土地との筆界について、筆界特定の申請をすることができます。'),
        'イ': ('抵当権者は、筆界特定を申請できない',
               '筆界特定の申請ができるのは、土地の所有権登記名義人等です（不動産登記法131条1項）。所有権登記名義人等は、所有権の登記名義人、表題部所有者、表題登記がない土地の所有者とその一般承継人で、抵当権者は含まれません（同法123条5号）。\n\n問題文は、抵当権者Cも申請できるとしているので、本肢は誤りです。\n\n**たとえば**、甲土地に抵当権の設定の登記を受けた銀行は、甲土地と乙土地との筆界が気になっても、自分では筆界特定の申請をすることができません。'),
        'ウ': ('筆界調査委員が質問するには、登記官の許可が必要',
               '筆界特定の意見聴取等の期日には、筆界調査委員が立ち会います。筆界調査委員が、申請人、関係人又は参考人に質問するときは、筆界特定登記官の許可を得なければなりません（不動産登記法140条3項）。\n\n問題文は、許可を得ることなく質問を発することができるとしているので、本肢は誤りです。\n\n**たとえば**、期日に立ち会った筆界調査委員が、申請人に事情を尋ねたいときは、まず筆界特定登記官の許可を得てから質問をします。'),
        'エ': ('所有権確認の判決は、筆界特定の却下事由ではない',
               '筆界特定の申請が却下されるのは、対象土地の筆界について、既に民事訴訟の手続により筆界の確定を求める訴えに係る判決が確定しているときです（不動産登記法132条1項6号）。\n\n所有権の範囲を争う所有権確認の訴えの判決は、これに当たりません。問題文は、却下されるとしているので、本肢は誤りです。\n\n**たとえば**、Aが「この範囲は自分の土地だ」と求めた所有権確認の訴えで勝訴しても、筆界を確定する判決ではありません。そのため、Aは、その後に筆界特定の申請をすることができます。'),
        'オ': ('申請人が両側から一人ずつなら、費用は等しい割合で負担する',
               '筆界特定の手続の費用は、申請人の負担です（不動産登記法146条1項）。申請人が二人あり、その一人が一方の土地の所有権登記名義人等、もう一人が他方の土地の所有権登記名義人等であるときは、等しい割合で手続費用を負担します（同条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地の所有者Aと、乙土地の所有者Bが共同で申請したとします。AとBは、手続費用を半分ずつ負担します。'),
    },
    summary=[
        ('ア', '正', '相続の登記をしていない相続人も、一般承継人として筆界特定を申請できる'),
        ('イ', '誤', '抵当権者は、筆界特定の申請ができる所有権登記名義人等に含まれない'),
        ('ウ', '誤', '筆界調査委員が質問するには、筆界特定登記官の許可が必要'),
        ('エ', '誤', '却下事由になるのは筆界確定訴訟の判決の確定で、所有権確認の判決は当たらない'),
        ('オ', '正', '申請人が両側の土地から一人ずつなら、手続費用は等しい割合で負担する'),
    ],
    summary_tail='イは申請人の範囲、ウは「許可」の有無、エは判決の種類をすり替えた出題です。筆界特定は筆界の手続だと押さえると、エの結論が見えてきます。',
    supplements=[
        '### 補足説明（イ）：筆界特定を申請できる人\n\n筆界特定を申請できるのは、土地の所有権登記名義人等です（不動産登記法131条1項、123条5号）。土地の状態によって、だれが当たるのかを整理します。\n\n| 土地の状態 | 申請できる人 |\n|---|---|\n| 所有権の登記がある | 所有権の登記名義人 |\n| 所有権の登記がない | 表題部所有者 |\n| 表題登記がない | 所有者 |\n\nこれらの人の相続人その他の一般承継人も含まれます。\n\n**たとえば**、抵当権者や、土地を借りている人は、この表のどれにも当たらないので、申請人にはなれません。',
        '### 補足説明（エ）：筆界特定の申請が却下される判決\n\n筆界特定の申請の却下事由のひとつは、対象土地の筆界について、筆界の確定を求める訴えの判決が、既に確定していることです（不動産登記法132条1項6号）。\n\n| 確定した判決 | 筆界特定の申請 |\n|---|---|\n| 筆界の確定を求める訴え（筆界確定訴訟） | 却下される |\n| 所有権の範囲を争う訴え（所有権確認の訴え） | 却下されない |\n\n**たとえば**、隣の土地との筆界を裁判所に定めてもらった後に、同じ筆界について改めて筆界特定を申請しても、却下されます。一方、所有権の範囲が争われた判決が確定しても、筆界特定の申請は妨げられません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第72日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法123条5号、131条1項、132条1項6号、140条3項、146条1項・2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの「所有権の範囲を争う訴えの判決は筆界を確定するものではない」という説明は、132条1項6号の文言（筆界の確定を求める訴え）から導いた一般的な整理です。',
        '補足説明（イ）の「土地を借りている人は含まれない」は、123条5号が申請人を所有権登記名義人等に限っていることからの整理で、個別の先例の確認はしていません。',
    ],
    phrases=['相続の登記前でも相続人は申請できます', '抵当権者は申請人になれません', '委員が質問するには許可が要ります', '所有権の判決では却下されません', '両側から一人ずつなら費用は半分ずつです'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='筆界特定の手続を、「申請人」（グループA：ア・イ）と「手続の進行と費用」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='申請人', col_b='手続の進行と費用', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '申請人手続の進行と費用', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='イ・エ肢', nb_intro='イ・エの補足説明に合わせた2枚です。1枚目は、筆界特定を申請できる人を土地の状態ごとに表で示します。2枚目は、却下される判決とされない判決を左右の対比で示します。',
    notebooks=[
        dict(name='筆界特定を申請できる人', args=dict(
            title='筆界特定を申請できるのは？', sub='所有権登記名義人等（毎日ドリル 第72日 イ）',
            req='a table',
            layout=_nb1_layout,
            callout='筆界特定を申請できるのは、土地の所有権登記名義人等です。\n抵当権者は含まれません。所有権の登記名義人などの相続人その他の一般承継人は含まれます。',
            footer='不動産登記法123条5号、131条1項',
            kanji=K('筆界特定を申請できるのは土地の状態所有権の登記名義人表題部所有者所有者相続人その他の一般承継人抵当権者含まれない不動産登記法'), what='table',
            check='confirm there are exactly four data rows plus a gray note below the table, ')),
        dict(name='筆界特定が却下される判決', args=dict(
            title='筆界特定が却下されるのは？', sub='筆界確定訴訟と所有権確認訴訟（毎日ドリル 第72日 エ）',
            req='a side-by-side comparison',
            layout=_nb2_layout,
            callout='筆界特定が却下されるのは、筆界の確定を求める訴えの判決が確定しているときです。\n所有権の範囲を争う所有権確認の訴えの判決は、却下事由に当たりません。',
            footer='不動産登記法132条1項6号',
            kanji=K('筆界特定が却下されるのは筆界確定訴訟所有権確認訴訟判決確定申請対象土地不動産登記法'), what='panels',
            check='confirm the two panel headers are different strings (筆界確定訴訟の判決が確定 on the left and 所有権確認訴訟の判決が確定 on the right) and that the left badge shows a red cross while the right badge shows a green check mark, ')),
    ],
)

for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = K(_a['title'], _a['sub'], _a['layout'], _a['callout'], _a['footer'])
