import { useMemo, useState, type ReactNode } from 'react'
import type { AnkiChapter, KijutsuData, OxCard, Question, TermCard } from '../types'
import { overallStats, wrongQuestionIds, dueQuestionIds, resetProgress, subjectStats, yearStats } from '../lib/storage'
import Survey from './Survey'
import Kijutsu from './Kijutsu'

type Props = {
  questions: Question[]
  ankiOx: OxCard[]
  ankiTerms: TermCard[]
  chapters: AnkiChapter[]
  kijutsu: KijutsuData
  onStartTakuitsu: (questions: Question[], title: string) => void
  onStartOx: (cards: OxCard[], title: string) => void
  onStartFlash: (cards: TermCard[], title: string) => void
}

// 配列をシャッフル（元配列は壊さない）
function shuffle<T>(arr: T[]): T[] {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

const SUBJECTS = ['民法', '不動産登記法', '土地家屋調査士法']

export default function Home(props: Props) {
  const [tab, setTab] = useState<'takuitsu' | 'anki' | 'kijutsu' | 'calc'>('takuitsu')
  const [statsKey, setStatsKey] = useState(0)
  const stats = useMemo(() => overallStats(), [statsKey])
  const wrongIds = useMemo(() => wrongQuestionIds(), [statsKey])
  const dueIds = useMemo(() => dueQuestionIds(), [statsKey])

  return (
    <div className="mx-auto max-w-2xl px-4 py-6">
      <header className="mb-4 text-center">
        <h1 className="text-2xl font-bold text-slate-800">
          土地家屋調査士 トレーニング
        </h1>
      </header>

      {/* タブ */}
      <div className="mb-5 flex rounded-xl bg-slate-200 p-1 text-sm font-semibold">
        <TabBtn active={tab === 'takuitsu'} onClick={() => setTab('takuitsu')}>
          択一
        </TabBtn>
        <TabBtn active={tab === 'anki'} onClick={() => setTab('anki')}>
          暗記
        </TabBtn>
        <TabBtn active={tab === 'kijutsu'} onClick={() => setTab('kijutsu')}>
          書式
        </TabBtn>
        <TabBtn active={tab === 'calc'} onClick={() => setTab('calc')}>
          計算
        </TabBtn>
      </div>

      {tab === 'takuitsu' && (
        <TakuitsuPanel
          {...props}
          wrongIds={wrongIds}
          dueIds={dueIds}
          stats={stats}
          onReset={() => {
            if (confirm('学習記録をすべて消去しますか？')) {
              resetProgress()
              setStatsKey((k) => k + 1)
            }
          }}
        />
      )}
      {tab === 'anki' && <AnkiPanel {...props} wrongIds={wrongIds} dueIds={dueIds} />}
      {tab === 'kijutsu' && <Kijutsu data={props.kijutsu} />}
      {tab === 'calc' && <Survey />}
    </div>
  )
}

/* ============ 択一パネル ============ */
function TakuitsuPanel({
  questions,
  onStartTakuitsu,
  wrongIds,
  dueIds,
  stats,
  onReset,
}: Props & {
  wrongIds: Set<string>
  dueIds: Set<string>
  stats: ReturnType<typeof overallStats>
  onReset: () => void
}) {
  const yearList = useMemo(
    () =>
      questions
        .map((q) => ({ code: q.yearCode, label: q.yearLabel }))
        .filter((v, i, arr) => arr.findIndex((x) => x.code === v.code) === i),
    [questions],
  )
  const [year, setYear] = useState(yearList[0]?.code ?? '')
  const wrongQuestions = questions.filter((q) => wrongIds.has(q.id))
  const dueQuestions = questions.filter((q) => dueIds.has(q.id))
  const subjStats = useMemo(() => subjectStats(questions), [questions, stats])
  const yrStats = useMemo(() => yearStats(questions), [questions, stats])

  const startYear = () => {
    const qs = questions
      .filter((q) => q.yearCode === year)
      .sort((a, b) => a.questionNo - b.questionNo)
    onStartTakuitsu(qs, `${qs[0]?.yearLabel ?? year} 択一（${qs.length}問）`)
  }

  return (
    <>
      {dueQuestions.length > 0 && (
        <button
          onClick={() =>
            onStartTakuitsu(shuffle(dueQuestions), `今日の復習（${dueQuestions.length}問）`)
          }
          className="mb-5 flex w-full items-center justify-between rounded-2xl bg-gradient-to-r from-indigo-600 to-violet-600 p-5 text-left text-white shadow-md transition hover:from-indigo-700 hover:to-violet-700"
        >
          <span>
            <span className="block text-lg font-bold">📅 今日の復習</span>
            <span className="text-xs text-indigo-100">
              忘却曲線に沿って最適なタイミングで再出題
            </span>
          </span>
          <span className="shrink-0 text-2xl font-bold">{dueQuestions.length}問 →</span>
        </button>
      )}

      <section className="mb-6 grid grid-cols-3 gap-3">
        <Stat label="解いた問題" value={`${stats.answeredQuestions}`} unit="問" />
        <Stat label="延べ正答率" value={`${stats.accuracy}`} unit="%" />
        <Stat label="今日の復習" value={`${dueQuestions.length}`} unit="問" />
      </section>

      {stats.answeredQuestions > 0 && (
        <Card title="弱点分析">
          <p className="mb-3 text-xs font-semibold text-slate-500">科目別正答率</p>
          <div className="mb-4 space-y-2">
            {subjStats.map((s) => (
              <SubjectBar key={s.subject} label={s.subject} accuracy={s.accuracy} wrongCount={s.wrongCount} />
            ))}
          </div>
          <p className="mb-2 text-xs font-semibold text-slate-500">年度別カバー率（解答済み / 全問）</p>
          <div className="grid grid-cols-2 gap-x-4 gap-y-1">
            {yrStats.map((y) => (
              <YearRow key={y.yearCode} label={y.yearLabel} answered={y.answered} accuracy={y.accuracy} />
            ))}
          </div>
        </Card>
      )}

      <Card title="年度別に解く">
        <div className="flex gap-2">
          <select
            value={year}
            onChange={(e) => setYear(e.target.value)}
            className="flex-1 rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm"
          >
            {yearList.map((y) => (
              <option key={y.code} value={y.code}>
                {y.label}
              </option>
            ))}
          </select>
          <button
            onClick={startYear}
            className="rounded-lg bg-indigo-600 px-5 py-2 text-sm font-semibold text-white hover:bg-indigo-700"
          >
            開始
          </button>
        </div>
      </Card>

      <Card title="分野別に解く">
        <div className="flex flex-wrap gap-2">
          {SUBJECTS.map((s) => {
            const qs = questions.filter((q) => q.subject === s)
            return (
              <PillButton
                key={s}
                onClick={() => onStartTakuitsu(shuffle(qs), `${s}（${qs.length}問）`)}
              >
                {s}
                <span className="ml-1 text-xs text-slate-400">{qs.length}問</span>
              </PillButton>
            )
          })}
        </div>
      </Card>

      <Card title="ランダムに解く">
        <div className="flex flex-wrap gap-2">
          <PillButton onClick={() => onStartTakuitsu(shuffle(questions).slice(0, 10), 'ランダム10問')}>
            10問
          </PillButton>
          <PillButton onClick={() => onStartTakuitsu(shuffle(questions).slice(0, 30), 'ランダム30問')}>
            30問
          </PillButton>
          <PillButton onClick={() => onStartTakuitsu(shuffle(questions), `全${questions.length}問`)}>
            全問
          </PillButton>
        </div>
      </Card>

      <Card title="間違い復習">
        {wrongQuestions.length > 0 ? (
          <button
            onClick={() => onStartTakuitsu(shuffle(wrongQuestions), `間違い復習（${wrongQuestions.length}問）`)}
            className="rounded-lg bg-rose-600 px-5 py-2 text-sm font-semibold text-white hover:bg-rose-700"
          >
            復習する（{wrongQuestions.length}問）
          </button>
        ) : (
          <p className="text-sm text-slate-500">間違えた問題がここに溜まります。</p>
        )}
      </Card>

      <div className="mt-8 text-center">
        <button
          onClick={onReset}
          className="text-xs text-slate-400 underline hover:text-slate-600"
        >
          学習記録をリセット
        </button>
      </div>
    </>
  )
}

/* ============ 暗記パネル ============ */
function AnkiPanel({
  ankiOx,
  ankiTerms,
  chapters,
  onStartOx,
  onStartFlash,
  wrongIds,
  dueIds,
}: Props & { wrongIds: Set<string>; dueIds: Set<string> }) {
  const wrongOx = ankiOx.filter((c) => wrongIds.has(c.id))
  const dueOx = ankiOx.filter((c) => dueIds.has(c.id))

  return (
    <>
      {dueOx.length > 0 && (
        <button
          onClick={() => onStartOx(shuffle(dueOx), `今日の復習（○×${dueOx.length}問）`)}
          className="mb-4 flex w-full items-center justify-between rounded-2xl bg-gradient-to-r from-teal-600 to-emerald-600 p-5 text-left text-white shadow-md transition hover:from-teal-700 hover:to-emerald-700"
        >
          <span>
            <span className="block text-lg font-bold">📅 今日の復習</span>
            <span className="text-xs text-teal-100">忘れる前に間違えた問題を再確認</span>
          </span>
          <span className="shrink-0 text-2xl font-bold">{dueOx.length}問 →</span>
        </button>
      )}

      <Card title="○× 一問一答">
        <div className="mb-3 flex flex-wrap gap-2">
          <PillButton onClick={() => onStartOx(shuffle(ankiOx).slice(0, 20), '○× ランダム20問')}>
            ランダム20問
          </PillButton>
          <PillButton onClick={() => onStartOx(shuffle(ankiOx), `○× 全${ankiOx.length}問`)}>
            全{ankiOx.length}問
          </PillButton>
          {wrongOx.length > 0 && (
            <button
              onClick={() => onStartOx(shuffle(wrongOx), `○× 間違い復習（${wrongOx.length}問）`)}
              className="rounded-lg bg-rose-600 px-4 py-2 text-sm font-semibold text-white hover:bg-rose-700"
            >
              間違い復習 {wrongOx.length}問
            </button>
          )}
        </div>
        <p className="mb-2 text-xs font-medium text-slate-400">章別</p>
        <div className="flex flex-wrap gap-2">
          {chapters.map((ch) => {
            const list = ankiOx.filter((c) => c.chapterId === ch.id)
            if (list.length === 0) return null
            return (
              <PillButton key={ch.id} onClick={() => onStartOx(shuffle(list), `${ch.title}（○×${list.length}問）`)}>
                {ch.title}
                <span className="ml-1 text-xs text-slate-400">{list.length}</span>
              </PillButton>
            )
          })}
        </div>
      </Card>

      <Card title="用語カード">
        <div className="mb-3">
          <PillButton onClick={() => onStartFlash(shuffle(ankiTerms), `用語カード 全${ankiTerms.length}語`)}>
            全{ankiTerms.length}語（シャッフル）
          </PillButton>
        </div>
        <p className="mb-2 text-xs font-medium text-slate-400">章別</p>
        <div className="flex flex-wrap gap-2">
          {chapters.map((ch) => {
            const list = ankiTerms.filter((c) => c.chapterId === ch.id)
            if (list.length === 0) return null
            return (
              <PillButton key={ch.id} onClick={() => onStartFlash(list, `${ch.title}（${list.length}語）`)}>
                {ch.title}
                <span className="ml-1 text-xs text-slate-400">{list.length}</span>
              </PillButton>
            )
          })}
        </div>
      </Card>
    </>
  )
}

/* ============ 小物 ============ */
function Stat({ label, value, unit }: { label: string; value: string; unit: string }) {
  return (
    <div className="rounded-xl bg-white p-3 text-center shadow-sm">
      <div className="text-xs text-slate-500">{label}</div>
      <div className="mt-1 text-2xl font-bold text-slate-800">
        {value}
        <span className="ml-0.5 text-sm font-normal text-slate-400">{unit}</span>
      </div>
    </div>
  )
}

function Card({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section className="mb-4 rounded-xl bg-white p-4 shadow-sm">
      <h2 className="mb-3 text-sm font-bold text-slate-700">{title}</h2>
      {children}
    </section>
  )
}

function TabBtn({
  active,
  onClick,
  children,
}: {
  active: boolean
  onClick: () => void
  children: ReactNode
}) {
  return (
    <button
      onClick={onClick}
      className={
        'flex-1 rounded-lg py-2 transition ' +
        (active ? 'bg-white text-indigo-700 shadow' : 'text-slate-500')
      }
    >
      {children}
    </button>
  )
}

function PillButton({ onClick, children }: { onClick: () => void; children: ReactNode }) {
  return (
    <button
      onClick={onClick}
      className="rounded-lg border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:border-indigo-400 hover:text-indigo-700"
    >
      {children}
    </button>
  )
}

function SubjectBar({ label, accuracy, wrongCount }: { label: string; accuracy: number; wrongCount: number }) {
  const color =
    accuracy >= 80 ? 'bg-emerald-500' : accuracy >= 60 ? 'bg-amber-400' : 'bg-rose-500'
  return (
    <div>
      <div className="mb-1 flex items-center justify-between text-xs">
        <span className="font-medium text-slate-700">{label}</span>
        <span className="text-slate-500">
          {accuracy}%
          {wrongCount > 0 && <span className="ml-2 text-rose-500">要復習 {wrongCount}問</span>}
        </span>
      </div>
      <div className="h-2 w-full overflow-hidden rounded-full bg-slate-100">
        <div className={`h-full rounded-full ${color} transition-all`} style={{ width: `${accuracy}%` }} />
      </div>
    </div>
  )
}

function YearRow({
  label,
  answered,
  accuracy,
}: {
  label: string
  answered: number
  accuracy: number
}) {
  const color = accuracy >= 80 ? 'text-emerald-600' : accuracy >= 60 ? 'text-amber-600' : 'text-rose-600'
  return (
    <div className="flex items-center justify-between text-xs">
      <span className="text-slate-600">{label}</span>
      <span className={`font-semibold ${color}`}>
        {answered > 0 ? `${accuracy}%` : '未解答'}
      </span>
    </div>
  )
}
