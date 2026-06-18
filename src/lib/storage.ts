// 学習記録をlocalStorage(高速/オフライン)とSupabase(クロスデバイス同期)の両方に保存する。
import { supabase } from './supabase'

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
