import { useState } from 'react'
import type { OxCard } from '../types'
import { recordAnswer } from '../lib/storage'

type Props = {
  title: string
  cards: OxCard[]
  onHome: () => void
}

export default function OxQuiz({ title, cards, onHome }: Props) {
  const [index, setIndex] = useState(0)
  const [picked, setPicked] = useState<boolean | null>(null)
  const [revealed, setRevealed] = useState(false)
  const [wrong, setWrong] = useState<OxCard[]>([])
  const [correctCount, setCorrectCount] = useState(0)
  const [done, setDone] = useState(false)

  const card = cards[index]
  const isLast = index === cards.length - 1

  const answer = (choice: boolean) => {
    if (revealed) return
    setPicked(choice)
    setRevealed(true)
    const ok = choice === card.correct
    recordAnswer(card.id, ok)
    if (ok) setCorrectCount((c) => c + 1)
    else setWrong((w) => [...w, card])
  }

  const next = () => {
    if (isLast) {
      setDone(true)
      return
    }
    setIndex((i) => i + 1)
    setPicked(null)
    setRevealed(false)
  }

  // 終了画面
  if (done) {
    const total = cards.length
    const pct = Math.round((correctCount / total) * 100)
    return (
      <div className="mx-auto max-w-2xl px-4 py-8">
        <h1 className="mb-1 text-center text-xl font-bold text-slate-800">結果</h1>
        <p className="mb-6 text-center text-sm text-slate-500">{title}</p>
        <div className="mb-6 rounded-2xl bg-white p-6 text-center shadow-sm">
          <div className="text-5xl font-bold text-teal-600">{pct}%</div>
          <div className="mt-2 text-slate-600">
            {total} 問中{' '}
            <span className="font-bold text-slate-800">{correctCount}</span> 問 正解
          </div>
        </div>
        {wrong.length === 0 ? (
          <p className="mb-6 text-center text-emerald-600">全問正解！🎉</p>
        ) : (
          <p className="mb-4 text-center text-sm text-slate-500">
            間違い {wrong.length} 問
          </p>
        )}
        <div className="space-y-3">
          {wrong.length > 0 && (
            <RetryWrong wrong={wrong} title={title} onHome={onHome} />
          )}
          <button
            onClick={onHome}
            className="w-full rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900"
          >
            メニューへ戻る
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-5">
      <div className="mb-3 flex items-center justify-between">
        <button onClick={onHome} className="text-sm text-slate-500 hover:text-slate-700">
          ← やめる
        </button>
        <span className="text-sm font-medium text-slate-500">
          {index + 1} / {cards.length}
        </span>
      </div>

      <div className="mb-4 h-2 w-full overflow-hidden rounded-full bg-slate-200">
        <div
          className="h-full bg-teal-500 transition-all"
          style={{ width: `${((index + (revealed ? 1 : 0)) / cards.length) * 100}%` }}
        />
      </div>

      <p className="mb-3 text-xs text-slate-400">{title}</p>

      <div className="rounded-xl bg-white p-5 shadow-sm">
        <div className="mb-3">
          <span className="rounded-full bg-teal-50 px-2 py-0.5 text-xs font-medium text-teal-700">
            {card.chapter}
          </span>
        </div>
        <p className="text-[15px] leading-relaxed text-slate-800">{card.stem}</p>
        <p className="mt-4 text-center text-sm text-slate-400">
          この記述は正しい？
        </p>

        <div className="mt-3 grid grid-cols-2 gap-3">
          <OxButton
            label="◯ 正しい"
            chosen={picked === true}
            isAnswer={card.correct === true}
            revealed={revealed}
            color="emerald"
            onClick={() => answer(true)}
          />
          <OxButton
            label="✗ 誤り"
            chosen={picked === false}
            isAnswer={card.correct === false}
            revealed={revealed}
            color="rose"
            onClick={() => answer(false)}
          />
        </div>
      </div>

      {revealed && (
        <div className="mt-4 rounded-xl bg-white p-5 shadow-sm">
          <p
            className={
              'mb-2 text-lg font-bold ' +
              (picked === card.correct ? 'text-emerald-600' : 'text-rose-600')
            }
          >
            {picked === card.correct ? '◯ 正解' : '✗ 不正解'}
            <span className="ml-2 text-sm font-normal text-slate-500">
              （答え：{card.correct ? '正しい' : '誤り'}）
            </span>
          </p>
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
            {card.explanation}
          </p>
        </div>
      )}

      <div className="sticky bottom-0 mt-5 bg-slate-100/80 py-3 backdrop-blur">
        <button
          onClick={next}
          disabled={!revealed}
          className="w-full rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900 disabled:bg-slate-300"
        >
          {isLast ? '結果を見る' : '次へ →'}
        </button>
      </div>
    </div>
  )
}

function OxButton({
  label,
  chosen,
  isAnswer,
  revealed,
  color,
  onClick,
}: {
  label: string
  chosen: boolean
  isAnswer: boolean
  revealed: boolean
  color: 'emerald' | 'rose'
  onClick: () => void
}) {
  let cls =
    'rounded-xl border-2 py-5 text-lg font-bold transition '
  if (!revealed) {
    cls +=
      color === 'emerald'
        ? 'border-emerald-200 bg-white text-emerald-700 hover:border-emerald-400'
        : 'border-rose-200 bg-white text-rose-700 hover:border-rose-400'
  } else if (isAnswer) {
    cls += 'border-emerald-500 bg-emerald-50 text-emerald-700'
  } else if (chosen) {
    cls += 'border-rose-400 bg-rose-50 text-rose-600'
  } else {
    cls += 'border-slate-200 bg-white text-slate-300'
  }
  return (
    <button onClick={onClick} disabled={revealed} className={cls}>
      {label}
    </button>
  )
}

// 間違いだけ再挑戦（新しいセッションとして同コンポーネントを描画）
function RetryWrong({
  wrong,
  title,
  onHome,
}: {
  wrong: OxCard[]
  title: string
  onHome: () => void
}) {
  const [retry, setRetry] = useState(false)
  if (retry) {
    return <OxQuiz title={`${title}（間違い直し）`} cards={wrong} onHome={onHome} />
  }
  return (
    <button
      onClick={() => setRetry(true)}
      className="w-full rounded-xl bg-rose-600 py-3 font-semibold text-white hover:bg-rose-700"
    >
      間違いだけもう一度（{wrong.length}問）
    </button>
  )
}
