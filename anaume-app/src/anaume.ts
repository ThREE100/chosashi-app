// 条文穴埋め: 解答履歴の保存と、忘却曲線に沿った復習スケジュールの計算。
//
// 保存するのは「いつ・どの空欄に・何と答えて・正誤はどうだったか」の履歴(Attempt)だけで、
// 復習リスト・次回の復習日時はすべて履歴から毎回計算し直す。履歴はこの端末のブラウザ
// (localStorage)に保存し、JSONで書き出し・読み込みできる。別の端末の履歴を読み込むと
// 足し合わせて計算し直すので、復習リストも一致する。
//
// 復習のルール
// - 1日2回の復習の回(朝 0:00〜11:59 / 夜 12:00〜23:59)を「回(slot)」の単位にする。
// - 間違えると復習リストに入り、「これまでに間違えた回数」だけ正解しないと消えない
//   (3回間違えたことがあれば3回正解が必要)。復習中にまた間違えると、必要な正解数は
//   その時点の通算の間違い回数に戻る。
// - 間違えた問題は次の回に出す(朝に間違えたらその日の夜、夜に間違えたら翌朝)。
// - 復習の回で正解するたびに、次の出題までの間隔を忘却曲線に合わせて延ばす
//   (次の回 → 1日後 → 2日後 → 4日後 → 7日後)。
// - 正解の数は「出題予定の回(期限が来た回)」に答えたものだけ数える。同じ回に何度も
//   正解して一気に消すことはできない(間隔をあけて思い出すことが忘却曲線の要点のため)。
import type { AnaumeData, AnaumeSet } from './types'

const KEY = 'chosashi_anaume_v1'

/** 1空欄・1回分の解答履歴 */
export type Attempt = {
  t: number // 解答日時(ミリ秒)
  b: string // 空欄ID(セットID-空欄番号)
  c: 0 | 1 // 1=正解
  a: string // 入力した答え
  m: 'p' | 'r' // p=通常の演習, r=復習
  o?: 1 // 1=表記ゆれ等で「正解扱い」にしたもの
}

/** 復習の間隔(回の数。1回=半日) */
export const INTERVALS = [1, 2, 4, 8, 14]
export const INTERVAL_LABELS = ['次の回', '1日後', '2日後', '4日後', '7日後']

export function loadAttempts(): Attempt[] {
  try {
    const raw = localStorage.getItem(KEY)
    return raw ? (JSON.parse(raw) as Attempt[]) : []
  } catch {
    return []
  }
}

function saveAttempts(list: Attempt[]) {
  try {
    localStorage.setItem(KEY, JSON.stringify(list))
  } catch {
    // 保存に失敗しても演習は続行できる
  }
}

// ---- 回(slot): 1日を朝・夜の2回に分けた通し番号 ----

/** 日時 → 回の通し番号(日数×2 + 朝0/夜1、端末のローカル時刻で判定) */
export function slotOf(t: number): number {
  const d = new Date(t)
  const day = Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 86400000
  return day * 2 + (d.getHours() >= 12 ? 1 : 0)
}

export function slotLabel(slot: number): string {
  const d = new Date(Math.floor(slot / 2) * 86400000)
  return `${d.getUTCMonth() + 1}/${d.getUTCDate()} ${slot % 2 === 0 ? '朝' : '夜'}`
}

export function slotDayLabel(slot: number): string {
  const d = new Date(Math.floor(slot / 2) * 86400000)
  const w = '日月火水木金土'[d.getUTCDay()]
  return `${d.getUTCMonth() + 1}/${d.getUTCDate()}(${w})`
}

// ---- 空欄ごとの状態(履歴から計算) ----

export type BlankState = {
  wrong: number // 通算の間違い回数
  correct: number // 通算の正解回数
  need: number // 復習リストから消えるまでに必要な残りの正解数(0=リスト外)
  streak: number // 復習中の連続正解数
  due: number | null // 次に出題する回(need>0のとき)
  lastT: number // 最後に解いた日時
}

export function computeStates(attempts: Attempt[]): Record<string, BlankState> {
  const sorted = [...attempts].sort((x, y) => x.t - y.t)
  const map: Record<string, BlankState> = {}
  for (const at of sorted) {
    const s = (map[at.b] ??= { wrong: 0, correct: 0, need: 0, streak: 0, due: null, lastT: 0 })
    const slot = slotOf(at.t)
    s.lastT = at.t
    if (!at.c) {
      s.wrong += 1
      s.need = s.wrong
      s.streak = 0
      s.due = slot + 1
    } else {
      s.correct += 1
      if (s.need > 0 && s.due !== null && slot >= s.due) {
        s.need -= 1
        s.streak += 1
        s.due = s.need > 0 ? slot + INTERVALS[Math.min(s.streak - 1, INTERVALS.length - 1)] : null
      }
    }
  }
  return map
}

/** 今の回に復習する空欄ID(期限が来ているもの、期限の古い順) */
export function dueBlankIds(states: Record<string, BlankState>, nowSlot: number): string[] {
  return Object.entries(states)
    .filter(([, s]) => s.need > 0 && s.due !== null && s.due <= nowSlot)
    .sort((a, b) => (a[1].due ?? 0) - (b[1].due ?? 0))
    .map(([id]) => id)
}

// ---- 記録 ----

/** 採点結果をまとめて記録する(同じ採点の空欄は同じ日時) */
export function recordAttempts(items: Omit<Attempt, 't'>[]): Attempt[] {
  const t = Date.now()
  const added = items.map((it) => ({ ...it, t }))
  const list = loadAttempts()
  list.push(...added)
  saveAttempts(list)
  return list
}

/** 間違いと判定された解答を「正解扱い」に直す(表記ゆれ等) */
export function overrideAttempt(t: number, b: string): Attempt[] {
  const list = loadAttempts()
  const at = list.find((x) => x.t === t && x.b === b)
  if (at && !at.c) {
    at.c = 1
    at.o = 1
    saveAttempts(list)
  }
  return list
}

export function exportAttemptsJson(): string {
  return JSON.stringify({ exportedAt: new Date().toISOString(), attempts: loadAttempts() }, null, 1)
}

// ---- 採点 ----

const KANJI_DIGIT: Record<string, string> = {
  〇: '0', 零: '0', 一: '1', 二: '2', 三: '3', 四: '4', 五: '5', 六: '6', 七: '7', 八: '8', 九: '9',
}

/** 表記の揺れを吸収して比べるための正規化(全角半角・空白・句読点・漢数字・カタカナ) */
export function normalizeAnswer(s: string): string {
  return s
    .normalize('NFKC')
    .replace(/\s+/g, '')
    .replace(/[〇零一二三四五六七八九]/g, (c) => KANJI_DIGIT[c])
    .replace(/・/g, '.')
    .replace(/[、,。「」]/g, '')
    .replace(/[ァ-ヶ]/g, (c) => String.fromCharCode(c.charCodeAt(0) - 0x60))
    .toLowerCase()
}

export function isCorrectAnswer(input: string, answer: string, alt: string[] = []): boolean {
  const x = normalizeAnswer(input)
  if (!x) return false
  return [answer, ...alt].some((a) => normalizeAnswer(a) === x)
}

// ---- 問題データの索引 ----

export type BlankInfo = { id: string; set: AnaumeSet; num: string; heading: string; answer: string }

export function blankId(setId: string, num: string): string {
  return `${setId}-${num}`
}

export function buildBlankIndex(data: AnaumeData): Record<string, BlankInfo> {
  const idx: Record<string, BlankInfo> = {}
  for (const set of data.sets) {
    for (const [num, b] of Object.entries(set.blanks)) {
      const art = set.articles.find((a) => a.text.includes(`{${num}}`))
      const id = blankId(set.id, num)
      idx[id] = { id, set, num, heading: art?.heading ?? '', answer: b.answer }
    }
  }
  return idx
}

// ---- 書き出し・読み込み(バックアップ／端末間の引き継ぎ) ----

/** 書き出したJSONを読み込み、今の履歴と足し合わせる。追加した件数を返す */
export function importAttemptsJson(json: string): number {
  const parsed = JSON.parse(json) as { attempts?: Attempt[] } | Attempt[]
  const incoming = Array.isArray(parsed) ? parsed : (parsed.attempts ?? [])
  const key = (a: Attempt) => `${a.t}|${a.b}`
  const merged = new Map(loadAttempts().map((a) => [key(a), a]))
  let added = 0
  for (const a of incoming) {
    if (typeof a?.t !== 'number' || typeof a?.b !== 'string') continue
    const cur = merged.get(key(a))
    if (!cur) added += 1
    // 片方で「正解扱い」に直していれば、それを優先する
    if (!cur || (a.o && !cur.o)) merged.set(key(a), { t: a.t, b: a.b, c: a.c ? 1 : 0, a: String(a.a ?? ''), m: a.m === 'r' ? 'r' : 'p', ...(a.o ? { o: 1 as const } : {}) })
  }
  saveAttempts([...merged.values()].sort((x, y) => x.t - y.t))
  return added
}

export function clearAttempts() {
  try {
    localStorage.removeItem(KEY)
  } catch {
    // ignore
  }
}
