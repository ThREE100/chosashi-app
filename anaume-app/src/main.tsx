import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import Anaume from './Anaume'
import type { AnaumeData } from './types'
import rawData from './data/anaume.json'

const data = rawData as unknown as AnaumeData

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <div className="mx-auto max-w-2xl px-4 py-6">
      <header className="mb-4 text-center">
        <h1 className="text-2xl font-bold text-slate-800">条文穴埋め</h1>
        <p className="text-xs text-slate-500">不動産登記法・令・規則・準則・区分所有法</p>
      </header>
      <Anaume data={data} />
    </div>
  </StrictMode>,
)
