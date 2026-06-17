import { useMemo, useState, type ReactNode } from 'react'
import type { KijutsuData, KijutsuProblem } from '../types'
import {
  loadKijutsuMarks,
  setKijutsuMark,
  type KijutsuMarks,
  getKijutsuReviewedIds,
  markKijutsuReviewed,
} from '../lib/storage'

const BASE = import.meta.env.BASE_URL

const MARK_LABEL: Record<string, string> = {
  solved: '◯ 解けた',
  partial: '△ 惜しい',
  failed: '✗ できなかった',
}
const MARK_CLASS: Record<string, string> = {
  solved: 'bg-emerald-100 text-emerald-700',
  partial: 'bg-amber-100 text-amber-700',
  failed: 'bg-rose-100 text-rose-700',
}

export default function Kijutsu({ data }: { data: KijutsuData }) {
  const [cat, setCat] = useState<'建物' | '土地'>('建物')
  const [openId, setOpenId] = useState<string | null>(null)
  const [marks, setMarks] = useState<KijutsuMarks>(() => loadKijutsuMarks())
  const [reviewed, setReviewed] = useState<Set<string>>(() => getKijutsuReviewedIds())
  const [zoom, setZoom] = useState<string | null>(null)

  const list = useMemo(
    () => data.problems.filter((p) => p.category === cat),
    [data, cat],
  )
  const current = data.problems.find((p) => p.id === openId) || null

  const mark = (id: string, m: 'solved' | 'partial' | 'failed') => {
    setKijutsuMark(id, m)
    setMarks({ ...loadKijutsuMarks() })
  }

  const handleReveal = (id: string) => {
    markKijutsuReviewed(id)
    setReviewed(getKijutsuReviewedIds())
  }

  // ---- 詳細 ----
  if (current) {
    return (
      <>
        <Detail
          p={current}
          mark={marks[current.id]}
          onMark={(m) => mark(current.id, m)}
          onBack={() => setOpenId(null)}
          onZoom={setZoom}
          onReveal={() => handleReveal(current.id)}
        />
        {zoom && <Lightbox src={zoom} onClose={() => setZoom(null)} />}
      </>
    )
  }

  const reviewedCount = list.filter((p) => reviewed.has(p.id)).length

  // ---- 一覧 ----
  return (
    <>
      <p className="mb-3 rounded-lg bg-amber-50 p-3 text-xs leading-relaxed text-amber-800">
        書式は自動採点できません。<b>まず答案用紙（紙）に手書きで挑戦</b>してから模範解答と
        見比べ、自己採点しましょう。
      </p>

      <div className="mb-3 flex items-center justify-between">
        <div className="flex gap-2 text-sm">
          {(['建物', '土地'] as const).map((c) => (
            <button
              key={c}
              onClick={() => setCat(c)}
              className={
                'rounded-lg px-4 py-2 font-semibold transition ' +
                (cat === c ? 'bg-indigo-600 text-white' : 'bg-white text-slate-600 shadow-sm')
              }
            >
              {c}（{data.problems.filter((p) => p.category === c).length}）
            </button>
          ))}
        </div>
        <span className="text-xs text-slate-500">
          解答確認済 <b className="text-slate-700">{reviewedCount}</b> / {list.length}
        </span>
      </div>

      <ul className="space-y-2">
        {list.map((p) => (
          <li key={p.id}>
            <button
              onClick={() => setOpenId(p.id)}
              className="flex w-full items-center justify-between rounded-xl bg-white p-4 text-left shadow-sm hover:shadow"
            >
              <span className="flex flex-wrap items-center gap-1">
                <span className="font-semibold text-slate-800">{p.yearLabel}</span>
                <span className="text-sm text-slate-500">第{p.questionNo}問 {p.category}</span>
                {p.problemImages.length > 0 && (
                  <span className="rounded bg-indigo-50 px-1.5 py-0.5 text-[10px] font-medium text-indigo-600">
                    図面あり
                  </span>
                )}
                {reviewed.has(p.id) && (
                  <span className="rounded bg-slate-100 px-1.5 py-0.5 text-[10px] text-slate-400">
                    確認済
                  </span>
                )}
              </span>
              {marks[p.id] && (
                <span className={'shrink-0 rounded-full px-2 py-0.5 text-xs font-medium ' + MARK_CLASS[marks[p.id]]}>
                  {MARK_LABEL[marks[p.id]]}
                </span>
              )}
            </button>
          </li>
        ))}
      </ul>
    </>
  )
}

/* ---------------- 詳細（問題→模範解答→自己採点） ---------------- */
function Detail({
  p,
  mark,
  onMark,
  onBack,
  onZoom,
  onReveal,
}: {
  p: KijutsuProblem
  mark?: 'solved' | 'partial' | 'failed'
  onMark: (m: 'solved' | 'partial' | 'failed') => void
  onBack: () => void
  onZoom: (src: string) => void
  onReveal: () => void
}) {
  const [revealed, setRevealed] = useState(false)
  const hasProblemImg = p.problemImages.length > 0
  const hasAnswerImg = p.answerImages.length > 0

  return (
    <div>
      <div className="mb-3 flex items-center justify-between">
        <button onClick={onBack} className="text-sm text-slate-500 hover:text-slate-700">
          ← 一覧へ
        </button>
        <span className="text-sm font-medium text-slate-500">
          {p.yearLabel} 第{p.questionNo}問 {p.category}
        </span>
      </div>

      {/* 問題 */}
      <h3 className="mb-2 text-sm font-bold text-slate-700">問題</h3>
      {hasProblemImg ? (
        <div className="space-y-2">
          {p.problemImages.map((src) => (
            <Img key={src} src={BASE + src} onZoom={onZoom} />
          ))}
          <details className="rounded-lg bg-white p-3 text-xs text-slate-500 shadow-sm">
            <summary className="cursor-pointer">問題文テキスト（OCR・補助用）</summary>
            <p className="mt-2 whitespace-pre-wrap leading-relaxed">{p.problemText}</p>
          </details>
        </div>
      ) : (
        <div className="rounded-xl bg-white p-4 shadow-sm">
          <p className="whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
            {p.problemText || '（問題文テキストは未収録です）'}
          </p>
          <p className="mt-3 rounded bg-slate-50 p-2 text-xs text-slate-400">
            ※この年度は図面画像が未収録です。図面は元の問題用紙でご確認ください。
          </p>
        </div>
      )}

      {/* 模範解答 */}
      <div className="mt-6">
        {!revealed ? (
          <button
            onClick={() => { setRevealed(true); onReveal() }}
            className="w-full rounded-xl bg-indigo-600 py-3 font-semibold text-white hover:bg-indigo-700"
          >
            模範解答を見る
          </button>
        ) : (
          <>
            <h3 className="mb-2 text-sm font-bold text-slate-700">模範解答</h3>
            {hasAnswerImg && (
              <div className="mb-2 space-y-2">
                {p.answerImages.map((src) => (
                  <Img key={src} src={BASE + src} onZoom={onZoom} />
                ))}
              </div>
            )}
            {p.modelAnswerText && (
              <details className="rounded-xl bg-white p-4 shadow-sm" open={!hasAnswerImg}>
                <summary className="cursor-pointer text-sm font-medium text-slate-600">
                  解説・解答テキスト
                </summary>
                <p className="mt-2 whitespace-pre-wrap text-sm leading-relaxed text-slate-700">
                  {p.modelAnswerText}
                </p>
              </details>
            )}

            {/* 自己採点 */}
            <div className="mt-5 rounded-xl bg-white p-4 shadow-sm">
              <p className="mb-3 text-center text-sm font-bold text-slate-600">
                自己採点
              </p>
              <div className="grid grid-cols-3 gap-2">
                <MarkBtn active={mark === 'solved'} color="emerald" onClick={() => onMark('solved')}>
                  ◯ 解けた
                </MarkBtn>
                <MarkBtn active={mark === 'partial'} color="amber" onClick={() => onMark('partial')}>
                  △ 惜しい
                </MarkBtn>
                <MarkBtn active={mark === 'failed'} color="rose" onClick={() => onMark('failed')}>
                  ✗ ダメ
                </MarkBtn>
              </div>
            </div>

            <button
              onClick={onBack}
              className="mt-4 w-full rounded-xl bg-slate-800 py-3 font-semibold text-white hover:bg-slate-900"
            >
              一覧へ戻る
            </button>
          </>
        )}
      </div>
    </div>
  )
}

function Img({ src, onZoom }: { src: string; onZoom: (src: string) => void }) {
  return (
    <button
      onClick={() => onZoom(src)}
      className="block w-full overflow-hidden rounded-lg border border-slate-200 bg-white"
      title="タップで拡大"
    >
      <img src={src} alt="" loading="lazy" className="w-full" />
    </button>
  )
}

function Lightbox({ src, onClose }: { src: string; onClose: () => void }) {
  return (
    <div
      onClick={onClose}
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-2"
    >
      <img src={src} alt="" className="max-h-full max-w-full object-contain" />
      <button
        onClick={onClose}
        className="absolute right-4 top-4 rounded-full bg-white/90 px-3 py-1 text-sm font-bold text-slate-700"
      >
        閉じる ✕
      </button>
    </div>
  )
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
