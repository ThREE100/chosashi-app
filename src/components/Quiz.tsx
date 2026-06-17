import { useState, type ReactNode } from 'react'
import type { AnswerResult, KaisetsuEntry, Question } from '../types'
import { recordAnswer } from '../lib/storage'

function renderWithTables(text: string): ReactNode[] {
  const lines = text.split('\n')
  const result: ReactNode[] = []
  let i = 0
  let key = 0

  while (i < lines.length) {
    if (lines[i].trimStart().startsWith('|')) {
      // Collect table block
      const tableLines: string[] = []
      while (i < lines.length && lines[i].trimStart().startsWith('|')) {
        tableLines.push(lines[i])
        i++
      }
      // Parse markdown table: header, separator, rows
      const rows = tableLines.filter(l => !/^\|[-| :]+\|$/.test(l.trim()))
      const parseCells = (line: string) =>
        line.replace(/^\||\|$/g, '').split('|').map(c => c.trim())
      const [header, ...body] = rows
      result.push(
        <div key={key++} className="my-2 overflow-x-auto">
          <table className="w-full border-collapse text-[13px]">
            <thead>
              <tr>
                {parseCells(header).map((c, j) => (
                  <th key={j} className="border border-slate-300 bg-slate-100 px-2 py-1 text-left font-semibold text-slate-700">
                    {c}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {body.map((row, ri) => (
                <tr key={ri} className={ri % 2 === 0 ? 'bg-white' : 'bg-slate-50'}>
                  {parseCells(row).map((c, j) => (
                    <td key={j} className="border border-slate-300 px-2 py-1 text-slate-800">
                      {c}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )
    } else {
      // Collect non-table lines
      const textLines: string[] = []
      while (i < lines.length && !lines[i].trimStart().startsWith('|')) {
        textLines.push(lines[i])
        i++
      }
      const block = textLines.join('\n')
      if (block.trim()) {
        result.push(
          <p key={key++} className="whitespace-pre-wrap text-[15px] leading-relaxed text-slate-800">
            {block}
          </p>
        )
      }
    }
  }
  return result
}

type Props = {
  title: string
  questions: Question[]
  kaisetsu?: Record<string, KaisetsuEntry>
  onFinish: (results: AnswerResult[]) => void
  onQuit: () => void
}

export default function Quiz({ title, questions, kaisetsu, onFinish, onQuit }: Props) {
  const [index, setIndex] = useState(0)
  const [selected, setSelected] = useState<number | null>(null)
  const [revealed, setRevealed] = useState(false)
  const [results, setResults] = useState<AnswerResult[]>([])

  const q = questions[index]
  const isLast = index === questions.length - 1

  const submit = () => {
    if (selected === null) return
    const isCorrect = selected === q.correctAnswer
    recordAnswer(q.id, isCorrect)
    setResults((r) => [...r, { question: q, selected, isCorrect }])
    setRevealed(true)
  }

  const next = () => {
    if (isLast) {
      onFinish(results)
      return
    }
    setIndex((i) => i + 1)
    setSelected(null)
    setRevealed(false)
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-5">
      {/* ヘッダー */}
      <div className="mb-3 flex items-center justify-between">
        <button
          onClick={onQuit}
          className="text-sm text-slate-500 hover:text-slate-700"
        >
          ← やめる
        </button>
        <span className="text-sm font-medium text-slate-500">
          {index + 1} / {questions.length}
        </span>
      </div>

      {/* 進捗バー */}
      <div className="mb-4 h-2 w-full overflow-hidden rounded-full bg-slate-200">
        <div
          className="h-full bg-indigo-500 transition-all"
          style={{ width: `${((index + (revealed ? 1 : 0)) / questions.length) * 100}%` }}
        />
      </div>

      <p className="mb-3 text-xs text-slate-400">{title}</p>

      {/* 問題カード */}
      <div className="rounded-xl bg-white p-5 shadow-sm">
        <div className="mb-3 flex flex-wrap gap-2 text-xs">
          <Badge className="bg-slate-100 text-slate-600">{q.yearLabel}</Badge>
          <Badge className="bg-slate-100 text-slate-600">第{q.questionNo}問</Badge>
          <Badge className="bg-indigo-50 text-indigo-700">{q.subject}</Badge>
        </div>

        <div className="mb-1">
          {renderWithTables(q.stem)}
        </div>

        {/* 記述ア〜オ */}
        {q.alts.length > 0 && (
          <ul className="mt-4 space-y-2">
            {q.alts.map((a) => (
              <li
                key={a.label}
                className="rounded-lg bg-slate-50 p-3 text-sm leading-relaxed text-slate-700"
              >
                <span className="mr-1 font-bold text-slate-900">{a.label}</span>
                {a.text}
              </li>
            ))}
          </ul>
        )}

        {/* 選択肢（組合せ 1〜5） */}
        <div className="mt-5 space-y-2">
          {q.combos.map((c) => {
            const isPicked = selected === c.no
            const isAnswer = c.no === q.correctAnswer
            let cls =
              'w-full rounded-lg border px-4 py-3 text-left text-sm transition '
            if (!revealed) {
              cls += isPicked
                ? 'border-indigo-500 bg-indigo-50 text-indigo-800'
                : 'border-slate-200 bg-white hover:border-indigo-300'
            } else if (isAnswer) {
              cls += 'border-emerald-500 bg-emerald-50 text-emerald-800'
            } else if (isPicked) {
              cls += 'border-rose-400 bg-rose-50 text-rose-700'
            } else {
              cls += 'border-slate-200 bg-white text-slate-400'
            }
            return (
              <button
                key={c.no}
                disabled={revealed}
                onClick={() => setSelected(c.no)}
                className={cls}
              >
                <span className="mr-2 font-bold">{c.no}</span>
                {c.text}
              </button>
            )
          })}
        </div>
      </div>

      {/* 解説 */}
      {revealed && (
        <div className="mt-4 rounded-xl bg-white p-5 shadow-sm">
          <p
            className={
              'mb-2 text-lg font-bold ' +
              (selected === q.correctAnswer
                ? 'text-emerald-600'
                : 'text-rose-600')
            }
          >
            {selected === q.correctAnswer ? '◯ 正解' : '✗ 不正解'}
            <span className="ml-2 text-sm font-normal text-slate-500">
              正解は {q.correctAnswer}
            </span>
          </p>
          {q.explanation ? (
            <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
              {q.explanation}
            </p>
          ) : (
            <p className="text-sm text-slate-400">（この問題の解説は未収録です）</p>
          )}
        </div>
      )}

      {/* オリジナル解説（考え方・落とし穴・暗記） */}
      {revealed && kaisetsu?.[q.id] && (
        <div className="mt-3 space-y-2">
          <Tip color="indigo" icon="💡" label="考え方・解き方">
            {kaisetsu[q.id].approach}
          </Tip>
          <Tip color="rose" icon="⚠️" label="間違えやすいポイント">
            {kaisetsu[q.id].pitfalls}
          </Tip>
          <Tip color="emerald" icon="🎯" label="覚えておくべきポイント">
            {kaisetsu[q.id].keyPoints}
          </Tip>
        </div>
      )}

      {/* 操作ボタン */}
      <div className="sticky bottom-0 mt-5 bg-slate-100/80 py-3 backdrop-blur">
        {!revealed ? (
          <button
            onClick={submit}
            disabled={selected === null}
            className="w-full rounded-xl bg-indigo-600 py-3 font-semibold text-white disabled:bg-slate-300"
          >
            解答する
          </button>
        ) : (
          <button
            onClick={next}
            className="w-full rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900"
          >
            {isLast ? '結果を見る' : '次の問題へ →'}
          </button>
        )}
      </div>
    </div>
  )
}

function Badge({
  children,
  className,
}: {
  children: ReactNode
  className: string
}) {
  return (
    <span className={'rounded-full px-2 py-0.5 font-medium ' + className}>
      {children}
    </span>
  )
}

function Tip({
  color,
  icon,
  label,
  children,
}: {
  color: 'indigo' | 'rose' | 'emerald'
  icon: string
  label: string
  children: ReactNode
}) {
  const c = {
    indigo: 'border-indigo-200 bg-indigo-50',
    rose: 'border-rose-200 bg-rose-50',
    emerald: 'border-emerald-200 bg-emerald-50',
  }[color]
  const t = {
    indigo: 'text-indigo-700',
    rose: 'text-rose-700',
    emerald: 'text-emerald-700',
  }[color]
  return (
    <div className={'rounded-xl border p-4 ' + c}>
      <div className={'mb-1 text-xs font-bold ' + t}>
        {icon} {label}
      </div>
      <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
        {children}
      </p>
    </div>
  )
}
