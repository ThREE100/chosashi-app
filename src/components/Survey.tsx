import { useMemo, useState, type ReactNode } from 'react'

// 測量座標系：X=北(N), Y=東(東), 方向角は北(+X)から時計回り。
// 座標法による倍面積：2A = Σ Xi(Y[i+1] − Y[i−1])

type Pt = { name: string; x: string; y: string }

const SAMPLE: Pt[] = [
  { name: 'A', x: '100.00', y: '100.00' },
  { name: 'B', x: '100.00', y: '120.00' },
  { name: 'C', x: '80.00', y: '120.00' },
  { name: 'D', x: '80.00', y: '100.00' },
]

export default function Survey() {
  const [tool, setTool] = useState<'area' | 'dir'>('area')
  return (
    <>
      <div className="mb-4 flex gap-2 text-sm">
        <SubTab active={tool === 'area'} onClick={() => setTool('area')}>
          座標求積
        </SubTab>
        <SubTab active={tool === 'dir'} onClick={() => setTool('dir')}>
          距離・方向角
        </SubTab>
      </div>
      {tool === 'area' ? <AreaTool /> : <DirectionTool />}
      <p className="mt-4 text-center text-xs text-slate-400">
        座標系：X＝北、Y＝東／方向角は北から時計回り
      </p>
    </>
  )
}

/* ---------------- 座標求積 ---------------- */
function AreaTool() {
  const [pts, setPts] = useState<Pt[]>(SAMPLE)

  const update = (i: number, key: keyof Pt, val: string) =>
    setPts((p) => p.map((pt, idx) => (idx === i ? { ...pt, [key]: val } : pt)))
  const addRow = () =>
    setPts((p) => [...p, { name: nextName(p.length), x: '', y: '' }])
  const delRow = (i: number) => setPts((p) => p.filter((_, idx) => idx !== i))

  const calc = useMemo(() => {
    const nums = pts.map((p) => ({
      name: p.name,
      x: parseFloat(p.x),
      y: parseFloat(p.y),
    }))
    const valid = nums.filter((p) => Number.isFinite(p.x) && Number.isFinite(p.y))
    if (valid.length < 3) return null
    const n = valid.length
    const rows = valid.map((p, i) => {
      const yNext = valid[(i + 1) % n].y
      const yPrev = valid[(i - 1 + n) % n].y
      const dy = yNext - yPrev // Y[i+1] − Y[i−1]
      const term = p.x * dy
      return { name: p.name, x: p.x, y: p.y, dy, term }
    })
    const doubleArea = rows.reduce((s, r) => s + r.term, 0)
    const area = Math.abs(doubleArea) / 2
    return { rows, doubleArea, area, n }
  }, [pts])

  return (
    <div>
      <div className="overflow-hidden rounded-xl bg-white shadow-sm">
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-slate-100 text-xs text-slate-500">
              <th className="px-2 py-2 font-medium">点名</th>
              <th className="px-2 py-2 font-medium">X（北）</th>
              <th className="px-2 py-2 font-medium">Y（東）</th>
              <th className="w-8"></th>
            </tr>
          </thead>
          <tbody>
            {pts.map((p, i) => (
              <tr key={i} className="border-t border-slate-100">
                <td className="px-1 py-1">
                  <input
                    value={p.name}
                    onChange={(e) => update(i, 'name', e.target.value)}
                    className="w-14 rounded border border-slate-200 px-2 py-1 text-center"
                  />
                </td>
                <td className="px-1 py-1">
                  <input
                    value={p.x}
                    onChange={(e) => update(i, 'x', e.target.value)}
                    inputMode="decimal"
                    className="w-full rounded border border-slate-200 px-2 py-1 text-right"
                  />
                </td>
                <td className="px-1 py-1">
                  <input
                    value={p.y}
                    onChange={(e) => update(i, 'y', e.target.value)}
                    inputMode="decimal"
                    className="w-full rounded border border-slate-200 px-2 py-1 text-right"
                  />
                </td>
                <td className="px-1 py-1 text-center">
                  <button
                    onClick={() => delRow(i)}
                    className="text-slate-300 hover:text-rose-500"
                    title="削除"
                  >
                    ×
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <button
        onClick={addRow}
        className="mt-2 w-full rounded-lg border border-dashed border-slate-300 py-2 text-sm text-slate-500 hover:border-indigo-400 hover:text-indigo-600"
      >
        ＋ 点を追加
      </button>

      {/* 結果 */}
      {calc ? (
        <>
          <div className="mt-4 rounded-xl bg-indigo-600 p-5 text-center text-white shadow-sm">
            <div className="text-xs opacity-80">面積</div>
            <div className="text-3xl font-bold">
              {calc.area.toLocaleString(undefined, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 4,
              })}
              <span className="ml-1 text-lg font-normal">㎡</span>
            </div>
            <div className="mt-1 text-xs opacity-80">
              倍面積 = {calc.doubleArea.toFixed(4)}
            </div>
          </div>

          {/* 求積表 */}
          <p className="mt-4 mb-1 text-xs font-bold text-slate-500">
            求積表（座標法）
          </p>
          <div className="overflow-x-auto rounded-xl bg-white shadow-sm">
            <table className="w-full text-xs">
              <thead>
                <tr className="bg-slate-100 text-slate-500">
                  <th className="px-2 py-2">点</th>
                  <th className="px-2 py-2">X</th>
                  <th className="px-2 py-2">Yi+1 − Yi−1</th>
                  <th className="px-2 py-2">X(Yi+1−Yi−1)</th>
                </tr>
              </thead>
              <tbody>
                {calc.rows.map((r, i) => (
                  <tr key={i} className="border-t border-slate-100 text-right">
                    <td className="px-2 py-1 text-center font-medium">{r.name}</td>
                    <td className="px-2 py-1">{r.x.toFixed(2)}</td>
                    <td className="px-2 py-1">{r.dy.toFixed(2)}</td>
                    <td className="px-2 py-1">{r.term.toFixed(2)}</td>
                  </tr>
                ))}
                <tr className="border-t-2 border-slate-300 text-right font-bold">
                  <td className="px-2 py-1 text-center" colSpan={3}>
                    倍面積 合計
                  </td>
                  <td className="px-2 py-1">{calc.doubleArea.toFixed(2)}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </>
      ) : (
        <p className="mt-4 text-center text-sm text-slate-400">
          点を3つ以上、正しい数値で入力してください
        </p>
      )}
    </div>
  )
}

/* ---------------- 距離・方向角 ---------------- */
function DirectionTool() {
  const [a, setA] = useState({ x: '100.00', y: '100.00' })
  const [b, setB] = useState({ x: '140.00', y: '130.00' })

  const r = useMemo(() => {
    const x1 = parseFloat(a.x),
      y1 = parseFloat(a.y),
      x2 = parseFloat(b.x),
      y2 = parseFloat(b.y)
    if (![x1, y1, x2, y2].every(Number.isFinite)) return null
    const dx = x2 - x1
    const dy = y2 - y1
    const dist = Math.hypot(dx, dy)
    let deg = (Math.atan2(dy, dx) * 180) / Math.PI // 北(+X)から時計回り
    if (deg < 0) deg += 360
    return { dist, deg }
  }, [a, b])

  return (
    <div>
      <div className="space-y-3">
        <PointInput label="起点" p={a} onChange={setA} />
        <PointInput label="終点" p={b} onChange={setB} />
      </div>
      {r ? (
        <div className="mt-4 grid grid-cols-2 gap-3">
          <div className="rounded-xl bg-white p-4 text-center shadow-sm">
            <div className="text-xs text-slate-500">距離</div>
            <div className="mt-1 text-2xl font-bold text-slate-800">
              {r.dist.toFixed(3)}
              <span className="ml-1 text-sm font-normal text-slate-400">m</span>
            </div>
          </div>
          <div className="rounded-xl bg-white p-4 text-center shadow-sm">
            <div className="text-xs text-slate-500">方向角</div>
            <div className="mt-1 text-2xl font-bold text-slate-800">
              {toDMS(r.deg)}
            </div>
            <div className="text-xs text-slate-400">{r.deg.toFixed(4)}°</div>
          </div>
        </div>
      ) : (
        <p className="mt-4 text-center text-sm text-slate-400">
          4つの座標を数値で入力してください
        </p>
      )}
    </div>
  )
}

function PointInput({
  label,
  p,
  onChange,
}: {
  label: string
  p: { x: string; y: string }
  onChange: (v: { x: string; y: string }) => void
}) {
  return (
    <div className="flex items-center gap-2 rounded-xl bg-white p-3 shadow-sm">
      <span className="w-10 text-sm font-bold text-slate-600">{label}</span>
      <label className="flex-1 text-xs text-slate-400">
        X（北）
        <input
          value={p.x}
          inputMode="decimal"
          onChange={(e) => onChange({ ...p, x: e.target.value })}
          className="mt-0.5 w-full rounded border border-slate-200 px-2 py-1 text-right text-sm text-slate-800"
        />
      </label>
      <label className="flex-1 text-xs text-slate-400">
        Y（東）
        <input
          value={p.y}
          inputMode="decimal"
          onChange={(e) => onChange({ ...p, y: e.target.value })}
          className="mt-0.5 w-full rounded border border-slate-200 px-2 py-1 text-right text-sm text-slate-800"
        />
      </label>
    </div>
  )
}

/* ---------------- 小物・ユーティリティ ---------------- */
function SubTab({
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
        'rounded-lg px-4 py-2 font-semibold transition ' +
        (active ? 'bg-indigo-600 text-white' : 'bg-white text-slate-600 shadow-sm')
      }
    >
      {children}
    </button>
  )
}

function nextName(len: number) {
  // A, B, ... Z, A1, B1 ...
  const base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  return len < 26 ? base[len] : base[len % 26] + Math.floor(len / 26)
}

function toDMS(deg: number) {
  const d = Math.floor(deg)
  const mf = (deg - d) * 60
  const m = Math.floor(mf)
  const s = Math.round((mf - m) * 60)
  let dd = d,
    mm = m,
    ss = s
  if (ss === 60) {
    ss = 0
    mm += 1
  }
  if (mm === 60) {
    mm = 0
    dd += 1
  }
  return `${dd}°${String(mm).padStart(2, '0')}′${String(ss).padStart(2, '0')}″`
}
