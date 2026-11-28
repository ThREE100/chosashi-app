"""第1回の台本（d01.py）を読み込み、各ツールの入力に共通で使う。"""
import importlib.util, sys
D01 = '/home/claude/chosashi-app/note-unei/hikkake-shindan/kaiwa/src/d01.py'
spec = importlib.util.spec_from_file_location('d01', D01)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ITEM = m.ITEM
SIDE = {'S': '左の人物（若い女性）', 'T': '右の人物（丸い鳥）'}
def plain_text():
    out = [f"題：{ITEM['catch']}", '']
    for i, p in enumerate(ITEM['pages'], 1):
        out.append(f"## ページ{i}　{p['caption']}")
        out.append(p['lead']); out.append('')
        for j, pn in enumerate(p['panels'], 1):
            out.append(f"コマ{j}：{pn['fig']}")
            for who, t in pn['talk']:
                out.append(f"　{SIDE[who]}「{t}」")
        out.append('')
    return '\n'.join(out)
if __name__ == '__main__':
    print(plain_text())
