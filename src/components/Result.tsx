import type { AnswerResult, Question } from '../types'

type Props = {
  title: string
  results: AnswerResult[]
  onRetryWrong: (questions: Question[]) => void
  onHome: () => void
}

export default function Result({ title, results, onRetryWrong, onHome }: Props) {
  const correct = results.filter((r) => r.isCorrect).length
  const total = results.length
  const pct = total > 0 ? Math.round((correct / total) * 100) : 0
  const wrong = results.filter((r) => !r.isCorrect).map((r) => r.question)

  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <h1 className="mb-1 text-center text-xl font-bold text-slate-800">結果</h1>
      <p className="mb-6 text-center text-sm text-slate-500">{title}</p>

      <div className="mb-6 rounded-2xl bg-white p-6 text-center shadow-sm">
        <div className="text-5xl font-bold text-indigo-600">{pct}%</div>
        <div className="mt-2 text-slate-600">
          {total} 問中 <span className="font-bold text-slate-800">{correct}</span>{' '}
          問 正解
        </div>
      </div>

      {wrong.length > 0 ? (
        <div className="mb-6">
          <h2 className="mb-2 text-sm font-bold text-slate-700">
            間違えた問題（{wrong.length}）
          </h2>
          <ul className="space-y-2">
            {wrong.map((q) => (
              <li
                key={q.id}
                className="rounded-lg bg-white p-3 text-sm text-slate-600 shadow-sm"
              >
                <span className="mr-2 text-xs font-medium text-rose-600">
                  {q.yearLabel} 第{q.questionNo}問
                </span>
                {q.stem.slice(0, 40)}…
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p className="mb-6 text-center text-emerald-600">全問正解！素晴らしい 🎉</p>
      )}

      <div className="space-y-3">
        {wrong.length > 0 && (
          <button
            onClick={() => onRetryWrong(wrong)}
            className="w-full rounded-xl bg-rose-600 py-3 font-semibold text-white hover:bg-rose-700"
          >
            間違いだけもう一度（{wrong.length}問）
          </button>
        )}
        <button
          onClick={onHome}
          className="w-full rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900"
        >
          ホームへ戻る
        </button>
      </div>
    </div>
  )
}
