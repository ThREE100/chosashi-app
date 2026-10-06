// 問題データ(src/data/anaume.json)の型
export type AnaumeBlank = {
  answer: string // 正解(レジュメの語群の表記)
  alt?: string[] // 正解として認める別の表記
}

export type AnaumeArticle = {
  heading: string // 例: 第1条（目的）
  text: string // 空欄は {番号}。改行は \n
}

export type AnaumeSet = {
  id: string // 例: fudosanho-p1(空欄IDの頭になり履歴と結びつくので、後から変えない)
  law: string
  title: string
  page: number
  articles: AnaumeArticle[]
  blanks: Record<string, AnaumeBlank>
}

export type AnaumeData = {
  meta: { title: string; note: string; source: string }
  sets: AnaumeSet[]
}
