def _kj(*texts, n=22):
    out = []
    for c in ''.join(texts):
        if '一' <= c <= '龥' and c not in out:
            out.append(c)
    return out[:n]


_P = dict(
    title='調査士会と協会のきまりを整理', sub='土地家屋調査士法 第53条から第63条（毎日ドリル 第106日）',
    col_a='調査士法人と調査士会', col_b='連合会と協会', n_a=3,
    cards=[
        dict(h='従たる事務所を設けたら、自動で会員になる',
             ill='an isometric map with a main office building on the left region and a branch office building on the right region, divided by a dotted border line. A thin arrow runs from the main office to a membership badge labeled 「会員」 at the branch region. A green check mark sits beside the badge.',
             words=['会員'], tag='主たる事務所で登記'),
        dict(h='会員になったら二週間以内に届け出る',
             ill='a calendar page labeled 「二週間」 beside an envelope holding two papers and an arrow pointing to two small building icons. A green check mark sits beside the calendar.',
             words=['二週間'], tag='調査士会と連合会へ'),
        dict(h='違反と思ったら、法務大臣に報告する',
             ill='a surveyors association building figure handing a report sheet up to a government building figure labeled 「法務大臣」. A green check mark sits beside the government building.',
             words=['法務大臣'], tag='報告の相手は大臣'),
        dict(h='登録審査会は会長と委員四人',
             ill='a round table with one chair marked by a badge labeled 「会長」 and four chairs around it. A green check mark sits beside the table.',
             words=['会長'], tag='委員の任期は二年'),
        dict(h='協会の定款の定めは変更できない',
             ill='an open association charter document with one highlighted line and a large padlock closed over that line. A green check mark sits beside the padlock.',
             words=[], tag='理事の過半数は社員'),
    ],
)
_P['kanji'] = _kj(_P['title'], _P['sub'], _P['col_a'], _P['col_b'], *[c['h'] + ''.join(c['words']) + c['tag'] for c in _P['cards']])

_N1 = dict(
    title='報告と、注意勧告の違い', sub='調査士会の役目（毎日ドリル 第106日 ウ）',
    req='a side-by-side comparison',
    layout="""IMPORTANT: the two panel headers are different strings and must not be confused: 「違反と思うとき」 on the left and 「違反するおそれがあるとき」 on the right. Draw them in different accent colors (blue and orange). This image uses no check marks and no cross marks.

--- COMPARISON ---
Two panels side by side (left and right), same height.

LEFT PANEL (blue accent):
Panel header: 違反と思うとき
Scene: an isometric scene of an association building handing a report sheet up to a government building figure.
Action badge: 法務大臣に報告

RIGHT PANEL (orange accent):
Panel header: 違反するおそれがあるとき
Scene: an isometric scene of an association building figure speaking to a member figure and holding a small caution flag.
Action badge: 会員に注意し勧告""",
    callout='調査士会は、会員が法律に違反すると思うときは、法務大臣に報告します。\n報告の相手は調査士会連合会ではありません。違反するおそれの段階では、会員に注意を促し、勧告できます。',
    footer='土地家屋調査士法55条・56条',
    what='panels',
    check='confirm the two panel headers are different strings (違反と思うとき on the left and 違反するおそれがあるとき on the right) and that the two action badges are different strings, ')
_N2 = dict(
    title='協会の定款で変更できない三つの定め', sub='公共嘱託登記土地家屋調査士協会（毎日ドリル 第106日 オ）',
    req='a checklist diagram',
    layout="""--- CHECKLIST ---
Render as a clean flat-design vertical list with a header block and three rows.
Header block (blue accent), header: 定款で変更できない定め. Next to the header, draw a closed padlock icon.
Below it, three rows stacked vertically, each with a small closed padlock icon, with these exact labels: 社員の資格 | 社員になる加入 | 理事の過半数は社員
Under the three rows, a note band (gray accent) with the label: 社員総会の決議でも変更できない
Use exactly these strings, and no others. This image uses no check marks and no cross marks.""",
    callout='協会の定款の次の三つの定めは、変更することができません。\n社員の資格、社員になる加入、理事の過半数は社員でなければならないこと、の三つです。社員総会で決議しても変えられません。',
    footer='土地家屋調査士法63条',
    what='blocks',
    check='confirm there are exactly three rows, each with a closed padlock icon, and no check marks or cross marks anywhere, ')
for _n in (_N1, _N2):
    _n['kanji'] = _kj(_n['title'], _n['sub'], _n['layout'].split('--- ')[-1], _n['callout'], _n['footer'])

D = dict(
    catch='違反の報告先は連合会でなく法務大臣',
    intro='調査士会、調査士会連合会、公共嘱託登記土地家屋調査士協会に関する、土地家屋調査士法のきまりを問う問題です（土地家屋調査士法53条・55条・62条・63条）。調査士法人の入会、会の報告義務、登録審査会、協会の定款が出題されています。\n\nこの記事では、だれが・いつ・だれに届け出たり報告したりするのかを、具体的な場面で確認します。この問題は、誤っているものの組合せを選ぶ形です。',
    sections={
        'ア': ('管轄外に従たる事務所を設けたら、自動で会員になる',
               '調査士法人は、その事務所の所在地を管轄する法務局や地方法務局の管轄区域の外に従たる事務所を設けたときは、主たる事務所の所在地でその旨の登記をした時に、従たる事務所の所在地の調査士会の会員となります（土地家屋調査士法53条4項）。\n\n本肢は正しいといえます。\n\n**たとえば**、X法務局の管内に主たる事務所がある法人Aが、Y地方法務局の管内に従たる事務所を設けた場合、Aは、X管内で従たる事務所の設置の登記をした時に、Y管内の調査士会の会員となります。Y管内の調査士会に入会の手続をする必要はありません。'),
        'イ': ('会員になったら二週間以内に、二か所へ届け出る',
               '調査士法人は、新たに調査士会の会員となったときは、会員となった日から二週間以内に、登記事項証明書と定款の写しを添えて、その旨を、その調査士会と調査士会連合会に届け出なければなりません（土地家屋調査士法53条6項）。\n\n本肢は正しいといえます。\n\n**たとえば**、4月1日に従たる事務所の設置の登記をして会員となった場合、その日から二週間以内に、届出を済ませる必要があります。届出先は、その調査士会と調査士会連合会の両方です。'),
        'ウ': ('調査士会の報告先は、法務大臣である',
               '調査士会は、所属の会員がこの法律やこの法律に基づく命令に違反すると思うときは、その旨を法務大臣に報告しなければなりません（土地家屋調査士法55条）。\n\n問題文は報告先を調査士会連合会としていますが、報告の相手は法務大臣です。本肢は誤りです。\n\n**たとえば**、X調査士会が、会員のBが法律に違反していると思ったとします。X調査士会が報告する相手は、全国の会をまとめる調査士会連合会ではなく、法務大臣です。'),
        'エ': ('登録審査会は、会長と委員四人で、委員の任期は二年',
               '調査士会連合会には登録審査会が置かれ、会長と委員四人で組織します。委員の任期は二年です。ただし、欠員が生じたときに補充される委員の任期は、前任者の残りの期間です（土地家屋調査士法62条1項・3項・6項）。\n\n本肢は正しいといえます。\n\n**たとえば**、委員のCさんが任期の途中で欠けて、新しくDさんが補充されたとします。Dさんの任期は、新たに二年ではなく、Cさんが務めるはずだった残りの期間です。'),
        'オ': ('協会の定款の定めは、社員総会の決議でも変更できない',
               '公共嘱託登記土地家屋調査士協会は、社員の資格、社員になる加入、理事の員数の過半数は社員でなければならないこと、という内容の定款の定めがあるものに限り、設立できます。この定めは、変更することができません（土地家屋調査士法63条1項・2項）。\n\n問題文は、社員総会の決議で、理事の員数の過半数を三分の一以上に変更できるとしています。変更はできないので、本肢は誤りです。\n\n**たとえば**、協会が「理事は社員が三分の一以上いればよい」と社員総会で決めたくなっても、決議だけでは変更できません。理事の過半数は社員のままです。'),
    },
    summary=[
        ('ア', '正', '管轄外に従たる事務所を設けたら、主たる事務所の所在地で登記をした時に、従たる事務所の所在地の調査士会の会員となる'),
        ('イ', '正', '新たに会員となったら、二週間以内に、登記事項証明書と定款の写しを添えて、調査士会と連合会に届け出る'),
        ('ウ', '誤', '会員の法令違反について、調査士会が報告する相手は法務大臣であり、調査士会連合会ではない'),
        ('エ', '正', '登録審査会は会長と委員四人で組織し、委員の任期は二年、補充の委員は前任者の残りの期間'),
        ('オ', '誤', '協会の定款の定めのうち、理事の過半数は社員とする定めなどは、社員総会の決議でも変更できない'),
    ],
    summary_tail='ウは「報告の相手」、オは「変更できるか」を入れ替えた出題です。報告は法務大臣へ、協会の核心の定めは変更できない、と押さえましょう。',
    supplements=[
        '### 補足説明（ウ）：報告と、注意勧告は、段階が違う\n\n調査士会は、会員の法令違反について、段階に応じて次のように対応します。\n\n- 違反すると思うとき：法務大臣に報告しなければならない（55条）。\n- 違反するおそれがあると認めるとき：会員に注意を促し、必要な措置を講ずべきことを勧告できる（56条）。\n\n**たとえば**、会員が届出を怠りそうな段階で、調査士会が「注意してください」と声をかけるのが注意勧告です。すでに違反していると思われるときは、調査士会は法務大臣に報告します。',
        '### 補足説明（オ）：協会の定款で変更できない三つの定め\n\n公共嘱託登記土地家屋調査士協会は、63条1項の三つの定款の定めがあるものに限り設立でき、その定めは変更できません（63条2項）。\n\n- 社員は、主たる事務所の所在地を管轄する区域内に事務所を有する調査士又は調査士法人であること。\n- そのような調査士や調査士法人が社員になろうとするときは、正当な理由がなければ拒めないこと。\n- 理事の員数の過半数は、社員であること。\n\n**たとえば**、理事の過半数を社員以外の人にしたいと考えても、社員総会で決めることはできません。',
    ],
    notes=[
        '文章としては、タイトルから補足説明までを、このままnoteに貼り付けて投稿できる内容です。',
        'この問題は、毎日ドリル（朝の択一）のオリジナル問題で、法務省の過去問ではありません。出題行は「出題：毎日ドリル　第106日（朝）　択一」とし、note の引用の出典欄は空欄にします。',
        '各肢の根拠のうち、土地家屋調査士法53条、55条、56条、62条、63条は、`note-articles/laws/` 配下の原文で確認しました。',
        'アの具体例（X管内とY管内の法人の例）は、53条4項の文言をかみ砕いた一般的な説明で、個別の運用の確認はしていません。',
        'オの具体例（理事の過半数を社員以外にしたい場合の説明）は、63条1項3号・2項の文言から導いた一般的な整理です。',
    ],
    phrases=['従たる事務所を設けたら会員になります', '会員になったら二週間以内に届出です', '違反の報告先は法務大臣です', '登録審査会は会長と委員四人です', '協会の核心の定めは変更できません'],
    header=dict(t1='報告の相手は、', t2='だれ？', topic='土地家屋調査士法　調査士会と協会',
                kanji='・'.join(_kj('報告の相手はだれ', '土地家屋調査士法調査士会と協会', '毎', n=8))),
    poster_intro='調査士会などのきまりを、「調査士法人と調査士会」（グループA：ア・イ・ウ）と「連合会と協会」（グループB：エ・オ）の2グループに分け、短い見出し・図解・短い結論タグだけで構成する2列・5枚のポスター型カードで俯瞰する構成です。カードに番号は付けません。',
    poster=_P,
    nb_label='ウ・オ肢', nb_intro='ウ・オの補足説明に合わせた2枚です。1枚目は、違反と思うときの報告と、違反するおそれの段階の注意勧告を、左右の対比で示します。2枚目は、協会の定款で変更できない三つの定めを整理します。',
    notebooks=[
        dict(name='報告と、注意勧告の違い', args=_N1),
        dict(name='協会の定款で変更できない三つの定め', args=_N2),
    ],
)
