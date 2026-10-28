def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='事前通知のしくみを整理', sub='不動産登記規則 第70条から第72条（毎日ドリル 第107日）',
    col_a='事前通知と前の住所地', col_b='申出の期間と本人確認', n_a=3,
    cards=[
        dict(h='書面申請の申出は、同じ印鑑を押す',
             ill='a notice sheet labeled 「真実」 held by an owner figure, a round seal being pressed on it, and an arrow toward a registry building. A smaller application sheet with the same seal mark sits beside it. A green check mark sits beside the seal.',
             words=['真実'], tag='申請書と同じ印'),
        dict(h='法人の本店宛は、書留郵便で送る',
             ill='a company building with a registered envelope being delivered, and a postal worker figure holding a receipt. The envelope carries a ribbon labeled 「書留」. A green check mark sits beside the envelope.',
             words=['書留'], tag='本人限定ではない'),
        dict(h='行政区画の変更なら前の住所地は通知なし',
             ill='a map where a town border is redrawn around a house that stays in the same place, with a faded gray letter icon at the old address position. A green check mark sits beside the house.',
             words=[], tag='引っ越しではない'),
        dict(h='申出の期間は、発送の日から数える',
             ill='a calendar page labeled 「二週間」 with a mail envelope flying out from a registry building at the start of the calendar. A green check mark sits beside the calendar.',
             words=['二週間'], tag='受け取りの日ではない'),
        dict(h='資格確認書は、二つ以上そろえる',
             ill='two identity papers side by side. The first is labeled 「資格確認書」 and the second is a plain official document with a government seal icon. A bracket joins them. A green check mark sits beside the bracket.',
             words=['資格確認書'], tag='一通では足りない'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='事前通知の送り方と、申出の期間', sub='不動産登記規則70条（毎日ドリル 第107日 イ・エ）',
    req='a comparison table',
    layout="""IMPORTANT: this is a four-row table with three columns. The three column headers 「宛先」, 「送り方」 and 「申出の期間」 are different strings. Draw the 「送り方」 column in blue and the 「申出の期間」 column in green so that they cannot be confused. This image uses no check marks and no cross marks.

--- TABLE ---
Row 1: 自然人 | 本人限定受取郵便 | 発送から二週間
Row 2: 法人の代表者の住所宛 | 本人限定受取郵便 | 発送から二週間
Row 3: 法人の本店宛 | 書留郵便など | 発送から二週間
Row 4: 外国に住所がある | 書留郵便など | 発送から四週間
Use exactly these strings, and no others.""",
    callout='法人の代表者の住所宛でなく本店宛に送るときは、本人限定受取郵便ではなく、書留郵便などで送ります。\n申出の期間は、通知を受け取った日ではなく、通知を発送した日から数えます。',
    footer='不動産登記規則70条',
    what='table',
    check='confirm the table has exactly four rows and three columns with the exact strings, ')
_N2 = dict(
    title='本人確認の書類は、数が違う', sub='資格者代理人の本人確認情報（毎日ドリル 第107日 オ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two sides must show OPPOSITE marks, not the same mark. The left side shows a green check mark; the right side shows a red cross. The two panel headers are different strings: 「一通で足りる書類」 on the left and 「二通以上が必要な書類」 on the right; draw them in different accent colors (blue and orange) so they can never be confused or duplicated.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 一通で足りる書類
Scene: an isometric scene with three identity card icons stacked vertically, each followed by a label: 運転免許証, 個人番号カード, 旅券等
Result badge with a green check mark: 一通だけでよい

RIGHT PANEL (orange accent):
Panel header: 二通以上が必要な書類
Scene: an isometric scene with one identity paper icon labeled 健康保険の資格確認書 and a second paper icon beside it with a faint outline and no text.
Result badge with a red cross: 一通だけでは足りない""",
    callout='運転免許証や個人番号カード、旅券等は、一通の提示で足ります。\n健康保険の資格確認書などは、二つ以上の提示か、官公庁が発行した書類と合わせた提示が必要です。',
    footer='不動産登記規則72条2項',
    what='panels',
    check='confirm the two panel headers are different strings (一通で足りる書類 on the left and 二通以上が必要な書類 on the right) and that the left panel shows a green check mark while the right panel shows a red cross, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='期間は発送から二週間、本店宛は書留',
    intro='登記識別情報を提供できないときの事前通知について、正しいものを選ぶ問題です（不動産登記法23条、不動産登記規則70条から72条）。登記官が登記義務者に通知を送り、申請が本当かを確かめる仕組みが問われています。\n\nこの記事では、申出の方法、通知の送り方、前の住所地への通知、本人確認の書類を、具体的な場面で確認していきましょう。この問題は、正しい肢の組合せを選ぶ形です。',
    sections={
        'ア': ('書面申請の申出は、申請書と同じ印鑑を押して出す',
               '書面で申請した場合、登記義務者が通知の内容は真実だと申し出る方法は、通知の書面に「申請の内容が真実である旨」を書き、記名し、申請書又は委任状に押したものと同じ印鑑で押印して、登記所に提出する方法です（不動産登記規則70条5項2号）。\n\n本肢は正しいといえます。\n\n**たとえば**、売主のAに法務局から事前通知の書面が届いたとします。Aは、その書面に「この申請は真実です」という旨を書いて記名し、売買の申請書に押したのと同じ印鑑を押して、法務局に提出します。'),
        'イ': ('法人の本店宛は、書留郵便などで送る',
               '登記義務者が法人で、代表者の住所に宛てて送るときは、本人限定受取郵便で送ります（不動産登記規則70条1項1号）。それ以外の法人宛の通知は、書留郵便、又は引受け・配達の記録を行う信書便で送ります（同項2号）。\n\n問題文は、代表者の住所ではなく本店に宛てて送るとしています。この場合は書留郵便などなので、本肢は誤りです。\n\n**たとえば**、株式会社Bの本店に宛てて事前通知を送るときは、書留郵便で送ります。本人限定受取郵便は、代表者個人の住所に宛てるときの送り方です。'),
        'ウ': ('住所の変更の原因が行政区画の変更なら、前の住所地への通知は不要',
               '所有権に関する登記で、登記義務者の住所について変更の登記がされているときは、登記官は、前の住所地にも通知をするのが原則です（不動産登記法23条2項）。\n\nただし、その変更の登記の原因が行政区画の変更などであるときは、通知をしなくてよいとされています（不動産登記規則71条2項1号）。\n\n本肢は正しいといえます。\n\n**たとえば**、市町村の合併で、住所の表示が変わったとします。引っ越しをしたわけではないので、前の住所地へ通知を送る意味がありません。この場合は、変更の登記から三か月が過ぎていなくても、前の住所地への通知は不要です。'),
        'エ': ('申出の期間は、受け取った日ではなく、発送した日から数える',
               '申出をすべき期間は、通知を発送した日から二週間です。ただし、登記義務者が外国に住所を有するときは、四週間です（不動産登記規則70条8項）。\n\n問題文は、通知を受け取った日から二週間としています。数え始めは受け取った日ではなく発送した日なので、本肢は誤りです。\n\n**たとえば**、法務局が4月1日に通知を発送したとします。Aが受け取ったのが4月3日でも、二週間の数え始めは4月1日です。受け取ってから二週間あるわけではありません。'),
        'オ': ('健康保険の資格確認書は、一通では足りない',
               '資格者代理人が、面識のない申請人の本人確認をするとき、提示を受ける書類は次のとおり分かれています（不動産登記規則72条2項）。\n\n- 運転免許証、個人番号カード、旅券等：いずれか一つ。\n- 健康保険の資格確認書などの書類：いずれか二つ以上の提示、又はそのうちの一つと官公庁が発行した書類の一つ以上の提示。\n\n問題文は、資格確認書一通で足りるとしているので、本肢は誤りです。\n\n**たとえば**、調査士のBが、面識のない登記義務者から健康保険の資格確認書を一通だけ見せられても、それだけでは足りません。もう一つ、住民票のような官公庁の書類などを加えて、確認をします。'),
    },
    summary=[
        ('ア', '正', '書面申請の申出は、通知の書面に真実である旨を書き、申請書や委任状と同じ印鑑を押して提出する'),
        ('イ', '誤', '法人の本店に宛てて送るときは、本人限定受取郵便ではなく、書留郵便などで送る'),
        ('ウ', '正', '住所の変更の原因が行政区画の変更なら、前の住所地への通知は不要'),
        ('エ', '誤', '申出の期間は、受け取った日ではなく、通知を発送した日から二週間'),
        ('オ', '誤', '健康保険の資格確認書は一通では足りず、二つ以上、又は官公庁の書類と合わせて提示を受ける'),
    ],
    summary_tail='イは「送り方」、エは「数え始め」、オは「書類の数」をすり替えた出題です。数や方法は、一つずつ条文に当てはめましょう。',
    supplements=[
        '### 補足説明（イ・エ）：事前通知の送り方と、申出の期間\n\n通知の送り方は、宛先で決まります（不動産登記規則70条1項）。\n\n- 自然人、法人の代表者の住所宛：本人限定受取郵便又はこれに準ずる方法。\n- 法人の本店など、上記以外の法人宛：書留郵便又は引受け・配達の記録を行う信書便。\n- 外国に住所を有する登記義務者：書留郵便等又はこれらに準ずる方法。\n\n申出の期間は、通知を発送した日から二週間です。外国に住所があるときだけ、四週間です（同条8項）。\n\n**たとえば**、国内の会社の本店に宛てた通知は書留で送り、申出の期間は発送の日から二週間です。外国に住所のある人なら、四週間になります。',
        '### 補足説明（オ）：本人確認の書類は、種類によって必要な数が違う\n\n面識のない申請人の本人確認で提示を受ける書類は、種類によって必要な数が違います（不動産登記規則72条2項）。\n\n- 運転免許証、個人番号カード、旅券等：一通でよい。\n- 健康保険の資格確認書など：二つ以上、又はそのうち一つと官公庁の書類を合わせる。\n\n**たとえば**、運転免許証を持っている人なら、その一通で確認できます。免許証がなく、健康保険の資格確認書しかない人は、もう一つの書類を用意してもらいます。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第107日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、不動産登記法23条、不動産登記規則70条、71条、72条は、`note-articles/laws/` 配下の原文で確認しました。',
        'ウの具体例（市町村合併で住所の表示が変わる場合）は、71条2項1号の「行政区画の変更」の例として挙げたもので、個別の運用の確認はしていません。「引っ越しをしたわけではない」という説明は、条文からの一般的な整理です。',
        'オの具体例（住民票のような官公庁の書類を加える例）は、72条2項3号の「官公庁から発行された書類」の例として挙げた一般的な説明です。',
    ],
    phrases=['書面申請の申出は同じ印鑑で出します', '法人の本店宛は書留郵便で送ります', '行政区画の変更なら前の住所地は不要です', '申出の期間は発送の日から数えます', '資格確認書は一通では足りません'],
    header=dict(t1='事前通知は、', t2='どう送る？', topic='不動産登記法　事前通知',
                kanji='・'.join(_kj('事前通知はどう送る', '不動産登記法事前通知', '毎', n=8))),
    poster_intro='事前通知を、「事前通知と前の住所地」（グループA：ア・イ・ウ）と「申出の期間と本人確認」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='イ・エ・オ肢', nb_intro='イ・エ・オの補足説明に合わせた2枚です。1枚目は、事前通知の送り方と申出の期間を表で整理します。2枚目は、本人確認の書類で一通で足りるものと足りないものを、左右の対比で示します。',
    notebooks=[
        dict(name='事前通知の送り方と、申出の期間', args=_N1),
        dict(name='本人確認の書類は、数が違う', args=_N2),
    ],
)
