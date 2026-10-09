#!/usr/bin/env python3
"""類似肢グループ出題（2026-10-09）。

未回答の肢のうち、すでに正解している肢とほぼ同じ文言・論点・結論のものを `data/dup_groups.json` にグループ化してある。
グループの代表（members の先頭）を1問だけ出題し、代表に正解したらグループの未回答の肢をまとめて正解（定着）扱いにする。
代表を誤答・「？」にしたときは、その代表だけを記録し、ほかの肢は未回答のまま残す（通常の出題で出る）。

  groupdrill.py status                 残りのグループ数
  groupdrill.py next [-n 5]            次のグループの代表を出題する
  groupdrill.py answer <G番号> <o|x|?>  代表の回答を記録し、正解ならグループをまとめて正解扱いにする
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import drill as D

GROUPS = os.path.join(HERE, 'data', 'dup_groups.json')
STATE = os.path.join(D.LOGDIR, 'group_state.json')


def load_groups():
    return json.load(open(GROUPS, encoding='utf-8'))['groups']


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE, encoding='utf-8'))
    return {'done': {}}   # 群ID → 'all'(まとめて正解) / 'rep_only'(代表のみ記録)


def save_state(s):
    json.dump(s, open(STATE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def pending(groups, state, st):
    out = []
    for g in groups:
        if g['id'] in state['done']:
            continue
        mem = [m for m in g['members'] if m not in st]
        if mem:
            out.append((g, mem))
    return out


def cmd_status(a):
    D.ensure_log_branch()
    st = D.item_state(D.read_log()); state = load_state()
    p = pending(load_groups(), state, st)
    print(f'未出題のグループ {len(p)}（未回答の肢 {sum(len(m) for _, m in p)}）／完了 {len(state["done"])}')


def cmd_next(a):
    D.ensure_log_branch()
    bank = D.load_bank(); st = D.item_state(D.read_log()); state = load_state()
    p = pending(load_groups(), state, st)[:a.n]
    if not p:
        print('出題できるグループがありません。')
        return
    for k, (g, mem) in enumerate(p, 1):
        rep = bank[mem[0]]
        extra = f'、同グループの未回答 {len(mem) - 1}問' if len(mem) > 1 else ''
        print(f'[{k}/{len(p)}] ({g["id"]}・{mem[0]}) 類似肢グループ・{rep["subject"]}／{rep["topic"]}')
        print(f'  {D.stmt_text(rep)}')
        print(f'  （正解済みの類似肢: {", ".join(g["refs"])}{extra}）')
        print()


def cmd_answer(a):
    D.ensure_log_branch()
    bank = D.load_bank(); st = D.item_state(D.read_log()); state = load_state()
    g = next((x for x in load_groups() if x['id'] == a.gid), None)
    if g is None:
        raise SystemExit(f'グループ不明: {a.gid}')
    mem = [m for m in g['members'] if m not in st]
    if not mem:
        raise SystemExit('このグループの肢はすべて回答済みです')
    rep = mem[0]
    # 代表の回答は通常の answer と同じ処理（解説も出す）
    D.cmd_answer(argparse.Namespace(id=rep, ans=a.ans))
    st2 = D.item_state(D.read_log())
    if st2[rep]['last_res'] == 'known' and len(mem) > 1:
        t = D.now().isoformat(timespec='seconds')
        with open(D.LOG, 'a', encoding='utf-8') as f:
            for m in mem[1:]:
                truth = bool(bank[m]['truth'])
                rec = {'t': t, 'id': m, 'ans': 'o' if truth else 'x', 'truth': truth, 'res': 'known', 'group': g['id'], 'via': rep}
                f.write(json.dumps(rec, ensure_ascii=False) + '\n')
        print(f'\n✅ 同じ論点の {len(mem) - 1}問をまとめて正解扱いにしました: {", ".join(mem[1:])}')
        state['done'][g['id']] = 'all'
    elif st2[rep]['last_res'] == 'known':
        state['done'][g['id']] = 'all'
    else:
        if len(mem) > 1:
            print(f'\n（代表のみ記録。同グループの {", ".join(mem[1:])} は未回答のまま残ります）')
        state['done'][g['id']] = 'rep_only'
    save_state(state)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('status').set_defaults(f=cmd_status)
    p = sp.add_parser('next'); p.add_argument('-n', type=int, default=5); p.set_defaults(f=cmd_next)
    p = sp.add_parser('answer'); p.add_argument('gid'); p.add_argument('ans'); p.set_defaults(f=cmd_answer)
    a = ap.parse_args(); a.f(a)


if __name__ == '__main__':
    main()
