/* ═══════════════════════════════════════════════════════════════════════════
   MathUNAL · Simulacros Pro — Laboratorio ("Compruébalo tú mismo")
   ---------------------------------------------------------------------------
   Widgets SVG interactivos, sin dependencias. Cada uno: un slider que mueve
   algo y un readout que muestra cómo cambia la cantidad que pregunta el
   ejercicio. Se montan desde __simExplHook cuando la pregunta trae `compruebalo`.
   window.__simLab.mount(hostEl, id)  ·  ids: escalera cono globo caja tangente limite
   Rama simulacros-pro. Sin desplegar.
   ═══════════════════════════════════════════════════════════════════════════ */
(function(){
"use strict";

function el(tag, attrs, kids){
  var n=document.createElementNS(tag==='svg'||SVG_TAGS[tag]?'http://www.w3.org/2000/svg':'http://www.w3.org/1999/xhtml', tag);
  if(attrs) Object.keys(attrs).forEach(function(k){ n.setAttribute(k, attrs[k]); });
  (kids||[]).forEach(function(c){ n.appendChild(typeof c==='string'?document.createTextNode(c):c); });
  return n;
}
var SVG_TAGS={svg:1,g:1,path:1,line:1,circle:1,ellipse:1,rect:1,polyline:1,polygon:1,text:1,'text':1};

/* shell común: título, SVG, slider, readout, nota */
function shell(host, opts){
  host.innerHTML='';
  var wrap=document.createElement('div'); wrap.className='sl-wrap';
  var svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
  svg.setAttribute('viewBox','0 0 320 200'); svg.setAttribute('class','sl-svg');
  var rng=document.createElement('input');
  rng.type='range'; rng.className='sl-range';
  rng.min=opts.min; rng.max=opts.max; rng.step=opts.step; rng.value=opts.def;
  var out=document.createElement('div'); out.className='sl-out';
  var note=document.createElement('div'); note.className='sl-note'; note.innerHTML=opts.note||'';
  var lbl=document.createElement('div'); lbl.className='sl-lbl'; lbl.textContent=opts.label||'';
  wrap.appendChild(svg); wrap.appendChild(lbl); wrap.appendChild(rng); wrap.appendChild(out); wrap.appendChild(note);
  host.appendChild(wrap);
  function upd(){ opts.draw(svg, parseFloat(rng.value), out); }
  rng.addEventListener('input', upd);
  upd();
  return {svg:svg, rng:rng, out:out};
}
function fmt(x,d){ return (Math.round(x*Math.pow(10,d||2))/Math.pow(10,d||2)).toString(); }
function ns(t,a){ var n=document.createElementNS('http://www.w3.org/2000/svg',t); if(a) Object.keys(a).forEach(function(k){n.setAttribute(k,a[k]);}); return n; }

var W={
 /* ── ESCALERA que resbala (razón de cambio) ─────────────────────────────── */
 escalera:function(host){
  var L=5;
  shell(host,{min:0.6,max:L-0.15,step:0.05,def:3,
   label:'Distancia de la base a la pared  ·  dx/dt = 1 m/s',
   note:'Mueve la base. Lejos de la pared (escalera casi acostada) la punta baja lentísimo; cerca de la pared baja rapidísimo. Eso es <b>dy/dt = −(x/y)·(dx/dt)</b>: cuando y es chico, la razón se dispara.',
   draw:function(svg,x,out){
     var y=Math.sqrt(L*L-x*x), s=30, ox=45, oy=175;
     var bx=ox+x*s, ty=oy-y*s, dydt=-x/y;
     svg.innerHTML='';
     svg.appendChild(ns('line',{x1:ox,y1:20,x2:ox,y2:oy,stroke:'var(--t3)','stroke-width':3}));
     svg.appendChild(ns('line',{x1:ox,y1:oy,x2:ox+170,y2:oy,stroke:'var(--t3)','stroke-width':3}));
     svg.appendChild(ns('path',{d:'M'+ox+' '+ty+' L'+ox+' '+oy+' L'+bx+' '+oy,fill:'var(--adim)',stroke:'none'}));
     svg.appendChild(ns('line',{x1:ox,y1:ty,x2:bx,y2:oy,stroke:'var(--acc)','stroke-width':5,'stroke-linecap':'round'}));
     svg.appendChild(ns('circle',{cx:ox,cy:ty,r:4.5,fill:'var(--acc2)'}));
     svg.appendChild(ns('circle',{cx:bx,cy:oy,r:4.5,fill:'var(--acc2)'}));
     var tY=ns('text',{x:ox-8,y:ty+4,fill:'var(--t2)','font-size':11,'text-anchor':'end'}); tY.textContent='y='+fmt(y);
     var tX=ns('text',{x:(ox+bx)/2,y:oy+16,fill:'var(--t2)','font-size':11,'text-anchor':'middle'}); tX.textContent='x='+fmt(x);
     svg.appendChild(tY); svg.appendChild(tX);
     // flecha de descenso proporcional a |dydt|
     var arr=Math.min(40,Math.abs(dydt)*22);
     svg.appendChild(ns('line',{x1:ox+13,y1:ty,x2:ox+13,y2:ty+arr,stroke:'var(--bad)','stroke-width':2.5,'marker-end':''}));
     svg.appendChild(ns('polygon',{points:(ox+9)+','+(ty+arr-5)+' '+(ox+17)+','+(ty+arr-5)+' '+(ox+13)+','+(ty+arr+3),fill:'var(--bad)'}));
     out.innerHTML='x = '+fmt(x)+' m  ·  y = '+fmt(y)+' m  ·  <b>dy/dt = '+fmt(dydt)+' m/s</b> (la punta baja)';
   }});
 },

 /* ── CONO que se llena (razón de cambio + semejanza) ────────────────────── */
 cono:function(host){
  var R=3,H=6,dVdt=2;
  shell(host,{min:0.4,max:H,step:0.05,def:3,
   label:'Nivel del agua h  ·  entra a 2 m³/min',
   note:'El radio de la superficie crece con el nivel (<b>r = h/2</b>), así que la superficie se ensancha y el mismo caudal sube el nivel cada vez más lento: <b>dh/dt = 8/(πh²)</b>.',
   draw:function(svg,h,out){
     var r=h/2, dhdt=8/(Math.PI*h*h);
     var cx=160, top=25, bot=185, ch=bot-top, s=ch/H;
     var halfTop=(R/H)*ch;
     // cono (triángulo invertido)
     svg.innerHTML='';
     svg.appendChild(ns('path',{d:'M'+(cx-halfTop)+' '+top+' L'+cx+' '+bot+' L'+(cx+halfTop)+' '+top,fill:'none',stroke:'var(--t3)','stroke-width':2.5,'stroke-linejoin':'round'}));
     svg.appendChild(ns('line',{x1:cx-halfTop,y1:top,x2:cx+halfTop,y2:top,stroke:'var(--t3)','stroke-width':2.5}));
     // agua
     var wy=bot-h*s, wHalf=(r/H)*ch;
     svg.appendChild(ns('path',{d:'M'+(cx-wHalf)+' '+wy+' L'+cx+' '+bot+' L'+(cx+wHalf)+' '+wy+' Z',fill:'var(--adim)',stroke:'var(--acc)','stroke-width':1.5}));
     svg.appendChild(ns('ellipse',{cx:cx,cy:wy,rx:wHalf,ry:5,fill:'var(--acc)','fill-opacity':0.35,stroke:'var(--acc)','stroke-width':1.5}));
     var tH=ns('text',{x:cx+halfTop+8,y:wy+4,fill:'var(--t2)','font-size':11}); tH.textContent='h='+fmt(h);
     svg.appendChild(tH);
     out.innerHTML='h = '+fmt(h)+' m  ·  r = '+fmt(r)+' m  ·  <b>dh/dt = '+fmt(dhdt)+' m/min</b>';
   }});
 },

 /* ── GLOBO que se infla (razón de cambio, esfera) ───────────────────────── */
 globo:function(host){
  var dVdt=100;
  shell(host,{min:1,max:8,step:0.1,def:5,
   label:'Radio r (cm)  ·  entra aire a 100 cm³/s',
   note:'Metes aire al mismo ritmo, pero el globo ya es más grande: la superficie 4πr² crece con r², así que <b>dr/dt = 100/(4πr²)</b> se hace cada vez más chico.',
   draw:function(svg,r,out){
     var drdt=dVdt/(4*Math.PI*r*r);
     var cx=160, cy=105, pr=r*10;
     svg.innerHTML='';
     svg.appendChild(ns('circle',{cx:cx,cy:cy,r:pr,fill:'var(--adim)',stroke:'var(--acc)','stroke-width':2}));
     svg.appendChild(ns('line',{x1:cx,y1:cy,x2:cx+pr,y2:cy,stroke:'var(--acc2)','stroke-width':2,'stroke-dasharray':'3 3'}));
     var tR=ns('text',{x:cx+pr/2,y:cy-5,fill:'var(--t2)','font-size':11,'text-anchor':'middle'}); tR.textContent='r='+fmt(r);
     svg.appendChild(tR);
     // nudo
     svg.appendChild(ns('path',{d:'M'+(cx-4)+' '+(cy+pr)+' l4 8 l4 -8 Z',fill:'var(--acc)'}));
     out.innerHTML='r = '+fmt(r)+' cm  ·  superficie = '+fmt(4*Math.PI*r*r,0)+' cm²  ·  <b>dr/dt = '+fmt(drdt,3)+' cm/s</b>';
   }});
 },

 /* ── CAJA de material mínimo (optimización) ─────────────────────────────── */
 caja:function(host){
  var V=32;
  shell(host,{min:1.4,max:7,step:0.05,def:2.5,
   label:'Lado de la base x  ·  volumen fijo V = 32',
   note:'La curva es el material total S(x) = x² + 128/x. Muévete: baja hasta un <b>valle en x = ∛64 = 4</b> y vuelve a subir. Ese valle es donde S′(x) = 0 — el mínimo.',
   draw:function(svg,x,out){
     var h=V/(x*x), S=x*x+128/x;
     // curva S(x) en un mini-plot
     var px0=30,px1=200,py0=185,py1=30, xa=1.4,xb=7;
     function Sf(t){ return t*t+128/t; }
     var sMin=Sf(4), sMax=Math.max(Sf(xa),Sf(xb));
     function X(t){ return px0+(t-xa)/(xb-xa)*(px1-px0); }
     function Y(v){ return py0-(v-sMin)/(sMax-sMin)*(py0-py1); }
     var d='M';
     for(var t=xa;t<=xb+1e-9;t+=0.1){ d+=(t>xa?' L':'')+fmt(X(t),1)+' '+fmt(Y(Sf(t)),1); }
     svg.innerHTML='';
     svg.appendChild(ns('line',{x1:px0,y1:py0,x2:px1,y2:py0,stroke:'var(--t3)','stroke-width':1.5}));
     svg.appendChild(ns('line',{x1:px0,y1:py0,x2:px0,y2:py1,stroke:'var(--t3)','stroke-width':1.5}));
     svg.appendChild(ns('path',{d:d,fill:'none',stroke:'var(--acc)','stroke-width':2}));
     // marca del mínimo
     svg.appendChild(ns('line',{x1:X(4),y1:py0,x2:X(4),y2:py1,stroke:'var(--t3)','stroke-width':1,'stroke-dasharray':'2 3'}));
     // punto actual
     svg.appendChild(ns('circle',{cx:X(x),cy:Y(S),r:4.5,fill:'var(--acc2)'}));
     // caja chiquita a la derecha
     var bx=230,by=95, w=Math.min(60,x*10), hh=Math.min(70,h*14);
     svg.appendChild(ns('path',{d:'M'+bx+' '+by+' l'+w+' 0 l0 '+hh+' l-'+w+' 0 Z M'+bx+' '+by+' l14 -10 l'+w+' 0 l-14 10 M'+(bx+w)+' '+by+' l14 -10 l0 '+hh+' l-14 10',fill:'var(--adim)',stroke:'var(--acc)','stroke-width':1.3,'stroke-linejoin':'round'}));
     var tX=ns('text',{x:X(x),y:py0+14,fill:'var(--t2)','font-size':10,'text-anchor':'middle'}); tX.textContent='x='+fmt(x,1);
     svg.appendChild(tX);
     out.innerHTML='x = '+fmt(x,2)+'  ·  altura h = '+fmt(h,2)+'  ·  <b>material S = '+fmt(S,1)+'</b>'+(Math.abs(x-4)<0.06?'  ← ¡mínimo!':'');
   }});
 },

 /* ── TANGENTE: la derivada es la pendiente ──────────────────────────────── */
 tangente:function(host){
  shell(host,{min:-2.4,max:2.4,step:0.05,def:1,
   label:'Punto  x = a  sobre  f(x) = x³ − 3x',
   note:'La <b>pendiente</b> de la recta que toca la curva en un punto <b>ES f′(a)</b>. Donde la curva está plana (máximo/mínimo), la recta queda horizontal y f′(a) = 0.',
   draw:function(svg,a,out){
     var px0=20,px1=300,py=105, sx=45, sy=13;
     function f(t){ return t*t*t-3*t; }
     function fp(t){ return 3*t*t-3; }
     function X(t){ return 160+t*sx; }
     function Y(v){ return py-v*sy; }
     var d='M';
     for(var t=-2.6;t<=2.6+1e-9;t+=0.08){ d+=(t>-2.6?' L':'')+fmt(X(t),1)+' '+fmt(Y(f(t)),1); }
     svg.innerHTML='';
     svg.appendChild(ns('line',{x1:px0,y1:py,x2:px1,y2:py,stroke:'var(--t3)','stroke-width':1}));
     svg.appendChild(ns('line',{x1:160,y1:15,x2:160,y2:195,stroke:'var(--t3)','stroke-width':1}));
     svg.appendChild(ns('path',{d:d,fill:'none',stroke:'var(--t2)','stroke-width':2}));
     // tangente
     var m=fp(a), b=f(a);
     var x1=a-1.6, x2=a+1.6;
     svg.appendChild(ns('line',{x1:X(x1),y1:Y(b+m*(x1-a)),x2:X(x2),y2:Y(b+m*(x2-a)),stroke:'var(--acc)','stroke-width':2.5}));
     svg.appendChild(ns('circle',{cx:X(a),cy:Y(b),r:4.5,fill:'var(--acc2)'}));
     out.innerHTML='a = '+fmt(a,2)+'  ·  f(a) = '+fmt(b,2)+'  ·  <b>pendiente f′(a) = '+fmt(m,2)+'</b>'+(Math.abs(m)<0.12?'  ← recta horizontal':'');
   }});
 },

 /* ── LÍMITE: acercarse a un punto ───────────────────────────────────────── */
 limite:function(host){
  shell(host,{min:0.02,max:1.2,step:0.02,def:0.6,
   label:'Qué tan cerca de x = 2 estás mirando (|x − 2|)',
   note:'La función tiene un hueco en x = 2, pero al acercarte por los dos lados f(x) se apila alrededor de <b>4</b>. Ese número es el límite, exista o no f(2).',
   draw:function(svg,dx,out){
     // f(x) = (x^2-4)/(x-2) = x+2, hueco en x=2 -> limite 4
     var px0=20,px1=300, sy=18, oy=175, sx=55, cx=90;
     function X(t){ return cx+(t-1)*sx; }
     function Y(v){ return oy-v*sy; }
     svg.innerHTML='';
     svg.appendChild(ns('line',{x1:px0,y1:oy,x2:px1,y2:oy,stroke:'var(--t3)','stroke-width':1}));
     // recta y = x+2
     svg.appendChild(ns('line',{x1:X(1),y1:Y(3),x2:X(3.4),y2:Y(5.4),stroke:'var(--t2)','stroke-width':2}));
     // hueco
     svg.appendChild(ns('circle',{cx:X(2),cy:Y(4),r:4,fill:'var(--bg)',stroke:'var(--t2)','stroke-width':2}));
     // linea horizontal en y=4
     svg.appendChild(ns('line',{x1:px0,y1:Y(4),x2:px1,y2:Y(4),stroke:'var(--acc)','stroke-width':1,'stroke-dasharray':'3 3'}));
     var t4=ns('text',{x:px1-4,y:Y(4)-4,fill:'var(--acc)','font-size':10,'text-anchor':'end'}); t4.textContent='y → 4';
     svg.appendChild(t4);
     // puntos acercándose
     [-1,1].forEach(function(sgn){
       var xv=2+sgn*dx, yv=xv+2;
       svg.appendChild(ns('circle',{cx:X(xv),cy:Y(yv),r:4,fill:'var(--acc)'}));
     });
     svg.appendChild(ns('line',{x1:X(2),y1:oy,x2:X(2),y2:20,stroke:'var(--t3)','stroke-width':1,'stroke-dasharray':'2 3'}));
     var t2=ns('text',{x:X(2),y:oy+13,fill:'var(--t2)','font-size':10,'text-anchor':'middle'}); t2.textContent='x=2';
     svg.appendChild(t2);
     var xl=2-dx, xr=2+dx;
     out.innerHTML='f('+fmt(xl,2)+') = '+fmt(xl+2,2)+'  ·  f('+fmt(xr,2)+') = '+fmt(xr+2,2)+'  ·  <b>límite = 4</b>';
   }});
 }
};

window.__simLab = {
  has:function(id){ return !!W[id]; },
  mount:function(host, id){ if(W[id]) try{ W[id](host); }catch(e){ host.innerHTML='<div class="sl-note">(no se pudo cargar el widget)</div>'; } }
};
})();
