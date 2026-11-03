(function(){
  var NS='http://www.w3.org/2000/svg';
  var RM=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  var L=JSON.parse(document.getElementById('leccion-datos').textContent);
  var G=L.grafica, SEC=(G.tipo==='secante'), A=SEC?G.a:G.hueco.x, ETQ=G.etiquetas||['Por la izquierda','Por la derecha'];

  /* ---------- utilidades ---------- */
  function cl(v,a,b){ return Math.max(a,Math.min(b,v)); }
  function ap(t,a,b){ return cl((t-a)/(b-a),0,1); }
  function eio(k){ return k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2; }
  function eo(k){ return 1-Math.pow(1-k,3); }
  function fmt(v){ return (Math.round(v*10000)/10000).toFixed(4).replace(/0+$/,'').replace(/\.$/,''); }
  function ic(id){ return '<svg class="ic" aria-hidden="true"><use href="#'+id+'"/></svg>'; }
  function attr(s){ return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;'); }
  function tween(dur,fn,done){ if(RM){ fn(1); if(done) done(); return; } var t0=null; (function s(now){ if(t0===null) t0=now; var k=cl((now-t0)/dur,0,1); fn(k); if(k<1) requestAnimationFrame(s); else if(done) done(); })(performance.now()); }
  function compile(expr){   /* fórmulas del JSON. Solo números, x, operadores y paréntesis */
    if(!/^[0-9x+\-*\/().^\s]+$/.test(expr)) throw new Error('Fórmula no permitida '+expr);
    return new Function('x','return '+expr.replace(/\^/g,'**'));
  }
  var fFun=compile(G.funcion), fCurve=SEC?fFun:compile(G.curva), fDer=SEC?compile(G.derivada):null;
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

  /* ---------- gráfica sin rejilla, configurada por el JSON ---------- */
  var gid=0;
  function GraphSecante(svg){
    var x0=70,x1=620,y0=330,y1=30, XR=G.x, YR=G.y, n=++gid;
    function X(x){ return x0+(x-XR[0])/(XR[1]-XR[0])*(x1-x0); } function Y(y){ return y0-(y-YR[0])/(YR[1]-YR[0])*(y0-y1); }
    function el(t,a,par){ var e=document.createElementNS(NS,t); for(var k in a) e.setAttribute(k,a[k]); (par||svg).appendChild(e); return e; }
    el('path',{'class':'ax',d:'M'+X(0)+' '+(y1-8)+' V'+y0+' M'+x0+' '+Y(0)+' H'+(x1+6)});
    for(var i=Math.ceil(XR[0]);i<=Math.floor(XR[1]);i++){ if(i===0) continue; el('path',{'class':'tk',d:'M'+X(i)+' '+(Y(0)-5)+' v10'}); var t=el('text',{'class':'tt',x:X(i),y:Y(0)+26,'text-anchor':'middle'}); t.textContent=i; }
    for(var j=Math.ceil(YR[0]);j<=Math.floor(YR[1]);j++){ if(j===0) continue; el('path',{'class':'tk',d:'M'+(X(0)-5)+' '+Y(j)+' h10'}); var u=el('text',{'class':'tt',x:X(0)-14,y:Y(j)+4,'text-anchor':'end'}); u.textContent=j; }
    var defs=el('defs',{}), cp=el('clipPath',{id:'cp'+n},defs); el('rect',{x:x0,y:y1,width:x1-x0+6,height:y0-y1},cp);
    var grp=el('g',{'clip-path':'url(#cp'+n+')'});
    var pts=[]; for(var k2=0;k2<=100;k2++){ var xx=XR[0]+(XR[1]-XR[0])*k2/100; pts.push((k2?'L':'M')+X(xx).toFixed(1)+' '+Y(fCurve(xx)).toFixed(1)); }
    var cv=el('path',{'class':'cv',pathLength:1,d:pts.join(' '),'stroke-dashoffset':1},grp);
    var tan=el('line',{'class':'tg',opacity:0},grp), sec=el('line',{'class':'sc',opacity:0},grp), run=el('path',{'class':'dl',d:'',stroke:'var(--warn)',opacity:0},grp);
    var halo=el('circle',{'class':'halo',cx:X(A),cy:Y(fFun(A)),r:12,opacity:0}), pP=el('circle',{'class':'pP',cx:X(A),cy:Y(fFun(A)),r:0}), pQ=el('circle',{'class':'pL',r:9,opacity:0});
    function line(e,m,w){ var xa=XR[0],xb=XR[1], ya=fFun(A)+m*(xa-A), yb=fFun(A)+m*(xb-A); e.setAttribute('x1',X(xa)); e.setAttribute('y1',Y(ya)); e.setAttribute('x2',X(xb)); e.setAttribute('y2',Y(yb)); }
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole; pP.setAttribute('r',9*h); halo.setAttribute('opacity',s.ok?1:0);
      var g=s.guide==null?0:s.guide; line(tan,fDer(A)); tan.setAttribute('opacity',g); tan.style.strokeWidth=s.ok?5:3.5;
      if(s.d==null){ sec.setAttribute('opacity',0); run.setAttribute('opacity',0); pQ.setAttribute('opacity',0); }
      else{ var q=A+s.d, m=(fFun(q)-fFun(A))/s.d, a=s.pa==null?1:s.pa; line(sec,m); sec.setAttribute('opacity',a*(g>0.5?0.35:1));
        run.setAttribute('d','M'+X(A)+' '+Y(fFun(A))+' H'+X(q)+' V'+Y(fFun(q))); run.setAttribute('opacity',a*(g>0.5?0:1));
        pQ.setAttribute('cx',X(q)); pQ.setAttribute('cy',Y(fFun(q))); pQ.setAttribute('opacity',a); }
    }};
  }
  function Graph(svg){
    if(SEC) return GraphSecante(svg);
    var x0=70,x1=620,y0=330,y1=30, XR=G.x, YR=G.y;
    function X(x){ return x0+(x-XR[0])/(XR[1]-XR[0])*(x1-x0); } function Y(y){ return y0-(y-YR[0])/(YR[1]-YR[0])*(y0-y1); }
    function el(t,a){ var e=document.createElementNS(NS,t); for(var k in a) e.setAttribute(k,a[k]); svg.appendChild(e); return e; }
    el('path',{'class':'ax',d:'M'+X(0)+' '+(y1-8)+' V'+y0+' M'+x0+' '+Y(0)+' H'+(x1+6)});
    for(var i=Math.ceil(XR[0]);i<=Math.floor(XR[1]);i++){ if(i===0) continue; el('path',{'class':'tk',d:'M'+X(i)+' '+(Y(0)-5)+' v10'}); var t=el('text',{'class':'tt',x:X(i),y:Y(0)+26,'text-anchor':'middle'}); t.textContent=i; }
    for(var j=Math.ceil(YR[0]);j<=Math.floor(YR[1]);j++){ if(j===0) continue; el('path',{'class':'tk',d:'M'+(X(0)-5)+' '+Y(j)+' h10'}); var u=el('text',{'class':'tt',x:X(0)-14,y:Y(j)+4,'text-anchor':'end'}); u.textContent=j; }
    var guide=el('path',{'class':'gd',d:'M'+X(XR[0]<0?0:XR[0])+' '+Y(G.limite)+' H'+(x1+4),opacity:0}); var gl2=el('text',{'class':'gl',x:x1,y:Y(G.limite)-10,'text-anchor':'end',opacity:0}); gl2.textContent='y = '+G.limite;
    var cv=el('path',{'class':'cv',pathLength:1,d:'M'+X(XR[0])+' '+Y(fCurve(XR[0]))+' L'+X(XR[1])+' '+Y(fCurve(XR[1])),'stroke-dashoffset':1});
    var halo=el('circle',{'class':'halo',cx:X(A),cy:Y(G.hueco.y),r:12,opacity:0});
    var hole=el('circle',{'class':'hole',cx:X(A),cy:Y(G.hueco.y),r:0});
    var zb=el('text',{'class':'zb',x:X(A)+18,y:Y(G.hueco.y)+34,opacity:0}); zb.textContent=G.etiquetaHueco||'';
    var dL=el('path',{'class':'dl',d:'',stroke:'var(--warn)',opacity:0}), dR=el('path',{'class':'dl',d:'',stroke:'var(--bad)',opacity:0});
    var pL=el('circle',{'class':'pL',r:9,opacity:0}), pR=el('circle',{'class':'pR',r:9,opacity:0});
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole; hole.setAttribute('r',8*h); hole.style.stroke=s.ok?'var(--ok)':'var(--acc)'; hole.style.fill=s.ok?'var(--ok)':'var(--surf)';
      halo.setAttribute('opacity',s.ok?1:0); zb.setAttribute('opacity',s.zero?1:0);
      guide.setAttribute('opacity',s.guide==null?0:s.guide); gl2.setAttribute('opacity',s.guide==null?0:s.guide);
      if(s.d==null){ [dL,dR,pL,pR].forEach(function(e){ e.setAttribute('opacity',0); }); }
      else{ var l=A-s.d, r=A+s.d, a=s.pa==null?1:s.pa, yl=fCurve(l), yr=fCurve(r);
        dL.setAttribute('d','M'+X(l)+' '+Y(0)+' V'+Y(yl)+' H'+X(0)); dR.setAttribute('d','M'+X(r)+' '+Y(0)+' V'+Y(yr)+' H'+X(0));
        pL.setAttribute('cx',X(l)); pL.setAttribute('cy',Y(yl)); pR.setAttribute('cx',X(r)); pR.setAttribute('cy',Y(yr));
        [dL,dR,pL,pR].forEach(function(e){ e.setAttribute('opacity',a); }); }
    }};
  }
  function readouts(d,lEl,rEl){ if(SEC){ if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } lEl.textContent='h = '+fmt(d); rEl.textContent='pendiente = '+fmt((fFun(A+d)-fFun(A))/d); return; }
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
    var s={}; ['draw','hole','guide'].forEach(function(n){ var v=chan(n,t); if(v!==undefined) s[n]=v; });
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
          (function nxt(){ if(i>=ds.length){ g.set({draw:1,hole:1,d:ds[ds.length-1],guide:1,ok:true}); return; }
            var a=cur,z=ds[i]; tween(1400,function(k){ var d=a+(z-a)*eio(k); g.set({draw:1,hole:1,d:d}); readouts(d,lEl,rEl); },function(){ cur=z; i++; setTimeout(nxt,RM?0:450); }); })();
        }; (actions[secId]=actions[secId]||[]).push(function(){ var g=Graph(document.getElementById(id2)); g.set({draw:1,hole:1}); run(); });
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
  var P=L.practicar.pasos, gP=Graph(document.getElementById('p-g')), cur=0, curD=0.1, stepsEl=document.getElementById('p-steps');
  stepsEl.innerHTML=P.map(function(s,i){ return '<div class="p-step" data-i="'+i+'"><button class="top" type="button" aria-expanded="false"><span class="num">'+(i+1)+'</span><h2>'+s.titulo+'</h2></button><div class="p-body">'+s.bloques.map(function(b){ return blockHtml(b,'p'+i); }).join('')+'</div></div>'; }).join('');
  [].forEach.call(stepsEl.querySelectorAll('[data-quiz]'),Quiz);
  var dS=document.getElementById('p-d'); function dFrom(v){ return Math.pow(10,-3+(100-v)/100*3); }
  function applyP(){
    var s=P[cur], st={}; for(var k in s.grafica) st[k]=s.grafica[k];
    var ctl=document.getElementById('p-ctl'), vals=document.getElementById('p-vals');
    if(s.laboratorio){ ctl.hidden=false; vals.hidden=false; if(s.d!=null) curD=s.d; st.d=curD; readouts(curD,document.getElementById('p-vl'),document.getElementById('p-vr')); document.getElementById('p-dv').textContent=fmt(curD); } else { ctl.hidden=true; vals.hidden=true; }
    gP.set(st);
    [].forEach.call(stepsEl.children,function(c,i){ c.classList.toggle('on',i===cur); c.classList.toggle('past',i<cur); c.querySelector('.top').setAttribute('aria-expanded',i===cur?'true':'false'); });
    document.getElementById('p-prev').disabled=(cur===0); document.getElementById('p-next').disabled=(cur===P.length-1);
    document.getElementById('p-prog').style.width=((cur+1)/P.length*100)+'%';
    if(window.MU&&MU.math) MU.math(document.getElementById('m-practicar'));
  }
  stepsEl.addEventListener('click',function(e){ var h=e.target.closest('.top'); if(!h) return; cur=+h.closest('.p-step').getAttribute('data-i'); applyP(); });
  document.getElementById('p-prev').addEventListener('click',function(){ if(cur>0){ cur--; applyP(); } });
  document.getElementById('p-next').addEventListener('click',function(){ if(cur<P.length-1){ cur++; applyP(); } });
  dS.addEventListener('input',function(){ curD=dFrom(+dS.value); var st={}; for(var k in P[cur].grafica) st[k]=P[cur].grafica[k]; st.d=curD; gP.set(st); readouts(curD,document.getElementById('p-vl'),document.getElementById('p-vr')); document.getElementById('p-dv').textContent=fmt(curD); });
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
