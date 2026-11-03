(function(){
  var NS='http://www.w3.org/2000/svg';
  var RM=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  var L=JSON.parse(document.getElementById('leccion-datos').textContent);
  var G=L.grafica, SEC=(G.tipo==='secante'), TVM=(G.tipo==='tvm'), A=(SEC||TVM)?G.a:G.hueco.x, ETQ=G.etiquetas||['Por la izquierda','Por la derecha'];

  /* ---------- utilidades ---------- */
  function cl(v,a,b){ return Math.max(a,Math.min(b,v)); }
  function ap(t,a,b){ return cl((t-a)/(b-a),0,1); }
  function eio(k){ return k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2; }
  function eo(k){ return 1-Math.pow(1-k,3); }
  function fmt(v){ return (Math.round(v*10000)/10000).toFixed(4).replace(/0+$/,'').replace(/\.$/,''); }
  function ic(id){ return '<svg class="ic" aria-hidden="true"><use href="#'+id+'"/></svg>'; }
  function attr(s){ return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;'); }
  function tween(dur,fn,done){ if(RM){ fn(1); if(done) done(); return; } var t0=null; (function s(now){ if(t0===null) t0=now; var k=cl((now-t0)/dur,0,1); fn(k); if(k<1) requestAnimationFrame(s); else if(done) done(); })(performance.now()); }
  function pasoNice(a,b){ var r=b-a, L=[1,2,5,10,20,50,100,200,500]; for(var i=0;i<L.length;i++) if(r/L[i]<=8) return L[i]; return 1000; }
  var FN=/\b(sin|cos|tan|exp|ln|sqrt|abs|pi)\b/g;
  function compile(expr){   /* fórmulas del JSON. Números, x, operadores, paréntesis y sin cos tan exp ln sqrt abs pi */
    if(!/^[0-9x+\-*\/().^\s]*$/.test(String(expr).replace(FN,''))) throw new Error('Fórmula no permitida '+expr);
    var js=String(expr).replace(/\^/g,'**').replace(/\bln\b/g,'log').replace(/\bpi\b/g,'PI').replace(FN,function(m){ return m; });
    js=js.replace(/\b(sin|cos|tan|exp|log|sqrt|abs|PI)\b/g,'Math.$1');
    return new Function('x','return '+js);
  }
  var fFun=compile(G.funcion), fCurve=(SEC||TVM)?fFun:compile(G.curva), fDer=(SEC||TVM)?compile(G.derivada):null;
  function gl(h){ return h.replace(/\{\{gl:([a-z0-9_]+)\|([^}]+)\}\}/g,'<button class="gl" type="button" data-g="$1">$2</button>'); }

  /* ---------- cabecera ---------- */
  document.title='Lección '+L.titulo;
  document.getElementById('crumb').innerHTML='<span>'+L.curso+'</span><span class="sep">/</span><span>'+L.modulo+'</span><span class="sep">/</span><span class="num">'+L.posicion+'</span>';
  document.getElementById('titulo').textContent=L.titulo;
  document.getElementById('lmeta').innerHTML='<span>'+ic('i-clock')+'<span class="num">'+L.minutos+'</span> min</span><span>'+ic('i-target')+'<span class="num">'+L.ejercicios+'</span> ejercicio</span><span>El mismo contenido en tres modos</span>';
  if(L.ejemplo) document.getElementById('chip-ej').hidden=false;
  document.getElementById('v-g').setAttribute('aria-label',G.alt||'Gráfica');
  document.getElementById('p-g').setAttribute('aria-label','Laboratorio de la gráfica');
  document.getElementById('l-left').textContent=L.minutos+' min de lectura';
  function etiquetas(){ [].forEach.call(document.querySelectorAll('.lab-l'),function(e){ e.textContent=ETQ[0]; }); [].forEach.call(document.querySelectorAll('.lab-r'),function(e){ e.textContent=ETQ[1]; }); }
  var sl=document.querySelector('.p-lab .ctl label'); if(G.etiquetaSlider&&sl) sl.firstChild.textContent=G.etiquetaSlider;
  document.getElementById('v-time').textContent='0 s de '+L.ver.duracion+' s';

  /* ---------- gráfica sin rejilla, configurada por el JSON. Con grafica.zoom={factor:N} acepta el estado zoom de 0 a 1 ---------- */
  var gid=0;
  function paso125(span,libre){   /* paso de marcas 1, 2 o 5 por una potencia de 10, con 8 marcas como máximo */
    var k=Math.floor(Math.log(span/8)/Math.LN10), c=[1,2,5,10], base=Math.pow(10,k);
    for(var i=0;i<c.length;i++){ if(span/(c[i]*base)<=8+1e-9){ var s=c[i]*base; return libre?s:Math.max(1,s); } }
    return libre?base*10:Math.max(1,base*10);
  }
  function Frame(svg,cx,cy){
    var F={x0:70,x1:620,y0:330,y1:30,XR:G.x.slice(),YR:G.y.slice(),z:-1,zf:(G.zoom&&G.zoom.factor)||0,onWin:null};
    F.X=function(x){ return F.x0+(x-F.XR[0])/(F.XR[1]-F.XR[0])*(F.x1-F.x0); };
    F.Y=function(y){ return F.y0-(y-F.YR[0])/(F.YR[1]-F.YR[0])*(F.y0-F.y1); };
    F.XA=function(){ return Math.max(F.x0,Math.min(F.x1,F.X(0))); };
    F.YA=function(){ return Math.max(F.y1,Math.min(F.y0,F.Y(0))); };
    F.el=function(t,a,par){ var e=document.createElementNS(NS,t); for(var k in a) e.setAttribute(k,a[k]); (par||svg).appendChild(e); return e; };
    var ag=F.el('g',{}), zl=null;
    function fm(v,dec){ var t=v.toFixed(dec); return t==='-0'||/^-0\.?0*$/.test(t)?t.replace('-',''):t; }
    F.axes=function(){
      while(ag.firstChild) ag.removeChild(ag.firstChild);
      var xa=F.XA(), ya=F.YA(), libre=F.z>0.001;
      F.el('path',{'class':'ax',d:'M'+xa+' '+(F.y1-8)+' V'+F.y0+' M'+F.x0+' '+ya+' H'+(F.x1+6)},ag);
      var sx=paso125(F.XR[1]-F.XR[0],libre), dx=Math.max(0,-Math.floor(Math.log(sx)/Math.LN10+1e-9));
      for(var i=Math.ceil(F.XR[0]/sx-1e-9);i*sx<=F.XR[1]+sx*1e-9;i++){ var v=i*sx; if(Math.abs(v)<sx*1e-6) continue; F.el('path',{'class':'tk',d:'M'+F.X(v)+' '+(ya-5)+' v10'},ag); var t=F.el('text',{'class':'tt',x:F.X(v),y:ya+26,'text-anchor':'middle'},ag); t.textContent=fm(v,dx); }
      var sy=paso125(F.YR[1]-F.YR[0],libre), dy=Math.max(0,-Math.floor(Math.log(sy)/Math.LN10+1e-9));
      for(var j=Math.ceil(F.YR[0]/sy-1e-9);j*sy<=F.YR[1]+sy*1e-9;j++){ var w=j*sy; if(Math.abs(w)<sy*1e-6) continue; F.el('path',{'class':'tk',d:'M'+(xa-5)+' '+F.Y(w)+' h10'},ag); var u=F.el('text',{'class':'tt',x:xa-14,y:F.Y(w)+4,'text-anchor':'end'},ag); u.textContent=fm(w,dy); }
    };
    F.zoomLabel=function(){ if(!F.zf) return; if(!zl){ var izq=SEC&&fDer(A)>0; zl=F.el('text',{'class':'zb',x:izq?F.x0+24:F.x1-4,y:F.y1+16,'text-anchor':izq?'start':'end',opacity:0}); } var f=(G.x[1]-G.x[0])/(F.XR[1]-F.XR[0]); zl.setAttribute('opacity',F.z>0.05?1:0); zl.textContent='Zoom ×'+(f>=10?Math.round(f):f.toFixed(1)); };
    F.setZ=function(z){
      if(!F.zf) return false; z=z||0; if(Math.abs(z-F.z)<1e-4) return false; F.z=z;
      if(z<=0){ F.XR=G.x.slice(); F.YR=G.y.slice(); }
      else{ var Wx=G.x[1]-G.x[0], Wy=G.y[1]-G.y[0], k=Math.pow(1/F.zf,z), wx=Wx*k, wy=Wy*k, rx=(cx-G.x[0])/Wx*(1-z)+0.5*z, ry=(cy-G.y[0])/Wy*(1-z)+0.5*z;
        F.XR=[cx-rx*wx,cx-rx*wx+wx]; F.YR=[cy-ry*wy,cy-ry*wy+wy]; }
      F.axes(); F.zoomLabel(); if(F.onWin) F.onWin(); return true;
    };
    F.curve=function(){ var d=[], on=false, N=160; for(var k=0;k<=N;k++){ var xx=F.XR[0]+(F.XR[1]-F.XR[0])*k/N, yv=fCurve(xx); if(!isFinite(yv)) yv=fCurve(xx+1e-9); if(!isFinite(yv)){ on=false; continue; } var py=Math.max(-5e4,Math.min(5e4,F.Y(yv))); d.push((on?'L':'M')+F.X(xx).toFixed(1)+' '+py.toFixed(1)); on=true; } return d.join(' '); };
    F.clip=function(){ var defs=F.el('defs',{}), cp=F.el('clipPath',{id:'cp'+(++gid)},defs); F.el('rect',{x:F.x0,y:F.y1-10,width:F.x1-F.x0+8,height:F.y0-F.y1+10},cp); return F.el('g',{'clip-path':'url(#cp'+gid+')'}); };
    F.line=function(e,m){ var xa=F.XR[0], xb=F.XR[1], ya=fFun(A)+m*(xa-A), yb=fFun(A)+m*(xb-A); e.setAttribute('x1',F.X(xa)); e.setAttribute('y1',F.Y(ya)); e.setAttribute('x2',F.X(xb)); e.setAttribute('y2',F.Y(yb)); };
    F.axes();
    return F;
  }
  function GraphSecante(svg){
    var F=Frame(svg,A,fFun(A)), X=F.X, Y=F.Y, el=F.el, grp=F.clip();
    var cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var nm=G.normal?el('line',{'class':'nm',opacity:0},grp):null; var tan=el('line',{'class':'tg',opacity:0},grp), sec=el('line',{'class':'sc',opacity:0},grp), run=el('path',{'class':'dl',d:'',stroke:'var(--warn)',opacity:0},grp);
    var halo=el('circle',{'class':'halo',r:12,opacity:0},grp), pP=el('circle',{'class':'pP',r:0},grp), pQ=el('circle',{'class':'pL',r:9,opacity:0},grp);
    F.onWin=function(){ cv.setAttribute('d',F.curve()); };
    return { set:function(s){
      F.setZ(s.zoom);
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole, ax=X(A), ay=Y(fFun(A)); pP.setAttribute('r',9*h); pP.setAttribute('cx',ax); pP.setAttribute('cy',ay); halo.setAttribute('cx',ax); halo.setAttribute('cy',ay); halo.setAttribute('opacity',s.ok?1:0);
      if(nm){ F.line(nm,-1/fDer(A)); nm.setAttribute('opacity',s.nor==null?0:s.nor); } var g=s.guide==null?0:s.guide; F.line(tan,fDer(A)); tan.setAttribute('opacity',g); tan.style.strokeWidth=s.ok?5:3.5;
      if(s.d==null){ sec.setAttribute('opacity',0); run.setAttribute('opacity',0); pQ.setAttribute('opacity',0); }
      else{ var q=A+s.d, m=(fFun(q)-fFun(A))/s.d, a=s.pa==null?1:s.pa; F.line(sec,m); sec.setAttribute('opacity',a*(g>0.5?0.35:1));
        run.setAttribute('d','M'+ax+' '+ay+' H'+X(q)+' V'+Y(fFun(q))); run.setAttribute('opacity',a*(g>0.5?0:1));
        pQ.setAttribute('cx',X(q)); pQ.setAttribute('cy',Y(fFun(q))); pQ.setAttribute('opacity',a); }
    }};
  }
  /* teorema del valor medio. La cuerda une (a, f(a)) con (b, f(b)) y una tangente recorre la curva. El estado d es el x del punto móvil */
  function GraphTVM(svg){
    var a=G.a, b=G.b, fa=fFun(a), fb=fFun(b), F=Frame(svg,(a+b)/2,(fa+fb)/2), X=F.X, Y=F.Y, el=F.el, grp=F.clip();
    var cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var chord=el('line',{'class':'sc',opacity:0,x1:X(a),y1:Y(fa),x2:X(b),y2:Y(fb)},grp), tan=el('line',{'class':'tg',opacity:0},grp);
    var pA=el('circle',{'class':'pP',cx:X(a),cy:Y(fa),r:0},grp), pB=el('circle',{'class':'pP',cx:X(b),cy:Y(fb),r:0},grp);
    var lA=el('text',{'class':'zb',x:X(a)-4,y:Y(fa)+30,'text-anchor':'middle',opacity:0},grp), lB=el('text',{'class':'zb',x:X(b)+4,y:Y(fb)+30,'text-anchor':'middle',opacity:0},grp);
    lA.textContent='a = '+fmt(a); lB.textContent='b = '+fmt(b);
    var halo=el('circle',{'class':'halo',r:12,opacity:0},grp), pM=el('circle',{'class':'pL',r:9,opacity:0},grp), lM=el('text',{'class':'zb','text-anchor':'middle',opacity:0},grp);
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole; pA.setAttribute('r',8*h); pB.setAttribute('r',8*h); lA.setAttribute('opacity',h>0.5?1:0); lB.setAttribute('opacity',h>0.5?1:0);
      chord.setAttribute('opacity',s.guide==null?0:s.guide);
      if(s.d==null){ tan.setAttribute('opacity',0); pM.setAttribute('opacity',0); lM.setAttribute('opacity',0); halo.setAttribute('opacity',0); return; }
      var x=s.d, y=fFun(x), m=fDer(x), al=s.pa==null?1:s.pa, xa=F.XR[0], xb=F.XR[1];
      tan.setAttribute('x1',X(xa)); tan.setAttribute('y1',Y(y+m*(xa-x))); tan.setAttribute('x2',X(xb)); tan.setAttribute('y2',Y(y+m*(xb-x)));
      tan.setAttribute('opacity',al); tan.style.strokeWidth=s.ok?5:3.5;
      pM.setAttribute('cx',X(x)); pM.setAttribute('cy',Y(y)); pM.setAttribute('opacity',al);
      halo.setAttribute('cx',X(x)); halo.setAttribute('cy',Y(y)); halo.setAttribute('opacity',s.ok?1:0);
      lM.setAttribute('x',X(x)); lM.setAttribute('y',Y(y)-18); lM.textContent='x = '+fmt(x); lM.setAttribute('opacity',al);
    }};
  }
  function Graph(svg){
    if(SEC) return GraphSecante(svg);
    if(TVM) return GraphTVM(svg);
    var F=Frame(svg,A,G.hueco.y), X=F.X, Y=F.Y, el=F.el, grp=F.clip();
    var guide=el('path',{'class':'gd',d:'',opacity:0},grp); var gl2=el('text',{'class':'gl',x:F.x1,'text-anchor':'end',opacity:0},grp); gl2.textContent='y = '+G.limite;
    var cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var halo=el('circle',{'class':'halo',r:12,opacity:0},grp);
    var hole=el('circle',{'class':'hole',r:0},grp);
    var zb=el('text',{'class':'zb',opacity:0},grp); zb.textContent=G.etiquetaHueco||'';
    var PT=G.punto||null, ptc=null, ptl=null;
    if(PT){ ptc=el('circle',{'class':'pv',r:0},grp); ptl=el('text',{'class':'zb',opacity:0},grp); ptl.textContent=PT.etiqueta||''; }
    var dL=el('path',{'class':'dl',d:'',stroke:'var(--warn)',opacity:0},grp), dR=el('path',{'class':'dl',d:'',stroke:'var(--bad)',opacity:0},grp);
    var pL=el('circle',{'class':'pL',r:9,opacity:0},grp), pR=el('circle',{'class':'pR',r:9,opacity:0},grp);
    F.onWin=function(){ cv.setAttribute('d',F.curve()); };
    return { set:function(s){
      F.setZ(s.zoom);
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var hx=X(A), hy=Y(G.hueco.y), xa=F.XA();
      var h=s.hole==null?0:s.hole; hole.setAttribute('r',8*h); hole.setAttribute('cx',hx); hole.setAttribute('cy',hy); hole.style.stroke=s.ok?'var(--ok)':'var(--acc)'; hole.style.fill=s.ok?'var(--ok)':'var(--surf)';
      halo.setAttribute('cx',hx); halo.setAttribute('cy',hy); halo.setAttribute('opacity',s.ok?1:0);
      zb.setAttribute('x',hx+18); zb.setAttribute('y',hy+34); zb.setAttribute('opacity',s.zero?1:0);
      if(PT){ var pv=s.pt==null?0:s.pt, fx=s.fix==null?0:s.fix, py=PT.y+(G.limite-PT.y)*fx; ptc.setAttribute('r',8*pv); ptc.setAttribute('cx',hx); ptc.setAttribute('cy',Y(py)); ptl.setAttribute('x',hx+18); ptl.setAttribute('y',fx>0.5?Y(py)+34:Y(py)+5); ptl.setAttribute('opacity',pv>0.5?1:0); ptl.textContent=fx>0.5?(PT.etiquetaFija||PT.etiqueta||''):(PT.etiqueta||''); }
      var gy=Y(G.limite), gstart=Math.max(F.x0,X(0)); guide.setAttribute('d','M'+gstart+' '+gy+' H'+(F.x1+4)); gl2.setAttribute('y',gy-10);
      guide.setAttribute('opacity',s.guide==null?0:s.guide); gl2.setAttribute('opacity',s.guide==null?0:s.guide);
      if(s.d==null){ [dL,dR,pL,pR].forEach(function(e){ e.setAttribute('opacity',0); }); }
      else{ var l=A-s.d, r=A+s.d, a=s.pa==null?1:s.pa, yl=fCurve(l), yr=fCurve(r), ya=F.YA();
        dL.setAttribute('d','M'+X(l)+' '+ya+' V'+Y(yl)+' H'+xa); dR.setAttribute('d','M'+X(r)+' '+ya+' V'+Y(yr)+' H'+xa);
        pL.setAttribute('cx',X(l)); pL.setAttribute('cy',Y(yl)); pR.setAttribute('cx',X(r)); pR.setAttribute('cy',Y(yr));
        [dL,dR,pL,pR].forEach(function(e){ e.setAttribute('opacity',a); }); }
    }};
  }
  function readouts(d,lEl,rEl){ if(TVM){ var RT=G.rotulos||['tangente','cuerda']; if(d==null){ lEl.textContent='sin datos'; rEl.textContent=RT[1]+' = '+fmt((fFun(G.b)-fFun(G.a))/(G.b-G.a)); return; } lEl.textContent=RT[0]+' = '+fmt(fDer(d)); rEl.textContent=RT[1]+' = '+fmt((fFun(G.b)-fFun(G.a))/(G.b-G.a)); return; }
    if(SEC){ if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } var R=G.rotulos||['h','pendiente']; lEl.textContent=R[0]+' = '+fmt(d); rEl.textContent=R[1]+' = '+fmt((fFun(A+d)-fFun(A))/d); return; }
    if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } lEl.textContent='f('+fmt(A-d)+') = '+fmt(fFun(A-d)); rEl.textContent='f('+fmt(A+d)+') = '+fmt(fFun(A+d)); }

  /* ---------- pregunta con ráfaga de símbolos ---------- */
  function burst(host,x,y){ if(RM) return; '∫∑π∞√'.split('').forEach(function(g,i){ var s=document.createElement('span'); s.className='burst'; s.textContent=g; s.style.left=x+'px'; s.style.top=y+'px'; s.style.setProperty('--x',((i-2)*40)+'px'); s.style.setProperty('--y',(-50-Math.random()*40)+'px'); s.style.setProperty('--r',((i-2)*22)+'deg'); host.appendChild(s); setTimeout(function(){ s.remove(); },1150); }); }
  function Quiz(host){
    var Q=L.pregunta;
    host.innerHTML='<p class="q">Calcula <span data-tex="'+attr(Q.tex)+'"></span></p><div class="opts">'+Q.opciones.map(function(o,i){ return '<button type="button" data-i="'+i+'"><span class="k">'+'abcdefgh'[i]+'</span><span>'+o+'</span></button>'; }).join('')+'</div><p class="fb" aria-live="polite"></p>';
    var fb=host.querySelector('.fb'), done=false;
    [].forEach.call(host.querySelectorAll('.opts button'),function(b){ b.addEventListener('click',function(){
      if(done) return; done=true; var i=+b.getAttribute('data-i');
      [].forEach.call(host.querySelectorAll('.opts button'),function(x){ x.disabled=true; var xi=+x.getAttribute('data-i'); if(xi===Q.correcta) x.classList.add('ok'); else if(xi===i) x.classList.add('no'); });
      if(i===Q.correcta){ var r=b.getBoundingClientRect(), h=host.getBoundingClientRect(); burst(host,r.left-h.left+40,r.top-h.top+8); }
      fb.innerHTML='<b>'+(i===Q.correcta?'Eso es.':'No era esa.')+'</b> '+Q.explicacion;
    }); });
  }

  /* ---------- glosario ---------- */
  var pop=document.getElementById('pop');
  document.addEventListener('click',function(e){ var b=e.target.closest('.gl');
    if(b){ if(!pop.hidden&&pop._b===b){ pop.hidden=true; return; } pop._b=b; pop.textContent=L.glosario[b.getAttribute('data-g')]||''; pop.hidden=false; var r=b.getBoundingClientRect(); pop.style.left=Math.max(8,Math.min(window.innerWidth-300,r.left+window.scrollX))+'px'; pop.style.top=(r.bottom+window.scrollY+8)+'px'; }
    else if(!e.target.closest('#pop')){ pop.hidden=true; } });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') pop.hidden=true; });

  /* ======================= VER ======================= */
  etiquetas();
  var V=L.ver, DUR=V.duracion, gV=Graph(document.getElementById('v-g')), tV=0, playing=false, speed=1, last=null, raf=0;
  function chan(name,t){   /* interpolación entre cuadros clave con suavizado */
    var kf=V.canales[name]; if(!kf) return undefined;
    if(t<kf[0][0]) return name==='d'?null:kf[0][1];
    for(var i=1;i<kf.length;i++){ if(t<kf[i][0]){ var a=kf[i-1],b=kf[i]; return a[1]+(b[1]-a[1])*eio(ap(t,a[0],b[0])); } }
    return kf[kf.length-1][1];
  }
  function stateV(t){
    var s={}; ['draw','hole','guide','pt','fix','nor','zoom'].forEach(function(n){ var v=chan(n,t); if(v!==undefined) s[n]=v; });
    var d=chan('d',t); if(d!==undefined&&d!==null){ s.d=d; s.pa=ap(t,V.canales.d[0][0],V.canales.d[0][0]+0.5); }
    var iv=V.intervalos||{}; if(iv.zero) s.zero=(t>=iv.zero[0]&&t<iv.zero[1]); if(iv.ok) s.ok=(t>=iv.ok[0]);
    return s;
  }
  var scriptEl=document.getElementById('v-script'), ticks=document.getElementById('v-ticks');
  scriptEl.innerHTML=V.capitulos.map(function(c,i){ return '<li data-i="'+i+'"><button type="button"><span class="num">'+(i+1)+'</span><span>'+c[2]+'</span></button></li>'; }).join('');
  ticks.innerHTML=V.capitulos.slice(1).map(function(c){ return '<i style="left:calc('+(c[0]/DUR*100)+'% - 1px)"></i>'; }).join('');
  scriptEl.addEventListener('click',function(e){ var li=e.target.closest('li'); if(!li) return; tV=V.capitulos[+li.getAttribute('data-i')][0]+0.02; renderV(); });
  function renderV(){
    var s=stateV(tV); gV.set(s); readouts(s.d==null?null:s.d,document.getElementById('v-vl'),document.getElementById('v-vr'));
    var cap='Toca play para empezar.', cur=-1; if(tV>0){ V.capitulos.forEach(function(c,i){ if(tV>=c[0]&&tV<c[1]){ cap=c[2]; cur=i; } }); }
    document.getElementById('v-cap').textContent=cap;
    [].forEach.call(scriptEl.children,function(li,i){ li.classList.toggle('cur',i===cur); });
    document.getElementById('v-seek').value=Math.round(tV/DUR*1000); document.getElementById('v-time').textContent=Math.floor(tV)+' s de '+DUR+' s';
  }
  function tickV(now){ if(last===null) last=now; var dt=(now-last)/1000; last=now; tV+=dt*speed; if(tV>=DUR){ tV=DUR; setPlay(false); } renderV(); if(playing) raf=requestAnimationFrame(tickV); }
  function setPlay(p){ playing=p; var b=document.getElementById('v-play'); b.setAttribute('aria-label',p?'Pausar':'Reproducir'); b.innerHTML=ic(p?'i-pause':'i-play'); cancelAnimationFrame(raf); last=null; if(p){ if(tV>=DUR) tV=0; raf=requestAnimationFrame(tickV); } }
  document.getElementById('v-play').addEventListener('click',function(){ setPlay(!playing); });
  document.getElementById('v-redo').addEventListener('click',function(){ tV=0; renderV(); setPlay(true); });
  document.getElementById('v-seek').addEventListener('input',function(e){ tV=e.target.value/1000*DUR; renderV(); });
  [].forEach.call(document.querySelectorAll('.v-sp button'),function(b){ b.addEventListener('click',function(){ speed=+b.getAttribute('data-s'); [].forEach.call(document.querySelectorAll('.v-sp button'),function(x){ x.setAttribute('aria-pressed',x===b?'true':'false'); }); }); });
  document.getElementById('v-stage').addEventListener('keydown',function(e){
    if(e.key===' '||e.key==='k'){ e.preventDefault(); setPlay(!playing); }
    else if(e.key==='ArrowRight'){ e.preventDefault(); tV=cl(tV+2,0,DUR); renderV(); }
    else if(e.key==='ArrowLeft'){ e.preventDefault(); tV=cl(tV-2,0,DUR); renderV(); } });
  if(RM) tV=DUR; renderV();

  /* ======================= LEER (se arma desde los bloques) ======================= */
  var actions={}, inits=[], uid=0;
  function blockHtml(b,secId){
    switch(b.t){
      case 'p': return '<p>'+gl(b.html)+'</p>';
      case 'nota': return '<p class="note">'+gl(b.html)+'</p>';
      case 'eq': return '<div class="eq"><span data-tex="'+attr(b.tex)+'" data-block></span></div>';
      case 'pregunta': return '<div class="card quiz" data-quiz></div>';
      case 'resumen': return '<ul class="sumlist">'+L.resumen.map(function(s,i){ return '<li style="--i:'+i+'">'+ic('i-check')+'<span>'+s+'</span></li>'; }).join('')+'</ul>';
      case 'grafica': { var id='f'+(++uid); (actions[secId]=actions[secId]||[]).push(function(){ var g=Graph(document.getElementById(id)); g.set({draw:0}); tween(1500,function(k){ g.set({draw:eio(k),hole:ap(k,.7,1),zero:k>.9}); }); }); return '<div class="l-fig"><svg class="g" id="'+id+'" viewBox="0 0 640 380" role="img" aria-label="'+attr(b.alt||'Gráfica')+'"></svg></div>'; }
      case 'acercando': { var id2='a'+(++uid), vl=id2+'l', vr=id2+'r'; var run=function(){
          var g=Graph(document.getElementById(id2)), lEl=document.getElementById(vl), rEl=document.getElementById(vr), ds=b.ds, i=1, cur=ds[0], finished=false;
          g.set({draw:1,hole:1,d:ds[0]}); readouts(ds[0],lEl,rEl);
          (function nxt(){ if(i>=ds.length){ var dl=ds[ds.length-1]; g.set({draw:1,hole:1,d:dl,guide:1,ok:true}); if(G.zoom&&b.zoom!==false){ setTimeout(function(){ tween(2200,function(k){ g.set({draw:1,hole:1,d:dl,guide:1,ok:true,zoom:eio(k)}); }); },RM?0:700); } return; }
            var a=cur,z=ds[i]; tween(1400,function(k){ var d=a+(z-a)*eio(k); g.set({draw:1,hole:1,d:d}); readouts(d,lEl,rEl); },function(){ cur=z; i++; setTimeout(nxt,RM?0:450); }); })();
        }; (actions[secId]=actions[secId]||[]).push(function(){ run(); });
        return '<div class="l-fig"><svg class="g" id="'+id2+'" viewBox="0 0 640 380" role="img" aria-label="'+attr(b.alt||'Gráfica')+'"></svg></div><div class="vals"><div class="v l"><span class="lab-l">Por la izquierda</span><b id="'+vl+'">sin datos</b></div><div class="v r"><span class="lab-r">Por la derecha</span><b id="'+vr+'">sin datos</b></div></div>'; }
      case 'piensa': { var pid='p'+(++uid); inits.push(function(){ var root=document.getElementById(pid), picked=false, ring=root.querySelector('.ring'), fg=root.querySelector('.fgc'), rev=root.querySelector('.rev span');
          [].forEach.call(root.querySelectorAll('.row button'),function(btn){ btn.addEventListener('click',function(){ if(picked) return; picked=true; var n=+btn.getAttribute('data-n');
            [].forEach.call(root.querySelectorAll('.row button'),function(x){ x.setAttribute('aria-pressed',x===btn?'true':'false'); x.disabled=true; });
            rev.textContent='Pensando…'; ring.hidden=false; fg.style.strokeDashoffset=100.5;
            tween(1600,function(k){ fg.style.strokeDashoffset=100.5*(1-k); },function(){ ring.hidden=true; root.querySelector('.row button[data-n="'+b.correcta+'"]').classList.add('right'); rev.textContent=(n===b.correcta?b.bien:'No es '+n+'. '+b.mal); }); }); }); });
        return '<p>'+gl(b.pregunta)+'</p><div class="l-think" id="'+pid+'"><div class="row" role="group" aria-label="Elige un número">'+b.opciones.map(function(o){ return '<button type="button" aria-pressed="false" data-n="'+o+'">'+o+'</button>'; }).join('')+'</div><div class="rev" aria-live="polite"><svg class="ring" viewBox="0 0 40 40" aria-hidden="true" hidden><circle class="bgc" cx="20" cy="20" r="16"/><circle class="fgc" cx="20" cy="20" r="16" stroke-dasharray="100.5" stroke-dashoffset="100.5"/></svg><span>Elige una opción y mira lo que pasa.</span></div></div>'; }
      case 'pasos': { var sid='s'+(++uid); inits.push(function(){ var root=document.getElementById(sid), items=root.querySelectorAll('.st'), n=0, next=root.parentNode.querySelector('[data-next]'), all=root.parentNode.querySelector('[data-all]');
            function show(){ if(n>=items.length) return; items[n].classList.add('on'); n++; if(window.MU&&MU.math) MU.math(root); if(n>=items.length){ next.disabled=true; next.firstChild.textContent='Listo'; next.querySelector('svg').style.display='none'; } else { next.firstChild.textContent='Mostrar el paso '+(n+1); } }
            next.addEventListener('click',show); all.addEventListener('click',function(){ while(n<items.length) show(); }); });
        return '<div class="l-steps" id="'+sid+'">'+b.items.map(function(s,i){ return '<div class="st"><div class="eq"><span data-tex="'+attr(s.tex)+'" data-block></span></div><div class="why"><span class="n">'+(i+1)+'</span>'+s.porque+'</div></div>'; }).join('')+'</div><div class="row" style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn pri sm" data-next type="button">Mostrar el primer paso'+ic('i-right')+'</button><button class="btn sec sm" data-all type="button">Ver todo</button></div>'; }
      case 'ojo': (actions[secId]=actions[secId]||[]).push(function(){ var w=document.querySelector('#'+secId+' .l-warn'); if(w) w.classList.add('pulse'); });
        return '<div class="l-warn"><h2>'+ic('i-bulb')+'Ojo con esto</h2><p>'+gl(b.html)+'</p></div>';
    }
    return '';
  }
  var art=document.getElementById('l-art');
  art.innerHTML=L.leer.secciones.map(function(s,i){ var id='ls-'+(i+1); return '<div class="l-sec" id="'+id+'" data-t="'+attr(s.corto||s.titulo)+'"><h2><span class="num">'+(i+1)+'</span>'+s.titulo+'</h2>'+s.bloques.map(function(b){ return blockHtml(b,id); }).join('')+'</div>'; }).join('')+'<p class="fine">'+document.getElementById('fine').textContent+'</p>';
  [].forEach.call(document.querySelectorAll('#m-leer [data-quiz]'),Quiz); inits.forEach(function(fn){ fn(); });
  var secs=[].slice.call(art.querySelectorAll('.l-sec')), rail=document.getElementById('l-rail');
  rail.innerHTML=secs.map(function(s,i){ return '<a href="#'+s.id+'" data-i="'+i+'"><i></i>'+s.getAttribute('data-t')+'</a>'; }).join('');
  var links=[].slice.call(rail.querySelectorAll('a')), ran={};
  function onEnter(id){ if(ran[id]) return; ran[id]=true; (actions[id]||[]).forEach(function(fn){ fn(); }); }
  var wrapL=document.getElementById('l-wrap'), fs=1;
  function setFs(v){ fs=cl(Math.round(v*100)/100,.9,1.3); wrapL.style.setProperty('--rs',fs); }
  document.getElementById('l-fs-m').addEventListener('click',function(){ setFs(fs-.1); }); document.getElementById('l-fs-p').addEventListener('click',function(){ setFs(fs+.1); });
  var fb2=document.getElementById('l-focus'); fb2.addEventListener('click',function(){ var on=fb2.getAttribute('aria-pressed')!=='true'; fb2.setAttribute('aria-pressed',on?'true':'false'); wrapL.classList.toggle('focus',on); });
  var pring=document.getElementById('l-pring'), mins=L.minutos;
  function lScroll(){
    var vh=window.innerHeight, r0=art.getBoundingClientRect();
    var pct=cl(Math.round((vh*0.7-r0.top)/Math.max(r0.height,1)*100),0,100);
    document.getElementById('l-prog').style.width=pct+'%'; document.getElementById('l-pct').textContent=pct+' % leído'; pring.style.strokeDashoffset=100.5*(1-pct/100);
    var left=Math.max(0,Math.round(mins*(1-pct/100))); document.getElementById('l-left').textContent=left>0?'Quedan unos '+left+' min':'Terminaste la lectura';
    var act=0; secs.forEach(function(s,i){ var r=s.getBoundingClientRect(); if(r.top<vh*0.45) act=i; if(r.top<vh*0.85){ s.classList.add('in'); onEnter(s.id); } });
    secs.forEach(function(s,i){ s.classList.toggle('act',i===act); links[i].classList.toggle('on',i===act); links[i].classList.toggle('seen',i<act); });
  }
  window.addEventListener('scroll',lScroll,{passive:true}); window.addEventListener('resize',lScroll);
  var doneB=document.getElementById('l-done');
  doneB.addEventListener('click',function(){ var on=doneB.getAttribute('aria-pressed')!=='true'; doneB.setAttribute('aria-pressed',on?'true':'false'); doneB.querySelector('span').textContent=on?'Vista':'Marcar como vista'; doneB.classList.toggle('sec',on); doneB.classList.toggle('pri',!on); });
  if(RM) secs.forEach(function(s){ s.classList.add('in'); });

  /* ======================= PRACTICAR ======================= */
  var zNow=0, zTok=0, P=L.practicar.pasos, gP=Graph(document.getElementById('p-g')), cur=0, curD=TVM?(G.a+0.3*(G.b-G.a)):0.1, stepsEl=document.getElementById('p-steps');
  stepsEl.innerHTML=P.map(function(s,i){ return '<div class="p-step" data-i="'+i+'"><button class="top" type="button" aria-expanded="false"><span class="num">'+(i+1)+'</span><h2>'+s.titulo+'</h2></button><div class="p-body">'+s.bloques.map(function(b){ return blockHtml(b,'p'+i); }).join('')+'</div></div>'; }).join('');
  [].forEach.call(stepsEl.querySelectorAll('[data-quiz]'),Quiz);
  var dS=document.getElementById('p-d'); function dFrom(v){ if(TVM) return G.a+(G.b-G.a)*(0.05+0.9*v/100); return Math.pow(10,-3+(100-v)/100*3); } function vFrom(d){ if(TVM) return ((d-G.a)/(G.b-G.a)-0.05)/0.9*100; return 100-(Math.log(d)/Math.LN10+3)/3*100; }
  function applyP(){
    var s=P[cur], st={}; for(var k in s.grafica) st[k]=s.grafica[k];
    var ctl=document.getElementById('p-ctl'), vals=document.getElementById('p-vals');
    if(s.laboratorio){ ctl.hidden=false; vals.hidden=false; if(s.d!=null) curD=s.d; dS.value=Math.max(0,Math.min(100,vFrom(curD))); st.d=curD; readouts(curD,document.getElementById('p-vl'),document.getElementById('p-vr')); document.getElementById('p-dv').textContent=fmt(curD); } else { ctl.hidden=true; vals.hidden=true; }
    var z1=st.zoom||0, z0=zNow; zNow=z1; zTok++; var tk=zTok;
    if(G.zoom&&z1!==z0&&!RM){ tween(1000,function(k){ if(tk!==zTok) return; var s2={}; for(var q in st) s2[q]=st[q]; s2.zoom=z0+(z1-z0)*eio(k); gP.set(s2); }); } else gP.set(st);
    [].forEach.call(stepsEl.children,function(c,i){ c.classList.toggle('on',i===cur); c.classList.toggle('past',i<cur); c.querySelector('.top').setAttribute('aria-expanded',i===cur?'true':'false'); });
    document.getElementById('p-prev').disabled=(cur===0); document.getElementById('p-next').disabled=(cur===P.length-1);
    document.getElementById('p-prog').style.width=((cur+1)/P.length*100)+'%';
    if(window.MU&&MU.math) MU.math(document.getElementById('m-practicar'));
  }
  stepsEl.addEventListener('click',function(e){ var h=e.target.closest('.top'); if(!h) return; cur=+h.closest('.p-step').getAttribute('data-i'); applyP(); });
  document.getElementById('p-prev').addEventListener('click',function(){ if(cur>0){ cur--; applyP(); } });
  document.getElementById('p-next').addEventListener('click',function(){ if(cur<P.length-1){ cur++; applyP(); } });
  dS.addEventListener('input',function(){ curD=dFrom(+dS.value); var st={}; for(var k in P[cur].grafica) st[k]=P[cur].grafica[k]; st.d=curD; zTok++; zNow=st.zoom||0; gP.set(st); readouts(curD,document.getElementById('p-vl'),document.getElementById('p-vr')); document.getElementById('p-dv').textContent=fmt(curD); });
  curD=dFrom(+dS.value); applyP();

  /* ======================= modos ======================= */
  var MODES=['ver','leer','practicar'];
  function setMode(m,fromUser){
    if(MODES.indexOf(m)<0) m='ver';
    MODES.forEach(function(k){ document.getElementById('m-'+k).classList.toggle('on',k===m); document.getElementById('mt-'+k).setAttribute('aria-selected',k===m?'true':'false'); });
    if(fromUser){ try{ localStorage.setItem('mu-modo',m); }catch(e){} document.getElementById('modehint').textContent='Quedó guardado como tu modo.'; }
    if(window.MU&&MU.math) MU.math(document.getElementById('m-'+m));
    if(m==='leer') setTimeout(lScroll,60);
    if(m!=='ver' && playing) setPlay(false);
  }
  [].forEach.call(document.querySelectorAll('.seg button'),function(b){ b.addEventListener('click',function(){ setMode(b.getAttribute('data-m'),true); try{ window.scrollTo(0,0); }catch(e){} }); });
  var saved='ver'; try{ saved=localStorage.getItem('mu-modo')||'ver'; }catch(e){}
  setMode(saved,false);
})();
