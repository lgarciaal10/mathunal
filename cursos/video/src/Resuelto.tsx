import React from 'react';
import {AbsoluteFill, Audio, Easing, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import TIM from './resuelto-timing.json';

export const FPS = 30;
const C = {bg:'#05060B',tx:'#F2F5FF',mu:'#8E9AC0',acc:'#E8632A',azul:'#6EA8FF',nar:'#FFA65C',ver:'#7CFF9B',amar:'#FFD84D',rojo:'#FF6B6B'};
const serif = "'Literata', Georgia, serif", sans = "'Space Grotesk', system-ui, sans-serif", mono = "'IBM Plex Mono', ui-monospace, monospace";
const eo = Easing.out(Easing.cubic);
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const pr = (t: number, a: number, b: number, e = eo) => interpolate(t, [a, b], [0, 1], {...clamp, easing: e});

type Sent = {t: string; a: number; b: number};
const SENT: Sent[] = (TIM as any).sent;
const FIN: number = (TIM as any).fin;
export const DURACION = Math.ceil(FIN * FPS);
const AUDIO: string | null = (TIM as any).audio || null;

const Tex: React.FC<{tex: string; size: number; color?: string}> = ({tex, size, color}) => (
  <span style={{fontSize: size, color: color || C.tx, whiteSpace: 'nowrap'}} dangerouslySetInnerHTML={{__html: katex.renderToString(tex, {throwOnError: false})}} />
);
const Pop: React.FC<{t: number; a: number; children: React.ReactNode; from?: number; style?: React.CSSProperties}> = ({t, a, children, from = 0.5, style}) => {
  const {fps} = useVideoConfig();
  const s = spring({frame: Math.max(0, (t - a) * fps), fps, config: {damping: 11, mass: 0.7}});
  return <div style={{opacity: pr(t, a, a + 0.15), transform: `scale(${from + (1 - from) * s})`, transformOrigin: 'center', color: C.tx, ...style}}>{children}</div>;
};

/* fondo vivo: cuadrícula que se desplaza, brillo que respira y símbolos que suben */
const SIMB = ['x', '²', '÷', 'π', '∫', '√', '+', 'f', '=', '∑', 'y', 'dx', '≠', '∞'];
const Fondo: React.FC<{t: number}> = ({t}) => (
  <AbsoluteFill>
    <div style={{position: 'absolute', inset: 0, background: `radial-gradient(ellipse at ${50 + 12 * Math.sin(t * 0.35)}% ${28 + 6 * Math.cos(t * 0.3)}%, #131B36 0%, ${C.bg} 68%)`}} />
    <div style={{position: 'absolute', inset: 0, opacity: 0.10, backgroundImage: 'linear-gradient(#6EA8FF 1px, transparent 1px), linear-gradient(90deg, #6EA8FF 1px, transparent 1px)', backgroundSize: '90px 90px', backgroundPosition: `${(t * 14) % 90}px ${(t * 9) % 90}px`, WebkitMaskImage: 'radial-gradient(ellipse at 50% 40%, #000 20%, transparent 75%)'}} />
    {SIMB.map((s, i) => { const x = (i * 197) % 1000 + 30, sp = 22 + (i % 5) * 7, y = ((i * 311 + 1900 - t * sp) % 2000 + 2000) % 2000 - 40; return <div key={i} style={{position: 'absolute', left: x, top: y, fontFamily: serif, fontStyle: 'italic', fontSize: 70 + (i % 4) * 26, color: i % 3 ? C.azul : C.acc, opacity: 0.07}}>{s}</div>; })}
  </AbsoluteFill>
);

/* destellos */
const Chispas: React.FC<{t: number; a: number; x: number; y: number; col: string; n?: number}> = ({t, a, x, y, col, n = 16}) => {
  const k = t - a; if (k < 0 || k > 1.1) return null;
  return <>{Array.from({length: n}).map((_, i) => { const ang = i * 2.399, v = 190 + (i % 4) * 70, d = v * (1 - Math.pow(1 - Math.min(1, k / 0.9), 3)); return <div key={i} style={{position: 'absolute', left: x + Math.cos(ang) * d, top: y + Math.sin(ang) * d, width: 14 - (i % 3) * 3, height: 14 - (i % 3) * 3, borderRadius: 20, background: col, opacity: 1 - k / 1.1}} />; })}</>;
};

const Karaoke: React.FC<{t: number; w: number}> = ({t, w}) => {
  const words: {w: string; a: number; b: number}[] = [];
  SENT.forEach(s => {
    const ws = s.t.split(/\s+/), tot = ws.reduce((m, x) => m + x.length + 1, 0); let c = s.a;
    ws.forEach(x => { const d = (s.b - s.a) * (x.length + 1) / tot; words.push({w: x, a: c, b: c + d}); c += d; });
  });
  let idx = words.findIndex(x => t >= x.a && t < x.b); if (idx < 0) { const nx = words.findIndex(x => x.a > t); idx = nx <= 0 ? -1 : nx - 1; }
  if (idx < 0 || t > words[words.length - 1].b + 0.4) return null;
  const g = Math.floor(idx / 4), grp = words.slice(g * 4, g * 4 + 4);
  return (
    <div style={{width: w, textAlign: 'center', fontFamily: sans, fontWeight: 700, fontSize: 66, lineHeight: 1.2, textShadow: '0 4px 18px rgba(0,0,0,.95)'}}>
      {grp.map((x, i) => { const cur = g * 4 + i === idx, past = g * 4 + i < idx; return <span key={i} style={{color: cur ? C.ver : past ? C.tx : 'rgba(242,245,255,.5)', marginRight: 18, display: 'inline-block', transform: cur ? 'scale(1.1)' : 'none'}}>{x.w}</span>; })}
    </div>
  );
};

const Etiqueta: React.FC<{t: number; a: number; col: string; children: string}> = ({t, a, col, children}) => (
  <div style={{opacity: pr(t, a, a + 0.3), transform: `translateX(${(1 - pr(t, a, a + 0.4)) * -40}px)`, fontFamily: sans, fontWeight: 700, color: col, fontSize: 36, letterSpacing: 2, textTransform: 'uppercase', marginBottom: 6}}>{children}</div>
);

const Grafica: React.FC<{t: number; a: number; W: number; H: number}> = ({t, a, W, H}) => {
  const xmin = -3, xmax = 6, ymin = -3, ymax = 6, pad = 60;
  const X = (x: number) => pad + (x - xmin) / (xmax - xmin) * (W - 2 * pad), Y = (y: number) => H - pad - (y - ymin) / (ymax - ymin) * (H - 2 * pad);
  const f = (x: number) => (x + 2) / (x + 1);
  const branch = (x0: number, x1: number, n: number) => { const p: string[] = []; for (let k = 0; k <= n; k++) { const x = x0 + (x1 - x0) * k / n; const y = Math.max(ymin, Math.min(ymax, f(x))); p.push(`${k ? 'L' : 'M'}${X(x).toFixed(1)} ${Y(y).toFixed(1)}`); } return p.join(' '); };
  const dr = pr(t, a, a + 1.4, Easing.inOut(Easing.quad));
  const xm = interpolate(t, [a + 1.4, a + 4.4], [-0.5, 4.5], {...clamp, easing: Easing.inOut(Easing.quad)});
  const mov = pr(t, a + 1.4, a + 1.7), enHueco = Math.abs(xm - 2) < 0.09;
  const hole = pr(t, a + 2.6, a + 3.0), pulse = 1 + 0.2 * Math.sin((t - a) * 7) * hole;
  const dotY = f(xm);
  return (
    <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`}>
      <path d={`M${X(0)} ${pad * 0.3} V${H - pad * 0.5} M${pad * 0.5} ${Y(0)} H${W - pad * 0.3}`} stroke={C.mu} strokeWidth={3} fill="none" opacity={0.6} />
      <path d={`M${X(-1)} ${pad * 0.3} V${H - pad * 0.5}`} stroke={C.rojo} strokeWidth={3} strokeDasharray="14 12" fill="none" opacity={0.7 * dr} />
      <text x={X(-1) - 14} y={pad * 0.8} fill={C.rojo} fontFamily={mono} fontSize={32} textAnchor="end" opacity={dr}>x = −1</text>
      {[[-3, -1.12], [-0.9, 1.93], [2.07, 6]].map(([x0, x1], i) => <path key={i} d={branch(x0, x1, 80)} pathLength={1} strokeDasharray="1" strokeDashoffset={1 - Math.min(1, Math.max(0, dr * 3 - i))} stroke={C.azul} strokeWidth={9} fill="none" strokeLinecap="round" />)}
      {mov > 0 && !enHueco && xm > -0.9 && <g opacity={mov}><line x1={X(xm)} y1={Y(0)} x2={X(xm)} y2={Y(dotY)} stroke={C.ver} strokeWidth={4} strokeDasharray="8 8" /><circle cx={X(xm)} cy={Y(dotY)} r={19} fill={C.ver} /></g>}
      <circle cx={X(2)} cy={Y(f(2))} r={22 * pulse} fill={C.bg} stroke={C.amar} strokeWidth={7} opacity={hole} />
      <text x={X(2) + 36} y={Y(f(2)) - 64} fill={C.amar} fontFamily={mono} fontSize={40} fontWeight={600} opacity={hole}>¡hueco en x = 2!</text>
      <text x={X(2) + 36} y={Y(f(2)) + 70} fill={C.mu} fontFamily={mono} fontSize={32} opacity={hole}>aquí no hay valor</text>
    </svg>
  );
};

export const Resuelto: React.FC = () => {
  const frame = useCurrentFrame(); const {width} = useVideoConfig(); const t = frame / FPS;
  const pad = 70, W = width - pad * 2;
  const A = (i: number) => SENT[i].a, B = (i: number) => SENT[i].b;
  const win = (a: number, b: number) => Math.min(pr(t, a, a + 0.35), 1 - pr(t, b - 0.3, b + 0.2));
  const sol = Math.min(pr(t, A(2) - 0.2, A(2) + 0.3), 1 - pr(t, A(8) - 0.3, A(8) + 0.2));
  const shake = Math.sin(t * 38) * 6 * (1 - pr(t, 1.2, 1.9));
  const cancel = pr(t, A(6) + 0.9, A(6) + 1.5), mover = pr(t, A(6) + 0.2, A(6) + 0.9, Easing.inOut(Easing.cubic));
  const up = pr(t, A(3) - 0.1, A(3) + 0.6, Easing.inOut(Easing.cubic));
  const glow = (t > A(5) && t < A(6) + 0.9) ? 0.55 + 0.45 * Math.sin((t - A(5)) * 7) : 0;
  const scene = SENT.findIndex((s, i) => t >= s.a && (i === SENT.length - 1 || t < SENT[i + 1].a));
  return (
    <AbsoluteFill style={{fontFamily: sans}}>
      <Fondo t={t} />
      {AUDIO && <Audio src={staticFile(AUDIO)} />}
      <div style={{position: 'absolute', left: pad, top: 80, display: 'flex', alignItems: 'center', gap: 16, fontFamily: serif, fontWeight: 900, fontSize: 46, color: C.tx}}>
        <svg width={44} height={44} viewBox="0 0 24 24" fill="none" stroke={C.acc} strokeWidth={2.4} strokeLinecap="round"><path d="M16 3.5c-2.6 0-3.4 1.6-3.4 4.2v8.6c0 2.6-.8 4.2-3.4 4.2" /></svg>
        <span>MATH<span style={{color: C.acc}}>UNAL</span></span>
      </div>
      <div style={{position: 'absolute', right: pad, top: 92, display: 'flex', gap: 10}}>{SENT.map((_, i) => <div key={i} style={{width: i === scene ? 34 : 12, height: 12, borderRadius: 8, background: i <= scene ? C.acc : 'rgba(255,255,255,.18)', transition: 'none'}} />)}</div>

      {/* 0 gancho */}
      <div style={{position: 'absolute', left: pad, top: 330, width: W, opacity: win(A(0), B(0) + 0.2), display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60}}>
        <div style={{fontFamily: serif, fontWeight: 900, fontSize: 98, lineHeight: 1.06, textAlign: 'center', color: C.tx}}>¿Cancelaste <span style={{color: C.rojo}}>así</span>?</div>
        <div style={{position: 'relative', transform: `translateX(${shake}px)`}}>
          <Pop t={t} a={0.5}><Tex tex={'\\dfrac{x+3}{x}\\;=\\;\\dfrac{\\textcolor{#FF6B6B}{\\cancel{x}}+3}{\\textcolor{#FF6B6B}{\\cancel{x}}}\\;=\\;3'} size={80} /></Pop>
          <Pop t={t} a={1.2} from={2.2} style={{position: 'absolute', right: 10, top: 190, fontFamily: sans, fontWeight: 900, fontSize: 150, color: C.rojo, textShadow: '0 0 40px rgba(255,107,107,.6)'}}>✗</Pop>
        </div>
      </div>

      {/* 1 regla */}
      <div style={{position: 'absolute', left: pad, top: 280, width: W, opacity: win(A(1), B(1)), display: 'flex', flexDirection: 'column', gap: 54}}>
        <Pop t={t} a={A(1) + 0.1} style={{fontFamily: serif, fontWeight: 900, fontSize: 84, lineHeight: 1.08, textAlign: 'center'}}>Solo se cancelan <span style={{color: C.ver}}>factores</span></Pop>
        <Pop t={t} a={A(1) + 1.8} from={0.8} style={{border: `6px solid ${C.ver}`, borderRadius: 32, padding: '34px 30px', background: 'rgba(124,255,155,.07)', boxShadow: `0 0 ${50 * (0.5 + 0.5 * Math.sin(t * 5))}px rgba(124,255,155,.25)`}}>
          <div style={{fontFamily: sans, fontWeight: 700, fontSize: 40, color: C.ver, marginBottom: 12}}>✓ Se multiplican, sí se cancelan</div>
          <div style={{textAlign: 'center'}}><Tex tex={'\\dfrac{\\textcolor{#7CFF9B}{\\cancel{x}}\\cdot 3}{\\textcolor{#7CFF9B}{\\cancel{x}}\\cdot 5}=\\dfrac{3}{5}'} size={86} /></div>
        </Pop>
        <Pop t={t} a={A(1) + 4.0} from={0.8} style={{border: `6px solid ${C.rojo}`, borderRadius: 32, padding: '34px 30px', background: 'rgba(255,107,107,.07)'}}>
          <div style={{fontFamily: sans, fontWeight: 700, fontSize: 40, color: C.rojo, marginBottom: 12}}>✗ Se suman, no se cancelan</div>
          <div style={{textAlign: 'center'}}><Tex tex={'\\dfrac{x+3}{x}\\ne 3'} size={86} /></div>
        </Pop>
      </div>

      {/* solución */}
      <div style={{position: 'absolute', left: 0, top: 0, width: '100%', height: 1400, opacity: sol}}>
        <div style={{position: 'absolute', left: pad, width: W, top: 330 - 120 * up, textAlign: 'center', transform: `scale(${1 - 0.36 * up})`, transformOrigin: 'top center'}}>
          <Pop t={t} a={A(2) + 0.2} from={0.3}><Tex tex={'\\dfrac{x^{2}-4}{x^{2}-x-2}'} size={128} /></Pop>
        </div>
        <div style={{position: 'absolute', left: pad, width: W, top: 450}}>
          <Etiqueta t={t} a={A(3) + 0.8} col={C.azul}>Arriba, diferencia de cuadrados</Etiqueta>
          <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
            <div style={{opacity: pr(t, A(3) + 0.8, A(3) + 1.2)}}><Tex tex={'x^{2}-4\\;=\\;'} size={60} /></div>
            <Pop t={t} a={A(3) + 2.2}><Tex tex={'\\textcolor{#FFA65C}{(x-2)}'} size={60} /></Pop>
            <Pop t={t} a={A(3) + 3.2}><Tex tex={'\\textcolor{#6EA8FF}{(x+2)}'} size={60} /></Pop>
          </div>
        </div>
        <div style={{position: 'absolute', left: pad, width: W, top: 640}}>
          <Etiqueta t={t} a={A(4) + 0.5} col={C.azul}>Abajo, suman −1 y multiplican −2</Etiqueta>
          <div style={{position: 'absolute', right: 0, top: -6, display: 'flex', gap: 14}}>
            <Pop t={t} a={A(4) + 2.0} from={0.2} style={{background: C.nar, color: '#05060B', borderRadius: 40, padding: '4px 24px', fontFamily: mono, fontWeight: 700, fontSize: 44}}>−2</Pop>
            <Pop t={t} a={A(4) + 2.6} from={0.2} style={{background: C.azul, color: '#05060B', borderRadius: 40, padding: '4px 24px', fontFamily: mono, fontWeight: 700, fontSize: 44}}>+1</Pop>
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: 14}}>
            <div style={{opacity: pr(t, A(4) + 0.5, A(4) + 0.9)}}><Tex tex={'x^{2}-x-2\\;=\\;'} size={60} /></div>
            <Pop t={t} a={A(4) + 3.6}><Tex tex={'\\textcolor{#FFA65C}{(x-2)}'} size={60} /></Pop>
            <Pop t={t} a={A(4) + 4.4}><Tex tex={'\\textcolor{#6EA8FF}{(x+1)}'} size={60} /></Pop>
          </div>
        </div>
        {/* fracción con factores, protagonista desde la frase 5 */}
        <div style={{position: 'absolute', left: pad, width: W, top: 830, height: 260, display: 'flex', justifyContent: 'center', opacity: pr(t, A(5) + 0.2, A(5) + 0.7)}}>
          <div style={{position: 'relative'}}>
            <div style={{opacity: 1 - cancel}}><Tex tex={'\\dfrac{\\textcolor{#FFA65C}{(x-2)}(x+2)}{\\textcolor{#FFA65C}{(x-2)}(x+1)}'} size={104} /></div>
            <div style={{position: 'absolute', inset: 0, opacity: cancel}}><Tex tex={'\\dfrac{\\textcolor{#FF6B6B}{\\cancel{(x-2)}}(x+2)}{\\textcolor{#FF6B6B}{\\cancel{(x-2)}}(x+1)}'} size={104} /></div>
            <div style={{position: 'absolute', inset: -22, borderRadius: 30, border: `5px solid rgba(255,166,92,${glow})`, boxShadow: `0 0 ${60 * glow}px rgba(255,166,92,${0.35 * glow})`}} />
            {mover > 0 && mover < 1 && <div style={{position: 'absolute', left: -150, top: 70, fontFamily: sans, fontWeight: 700, fontSize: 44, color: C.ver, opacity: Math.sin(mover * Math.PI)}}>÷ (x−2)</div>}
          </div>
        </div>
        <Chispas t={t} a={A(6) + 1.0} x={540} y={950} col={C.rojo} />
        <div style={{position: 'absolute', left: pad, width: W, top: 1160, display: 'flex', justifyContent: 'center'}}>
          <Pop t={t} a={A(7) + 0.3} from={0.2} style={{border: `7px solid ${C.amar}`, borderRadius: 32, padding: '20px 64px', boxShadow: '0 0 70px rgba(255,216,77,.28)'}}><Tex tex={'\\dfrac{x+2}{x+1}'} size={88} color={C.amar} /></Pop>
        </div>
        <Chispas t={t} a={A(7) + 0.45} x={540} y={1250} col={C.amar} n={22} />
      </div>

      {/* 8 gráfica */}
      <div style={{position: 'absolute', left: pad, top: 250, width: W, opacity: win(A(8), B(8) + 0.2)}}>
        <div style={{fontFamily: sans, fontWeight: 700, color: C.amar, fontSize: 44, letterSpacing: 2, textTransform: 'uppercase', marginBottom: 10}}>Pero ojo con el dominio</div>
        <Grafica t={t} a={A(8) + 0.5} W={W} H={1000} />
      </div>

      {/* 9 dominio */}
      <div style={{position: 'absolute', left: pad, top: 360, width: W, opacity: win(A(9), B(9) + 0.2), display: 'flex', flexDirection: 'column', gap: 44}}>
        <Pop t={t} a={A(9) + 0.1} style={{fontFamily: serif, fontWeight: 900, fontSize: 90, lineHeight: 1.08, textAlign: 'center'}}>Antes de cancelar, revisa el <span style={{color: C.amar}}>dominio</span></Pop>
        {[['x ≠ 2', 'se anula el factor x − 2'], ['x ≠ −1', 'se anula el factor x + 1']].map(([a, b], i) => (
          <Pop key={i} t={t} a={A(9) + 1.2 + i * 0.8} from={0.7} style={{display: 'flex', alignItems: 'center', gap: 28, border: `5px solid ${C.amar}`, borderRadius: 28, padding: '22px 34px', background: 'rgba(255,216,77,.06)'}}>
            <span style={{fontFamily: mono, fontWeight: 700, fontSize: 70, color: C.amar}}>{a}</span><span style={{fontFamily: sans, fontSize: 42, color: C.mu}}>{b}</span>
          </Pop>))}
      </div>

      {/* 10 cierre */}
      <div style={{position: 'absolute', left: pad, top: 460, width: W, opacity: pr(t, A(10) - 0.1, A(10) + 0.4), display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 50}}>
        <Pop t={t} a={A(10)} style={{fontFamily: serif, fontWeight: 900, fontSize: 96, lineHeight: 1.08, textAlign: 'center'}}>Practica con preguntas <span style={{color: C.acc}}>reales</span> de parciales</Pop>
        <Pop t={t} a={A(10) + 0.5} from={0.6} style={{background: C.acc, color: '#05060B', fontFamily: sans, fontWeight: 700, fontSize: 64, padding: '26px 76px', borderRadius: 100, boxShadow: `0 0 ${70 * (0.5 + 0.5 * Math.sin(t * 6))}px rgba(232,99,42,.45)`}}>mathunal.com</Pop>
      </div>

      <div style={{position: 'absolute', left: pad, top: 1490, width: W}}><Karaoke t={t} w={W} /></div>
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 8, width: width * Math.min(1, t / FIN), background: C.acc}} />
    </AbsoluteFill>
  );
};
