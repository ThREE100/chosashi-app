def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='合筆できるのは、', t2='どんな場合？', topic='不動産登記法　合筆の登記')
_PT = '合筆の登記を整理'
_PS = '合筆の申請人と権利の特例（毎日ドリル 第71日）'

_cards = [
    dict(h='名義人でない買主は合筆を申請できない',
         ill='two neighboring land plots. A buyer figure holding a sales contract stands outside, drawn in faded gray, while an owner figure with a name tag labeled 「登記名義人」 holds a form. No check mark and no cross mark on this card.',
         words=['登記名義人'], tag='申請できるのは名義人'),
    dict(h='担保権の登記は全部が同一なら合筆できる',
         ill='two land plots each with a mortgage line on a record sheet. Three matching tags labeled 「目的」, 「受付」 and 「原因」 are connected between the two sheets by green lines. A green check mark sits beside the tags.',
         words=['目的', '受付', '原因'], tag='三つとも同一'),
    dict(h='承役地の地役権は範囲を申請情報にする',
         ill='two land plots being joined, with a shaded strip across a part of the merged plot. A document labeled 「地役権図面」 sits beside the plots. A green check mark sits beside the document.',
         words=['地役権図面'], tag='一部なら範囲を提供'),
    dict(h='合筆では乙土地の登記記録に集約する',
         ill='two record sheets, the left one with a cross-hatch pattern and labeled 「甲土地」, the right one highlighted and labeled 「乙土地」. An arrow runs from the left sheet to the right sheet. A green check mark sits beside the right sheet.',
         words=['甲土地', '乙土地'], tag='閉鎖されるのは甲土地'),
    dict(h='同一の担保権は全部に関する旨を付記する',
         ill='a merged land plot with a record sheet beside it. A mortgage line on the sheet has a small side-note line below it labeled 「付記登記」. A green check mark sits beside the side-note line.',
         words=['付記登記'], tag='合筆後の土地の全部'),
]

_nb1_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and three data rows.

Header row: 同一であることが必要な事項 | 内容

Row 1 (blue accent): 登記の目的 | 抵当権設定など
Row 2 (blue accent): 申請の受付の年月日及び受付番号 | 受付の日と番号
Row 3 (blue accent): 登記原因及びその日付 | 設定契約とその日

Below the table, a callout banner with the label: 三つとも同一であれば、合筆の制限の例外
Use exactly these strings, and no others."""

_nb2_layout = """--- FLOW ---
Render as a clean flat-design diagram in two stacked blocks connected by a small downward arrow with no text.
Block 1 (blue accent), block header: 合筆前. Scene: two record sheets side by side, the left labeled 甲土地 and the right labeled 乙土地.
Block 2 (green accent), block header: 合筆後. Scene: the right sheet labeled 乙土地 (合筆後の表題部を記録), and the left sheet labeled 甲土地 shown in faded gray with the label 閉鎖.
Use exactly these strings, and no others."""

D = dict(
    catch='合筆の特例は、承役地の地役権と担保権',
    intro='合筆の登記について、だれが申請できるのか、権利に関する登記があっても合筆できる場合、合筆後の登記記録の記録の仕方を問う問題です（不動産登記法39条・41条、不動産登記令別表、不動産登記規則105条〜107条）。\n\nこの記事では、合筆の制限の例外と、合筆後の登記記録の扱いを、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('名義人でない買主は、合筆を申請できない',
               '分筆又は合筆の登記は、表題部所有者又は所有権の登記名義人以外の者は、申請することができません（不動産登記法39条1項）。また、表題部所有者又は所有権の登記名義人が相互に異なる土地の合筆の登記は、することができません（同法41条3号）。\n\n甲土地を買い受けたBは、所有権の移転の登記を受けるまでは、登記名義人ではありません。本肢は誤りです。\n\n**たとえば**、Bが甲土地を買ったのに、登記名義人がまだ売主Aのままだとします。Bは、自分の乙土地との合筆の登記を申請することはできません。登記記録の上で甲土地はA、乙土地はBとなっており、名義人が異なるので、合筆の制限にも当たります。'),
        'イ': ('追加設定で受付が違う抵当権は、合筆できない',
               '所有権の登記以外の権利に関する登記がある土地は、原則として合筆の登記をすることができません（不動産登記法41条6号）。例外のひとつが、担保権の登記で、登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が、すべて同一のものです（不動産登記規則105条2号）。\n\n甲土地と乙土地の抵当権は受付の年月日及び受付番号が異なるので、この例外に当たりません。本肢は誤りです。\n\n**たとえば**、同じ債権を担保するために、甲土地に抵当権を設定した後、乙土地を追加で担保に入れたとします。受付が別々になるので、甲土地と乙土地は合筆できません。'),
        'ウ': ('地役権設定の範囲が一部なら、範囲を提供する',
               '承役地についてする地役権の登記は、合筆の制限の例外です（不動産登記規則105条1号）。地役権設定の範囲が合筆後の土地の一部であるときは、その範囲を申請情報の内容とします。\n\nあわせて、添付情報として、地役権設定の範囲を証する地役権者が作成した情報と、地役権図面を提供します（不動産登記令別表九の項）。本肢は正しいといえます。\n\n**たとえば**、承役地の甲土地を乙土地に合筆した後、地役権が及ぶのは合筆後の土地の南側だけだとします。この場合は、その南側の範囲を申請情報として示し、範囲を証する情報と地役権図面を提供します。'),
        'エ': ('合筆では、乙土地の登記記録に集約し、新しい登記記録は作らない',
               '甲土地を乙土地に合筆する合筆の登記では、乙土地の登記記録の表題部に合筆後の表題部の登記事項を記録し、甲土地の登記記録は閉鎖します（不動産登記規則106条1項・2項）。\n\n問題文は、乙土地の登記記録が閉鎖され、新たに登記記録が作成されるとしているので、本肢は誤りです。\n\n**たとえば**、甲土地を乙土地に合筆すると、残るのは乙土地の登記記録です。そこに合筆後の面積などが記録され、甲土地の登記記録は閉鎖されます。'),
        'オ': ('同一の担保権は、全部に関する旨を付記登記で記録する',
               '甲土地を乙土地に合筆する場合に、両方の登記記録に、登記の目的、申請の受付の年月日及び受付番号、登記原因及びその日付が同一の担保権の登記があるときは、乙土地の登記記録に、その登記が合筆後の土地の全部に関する旨を、付記登記によって記録します（不動産登記規則107条6項）。\n\n本肢は正しいといえます。\n\n**たとえば**、甲土地と乙土地に同一の抵当権の登記がある場合、合筆後の乙土地の抵当権の登記に、その抵当権が合筆後の土地の全部に及ぶ旨が付記されます。'),
    },
    summary=[
        ('ア', '誤', '合筆を申請できるのは、表題部所有者又は所有権の登記名義人だけ。移転の登記を受けていない買主は申請できない'),
        ('イ', '誤', '担保権の登記が合筆の例外になるのは、登記の目的、受付、登記原因とその日付が同一のときだけ'),
        ('ウ', '正', '承役地の地役権の範囲が合筆後の土地の一部なら、範囲を申請情報とし、範囲を証する情報と地役権図面を提供する'),
        ('エ', '誤', '合筆では、乙土地の登記記録に集約され、閉鎖されるのは甲土地。新しい登記記録は作られない'),
        ('オ', '正', '同一の担保権の登記は、乙土地の登記記録に、合筆後の土地の全部に関する旨が付記される'),
    ],
    summary_tail='アは申請人、イは「すべて同一」という条件、エは閉鎖される登記記録の取り違えです。合筆の制限には例外があり、例外の条件はすべて満たす必要があります。',
    supplements=[
        '### 補足説明（イ・オ）：担保権の登記があるのに合筆できる場合\n\n担保権の登記があっても合筆できるのは、次の3つが同一であるときです（不動産登記規則105条2号）。\n\n| 同一であることが必要な事項 | 具体例 |\n|---|---|\n| 登記の目的 | 抵当権設定 |\n| 申請の受付の年月日及び受付番号 | 同じ日に同じ番号で受け付けた登記 |\n| 登記原因及びその日付 | 同じ契約とその日付 |\n\n**たとえば**、甲土地と乙土地を一緒に担保に入れる抵当権を、同じ日に同じ申請で設定していれば、この3つが同一になります。そのときは合筆でき、合筆後は、その抵当権が合筆後の土地の全部に関する旨が付記されます。',
        '### 補足説明（エ）：合筆後の登記記録の扱い\n\n甲土地を乙土地に合筆したときの登記記録を整理します（不動産登記規則106条）。\n\n- 乙土地の登記記録：合筆後の表題部の登記事項を記録する。\n- 甲土地の登記記録：合筆した旨を記録して、閉鎖する。\n\n**たとえば**、甲土地の面積が200平方メートル、乙土地の面積が300平方メートルなら、合筆後は乙土地の登記記録に500平方メートルと記録されます。甲土地の登記記録は閉鎖されます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第71日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法39条1項、41条、不動産登記令別表九の項、不動産登記規則105条から107条までは、`note-articles/laws/` 配下の原文で確認しました。',
        '合筆後の土地の面積を足し合わせる例（補足説明エ）は、合筆後の表題部の記録を説明するための仮定の数字で、実際の面積の記録の仕方は個別の事案によります。',
        'イの「追加で担保に入れた」という場面は、受付の年月日及び受付番号が異なる典型例として挙げたものです。共同担保の取扱いの詳細は確認していません。',
    ],
    phrases=['合筆を申請できるのは名義人だけです', '担保権は三つとも同一なら合筆できます', '承役地の地役権は範囲を申請情報にします', '合筆で閉鎖されるのは甲土地です', '同一の担保権は付記登記で全部に及びます'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='合筆の登記を、「申請人と制限の例外」（グループA：ア・イ・ウ）と「合筆後の記録」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='申請人と制限の例外', col_b='合筆後の記録', n_a=3,
        cards=_cards,
        kanji=K(_PT, _PS, '申請人と制限の例外合筆後の記録', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='イ・オ・エ肢', nb_intro='イ・オとエの補足説明に合わせた2枚です。1枚目は、担保権の登記があっても合筆できるために同一であることが必要な3つの事項を示します。2枚目は、合筆後の登記記録の扱いを示します。',
    notebooks=[
        dict(name='担保権があっても合筆できる条件', args=dict(
            title='担保権があっても合筆できる？', sub='合筆の制限の例外（毎日ドリル 第71日 イ・オ）',
            req='a table',
            layout=_nb1_layout,
            callout='担保権の登記があっても合筆できるのは、登記の目的、受付の年月日及び受付番号、登記原因及びその日付が、すべて同一のときだけです。\n一つでも違えば、合筆できません。',
            footer='不動産登記規則105条2号',
            kanji=K('担保権があっても合筆できる登記の目的申請の受付の年月日及び受付番号登記原因及びその日付同一抵当権設定不動産登記規則'), what='table',
            check='confirm there are exactly three data rows, ')),
        dict(name='合筆後の登記記録', args=dict(
            title='合筆すると、登記記録はどうなる？', sub='合筆後の登記記録の扱い（毎日ドリル 第71日 エ）',
            req='a diagram',
            layout=_nb2_layout,
            callout='甲土地を乙土地に合筆すると、乙土地の登記記録に合筆後の表題部の登記事項が記録されます。\n閉鎖されるのは、合筆された甲土地の登記記録です。新しい登記記録は作られません。',
            footer='不動産登記規則106条1項・2項',
            kanji=K('合筆すると登記記録はどうなる甲土地乙土地合筆前合筆後表題部閉鎖不動産登記規則'), what='blocks',
            check='confirm there are exactly two blocks connected by one downward arrow with no text, ')),
    ],
)
