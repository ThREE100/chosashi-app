def _k(*t, n=24):
    out = []
    for c in ''.join(t):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_T1, _T2, _TOP = '宅地か雑種地か、', '準則で見分ける', '不動産登記法　地目の認定'
_cards = [
    dict(h='畑の中の農具小屋の敷地は宅地',
         ill='an isometric field of crop rows with a small sturdy shed standing on a concrete base in one corner. A signpost labeled 「宅地」 stands in front of the shed. A green check mark sits beside the shed.',
         words=['宅地'], tag='永久的な建物に限る'),
    dict(h='宅地に接しないテニスコートは雑種地',
         ill='an isometric tennis court on the right, separated from a house plot on the left by a narrow road. A signpost labeled 「雑種地」 stands beside the tennis court. A green check mark sits beside the signpost.',
         words=['雑種地'], tag='宅地に接すれば宅地'),
    dict(h='地目が変わったら一月以内に申請',
         ill='an isometric land plot changing from crop rows on the left into bare ground on the right, with a thin arrow between them. A calendar page labeled 「一月以内」 sits above the arrow. A green check mark sits beside the bare ground.',
         words=['一月以内'], tag='変更の日から数える'),
    dict(h='変更後の名義人は自分の登記から',
         ill='a horizontal timeline. On the left a flag with a small crop-row icon; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
         words=['自分の登記', '一月以内'], tag='起算日は登記があった日'),
    dict(h='ガスタンクの敷地は宅地',
         ill='an isometric large round gas tank standing on a land plot, with a signpost labeled 「宅地」 beside it. A smaller oil tank stands next to it on the same plot. A green check mark sits beside the signpost.',
         words=['宅地'], tag='石油タンクの敷地も宅地'),
]

D = dict(
    catch='地目の認定と、変更の登記の起算日',
    intro='土地の「地目」を、どのように認定するのかと、地目が変わったときの登記の申請を問う問題です（不動産登記事務取扱手続準則69条、不動産登記法37条）。この問題は、誤っているものの組合せを選びます。\n\nこの記事では、農具小屋、テニスコート、ガスタンクの敷地といった具体的な場面で地目を判断する決まりと、地目の変更の登記を申請する期限の数え始めを確認していきましょう。',
    sections={
        'ア': ('耕作地の中にある永久的設備の農具小屋の敷地は、宅地とする',
               '耕作地の区域内にある農具小屋などの敷地は、その建物が永久的設備と認められるものに限り、宅地とします（不動産登記事務取扱手続準則69条3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、畑の一角に、コンクリートの基礎を打った頑丈な農具小屋が建てられたとします。永久的設備と認められるので、その小屋の敷地の部分は宅地になります。仮設の小屋なら、この決まりは当てはまりません。'),
        'イ': ('テニスコートは、宅地に接続していなければ雑種地とする',
               'テニスコートやプールは、宅地に接続するものは宅地とし、その他は雑種地とします（不動産登記事務取扱手続準則69条9号）。\n\n問題文は、宅地に接続していないテニスコートを宅地としているので、本肢は誤りです。宅地に接続していなければ、雑種地です。\n\n**たとえば**、住宅の庭に続いて作られたテニスコートは宅地ですが、住宅から道路を隔てた別の土地につくったテニスコートは、雑種地になります。'),
        'ウ': ('地目が変更されたら、変更の日から一月以内に変更の登記を申請する',
               '地目又は地積について変更があったときは、表題部所有者又は所有権の登記名義人は、その変更があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条1項）。\n\n本肢は正しいといえます。\n\n**たとえば**、Cさんが所有する土地の地目が、田から雑種地に変わったとします。Cさんは、地目が変わった日から一月以内に、地目の変更の登記を申請しなければなりません。'),
        'エ': ('変更の後に所有者になった人は、自分の登記があった日から一月以内に申請する',
               '地目又は地積について変更があった後に表題部所有者又は所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、変更の登記を申請しなければなりません（不動産登記法37条2項）。\n\n本肢は正しいといえます。\n\n**たとえば**、すでに地目が変わっていた土地を、Dさんが買って所有権の移転の登記を受けたとします。Dさんの一月は、地目が変わった日からではなく、Dさんの所有権の登記があった日から数えます。'),
        'オ': ('ガスタンクの敷地は、宅地とする（雑種地ではない）',
               'ガスタンクの敷地や石油タンクの敷地は、宅地とします（不動産登記事務取扱手続準則69条10号）。\n\n問題文は、ガスタンクの敷地を雑種地としているので、本肢は誤りです。\n\n**たとえば**、E株式会社の土地にガスタンクが設置され、その敷地として使われることになった場合、その土地の地目は宅地です。同じタンクでも、鉄塔や変電所の敷地は、雑種地とされています（同条14号）。'),
    },
    summary=[
        ('ア', '正', '耕作地の中にある永久的設備の農具小屋の敷地は、宅地とする'),
        ('イ', '誤', 'テニスコートは、宅地に接続していなければ雑種地（宅地ではない）'),
        ('ウ', '正', '地目が変更されたときは、変更の日から一月以内に変更の登記を申請する'),
        ('エ', '正', '変更の後に所有者になった人は、自分の所有権の登記があった日から一月以内に申請する'),
        ('オ', '誤', 'ガスタンクの敷地は宅地（雑種地ではない）'),
    ],
    summary_tail='イは「宅地に接続している」かどうか、オは「宅地」と「雑種地」を入れ替えた出題です。地目の認定は、準則69条の例を一つずつ、表で覚えましょう。',
    supplements=[
        '### 補足説明（イ・オ）：宅地になるもの、雑種地になるもの\n\n準則69条は、判断に迷いやすい土地について、地目の決め方を例示しています。\n\n| 土地 | 地目 | 準則69条 |\n|---|---|---|\n| 耕作地の区域内の農具小屋の敷地（永久的設備に限る） | 宅地 | 3号 |\n| 宅地に接続するテニスコート・プール | 宅地 | 9号 |\n| 宅地に接続しないテニスコート・プール | 雑種地 | 9号 |\n| ガスタンク敷地・石油タンク敷地 | 宅地 | 10号 |\n| 鉄塔敷地・変電所敷地 | 雑種地 | 14号 |\n\n**たとえば**、同じ「タンク」でも、ガスタンクや石油タンクの敷地は宅地、鉄塔や変電所の敷地は雑種地です。名前の印象で決めずに、決まりを一つずつ覚えましょう。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第90日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記事務取扱手続準則69条3号・9号・10号・14号と、不動産登記法37条1項・2項は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの具体例（田から雑種地への変更）は、問題文の設定に沿って作った例で、田が何に使われて雑種地になるのかは条文では確認していません。',
        'アの「仮設の小屋なら、この決まりは当てはまりません」は、準則69条3号の「永久的設備と認められるものに限り」という文言から導いた説明です。',
    ],
    phrases=['永久的な農具小屋の敷地は宅地です', '宅地に接しないテニスコートは雑種地です', '地目が変わったら一月以内に申請です', '変更後の名義人は自分の登記から数えます', 'ガスタンクの敷地は宅地です'],
    header=dict(t1=_T1, t2=_T2, topic=_TOP, kanji='・'.join(_k(_T1, _T2, _TOP))),
    poster_intro='地目の認定と変更の登記を、「地目の認定と変更の登記」（グループA：ア・イ・ウ）と「名義人の変更と地目の認定」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title='地目の認定と変更を整理', sub='不動産登記法 第37条、準則 第69条（毎日ドリル 第90日）',
        col_a='地目の認定と変更の登記', col_b='名義人の変更と地目の認定', n_a=3,
        cards=_cards,
        kanji=_k(*[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards], '地目の認定と変更を整理地目の認定と変更の登記名義人の変更と地目の認定', n=24)),
    nb_label='イ・オ肢', nb_intro='イ・オの補足説明に合わせた1枚です。宅地になるものと、雑種地になるものを、場面ごとに表で整理します。',
    notebooks=[
        dict(name='宅地になるもの、雑種地になるもの', args=dict(
            title='宅地になるもの、雑種地になるもの', sub='準則69条の地目の例（毎日ドリル 第90日 イ・オ）',
            req='a five-row table',
            layout="""IMPORTANT: the two land categories are different strings: 「宅地」 and 「雑種地」. Draw 宅地 in blue and 雑種地 in orange everywhere they appear, so they can never be confused.

--- TABLE ---
A table with five rows. Each row has a scene on the left and the land category on the right, connected by a thin arrow.
Row 1: scene 「耕作地の中の、永久的設備の農具小屋の敷地」 (a sturdy shed in a field) → 宅地
Row 2: scene 「宅地に接続するテニスコート・プール」 (a tennis court next to a house) → 宅地
Row 3: scene 「宅地に接続しないテニスコート・プール」 (a tennis court across a road from a house) → 雑種地
Row 4: scene 「ガスタンク敷地・石油タンク敷地」 (a round tank) → 宅地
Row 5: scene 「鉄塔敷地・変電所敷地」 (a pylon tower) → 雑種地""",
            callout='テニスコートやプールは、宅地に接続していれば宅地、接続していなければ雑種地です。\nガスタンクや石油タンクの敷地は宅地で、鉄塔や変電所の敷地は雑種地です。',
            footer='不動産登記事務取扱手続準則69条',
            kanji='・'.join(_k('宅地雑種地耕作地永久的設備農具小屋敷地接続庭鉄塔変電所石油不動産登記事務取扱手続準則')), what='table',
            check='confirm 宅地 is drawn in blue and 雑種地 is drawn in orange in every row and that the two words are never confused, ')),
    ],
)
