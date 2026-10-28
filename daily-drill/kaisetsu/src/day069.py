def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='附属建物にできる', t2='条件は何？', topic='不動産登記法　附属建物')
_PT = '附属建物の取扱いを整理'
_PS = '建物の表題登記と変更登記（毎日ドリル 第69日）'

_cards = [
    dict(h='効用上一体でなければ附属建物にできない',
         ill='an isometric house and a separate storehouse placed apart with a dotted gap between them. A tag labeled 「効用上一体」 sits between them with a green outline. A green check mark sits beside the tag.',
         words=['効用上一体'], tag='一体性が要件'),
    dict(h='主である建物だけ取り壊したら変更登記',
         ill='an isometric house with its main building half demolished and a small shed remaining intact. A form labeled 「主たる建物に変更」 sits beside the shed. A green check mark sits beside the form.',
         words=['主たる建物に変更'], tag='附属建物が主になる'),
    dict(h='附属建物の新築には所有権の証明も必要',
         ill='a house with a newly built garage beside it. A drawing sheet labeled 「建物図面」 and a certificate labeled 「所有権」 are shown next to each other. A green check mark sits beside the two papers.',
         words=['建物図面', '所有権'], tag='図面と所有権の証明'),
    dict(h='同日の新築なら附属建物の日付は不要',
         ill='a calendar page with one circled date, and a house and a storehouse both pointing to the same circled date. A green check mark sits beside the calendar.',
         words=[], tag='日付は主と同じ'),
    dict(h='先取特権の保存後は遅滞なく変更登記',
         ill='a house with a storehouse under construction beside it, and a stamp labeled 「先取特権」 on a record sheet. A stopwatch labeled 「遅滞なく」 sits beside the sheet. A green check mark sits beside the stopwatch.',
         words=['先取特権', '遅滞なく'], tag='一月ではなく遅滞なく'),
]

_nb1_layout = """--- COMPARISON ---
Render as a clean flat-design two-panel comparison, left and right, same height, connected by a small arrow with no text between the panels.

LEFT PANEL (blue accent):
Panel header: 主である建物と附属建物
Scene: an isometric house labeled 居宅（主である建物） and a small shed labeled 物置（附属建物） beside it.

RIGHT PANEL (green accent):
Panel header: 居宅だけを取り壊したとき
Scene: the house shown as demolished and drawn in faded gray, while the shed remains intact and highlighted in green with the label 物置が主である建物に変わる.
Below the scene, a small tag: 表題部の変更の登記

Use exactly these strings, and no others."""

_nb2_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and three data rows.

Header row: 変更の場面 | 添付情報

Row 1 (blue accent): 附属建物を新築したとき | 変更後の建物図面、変更後の各階平面図、附属建物の所有権を証する情報
Row 2 (gray accent): 床面積を変更したとき | 変更後の建物図面、変更後の各階平面図
Row 3 (gray accent): 建物の所在や地番を変更したとき | 変更後の建物図面

IMPORTANT: Row 1 is highlighted in blue and carries the extra item 附属建物の所有権を証する情報; rows 2 and 3 do not carry this item. Draw the extra item in blue so it is clearly distinct from the other cells.
Use exactly these strings, and no others."""

D = dict(
    catch='附属建物は、効用上の一体性がカギ',
    intro='附属建物について、どんなときに附属建物にできるのか、主である建物がなくなったらどうなるのか、新築したときに何を提供するのかを問う問題です（不動産登記法2条・87条、不動産登記事務取扱手続準則78条・102条、不動産登記令別表）。\n\nこの記事では、附属建物の基本的な取扱いを、具体的な場面で確認します。この問題は、誤っているものを選ぶ形式です。',
    sections={
        'ア': ('効用上一体でなければ、附属建物にできない',
               '附属建物は、表題登記がある建物に附属する建物で、その建物と一体のものとして一個の建物として登記されるものです（不動産登記法2条23号）。効用上一体として利用される状態にある数棟の建物は、所有者の意思に反しない限り、1個の建物として取り扱います（準則78条1項）。\n\n効用上一体として利用される状態にない倉庫を、附属建物とすることはできません。本肢は正しいといえます。\n\n**たとえば**、Aの居宅の近くに、Aの倉庫が建っていても、居宅と一体として使われていなければ、倉庫を附属建物とする登記はできません。同じ所有者で近くにあるというだけでは足りません。'),
        'イ': ('主である建物だけを取り壊したら、変更の登記',
               '附属建物がある主たる建物が滅失したときは、登記を抹消するのではなく、表題部の変更の登記をします。\n\nこの登記では、滅失の原因を記録したうえで、主たる建物となる附属建物の種類・構造・床面積を記録し、「主たる建物に変更」と記録します（準則102条）。\n\n問題文は、表題部の登記の抹消を申請しなければならないとしているので、本肢は誤りです。\n\n**たとえば**、居宅と物置からなる建物で、居宅だけを取り壊したとします。物置が残っているので、建物全体の登記は残ります。物置が主である建物に変わる、という変更の登記をします。'),
        'ウ': ('附属建物の新築では、所有権を証する情報も必要',
               '附属建物を新築して表題部の変更の登記を申請するときは、変更後の建物図面と各階平面図に加えて、附属建物について所有権を有することを証する情報を提供しなければなりません（不動産登記令別表十四の項添付情報欄ハ）。\n\n問題文は、所有権を証する情報の提供を要しないとしているので、本肢は誤りです。\n\n**たとえば**、Aが居宅の隣に車庫を新築し、附属建物として登記するとします。図面を提供するだけでは足りず、その車庫がAの所有であることを証する情報も、あわせて提供します。'),
        'エ': ('同じ日に新築なら、附属建物の新築の日は書かなくてよい',
               '居宅と物置を同じ日に新築して、物置を附属建物とする表題登記を申請するときは、附属建物の新築の日を、申請情報の内容とすることを要しません。附属建物の新築の日が、主である建物の新築の日と同じだからです。本肢は正しいといえます。\n\n**たとえば**、Aが居宅と物置を同じ日に建てた場合は、物置について、別に新築の日を書く必要はありません。新築の日が主である建物と違うときは、附属建物について新築の日を書きます。'),
        'オ': ('先取特権の保存後は、遅滞なく変更の登記をする',
               '附属建物を新築するため、不動産工事の先取特権の保存の登記がされた後、その附属建物の建築が完了したときは、その建物の所有権の登記名義人は、遅滞なく、附属建物の新築による建物の表題部の変更の登記を申請しなければなりません（不動産登記法87条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、増築中の附属建物について先取特権の保存の登記をしていた場合、建物が完成したら、通常の一月以内よりも急いで、変更の登記を申請します。'),
    },
    summary=[
        ('ア', '正', '効用上一体として利用される状態にない建物は、附属建物にできない'),
        ('イ', '誤', '主である建物だけを取り壊したときは、抹消ではなく、表題部の変更の登記をする'),
        ('ウ', '誤', '附属建物の新築では、図面のほか、附属建物の所有権を証する情報も提供する'),
        ('エ', '正', '同じ日に新築した附属建物は、新築の日を申請情報の内容とすることを要しない'),
        ('オ', '正', '先取特権の保存の登記後に附属建物の建築が完了したときは、遅滞なく変更の登記を申請する'),
    ],
    summary_tail='イは「抹消」と「変更」の取り違え、ウは「所有権を証する情報」の見落としです。附属建物が残るなら登記は残る、新築なら所有権の証明が必要、と押さえましょう。',
    supplements=[
        '### 補足説明（イ）：主である建物が滅失したとき\n\n主である建物だけがなくなったときの取扱いを、全部が滅失した場合と比べて整理します（準則102条）。\n\n| 場面 | 登記 |\n|---|---|\n| 主である建物だけが滅失（附属建物が残る） | 表題部の変更の登記（附属建物が主である建物になる） |\n| 建物全体が滅失 | 表題部の登記の抹消 |\n\n**たとえば**、居宅と物置のうち居宅だけを取り壊したときは、物置が残るので、登記記録は残ります。居宅も物置も取り壊したときは、建物がなくなるので、登記は抹消されます。',
        '### 補足説明（ウ）：変更の登記で提供する情報\n\n建物の表題部の変更の登記では、変更の内容によって、提供する情報が変わります（不動産登記令別表十四の項添付情報欄）。\n\n| 変更の場面 | 添付情報 |\n|---|---|\n| 附属建物を新築したとき | 変更後の建物図面と各階平面図、附属建物の所有権を証する情報 |\n| 床面積を変更したとき | 変更後の建物図面と各階平面図（増加するときは、増加した部分の所有権を証する情報も） |\n| 建物の所在や地番を変更したとき | 変更後の建物図面 |\n\n**たとえば**、居宅の隣に車庫を新築したときは、図面に加えて、車庫の所有権を証する情報が要ります。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第69日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法2条23号、87条2項、不動産登記令別表十四の項、不動産登記事務取扱手続準則78条1項・102条は、`note-articles/laws/` 配下の原文で確認しました。',
        'エの結論（附属建物の新築の日が主である建物と同じなら、新築の日を申請情報の内容とすることを要しない）は、登記実務の取扱いによるもので、手元の法令の原文では確認できていません（原文は未確認）。',
        'アの結論は、2条23号と準則78条1項から導いた整理で、効用上一体でない建物を附属建物にできないことを直接定めた条文の文言は確認していません。',
    ],
    phrases=['効用上一体でなければ附属建物にできません', '主である建物だけ壊したら変更登記です', '新築した附属建物は所有権の証明も要ります', '同じ日に建てたら新築の日は省けます', '先取特権の後は遅滞なく変更登記です'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='附属建物の取扱いを、「附属建物の要件と滅失」（グループA：ア・イ）と「新築と申請の期限」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='附属建物の要件と滅失', col_b='新築と申請の期限', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '附属建物の要件と滅失新築と申請の期限', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='イ・ウ肢', nb_intro='イ・ウの補足説明に合わせた2枚です。1枚目は、主である建物だけを取り壊したときの取扱いを示します。2枚目は、変更の登記の場面ごとの添付情報を表で示します。',
    notebooks=[
        dict(name='主である建物だけを取り壊したとき', args=dict(
            title='居宅だけ壊したら、どうなる？', sub='主である建物の滅失（毎日ドリル 第69日 イ）',
            req='a diagram',
            layout=_nb1_layout,
            callout='主である建物だけが滅失しても、附属建物が残るので、登記は抹消しません。\n附属建物が主である建物になる、表題部の変更の登記をします。',
            footer='不動産登記事務取扱手続準則102条',
            kanji=K('居宅だけ壊したらどうなる主である建物の滅失附属建物物置取り壊したとき表題部の変更の登記不動産登記事務取扱手続準則'), what='panels',
            check='confirm there are exactly two panels connected by one small arrow with no text, ')),
        dict(name='変更の登記で提供する情報', args=dict(
            title='変更の登記で、何を提供する？', sub='建物の表題部の変更の登記（毎日ドリル 第69日 ウ）',
            req='a table',
            layout=_nb2_layout,
            callout='附属建物を新築したときは、図面のほかに、附属建物の所有権を証する情報も提供します。\n図面だけでは足りません。',
            footer='不動産登記令別表十四の項添付情報欄',
            kanji=K('変更の登記で何を提供する建物の表題部附属建物新築床面積所在地番建物図面各階平面図所有権証する情報不動産登記令'), what='table',
            check='confirm that only row 1 carries the extra item 附属建物の所有権を証する情報, drawn in blue, ')),
    ],
)
