import { useState, useEffect } from 'react'
import type { Session } from '@supabase/supabase-js'
import { supabase } from './lib/supabase'
import { syncOnLogin } from './lib/storage'
import Login from './components/Login'
import type {
  AnkiData,
  AnswerResult,
  Dataset,
  KaisetsuPlus,
  KijutsuData,
  OxCard,
  Question,
  TermCard,
} from './types'
import rawData from './data/takuitsu.json'
import rawAnki from './data/ankicards.json'
import rawKijutsu from './data/kijutsu.json'
import rawKaisetsu from './data/kaisetsu_plus.json'
import Home from './components/Home'
import Quiz from './components/Quiz'
import Result from './components/Result'
import OxQuiz from './components/OxQuiz'
import Flashcard from './components/Flashcard'

const data = rawData as unknown as Dataset
const anki = rawAnki as unknown as AnkiData
const kijutsu = rawKijutsu as unknown as KijutsuData
const kaisetsu = (rawKaisetsu as unknown as KaisetsuPlus).entries
const ALL_QUESTIONS = data.questions

type View =
  | { name: 'home' }
  | { name: 'quiz'; title: string; questions: Question[] }
  | { name: 'result'; title: string; results: AnswerResult[] }
  | { name: 'oxquiz'; title: string; cards: OxCard[] }
  | { name: 'flashcards'; title: string; cards: TermCard[] }

export default function App() {
  const [session, setSession] = useState<Session | null | undefined>(undefined)
  const [view, setView] = useState<View>({ name: 'home' })

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session)
      if (session) syncOnLogin()
    })
    const { data: { subscription } } = supabase.auth.onAuthStateChange((_, s) => {
      setSession(s)
      if (s) syncOnLogin()
    })
    return () => subscription.unsubscribe()
  }, [])

  if (session === undefined) {
    return (
      <div className="min-h-screen flex items-center justify-center text-gray-500 dark:text-gray-400">
        読み込み中…
      </div>
    )
  }
  if (!session) return <Login />

  const home = () => setView({ name: 'home' })

  const startTakuitsu = (questions: Question[], title: string) => {
    if (questions.length === 0) return
    setView({ name: 'quiz', title, questions })
  }
  const startOx = (cards: OxCard[], title: string) => {
    if (cards.length === 0) return
    setView({ name: 'oxquiz', title, cards })
  }
  const startFlash = (cards: TermCard[], title: string) => {
    if (cards.length === 0) return
    setView({ name: 'flashcards', title, cards })
  }

  if (view.name === 'quiz') {
    return (
      <Quiz
        title={view.title}
        questions={view.questions}
        kaisetsu={kaisetsu}
        onQuit={home}
        onFinish={(results) => setView({ name: 'result', title: view.title, results })}
      />
    )
  }

  if (view.name === 'result') {
    return (
      <Result
        title={view.title}
        results={view.results}
        onRetryWrong={(qs) => startTakuitsu(qs, '間違い直し')}
        onHome={home}
      />
    )
  }

  if (view.name === 'oxquiz') {
    return <OxQuiz title={view.title} cards={view.cards} onHome={home} />
  }

  if (view.name === 'flashcards') {
    return <Flashcard title={view.title} cards={view.cards} onHome={home} />
  }

  return (
    <Home
      questions={ALL_QUESTIONS}
      ankiOx={anki.ox}
      ankiTerms={anki.terms}
      chapters={anki.chapters}
      kijutsu={kijutsu}
      userEmail={session.user.email}
      onStartTakuitsu={startTakuitsu}
      onStartOx={startOx}
      onStartFlash={startFlash}
    />
  )
}
