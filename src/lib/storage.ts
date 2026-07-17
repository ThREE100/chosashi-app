// 学習記録をlocalStorage(高速/オフライン)とSupabase(クロスデバイス同期)の両方に保存する。
import { supabase } from './supabase'
import type { KijutsuMark } from '../types'

const KEY = 'chosashi_progress_v1'

export type QStat = {
  correct: number // 正解した回数
  wrong: number // 間違えた回数
  last: 'correct' | 'wrong' // 直近の結果
}

export type Progress = Record<string, QStat>

export function loadProgress(): Progress {
  try {
    const raw = localStorage.getItem(KEY)
    return raw ? (JSON.parse(raw) as Progress) : {}
  } catch {
    return {}
  }
}

function save(p: Progress) {
  try {
    localStorage.setItem(KEY, JSON.stringify(p))
  } catch {
    // 保存に失敗しても演習は続行できる
  }
}

/** 1問の解答を記録する */
export function recordAnswer(id: string, isCorrect: boolean) {
  const p = loadProgress()
  const s: QStat = p[id] ?? { correct: 0, wrong: 0, last: 'wrong' }
  if (isCorrect) s.correct += 1
  else s.wrong += 1
  s.last = isCorrect ? 'correct' : 'wrong'
  p[id] = s
  save(p)
  scheduleSrs(id, isCorrect) // 復習スケジュール更新
  logStudyAnswer(isCorrect) // 今日の学習ログに加算
  syncAnswerToSupabase(id, s) // fire-and-forget
}

/** Supabase に1問分の記録を upsert する（オフライン時はスキップ） */
async function syncAnswerToSupabase(id: string, s: QStat) {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return
    await supabase.from('progress').upsert({
      user_id: user.id,
      question_id: id,
      correct: s.correct,
      wrong: s.wrong,
      last_result: s.last,
      updated_at: new Date().toISOString(),
    }, { onConflict: 'user_id,question_id' })
  } catch {
    // オフライン時はスキップ
  }
}

/** ログイン時: Supabase とローカルを双方向同期する。
 *  リモートを取得してローカルへ反映 → リモートに無いローカル記録
 *  （認証導入前に貯めた記録など）をアップロードする。 */
export async function syncOnLogin() {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return
    await mergeProgress(user.id)
    await mergeSrs(user.id)
    await mergeStudyLog(user.id)
  } catch {
    // オフライン時はスキップ
  }
}

async function mergeProgress(userId: string) {
  const { data } = await supabase
    .from('progress')
    .select('question_id,correct,wrong,last_result')
    .eq('user_id', userId)
  const remote = data ?? []
  const remoteIds = new Set(remote.map((r) => r.question_id))
  const p = loadProgress()
  for (const row of remote) {
    p[row.question_id] = {
      correct: row.correct,
      wrong: row.wrong,
      last: row.last_result as 'correct' | 'wrong',
    }
  }
  save(p)
  const toPush = Object.entries(p)
    .filter(([id]) => !remoteIds.has(id))
    .map(([id, s]) => ({
      user_id: userId,
      question_id: id,
      correct: s.correct,
      wrong: s.wrong,
      last_result: s.last,
      updated_at: new Date().toISOString(),
    }))
  if (toPush.length) {
    await supabase.from('progress').upsert(toPush, { onConflict: 'user_id,question_id' })
  }
}

/** 直近で間違えた問題のIDセット */
export function wrongQuestionIds(): Set<string> {
  const p = loadProgress()
  return new Set(
    Object.entries(p)
      .filter(([, s]) => s.last === 'wrong')
      .map(([id]) => id),
  )
}

/** 全体統計（解答済み問題数・延べ正答率） */
export function overallStats() {
  const p = loadProgress()
  const ids = Object.keys(p)
  let correct = 0
  let total = 0
  for (const id of ids) {
    correct += p[id].correct
    total += p[id].correct + p[id].wrong
  }
  return {
    answeredQuestions: ids.length, // 一度でも解いた問題数
    totalAttempts: total, // 延べ解答数
    correctAttempts: correct,
    accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
  }
}

export function resetProgress() {
  try {
    localStorage.removeItem(KEY)
    localStorage.removeItem(SRS_KEY)
  } catch {
    // ignore
  }
}

export type SubjectStat = {
  subject: string
  answered: number
  accuracy: number
  wrongCount: number
}

/** 科目別の正答率を返す */
export function subjectStats(questions: { id: string; subject: string }[]): SubjectStat[] {
  const p = loadProgress()
  const bySubject: Record<string, { correct: number; total: number; wrong: number }> = {}

  for (const q of questions) {
    const s = p[q.id]
    if (!s) continue
    if (!bySubject[q.subject]) bySubject[q.subject] = { correct: 0, total: 0, wrong: 0 }
    bySubject[q.subject].correct += s.correct
    bySubject[q.subject].total += s.correct + s.wrong
    if (s.last === 'wrong') bySubject[q.subject].wrong += 1
  }

  return Object.entries(bySubject).map(([subject, s]) => ({
    subject,
    answered: s.total,
    accuracy: s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0,
    wrongCount: s.wrong,
  }))
}

export type YearStat = {
  yearCode: string
  yearLabel: string
  answered: number
  total: number
  accuracy: number
}

/** 年度別の解答状況を返す */
export function yearStats(
  questions: { id: string; yearCode: string; yearLabel: string }[],
): YearStat[] {
  const p = loadProgress()
  const byYear: Record<string, { yearLabel: string; correct: number; total: number; qTotal: number }> = {}

  for (const q of questions) {
    if (!byYear[q.yearCode]) byYear[q.yearCode] = { yearLabel: q.yearLabel, correct: 0, total: 0, qTotal: 0 }
    byYear[q.yearCode].qTotal += 1
    const s = p[q.id]
    if (s) {
      byYear[q.yearCode].correct += s.correct
      byYear[q.yearCode].total += s.correct + s.wrong
    }
  }

  return Object.entries(byYear).map(([yearCode, s]) => ({
    yearCode,
    yearLabel: s.yearLabel,
    answered: s.total,
    total: s.qTotal,
    accuracy: s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0,
  }))
}

export type GenreStat = {
  genre: string
  answered: number
  accuracy: number
  wrongCount: number
}

/** ジャンル別の正答率を返す（ジャンル未設定の問題は集計対象外） */
export function genreStats(questions: { id: string; genre: string | null }[]): GenreStat[] {
  const p = loadProgress()
  const byGenre: Record<string, { correct: number; total: number; wrong: number }> = {}

  for (const q of questions) {
    if (!q.genre) continue
    const s = p[q.id]
    if (!s) continue
    if (!byGenre[q.genre]) byGenre[q.genre] = { correct: 0, total: 0, wrong: 0 }
    byGenre[q.genre].correct += s.correct
    byGenre[q.genre].total += s.correct + s.wrong
    if (s.last === 'wrong') byGenre[q.genre].wrong += 1
  }

  return Object.entries(byGenre).map(([genre, s]) => ({
    genre,
    answered: s.total,
    accuracy: s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0,
    wrongCount: s.wrong,
  }))
}

// ---- 学習時間ログ（今日の学習: 手動記録した時間 + 解答数・正解数） ----
const STUDYLOG_KEY = 'chosashi_studylog_v1'

export type StudyDay = { min: number; ans: number; correct: number }
export type StudyLog = Record<string, StudyDay>

export function loadStudyLog(): StudyLog {
  try {
    const raw = localStorage.getItem(STUDYLOG_KEY)
    return raw ? (JSON.parse(raw) as StudyLog) : {}
  } catch {
    return {}
  }
}

function saveStudyLog(log: StudyLog) {
  try {
    localStorage.setItem(STUDYLOG_KEY, JSON.stringify(log))
  } catch {
    // ignore
  }
}

/** 解答1件を今日の学習ログに加算する（択一/暗記/書式の各記録処理から呼ばれる） */
export function logStudyAnswer(isCorrect: boolean) {
  const log = loadStudyLog()
  const key = todayStr()
  const day = log[key] ?? { min: 0, ans: 0, correct: 0 }
  day.ans += 1
  if (isCorrect) day.correct += 1
  log[key] = day
  saveStudyLog(log)
  syncStudyDayToSupabase(key, day) // fire-and-forget
}

/** 手動で今日の学習時間を加減する（0分未満にはならない） */
export function addStudyMinutes(delta: number) {
  const log = loadStudyLog()
  const key = todayStr()
  const day = log[key] ?? { min: 0, ans: 0, correct: 0 }
  day.min = Math.max(0, day.min + delta)
  log[key] = day
  saveStudyLog(log)
  syncStudyDayToSupabase(key, day) // fire-and-forget
}

/** Supabase に1日分の学習記録を upsert する（オフライン時はスキップ） */
async function syncStudyDayToSupabase(day: string, d: StudyDay) {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return
    await supabase.from('studylog').upsert({
      user_id: user.id,
      day,
      min: d.min,
      ans: d.ans,
      correct: d.correct,
      updated_at: new Date().toISOString(),
    }, { onConflict: 'user_id,day' })
  } catch {
    // オフライン時はスキップ
  }
}

/** ログイン時: Supabase の学習記録とローカルを双方向同期する */
async function mergeStudyLog(userId: string) {
  const { data } = await supabase
    .from('studylog')
    .select('day,min,ans,correct')
    .eq('user_id', userId)
  const remote = data ?? []
  const remoteDays = new Set(remote.map((r) => r.day))
  const log = loadStudyLog()
  for (const row of remote) {
    log[row.day] = { min: row.min, ans: row.ans, correct: row.correct }
  }
  saveStudyLog(log)
  const toPush = Object.entries(log)
    .filter(([day]) => !remoteDays.has(day))
    .map(([day, d]) => ({
      user_id: userId,
      day,
      min: d.min,
      ans: d.ans,
      correct: d.correct,
      updated_at: new Date().toISOString(),
    }))
  if (toPush.length) {
    await supabase.from('studylog').upsert(toPush, { onConflict: 'user_id,day' })
  }
}

/** 今日の学習ログ */
export function getTodayStudy(): StudyDay {
  return loadStudyLog()[todayStr()] ?? { min: 0, ans: 0, correct: 0 }
}

/** 直近7日間（今日を含む）の学習時間合計 */
export function weekStudyMinutes(): number {
  const log = loadStudyLog()
  const today = todayStr()
  let total = 0
  for (let i = 0; i < 7; i++) {
    total += log[addDays(today, -i)]?.min ?? 0
  }
  return total
}

/** 累計学習時間（分） */
export function totalStudyMinutes(): number {
  const log = loadStudyLog()
  return Object.values(log).reduce((sum, d) => sum + d.min, 0)
}

/** 連続学習日数（min>0 または ans>0 の日が何日連続続いているか）。
 *  今日まだ学習していなくても、昨日までの連続記録はそのまま表示する（0にリセットしない）。 */
export function studyStreak(): number {
  const log = loadStudyLog()
  const today = todayStr()
  const hasActivity = (key: string) => {
    const d = log[key]
    return !!d && (d.min > 0 || d.ans > 0)
  }
  const start = hasActivity(today) ? today : addDays(today, -1)
  let streak = 0
  let cursor = start
  while (hasActivity(cursor)) {
    streak += 1
    cursor = addDays(cursor, -1)
  }
  return streak
}

/** 直近N週間分のヒートマップ用データ（日曜始まり、古い→新しい順、35件=5週なら7×5） */
export function studyHeatmap(weeks = 5): { date: string; min: number; ans: number }[] {
  const log = loadStudyLog()
  const today = todayStr()
  const todayDow = new Date(today + 'T00:00:00').getDay() // 0=日曜
  const totalDays = weeks * 7
  const start = addDays(today, -(totalDays - 1 - todayDow))
  const result: { date: string; min: number; ans: number }[] = []
  let cursor = start
  for (let i = 0; i < totalDays; i++) {
    const d = log[cursor]
    result.push({ date: cursor, min: d?.min ?? 0, ans: d?.ans ?? 0 })
    cursor = addDays(cursor, 1)
  }
  return result
}

/** 直近N日間の日別正答率推移データ（古い→新しい順） */
export function studyAccuracyTrend(days = 30): { date: string; ans: number; correct: number }[] {
  const log = loadStudyLog()
  const today = todayStr()
  const result: { date: string; ans: number; correct: number }[] = []
  for (let i = days - 1; i >= 0; i--) {
    const key = addDays(today, -i)
    const d = log[key]
    result.push({ date: key, ans: d?.ans ?? 0, correct: d?.correct ?? 0 })
  }
  return result
}

// ---- 書式の自己採点（solved / partial / failed） ----
const KIJUTSU_KEY = 'chosashi_kijutsu_v1'

export type KijutsuMarks = Record<string, 'solved' | 'partial' | 'failed'>

export function loadKijutsuMarks(): KijutsuMarks {
  try {
    const raw = localStorage.getItem(KIJUTSU_KEY)
    return raw ? (JSON.parse(raw) as KijutsuMarks) : {}
  } catch {
    return {}
  }
}

export function setKijutsuMark(id: string, mark: 'solved' | 'partial' | 'failed') {
  const m = loadKijutsuMarks()
  m[id] = mark
  try {
    localStorage.setItem(KIJUTSU_KEY, JSON.stringify(m))
  } catch {
    // ignore
  }
  logStudyAnswer(mark === 'solved') // 今日の学習ログに加算（solved=正解扱い）
}

// ---- 用語カードの自己採点（◯△✗、weak-point集計・学習ログ向け） ----
const FLASHCARD_KEY = 'chosashi_flashcard_v1'

export type FlashcardMarks = Record<string, KijutsuMark>

export function loadFlashcardMarks(): FlashcardMarks {
  try {
    const raw = localStorage.getItem(FLASHCARD_KEY)
    return raw ? (JSON.parse(raw) as FlashcardMarks) : {}
  } catch {
    return {}
  }
}

export function setFlashcardMark(id: string, mark: KijutsuMark) {
  const m = loadFlashcardMarks()
  m[id] = mark
  try {
    localStorage.setItem(FLASHCARD_KEY, JSON.stringify(m))
  } catch {
    // ignore
  }
  logStudyAnswer(mark === 'solved') // 今日の学習ログに加算（solved=正解扱い）
}

// ---- 書式の解答確認フラグ（模範解答を一度でも表示したか） ----
const REVIEWED_KEY = 'chosashi_reviewed_v1'

export function getKijutsuReviewedIds(): Set<string> {
  try {
    const raw = localStorage.getItem(REVIEWED_KEY)
    return raw ? new Set(JSON.parse(raw) as string[]) : new Set()
  } catch {
    return new Set()
  }
}

export function markKijutsuReviewed(id: string) {
  const ids = getKijutsuReviewedIds()
  ids.add(id)
  try {
    localStorage.setItem(REVIEWED_KEY, JSON.stringify([...ids]))
  } catch {
    // ignore
  }
}

// ---- 間隔反復（SM-2簡易版）: 間違えた問題を忘却曲線に沿って再出題 ----
// 仕組み: 間違えた問題を翌日→3日後→約1週間後…と、正解するたびに間隔を延ばす。
// 初回から正解できた問題は「習得済み」とみなし追跡しない。
const SRS_KEY = 'chosashi_srs_v1'

export type SrsCard = {
  ease: number // 易しさ係数（正解で微増・不正解で減少）
  interval: number // 次回復習までの日数
  reps: number // 連続正解回数
  due: string // 次回復習日 'YYYY-MM-DD'
}
export type SrsDeck = Record<string, SrsCard>

function ymd(d: Date): string {
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}
function todayStr(): string {
  return ymd(new Date())
}
function addDays(base: string, days: number): string {
  const d = new Date(base + 'T00:00:00')
  d.setDate(d.getDate() + days)
  return ymd(d)
}

export function loadSrs(): SrsDeck {
  try {
    const raw = localStorage.getItem(SRS_KEY)
    return raw ? (JSON.parse(raw) as SrsDeck) : {}
  } catch {
    return {}
  }
}
function saveSrs(d: SrsDeck) {
  try {
    localStorage.setItem(SRS_KEY, JSON.stringify(d))
  } catch {
    // ignore
  }
}

/** 解答結果に応じて復習スケジュールを更新する */
function scheduleSrs(id: string, correct: boolean) {
  const deck = loadSrs()
  const prev = deck[id]
  const today = todayStr()

  let card: SrsCard
  if (!prev) {
    if (correct) return // 初回正解 → 復習不要
    card = { ease: 2.5, interval: 1, reps: 0, due: addDays(today, 1) }
  } else if (!correct) {
    // 間違えた → 翌日に再出題、係数を下げる
    card = { ease: Math.max(1.3, prev.ease - 0.2), interval: 1, reps: 0, due: addDays(today, 1) }
  } else {
    // 正解 → 間隔を延ばす（1→3→×ease）
    const reps = prev.reps + 1
    const interval = reps === 1 ? 1 : reps === 2 ? 3 : Math.round(prev.interval * prev.ease)
    const ease = Math.min(2.8, prev.ease + 0.05)
    card = { ease, interval, reps, due: addDays(today, interval) }
  }
  deck[id] = card
  saveSrs(deck)
  syncSrsToSupabase(id, card) // fire-and-forget
}

/** 今日が復習日（due <= 今日）の問題IDセット */
export function dueQuestionIds(): Set<string> {
  const deck = loadSrs()
  const today = todayStr()
  return new Set(
    Object.entries(deck)
      .filter(([, c]) => c.due <= today)
      .map(([id]) => id),
  )
}

async function syncSrsToSupabase(id: string, c: SrsCard) {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return
    await supabase.from('srs').upsert({
      user_id: user.id,
      question_id: id,
      ease: c.ease,
      ivl: c.interval,
      reps: c.reps,
      due: c.due,
      updated_at: new Date().toISOString(),
    }, { onConflict: 'user_id,question_id' })
  } catch {
    // オフライン時はスキップ
  }
}

/** secretary2(学習管理)向けの進捗サマリーをテキスト化する。コピーしてチャットに貼り付ける想定。 */
export function buildProgressSummaryText(
  questions: { id: string; subject: string; yearCode: string; yearLabel: string; genre: string | null }[],
): string {
  const stats = overallStats()
  const subj = subjectStats(questions)
  const yr = yearStats(questions)
  const weakGenres = genreStats(questions)
    .filter((g) => g.answered >= 3)
    .sort((a, b) => a.accuracy - b.accuracy)
    .slice(0, 5)
  const due = dueQuestionIds().size

  const kMarks = loadKijutsuMarks()
  const kCounts = { solved: 0, partial: 0, failed: 0 }
  for (const m of Object.values(kMarks)) kCounts[m] += 1

  const fMarks = loadFlashcardMarks()
  const fCounts = { solved: 0, partial: 0, failed: 0 }
  for (const m of Object.values(fMarks)) fCounts[m] += 1

  const lines: string[] = []
  lines.push(`# 進捗サマリー（chosashi-app）${todayStr()} 出力`)
  lines.push('')
  lines.push('## 学習時間')
  lines.push(`- 連続学習日数: ${studyStreak()}日`)
  lines.push(`- 今週累計: ${weekStudyMinutes()}分 / 全期間累計: ${totalStudyMinutes()}分`)
  lines.push('')
  lines.push('## 択一')
  lines.push(
    `- 解いた問題: ${stats.answeredQuestions}問 / 延べ解答数: ${stats.totalAttempts}回 / 延べ正答率: ${stats.accuracy}%`,
  )
  lines.push(`- 今日の復習待ち（SRS）: ${due}問`)
  if (subj.length > 0) {
    lines.push('- 科目別正答率:')
    for (const s of subj) {
      lines.push(`  - ${s.subject}: ${s.accuracy}%（解答${s.answered}回・要復習${s.wrongCount}問）`)
    }
  }
  if (yr.length > 0) {
    lines.push('- 年度別正答率:')
    for (const y of yr) {
      lines.push(`  - ${y.yearLabel}: ${y.answered > 0 ? `${y.accuracy}%` : '未解答'}`)
    }
  }
  if (weakGenres.length > 0) {
    lines.push('- 弱点ジャンルTOP5（3回以上解答したジャンルのみ）:')
    for (const g of weakGenres) {
      lines.push(`  - ${g.genre}: ${g.accuracy}%（要復習${g.wrongCount}問）`)
    }
  }
  lines.push('')
  lines.push('## 書式（記述）自己採点')
  lines.push(`- ◯解けた: ${kCounts.solved} / △惜しい: ${kCounts.partial} / ✗できなかった: ${kCounts.failed}`)
  lines.push('')
  lines.push('## 用語カード自己採点')
  lines.push(`- ◯覚えた: ${fCounts.solved} / △うろ覚え: ${fCounts.partial} / ✗覚えていない: ${fCounts.failed}`)

  return lines.join('\n')
}

async function mergeSrs(userId: string) {
  const { data } = await supabase
    .from('srs')
    .select('question_id,ease,ivl,reps,due')
    .eq('user_id', userId)
  const remote = data ?? []
  const remoteIds = new Set(remote.map((r) => r.question_id))
  const deck = loadSrs()
  for (const row of remote) {
    deck[row.question_id] = {
      ease: row.ease,
      interval: row.ivl,
      reps: row.reps,
      due: row.due,
    }
  }
  saveSrs(deck)
  const toPush = Object.entries(deck)
    .filter(([id]) => !remoteIds.has(id))
    .map(([id, c]) => ({
      user_id: userId,
      question_id: id,
      ease: c.ease,
      ivl: c.interval,
      reps: c.reps,
      due: c.due,
      updated_at: new Date().toISOString(),
    }))
  if (toPush.length) {
    await supabase.from('srs').upsert(toPush, { onConflict: 'user_id,question_id' })
  }
}
