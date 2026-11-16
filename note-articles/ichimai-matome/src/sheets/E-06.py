# E-06 床面積に入るもの・入らないもの（準則第82条の各号）
from decimal import Decimal as D, ROUND_DOWN

# 計算例1：2階建の住宅（壁心で測った外形 8.19×6.37。2階に吹抜 2.73×1.82。屋外の階段は算入しない）
A, B = D('8.19'), D('6.37')
FUKI_A, FUKI_B = D('2.73'), D('1.82')
F1 = A * B
FUKI = FUKI_A * FUKI_B
F2 = F1 - FUKI

# 計算例2：停車場の乗降場（全長 60.00×幅 6.00。上屋があるのは 40.00 の部分だけ）
JOU_L, JOU_W, UWAYA_L = D('60.00'), D('6.00'), D('40.00')
JOU_ALL = JOU_L * JOU_W
JOU_UWAYA = UWAYA_L * JOU_W


def cut(x):
    return x.quantize(D('0.01'), rounding=ROUND_DOWN)


SHEET = dict(
    id='E-06',
    law='準則',
    articles='準則第77条・第82条、不動産登記規則第115条',
    conclusion=[
        '準則第82条の各号は、ふつうの建物の部分と、**特殊な施設**（第2号〜第5号）に分けて覚える。',
        '乗降場・荷物積卸場は**上屋の占める部分**、観覧席は**屋根の設備のある部分**だけを床面積にする（第2号・第3号）。建物と扱う範囲と同じ（準則第77条）。',
        '地下街などは**区画された部分**から、**常時一般に開放されている通路・階段**を除く（第4号）。',
    ],
    blocks=[
        dict(kind='table', title='ふつうの建物の部分（準則第82条）',
             head=['部分', '扱い', '号'],
             rows=[['天井高1.5メートル未満の地階・屋階', '入らない', '第1号'],
                   ['1室の一部だけ天井高1.5メートル未満', '例外：その1室に入る', '第1号'],
                   ['階段室・エレベーター室など', '入る（床があるとみなす）', '第6号'],
                   ['建物に附属する屋外の階段', '入らない', '第7号'],
                   ['上階まで吹抜の部分', '上階に入らない', '第8号'],
                   ['煙突・ダストシュート', '内部（一部が外側に及ぶものを含む）は入る。外側は入らない', '第10号'],
                   ['出窓', '高さ1.5メートル以上・下部が床面と同じ高さなら入る', '第11号']]),
        dict(kind='table', title='特殊な施設（準則第82条第2号〜第5号）',
             head=['施設', '床面積にする部分', '号'],
             rows=[['停車場の上屋を有する乗降場・荷物積卸場', '上屋の占める部分の面積', '第2号'],
                   ['野球場・競馬場などの観覧席', '屋根の設備のある部分の面積', '第3号'],
                   ['地下停車場・地下駐車場・地下街', '壁又は柱等で区画された部分。常時開放の通路・階段は除く', '第4号'],
                   ['停車場の地下道設備（地下停車場のものを含む）', '入らない', '第5号']]),
    ],
    example=dict(kind='計算例', title='入る部分と入らない部分を分けて求める',
                 lines=[f'1階：{A} × {B} ＝ {F1} → {cut(F1)}㎡（屋外の階段は足さない。第7号）',
                        f'2階：{A} × {B} − {FUKI_A} × {FUKI_B}（吹抜）＝ {F1} − {FUKI} ＝ {F2} → {cut(F2)}㎡（第8号）。',
                        f'乗降場：全体 {JOU_L} × {JOU_W} ＝ {cut(JOU_ALL)}㎡ではなく、上屋の部分 {UWAYA_L} × {JOU_W} ＝ {cut(JOU_UWAYA)}㎡（第2号）。']),
    traps=['乗降場・観覧席は**全体の面積ではない**（第2号・第3号）。',
           '地下街は区画された部分でも、**常時一般に開放されている通路・階段**は除く（第4号ただし書）。',
           '吹抜は**上階**に入れないだけ。下の階からは引かない（第8号）。'],
    basis=['準則第77条・第82条', '不動産登記規則第115条'],
    more=['topics/KE_10_yukamenseki-sannyu.md'],
    claims=[
        ('準則', '82', '停車場の上屋を有する乗降場及び荷物積卸場の床面積は、その上屋の占める部分の乗降場及び荷物積卸場の面積により計算する'),
        ('準則', '82', '屋根の設備のある部分の面積を床面積として計算する'),
        ('準則', '82', '壁又は柱等により区画された部分の面積により定める。ただし、常時一般に開放されている通路及び階段の部分を除く'),
        ('準則', '82', '停車場の地下道設備（地下停車場のものを含む。）は、床面積に算入しない'),
        ('準則', '82', '各階の床面の接着する壁その他の区画の中心線で囲まれた部分による'),
        ('準則', '82', '建物に附属する屋外の階段は、床面積に算入しない'),
        ('準則', '82', 'その吹抜の部分は、上階の床面積に算入しない'),
        ('準則', '82', '出窓は、その高さ１．５メートル以上のものでその下部が床面と同一の高さにあるものに限り、床面積に算入する'),
        ('準則', '77', 'ただし、上屋を有する部分に限る'),
        ('準則', '77', 'ただし、屋根を有する部分に限る'),
        ('不動産登記規則', '115', '一平方メートルの百分の一未満の端数は、切り捨てるものとする'),
    ],
    unverified=['「外気分断性」「出入口の有無」で算入を判断するという説明は、解説書の整理で、規則・準則の原文にはない（準則第82条第7号は「建物に附属する屋外の階段」とだけ書く）。本シートは原文の語だけで書いた。',
                '区分建物の一棟の建物の床面積をどの線で測るかは、規則・準則の原文で確かめられなかったため書いていない。'],
    header=dict(l1='床面積に', l2='入るもの・入らないもの', hl='入らないもの',
                left='a railway platform with a roof covering only part of it, and a stadium stand with a roof over some seats, all without any text',
                right='a cutaway of a two-story house with an open void, an outside staircase and a bay window, all without any text'),
    zukai=dict(title='床面積に入るか入らないか', topics='乗降場・観覧席・地下街・吹抜・屋外の階段・出窓',
               cards=[
                   dict(h='乗降場は上屋の部分だけ', illust='A long railway platform; only the part under the roof is shaded, the uncovered end is left blank.', words=['上屋'], tag='上屋の占める部分'),
                   dict(h='観覧席は屋根のある部分', illust='A stadium stand where only the seats under the roof are shaded; open seats are blank.', words=['屋根'], tag='屋根の設備のある部分'),
                   dict(h='地下街の開放通路は除く', illust='An underground mall seen from above: shops divided by walls are shaded, a public passage and stairs in the middle are left blank.', words=['通路'], tag='通路・階段を除く'),
                   dict(h='吹抜は上の階に入れない', illust='A two-story section; the first floor is fully shaded, the void area on the second floor is blank.', words=['吹抜'], tag='上階に算入しない'),
                   dict(h='屋外の階段は入れない', illust='A house with an outside staircase attached to the wall; the staircase is left unshaded.', words=[], tag='屋外の階段は不算入'),
                   dict(h='床と同じ高さの高い出窓', illust='Two bay windows side by side: a tall one starting at floor level is shaded, a small raised one is blank.', words=['出窓'], tag='条件つきで算入'),
               ]),
)


def verify():
    assert F1 == D('52.1703') and cut(F1) == D('52.17'), F1
    assert FUKI == D('4.9686'), FUKI
    assert F2 == D('47.2017') and cut(F2) == D('47.20'), F2
    assert JOU_ALL == D('360.0000') and cut(JOU_UWAYA) == D('240.00')
    assert cut(F2) < cut(F1)
