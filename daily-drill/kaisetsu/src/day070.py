def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='建物が合体したら、', t2='登記はどうなる？', topic='不動産登記法　建物の合体')
_PT = '建物の合体による登記等を整理'
_PS = '合体した建物の登記（毎日ドリル 第70日）'

_cards = [
    dict(h='所有権の登記がある建物は、表題部所有者を書かない',
         ill='two isometric buildings merging into one building. A record sheet beside the merged building has an empty line labeled 「表題部所有者」 drawn in faded gray, and a filled line labeled 「所有権の登記」. A green check mark sits beside the filled line.',
         words=['表題部所有者', '所有権の登記'], tag='甲区に所有権の登記'),
    dict(h='消滅を承諾した抵当権は付記登記で消す',
         ill='a bank figure handing a signed consent paper to a registrar figure. A record sheet beside them shows a small side-note line labeled 「付記登記」 attached to a mortgage line labeled 「抵当権」. A green check mark sits beside the side-note line.',
         words=['付記登記', '抵当権'], tag='合体後に移記しない'),
    dict(h='表題登記のない建物の所有者も名義人にする',
         ill='two buildings merging into one. Two owner figures stand beside the merged building: one holding a title paper and one with a name tag labeled 「所有者」. The merged building has a stamp labeled 「所有権の登記」. A green check mark sits beside the stamp.',
         words=['所有者', '所有権の登記'], tag='併せて申請'),
    dict(h='主と附属の合体は表題部の変更',
         ill='a main building and a small shed joined by a new passage into one building, drawn on a single record sheet labeled 「表題部」. A stamp labeled 「変更」 sits beside the sheet. A green check mark sits beside the stamp.',
         words=['表題部', '変更'], tag='合体による登記等ではない'),
    dict(h='存続登記は抵当権なら乙区へ移す',
         ill='two record sheets side by side with an arrow from the left to the right. The left sheet shows a mortgage line labeled 「抵当権」 and the right sheet shows the same line placed in the lower section labeled 「乙区」. A green check mark sits beside the right sheet.',
         words=['抵当権', '乙区'], tag='相当区に移記'),
]

_nb1_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and two data rows.

Header row: 合体前の建物 | 合体による登記等と併せて申請する所有権の登記

Row 1 (blue accent): 表題登記がない建物と、所有権の登記がある建物 | 表題登記がない建物の所有者を登記名義人とする所有権の登記
Row 2 (green accent): 表題登記がある建物と、所有権の登記がある建物 | 表題登記がある建物の表題部所有者を登記名義人とする所有権の登記

IMPORTANT: the two rows end with different strings: 表題登記がない建物の所有者を登記名義人とする所有権の登記 and 表題登記がある建物の表題部所有者を登記名義人とする所有権の登記. Draw them in different accent colors (blue and green) so they can never be confused or duplicated.
Use exactly these strings, and no others."""

_nb2_layout = """IMPORTANT: the two sides must show OPPOSITE results. The left side shows a mortgage that is moved to the merged building; the right side shows a mortgage that is not moved. The left badge carries a green check mark and the right badge carries a red cross. The two panel headers are different strings: 「存続登記」 on the left and 「消滅の承諾あり」 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 存続登記
Scene: a record sheet of the pre-merger building with a mortgage line, an arrow leading to the merged building's record sheet, where the line sits in the lower section labeled 乙区.
Result badge with a green check mark: 乙区に移記する

RIGHT PANEL (orange accent):
Panel header: 消滅の承諾あり
Scene: a record sheet with a mortgage line and a small side-note line attached below it, labeled 消滅した旨を付記登記で記録する. No arrow leads to the merged building's record sheet.
Result badge with a red cross: 合体後の建物に移記しない"""

D = dict(
    catch='合体の登記は、所有権の有無で変わる',
    intro='二以上の建物が合体して一個の建物になったときの登記を問う問題です（不動産登記法49条・50条、不動産登記規則120条、不動産登記事務取扱手続準則95条）。\n\nこの記事では、合体前の建物に所有権の登記があるかどうかで、申請の内容と登記記録の記録の仕方がどう変わるかを、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('所有権の登記があるときは、表題部所有者を記録しない',
               '合体後の建物の表題登記をする場合、合体前の建物に所有権の登記がある建物があるときは、合体後の建物の登記記録の表題部に、表題部所有者に関する登記事項を記録することを要しません（不動産登記規則120条1項）。\n\nこの場合は、合体後の建物の甲区に、合体による所有権の登記をする旨や、所有権の登記名義人などを記録します（同条2項）。\n\n問題文は、表題部所有者としてAが記録されるとしているので、本肢は誤りです。\n\n**たとえば**、Aが所有権の登記がある甲建物と、表題登記だけがある乙建物（表題部所有者もA）を合体させたとします。合体後の建物の表題部には表題部所有者を記録せず、甲区に、Aを所有権の登記名義人とする、合体による所有権の登記をします。'),
        'イ': ('消滅を承諾した抵当権は、付記登記で消し、移記しない',
               '合体前の建物に抵当権の登記がある場合に、抵当権者が合体後の建物についてその抵当権を消滅させることを承諾したことを証する情報が、申請情報と併せて提供されたときは、権利が消滅した旨を登記します（不動産登記法50条、規則120条5項）。\n\nこの登記は付記登記でします。合体後の建物の登記記録に、その抵当権の登記を移記することは要しません（同条6項）。本肢は正しいといえます。\n\n**たとえば**、合体前の甲建物に銀行の抵当権があり、銀行が合体後の建物についてその抵当権が消えることを承諾したとします。この場合、その抵当権は合体後の建物には引き継がれず、消滅した旨だけが付記登記で記録されます。'),
        'ウ': ('表題登記がない建物の所有者を名義人とする所有権の登記も申請する',
               '表題登記がない建物と、所有権の登記がある建物が合体した場合は、合体による登記等を申請するときに、表題登記がない建物の所有者を登記名義人とする所有権の登記を、併せて申請しなければなりません（不動産登記法49条1項2号、同項後段）。\n\n問題文は、この所有権の登記を併せて申請することを要しないとしているので、本肢は誤りです。\n\n**たとえば**、表題登記がないAの甲建物と、Bが所有権の登記を受けている乙建物が合体したとします。Bが合体による登記等を申請するときも、Aを登記名義人とする所有権の登記を、併せて申請します。'),
        'エ': ('主たる建物と附属建物の合体は、表題部の変更の登記',
               '主たる建物と附属建物の合体による、建物の表題部の登記事項に関する変更の登記では、主たる建物の床面積の変更について、原因欄に、床面積欄の番号を冠記して「③令和何年何月何日附属建物合体」のように記録します。\n\n附属建物の表題部の抹消については、「令和何年何月何日主たる建物に合体」と記録します（準則95条）。\n\n本肢は正しいといえます。\n\n**たとえば**、一つの建物として登記されている母屋と物置の間を増築でつないで、一つの建物になったとします。この場合は、合体による登記等ではなく、表題部の変更の登記で、物置の表示を主たる建物に合体した旨を記録します。'),
        'オ': ('存続登記は、抵当権なら乙区に移記する',
               '合体前の建物に存続登記がある場合に、合体後の建物の持分について、その存続登記と同一の登記をするときは、登記官は、合体前の建物の登記記録から、合体後の建物の登記記録の権利部の「相当区」に、その存続登記を移記します（不動産登記規則120条4項）。\n\n抵当権の登記は、乙区に記録されるものです。問題文は、甲区に移記するとしているので、本肢は誤りです。\n\n**たとえば**、合体前の甲建物の抵当権が存続登記として残る場合、その抵当権は、合体後の建物の乙区に移されます。甲区は所有権に関する記録の場所なので、そこには移しません。'),
    },
    summary=[
        ('ア', '誤', '合体前に所有権の登記がある建物があるときは、合体後の建物の表題部に表題部所有者を記録しない'),
        ('イ', '正', '消滅を承諾した抵当権は、消滅した旨を付記登記で記録し、合体後の建物に移記しない'),
        ('ウ', '誤', '表題登記がない建物の所有者を名義人とする所有権の登記を、併せて申請する'),
        ('エ', '正', '主たる建物と附属建物の合体は、表題部の変更の登記で、③を冠記して記録する'),
        ('オ', '誤', '存続登記は、合体後の建物の登記記録の相当区に移記する。抵当権なら乙区'),
    ],
    summary_tail='アは表題部所有者の記録、ウは併せて申請する所有権の登記、オは移記する区の取り違えです。合体前の建物に所有権の登記があるかどうかが、すべての出発点になります。',
    supplements=[
        '### 補足説明（ア・ウ）：所有権の登記があると、どうなるか\n\n合体前の建物に所有権の登記がある建物が含まれるときは、合体後の建物について、所有権の登記が必要になります（不動産登記法49条1項、規則120条）。\n\n| 合体前の建物 | 併せて申請する所有権の登記 |\n|---|---|\n| 表題登記がない建物と、所有権の登記がある建物 | 表題登記がない建物の所有者を登記名義人とする所有権の登記 |\n| 表題登記がある建物と、所有権の登記がある建物 | 表題登記がある建物の表題部所有者を登記名義人とする所有権の登記 |\n\n**たとえば**、表題登記だけがある建物と、所有権の登記がある建物が合体したときは、表題部所有者だった人が登記名義人になる、所有権の登記を併せて申請します。合体後の建物の表題部には、表題部所有者を記録しません。',
        '### 補足説明（イ・オ）：合体前の抵当権の行き先\n\n合体前の建物に抵当権の登記があるとき、その行き先は、抵当権者の承諾があるかどうかで変わります（不動産登記法50条、規則120条4項から6項まで）。\n\n- 消滅の承諾がある場合：消滅した旨を付記登記で記録し、合体後の建物には移記しない。\n- 存続登記と同一の登記をする場合：合体後の建物の登記記録の相当区に移記する。抵当権なら乙区。\n\n**たとえば**、銀行が「合体後の建物では抵当権が消えてよい」と承諾すれば、抵当権は引き継がれません。一方、存続登記をするときは、抵当権が合体後の建物の乙区に移されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第70日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法49条1項、50条、不動産登記規則120条1項から6項まで、不動産登記事務取扱手続準則95条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「抵当権の登記は乙区に記録される」という説明は、権利部の構成についての条文からの一般的な整理で、120条4項の「相当区」を言い換えたものです。',
        '補足説明（ア・ウ）の表は、49条1項2号と4号の場合を取り上げたものです。3つ以上の建物が合体する場合（6号）は省いています。',
    ],
    phrases=['所有権の登記があれば表題部所有者は書きません', '消滅を承諾した抵当権は移記されません', '併せて所有権の登記も申請します', '主と附属の合体は表題部の変更です', '存続登記は乙区に移記します'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='建物の合体による登記等を、「合体後の記録と権利」（グループA：ア・イ）と「申請と移記」（グループB：ウ・エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='合体後の記録と権利', col_b='申請と移記', n_a=2,
        cards=_cards,
        kanji=K(_PT, _PS, '合体後の記録と権利申請と移記', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ア・ウ・イ・オ肢', nb_intro='ア・ウとイ・オの補足説明に合わせた2枚です。1枚目は、併せて申請する所有権の登記を表で示します。2枚目は、存続登記と消滅の承諾がある抵当権の行き先を左右の対比で示します。',
    notebooks=[
        dict(name='併せて申請する所有権の登記', args=dict(
            title='合体で、所有権の登記も申請する？', sub='合体前の建物と所有権の登記（毎日ドリル 第70日 ア・ウ）',
            req='a table',
            layout=_nb1_layout,
            callout='合体前の建物に所有権の登記がある建物が含まれるときは、合体による登記等と併せて、所有権の登記を申請します。\n合体後の建物の表題部には、表題部所有者を記録しません。',
            footer='不動産登記法49条1項、不動産登記規則120条1項',
            kanji=K('合体で所有権の登記も申請する合体前の建物表題登記がない所有者登記名義人表題部所有者併せて不動産登記法規則'), what='table',
            check='confirm that the two right-hand cells are different strings drawn in different colors (blue and green), ')),
        dict(name='合体前の抵当権の行き先', args=dict(
            title='合体前の抵当権は、どうなる？', sub='存続登記と消滅の承諾（毎日ドリル 第70日 イ・オ）',
            req='a side-by-side comparison',
            layout=_nb2_layout,
            callout='抵当権者が消滅を承諾したときは、消滅した旨を付記登記で記録し、合体後の建物には移記しません。\n存続登記と同一の登記をするときは、合体後の建物の相当区に移記します。抵当権なら乙区です。',
            footer='不動産登記法50条、不動産登記規則120条4項から6項まで',
            kanji=K('合体前の抵当権はどうなる存続登記消滅の承諾付記登記乙区移記合体後の建物相当区不動産登記法規則'), what='panels',
            check='confirm the two panel headers are different strings (存続登記 on the left and 消滅の承諾あり on the right) and that the left badge shows a green check mark while the right badge shows a red cross, ')),
    ],
)
