def K(*texts, n=20):
    out = []
    for t in texts:
        for c in t:
            if '一' <= c <= '龥' and c not in out and c not in '一二三四五六七八九十':
                out.append(c)
    return out[:n]


_H = dict(t1='地目は何になる？', t2='いつから数える？', topic='不動産登記法　地目の認定')
_PT = '地目の認定と変更の登記を整理'
_PS = '地目変更の申請と地目の認定（毎日ドリル 第73日）'

_cards = [
    dict(h='変更の後に名義人になったら自分の登記から',
         ill='a horizontal timeline. On the left a flag labeled 「造成完了」; further right a second flag labeled 「自分の登記」. A green bracket labeled 「一月以内」 starts at the second flag and extends to the right. The part of the timeline before the second flag is drawn in gray with no bracket.',
         words=['造成完了', '自分の登記', '一月以内'], tag='起算日は自分の登記'),
    dict(h='工場に接続する物干場は宅地',
         ill='an isometric factory building with a clothes drying area beside it. A land plot under the factory and the drying area is drawn in one color, with a label 「宅地」. A green check mark sits beside the label.',
         words=['宅地'], tag='建物の効用を果たす土地'),
    dict(h='耕作地の農具小屋は、永久的設備なら宅地',
         ill='a farm field with a small solid tool shed on it. A label 「永久的設備」 sits beside the shed, and the plot under the shed is labeled 「宅地」. A green check mark sits beside the shed.',
         words=['永久的設備', '宅地'], tag='永久的設備に限る'),
    dict(h='牧場地域の牧畜の建物の敷地は牧場',
         ill='a ranch area with a barn and grazing cattle. The land plot under the barn is drawn in the same color as the pasture, with a label 「牧場」. A green check mark sits beside the label.',
         words=['牧場'], tag='すべて牧場'),
    dict(h='地目変更の原因日付は現況が変わった日',
         ill='a horizontal timeline with two flags: the left flag labeled 「許可」 is drawn in faded gray, and the right flag labeled 「造成完了」 is highlighted with a green circle labeled 「原因日付」. A green check mark sits beside the right flag.',
         words=['許可', '造成完了', '原因日付'], tag='許可日ではない'),
]

_nb1_layout = """--- TABLE ---
Render as a clean flat-design table with a header row and three data rows, with a small icon at the start of each row.

Header row: 土地の場所と建物 | 地目

Row 1 (blue accent): 耕作地の区域内の農具小屋の敷地（永久的設備に限る） | 宅地
Row 2 (green accent): 牧場地域内の牧畜のための建物の敷地 | 牧場
Row 3 (orange accent): 工場に接続する物干場 | 宅地

IMPORTANT: Row 2 ends with the string 牧場 and Rows 1 and 3 end with the string 宅地. Draw 牧場 in green and 宅地 in blue so they can never be confused or duplicated.
Use exactly these strings, and no others."""

_nb2_layout = """--- TIMELINE ---
Render as a clean flat-design horizontal timeline with three flags from left to right, labeled with these strings:
Left flag (gray): 農地転用の許可を受ける
Middle flag (green): 造成工事が完了して宅地になる
Right flag (gray): 登記を申請する
A green circle highlights the middle flag with the label: 地目変更の登記の原因日付
The left flag carries a red cross and the label 原因日付ではない.
Use exactly these strings, and no others."""

D = dict(
    catch='地目の起算日は、自分の登記の日から',
    intro='地目の認定と、地目に関する変更の登記の問題です（不動産登記法37条、不動産登記事務取扱手続準則68条・69条）。\n\nこの記事では、変更の登記の期限がいつから数えられるのか、建物のある土地の地目の決め方、登記原因の日付の考え方を、具体的な場面で確認します。この問題は、正しいものを選ぶ形式です。',
    sections={
        'ア': ('変更の後に名義人になった人は、自分の登記の日から数える',
               '地目又は地積について変更があった後に所有権の登記名義人となった者は、その者に係る所有権の登記があった日から一月以内に、地目に関する変更の登記を申請しなければなりません（不動産登記法37条2項）。\n\n変更のあった日から数えるのではありません。本肢は正しいといえます。\n\n**たとえば**、5月10日に畑が宅地に造成され、6月20日にBが所有権の移転の登記を受けたとします。Bの一月は、5月10日からではなく、登記を受けた6月20日から数えます。'),
        'イ': ('工場に接続する物干場は、宅地とする',
               '工場又は営業場に接続する物干場又はさらし場は、宅地とします（不動産登記事務取扱手続準則69条11号）。\n\n問題文は、建物の敷地ではないから雑種地とするとしているので、本肢は誤りです。\n\n**たとえば**、工場の隣にある洗濯物を干す場所は、工場に接続していれば、その土地の地目は宅地となります。雑種地ではありません。'),
        'ウ': ('耕作地の農具小屋は、永久的設備なら宅地とする',
               '耕作地の区域内にある農具小屋等の敷地は、その建物が永久的設備と認められるものに限り、宅地とします（準則69条3号）。\n\n本肢は正しいといえます。\n\n**たとえば**、畑の中に、しっかりと建てられた農具小屋があるとします。その小屋の敷地は、永久的設備と認められるなら宅地です。簡単に動かせる小屋であれば、周りの畑と同じ地目のままです。'),
        'エ': ('牧場地域内の牧畜の建物の敷地は、牧場とする',
               '牧畜のために使用する建物の敷地、牧草栽培地及び林地等で牧場地域内にあるものは、すべて牧場とします（準則69条4号）。\n\n問題文は、永久的設備と認められる建物の敷地は宅地とするとしているので、本肢は誤りです。\n\n**たとえば**、牧場の中に牛舎を建てたとします。牛舎が永久的設備であっても、牧場地域内の牧畜のための建物なので、その敷地は牧場です。宅地にはなりません。'),
        'オ': ('地目変更の原因日付は、現況が変わった日',
               '地目は、土地の現況及び利用目的に重点を置いて定めます（準則68条柱書）。そのため、地目に関する変更の登記の原因の日付は、農地法の許可を受けた日ではなく、現況が変わった日です。\n\n問題文は、許可を受けた令和8年6月1日としているので、本肢は誤りです。\n\n**たとえば**、6月1日に農地転用の許可を受け、8月1日に造成工事を終えて宅地にしたとします。登記原因の日付は、許可の日の6月1日ではなく、造成工事が終わった8月1日です。'),
    },
    summary=[
        ('ア', '正', '変更の後に所有権の登記名義人となった人の一月は、自分に係る登記があった日から数える'),
        ('イ', '誤', '工場に接続する物干場は、宅地とする'),
        ('ウ', '正', '耕作地の区域内の農具小屋の敷地は、永久的設備と認められるものに限り宅地とする'),
        ('エ', '誤', '牧場地域内にある牧畜のための建物の敷地は、永久的設備でもすべて牧場とする'),
        ('オ', '誤', '地目変更の登記の原因日付は、許可の日ではなく、現況が変わった日'),
    ],
    summary_tail='ウとエは、耕作地の農具小屋と牧場地域の建物の取り違えを誘う出題です。オは、許可の日と現況が変わった日の取り違えです。地目は現況で決める、という原則に戻って考えましょう。',
    supplements=[
        '### 補足説明（ウ・エ・イ）：建物の敷地の地目の認定\n\n準則69条は、場所や建物の種類ごとに、地目の認定の仕方を定めています。似た場面を比べて整理します。\n\n| 場面 | 地目 | 準則69条 |\n|---|---|---|\n| 耕作地の区域内の農具小屋の敷地（永久的設備に限る） | 宅地 | 3号 |\n| 牧場地域内の牧畜のための建物の敷地 | 牧場 | 4号 |\n| 工場又は営業場に接続する物干場又はさらし場 | 宅地 | 11号 |\n\n**たとえば**、同じように畑や牧場の中に建物を建てても、耕作地の中なら、永久的設備のときだけ宅地です。牧場地域の中なら、永久的設備でも牧場のままです。',
        '### 補足説明（オ）：地目変更の原因日付\n\n地目の変更があったときの原因日付は、「現況が変わった日」です。農地転用の許可を受けただけでは、現況は変わっていません。\n\n- 許可を受けた日：まだ畑のまま。\n- 造成工事が完了して、宅地として使える状態になった日：現況が変わった日。登記原因の日付になる。\n\n**たとえば**、6月1日に許可を受け、8月1日に造成を終えたなら、8月1日が原因日付です。変更の登記の期限（一月）も、8月1日から数えます（不動産登記法37条1項）。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第73日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法37条1項・2項、不動産登記事務取扱手続準則68条柱書、69条3号・4号・11号は、`note-articles/laws/` 配下の原文で確認しました。',
        'オの「登記原因の日付は、許可の日ではなく、現況が変わった日」という結論は、登記実務の取扱いによるもので、手元の法令の原文では日付の定め方を直接確認できていません（原文は未確認）。準則68条柱書の「現況及び利用目的に重点を置く」という定めから導いた整理を本文に書いています。',
        'ウの「簡単に動かせる小屋なら、周りの畑と同じ地目のまま」という説明は、準則69条3号が永久的設備に限るとしていることからの一般的な整理で、個別の事案ごとの判断は確認していません。',
    ],
    phrases=['変更の後に名義人になったら自分の登記から数えます', '工場に接続する物干場は宅地です', '農具小屋は永久的設備なら宅地です', '牧場地域の建物の敷地は牧場です', '原因日付は許可日ではありません'],
    header=dict(t1=_H['t1'], t2=_H['t2'], topic=_H['topic'], kanji='・'.join(K(*_H.values()))),
    poster_intro='地目の認定と変更の登記を、「変更の登記と建物の敷地の地目」（グループA：ア・イ・ウ）と「牧場と原因日付」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=dict(
        title=_PT, sub=_PS,
        col_a='変更の登記と建物の敷地の地目', col_b='牧場と原因日付', n_a=3,
        cards=_cards,
        kanji=K(_PT, _PS, '変更の登記と建物の敷地の地目牧場と原因日付', *[c['h'] + c['tag'] + ''.join(c['words']) for c in _cards])),
    nb_label='ウ・エ・イ肢と、オ肢', nb_intro='ウ・エ・イとオの補足説明に合わせた2枚です。1枚目は、建物の敷地の地目を場面ごとに表で示します。2枚目は、地目変更の原因日付を時間の流れで示します。',
    notebooks=[
        dict(name='建物の敷地の地目の認定', args=dict(
            title='この土地の地目は何？', sub='準則69条の地目の認定（毎日ドリル 第73日 イ・ウ・エ）',
            req='a table',
            layout=_nb1_layout,
            callout='耕作地の中の農具小屋は、永久的設備と認められるものに限り宅地です。\n牧場地域内の牧畜のための建物の敷地は、永久的設備でもすべて牧場です。',
            footer='不動産登記事務取扱手続準則69条3号・4号・11号',
            kanji=[], what='table',
            check='confirm that the string 牧場 in row 2 and the string 宅地 in rows 1 and 3 are different strings drawn in different colors, ')),
        dict(name='地目変更の原因日付', args=dict(
            title='地目変更の原因日付はいつ？', sub='許可の日と現況が変わった日（毎日ドリル 第73日 オ）',
            req='a timeline diagram',
            layout=_nb2_layout,
            callout='地目は、土地の現況及び利用目的に重点を置いて定めます。\n登記原因の日付は、許可を受けた日ではなく、造成工事が完了して現況が変わった日です。',
            footer='不動産登記事務取扱手続準則68条柱書',
            kanji=[], what='timeline',
            check='confirm there are exactly three flags and that only the middle flag is highlighted, ')),
    ],
)

for _nb in D['notebooks']:
    _a = _nb['args']
    _a['kanji'] = K(_a['title'], _a['sub'], _a['layout'], _a['callout'], _a['footer'])
