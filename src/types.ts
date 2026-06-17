export type Alt = { label: string; text: string }
export type Combo = { no: number; text: string }

export type Question = {
  id: string
  yearCode: string
  yearLabel: string
  year: number
  questionNo: number
  subject: string
  stem: string
  alts: Alt[]
  combos: Combo[]
  correctAnswer: number
  explanation: string
}

export type Dataset = {
  meta: {
    title: string
    source: string
    count: number
    years: string[]
  }
  questions: Question[]
}

/** 1問の解答結果 */
export type AnswerResult = {
  question: Question
  selected: number
  isCorrect: boolean
}

// ---- 暗記（一問一答・用語カード） ----

export type OxCard = {
  id: string
  chapterId: string
  chapter: string
  stem: string
  correct: boolean // true = ○（正しい記述）, false = ×（誤った記述）
  explanation: string
  tags: string[]
}

export type TermCard = {
  id: string
  chapterId: string
  chapter: string
  term: string
  yomi: string
  definition: string
  cautions: string
}

export type AnkiChapter = { id: string; no: number; title: string }

export type AnkiData = {
  meta: { title: string; oxCount: number; termCount: number; source: string }
  chapters: AnkiChapter[]
  ox: OxCard[]
  terms: TermCard[]
}

// ---- 書式（記述）レビュー ----

export type KijutsuProblem = {
  id: string
  yearCode: string
  yearLabel: string
  category: '土地' | '建物'
  questionNo: number
  problemText: string
  modelAnswerText: string
  problemImages: string[] // public/ からの相対パス（無ければ空）
  answerImages: string[]
}

export type KijutsuData = {
  meta: { title: string; note: string; count: number; withImages: number }
  problems: KijutsuProblem[]
}

/** 書式の自己採点 */
export type KijutsuMark = 'solved' | 'partial' | 'failed'

// ---- 択一オリジナル解説（考え方・落とし穴・暗記ポイント） ----
export type KaisetsuEntry = {
  approach: string
  pitfalls: string
  keyPoints: string
  checkNote?: string
  reviewed?: boolean
}
export type KaisetsuPlus = {
  meta: Record<string, unknown>
  entries: Record<string, KaisetsuEntry>
}
