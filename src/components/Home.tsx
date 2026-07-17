import { useMemo, useState, type ReactNode } from 'react'
import type { AnkiChapter, KijutsuData, OxCard, Question, TermCard } from '../types'
import {
  overallStats,
  wrongQuestionIds,
  dueQuestionIds,
  resetProgress,
  subjectStats,
  yearStats,
  genreStats,
  getTodayStudy,
  addStudyMinutes,
  weekStudyMinutes,
  totalStudyMinutes,
  studyStreak,
  studyHeatmap,
  studyAccuracyTrend,
  loadKijutsuMarks,
  loadFlashcardMarks,
  buildProgressSummaryText,
} from '../lib/storage'
import { supabase } from '../lib/supabase'
import Survey from './Survey'
import Kijutsu from './Kijutsu'

type Props = {
  questions: Question[]
  ankiOx: OxCard[]
  ankiTerms: TermCard[]
  chapters: AnkiChapter[]
  kijutsu: KijutsuData
  userEmail?: string
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
  const [tab, setTab] = useState<'takuitsu' | 'anki' | 'kijutsu' | 'calc' | 'log'>('takuitsu')
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

      <StudyStrip />

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
        <TabBtn active={tab === 'log'} onClick={() => setTab('log')}>
          記録
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
      {tab === 'log' && (
        <LogPanel
          questions={props.questions}
          kijutsu={props.kijutsu}
          dueCount={dueIds.size}
          onGotoKijutsu={() => setTab('kijutsu')}
        />
      )}

      {/* アカウント */}
      <div className="mt-10 flex flex-col items-center gap-1 border-t border-slate-200 pt-5">
        {props.userEmail && (
          <p className="text-xs text-slate-400">{props.userEmail} でログイン中</p>
        )}
        <button
          onClick={() => supabase.auth.signOut()}
          className="text-xs text-slate-400 underline hover:text-slate-600"
        >
          ログアウト
        </button>
      </div>
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
  const genreAgg = useMemo(() => genreStats(questions), [questions, stats])
  const weakGenres = useMemo(
    () =>
      genreAgg
        .filter((g) => g.answered >= 3)
        .sort((a, b) => a.accuracy - b.accuracy)
        .slice(0, 5),
    [genreAgg],
  )

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

          {weakGenres.length > 0 && (
            <>
              <p className="mb-3 mt-4 text-xs font-semibold text-slate-500">
                弱点ジャンルTOP5（3回以上解答したジャンルのみ）
              </p>
              <div className="space-y-2">
                {weakGenres.map((g) => (
                  <SubjectBar key={g.genre} label={g.genre} accuracy={g.accuracy} wrongCount={g.wrongCount} />
                ))}
              </div>
            </>
          )}
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

      <Card title="苦手をまとめて復習">
        <p className="mb-3 text-xs text-slate-500">
          復習日に関係なく、直近で間違えた問題をすべて出題します。
        </p>
        {wrongQuestions.length > 0 ? (
          <button
            onClick={() => onStartTakuitsu(shuffle(wrongQuestions), `苦手復習（${wrongQuestions.length}問）`)}
            className="rounded-lg bg-rose-600 px-5 py-2 text-sm font-semibold text-white hover:bg-rose-700"
          >
            まとめて復習（{wrongQuestions.length}問）
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
              onClick={() => onStartOx(shuffle(wrongOx), `○× 苦手復習（${wrongOx.length}問）`)}
              className="rounded-lg bg-rose-600 px-4 py-2 text-sm font-semibold text-white hover:bg-rose-700"
            >
              苦手をまとめて {wrongOx.length}問
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

/* ============ 今日の学習 ストリップ ============ */
const DAILY_TARGET_MIN = 120

function StudyStrip() {
  const [tick, setTick] = useState(0)
  const bump = () => setTick((t) => t + 1)

  const today = useMemo(() => getTodayStudy(), [tick])
  const streak = useMemo(() => studyStreak(), [tick])
  const weekMin = useMemo(() => weekStudyMinutes(), [tick])
  const totalMin = useMemo(() => totalStudyMinutes(), [tick])
  const heat = useMemo(() => studyHeatmap(5), [tick])
  const pct = Math.min(100, Math.round((today.min / DAILY_TARGET_MIN) * 100))

  return (
    <section className="mb-5 rounded-xl bg-white p-4 shadow-sm">
      <div className="mb-2 flex items-center justify-between">
        <h2 className="text-sm font-bold text-slate-700">今日の学習</h2>
        {streak > 0 && (
          <span className="text-xs font-semibold text-amber-600">🔥 {streak}日連続</span>
        )}
      </div>

      <div className="mb-2 flex items-baseline gap-1">
        <span className="text-2xl font-bold text-slate-800">{today.min}</span>
        <span className="text-xs text-slate-400">/ {DAILY_TARGET_MIN}分</span>
      </div>
      <div className="mb-3 h-2 w-full overflow-hidden rounded-full bg-slate-100">
        <div
          className="h-full rounded-full bg-indigo-500 transition-all"
          style={{ width: `${pct}%` }}
        />
      </div>

      <div className="mb-3 flex flex-wrap gap-2">
        <TimeBtn
          label="−15"
          onClick={() => {
            addStudyMinutes(-15)
            bump()
          }}
        />
        <TimeBtn
          label="+15"
          onClick={() => {
            addStudyMinutes(15)
            bump()
          }}
        />
        <TimeBtn
          label="+30"
          onClick={() => {
            addStudyMinutes(30)
            bump()
          }}
        />
        <TimeBtn
          label="+60"
          onClick={() => {
            addStudyMinutes(60)
            bump()
          }}
        />
      </div>

      <div className="mb-3 grid grid-cols-2 gap-3">
        <div className="rounded-lg bg-slate-50 p-2 text-center">
          <div className="text-xs text-slate-500">今週</div>
          <div className="text-lg font-bold text-slate-800">
            {weekMin}
            <span className="ml-0.5 text-xs font-normal text-slate-400">分</span>
          </div>
        </div>
        <div className="rounded-lg bg-slate-50 p-2 text-center">
          <div className="text-xs text-slate-500">累計</div>
          <div className="text-lg font-bold text-slate-800">
            {totalMin}
            <span className="ml-0.5 text-xs font-normal text-slate-400">分</span>
          </div>
        </div>
      </div>

      <Heatmap days={heat} />
    </section>
  )
}

function TimeBtn({ label, onClick }: { label: string; onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="rounded-lg border border-slate-300 bg-white px-3 py-1.5 text-xs font-semibold text-slate-600 hover:border-indigo-400 hover:text-indigo-700"
    >
      {label}分
    </button>
  )
}

function Heatmap({ days }: { days: { date: string; min: number; ans: number }[] }) {
  const weeks: (typeof days)[] = []
  for (let i = 0; i < days.length; i += 7) weeks.push(days.slice(i, i + 7))

  const colorFor = (d: { min: number; ans: number }) => {
    const score = d.min + d.ans
    if (score === 0) return 'bg-slate-100'
    if (score < 15) return 'bg-indigo-200'
    if (score < 30) return 'bg-indigo-300'
    if (score < 60) return 'bg-indigo-500'
    return 'bg-indigo-700'
  }

  return (
    <div className="flex gap-1 overflow-x-auto">
      {weeks.map((w, wi) => (
        <div key={wi} className="flex flex-col gap-1">
          {w.map((d) => (
            <div
              key={d.date}
              title={`${d.date}: ${d.min}分 / ${d.ans}問`}
              className={`h-3 w-3 rounded-sm ${colorFor(d)}`}
            />
          ))}
        </div>
      ))}
    </div>
  )
}

/* ============ 記録パネル ============ */
function LogPanel({
  questions,
  kijutsu,
  dueCount,
  onGotoKijutsu,
}: {
  questions: Question[]
  kijutsu: KijutsuData
  dueCount: number
  onGotoKijutsu: () => void
}) {
  const genreAgg = useMemo(() => genreStats(questions), [questions])
  const rankedGenres = useMemo(
    () => genreAgg.filter((g) => g.answered >= 3).sort((a, b) => a.accuracy - b.accuracy),
    [genreAgg],
  )

  const kijutsuMarks = useMemo(() => loadKijutsuMarks(), [])
  const kijutsuFailed = useMemo(
    () => kijutsu.problems.filter((p) => kijutsuMarks[p.id] === 'failed'),
    [kijutsu, kijutsuMarks],
  )
  const kijutsuCounts = useMemo(() => {
    const c = { solved: 0, partial: 0, failed: 0 }
    for (const m of Object.values(kijutsuMarks)) c[m] += 1
    return c
  }, [kijutsuMarks])

  const flashcardMarks = useMemo(() => loadFlashcardMarks(), [])
  const flashcardCounts = useMemo(() => {
    const c = { solved: 0, partial: 0, failed: 0 }
    for (const m of Object.values(flashcardMarks)) c[m] += 1
    return c
  }, [flashcardMarks])

  const trend = useMemo(() => studyAccuracyTrend(30), [])
  const combinedDue = dueCount + kijutsuFailed.length

  return (
    <>
      <ProgressSummaryCard questions={questions} />

      <section className="mb-6 grid grid-cols-2 gap-3">
        <Stat label="今日の復習（択一＋暗記）" value={`${dueCount}`} unit="問" />
        <Stat label="今日の復習（合計）" value={`${combinedDue}`} unit="件" />
      </section>

      {kijutsuFailed.length > 0 && (
        <Card title="書式 要復習">
          <p className="mb-3 text-xs text-slate-500">
            自己採点で「✗ できなかった」にした問題です。もう一度解いてみましょう。
          </p>
          <ul className="mb-3 space-y-1">
            {kijutsuFailed.map((p) => (
              <li key={p.id} className="text-sm text-slate-700">
                {p.yearLabel} 第{p.questionNo}問 {p.category}
              </li>
            ))}
          </ul>
          <button
            onClick={onGotoKijutsu}
            className="rounded-lg bg-rose-600 px-4 py-2 text-sm font-semibold text-white hover:bg-rose-700"
          >
            書式タブへ
          </button>
        </Card>
      )}

      <Card title="弱点ジャンルランキング">
        {rankedGenres.length > 0 ? (
          <div className="space-y-2">
            {rankedGenres.map((g) => (
              <SubjectBar key={g.genre} label={g.genre} accuracy={g.accuracy} wrongCount={g.wrongCount} />
            ))}
          </div>
        ) : (
          <p className="text-sm text-slate-500">
            ジャンルごとに3回以上解答すると、ここにランキングが表示されます。
          </p>
        )}
      </Card>

      <Card title="日別正答率の推移（直近30日）">
        <AccuracySparkline trend={trend} />
      </Card>

      <Card title="書式 自己採点サマリー">
        <div className="grid grid-cols-3 gap-2 text-center text-sm">
          <div className="rounded-lg bg-emerald-50 p-2">
            <div className="font-bold text-emerald-700">{kijutsuCounts.solved}</div>
            <div className="text-xs text-emerald-600">◯ 解けた</div>
          </div>
          <div className="rounded-lg bg-amber-50 p-2">
            <div className="font-bold text-amber-700">{kijutsuCounts.partial}</div>
            <div className="text-xs text-amber-600">△ 惜しい</div>
          </div>
          <div className="rounded-lg bg-rose-50 p-2">
            <div className="font-bold text-rose-700">{kijutsuCounts.failed}</div>
            <div className="text-xs text-rose-600">✗ できなかった</div>
          </div>
        </div>
      </Card>

      <Card title="用語カード 自己採点サマリー">
        {flashcardCounts.solved + flashcardCounts.partial + flashcardCounts.failed > 0 ? (
          <div className="grid grid-cols-3 gap-2 text-center text-sm">
            <div className="rounded-lg bg-emerald-50 p-2">
              <div className="font-bold text-emerald-700">{flashcardCounts.solved}</div>
              <div className="text-xs text-emerald-600">◯ 覚えた</div>
            </div>
            <div className="rounded-lg bg-amber-50 p-2">
              <div className="font-bold text-amber-700">{flashcardCounts.partial}</div>
              <div className="text-xs text-amber-600">△ うろ覚え</div>
            </div>
            <div className="rounded-lg bg-rose-50 p-2">
              <div className="font-bold text-rose-700">{flashcardCounts.failed}</div>
              <div className="text-xs text-rose-600">✗ 覚えていない</div>
            </div>
          </div>
        ) : (
          <p className="text-sm text-slate-500">用語カードで自己採点すると、ここに集計されます。</p>
        )}
      </Card>
    </>
  )
}

/* ============ secretary2向け 進捗サマリー ============ */
function ProgressSummaryCard({ questions }: { questions: Question[] }) {
  const [copied, setCopied] = useState(false)
  const [showFallback, setShowFallback] = useState(false)
  const summary = useMemo(() => buildProgressSummaryText(questions), [questions])

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(summary)
      setCopied(true)
      setShowFallback(false)
      setTimeout(() => setCopied(false), 2000)
    } catch {
      setShowFallback(true)
    }
  }

  return (
    <Card title="📋 secretary2向け 進捗サマリー">
      <p className="mb-3 text-xs text-slate-500">
        コピーして、学習管理チャット（secretary2）に貼り付けると最新の進捗を報告できます。
      </p>
      <button
        onClick={handleCopy}
        className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-700"
      >
        {copied ? 'コピーしました ✓' : 'サマリーをコピー'}
      </button>
      {showFallback && (
        <textarea
          readOnly
          value={summary}
          onFocus={(e) => e.currentTarget.select()}
          className="mt-3 h-48 w-full rounded-lg border border-slate-300 p-2 font-mono text-xs"
        />
      )}
    </Card>
  )
}

function AccuracySparkline({ trend }: { trend: { date: string; ans: number; correct: number }[] }) {
  const hasData = trend.some((t) => t.ans > 0)
  if (!hasData) {
    return <p className="text-sm text-slate-500">解答を記録すると、正答率の推移が表示されます。</p>
  }

  const w = 300
  const h = 60
  const pad = 4
  const points = trend.map((t, i) => {
    const x = pad + (i / (trend.length - 1)) * (w - pad * 2)
    const acc = t.ans > 0 ? t.correct / t.ans : null
    return { x, acc }
  })
  const withAcc = points.filter((p): p is { x: number; acc: number } => p.acc !== null)
  const path = withAcc
    .map((p) => `${p.x},${pad + (1 - p.acc) * (h - pad * 2)}`)
    .join(' ')

  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="w-full" preserveAspectRatio="none">
      <polyline points={path} fill="none" stroke="#4f46e5" strokeWidth={2} />
      {withAcc.map((p, i) => (
        <circle key={i} cx={p.x} cy={pad + (1 - p.acc) * (h - pad * 2)} r={2} fill="#4f46e5" />
      ))}
    </svg>
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
