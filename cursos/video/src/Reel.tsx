import React, {useMemo} from 'react';
import {AbsoluteFill, Audio, Easing, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import katex from 'katex';
import 'katex/dist/katex.min.css';

export const FPS = 30;
const C: Record<string, string> = {bg:'#05060B',tx:'#F2F5FF',mu:'#8E9AC0',acc:'#E8632A',azul:'#6EA8FF',nar:'#FFA65C',ver:'#7CFF9B',amar:'#FFD84D',rojo:'#FF6B6B'};
const serif = "'Literata', Georgia, serif", sans = "'Space Grotesk', system-ui, sans-serif", mono = "'IBM Plex Mono', ui-monospace, monospace";
const eo = Easing.out(Easing.cubic);
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const pr = (t: number, a: number, b: number, e = eo) => interpolate(t, [a, b], [0, 1], {...clamp, easing: e});

export type Guion = any;
export const duracion = (g: Guion) => Math.ceil(g.fin * FPS);

const Tex: React.FC<{tex: string; size: number; color?: string}> = ({tex, size, color}) => (
  <span style={{fontSize: size, color: color || C.tx, whiteSpace: 'nowrap'}} dangerouslySetInnerHTML={{__html: katex.renderToString(tex, {throwOnError: false})}} />
);
const Pop: React.FC<{t: number; a: number; children: React.ReactNode; from?: number; style?: React.CSSProperties}> = ({t, a, children, from = 0.5, style}) => {
  const {fps} = useVideoConfig();
  const s = spring({frame: Math.max(0, (t - a) * fps), fps, config: {damping: 11, mass: 0.7}});
  return <div style={{opacity: pr(t, a, a + 0.15), transform: `scale(${from + (1 - from) * s})`, transformOrigin: 'center', color: C.tx, ...style}}>{children}</div>;
};
/* texto con *acento* */
const Rico: React.FC<{txt: string; col: string}> = ({txt, col}) => <>{txt.split('*').map((p, i) => i % 2 ? <span key={i} style={{color: C[col] || col}}>{p}</span> : <React.Fragment key={i}>{p}</React.Fragment>)}</>;

const SIMB = ['x', '²', '÷', 'π', '∫', '√', '+', 'f', '=', '∑', 'y', 'dx', '≠', '∞'];
const Fondo: React.FC<{t: number}> = ({t}) => (
  <AbsoluteFill>
    <div style={{position: 'absolute', inset: 0, background: `radial-gradient(ellipse at ${50 + 12 * Math.sin(t * 0.35)}% ${28 + 6 * Math.cos(t * 0.3)}%, #131B36 0%, ${C.bg} 68%)`}} />
    <div style={{position: 'absolute', inset: 0, opacity: 0.10, backgroundImage: 'linear-gradient(#6EA8FF 1px, transparent 1px), linear-gradient(90deg, #6EA8FF 1px, transparent 1px)', backgroundSize: '90px 90px', backgroundPosition: `${(t * 14) % 90}px ${(t * 9) % 90}px`, WebkitMaskImage: 'radial-gradient(ellipse at 50% 40%, #000 20%, transparent 75%)'}} />
    {SIMB.map((s, i) => { const x = (i * 197) % 1000 + 30, sp = 22 + (i % 5) * 7, y = ((i * 311 + 1900 - t * sp) % 2000 + 2000) % 2000 - 40; return <div key={i} style={{position: 'absolute', left: x, top: y, fontFamily: serif, fontStyle: 'italic', fontSize: 70 + (i % 4) * 26, color: i % 3 ? C.azul : C.acc, opacity: 0.07}}>{s}</div>; })}
  </AbsoluteFill>
);
const Chispas: React.FC<{t: number; a: number; x: number; y: number; col: string; n?: number}> = ({t, a, x, y, col, n = 18}) => {
  const k = t - a; if (k < 0 || k > 1.1) return null;
  return <>{Array.from({length: n}).map((_, i) => { const ang = i * 2.399, v = 190 + (i % 4) * 70, d = v * (1 - Math.pow(1 - Math.min(1, k / 0.9), 3)); return <div key={i} style={{position: 'absolute', left: x + Math.cos(ang) * d, top: y + Math.sin(ang) * d, width: 14 - (i % 3) * 3, height: 14 - (i % 3) * 3, borderRadius: 20, background: col, opacity: 1 - k / 1.1}} />; })}</>;
};
const Karaoke: React.FC<{t: number; w: number; sent: any[]}> = ({t, w, sent}) => {
  const words = useMemo(() => { const o: {w: string; a: number; b: number}[] = []; sent.forEach(s => { const ws = s.t.split(/\s+/), tot = ws.reduce((m: number, x: string) => m + x.length + 1, 0); let c = s.a; ws.forEach((x: string) => { const d = (s.b - s.a) * (x.length + 1) / tot; o.push({w: x, a: c, b: c + d}); c += d; }); }); return o; }, [sent]);
  let idx = words.findIndex(x => t >= x.a && t < x.b); if (idx < 0) { const nx = words.findIndex(x => x.a > t); idx = nx <= 0 ? -1 : nx - 1; }
  if (idx < 0 || t > words[words.length - 1].b + 0.4) return null;
  const g = Math.floor(idx / 4), grp = words.slice(g * 4, g * 4 + 4);
  return (
    <div style={{width: w, textAlign: 'center', fontFamily: sans, fontWeight: 700, fontSize: 66, lineHeight: 1.2, textShadow: '0 4px 18px rgba(0,0,0,.95)'}}>
      {grp.map((x, i) => { const cur = g * 4 + i === idx, past = g * 4 + i < idx; return <span key={i} style={{color: cur ? C.ver : past ? C.tx : 'rgba(242,245,255,.5)', marginRight: 18, display: 'inline-block', transform: cur ? 'scale(1.1)' : 'none'}}>{x.w}</span>; })}
    </div>
  );
};

const evaluar = (expr: string, vars: string[]) => { try { return new Function(...vars, 'const {sqrt,abs,sin,cos,tan,exp,log,pow,PI}=Math; return ' + expr + ';') as (...a: number[]) => number; } catch (e) { return () => NaN; } };

/* ---------------- escenas ---------------- */
type P = {e: any; t: number; A: (i: number) => number; W: number; sent: any[]};
const at = (A: (i: number) => number, s: number, dt = 0) => A(s) + (dt || 0);

const Gancho: React.FC<P> = ({e, t, A, W}) => {
  const a0 = at(A, e.s[0]); const shake = e.mal ? Math.sin(t * 38) * 6 * (1 - pr(t, a0 + 1.2, a0 + 1.9)) : 0;
  return (
    <div style={{position: 'absolute', left: 70, top: 330, width: W, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 60}}>
      <Pop t={t} a={a0} from={0.8} style={{fontFamily: serif, fontWeight: 900, fontSize: 96, lineHeight: 1.06, textAlign: 'center'}}><Rico txt={e.titulo} col={e.mal ? 'rojo' : 'amar'} /></Pop>
      <div style={{position: 'relative', transform: `translateX(${shake}px)`}}>
        <Pop t={t} a={a0 + 0.5}><Tex tex={e.tex} size={e.size || 90} /></Pop>
        {e.mal && <Pop t={t} a={a0 + 1.2} from={2.2} style={{position: 'absolute', right: 10, top: 190, fontFamily: sans, fontWeight: 900, fontSize: 150, color: C.rojo, textShadow: '0 0 40px rgba(255,107,107,.6)'}}>✗</Pop>}
      </div>
    </div>
  );
};
const Tarjetas: React.FC<P> = ({e, t, A, W}) => (
  <div style={{position: 'absolute', left: 70, top: e.top || 280, width: W, display: 'flex', flexDirection: 'column', gap: 46}}>
    {e.titulo && <Pop t={t} a={at(A, e.s[0], 0.1)} style={{fontFamily: serif, fontWeight: 900, fontSize: 80, lineHeight: 1.08, textAlign: 'center'}}><Rico txt={e.titulo} col="ver" /></Pop>}
    {e.cards.map((c: any, i: number) => { const col = C[c.tipo === 'ok' ? 'ver' : c.tipo === 'mal' ? 'rojo' : 'amar']; const a = at(A, c.s, c.dt); return (
      <Pop key={i} t={t} a={a} from={0.8} style={{border: `6px solid ${col}`, borderRadius: 32, padding: '30px 30px', background: 'rgba(255,255,255,.04)', boxShadow: c.tipo === 'ok' ? `0 0 ${46 * (0.5 + 0.5 * Math.sin(t * 5))}px ${col}33` : 'none'}}>
        <div style={{fontFamily: sans, fontWeight: 700, fontSize: 40, color: col, marginBottom: 10}}>{c.tipo === 'ok' ? '✓ ' : c.tipo === 'mal' ? '✗ ' : ''}{c.label}</div>
        <div style={{textAlign: 'center'}}><Tex tex={c.tex} size={c.size || 78} /></div>
      </Pop>); })}
  </div>
);
const Pasos: React.FC<P> = ({e, t, A, W}) => (
  <div style={{position: 'absolute', left: 70, top: e.top || 250, width: W, display: 'flex', flexDirection: 'column', gap: 40}}>
    {e.titulo && <Pop t={t} a={at(A, e.s[0], 0.1)} style={{fontFamily: sans, fontWeight: 700, color: C.amar, fontSize: 40, letterSpacing: 2, textTransform: 'uppercase'}}>{e.titulo}</Pop>}
    {e.pasos.map((p: any, i: number) => { const a = at(A, p.s, p.dt), alt = p.alt ? pr(t, at(A, p.alt.s, p.alt.dt), at(A, p.alt.s, p.alt.dt) + 0.5) : 0; const col = C[p.col || 'azul']; return (
      <div key={i} style={{opacity: pr(t, a, a + 0.3), transform: `translateY(${(1 - pr(t, a, a + 0.45)) * 30}px)`}}>
        <div style={{fontFamily: sans, fontWeight: 700, fontSize: 34, letterSpacing: 2, textTransform: 'uppercase', color: col, marginBottom: 6}}>{p.label}</div>
        <div style={{position: 'relative', display: 'flex', justifyContent: p.centro ? 'center' : 'flex-start'}}>
          <div style={{opacity: 1 - alt}}><Tex tex={p.tex} size={p.size || 64} /></div>
          {p.alt && <div style={{position: 'absolute', inset: 0, opacity: alt, display: 'flex', justifyContent: p.centro ? 'center' : 'flex-start'}}><Tex tex={p.alt.tex} size={p.size || 64} /></div>}
        </div>
      </div>); })}
    {e.caja && <Pop t={t} a={at(A, e.caja.s, e.caja.dt)} from={0.2} style={{alignSelf: 'center', border: `7px solid ${C.amar}`, borderRadius: 32, padding: '20px 56px', boxShadow: '0 0 70px rgba(255,216,77,.28)'}}><Tex tex={e.caja.tex} size={e.caja.size || 88} color={C.amar} /></Pop>}
    {e.caja && <Chispas t={t} a={at(A, e.caja.s, (e.caja.dt || 0) + 0.15)} x={540} y={e.caja.chispasY || 1180} col={C.amar} n={22} />}
  </div>
);
const Lista: React.FC<P> = ({e, t, A, W}) => (
  <div style={{position: 'absolute', left: 70, top: e.top || 360, width: W, display: 'flex', flexDirection: 'column', gap: 44}}>
    <Pop t={t} a={at(A, e.s[0], 0.1)} style={{fontFamily: serif, fontWeight: 900, fontSize: 88, lineHeight: 1.08, textAlign: 'center'}}><Rico txt={e.titulo} col="amar" /></Pop>
    {e.items.map((it: any, i: number) => (
      <Pop key={i} t={t} a={at(A, it.s, it.dt)} from={0.7} style={{display: 'flex', alignItems: 'center', gap: 28, border: `5px solid ${C.amar}`, borderRadius: 28, padding: '22px 34px', background: 'rgba(255,216,77,.06)'}}>
        <span style={{fontFamily: mono, fontWeight: 700, fontSize: 66, color: C.amar}}>{it.big}</span><span style={{fontFamily: sans, fontSize: 40, color: C.mu}}>{it.small}</span>
      </Pop>))}
  </div>
);
const Cierre: React.FC<P> = ({e, t, A, W}) => (
  <div style={{position: 'absolute', left: 70, top: e.top || 440, width: W, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 50}}>
    <Pop t={t} a={at(A, e.s[0])} style={{fontFamily: serif, fontWeight: 900, fontSize: 92, lineHeight: 1.08, textAlign: 'center'}}><Rico txt={e.titulo} col="acc" /></Pop>
    <Pop t={t} a={at(A, e.s[0], 0.6)} from={0.6} style={{background: C.acc, color: '#05060B', fontFamily: sans, fontWeight: 700, fontSize: 64, padding: '26px 76px', borderRadius: 100, boxShadow: `0 0 ${70 * (0.5 + 0.5 * Math.sin(t * 6))}px rgba(232,99,42,.45)`}}>mathunal.com</Pop>
  </div>
);

const Grafica: React.FC<P> = ({e, t, A, W}) => {
  const H = e.alto || 1000, pad = 60, [xmin, xmax] = e.xr, [ymin, ymax] = e.yr;
  const X = (x: number) => pad + (x - xmin) / (xmax - xmin) * (W - 2 * pad), Y = (y: number) => H - pad - (y - ymin) / (ymax - ymin) * (H - 2 * pad);
  const kf: number[][] = (e.param?.kf || []).map((k: any) => [at(A, k[0], k[1]), k[2]]);
  let p = 0;
  if (kf.length) { p = kf[0][1]; for (let i = 1; i < kf.length; i++) if (t >= kf[i - 1][0]) p = interpolate(t, [kf[i - 1][0], kf[i][0]], [kf[i - 1][1], kf[i][1]], {...clamp, easing: Easing.inOut(Easing.quad)}); }
  const a0 = at(A, e.s[0], 0.2), dr = pr(t, a0, a0 + 1.4, Easing.inOut(Easing.quad));
  const fs = useMemo(() => (e.curvas || []).map((c: any) => evaluar(c.f, ['x', 'p'])), [e]);
  const paths = (e.curvas || []).map((c: any, ci: number) => {
    const f = fs[ci], N = 240, segs: string[] = []; let pen = false, cur = '';
    for (let k = 0; k <= N; k++) { const x = xmin + (xmax - xmin) * k / N, ex = (c.excluir || []).some((r: number[]) => x > r[0] && x < r[1]), y = f(x, p);
      if (!isFinite(y) || ex || y > ymax + 1 || y < ymin - 1) { if (cur) segs.push(cur); cur = ''; pen = false; continue; }
      cur += `${pen ? 'L' : 'M'}${X(x).toFixed(1)} ${Y(y).toFixed(1)}`; pen = true; }
    if (cur) segs.push(cur); return segs; });
  const dots = (e.puntos || []).map((d: any) => { const fx = evaluar(d.x, ['p', 'x']), fy = evaluar(d.y, ['p', 'x']); const x = fx(p, 0), y = fy(p, x); return {d, x, y}; });
  return (
    <div style={{position: 'absolute', left: 70, top: e.top || 250, width: W}}>
      {e.titulo && <Pop t={t} a={at(A, e.s[0], 0.05)} style={{fontFamily: sans, fontWeight: 700, color: C.amar, fontSize: 44, letterSpacing: 2, textTransform: 'uppercase', marginBottom: 10}}>{e.titulo}</Pop>}
      <svg width={W} height={H} viewBox={`0 0 ${W} ${H}`}>
        <path d={`M${X(0)} ${pad * 0.3} V${H - pad * 0.5} M${pad * 0.5} ${Y(0)} H${W - pad * 0.3}`} stroke={C.mu} strokeWidth={3} fill="none" opacity={0.6} />
        {(e.vlineas || []).map((v: any, i: number) => <g key={i} opacity={dr}><path d={`M${X(v.x)} ${pad * 0.3} V${H - pad * 0.5}`} stroke={C[v.col || 'rojo']} strokeWidth={3} strokeDasharray="14 12" fill="none" opacity={0.7} /><text x={X(v.x) - 14} y={pad * 0.8} fill={C[v.col || 'rojo']} fontFamily={mono} fontSize={32} textAnchor="end">{v.txt}</text></g>)}
        {paths.map((segs: string[], ci: number) => segs.map((d, i) => <path key={ci + '-' + i} d={d} pathLength={1} strokeDasharray="1" strokeDashoffset={1 - Math.min(1, Math.max(0, dr * (e.curvas[ci].retraso ? 1.4 : 3) - (e.curvas[ci].retraso || 0) - i * 0.15))} stroke={C[e.curvas[ci].col || 'azul']} strokeWidth={9} fill="none" strokeLinecap="round" />))}
        {dots.map(({d, x, y}: any, i: number) => { const on = pr(t, at(A, d.s, d.dt), at(A, d.s, d.dt) + 0.3); if (!isFinite(y) || on <= 0 || (d.oculto && evaluar(d.oculto, ['p', 'x'])(p, x))) return null; return <g key={i} opacity={on}>{d.guia && <line x1={X(x)} y1={Y(0)} x2={X(x)} y2={Y(y)} stroke={C[d.col || 'ver']} strokeWidth={4} strokeDasharray="8 8" />}<circle cx={X(x)} cy={Y(y)} r={19} fill={C[d.col || 'ver']} /></g>; })}
        {(e.marcas || []).map((m: any, i: number) => { const a = at(A, m.s, m.dt), on = pr(t, a, a + 0.4), pulse = 1 + 0.2 * Math.sin((t - a) * 7) * on, mx = evaluar(m.x, ['p'])(p), my = evaluar(m.y, ['p'])(p); if (!isFinite(mx) || !isFinite(my)) return null; return (
          <g key={i} opacity={on}><circle cx={X(mx)} cy={Y(my)} r={22 * pulse} fill={m.hueco ? C.bg : C[m.col || 'amar']} stroke={C[m.col || 'amar']} strokeWidth={7} />
            <text x={X(mx) + 36} y={Y(my) + (m.dy ?? -60)} fill={C[m.col || 'amar']} fontFamily={mono} fontSize={40} fontWeight={600}>{m.txt}</text>
            {m.txt2 && <text x={X(mx) + 36} y={Y(my) + (m.dy ?? -60) + 54} fill={C.mu} fontFamily={mono} fontSize={32}>{m.txt2}</text>}</g>); })}
        {(e.textos || []).map((tx: any, i: number) => { const a = at(A, tx.s, tx.dt); const v = evaluar('`' + tx.txt + '`', ['p'])(p); return <text key={i} x={tx.x} y={tx.y} fill={C[tx.col || 'tx']} fontFamily={mono} fontSize={tx.size || 46} fontWeight={700} opacity={pr(t, a, a + 0.3)}>{String(v)}</text>; })}
      </svg>
    </div>
  );
};

const TIPOS: Record<string, React.FC<P>> = {gancho: Gancho, tarjetas: Tarjetas, pasos: Pasos, lista: Lista, cierre: Cierre, grafica: Grafica};

export const Reel: React.FC<{g: Guion}> = ({g}) => {
  const frame = useCurrentFrame(); const {width} = useVideoConfig(); const t = frame / FPS;
  const sent = g.sent, W = width - 140, A = (i: number) => sent[i].a;
  const scene = sent.findIndex((s: any, i: number) => t >= s.a && (i === sent.length - 1 || t < sent[i + 1].a));
  return (
    <AbsoluteFill style={{fontFamily: sans}}>
      <Fondo t={t} />
      {g.audio && <Audio src={staticFile(g.audio)} />}
      <div style={{position: 'absolute', left: 70, top: 80, display: 'flex', alignItems: 'center', gap: 16, fontFamily: serif, fontWeight: 900, fontSize: 46, color: C.tx}}>
        <svg width={44} height={44} viewBox="0 0 24 24" fill="none" stroke={C.acc} strokeWidth={2.4} strokeLinecap="round"><path d="M16 3.5c-2.6 0-3.4 1.6-3.4 4.2v8.6c0 2.6-.8 4.2-3.4 4.2" /></svg>
        <span>MATH<span style={{color: C.acc}}>UNAL</span></span>
      </div>
      <div style={{position: 'absolute', right: 70, top: 92, display: 'flex', gap: 10}}>{sent.map((_: any, i: number) => <div key={i} style={{width: i === scene ? 34 : 12, height: 12, borderRadius: 8, background: i <= scene ? C.acc : 'rgba(255,255,255,.18)'}} />)}</div>
      {g.escenas.map((e: any, i: number) => {
        const a = sent[e.s[0]].a - 0.1, b = sent[e.s[e.s.length - 1]].b + 0.2, vis = Math.min(pr(t, a, a + 0.35), 1 - pr(t, b - 0.3, b + 0.2)), Comp = TIPOS[e.tipo];
        return vis > 0.001 ? <div key={i} style={{position: 'absolute', inset: 0, transform: ['grafica', 'cierre'].includes(e.tipo) ? 'none' : 'translateY(90px)', opacity: e.tipo === 'cierre' ? pr(t, a, a + 0.4) : vis}}><Comp e={e} t={t} A={A} W={W} sent={sent} /></div> : null;
      })}
      <div style={{position: 'absolute', left: 70, top: 1490, width: W}}><Karaoke t={t} w={W} sent={sent} /></div>
      <div style={{position: 'absolute', left: 0, bottom: 0, height: 8, width: width * Math.min(1, t / g.fin), background: C.acc}} />
    </AbsoluteFill>
  );
};
