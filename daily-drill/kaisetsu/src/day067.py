def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='審査請求に、', t2='期限はある？', topic='不動産登記法　審査請求')
_PT = '登記官の処分への審査請求を整理'
_PS = '不動産登記法（毎日ドリル 第67日）'

_cards = [
    dict(h='審査請求に期間の制限はない',
         ill='a calendar with several pages flipping past, drawn in faded gray, and a form labeled 「審査請求」 resting in front of the calendar. A green check mark sits beside the form.',
         words=['審査請求'], tag='期間制限なし'),
    dict(h='審査請求は登記官を経由する',
         ill='a three-step route drawn left to right: an applicant figure holding a form labeled 「審査請求」, then a registrar figure at a desk, then a building labeled 「法務局長」. Arrows connect the three. A green check mark sits beside the registrar.',
         words=['審査請求', '法務局長'], tag='まず登記官へ'),
    dict(h='却下すべきなら登記官に命じる',
         ill='a building labeled 「法務局長」 with a figure pointing toward a registrar figure at a desk, who holds a stamp labeled 「却下」. A green check mark sits beside the registrar.',
         words=['法務局長', '却下'], tag='処分するのは登記官'),
    dict(h='理由がなければ三日以内に送付',
         ill='a registrar figure at a desk placing a folder into an envelope, with a small calendar page labeled 「三日以内」 beside it. A green check mark sits beside the calendar.',
         words=['三日以内'], tag='意見を付けて送る'),
    dict(h='隣地の所有者は筆界異議で争えない',
         ill='two neighboring land plots with a dotted boundary line between them. A neighbor owner figure holds a form labeled 「筆界特定」 and stands at the boundary. A green check mark sits beside the form. No cross mark on this card.',
         words=['筆界特定'], tag='筆界を争うなら別の手続'),
]

_nb1_layout = """--- FLOW ---
Render as a clean flat-design vertical flow in four steps connected by small downward arrows with no text.
Step 1 (blue accent), step header: 審査請求人. A person figure holding a form, with the label: 登記官を経由して審査請求をする
Step 2 (green accent), step header: 登記官. A registrar figure at a desk with two short branches, labeled: 理由があると認める：相当の処分をする | 理由があると認めない：審査請求の日から三日以内に、意見を付けて送付する
Step 3 (orange accent), step header: 法務局長. A building icon with the label: 理由があると認める：登記官に相当の処分を命じる
Use exactly these strings, and no others."""

_nb2_layout = """IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a red cross; the right side shows a green check mark. The two panel headers are different strings: 「地積更正の取消しを求める審査請求」 on the left and 「筆界特定の申請」 on the right; draw them in different accent colors (gray and blue) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (gray accent):
Panel header: 地積更正の取消しを求める審査請求
Scene: a neighbor owner figure holding a form toward a record sheet labeled 「地積更正」, with the label 筆界に異議があることを理由とする.
Result badge with a red cross: 認められない

RIGHT PANEL (blue accent):
Panel header: 筆界特定の申請
Scene: a neighbor owner figure beside two land plots with a dotted boundary line between them, holding a form.
Result badge with a green check mark: 筆界を争う手続"""

D = dict(
    catch='審査請求に期間の制限はありません',
    intro='登記官の処分や不作為に不服があるときの、審査請求の問題です（不動産登記法156条〜158条）。判例の趣旨に照らして、正しいものを選びます。\n\nこの記事では、期間の制限があるのか、審査請求はどこに出すのか、法務局の長は何を命じるのかを、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('登記官の処分への審査請求には、期間の制限がない',
               '登記官の処分に不服がある人は、登記官を監督する法務局又は地方法務局の長に審査請求をすることができます（不動産登記法156条1項）。\n\nこの審査請求には、行政不服審査法18条（審査請求期間）が適用されません（不動産登記法158条）。そのため、却下の処分を知った日の翌日から3月を過ぎた後でも、審査請求をすることができます。本肢は正しいといえます。\n\n**たとえば**、分筆の登記の申請が却下され、そのときは納得して放置していたAが、半年後に「やはり納得できない」と考えたとします。この場合も、Aは審査請求をすることができます。'),
        'イ': ('審査請求は、登記官を経由してする',
               '審査請求は、登記官を経由してしなければなりません（不動産登記法156条2項）。\n\n問題文は、登記官を経由することができないとしているので、本肢は誤りです。\n\n**たとえば**、登記官の処分に不服がある人は、審査請求書を、処分をした登記官を経由して出します。登記官は、審査請求を理由があると認めるときは、自分で相当の処分をします（同法157条1項）。登記官にも、見直す機会があるということです。'),
        'ウ': ('却下すべきと認めるときも、登記官に却下を命じる',
               '不作為についての審査請求で、法務局又は地方法務局の長は、申請を却下すべきものと認めるときは、登記官にその申請を却下する処分を命じなければなりません（不動産登記法157条5項）。\n\n本肢は正しいといえます。\n\n**たとえば**、地目の変更の登記を申請したのに、登記官が何も処分をしないため、Aが審査請求をしたとします。法務局の長は、その申請を却下すべきと考えたときでも、自分で却下せず、登記官に「却下する処分をしなさい」と命じます。'),
        'エ': ('送付の期限は、審査請求の日から三日以内',
               '登記官は、審査請求を理由があると認めない場合には、審査請求の日から三日以内に、意見を付して事件を法務局又は地方法務局の長に送付しなければなりません（不動産登記法157条2項）。\n\n問題文は「1週間以内」としているので、本肢は誤りです。\n\n**たとえば**、審査請求を受けた登記官が、見直したうえで「理由があるとは認められない」と判断したとします。登記官は、三日以内に、意見を付けて、法務局の長に事件を送ります。'),
        'オ': ('隣地の所有者は、筆界の異議を理由に争えない',
               '判例の趣旨によれば、甲土地について地積の更正の登記がされた場合に、隣接する乙土地の所有者が、筆界に異議があることを理由として、その登記の取消しを求める審査請求をすることはできません。この結論は、条文に明文があるものではありません。\n\n問題文は「審査請求をすることができる」としているので、本肢は誤りです。\n\n**たとえば**、隣の土地の面積が更正の登記で書き換えられ、「境界がおかしい」と感じたBがいるとします。筆界を争いたいときは、審査請求ではなく、筆界特定の申請（不動産登記法131条1項）などの手続によります。'),
    },
    summary=[
        ('ア', '正', '登記官の処分への審査請求には、期間の制限がない'),
        ('イ', '誤', '審査請求は、登記官を経由してしなければならない'),
        ('ウ', '正', '不作為の審査請求で却下すべきと認めるときも、法務局の長は登記官に却下の処分を命じる'),
        ('エ', '誤', '登記官が意見を付けて事件を送付する期限は、審査請求の日から三日以内'),
        ('オ', '誤', '隣地の所有者は、筆界の異議を理由に、地積更正の登記の取消しを求める審査請求はできない'),
    ],
    summary_tail='イは「経由」の有無を、エは「三日以内」という数字を入れ替えた出題です。審査請求は、登記官を経由し、登記官が三日以内に送付する、という流れで覚えておきましょう。',
    supplements=[
        '### 補足説明（イ・エ）：審査請求の流れ\n\n登記官の処分についての審査請求の流れを、順に整理します（不動産登記法156条〜157条）。\n\n1. 審査請求人が、登記官を経由して、審査請求をする（156条2項）。\n2. 登記官が、審査請求を理由があると認めるときは、相当の処分をする（157条1項）。\n3. 理由があると認めないときは、審査請求の日から三日以内に、意見を付して法務局の長に送付する（157条2項）。\n4. 法務局の長が、理由があると認めるときは、登記官に相当の処分を命じる（157条3項）。\n\n**たとえば**、却下の処分を受けた人が審査請求をすると、まず処分をした登記官が見直します。登記官が考えを改めなければ、三日以内に、意見を付けて法務局の長へ送ります。',
        '### 補足説明（オ）：筆界を争うときの手続\n\n筆界に異議があるときに使う手続は、地積の更正の登記の取消しを求める審査請求ではありません。\n\n| 手続 | 筆界を争う手続になるか |\n|---|---|\n| 地積の更正の登記の取消しを求める審査請求（筆界の異議を理由とする） | 認められない |\n| 筆界特定の申請（不動産登記法131条1項） | 筆界の位置を特定する手続 |\n\n**たとえば**、隣の土地の更正の登記に納得がいかなくても、その登記の取消しを求める審査請求はできません。筆界がどこにあるかを明らかにしたいときは、筆界特定の申請をします。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第67日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法131条1項、156条、157条、158条は、`note-articles/laws/` 配下の原文で確認しました。',
        'オは判例の趣旨による肢で、結論を直接定めた条文はありません（原文は未確認）。本文では「判例の趣旨によれば」と明示しました。筆界確定訴訟によって争うという一般的な整理は、条文からの一般的な整理で、補足説明では筆界特定の申請だけを挙げています。',
        'アの結論は、158条が行政不服審査法18条の適用を除外していることから導いたものです。具体例の「半年後」は、期間制限がないことを示すための仮定の数字です。',
    ],
    phrases=['審査請求に期間の制限はありません', '審査請求は登記官を経由します', '却下を命じるのも登記官なんです', '送付の期限は三日以内です', '隣地の所有者は筆界異議で争えません'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='登記官の処分への審査請求を、「審査請求の仕組み」（グループA：ア・イ・ウ）と「送付と争えない場合」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='審査請求の仕組み', col_b='送付と争えない場合', n_a=3,
        cards=_cards,
        kanji=K(_PT, _PS, '審査請求の仕組み送付と争えない場合', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、審査請求の流れを順に示します。2枚目は、筆界を争う手続として認められるものとそうでないものを左右の対比で示します。',
    notebooks=[
        dict(name='審査請求の流れ', args=dict(
            title='審査請求は、どこを通る？', sub='登記官の処分についての審査請求（毎日ドリル 第67日 イ・エ）',
            req='a flow diagram',
            layout=_nb1_layout,
            callout='審査請求は、登記官を経由してします。\n登記官は、理由があると認めないときは、審査請求の日から三日以内に、意見を付けて法務局の長に送付します。',
            footer='不動産登記法156条2項、157条1項から3項まで',
            kanji=K('審査請求は登記官を経由してどこを通る理由があると認めない三日以内意見を付けて法務局の長に送付相当の処分を命じる不動産登記法'), what='blocks',
            check='confirm there are exactly three steps connected by downward arrows with no text, and that Step 2 has two branches, ')),
        dict(name='筆界を争う手続', args=dict(
            title='筆界を争えるのは、どちら？', sub='審査請求と筆界特定の申請（毎日ドリル 第67日 オ）',
            req='a side-by-side comparison',
            layout=_nb2_layout,
            callout='隣地の所有者は、筆界に異議があることを理由に、地積更正の登記の取消しを求める審査請求はできません。\n筆界を争うなら、筆界特定の申請などの手続によります。',
            footer='不動産登記法131条1項',
            kanji=K('筆界を争えるのはどちら地積更正の取消しを求める審査請求筆界特定の申請隣地の所有者異議認められない手続'), what='panels',
            check='confirm the two panel headers are different strings (地積更正の取消しを求める審査請求 on the left and 筆界特定の申請 on the right) and that the left panel shows a red cross while the right panel shows a green check mark, ')),
    ],
)
