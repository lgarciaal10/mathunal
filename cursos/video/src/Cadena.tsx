import React from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import katex from 'katex';
import 'katex/dist/katex.min.css';

export const FPS = 30;
export const DURACION = 750; // 25 segundos
const C = {bg:'#060B1E',surf:'#0E1A3F',surf2:'#14224F',tx:'#EAF0FF',mu:'#9FB0DA',acc:'#E8632A',curve:'#8FB4F2',ok:'#22C55E',warn:'#FBBF24',bad:'#F87171'};
const serif = "'Literata', Georgia, serif", sans = "'Space Grotesk', system-ui, sans-serif", mono = "'IBM Plex Mono', ui-monospace, monospace";
const ease = Easing.inOut(Easing.cubic), easeOut = Easing.out(Easing.cubic);
const clamp = {extrapolateLeft:'clamp', extrapolateRight:'clamp'} as const;
const prog = (f: number, a: number, b: number, e = ease) => interpolate(f, [a, b], [0, 1], {...clamp, easing: e});

const Tex: React.FC<{tex: string; size: number; color?: string}> = ({tex, size, color}) => (
  <span style={{fontSize: size, color: color || C.tx, whiteSpace: 'nowrap'}} dangerouslySetInnerHTML={{__html: katex.renderToString(tex, {throwOnError: false, displayMode: false})}} />
);

const Brand: React.FC<{u: number}> = ({u}) => (
  <div style={{display:'flex', alignItems:'center', gap: u*0.9, fontFamily: serif, fontWeight: 900, fontSize: u*2.1, color: C.tx, letterSpacing: 1}}>
    <svg width={u*2.2} height={u*2.2} viewBox="0 0 24 24" fill="none" stroke={C.acc} strokeWidth={2.4} strokeLinecap="round"><path d="M16 3.5c-2.6 0-3.4 1.6-3.4 4.2v8.6c0 2.6-.8 4.2-3.4 4.2" /></svg>
    <span>MATH<span style={{color: C.acc}}>UNAL</span></span>
  </div>
);

const CAPS: {a: number; b: number; t: string}[] = [
  {a: 0, b: 90, t: 'La regla de la cadena sale en 3 de los 4 parciales del banco de MathUNAL.'},
  {a: 90, b: 270, t: 'Esta curva tiene pendiente 12 en x igual a 1. Mira cómo la secante se vuelve tangente.'},
  {a: 270, b: 480, t: 'Se deriva lo de afuera y se multiplica por la derivada de lo de adentro.'},
  {a: 480, b: 660, t: 'El error típico es olvidar ese último factor. Por eso sale 6 en vez de 12.'},
  {a: 660, b: 750, t: 'Practica con pistas de a una y preguntas reales de parciales.'},
];

const Caption: React.FC<{frame: number; u: number; w: number}> = ({frame, u, w}) => {
  const cur = CAPS.find(c => frame >= c.a && frame < c.b) || CAPS[CAPS.length - 1];
  const op = Math.min(prog(frame, cur.a, cur.a + 10, easeOut), 1 - prog(frame, cur.b - 8, cur.b));
  const y = (1 - prog(frame, cur.a, cur.a + 14, easeOut)) * u * 1.2;
  return (
    <div style={{width: w, textAlign: 'center', opacity: op, transform: `translateY(${y}px)`, fontFamily: sans, fontWeight: 500, fontSize: u * 2.5, lineHeight: 1.28, color: C.tx}}>
      <span style={{background: 'rgba(6,11,30,.82)', padding: `${u*0.35}px ${u*0.8}px`, borderRadius: u*1.2, WebkitBoxDecorationBreak: 'clone' as any}}>{cur.t}</span>
    </div>
  );
};

/* ---------- gráfica de la escena B ---------- */
const f = (x: number) => (2 * x + 1) ** 2;
const Grafica: React.FC<{frame: number; W: number; H: number}> = ({frame, W, H}) => {
  const xmin = -1.2, xmax = 2.2, ymin = 0, ymax = 30, pad = 70;
  const X = (x: number) => pad + (x - xmin) / (xmax - xmin) * (W - 2 * pad), Y = (y: number) => H - pad - (y - ymin) / (ymax - ymin) * (H - 2 * pad);
  const pts: string[] = [];
  for (let k = 0; k <= 160; k++) { const x = xmin + (xmax - xmin) * k / 160; pts.push(`${k ? 'L' : 'M'}${X(x).toFixed(1)} ${Y(f(x)).toFixed(1)}`); }
  const draw = prog(frame, 100, 150), showPt = prog(frame, 150, 165, easeOut);
  const t = prog(frame, 175, 245, Easing.inOut(Easing.quad)), h = Math.pow(0.01, t), m = 12 + 4 * h;
  const secOn = frame >= 168, tanOn = prog(frame, 245, 262);
  const line = (slope: number, color: string, w: number, op: number) => {
    const xa = xmin, xb = xmax, ya = 9 + slope * (xa - 1), yb = 9 + slope * (xb - 1);
    return <line x1={X(xa)} y1={Y(ya)} x2={X(xb)} y2={Y(yb)} stroke={color} strokeWidth={w} strokeLinecap="round" opacity={op} />;
  };
  const q = 1 + h;
  return (
    <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`} style={{overflow: 'hidden'}}>
      <defs><clipPath id="cp"><rect x={pad} y={pad * 0.4} width={W - 2 * pad + 10} height={H - pad * 1.4} /></clipPath></defs>
      <path d={`M${X(0)} ${pad * 0.3} V${H - pad} M${pad} ${Y(0)} H${W - pad * 0.5}`} stroke={C.mu} strokeWidth={3} fill="none" opacity={0.7} />
      {[1, 2].map(i => <g key={i}><path d={`M${X(i)} ${Y(0) - 8} v16`} stroke={C.mu} strokeWidth={3} /><text x={X(i)} y={Y(0) + 46} fill={C.mu} fontFamily={mono} fontSize={30} textAnchor="middle">{i}</text></g>)}
      {[10, 20, 30].map(i => <g key={i}><path d={`M${X(0) - 8} ${Y(i)} h16`} stroke={C.mu} strokeWidth={3} /><text x={X(0) - 20} y={Y(i) + 10} fill={C.mu} fontFamily={mono} fontSize={30} textAnchor="end">{i}</text></g>)}
      <g clipPath="url(#cp)">
        <path d={pts.join(' ')} pathLength={1} strokeDasharray="1" strokeDashoffset={1 - draw} stroke={C.curve} strokeWidth={9} fill="none" strokeLinecap="round" />
        {secOn && tanOn < 1 && line(m, C.warn, 7, 1 - tanOn * 0.6)}
        {tanOn > 0 && line(12, C.ok, 10, tanOn)}
        {secOn && <circle cx={X(q)} cy={Y(f(q))} r={17} fill={C.warn} opacity={1 - tanOn * 0.4} />}
        <circle cx={X(1)} cy={Y(9)} r={20 * showPt} fill={C.acc} />
      </g>
      {showPt > 0.5 && <text x={X(1) + 28} y={Y(9) + 54} fill={C.tx} fontFamily={mono} fontSize={34}>(1, 9)</text>}
    </svg>
  );
};

const Lecturas: React.FC<{frame: number; u: number}> = ({frame, u}) => {
  const t = prog(frame, 175, 245, Easing.inOut(Easing.quad)), h = Math.pow(0.01, t), m = 12 + 4 * h;
  const op = prog(frame, 165, 180, easeOut);
  const box = (lab: string, val: string, col: string) => (
    <div style={{flex: 1, background: C.surf2, borderRadius: u * 1.4, padding: `${u*1.1}px ${u*1.5}px`}}>
      <div style={{fontFamily: sans, color: C.mu, fontSize: u * 1.9}}>{lab}</div>
      <div style={{fontFamily: mono, color: col, fontSize: u * 2.7, fontWeight: 600}}>{val}</div>
    </div>
  );
  return <div style={{display: 'flex', gap: u * 1.2, opacity: op}}>{box('Distancia h', `h = ${h.toFixed(2)}`, C.warn)}{box('Pendiente de la secante', `${m.toFixed(3)}`, C.bad)}</div>;
};

/* ---------- escena C y D ---------- */
const Regla: React.FC<{frame: number; u: number}> = ({frame, u}) => {
  const a = prog(frame, 280, 310, easeOut), b = prog(frame, 320, 350, easeOut), c = prog(frame, 360, 395, easeOut), d = prog(frame, 410, 450, easeOut);
  const card = (op: number, children: React.ReactNode, extra?: React.CSSProperties) => <div style={{background: C.surf, borderRadius: u * 1.8, padding: `${u * 1.5}px ${u * 2}px`, opacity: op, transform: `translateY(${(1 - op) * u * 1.5}px)`, ...extra}}>{children}</div>;
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap: u * 2.2, width: '100%'}}>
      {card(a, <div style={{textAlign: 'center'}}><Tex tex={'f(x)=\\textcolor{#8FB4F2}{(\\textcolor{#E8632A}{2x+1})^{2}}'} size={u * 3.7} /></div>)}
      {card(b, <div style={{display: 'flex', justifyContent: 'space-around', fontFamily: sans, fontSize: u * 2.2}}><span style={{color: C.curve}}>● Afuera, elevar al cuadrado</span><span style={{color: C.acc}}>● Adentro, 2x + 1</span></div>)}
      {card(c, <div style={{textAlign: 'center'}}><Tex tex={"f'(x)=\\textcolor{#8FB4F2}{2(2x+1)}\\cdot\\textcolor{#E8632A}{2}"} size={u * 3.7} /></div>)}
      {card(d, <div style={{textAlign: 'center'}}><Tex tex={"f'(1)=2\\cdot 3\\cdot 2=\\textcolor{#22C55E}{12}"} size={u * 3.7} /></div>)}
    </div>
  );
};
const Error: React.FC<{frame: number; u: number}> = ({frame, u}) => {
  const a = prog(frame, 490, 520, easeOut), b = prog(frame, 545, 575, easeOut), x = prog(frame, 575, 590), p = prog(frame, 600, 640);
  const row = (op: number, col: string, sym: string, tex: string, extra?: React.ReactNode) => (
    <div style={{display: 'flex', alignItems: 'center', gap: u * 1.6, background: C.surf, borderRadius: u * 1.8, padding: `${u * 1.7}px ${u * 2}px`, opacity: op, transform: `translateY(${(1 - op) * u}px)`, border: `4px solid ${col}`}}>
      <span style={{fontFamily: sans, fontWeight: 700, color: col, fontSize: u * 3.6, width: u * 3.6}}>{sym}</span>
      <div style={{position: 'relative'}}><Tex tex={tex} size={u * 3.4} />{extra}</div>
    </div>
  );
  return (
    <div style={{display: 'flex', flexDirection: 'column', gap: u * 1.8, width: '100%'}}>
      {row(a, C.bad, '✗', "f'(1)=2\\cdot 3=6", <div style={{position: 'absolute', left: 0, top: '52%', height: 6, width: `${x * 100}%`, background: C.bad, borderRadius: 4}} />)}
      {row(b, C.ok, '✓', "f'(1)=2\\cdot 3\\cdot \\textcolor{#E8632A}{2}=12")}
      <div style={{fontFamily: sans, fontSize: u * 2.4, color: C.acc, textAlign: 'center', opacity: p, transform: `scale(${0.9 + 0.1 * p})`}}>Falta la derivada de lo de adentro</div>
    </div>
  );
};

export const Cadena: React.FC<{formato: 'vertical' | 'horizontal'}> = ({formato}) => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const V = formato === 'vertical', u = V ? 20 : 14;
  const sceneOp = (a: number, b: number) => Math.min(prog(frame, a, a + 12, easeOut), 1 - prog(frame, b - 10, b));
  const pad = V ? 70 : 90;
  const innerW = width - pad * 2;
  const bar = frame / DURACION;
  const cta = prog(frame, 665, 700, easeOut);
  return (
    <AbsoluteFill style={{background: C.bg, fontFamily: sans}}>
      <div style={{position: 'absolute', left: pad, top: V ? 70 : 45}}><Brand u={u} /></div>
      <div style={{position: 'absolute', right: pad, top: V ? 82 : 55, fontFamily: sans, color: C.mu, fontSize: u * 1.7}}>Cálculo Diferencial</div>
      <div style={{position: 'absolute', left: pad, top: V ? 200 : 140, width: innerW, height: V ? 1100 : 640}}>
        {/* A */}
        <div style={{position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: u * 1.4, opacity: sceneOp(0, 100)}}>
          <div style={{fontFamily: serif, fontWeight: 900, fontSize: u * (V ? 6.6 : 5.6), lineHeight: 1.05, color: C.tx, transform: `translateY(${(1 - prog(frame, 0, 24, easeOut)) * u * 2}px)`, opacity: prog(frame, 0, 20, easeOut)}}>La regla de la cadena</div>
          <div style={{fontFamily: mono, fontSize: u * 3.2, color: C.acc, opacity: prog(frame, 22, 44, easeOut)}}>f(x) = (2x + 1)²</div>
        </div>
        {/* B */}
        <div style={{position: 'absolute', inset: 0, display: 'flex', flexDirection: V ? 'column' : 'row', gap: u * 1.4, opacity: sceneOp(90, 275)}}>
          <div style={{flex: V ? '0 0 auto' : 1}}><Grafica frame={frame} W={V ? innerW : innerW * 0.58} H={V ? 780 : 600} /></div>
          <div style={{flex: 1, display: 'flex', alignItems: V ? 'flex-start' : 'center'}}><div style={{width: '100%'}}><Lecturas frame={frame} u={u} /></div></div>
        </div>
        {/* C */}
        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', opacity: sceneOp(270, 485)}}><Regla frame={frame} u={u * (V ? 1 : 0.8)} /></div>
        {/* D */}
        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', opacity: sceneOp(480, 665)}}><Error frame={frame} u={u * (V ? 1 : 0.8)} /></div>
        {/* E */}
        <div style={{position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: u * 2, opacity: prog(frame, 660, 680, easeOut)}}>
          <div style={{fontFamily: serif, fontWeight: 900, fontSize: u * (V ? 5.2 : 4.6), textAlign: 'center', color: C.tx, lineHeight: 1.1, transform: `translateY(${(1 - cta) * u * 2}px)`}}>Practica con preguntas reales de parciales</div>
          <div style={{background: C.acc, color: '#060B1E', fontFamily: sans, fontWeight: 700, fontSize: u * 3.2, padding: `${u * 1.3}px ${u * 3.4}px`, borderRadius: u * 5, transform: `scale(${0.9 + 0.1 * cta})`, opacity: cta}}>mathunal.com</div>
        </div>
      </div>
      <div style={{position: 'absolute', left: pad, bottom: V ? 170 : 70}}><Caption frame={frame} u={u} w={innerW} /></div>
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 10, width: width * bar, background: C.acc}} />
    </AbsoluteFill>
  );
};
