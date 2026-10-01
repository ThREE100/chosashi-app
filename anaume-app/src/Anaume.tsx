import { Fragment, useEffect, useMemo, useRef, useState, type ReactNode } from 'react'
import type { AnaumeData, AnaumeSet } from './types'
import {
  INTERVAL_LABELS,
  blankId,
  buildBlankIndex,
  computeStates,
  dueBlankIds,
  clearAttempts,
  exportAttemptsJson,
  importAttemptsJson,
  isCorrectAnswer,
  loadAttempts,
  overrideAttempt,
  recordAttempts,
  slotDayLabel,
  slotLabel,
  slotOf,
  type Attempt,
  type BlankState,
} from './anaume'

type View =
  | { name: 'menu' }
  | { name: 'drill'; title: string; mode: 'p' | 'r'; ask: string[] }
  | { name: 'history' }

export default function Anaume({ data }: { data: AnaumeData }) {
  const [attempts, setAttempts] = useState<Attempt[]>(() => loadAttempts())
  const [now, setNow] = useState(() => Date.now())
  const [view, setView] = useState<View>({ name: 'menu' })
  const index = useMemo(() => buildBlankIndex(data), [data])
  const states = useMemo(() => computeStates(attempts), [attempts])
  const nowSlot = slotOf(now)
  const due = useMemo(() => dueBlankIds(states, nowSlot).filter((id) => index[id]), [states, nowSlot, index])

  // 他の端末の履歴を取り込んだら表示を更新する
  useEffect(() => {
    const onSync = () => {
      setAttempts(loadAttempts())
      setNow(Date.now())
    }
    window.addEventListener('anaume-synced', onSync)
    return () => window.removeEventListener('anaume-synced', onSync)
  }, [])

  const backToMenu = () => {
    setAttempts(loadAttempts())
    setNow(Date.now())
    setView({ name: 'menu' })
    window.scrollTo(0, 0)
  }

  if (view.name === 'drill') {
    return (
      <Drill
        key={view.title + view.ask.join()}
        data={data}
        title={view.title}
        mode={view.mode}
        ask={view.ask}
        onRecorded={(list) => setAttempts(list)}
        onBack={backToMenu}
        states={states}
      />
    )
  }
  if (view.name === 'history') {
    return (
      <History
        attempts={attempts}
        states={states}
        index={index}
        nowSlot={nowSlot}
        onBack={backToMenu}
        onChanged={() => {
          setAttempts(loadAttempts())
          setNow(Date.now())
        }}
      />
    )
  }

  const startSet = (set: AnaumeSet) => {
    setView({
      name: 'drill',
      title: `${set.law} ${set.title}`,
      mode: 'p',
      ask: Object.keys(set.blanks).map((n) => blankId(set.id, n)),
    })
    window.scrollTo(0, 0)
  }

  return (
    <Menu
      data={data}
      states={states}
      attempts={attempts}
      nowSlot={nowSlot}
      due={due}
      onStartReview={() => {
        setView({ name: 'drill', title: `${slotLabel(nowSlot)}の復習（${due.length}問）`, mode: 'r', ask: due })
        window.scrollTo(0, 0)
      }}
      onStartSet={startSet}
      onHistory={() => {
        setView({ name: 'history' })
        window.scrollTo(0, 0)
      }}
    />
  )
}

/* ============ メニュー ============ */
function Menu({
  data,
  states,
  attempts,
  nowSlot,
  due,
  onStartReview,
  onStartSet,
  onHistory,
}: {
  data: AnaumeData
  states: Record<string, BlankState>
  attempts: Attempt[]
  nowSlot: number
  due: string[]
  onStartReview: () => void
  onStartSet: (s: AnaumeSet) => void
  onHistory: () => void
}) {
  const reviewList = Object.values(states).filter((s) => s.need > 0)
  const needTotal = reviewList.reduce((sum, s) => sum + s.need, 0)
  const isMorning = nowSlot % 2 === 0

  // 今後の回ごとの予定数
  const upcoming: { slot: number; n: number }[] = []
  for (let k = 1; k <= 4; k++) {
    const slot = nowSlot + k
    upcoming.push({ slot, n: reviewList.filter((s) => s.due === slot).length })
  }

  // 直近7日の復習の実施状況(回ごとの復習の解答数)
  const reviewBySlot = new Map<number, { n: number; ok: number }>()
  for (const a of attempts) {
    if (a.m !== 'r') continue
    const slot = slotOf(a.t)
    const r = reviewBySlot.get(slot) ?? { n: 0, ok: 0 }
    r.n += 1
    r.ok += a.c
    reviewBySlot.set(slot, r)
  }
  const todayAm = nowSlot - (nowSlot % 2)
  const days = Array.from({ length: 7 }, (_, i) => todayAm - i * 2)

  const laws = [...new Set(data.sets.map((s) => s.law))]

  return (
    <div>
      {/* 今の回の復習 */}
      <section className="mb-4 rounded-xl bg-white p-4 shadow-sm">
        <div className="mb-2 flex items-baseline justify-between">
          <h2 className="text-sm font-bold text-slate-700">
            今日の復習 <span className="text-indigo-600">{isMorning ? '朝の回' : '夜の回'}</span>
          </h2>
          <span className="text-xs text-slate-400">朝 0〜12時 ／ 夜 12〜24時</span>
        </div>
        {due.length > 0 ? (
          <button
            onClick={onStartReview}
            className="w-full rounded-lg bg-rose-600 px-4 py-3 text-base font-bold text-white hover:bg-rose-700"
          >
            {isMorning ? '朝' : '夜'}の復習を始める（{due.length}問）
          </button>
        ) : (
          <p className="rounded-lg bg-emerald-50 px-3 py-3 text-center text-sm font-semibold text-emerald-700">
            {reviewBySlot.has(nowSlot) ? 'この回の復習は完了しました' : 'この回に復習する問題はありません'}
          </p>
        )}
        <div className="mt-3 grid grid-cols-4 gap-2 text-center text-xs">
          {upcoming.map((u) => (
            <div key={u.slot} className="rounded-lg bg-slate-50 p-2">
              <div className="text-slate-400">{slotLabel(u.slot)}</div>
              <div className="font-bold text-slate-700">{u.n}問</div>
            </div>
          ))}
        </div>
        <p className="mt-3 text-xs leading-relaxed text-slate-500">
          復習リスト：<b className="text-slate-700">{reviewList.length}問</b>
          （消えるまでに必要な正解 あと{needTotal}回）。間違えた回数と同じ回数だけ正解すると消えます。
          出題間隔は忘却曲線に合わせて {INTERVAL_LABELS.join(' → ')} と延びます。
        </p>
      </section>

      {/* 直近7日の復習記録 */}
      <section className="mb-4 rounded-xl bg-white p-4 shadow-sm">
        <h2 className="mb-2 text-sm font-bold text-slate-700">復習の記録（直近7日・朝／夜）</h2>
        <div className="grid grid-cols-7 gap-1 text-center text-[11px]">
          {[...days].reverse().map((am) => (
            <div key={am}>
              <div className="mb-1 text-slate-400">{slotDayLabel(am).replace(/\(.\)/, '')}</div>
              {[am, am + 1].map((slot) => {
                const r = reviewBySlot.get(slot)
                const future = slot > nowSlot
                return (
                  <div
                    key={slot}
                    className={`mb-1 rounded py-1 ${
                      r ? 'bg-emerald-100 text-emerald-700' : future ? 'bg-slate-50 text-slate-300' : 'bg-slate-100 text-slate-400'
                    }`}
                    title={slotLabel(slot)}
                  >
                    {slot % 2 === 0 ? '朝' : '夜'}
                    {r ? ` ${r.ok}/${r.n}` : ''}
                  </div>
                )
              })}
            </div>
          ))}
        </div>
      </section>

      {/* セット一覧 */}
      {laws.map((law) => (
        <section key={law} className="mb-4 rounded-xl bg-white p-4 shadow-sm">
          <h2 className="mb-2 text-sm font-bold text-slate-700">{law}</h2>
          <div className="flex flex-col gap-2">
            {data.sets
              .filter((s) => s.law === law)
              .map((s) => {
                const ids = Object.keys(s.blanks).map((n) => blankId(s.id, n))
                let c = 0
                let w = 0
                let rev = 0
                let tried = 0
                for (const id of ids) {
                  const st = states[id]
                  if (!st) continue
                  tried += 1
                  c += st.correct
                  w += st.wrong
                  if (st.need > 0) rev += 1
                }
                const acc = c + w > 0 ? Math.round((c / (c + w)) * 100) : null
                return (
                  <button
                    key={s.id}
                    onClick={() => onStartSet(s)}
                    className="flex items-center justify-between rounded-lg border border-slate-200 px-3 py-2 text-left hover:border-indigo-400"
                  >
                    <span>
                      <span className="block text-sm font-semibold text-slate-800">{s.title}</span>
                      {s.articles.length > 1 && (
                        <span className="block text-xs text-slate-400">
                          {s.articles.map((a) => a.heading.replace(/（.*$/, '')).join('・')}
                        </span>
                      )}
                    </span>
                    <span className="ml-2 shrink-0 text-right text-xs text-slate-500">
                      {ids.length}問
                      <br />
                      {acc === null ? '未着手' : `正答率${acc}%`}
                      {tried > 0 && tried < ids.length && `・${tried}問済`}
                      {rev > 0 && <span className="ml-1 font-bold text-rose-600">要復習{rev}</span>}
                    </span>
                  </button>
                )
              })}
          </div>
        </section>
      ))}

      <button
        onClick={onHistory}
        className="w-full rounded-lg border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:border-indigo-400 hover:text-indigo-700"
      >
        正誤の履歴・復習リストを見る
      </button>
      <p className="mt-3 text-[11px] leading-relaxed text-slate-400">{data.meta.note}</p>
    </div>
  )
}

/* ============ 演習・復習画面 ============ */
function Drill({
  data,
  title,
  mode,
  ask,
  states,
  onRecorded,
  onBack,
}: {
  data: AnaumeData
  title: string
  mode: 'p' | 'r'
  ask: string[]
  states: Record<string, BlankState>
  onRecorded: (list: Attempt[]) => void
  onBack: () => void
}) {
  const askSet = useMemo(() => new Set(ask), [ask])
  const [inputs, setInputs] = useState<Record<string, string>>({})
  const [graded, setGraded] = useState<{ t: number; result: Record<string, boolean> } | null>(null)
  const [overridden, setOverridden] = useState<Set<string>>(new Set())
  const [showBank, setShowBank] = useState(false)
  const inputRefs = useRef<Map<string, HTMLInputElement>>(new Map())

  // 出題する条文(復習では、出題する空欄を含む条文だけ)
  const blocks = useMemo(() => {
    const out: { set: AnaumeSet; articles: AnaumeSet['articles'] }[] = []
    for (const set of data.sets) {
      const arts = set.articles.filter((a) =>
        [...a.text.matchAll(/\{(\d+)\}/g)].some((m) => askSet.has(blankId(set.id, m[1]))),
      )
      if (arts.length) out.push({ set, articles: arts })
    }
    return out
  }, [data, askSet])

  // 入力欄の並び順(最初に出てくる位置に入力欄を置く)
  const order = useMemo(() => {
    const seen: string[] = []
    for (const { set, articles } of blocks) {
      for (const a of articles) {
        for (const m of a.text.matchAll(/\{(\d+)\}/g)) {
          const id = blankId(set.id, m[1])
          if (askSet.has(id) && !seen.includes(id)) seen.push(id)
        }
      }
    }
    return seen
  }, [blocks, askSet])

  const answerOf = (id: string) => {
    const i = id.lastIndexOf('-')
    const set = data.sets.find((s) => s.id === id.slice(0, i))
    return set?.blanks[id.slice(i + 1)]
  }

  const grade = () => {
    const empty = order.filter((id) => !(inputs[id] ?? '').trim()).length
    if (empty > 0 && !confirm(`未入力が${empty}問あります。不正解として採点しますか？`)) return
    const result: Record<string, boolean> = {}
    const items: Omit<Attempt, 't'>[] = []
    for (const id of order) {
      const b = answerOf(id)
      const ok = !!b && isCorrectAnswer(inputs[id] ?? '', b.answer, b.alt)
      result[id] = ok
      items.push({ b: id, c: ok ? 1 : 0, a: (inputs[id] ?? '').trim(), m: mode })
    }
    const list = recordAttempts(items)
    setGraded({ t: list[list.length - 1]?.t ?? Date.now(), result })
    onRecorded(list)
  }

  const override = (id: string) => {
    if (!graded) return
    const list = overrideAttempt(graded.t, id)
    setOverridden(new Set(overridden).add(id))
    onRecorded(list)
  }

  const okCount = graded ? order.filter((id) => graded.result[id] || overridden.has(id)).length : 0

  const bank = useMemo(() => {
    const words = order.map((id) => answerOf(id)?.answer ?? '')
    // 表示のたびに並びが変わらないよう、決まった順に混ぜる
    return [...new Set(words)].sort((a, b) => hash(a) - hash(b))
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [order])

  const focusNext = (id: string) => {
    const i = order.indexOf(id)
    const next = order[i + 1]
    if (next) inputRefs.current.get(next)?.focus()
    else inputRefs.current.get(id)?.blur()
  }

  const renderText = (set: AnaumeSet, text: string, rendered: Set<string>) => {
    const parts = text.split(/\{(\d+)\}/)
    return parts.map((p, i) => {
      if (i % 2 === 0) return <Fragment key={i}>{p}</Fragment>
      const id = blankId(set.id, p)
      const b = set.blanks[p]
      if (!askSet.has(id)) {
        // 復習で出題しない空欄は答えを表示しておく
        return (
          <span key={i} className="mx-0.5 border-b border-slate-300 px-0.5 text-slate-500">
            {b.answer}
          </span>
        )
      }
      const ok = graded ? graded.result[id] || overridden.has(id) : null
      if (rendered.has(id)) {
        // 同じ番号の2回目以降は、入力欄を置かずに参照だけ表示
        return (
          <span
            key={i}
            className={`mx-0.5 rounded px-1 text-sm ${
              ok === null ? 'bg-indigo-50 text-indigo-700' : ok ? 'bg-emerald-50 text-emerald-700' : 'bg-rose-50 text-rose-700'
            }`}
          >
            （{p}）{graded ? b.answer : inputs[id] || ''}
          </span>
        )
      }
      rendered.add(id)
      const width = Math.min(Math.max(b.answer.length + 1.5, 4), 22)
      return (
        <span key={i} className="mx-0.5 inline-block align-baseline">
          <span className="mr-0.5 text-[10px] font-bold text-indigo-500">{p}</span>
          <input
            ref={(el) => {
              if (el) inputRefs.current.set(id, el)
              else inputRefs.current.delete(id)
            }}
            value={inputs[id] ?? ''}
            disabled={!!graded}
            onChange={(e) => setInputs({ ...inputs, [id]: e.target.value })}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.nativeEvent.isComposing) {
                e.preventDefault()
                focusNext(id)
              }
            }}
            enterKeyHint="next"
            autoComplete="off"
            autoCapitalize="off"
            spellCheck={false}
            style={{ width: `${width}em`, maxWidth: '100%' }}
            className={`rounded border px-1 py-0.5 text-base ${
              ok === null
                ? 'border-indigo-300 bg-indigo-50/40 focus:border-indigo-600 focus:outline-none'
                : ok
                  ? 'border-emerald-400 bg-emerald-50 text-emerald-800'
                  : 'border-rose-400 bg-rose-50 text-rose-800 line-through'
            }`}
          />
          {graded && !ok && <span className="ml-1 font-bold text-rose-700">{b.answer}</span>}
        </span>
      )
    })
  }

  const rendered = new Set<string>()

  return (
    <div>
      <div className="mb-3 flex items-center justify-between">
        <button onClick={onBack} className="text-sm text-slate-500 hover:text-slate-700">
          ← もどる
        </button>
        <span className="text-xs text-slate-400">{mode === 'r' ? '復習' : '演習'}・{order.length}問</span>
      </div>
      <h2 className="mb-3 text-base font-bold text-slate-800">{title}</h2>

      {!graded && (
        <div className="mb-3">
          <button
            onClick={() => setShowBank(!showBank)}
            className="text-xs text-indigo-600 underline hover:text-indigo-800"
          >
            {showBank ? 'ヒント（語群）を隠す' : 'ヒント（語群）を表示'}
          </button>
          {showBank && (
            <div className="mt-2 flex flex-wrap gap-1.5 rounded-lg bg-amber-50 p-2">
              {bank.map((w) => (
                <span key={w} className="rounded bg-white px-2 py-0.5 text-xs text-slate-700 shadow-sm">
                  {w}
                </span>
              ))}
            </div>
          )}
        </div>
      )}

      {blocks.map(({ set, articles }) => (
        <section key={set.id} className="mb-4 rounded-xl bg-white p-4 shadow-sm">
          {mode === 'r' && <p className="mb-2 text-xs font-bold text-slate-400">{set.law}</p>}
          {articles.map((a) => (
            <div key={a.heading} className="mb-4 last:mb-0">
              <h3 className="mb-1 text-sm font-bold text-slate-700">{a.heading}</h3>
              <div className="space-y-1 text-[15px] leading-9 text-slate-800">
                {a.text.split('\n').map((line, li) => (
                  <p key={li} className={/^[一二三四五六七八九十]+\u3000|^\d\u3000/.test(line) ? 'pl-4 -indent-4' : 'indent-4'}>
                    {renderText(set, line, rendered)}
                  </p>
                ))}
              </div>
            </div>
          ))}
        </section>
      ))}

      {!graded ? (
        <button
          onClick={grade}
          className="sticky bottom-3 w-full rounded-lg bg-indigo-600 px-4 py-3 text-base font-bold text-white shadow-lg hover:bg-indigo-700"
        >
          採点する
        </button>
      ) : (
        <section className="rounded-xl bg-white p-4 shadow-sm">
          <p className="mb-2 text-center text-lg font-bold text-slate-800">
            {okCount} / {order.length} 正解
          </p>
          {order.some((id) => !graded.result[id]) && (
            <div className="mb-3">
              <p className="mb-1 text-xs text-slate-500">
                間違えた問題（表記の違いだけで意味が同じなら「正解扱い」にできます）
              </p>
              <ul className="divide-y divide-slate-100 text-sm">
                {order
                  .filter((id) => !graded.result[id])
                  .map((id) => {
                    const b = answerOf(id)
                    const st = states[id]
                    return (
                      <li key={id} className="flex items-center justify-between gap-2 py-1.5">
                        <span>
                          <span className="text-xs text-indigo-500">（{id.slice(id.lastIndexOf('-') + 1)}）</span>
                          <b className="text-slate-800">{b?.answer}</b>
                          <span className="ml-2 text-xs text-slate-400">入力：{inputs[id]?.trim() || '（空欄）'}</span>
                          {!overridden.has(id) && st && (
                            <span className="ml-2 text-xs text-rose-600">
                              間違い通算{st.wrong}回 → あと{st.need}回正解で復習リストから消えます
                            </span>
                          )}
                        </span>
                        {overridden.has(id) ? (
                          <span className="shrink-0 text-xs font-semibold text-emerald-600">正解扱い済</span>
                        ) : (
                          <button
                            onClick={() => override(id)}
                            className="shrink-0 rounded border border-slate-300 px-2 py-0.5 text-xs text-slate-600 hover:border-emerald-500 hover:text-emerald-700"
                          >
                            正解扱いにする
                          </button>
                        )}
                      </li>
                    )
                  })}
              </ul>
            </div>
          )}
          <div className="flex gap-2">
            {mode === 'p' && (
              <button
                onClick={() => {
                  setInputs({})
                  setGraded(null)
                  setOverridden(new Set())
                  window.scrollTo(0, 0)
                }}
                className="flex-1 rounded-lg border border-slate-300 px-4 py-2 text-sm font-semibold text-slate-700 hover:border-indigo-400"
              >
                もう一度解く
              </button>
            )}
            <button
              onClick={onBack}
              className="flex-1 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700"
            >
              メニューへ
            </button>
          </div>
        </section>
      )}
    </div>
  )
}

function hash(s: string): number {
  let h = 0
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0
  return h
}

/* ============ 履歴 ============ */
function History({
  attempts,
  states,
  index,
  nowSlot,
  onBack,
  onChanged,
}: {
  attempts: Attempt[]
  states: Record<string, BlankState>
  index: ReturnType<typeof buildBlankIndex>
  nowSlot: number
  onBack: () => void
  onChanged: () => void
}) {
  const fileRef = useRef<HTMLInputElement>(null)
  const [tab, setTab] = useState<'review' | 'log' | 'days'>('review')
  const total = attempts.length
  const ok = attempts.filter((a) => a.c).length

  const reviewRows = Object.entries(states)
    .filter(([id, s]) => s.need > 0 && index[id])
    .sort((a, b) => (a[1].due ?? 0) - (b[1].due ?? 0))

  const byDay = new Map<number, { n: number; ok: number; r: number }>()
  for (const a of attempts) {
    const day = Math.floor(slotOf(a.t) / 2)
    const d = byDay.get(day) ?? { n: 0, ok: 0, r: 0 }
    d.n += 1
    d.ok += a.c
    if (a.m === 'r') d.r += 1
    byDay.set(day, d)
  }
  const dayRows = [...byDay.entries()].sort((a, b) => b[0] - a[0])
  const recent = [...attempts].sort((a, b) => b.t - a.t).slice(0, 200)

  const download = () => {
    const blob = new Blob([exportAttemptsJson()], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `anaume_history_${new Date().toISOString().slice(0, 10)}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <div>
      <div className="mb-3 flex items-center justify-between">
        <button onClick={onBack} className="text-sm text-slate-500 hover:text-slate-700">
          ← もどる
        </button>
        <span className="flex gap-3">
          <button onClick={download} className="text-xs text-indigo-600 underline">
            履歴を書き出す
          </button>
          <button onClick={() => fileRef.current?.click()} className="text-xs text-indigo-600 underline">
            読み込む
          </button>
        </span>
        <input
          ref={fileRef}
          type="file"
          accept="application/json,.json"
          className="hidden"
          onChange={async (e) => {
            const f = e.target.files?.[0]
            e.target.value = ''
            if (!f) return
            try {
              const n = importAttemptsJson(await f.text())
              alert(`${n}件の履歴を追加しました`)
              onChanged()
            } catch {
              alert('読み込めませんでした（書き出したJSONファイルを選んでください）')
            }
          }}
        />
      </div>
      <p className="mb-3 text-[11px] leading-relaxed text-slate-400">
        履歴はこの端末のブラウザに保存されます。機種変更や別の端末で続けるときは「書き出す」で保存したファイルを、
        続ける端末で「読み込む」と、両方の履歴を足し合わせて復習リストを計算し直します。
      </p>
      <section className="mb-4 grid grid-cols-3 gap-2 text-center">
        <Stat label="解答数（延べ）" value={`${total}`} />
        <Stat label="正答率" value={total ? `${Math.round((ok / total) * 100)}%` : '—'} />
        <Stat label="復習リスト" value={`${reviewRows.length}問`} />
      </section>

      <div className="mb-3 flex rounded-xl bg-slate-200 p-1 text-xs font-semibold">
        {(
          [
            ['review', '復習リスト'],
            ['log', '解答履歴'],
            ['days', '日別'],
          ] as const
        ).map(([k, label]) => (
          <button
            key={k}
            onClick={() => setTab(k)}
            className={`flex-1 rounded-lg py-1.5 ${tab === k ? 'bg-white text-indigo-700 shadow-sm' : 'text-slate-600'}`}
          >
            {label}
          </button>
        ))}
      </div>

      {tab === 'review' && (
        <Card>
          {reviewRows.length === 0 ? (
            <p className="text-center text-sm text-slate-400">復習リストは空です</p>
          ) : (
            <ul className="divide-y divide-slate-100 text-sm">
              {reviewRows.map(([id, s]) => {
                const info = index[id]
                const overdue = (s.due ?? 0) <= nowSlot
                return (
                  <li key={id} className="py-2">
                    <div className="flex justify-between gap-2">
                      <span className="text-xs text-slate-400">
                        {info.set.law} {info.heading}（{info.num}）
                      </span>
                      <span className={`shrink-0 text-xs font-semibold ${overdue ? 'text-rose-600' : 'text-slate-500'}`}>
                        {overdue ? '今の回で出題' : `次回 ${slotLabel(s.due ?? 0)}`}
                      </span>
                    </div>
                    <div className="flex justify-between gap-2">
                      <b className="text-slate-800">{info.answer}</b>
                      <span className="shrink-0 text-xs text-slate-500">
                        間違い{s.wrong}回・あと<b className="text-rose-600">{s.need}</b>回正解
                      </span>
                    </div>
                  </li>
                )
              })}
            </ul>
          )}
        </Card>
      )}

      {tab === 'log' && (
        <Card>
          {recent.length === 0 ? (
            <p className="text-center text-sm text-slate-400">まだ解答がありません</p>
          ) : (
            <ul className="divide-y divide-slate-100 text-sm">
              {recent.map((a) => {
                const info = index[a.b]
                const d = new Date(a.t)
                return (
                  <li key={`${a.t}-${a.b}`} className="flex items-start gap-2 py-1.5">
                    <span className={`w-5 shrink-0 font-bold ${a.c ? 'text-emerald-600' : 'text-rose-600'}`}>
                      {a.c ? '○' : '×'}
                    </span>
                    <span className="flex-1">
                      <span className="block text-xs text-slate-400">
                        {d.getMonth() + 1}/{d.getDate()} {String(d.getHours()).padStart(2, '0')}:
                        {String(d.getMinutes()).padStart(2, '0')} {a.m === 'r' ? '復習' : '演習'}・
                        {info ? `${info.set.law} ${info.heading}（${info.num}）` : a.b}
                      </span>
                      <span className="text-slate-800">{info?.answer}</span>
                      {(!a.c || a.o) && (
                        <span className="ml-2 text-xs text-slate-400">
                          入力：{a.a || '（空欄）'}
                          {a.o ? '（正解扱い）' : ''}
                        </span>
                      )}
                    </span>
                  </li>
                )
              })}
            </ul>
          )}
        </Card>
      )}

      {tab === 'days' && (
        <Card>
          {dayRows.length === 0 ? (
            <p className="text-center text-sm text-slate-400">まだ解答がありません</p>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="text-xs text-slate-400">
                  <th className="py-1 text-left">日付</th>
                  <th className="text-right">解答</th>
                  <th className="text-right">うち復習</th>
                  <th className="text-right">正答率</th>
                </tr>
              </thead>
              <tbody>
                {dayRows.map(([day, d]) => (
                  <tr key={day} className="border-t border-slate-100">
                    <td className="py-1">{slotDayLabel(day * 2)}</td>
                    <td className="text-right">{d.n}</td>
                    <td className="text-right">{d.r}</td>
                    <td className="text-right">{Math.round((d.ok / d.n) * 100)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </Card>
      )}

      <button
        onClick={() => {
          if (confirm('この端末の履歴をすべて消去しますか？（元に戻せません。先に書き出しておくと安全です）')) {
            clearAttempts()
            onChanged()
          }
        }}
        className="mt-6 w-full text-xs text-slate-400 underline hover:text-rose-600"
      >
        履歴をすべて消去
      </button>
    </div>
  )
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl bg-white p-3 shadow-sm">
      <div className="text-lg font-bold text-slate-800">{value}</div>
      <div className="text-[11px] text-slate-500">{label}</div>
    </div>
  )
}

function Card({ children }: { children: ReactNode }) {
  return <section className="rounded-xl bg-white p-4 shadow-sm">{children}</section>
}
