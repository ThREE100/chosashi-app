# C-08 規約のつくり方（集会の決議と公正証書）
from fractions import Fraction as F

N, V = 40, 1000          # 区分所有者の数、議決権の合計
N_IN, V_IN = 25, 620     # 出席した区分所有者、その議決権
YES = [(19, 470), (19, 460)]  # 賛成（人数、議決権）

Q = F(3, 4)
NEED_N = -(-N_IN * Q.numerator // Q.denominator)   # 切り上げ：19
NEED_V = -(-V_IN * Q.numerator // Q.denominator)   # 465


def quorum():
    return N_IN * 2 > N and V_IN * 2 > V


def passed(n, v):
    return quorum() and F(n, N_IN) >= Q and F(v, V_IN) >= Q


def _r(n, v):
    return '可決' if passed(n, v) else '否決（議決権が足りない）'


LINES = [
    f'区分所有者{N}人・議決権の合計{V}。集会に{N_IN}人（議決権{V_IN}）が出席した。',
    f'定足数：{N_IN}人は{N}人の過半数、{V_IN}は{V}の過半数を超えるので足りる。',
    f'必要な賛成：{N_IN} × 3/4 ＝ {float(N_IN * Q):g} → **{NEED_N}人以上**、{V_IN} × 3/4 ＝ {float(V_IN * Q):g} → **{NEED_V}以上**。',
] + [f'賛成{n}人・議決権{v} → **{_r(n, v)}**。' for n, v in YES]


def verify():
    assert quorum()
    assert NEED_N == 19 and NEED_V == 465
    assert passed(19, 470) and not passed(19, 460) and not passed(18, 620)


SHEET = dict(
    id='C-08',
    law='区分所有法',
    articles='区分所有法第30条〜第32条・第37条・第45条・第66条・第67条',
    conclusion=[
        '規約は集会でつくる。区分所有者の**過半数**で議決権の**過半数**を持つ者が出席し、出席者と議決権の**各4分の3以上**で決める（区分所有法第31条第1項）。',
        '一部の区分所有者に**特別の影響**があるときは、その人の**承諾**も要る（区分所有法第31条第1項）。規約は**書面か電磁的記録**でつくる（区分所有法第30条第5項）。',
        '集会を経ずに**公正証書**でつくれるのは、最初に専有部分の全部を所有する者（区分所有法第32条）と、団地内の数棟の全部を所有する者（区分所有法第67条第2項）だけ。',
    ],
    blocks=[
        dict(kind='table', title='設定の方法（場合分け）',
             head=['場面', '方法', '根拠'],
             rows=[['区分所有者が設定する（原則）', '集会：定足数を満たし、出席者と議決権の各4分の3以上', '区分所有法第31条第1項'],
                   ['特別の影響を受ける区分所有者がいる', 'その区分所有者の承諾も要る', '区分所有法第31条第1項'],
                   ['一部共用部分の事項（全員の利害に関係しない）', '全員の規約に定めがなければ、共用すべき区分所有者の規約で', '区分所有法第30条第2項'],
                   ['その事項を全員の規約で定める', '共用すべき者の4分の1超（人数か議決権）が反対すればできない', '区分所有法第31条第2項'],
                   ['集会の手続', 'あらかじめ通知した事項だけ決議できる', '区分所有法第37条第1項'],
                   ['議決権を持つ区分所有者全員の承諾がある', '書面・電磁的方法による決議ができる', '区分所有法第45条第1項'],
                   ['最初に専有部分の全部を所有する者', '公正証書で：共用部分・規約敷地・分離処分可能・敷地権の割合の規約', '区分所有法第32条'],
                   ['団地内の数棟の全部を所有する者', '公正証書で団地共用部分の規約', '区分所有法第67条第2項'],
                   ['団地の規約', '区分所有法第31条第1項を準用（第31条第2項・第32条は準用しない）', '区分所有法第66条']]),
    ],
    example=dict(kind='計算例', title='集会の決議の数え方', lines=LINES),
    traps=['4分の3の分母は**出席した**区分所有者とその議決権で、人数と議決権の**両方**が要る。その前に定足数（過半数の出席）を満たす必要がある。',
           '公正証書で設定できるのは**最初に**全部を所有する者で、規約の種類も区分所有法第32条の4つに限る。管理・使用のきまりは集会でつくる。',
           '一部共用部分の事項は、全員の規約に定めがなければ**共用すべき区分所有者の規約**で定められる（区分所有法第30条第2項）。'],
    basis=['区分所有法第30条・第31条・第32条・第37条・第45条・第66条・第67条'],
    more=['topics/KE_15_shitchiken-bunrishobun-kanou-kiyaku.md', 'joubun-nigate/kubunshoyuu-hou/art005-kiyaku-shikichi/note_art005.md'],
    claims=[
        ('区分所有法', '31', '出席した区分所有者及びその議決権の各四分の三以上の多数による決議によつてする'),
        ('区分所有法', '31', '過半数（これを上回る割合を規約で定めた場合にあつては、その割合以上）の者であつて議決権の過半数'),
        ('区分所有法', '31', '一部の区分所有者の権利に特別の影響を及ぼすべきときは、その承諾を得なければならない'),
        ('区分所有法', '31', '四分の一を超える者又はその議決権の四分の一を超える議決権を有する者が反対したときは、することができない'),
        ('区分所有法', '30', '書面又は電磁的記録'),
        ('区分所有法', '30', '区分所有者間の利害の衡平が図られるように定めなければならない'),
        ('区分所有法', '30', '区分所有者以外の者の権利を害することができない'),
        ('区分所有法', '30', 'これを共用すべき区分所有者の規約で定めることができる'),
        ('区分所有法', '32', '最初に建物の専有部分の全部を所有する者は、公正証書により'),
        ('区分所有法', '67', '一団地内の数棟の建物の全部を所有する者は、公正証書により、前項の規約を設定することができる'),
        ('区分所有法', '66', '第三十一条第二項及び第三十二条を除く'),
        ('区分所有法', '45', '全員の承諾があるときは、書面又は電磁的方法による決議をすることができる'),
        ('区分所有法', '37', 'あらかじめ通知した事項についてのみ、決議をすることができる'),
    ],
    note_law='区分所有法は令和7年法律第47号による改正（令和8年4月1日施行）後の条文で書いた。規約の設定の決議は、定足数を満たした集会で、出席した区分所有者とその議決権で数える。',
    header=dict(l1='規約の', l2='つくり方', hl='つくり方',
                left='a meeting room with residents raising hands around a table and a rule book on it, all without any text',
                right='a notary office desk with a document tied with a ribbon and a round seal, next to a small apartment building model, all without any text'),
    zukai=dict(title='規約のつくり方', topics='定足数・4分の3・特別の影響・公正証書・通知',
               cards=[
                   dict(h='まず過半数が出席する', illust='A meeting room where more than half of the seats around the table are filled, a ballot box in the center.', words=[], tag='定足数が先'),
                   dict(h='出席者の各4分の3以上で決める', illust='Two balance scales side by side, one weighing people and one weighing voting power, each tilting toward the agreeing side with three quarters filled.', words=[], tag='人数と議決権の両方'),
                   dict(h='特別の影響があれば承諾も要る', illust='One resident whose room is highlighted under a spotlight, signing a consent paper at the meeting table while others watch.', words=[], tag='その人の承諾'),
                   dict(h='公正証書でつくれる人は限られる', illust='A single owner at a notary office desk signing a document tied with a ribbon and a round seal, an apartment building model beside him.', words=[], tag='最初の所有者など'),
                   dict(h='通知した事項だけ決議できる', illust='A notice sheet with a few checked agenda items pinned on a board, and a separate unlisted item left outside the meeting room door.', words=[], tag='通知が前提'),
               ]),
)
