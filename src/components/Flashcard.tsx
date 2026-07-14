import { useState, type ReactNode } from 'react'
import type { TermCard, KijutsuMark } from '../types'
import { loadFlashcardMarks, setFlashcardMark, type FlashcardMarks } from '../lib/storage'

type Props = {
  title: string
  cards: TermCard[]
  onHome: () => void
}

export default function Flashcard({ title, cards, onHome }: Props) {
  const [index, setIndex] = useState(0)
  const [flipped, setFlipped] = useState(false)
  const [marks, setMarks] = useState<FlashcardMarks>(() => loadFlashcardMarks())

  const card = cards[index]
  const isLast = index === cards.length - 1
  const isFirst = index === 0

  const go = (dir: 1 | -1) => {
    setFlipped(false)
    setIndex((i) => Math.min(cards.length - 1, Math.max(0, i + dir)))
  }

  const mark = (m: KijutsuMark) => {
    setFlashcardMark(card.id, m)
    setMarks({ ...loadFlashcardMarks() })
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-5">
      <div className="mb-3 flex items-center justify-between">
        <button onClick={onHome} className="text-sm text-slate-500 hover:text-slate-700">
          ← メニュー
        </button>
        <span className="text-sm font-medium text-slate-500">
          {index + 1} / {cards.length}
        </span>
      </div>

      <div className="mb-4 h-2 w-full overflow-hidden rounded-full bg-slate-200">
        <div
          className="h-full bg-amber-500 transition-all"
          style={{ width: `${((index + 1) / cards.length) * 100}%` }}
        />
      </div>

      <p className="mb-3 text-xs text-slate-400">{title}</p>

      {/* カード：タップで裏返し */}
      <button
        onClick={() => setFlipped((f) => !f)}
        className="flex min-h-72 w-full flex-col items-center justify-center rounded-2xl bg-white p-6 text-center shadow-sm transition hover:shadow"
      >
        <span className="mb-3 flex flex-wrap items-center justify-center gap-2">
          <span className="rounded-full bg-amber-50 px-2 py-0.5 text-xs font-medium text-amber-700">
            {card.chapter}
          </span>
          {marks[card.id] && (
            <span className={'rounded-full px-2 py-0.5 text-xs font-medium ' + MARK_CLASS[marks[card.id]]}>
              {MARK_LABEL[marks[card.id]]}
            </span>
          )}
        </span>
        {!flipped ? (
          <>
            <span className="text-2xl font-bold text-slate-800">{card.term}</span>
            {card.yomi && (
              <span className="mt-1 text-sm text-slate-400">{card.yomi}</span>
            )}
            <span className="mt-6 text-xs text-slate-400">タップで意味を表示</span>
          </>
        ) : (
          <div className="text-left">
            <p className="text-base font-semibold text-slate-800">{card.term}</p>
            <p className="mt-2 whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
              {card.definition}
            </p>
            {card.cautions && (
              <div className="mt-3 rounded-lg bg-amber-50 p-3 text-sm leading-relaxed text-amber-900">
                <span className="font-bold">⚠ 注意：</span>
                <span className="whitespace-pre-wrap">{card.cautions}</span>
              </div>
            )}
          </div>
        )}
      </button>

      {flipped && (
        <div className="mt-4 rounded-xl bg-white p-4 shadow-sm">
          <p className="mb-3 text-center text-sm font-bold text-slate-600">覚えられた？</p>
          <div className="grid grid-cols-3 gap-2">
            <MarkBtn active={marks[card.id] === 'solved'} color="emerald" onClick={() => mark('solved')}>
              ◯ 覚えた
            </MarkBtn>
            <MarkBtn active={marks[card.id] === 'partial'} color="amber" onClick={() => mark('partial')}>
              △ うろ覚え
            </MarkBtn>
            <MarkBtn active={marks[card.id] === 'failed'} color="rose" onClick={() => mark('failed')}>
              ✗ 忘れた
            </MarkBtn>
          </div>
        </div>
      )}

      <div className="mt-5 flex gap-3">
        <button
          onClick={() => go(-1)}
          disabled={isFirst}
          className="flex-1 rounded-xl bg-white py-3 font-semibold text-slate-700 shadow-sm disabled:text-slate-300"
        >
          ← 前へ
        </button>
        {isLast ? (
          <button
            onClick={onHome}
            className="flex-1 rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900"
          >
            終了
          </button>
        ) : (
          <button
            onClick={() => go(1)}
            className="flex-1 rounded-xl bg-amber-500 py-3 font-semibold text-white hover:bg-amber-600"
          >
            次へ →
          </button>
        )}
      </div>
    </div>
  )
}

const MARK_LABEL: Record<KijutsuMark, string> = {
  solved: '◯ 覚えた',
  partial: '△ うろ覚え',
  failed: '✗ 忘れた',
}
const MARK_CLASS: Record<KijutsuMark, string> = {
  solved: 'bg-emerald-100 text-emerald-700',
  partial: 'bg-amber-100 text-amber-700',
  failed: 'bg-rose-100 text-rose-700',
}

function MarkBtn({
  active,
  color,
  onClick,
  children,
}: {
  active: boolean
  color: 'emerald' | 'amber' | 'rose'
  onClick: () => void
  children: ReactNode
}) {
  const base = {
    emerald: 'border-emerald-500 bg-emerald-50 text-emerald-700',
    amber: 'border-amber-500 bg-amber-50 text-amber-700',
    rose: 'border-rose-500 bg-rose-50 text-rose-700',
  }[color]
  return (
    <button
      onClick={onClick}
      className={
        'rounded-lg border-2 py-2 text-sm font-semibold transition ' +
        (active ? base : 'border-slate-200 bg-white text-slate-500')
      }
    >
      {children}
    </button>
  )
}
