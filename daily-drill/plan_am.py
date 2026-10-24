"""朝（択一＋空欄補充）の第23日〜第120日の論点の割り当てを、過去問の出題頻度で作る（schedule/am_plan.json・am_plan.md）。
頻度は、note-articles/ の年度別の択一式解説記事（平成17年度〜令和8年度）のファイル名の論点（例：q09-hikkai-tokutei）を数えたもの。
配分は本番に合わせて、21日周期で不動産登記法（令・規則・準則・先例を含む）17・民法3・調査士法1（98日で約80・14・4）。
重みの大きい論点ほど早く・多く出す（なめらかな重み付きラウンドロビン。同じ論点を2日続けない）。
第d日の択一は論点 A(d)、空欄補充は翌日の択一の論点 A(d+1) の条文（同じ日の択一と条文を分ける）。第23日の択一は第22日の空欄補充（法第6条・第7条・第9条・第10条）。
使い方: python3 daily-drill/plan_am.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
# (論点, 分野, 重み, 過去問の解説の論点名〈note-articles の qNN-<論点>.md〉, 条文の目安)
T = [
 ('筆界特定（申請・手続・効果）', '不登法', 5, ['hikkai-tokutei', 'hikkaitokutei'], '法第123条〜第150条、規則第206条〜'),
 ('地目の認定・地目変更の登記', '不登法', 5, ['chimoku', 'chimoku-nintei', 'chimoku-henkou'], '法第37条、規則第99条、準則第68条・第69条'),
 ('分筆の登記（申請人・地積測量図・権利の登記の移記）', '不登法', 5, ['bunpitsu', 'bunpitsu-touki', 'tochi-bunpitsu'], '法第39条・第40条、規則第78条・第101条〜第105条、準則第67条・第72条'),
 ('地図・地図に準ずる図面・地図訂正', '不登法', 5, ['chizu-teisei', 'chizu', 'chiban'], '法第14条、規則第10条〜第16条、準則第12条〜第17条'),
 ('建物の認定・種類・個数', '不登法', 5, ['tatemono-nintei', 'tatemono-kosuu', 'tatemono-shurui'], '規則第111条〜第114条、準則第77条〜第81条'),
 ('建物の合併・分割', '不登法', 5, ['tatemono-gappei', 'tatemono-bunkatsu', 'tatemono-bunkatsu-gappei'], '法第54条・第56条、規則第128条〜第134条'),
 ('床面積（算入・不算入・区分建物の内法）', '不登法', 4, ['yukamenseki'], '規則第115条、準則第82条'),
 ('附属建物', '不登法', 3, ['fuzoku-tatemono'], '法第2条第23号、準則第78条、規則第112条'),
 ('区分建物（表題登記・専有部分・一括申請）', '不登法', 4, ['kubun-tatemono', 'kubun-tatemono-hyouji', 'senyuken'], '法第47条・第48条、区分所有法第1条・第2条'),
 ('共用部分・共用部分である旨の登記', '不登法', 2, ['kyouyoububun'], '法第58条、区分所有法第4条、規則第141条'),
 ('敷地権（要件・割合・敷地権である旨の登記）', '不登法', 2, ['shikichiken'], '法第44条第1項第9号・第46条、区分所有法第22条、規則第118条〜第123条'),
 ('建物の合体による登記等', '不登法', 3, ['gattai-touki', 'gattai'], '法第49条・第50条、令別表十三、規則第120条'),
 ('合筆の登記（制限・申請人）', '不登法', 3, ['gappitsu', 'tochi-gappitsu'], '法第39条・第41条、規則第105条・第106条'),
 ('登記識別情報（通知・提供・失効）', '不登法', 2, ['touki-shikibetsu-jouhou', 'toukishikibetsujouhou', 'touki-shikibetsu-joho'], '法第21条・第22条、令第8条、規則第61条〜第68条'),
 ('地積測量図・建物図面・各階平面図', '不登法', 2, ['tatemonozumen', 'tatemono-zumen', 'chisekisokuryouzu', 'zumen-sakusei'], '規則第73条〜第83条、準則第50条〜第55条'),
 ('建物の所在・家屋番号', '不登法', 2, ['tatemono-shozai'], '規則第112条、準則第79条・第88条'),
 ('表題部所有者（変更・更正・所有権証明）', '不登法', 2, ['hyoudaibu-shoyuusha', 'shutoku-jikou'], '法第27条第3号・第31条〜第33条、準則第87条'),
 ('建物の滅失の登記', '不登法', 2, ['tatemono-messitsu', 'tatemono-messhitsu'], '法第57条、準則第102条'),
 ('地積の更正・地積に関する変更の登記', '不登法', 2, ['chiseki-kousei'], '法第37条・第38条、規則第10条第4項、準則第72条'),
 ('申請情報・添付情報', '不登法', 2, ['tenpu-jouhou', 'tatemono-tenpu', 'shinsei-jouhou'], '令第3条・第7条・別表、規則第34条〜第37条'),
 ('建物の表題登記・表題部の変更の登記', '不登法', 2, ['tatemono-hyoudai-touki', 'tatemono-hyoudai', 'tatemono-hyoudaibu-henkou', 'tatemono-hyoudaibu'], '法第47条・第51条・第53条'),
 ('土地の表題登記', '不登法', 1, ['tochi-hyoudai'], '法第36条、令別表四'),
 ('登録免許税（表示の登記）', '不登法', 2, ['touroku-menkyozei'], '登録免許税法別表第一の一（十三）・第5条'),
 ('登記記録・保存期間・登記事項証明書', '不登法', 2, ['hozon-kikan', 'hozonkikan', 'toukijikou-shoumei'], '法第119条〜第121条、規則第28条'),
 ('申請の手続（電子申請・代理・原本還付・取下げ・却下）', '不登法', 2, ['denshi-shinsei', 'dairi', 'genpon-kanpu', 'kyakka-torisage', 'kyakka', 'kankatsu'], '法第17条・第18条・第25条、規則第39条・第55条'),
 ('代位による申請・相続人による申請', '不登法', 2, ['daii-shinsei', 'touki-shinseinin'], '法第30条・第33条、民法第423条'),
 ('本人確認・事前通知・資格者代理人', '不登法', 2, ['honnin-kakunin'], '法第23条・第24条、規則第70条〜第72条'),
 ('審査請求', '不登法', 1, ['shinsaseikyuu'], '法第156条〜第158条'),
 ('民法：意思表示・無効と取消し・行為能力', '民法', 3, ['ishihyouji', 'ishi-hyouji', 'mukou-torikeshi', 'koui-nouryoku'], '民法第3条〜第21条・第93条〜第126条'),
 ('民法：代理', '民法', 1, ['dairi'], '民法第99条〜第118条'),
 ('民法：時効（取得時効・消滅時効・完成猶予と更新）', '民法', 1, ['jikou'], '民法第144条〜第169条'),
 ('民法：物権変動と対抗要件', '民法', 2, ['taikouyouken', 'bukken-hendou'], '民法第176条・第177条'),
 ('民法：共有', '民法', 2, ['kyouyuu'], '民法第249条〜第264条'),
 ('民法：相隣関係・所有権の取得', '民法', 1, ['souringkankei'], '民法第209条〜第248条'),
 ('民法：相続（法定相続・代襲・遺産分割・遺言）', '民法', 3, ['souzoku', 'houtei-souzoku', 'daishuu-souzoku', 'isanbunkatsu', 'igon'], '民法第882条〜第1044条'),
 ('調査士法：業務・義務・責任', '調査士法', 2, ['chousashihou'], '調査士法第3条・第20条〜第25条'),
 ('調査士法：登録・懲戒', '調査士法', 1, ['chousashi-touroku'], '調査士法第8条〜第16条・第42条〜第46条'),
 ('調査士法：調査士法人', '調査士法', 1, ['chousashi-houjin'], '調査士法第26条〜第41条'),
 ('調査士法：調査士会・連合会・公共嘱託登記', '調査士法', 1, ['chousashihou'], '調査士法第47条〜第68条'),
]
FIRST = ('登記所・事務の委任・登記官（法第6条・第7条・第9条・第10条）', '不登法', 0, ['kankatsu'], '法第6条・第7条・第9条・第10条')
STYLES = ['事例', '規則準則', '条文', '先例', '事例', '規則準則', '条文']   # 7日あたり 事例2・規則準則2・条文2・先例1


PATTERN = ['不登法', '不登法', '不登法', '民法', '不登法', '不登法', '不登法', '不登法', '不登法', '不登法', '民法',
           '不登法', '不登法', '不登法', '不登法', '不登法', '不登法', '民法', '不登法', '不登法', '調査士法']   # 21日で 不登17・民法3・調査士法1


def swrr(items, n):
    """なめらかな重み付きラウンドロビン：重みの大きいものほど早く・多く。同じものを2回続けない"""
    cur = [0.0] * len(items)
    tot = sum(t[2] for t in items)
    out, last = [], None
    for _ in range(n):
        for i, t in enumerate(items):
            cur[i] += t[2]
        order = sorted(range(len(items)), key=lambda i: (-cur[i], i))
        i = next((j for j in order if j != last), order[0])
        cur[i] -= tot
        out.append(items[i])
        last = i
    return out


def seq(n):
    fields = [PATTERN[(k + 1) % len(PATTERN)] for k in range(n)]      # 第24日から
    pools = {f: iter(swrr([t for t in T if t[1] == f], fields.count(f))) for f in set(fields)}
    return [next(pools[f]) for f in fields]


def main():
    s = seq(98)              # 第24日〜第121日（第121日は第120日の空欄補充のためだけ）
    days = {23: FIRST}
    for k, i in enumerate(s):  # i は論点のタプル
        days[24 + k] = i
    plan = []
    for d in range(23, 121):
        a, w = days[d], days[d + 1]
        st = STYLES[(d - 23) % 7] if a[1] == '不登法' else ('事例' if (d % 2) else '条文')
        plan.append({'day': d, 'id': f'AM-{d:03d}', 'takuitsu': a[0], 'field': a[1], 'style': st, 'past_topics': a[3], 'articles_hint': a[4],
                     'cloze_topic': w[0], 'cloze_field': w[1], 'cloze_hint': w[4], 'mode': '正しい' if d % 2 else '誤り'})
    json.dump(plan, open(os.path.join(HERE, 'schedule', 'am_plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    from collections import Counter
    md = ['# 朝（択一＋空欄補充）第23日〜第120日の割り当て（出題頻度順。plan_am.py で自動生成）', '',
          '| 日 | 択一の論点 | 形式 | 空欄補充の論点（翌日の択一） |', '|---|---|---|---|']
    md += [f"| {p['day']} | {p['takuitsu']} | {p['style']} | {p['cloze_topic']} |" for p in plan]
    c = Counter(p['field'] for p in plan)
    md += ['', f'分野の内訳：' + '、'.join(f'{k} {v}日' for k, v in c.items())]
    open(os.path.join(HERE, 'schedule', 'am_plan.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    print(dict(c))


if __name__ == '__main__':
    main()
