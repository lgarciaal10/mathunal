import React from 'react';
import {AbsoluteFill, Audio, Easing, interpolate, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import TIM from './resuelto-timing.json';

export const FPS = 30;
const C = {bg:'#05060B',tx:'#F2F5FF',mu:'#8E9AC0',acc:'#E8632A',azul:'#6EA8FF',nar:'#FFA65C',ver:'#7CFF9B',amar:'#FFD84D',rojo:'#FF6B6B',card:'#0C101C'};
const serif = "'Literata', Georgia, serif", sans = "'Space Grotesk', system-ui, sans-serif", mono = "'IBM Plex Mono', ui-monospace, monospace";
const eo = Easing.out(Easing.cubic), eio = Easing.inOut(Easing.cubic);
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const pr = (t: number, a: number, b: number, e = eo) => interpolate(t, [a, b], [0, 1], {...clamp, easing: e});

type Sent = {t: string; a: number; b: number};
const SENT: Sent[] = (TIM as any).sent;
export const DURACION = Math.ceil(((TIM as any).fin) * FPS);
const AUDIO: string | null = (TIM as any).audio || null;

const Tex: React.FC<{tex: string; size: number; color?: string}> = ({tex, size, color}) => (
  <span style={{fontSize: size, color: color || C.tx, whiteSpace: 'nowrap'}} dangerouslySetInnerHTML={{__html: katex.renderToString(tex, {throwOnError: false})}} />
);

/* subtítulos palabra por palabra */
const Karaoke: React.FC<{t: number; u: number; w: number}> = ({t, u, w}) => {
  const words: {w: string; a: number; b: number}[] = [];
  SENT.forEach(s => {
    const ws = s.t.split(/\s+/), tot = ws.reduce((m, x) => m + x.length + 1, 0);
    let c = s.a;
    ws.forEach(x => { const d = (s.b - s.a) * (x.length + 1) / tot; words.push({w: x, a: c, b: c + d}); c += d; });
  });
  let idx = words.findIndex(x => t >= x.a && t < x.b); if (idx < 0) idx = t < words[0].a ? -1 : words.length - 1;
  if (idx < 0) return null;
  const g = Math.floor(idx / 4), grp = words.slice(g * 4, g * 4 + 4);
  const fin = words[words.length - 1].b + 0.3; if (t > fin) return null;
  return (
    <div style={{width: w, textAlign: 'center', fontFamily: sans, fontWeight: 700, fontSize: u * 3.3, lineHeight: 1.2, textShadow: '0 4px 18px rgba(0,0,0,.9)'}}>
      {grp.map((x, i) => { const cur = g * 4 + i === idx, past = g * 4 + i < idx; return <span key={i} style={{color: cur ? C.ver : past ? C.tx : 'rgba(242,245,255,.55)', marginRight: u * 0.9, display: 'inline-block', transform: cur ? 'scale(1.08)' : 'none'}}>{x.w}</span>; })}
    </div>
  );
};

/* una línea de la solución, con etiqueta de color */
const Linea: React.FC<{t: number; a: number; tag: string; col: string; tex: React.ReactNode; u: number}> = ({t, a, tag, col, tex, u}) => {
  const p = pr(t, a, a + 0.45), clip = pr(t, a, a + 0.9, Easing.out(Easing.quad));
  return (
    <div style={{opacity: p, transform: `translateY(${(1 - p) * u * 1.2}px)`, width: '100%'}}>
      <div style={{fontFamily: sans, fontWeight: 700, color: col, fontSize: u * 1.9, letterSpacing: 2, textTransform: 'uppercase', marginBottom: u * 0.5}}>{tag}</div>
      <div style={{clipPath: `inset(0 ${(1 - clip) * 100}% 0 0)`}}>{tex}</div>
    </div>
  );
};

/* gráfica con hueco */
const Grafica: React.FC<{t: number; a: number; W: number; H: number}> = ({t, a, W, H}) => {
  const xmin = -3, xmax = 6, ymin = -3, ymax = 6, pad = 60;
  const X = (x: number) => pad + (x - xmin) / (xmax - xmin) * (W - 2 * pad), Y = (y: number) => H - pad - (y - ymin) / (ymax - ymin) * (H - 2 * pad);
  const f = (x: number) => (x + 2) / (x + 1);
  const branch = (x0: number, x1: number, n: number) => { const p: string[] = []; for (let k = 0; k <= n; k++) { const x = x0 + (x1 - x0) * k / n; const y = Math.max(ymin, Math.min(ymax, f(x))); p.push(`${k ? 'L' : 'M'}${X(x).toFixed(1)} ${Y(y).toFixed(1)}`); } return p.join(' '); };
  const dr = pr(t, a, a + 1.6, Easing.inOut(Easing.quad)), hole = pr(t, a + 1.6, a + 2.2), pulse = 1 + 0.18 * Math.sin((t - a) * 6) * hole;
  return (
    <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`}>
      <path d={`M${X(0)} ${pad * 0.4} V${H - pad * 0.6} M${pad * 0.6} ${Y(0)} H${W - pad * 0.4}`} stroke={C.mu} strokeWidth={3} fill="none" opacity={0.6} />
      <path d={`M${X(-1)} ${pad * 0.4} V${H - pad * 0.6}`} stroke={C.rojo} strokeWidth={3} strokeDasharray="14 12" fill="none" opacity={0.7 * dr} />
      <text x={X(-1) - 14} y={pad * 0.9} fill={C.rojo} fontFamily={mono} fontSize={30} textAnchor="end" opacity={dr}>x = −1</text>
      {[ [-3, -1.12], [-0.9, 1.93], [2.07, 6] ].map(([x0, x1], i) => <path key={i} d={branch(x0, x1, 80)} pathLength={1} strokeDasharray="1" strokeDashoffset={1 - Math.min(1, Math.max(0, dr * 3 - i))} stroke={C.azul} strokeWidth={9} fill="none" strokeLinecap="round" />)}
      <circle cx={X(2)} cy={Y(f(2))} r={22 * pulse} fill={C.bg} stroke={C.amar} strokeWidth={7} opacity={hole} />
      <text x={X(2) + 34} y={Y(f(2)) - 70} fill={C.amar} fontFamily={mono} fontSize={38} fontWeight={600} opacity={hole}>hueco en x = 2</text>
      <text x={X(2) + 34} y={Y(f(2)) + 70} fill={C.mu} fontFamily={mono} fontSize={30} opacity={hole}>(2, 4/3)</text>
    </svg>
  );
};

export const Resuelto: React.FC = () => {
  const frame = useCurrentFrame(); const {width} = useVideoConfig(); const t = frame / FPS;
  const u = 20, pad = 70, W = width - pad * 2;
  const T = (i: number) => SENT[i].a;
  const sc1 = 1 - pr(t, T(5) - 0.3, T(5) + 0.4); // desaparece la solución para dar paso a la gráfica
  const fin = SENT[SENT.length - 1];
  const cancel = pr(t, T(3) + 0.8, T(3) + 1.4), caja = pr(t, T(4) + 0.4, T(4) + 1.1);
  const intro = pr(t, 0, 0.6);
  return (
    <AbsoluteFill style={{background: `radial-gradient(ellipse at 50% 30%, #0E1426 0%, ${C.bg} 70%)`, fontFamily: sans}}>
      {AUDIO && <Audio src={staticFile(AUDIO)} />}
      <div style={{position: 'absolute', left: pad, top: 80, display: 'flex', alignItems: 'center', gap: 16, fontFamily: serif, fontWeight: 900, fontSize: 46, color: C.tx, opacity: intro}}>
        <svg width={44} height={44} viewBox="0 0 24 24" fill="none" stroke={C.acc} strokeWidth={2.4} strokeLinecap="round"><path d="M16 3.5c-2.6 0-3.4 1.6-3.4 4.2v8.6c0 2.6-.8 4.2-3.4 4.2" /></svg>
        <span>MATH<span style={{color: C.acc}}>UNAL</span></span>
      </div>
      <div style={{position: 'absolute', right: pad, top: 92, fontFamily: sans, fontWeight: 600, color: C.mu, fontSize: 32, opacity: intro}}>Matemáticas Básicas</div>
      <div style={{position: 'absolute', left: pad, top: 230, width: W, display: 'flex', flexDirection: 'column', gap: 46, opacity: sc1}}>
        <Linea t={t} a={0.3} tag="Simplifica" col={C.mu} u={u} tex={<div style={{textAlign: 'center'}}><Tex tex={'\\dfrac{x^{2}-4}{x^{2}-x-2}'} size={u * 5.4} /></div>} />
        <Linea t={t} a={T(1) + 0.3} tag="Numerador, diferencia de cuadrados" col={C.azul} u={u} tex={<Tex tex={'x^{2}-4=\\textcolor{#FFA65C}{(x-2)}(x+2)'} size={u * 3.2} />} />
        <Linea t={t} a={T(2) + 0.3} tag="Denominador, dos números que suman −1" col={C.azul} u={u} tex={<Tex tex={'x^{2}-x-2=\\textcolor{#FFA65C}{(x-2)}(x+1)'} size={u * 3.2} />} />
        <Linea t={t} a={T(3) + 0.1} tag="Se cancela el factor repetido" col={C.ver} u={u} tex={
          <div style={{textAlign: 'center', position: 'relative', minHeight: u * 13}}>
            <div style={{position: 'absolute', inset: 0, opacity: 1 - cancel}}><Tex tex={'\\dfrac{\\textcolor{#FFA65C}{(x-2)}(x+2)}{\\textcolor{#FFA65C}{(x-2)}(x+1)}'} size={u * 4.6} /></div>
            <div style={{position: 'absolute', inset: 0, opacity: cancel}}><Tex tex={'\\dfrac{\\textcolor{#FF6B6B}{\\cancel{(x-2)}}(x+2)}{\\textcolor{#FF6B6B}{\\cancel{(x-2)}}(x+1)}'} size={u * 4.6} /></div>
          </div>} />
        <div style={{opacity: caja, transform: `scale(${0.92 + 0.08 * caja})`, alignSelf: 'center', border: `6px solid ${C.amar}`, borderRadius: 28, padding: '22px 52px', boxShadow: `0 0 ${60 * caja}px rgba(255,216,77,.25)`}}>
          <Tex tex={'\\dfrac{x+2}{x+1}'} size={u * 5} color={C.amar} />
        </div>
      </div>
      <div style={{position: 'absolute', left: pad, top: 240, width: W, opacity: pr(t, T(5) - 0.2, T(5) + 0.5) * (1 - pr(t, fin.a - 0.2, fin.a + 0.5))}}>
        <div style={{fontFamily: sans, fontWeight: 700, color: C.amar, fontSize: 38, letterSpacing: 2, textTransform: 'uppercase', marginBottom: 18}}>Pero ojo con el dominio</div>
        <Grafica t={t} a={T(5) + 0.3} W={W} H={1000} />
      </div>
      <div style={{position: 'absolute', left: pad, top: 640, width: W, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 44, opacity: pr(t, fin.a - 0.1, fin.a + 0.6)}}>
        <div style={{fontFamily: serif, fontWeight: 900, fontSize: 92, lineHeight: 1.08, textAlign: 'center', color: C.tx}}>Revisa siempre el <span style={{color: C.amar}}>dominio</span> antes de cancelar</div>
        <div style={{background: C.acc, color: '#05060B', fontFamily: sans, fontWeight: 700, fontSize: 60, padding: '24px 70px', borderRadius: 100}}>mathunal.com</div>
      </div>
      <div style={{position: 'absolute', left: pad, top: 1420, width: W}}><Karaoke t={t} u={u} w={W} /></div>
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 8, width: width * Math.min(1, t / (DURACION / FPS)), background: C.acc}} />
    </AbsoluteFill>
  );
};
