import { useState } from 'react'
import { supabase } from '../lib/supabase'

const REDIRECT = window.location.origin + window.location.pathname

export default function Login() {
  const [email, setEmail] = useState('')
  const [sent, setSent] = useState(false)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    const { error } = await supabase.auth.signInWithOtp({
      email,
      options: { emailRedirectTo: REDIRECT },
    })
    setLoading(false)
    if (error) setError(error.message)
    else setSent(true)
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100 px-4">
      <div className="w-full max-w-sm rounded-2xl bg-white p-8 shadow-lg">
        <h1 className="mb-2 text-center text-xl font-bold text-slate-800">
          土地家屋調査士 トレーニング
        </h1>
        <p className="mb-6 text-center text-sm text-slate-500">
          学習記録を端末間で同期するには<br />メールアドレスでログインしてください
        </p>
        {sent ? (
          <div className="rounded-xl bg-emerald-50 p-4 text-center text-sm text-emerald-700">
            <p className="font-semibold">メールを送信しました</p>
            <p className="mt-1 text-xs">{email} のリンクをタップしてログインしてください</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="email"
              required
              placeholder="メールアドレス"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-xl border border-slate-300 px-4 py-3 text-sm focus:border-indigo-500 focus:outline-none"
            />
            {error && <p className="text-xs text-rose-600">{error}</p>}
            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-xl bg-indigo-600 py-3 font-semibold text-white hover:bg-indigo-700 disabled:opacity-60"
            >
              {loading ? '送信中…' : 'ログインリンクを送信'}
            </button>
          </form>
        )}
      </div>
    </div>
  )
}
