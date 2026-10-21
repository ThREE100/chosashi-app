"""仮のアバター（SVG）。口を閉じた絵と開いた絵の2枚を切り替えて口パクさせる。

本番では、キャラクターシートから作った画像（口を閉じた PNG と開いた PNG の2枚）に差し替えられる。
台本の characters.<key>.images に {"closed": "...png", "open": "...png"} を書けば、そちらが優先される。
"""


def tori_svg(mouth_open: bool) -> str:
    beak = (
        '<path d="M150 150 L185 160 L150 168 Z" fill="#f59e0b"/>'
        '<path d="M150 172 L180 176 L150 190 Z" fill="#d97706"/>'
        if mouth_open else
        '<path d="M150 152 L190 166 L150 178 Z" fill="#f59e0b"/><path d="M152 166 L188 166" stroke="#b45309" stroke-width="2"/>'
    )
    return f'''<svg viewBox="0 0 260 300" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="130" cy="285" rx="80" ry="10" fill="#00000018"/>
  <path d="M95 270 l-10 18 M110 270 l0 20 M150 270 l0 20 M165 270 l10 18" stroke="#f59e0b" stroke-width="7" stroke-linecap="round"/>
  <ellipse cx="130" cy="185" rx="105" ry="95" fill="#f8fafc" stroke="#475569" stroke-width="4"/>
  <ellipse cx="130" cy="215" rx="62" ry="55" fill="#fde68a"/>
  <path d="M30 175 q-25 45 15 75 q15-35 5-75 z" fill="#e2e8f0" stroke="#475569" stroke-width="3"/>
  <path d="M230 175 q25 45 -15 75 q-15-35 -5-75 z" fill="#e2e8f0" stroke="#475569" stroke-width="3"/>
  <path d="M115 92 q10-30 25-5 q10-25 20 5" fill="none" stroke="#475569" stroke-width="5" stroke-linecap="round"/>
  <circle cx="100" cy="140" r="15" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="104" cy="142" r="7" fill="#0f172a"/>
  <circle cx="160" cy="140" r="15" fill="#fff" stroke="#334155" stroke-width="3"/><circle cx="164" cy="142" r="7" fill="#0f172a"/>
  <path d="M82 118 l30 8 M178 118 l-30 8" stroke="#334155" stroke-width="5" stroke-linecap="round"/>
  <circle cx="80" cy="172" r="10" fill="#fca5a5" opacity=".6"/><circle cx="182" cy="172" r="10" fill="#fca5a5" opacity=".6"/>
  {beak}
</svg>'''


def aiko_svg(mouth_open: bool) -> str:
    mouth = ('<ellipse cx="130" cy="128" rx="9" ry="8" fill="#9f1239"/><ellipse cx="130" cy="132" rx="5" ry="3" fill="#fb7185"/>'
             if mouth_open else '<path d="M120 127 q10 7 20 0" stroke="#9f1239" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
    stripes = "".join(f'<line x1="{x}" y1="170" x2="{x}" y2="300" stroke="#93c5fd" stroke-width="2.4"/>' for x in range(108, 156, 7))
    return f'''<svg viewBox="0 0 260 300" xmlns="http://www.w3.org/2000/svg">
  <path d="M60 300 q0-110 70-125 q70 15 70 125 z" fill="#1e3a8a"/>
  <path d="M104 170 L130 300 L156 170 z" fill="#eff6ff"/>
  <clipPath id="b"><path d="M104 170 L130 300 L156 170 z"/></clipPath><g clip-path="url(#b)">{stripes}</g>
  <path d="M104 170 L130 235 L95 300 L70 300 q5-100 34-130z" fill="#172554"/>
  <path d="M156 170 L130 235 L165 300 L190 300 q-5-100 -34-130z" fill="#172554"/>
  <rect x="117" y="140" width="26" height="30" fill="#fcd9bd"/>
  <path d="M62 120 q-6-95 68-98 q74 3 68 98 q-4 35 -14 52 l-6-60 q-48 -6 -96 0 l-6 60 q-10-17-14-52z" fill="#1f2937"/>
  <ellipse cx="130" cy="98" rx="52" ry="58" fill="#fde2cc"/>
  <path d="M78 92 q15-62 104-14 q-6-48 -52-50 q-50 2 -52 64z" fill="#1f2937"/>
  <ellipse cx="110" cy="102" rx="6" ry="8" fill="#1e293b"/><ellipse cx="150" cy="102" rx="6" ry="8" fill="#1e293b"/>
  <circle cx="112" cy="99" r="2" fill="#fff"/><circle cx="152" cy="99" r="2" fill="#fff"/>
  <path d="M100 88 q10-5 20 0 M140 88 q10-5 20 0" stroke="#1f2937" stroke-width="3" fill="none" stroke-linecap="round"/>
  <circle cx="98" cy="118" r="8" fill="#fca5a5" opacity=".5"/><circle cx="162" cy="118" r="8" fill="#fca5a5" opacity=".5"/>
  {mouth}
</svg>'''


BUILTIN = {"tori": tori_svg, "aiko": aiko_svg}
