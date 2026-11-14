(function(){
  var NS='http://www.w3.org/2000/svg';
  var RM=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  var L=JSON.parse(document.getElementById('leccion-datos').textContent);
  var G=L.grafica, SEC=(G.tipo==='secante'), TVM=(G.tipo==='tvm'), NEW=(G.tipo==='newton'), ARE=(G.tipo==='area'||G.tipo==='entre'||G.tipo==='polar'), ENT=(G.tipo==='entre'), POL=(G.tipo==='polar'), PLA=(G.tipo==='plano'), ASI=(G.tipo==='asintota'), A=(SEC||TVM||ARE)?G.a:(G.hueco?G.hueco.x:0), ETQ=G.etiquetas||['Por la izquierda','Por la derecha'];

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
  var FN=/\b(sin|cos|tan|asin|acos|atan|exp|ln|sqrt|abs|pi)\b/g;
  function compile(expr){   /* fórmulas del JSON. Números, x, operadores, paréntesis y sin cos tan exp ln sqrt abs pi */
    if(!/^[0-9x+\-*\/().^\s]*$/.test(String(expr).replace(FN,''))) throw new Error('Fórmula no permitida '+expr);
    var js=String(expr).replace(/\^/g,'**').replace(/\bln\b/g,'log').replace(/\bpi\b/g,'PI').replace(FN,function(m){ return m; });
    js=js.replace(/\b(sin|cos|tan|asin|acos|atan|exp|log|sqrt|abs|PI)\b/g,'Math.$1');
    return new Function('x','return '+js);
  }
  var fFun=PLA?null:compile(G.funcion), fCurve=PLA?null:((SEC||TVM||NEW||ARE||ASI)?fFun:compile(G.curva)), fDer=(SEC||TVM||NEW)?compile(G.derivada):null, fPri=ARE?compile(G.primitiva):null, fInf=ENT?compile(G.inferior):null, NX=null;
  if(NEW){ NX=[G.x0]; for(var ni=0;ni<G.pasos;ni++) NX.push(NX[ni]-fFun(NX[ni])/fDer(NX[ni])); }
  function nf(v){ if(!isFinite(v)) return v>0?'∞':(v<0?'-∞':'sin valor'); var a=Math.abs(v); if(a!==0&&(a<1e-6||a>=1e6)) return v.toExponential(2); return (+v.toFixed(a>=100?2:(a>=1?6:8))).toString(); }
  function gl(h){ return h.replace(/\{\{gl:([a-z0-9_]+)\|([^}]+)\}\}/g,'<button class="gl" type="button" data-g="$1">$2</button>'); }

  /* ---------- cabecera ---------- */
  document.title='Lección '+L.titulo;
  document.getElementById('crumb').innerHTML='<span>'+L.curso+'</span><span class="sep">/</span><span>'+L.modulo+'</span><span class="sep">/</span><span class="num">'+L.posicion+'</span>';
  document.getElementById('titulo').textContent=L.titulo;
  document.getElementById('lmeta').innerHTML='<span>'+ic('i-clock')+'<span class="num">'+L.minutos+'</span> min</span><span>'+ic('i-target')+'<span class="num">'+L.ejercicios+'</span> '+(L.ejercicios==1?'ejercicio':'ejercicios')+'</span><span>El mismo contenido en tres modos</span>';
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
    F.XA=function(){ var v=F.X(0); return (v<F.x0||v>F.x1)?F.x0:v; };
    F.YA=function(){ var v=F.Y(0); return (v>F.y0||v<F.y1)?F.y0:v; };
    F.el=function(t,a,par){ var e=document.createElementNS(NS,t); for(var k in a) e.setAttribute(k,a[k]); (par||svg).appendChild(e); return e; };
    var ag=F.el('g',{}), zl=null;
    function fm(v,dec){ var t=v.toFixed(dec); return t==='-0'||/^-0\.?0*$/.test(t)?t.replace('-',''):t; }
    F.axes=function(){
      while(ag.firstChild) ag.removeChild(ag.firstChild);
      if(G.sinejes) return;
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
    F.curve=function(fn){ var fc=fn||fCurve, d=[], on=false, N=160, prev=0, salto=(F.YR[1]-F.YR[0])*20; for(var k=0;k<=N;k++){ var xx=F.XR[0]+(F.XR[1]-F.XR[0])*k/N, yv=fc(xx); if(!isFinite(yv)) yv=fc(xx+1e-9); if(!isFinite(yv)){ on=false; continue; } if(on&&Math.abs(yv-prev)>salto) on=false; prev=yv; var py=Math.max(-5e4,Math.min(5e4,F.Y(yv))); d.push((on?'L':'M')+F.X(xx).toFixed(1)+' '+py.toFixed(1)); on=true; } return d.join(' '); };
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
  /* método de Newton. Estado d = número de tangentes dibujadas (admite decimales para animar) */
  function GraphNewton(svg){
    var N=G.pasos, F=Frame(svg,0,0), X=F.X, Y=F.Y, el=F.el, grp=F.clip();
    var cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var vl=[], tl=[], pc=[], pa=[], lb=[];
    for(var j=0;j<=N;j++){ vl.push(el('path',{'class':'dl',stroke:'var(--warn)',opacity:0,d:'M'+X(NX[j])+' '+Y(0)+' V'+Y(fFun(NX[j]))},grp)); }
    for(var j2=0;j2<N;j2++){ var m=fDer(NX[j2]), xa=F.XR[0], xb=F.XR[1], y0=fFun(NX[j2]); tl.push(el('line',{'class':'tg',opacity:0,x1:X(xa),y1:Y(y0+m*(xa-NX[j2])),x2:X(xb),y2:Y(y0+m*(xb-NX[j2]))},grp)); }
    for(var j3=0;j3<=N;j3++){ pc.push(el('circle',{'class':'pL',r:7,opacity:0,cx:X(NX[j3]),cy:Y(fFun(NX[j3]))},grp)); pa.push(el('circle',{'class':'pP',r:7,opacity:0,cx:X(NX[j3]),cy:Y(0)},grp)); var t=el('text',{'class':'zb',opacity:0,x:X(NX[j3])+9,y:Y(0)-9-(j3%2)*18},grp); t.textContent='x'+j3; lb.push(t); }
    var halo=el('circle',{'class':'halo',r:12,opacity:0,cx:X(G.raiz),cy:Y(0)},grp);
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var k=s.d; halo.setAttribute('opacity',s.ok?1:0);
      for(var j=0;j<=N;j++){ var op=(k==null)?0:(j===0?1:cl(k-(j-1),0,1)); [vl[j],pc[j],pa[j],lb[j]].forEach(function(e){ e.setAttribute('opacity',op); }); }
      for(var i=0;i<N;i++){ var t2=(k==null)?0:cl(k-i,0,1), old=(k!=null&&k-i>1); tl[i].setAttribute('opacity',old?0.35:t2); tl[i].style.strokeWidth=old?2.5:3.5; }
    }};
  }
  /* área bajo la curva. Estado d = límite superior x, guide muestra la franja delgada, hole marca el límite inferior */
  function GraphArea(svg){
    var a=G.a, b=G.b, lo=function(x){ return ENT?fInf(x):0; }, F=Frame(svg,(a+b)/2,ENT?(fFun(b)+fInf(b))/2:fFun(b)/2), X=F.X, Y=F.Y, el=F.el, grp=F.clip(), w=G.franja||0.15;
    var ar=el('path',{'class':'ar',opacity:0,d:''},grp), cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var cv2=ENT?el('path',{'class':'cv cv2',pathLength:1,d:F.curve(fInf),'stroke-dashoffset':1},grp):null, pB=ENT?el('circle',{'class':'pL',r:7,opacity:0},grp):null;
    var sl=el('rect',{'class':'ar2',opacity:0},grp), vl=el('path',{'class':'dl',stroke:'var(--warn)',opacity:0},grp);
    var pA=el('circle',{'class':'pP',r:0,cx:X(a),cy:Y(lo(a))},grp), lA=el('text',{'class':'zb',opacity:0,x:X(a),y:Y(lo(a))+34,'text-anchor':'middle'},grp); lA.textContent='a = '+fmt(a);
    var pM=el('circle',{'class':'pL',r:9,opacity:0},grp), lM=el('text',{'class':'zb','text-anchor':'middle',opacity:0},grp), halo=el('circle',{'class':'halo',r:12,opacity:0},grp);
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole; pA.setAttribute('r',8*h); lA.setAttribute('opacity',h>0.5?1:0); if(cv2) cv2.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      if(s.d==null){ [ar,sl,vl,pM,lM,halo].concat(pB?[pB]:[]).forEach(function(e){ e.setAttribute('opacity',0); }); return; }
      var x=s.d, y=fFun(x), yb=lo(x), al=s.pa==null?1:s.pa, d=['M'+X(a)+' '+Y(lo(a))]; for(var k=0;k<=60;k++){ var xx=a+(x-a)*k/60; d.push('L'+X(xx).toFixed(1)+' '+Y(fFun(xx)).toFixed(1)); } if(ENT){ for(var k2=60;k2>=0;k2--){ var xb=a+(x-a)*k2/60; d.push('L'+X(xb).toFixed(1)+' '+Y(fInf(xb)).toFixed(1)); } d.push('Z'); } else d.push('L'+X(x)+' '+Y(0)+' Z');
      ar.setAttribute('d',d.join(' ')); ar.setAttribute('opacity',al);
      var g=s.guide==null?0:s.guide; sl.setAttribute('x',X(x)); sl.setAttribute('y',Y(y)); sl.setAttribute('width',Math.max(1,X(x+w)-X(x))); sl.setAttribute('height',Math.max(0,Y(yb)-Y(y))); sl.setAttribute('opacity',g);
      vl.setAttribute('d','M'+X(x)+' '+Y(yb)+' V'+Y(y)); vl.setAttribute('opacity',al); if(pB){ pB.setAttribute('cx',X(x)); pB.setAttribute('cy',Y(yb)); pB.setAttribute('opacity',al); }
      pM.setAttribute('cx',X(x)); pM.setAttribute('cy',Y(y)); pM.setAttribute('opacity',al); halo.setAttribute('cx',X(x)); halo.setAttribute('cy',Y(y)); halo.setAttribute('opacity',s.ok?1:0);
      lM.setAttribute('x',X(x)); lM.setAttribute('y',Y(y)-18); lM.textContent='x = '+fmt(x); lM.setAttribute('opacity',al);
    }};
  }
  /* asíntotas. Estado d = x del punto móvil. Con expandir la ventana crece para incluir x grandes */
  function GraphAsint(svg){
    var F=Frame(svg,0,0), X=F.X, Y=F.Y, el=F.el, grp=F.clip(), base=G.x.slice();
    var cv=el('path',{'class':'cv',pathLength:1,d:F.curve(),'stroke-dashoffset':1},grp);
    var as=(G.asintotas||[]).map(function(a){ var p=el('path',{'class':'gd',opacity:0,d:''},grp), t=el('text',{'class':'gl',opacity:0,'text-anchor':a.x!=null?'start':'end'},grp); t.textContent=a.etiqueta||''; return {a:a,p:p,t:t}; });
    var dv=el('path',{'class':'dl',stroke:'var(--warn)',opacity:0,d:''},grp), pM=el('circle',{'class':'pL',r:9,opacity:0},grp), lM=el('text',{'class':'zb','text-anchor':'middle',opacity:0},grp);
    return { set:function(s){
      var xmax=base[1]; if(G.expandir&&s.d!=null) xmax=Math.max(base[1],s.d*1.12);
      if(Math.abs(xmax-F.XR[1])>1e-9){ F.XR=[base[0],xmax]; F.axes(); cv.setAttribute('d',F.curve()); }
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var g=s.guide==null?0:s.guide;
      as.forEach(function(o){ if(o.a.y!=null){ o.p.setAttribute('d','M'+F.x0+' '+Y(o.a.y)+' H'+(F.x1+4)); o.t.setAttribute('x',F.x1-6); o.t.setAttribute('y',Y(o.a.y)-10); }
        else { o.p.setAttribute('d','M'+X(o.a.x)+' '+(F.y1-4)+' V'+F.y0); o.t.setAttribute('x',X(o.a.x)+10); o.t.setAttribute('y',F.y1+16); }
        o.p.setAttribute('opacity',g); o.t.setAttribute('opacity',g); });
      if(s.d==null){ [dv,pM,lM].forEach(function(e){ e.setAttribute('opacity',0); }); return; }
      var x=G.entero?Math.max(0,Math.round(s.d)):s.d, y=fFun(x), al=s.pa==null?1:s.pa;
      pM.setAttribute('cx',X(x)); pM.setAttribute('cy',Y(y)); pM.setAttribute('opacity',al);
      dv.setAttribute('d','M'+X(x)+' '+F.YA()+' V'+Y(y)); dv.setAttribute('opacity',al);
      lM.setAttribute('x',X(x)); lM.setAttribute('y',Y(y)-18); lM.textContent=(G.rotulos?G.rotulos[0]:'x')+' = '+nf(x); lM.setAttribute('opacity',al);
    }};
  }
  /* polares. La función es r de theta. Estado d = theta del radio móvil. primitiva es el área del sector, la mitad de la integral de r cuadrado */
  function GraphPolar(svg){
    var a=G.a, w=G.franja||0.15, F=Frame(svg,0,0), X=F.X, Y=F.Y, el=F.el, grp=F.clip(), r0=G.rango||[G.a,G.b];
    function P(t){ var r=fFun(t); return [X(r*Math.cos(t)),Y(r*Math.sin(t))]; }
    function tr(t0,t1,n,mv){ var d=[]; for(var k=0;k<=n;k++){ var t=t0+(t1-t0)*k/n, p=P(t); d.push((k===0&&mv?'M':'L')+p[0].toFixed(1)+' '+p[1].toFixed(1)); } return d.join(' '); }
    var O='M'+X(0)+' '+Y(0);
    var ar=el('path',{'class':'ar',opacity:0,d:''},grp), cv=el('path',{'class':'cv',pathLength:1,d:tr(r0[0],r0[1],240,true),'stroke-dashoffset':1},grp);
    var sl=el('path',{'class':'ar2',opacity:0,d:''},grp), vl=el('path',{'class':'dl',stroke:'var(--warn)',opacity:0},grp);
    var pa=P(a), pA=el('circle',{'class':'pP',r:0,cx:pa[0],cy:pa[1]},grp), lA=el('text',{'class':'zb',opacity:0,x:pa[0]+4,y:pa[1]-16,'text-anchor':'middle'},grp); lA.textContent='\u03b8 = '+fmt(a);
    var pM=el('circle',{'class':'pL',r:9,opacity:0},grp), lM=el('text',{'class':'zb','text-anchor':'middle',opacity:0},grp), halo=el('circle',{'class':'halo',r:12,opacity:0},grp);
    return { set:function(s){
      cv.style.strokeDashoffset=1-(s.draw==null?1:s.draw);
      var h=s.hole==null?0:s.hole; pA.setAttribute('r',8*h); lA.setAttribute('opacity',h>0.5?1:0);
      if(s.d==null){ [ar,sl,vl,pM,lM,halo].forEach(function(e){ e.setAttribute('opacity',0); }); return; }
      var t=s.d, al=s.pa==null?1:s.pa, p=P(t), g=s.guide==null?0:s.guide;
      ar.setAttribute('d',O+' '+tr(a,t,Math.max(2,Math.ceil(120*Math.abs(t-a)/(2*Math.PI)+2)),false)+' Z'); ar.setAttribute('opacity',al);
      sl.setAttribute('d',O+' '+tr(t,t+w,6,false)+' Z'); sl.setAttribute('opacity',g);
      vl.setAttribute('d',O+' L'+p[0]+' '+p[1]); vl.setAttribute('opacity',al);
      pM.setAttribute('cx',p[0]); pM.setAttribute('cy',p[1]); pM.setAttribute('opacity',al); halo.setAttribute('cx',p[0]); halo.setAttribute('cy',p[1]); halo.setAttribute('opacity',s.ok?1:0);
      lM.setAttribute('x',p[0]); lM.setAttribute('y',p[1]-18); lM.textContent='\u03b8 = '+fmt(t); lM.setAttribute('opacity',al);
    }};
  }
  /* plano. Escena con vectores, polígonos, rectas, segmentos y puntos cuyas coordenadas son fórmulas del parámetro x. Estado d = parámetro, draw va mostrando los elementos en orden, guide muestra los que traen guia y ok los que traen fin */
  var COL=['var(--curve)','var(--warn)','var(--acc)','var(--ok)'];
  var LEC=PLA?(G.lecturas||[]).map(function(l){ return {r:l.rotulo,f:compile(String(l.formula))}; }):[];
  function GraphPlano(svg){
    var F=Frame(svg,0,0), X=F.X, Y=F.Y, el=F.el, grp=F.clip(), items=[], E=G.elementos||[];
    function cp(a){ return (a||['0','0']).map(function(s){ return compile(String(s)); }); }
    function ev(c,t){ return [c[0](t),c[1](t)]; }
    E.forEach(function(e){
      var o={e:e,col:COL[(e.c||0)%4]};
      if(e.t==='vector'){ o.a=cp(e.a); o.b=cp(e.b); o.ln=el('path',{fill:'none',stroke:o.col,'stroke-width':4,'stroke-linecap':'round',opacity:0},grp); o.hd=el('path',{fill:o.col,stroke:'none',opacity:0},grp); }
      else if(e.t==='trazo'){ o.p=(e.puntos||[]).map(cp); o.ln=el('path',{fill:'none',stroke:o.col,'stroke-width':4,'stroke-linejoin':'round','stroke-linecap':'round',opacity:0},grp); }
      else if(e.t==='poligono'){ o.p=(e.puntos||[]).map(cp); o.ln=el('path',{fill:o.col,'fill-opacity':0.26,stroke:o.col,'stroke-width':2,opacity:0},grp); }
      else if(e.t==='recta'){ o.p=cp(e.p); o.d=cp(e.dir); o.ln=el('path',{fill:'none',stroke:o.col,'stroke-width':3,'stroke-dasharray':e.guion?'7 6':'none',opacity:0},grp); }
      else if(e.t==='segmento'){ o.a=cp(e.a); o.b=cp(e.b); o.ln=el('path',{fill:'none',stroke:o.col,'stroke-width':3,'stroke-dasharray':e.guion?'7 6':'none',opacity:0},grp); }
      else if(e.t==='punto'){ o.p=cp(e.p); o.pt=el('circle',{r:7,fill:o.col,opacity:0},grp); }
      if(e.nombre){ o.tx=el('text',{'class':'zb',opacity:0,'text-anchor':'middle'},grp); o.tx.textContent=e.nombre; o.tx.style.fill=o.col; }
      items.push(o);
    });
    return { set:function(s){
      var t=s.d==null?(G.inicio!=null?G.inicio:G.a):s.d; if(G.entero) t=Math.round(t); var dr=s.draw==null?1:s.draw, n=Math.max(1,items.length), gd=s.guide==null?0:Math.min(1,s.guide);
      items.forEach(function(o,i){
        var e=o.e, al=Math.max(0,Math.min(1,dr*n-i)); if(e.guia) al*=gd; if(e.fin) al*=(s.ok?1:0);
        var main=o.ln||o.pt; main.setAttribute('opacity',al); if(o.hd) o.hd.setAttribute('opacity',al); if(o.tx) o.tx.setAttribute('opacity',al);
        if(al<=0) return;
        var lx=0, ly=0;
        if(e.t==='vector'){
          var a=ev(o.a,t), b=ev(o.b,t), pa0=X(a[0]), pa1=Y(a[1]), pb0=X(b[0]), pb1=Y(b[1]), dx=pb0-pa0, dy=pb1-pa1, len=Math.sqrt(dx*dx+dy*dy), ang=Math.atan2(dy,dx), c=Math.cos(ang), sn=Math.sin(ang);
          if(len<14){ o.ln.setAttribute('d',''); o.hd.setAttribute('d',''); if(o.tx) o.tx.setAttribute('opacity',0); }
          else { o.ln.setAttribute('d','M'+pa0+' '+pa1+' L'+(pb0-9*c)+' '+(pb1-9*sn)); o.hd.setAttribute('d','M'+pb0+' '+pb1+' L'+(pb0-15*Math.cos(ang-0.42))+' '+(pb1-15*Math.sin(ang-0.42))+' L'+(pb0-15*Math.cos(ang+0.42))+' '+(pb1-15*Math.sin(ang+0.42))+' Z'); }
          lx=pb0+20*c; ly=pb1+20*sn+4;
        } else if(e.t==='trazo'){
          var tq=o.p.map(function(q){ var v=ev(q,t); return isFinite(v[0])&&isFinite(v[1])?[X(v[0]),Y(Math.max(-1e5,Math.min(1e5,v[1])))]:null; }), dd='', pen=false; tq.forEach(function(q){ if(!q){ pen=false; return; } dd+=(pen?' L':' M')+q[0].toFixed(1)+' '+q[1].toFixed(1); pen=true; }); o.ln.setAttribute('d',dd.trim()); var ql=tq.filter(function(q){ return q; }); if(ql.length){ lx=ql[ql.length-1][0]; ly=ql[ql.length-1][1]-1; }2;
        } else if(e.t==='poligono'){
          var ps=o.p.map(function(q){ var v=ev(q,t); return [X(v[0]),Y(v[1])]; }); o.ln.setAttribute('d','M'+ps.map(function(q){ return q[0].toFixed(1)+' '+q[1].toFixed(1); }).join(' L')+' Z');
          lx=ps.reduce(function(m,q){ return m+q[0]; },0)/ps.length; ly=ps.reduce(function(m,q){ return m+q[1]; },0)/ps.length+4;
        } else if(e.t==='recta'){
          var p=ev(o.p,t), d=ev(o.d,t), q0=X(p[0]), q1=Y(p[1]), ex=X(p[0]+d[0])-q0, ey=Y(p[1]+d[1])-q1, ee=Math.sqrt(ex*ex+ey*ey)||1; ex=ex/ee*2000; ey=ey/ee*2000;
          o.ln.setAttribute('d','M'+(q0-ex)+' '+(q1-ey)+' L'+(q0+ex)+' '+(q1+ey)); lx=q0+14; ly=q1-12;
        } else if(e.t==='segmento'){
          var a2=ev(o.a,t), b2=ev(o.b,t); o.ln.setAttribute('d','M'+X(a2[0])+' '+Y(a2[1])+' L'+X(b2[0])+' '+Y(b2[1])); lx=(X(a2[0])+X(b2[0]))/2+12; ly=(Y(a2[1])+Y(b2[1]))/2-8;
        } else if(e.t==='punto'){
          var pp=ev(o.p,t); o.pt.setAttribute('cx',X(pp[0])); o.pt.setAttribute('cy',Y(pp[1])); lx=X(pp[0]); ly=Y(pp[1])-14;
        }
        if(o.tx){ o.tx.setAttribute('x',lx); o.tx.setAttribute('y',ly); }
      });
    }};
  }
  function Graph(svg){
    if(SEC) return GraphSecante(svg);
    if(TVM) return GraphTVM(svg);
    if(NEW) return GraphNewton(svg);
    if(PLA) return GraphPlano(svg);
    if(POL) return GraphPolar(svg);
    if(ARE) return GraphArea(svg);
    if(ASI) return GraphAsint(svg);
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
  function readouts(d,lEl,rEl){
    if(PLA){ var tt=d==null?(G.inicio!=null?G.inicio:G.a):d; if(G.entero) tt=Math.round(tt); var sp=function(v){ return Math.abs(v)<1e-6?0:v; }; lEl.textContent=LEC[0].r+' = '+nf(sp(LEC[0].f(tt))); rEl.textContent=LEC[1].r+' = '+nf(sp(LEC[1].f(tt))); return; }
    if(NEW){ if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } var kk=Math.max(0,Math.min(G.pasos,Math.round(d))); lEl.textContent='x'+kk+' = '+nf(NX[kk]); rEl.textContent='f(x'+kk+') = '+nf(fFun(NX[kk])); return; }
    if(ARE){ var RA=G.rotulos||(ENT?['área','separación']:(POL?['área','r']:['área','altura'])); if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } var sn=function(v){ return Math.abs(v)<1e-7?0:v; }; lEl.textContent=RA[0]+' = '+nf(sn(fPri(d)-fPri(G.a))); rEl.textContent=RA[1]+' = '+nf(sn(ENT?fFun(d)-fInf(d):fFun(d))); return; }
    if(ASI){ if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } var dd=G.entero?Math.max(0,Math.round(d)):d, RS=G.rotulos||['x','f(x)']; lEl.textContent=RS[0]+' = '+nf(dd); rEl.textContent=RS[1]+' = '+nf(fFun(dd)); return; }
    if(TVM){ var RT=G.rotulos||['tangente','cuerda']; if(d==null){ lEl.textContent='sin datos'; rEl.textContent=RT[1]+' = '+fmt((fFun(G.b)-fFun(G.a))/(G.b-G.a)); return; } lEl.textContent=RT[0]+' = '+fmt(fDer(d)); rEl.textContent=RT[1]+' = '+fmt((fFun(G.b)-fFun(G.a))/(G.b-G.a)); return; }
    if(SEC){ if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } var R=G.rotulos||['h','pendiente']; lEl.textContent=R[0]+' = '+fmt(d); rEl.textContent=R[1]+' = '+fmt((fFun(A+d)-fFun(A))/d); return; }
    if(d==null){ lEl.textContent='sin datos'; rEl.textContent='sin datos'; return; } lEl.textContent='f('+fmt(A-d)+') = '+fmt(fFun(A-d)); rEl.textContent='f('+fmt(A+d)+') = '+fmt(fFun(A+d)); }

  /* ---------- pregunta con ráfaga de símbolos ---------- */
  function burst(host,x,y){ if(RM) return; '∫∑π∞√'.split('').forEach(function(g,i){ var s=document.createElement('span'); s.className='burst'; s.textContent=g; s.style.left=x+'px'; s.style.top=y+'px'; s.style.setProperty('--x',((i-2)*40)+'px'); s.style.setProperty('--y',(-50-Math.random()*40)+'px'); s.style.setProperty('--r',((i-2)*22)+'deg'); host.appendChild(s); setTimeout(function(){ s.remove(); },1150); }); }
  /* ---------- texto con matemática en línea, repaso espaciado y actividades guiadas ---------- */
  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;'); }
  function mt(s){ return String(s).split('$').map(function(x,i){ return i%2?'<span data-tex="'+attr(x)+'"></span>':esc(x); }).join(''); }
  function mtH(s){ return /\$/.test(s)?mt(s):s; }
  function mathIn(el){ if(window.MU&&MU.math) MU.math(el); }
  function fechaCorta(ms){ try{ return new Date(ms).toLocaleDateString('es-CO',{day:'numeric',month:'long'}); }catch(e){ return ''; } }
  var PG=(function(){
    var KEY='mu-progreso';
    function leer(){ try{ return JSON.parse(localStorage.getItem(KEY))||{}; }catch(e){ return {}; } }
    function guardar(o){ try{ localStorage.setItem(KEY,JSON.stringify(o)); }catch(e){} }
    function avisar(){ try{ document.dispatchEvent(new CustomEvent('mu-repaso')); }catch(e){} }
    function reg(o,id){ o[id]=o[id]||{modos:{},ins:{}}; o[id].modos=o[id].modos||{}; o[id].ins=o[id].ins||{}; return o[id]; }
    return {
      get:function(id){ var r=leer()[id]; return r?{modos:r.modos||{},ins:r.ins||{}}:{modos:{},ins:{}}; },
      modo:function(id,m){ var o=leer(), r=reg(o,id); if(r.modos[m]) return; r.modos[m]=Date.now(); if(r.modos.ver&&r.modos.leer&&r.modos.practicar&&!r.ins.completo) r.ins.completo=Date.now(); guardar(o); avisar(); },
      insignia:function(id,k){ var o=leer(), r=reg(o,id); if(r.ins[k]) return false; r.ins[k]=Date.now(); guardar(o); avisar(); return true; },
      borrar:function(id){ var o=leer(); delete o[id]; guardar(o); avisar(); }
    };
  })();
  window.MU=window.MU||{}; window.MU.progreso=PG;
  var SR=(function(){
    var KEY='mu-repaso', DIAS=[1,3,7,14,30];
    function leer(){ try{ return JSON.parse(localStorage.getItem(KEY))||{}; }catch(e){ return {}; } }
    function guardar(o){ try{ localStorage.setItem(KEY,JSON.stringify(o)); }catch(e){} }
    function avisar(){ try{ document.dispatchEvent(new CustomEvent('mu-repaso')); }catch(e){} }
    return {
      get:function(id){ return leer()[id]||null; },
      registrar:function(id,titulo,calidad){
        var o=leer(), r=o[id]||{titulo:titulo,caja:0,aciertos:0,fallos:0}, now=Date.now(), vencida=!!(o[id]&&o[id].prox<=now);
        if(calidad==='ok'){ r.caja=Math.min(r.caja+1,DIAS.length-1); r.aciertos++; }
        else if(calidad==='ayuda'){ r.aciertos++; }
        else { r.caja=0; r.fallos++; }
        r.titulo=titulo; r.ultimo=now; r.prox=now+DIAS[r.caja]*86400000; r.calidad=calidad; o[id]=r; guardar(o); if(vencida&&calidad!=='fallo') PG.insignia(id,'puntual'); avisar(); return r;
      },
      pendientes:function(){ var o=leer(), now=Date.now(); return Object.keys(o).filter(function(k){ return o[k].prox<=now; }).map(function(k){ return {id:k,titulo:o[k].titulo,prox:o[k].prox}; }); },
      borrar:function(){ try{ localStorage.removeItem(KEY); }catch(e){} avisar(); }
    };
  })();
  window.MU=window.MU||{}; window.MU.repaso=SR;
  /* cuaderno de errores y confianza. Se guardan en localStorage con las claves mu-errores y mu-confianza, para que la página de estudio del sitio los lea */
  var ME=(function(){ var K='mu-errores', KC='mu-confianza';
    function leer(k){ try{ return JSON.parse(localStorage.getItem(k)||'null'); }catch(e){ return null; } }
    function guardar(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
    function clave(s){ var h=0; s=String(s); for(var i=0;i<s.length;i++){ h=(h*31+s.charCodeAt(i))|0; } return (h>>>0).toString(36); }
    function reg(r){ var d=leer(K)||{}, id=L.id+'|'+clave(r.q), e=d[id]||{lid:L.id,lt:L.titulo,curso:L.curso,q:r.q,opts:r.opts||null,correcta:(r.correcta==null?null:r.correcta),respuesta:r.respuesta==null?null:r.respuesta,expl:r.expl||'',fallos:[],n:0,ok:false};
      e.n++; e.ok=false; e.ts=Date.now(); e.fallos.push({i:r.elegida==null?null:r.elegida,resp:r.resp==null?null:r.resp,err:r.err||'',conf:r.conf==null?null:r.conf}); if(e.fallos.length>6) e.fallos=e.fallos.slice(-6); d[id]=e; guardar(K,d); }
    function acierto(q){ var d=leer(K)||{}, id=L.id+'|'+clave(q); if(d[id]){ d[id].ok=true; d[id].tsok=Date.now(); guardar(K,d); } }
    function conf(c,ok){ var d=leer(KC)||{}, k=['a','m','s'][c]+(ok?'_ok':'_no'); d[k]=(d[k]||0)+1; guardar(KC,d); }
    return {registrar:reg,acierto:acierto,confianza:conf,todos:function(){ return leer(K)||{}; }};
  })();
  window.MU.errores=ME;

  /* pregunta de opción múltiple. Con pistas o errores es guiada, deja reintentar y explica cada error. Sin ellos se comporta como siempre */
  function QuizCore(host,cfg){
    var pistas=cfg.pistas||[], guiado=!!(pistas.length||cfg.errores), intentos=0, ayudas=0, done=false, mostradas=0, conf=null;
    host.innerHTML='<div class="q">'+cfg.head+'</div><div class="conf" role="group" aria-label="Qué tan seguro estás"><span>¿Qué tan seguro estás?</span><button type="button" data-c="2" aria-pressed="false">Seguro</button><button type="button" data-c="1" aria-pressed="false">Más o menos</button><button type="button" data-c="0" aria-pressed="false">Adivino</button></div><div class="opts" role="group" aria-label="Opciones de respuesta">'+cfg.opciones.map(function(o,i){ return '<button type="button" data-i="'+i+'"><span class="k">'+'abcdefgh'[i]+'</span><span>'+mtH(o)+'</span></button>'; }).join('')+'</div>'
      +(pistas.length?'<div class="hintbar"><button type="button" class="btn sec sm" data-hint>'+ic('i-bulb')+'<span>Dame una pista</span></button><span class="hc num" data-hc>0 de '+pistas.length+'</span></div><ol class="hints" aria-live="polite"></ol>':'')
      +'<p class="fb" aria-live="polite"></p><div class="giveup" hidden><button type="button" class="btn sec sm" data-show>Mostrar la respuesta</button></div>';
    var fb=host.querySelector('.fb'), hl=host.querySelector('.hints'), hb=host.querySelector('[data-hint]'), hc=host.querySelector('[data-hc]'), gu=host.querySelector('.giveup'), btns=[].slice.call(host.querySelectorAll('.opts button'));
    [].forEach.call(host.querySelectorAll('.conf button'),function(cb){ cb.addEventListener('click',function(){ if(done) return; conf=+cb.getAttribute('data-c'); [].forEach.call(host.querySelectorAll('.conf button'),function(o){ o.setAttribute('aria-pressed',o===cb?'true':'false'); }); }); });
    function calib(ok,aj){ if(conf==null) return ''; ME.confianza(conf,ok); if(conf===2&&!ok) return ' Estabas seguro y fallaste, así que conviene repasar este punto.'; if(conf===0&&ok) return ' Acertaste adivinando. Vale la pena repasarlo para estar seguro.'; return ''; }
    function pista(){ if(mostradas>=pistas.length) return; var li=document.createElement('li'); li.innerHTML=mtH(pistas[mostradas]); hl.appendChild(li); mostradas++; ayudas++; hc.textContent=mostradas+' de '+pistas.length; hb.querySelector('span').textContent=mostradas>=pistas.length?'Sin más pistas':'Otra pista'; if(mostradas>=pistas.length) hb.disabled=true; mathIn(li); }
    function cerrar(rendido){
      done=true; btns.forEach(function(x){ x.disabled=true; if(+x.getAttribute('data-i')===cfg.correcta) x.classList.add('ok'); }); if(hb) hb.disabled=true; gu.hidden=true;
      var calidad=rendido?'fallo':(intentos===0&&ayudas===0?'ok':(intentos<=1?'ayuda':'fallo'));
      if(!rendido){ var rb=host.querySelector('.opts .ok').getBoundingClientRect(), rh=host.getBoundingClientRect(); burst(host,rb.left-rh.left+40,rb.top-rh.top+8); }
      ME.acierto(cfg.head); fb.innerHTML='<b>'+(rendido?'Esta es la respuesta.':'Eso es.')+'</b> '+mtH(cfg.explicacion||'')+((!rendido&&ayudas)?' Usaste '+ayudas+(ayudas===1?' pista.':' pistas.'):'')+calib(!rendido&&intentos===0&&ayudas===0); mathIn(host);
      if(cfg.onDone) cfg.onDone({calidad:calidad,intentos:intentos,ayudas:ayudas});
    }
    btns.forEach(function(b){ b.addEventListener('click',function(){
      if(done) return; var i=+b.getAttribute('data-i'), ok=(i===cfg.correcta);
      if(!guiado){ done=true; btns.forEach(function(x){ x.disabled=true; var xi=+x.getAttribute('data-i'); if(xi===cfg.correcta) x.classList.add('ok'); else if(xi===i) x.classList.add('no'); });
        if(ok){ var r=b.getBoundingClientRect(), h=host.getBoundingClientRect(); burst(host,r.left-h.left+40,r.top-h.top+8); }
        if(ok) ME.acierto(cfg.head); else ME.registrar({q:cfg.head,opts:cfg.opciones,correcta:cfg.correcta,elegida:i,err:'',expl:cfg.explicacion,conf:conf}); fb.innerHTML='<b>'+(ok?'Eso es.':'No era esa.')+'</b> '+mtH(cfg.explicacion||'')+calib(ok); mathIn(host); if(cfg.onDone) cfg.onDone({calidad:ok?'ok':'fallo'}); return; }
      if(ok){ cerrar(false); return; }
      intentos++; b.classList.add('no'); b.disabled=true; ME.registrar({q:cfg.head,opts:cfg.opciones,correcta:cfg.correcta,elegida:i,err:(cfg.errores&&cfg.errores[i])||'',expl:cfg.explicacion,conf:conf});
      fb.innerHTML='<b>No era esa.</b> '+mtH((cfg.errores&&cfg.errores[i])||'Revisa el procedimiento e inténtalo de nuevo.'); mathIn(fb);
      if(mostradas<pistas.length&&mostradas<intentos) pista();
      if(intentos>=2) gu.hidden=false;
    }); });
    if(hb) hb.addEventListener('click',pista);
    gu.querySelector('button').addEventListener('click',function(){ cerrar(true); });
  }
  function Quiz(host){ var Q=L.pregunta; QuizCore(host,{head:(Q.encabezado?mt(Q.encabezado):'Calcula <span data-tex="'+attr(Q.tex)+'"></span>'),opciones:Q.opciones,correcta:Q.correcta,explicacion:Q.explicacion,pistas:Q.pistas,errores:Q.errores,onDone:function(r){ SR.registrar(L.id,L.titulo,r.calidad); if(r.calidad==='ok') PG.insignia(L.id,'sinpistas'); }}); mathIn(host); }

  /* mini simulacro con preguntas del banco. Cada una puede ser de opción múltiple o numérica */
  function Simulacro(root,b){
    var P=b.preguntas, i=0, aciertos=0;
    function numerica(host,q,listo){
      var nid='n'+(++uid);
      host.innerHTML='<div class="q">'+mt(q.texto)+'</div><div class="numrow"><label for="'+nid+'" class="sr">Tu respuesta</label><input id="'+nid+'" class="numin" type="text" inputmode="decimal" autocomplete="off" placeholder="Tu respuesta"><button type="button" class="btn pri sm" data-chk>Comprobar</button></div><p class="fb" aria-live="polite"></p>';
      var inp=host.querySelector('input'), fb=host.querySelector('.fb'), bt=host.querySelector('[data-chk]'), hecho=false;
      function chk(){ if(hecho) return; var v=parseFloat(String(inp.value).replace(',','.')); if(isNaN(v)){ fb.textContent='Escribe un número.'; return; }
        hecho=true; var ok=Math.abs(v-parseFloat(q.respuesta))<=(q.tolNum||0.001); inp.disabled=true; bt.disabled=true;
        if(ok) ME.acierto(mt(q.texto)); else ME.registrar({q:mt(q.texto),opts:null,correcta:null,respuesta:q.respuesta,resp:v,err:'',expl:q.resumen}); fb.innerHTML='<b>'+(ok?'Eso es.':'No era.')+'</b> '+(ok?'':'La respuesta es '+esc(q.respuesta)+'. ')+mt(q.resumen||''); mathIn(host); listo(ok); }
      bt.addEventListener('click',chk); inp.addEventListener('keydown',function(e){ if(e.key==='Enter'){ e.preventDefault(); chk(); } });
    }
    function fin(){
      if(aciertos>=P.length) PG.insignia(L.id,'simulacro'); var calidad=aciertos>=P.length?'ok':(aciertos>=Math.ceil(P.length*2/3)?'ayuda':'fallo'), r=SR.registrar(L.id,L.titulo,calidad);
      var msg=aciertos>=P.length?'Muy bien. Este tema ya lo estás manejando.':(aciertos>=Math.ceil(P.length*2/3)?'Vas bien. Mira la explicación de la que fallaste para no repetir el error.':'Vale la pena volver a los pasos y a las pistas de esta lección. El repaso queda programado.');
      root.innerHTML='<div class="sim-h"><span class="chip soft">Resultado</span></div><p class="sim-score"><span class="num big">'+aciertos+'</span> de '+P.length+' correctas</p><p>'+msg+'</p><p class="mu">Próximo repaso el '+fechaCorta(r.prox)+'.</p><button class="btn sec sm" type="button" data-redo>Intentarlo otra vez</button>';
      root.querySelector('[data-redo]').addEventListener('click',function(){ i=0; aciertos=0; pintar(); });
    }
    function pintar(){
      if(i>=P.length){ fin(); return; }
      var q=P[i];
      root.innerHTML='<div class="sim-h"><span class="chip soft">'+esc(b.titulo||'Mini simulacro')+'</span><span class="num">Pregunta '+(i+1)+' de '+P.length+'</span></div><p class="sim-f">'+esc(q.fuente||'')+'</p><div class="sim-q"></div><div class="sim-n"></div>';
      var host=root.querySelector('.sim-q'), nx=root.querySelector('.sim-n');
      function listo(ok){ if(ok) aciertos++; nx.innerHTML='<button type="button" class="btn pri sm">'+(i+1<P.length?'Siguiente pregunta':'Ver mi resultado')+ic('i-right')+'</button>'; nx.querySelector('button').addEventListener('click',function(){ i++; pintar(); }); }
      if(q.tipo==='numerica') numerica(host,q,listo);
      else QuizCore(host,{head:mt(q.texto),opciones:q.opciones,correcta:q.correcta,explicacion:q.resumen,onDone:function(r){ listo(r.calidad==='ok'); }});
      mathIn(root);
    }
    pintar();
  }

  /* completar un paso: se elige la pieza que falta en la ecuación */
  function Completar(root,b){
    var eq=root.querySelector('[data-eq]'), fb=root.querySelector('.fb'), chips=[].slice.call(root.querySelectorAll('.chip-btn')), fallos=0, hecho=false;
    chips.forEach(function(c){ c.addEventListener('click',function(){
      if(hecho) return; var i=+c.getAttribute('data-i');
      if(i===b.correcta){ hecho=true; chips.forEach(function(x){ x.disabled=true; }); c.classList.add('ok'); eq.removeAttribute('data-done'); eq.setAttribute('data-tex',b.tex.replace('[[hueco]]','\\boxed{'+b.opciones[i].tex+'}')); fb.innerHTML='<b>Eso es.</b> '+(b.porque||''); mathIn(root); if(!RM) burst(root,c.offsetLeft+30,c.offsetTop); }
      else { fallos++; c.classList.add('no'); c.disabled=true; fb.innerHTML='<b>Todavía no.</b> '+((b.errores&&b.errores[i])||'Mira otra vez qué se está derivando en este paso.')+((fallos>=2&&b.pista)?' <i>'+b.pista+'</i>':''); mathIn(fb); }
    }); });
  }

  /* encontrar el error en una solución ya resuelta */
  function Encuentra(root,b){
    var bt=[].slice.call(root.querySelectorAll('.stepbtn')), fb=root.querySelector('.fb'), cor=root.querySelector('.corr'), fallos=0, hecho=false;
    bt.forEach(function(s){ s.addEventListener('click',function(){
      if(hecho) return; var i=+s.getAttribute('data-i');
      if(i===b.mal){ hecho=true; bt.forEach(function(x){ x.disabled=true; }); s.classList.add('bad'); s.setAttribute('aria-pressed','true'); fb.innerHTML='<b>Ahí está el error.</b> '+b.explicacion; cor.hidden=false; mathIn(root); }
      else { fallos++; s.classList.add('good'); s.disabled=true; var p=b.pasos[i].porque; fb.innerHTML='<b>Ese paso está bien.</b> '+(p||'')+((fallos>=2&&b.pista)?' <i>'+b.pista+'</i>':''); mathIn(fb); }
    }); });
  }

  /* ordenar los pasos de un procedimiento, tocando cada paso en el orden que le toca */
  function Ordena(root,b){
    var pool=root.querySelector('.pool'), put=root.querySelector('.put'), fb=root.querySelector('.fb'), rst=root.querySelector('[data-reset]'), n=b.pasos.length, colocados=0, puestos={}, G=b.equiv||[];
    function mismoGrupo(a,c){ for(var i=0;i<G.length;i++){ if(G[i].indexOf(a)>=0&&G[i].indexOf(c)>=0) return true; } return false; }
    function mover(btn){ var k=+btn.getAttribute('data-k');
      if(!puestos[k]&&(k===colocados||mismoGrupo(k,colocados))){ puestos[k]=1; btn.disabled=true; btn.classList.add('ok'); var li=document.createElement('li'); li.innerHTML='<span data-tex="'+attr(b.pasos[k])+'"></span>'; put.appendChild(li); colocados++; mathIn(li);
        if(colocados===n){ fb.innerHTML='<b>Quedó en orden.</b> '+(b.porque||''); } else fb.innerHTML='<b>Bien.</b> Ahora, ¿qué sigue?'; }
      else { btn.classList.remove('no'); void btn.offsetWidth; btn.classList.add('no'); fb.innerHTML='<b>Todavía no.</b> '+(b.pista||'Piensa qué hay que hacer justo después del último paso que pusiste.'); } }
    [].forEach.call(pool.querySelectorAll('.stepbtn'),function(x){ x.addEventListener('click',function(){ mover(x); }); });
    rst.addEventListener('click',function(){ colocados=0; puestos={}; put.innerHTML=''; fb.textContent=''; [].forEach.call(pool.querySelectorAll('.stepbtn'),function(x){ x.disabled=false; x.classList.remove('ok','no'); }); });
  }

  /* tarjeta de repaso espaciado y aviso cuando toca repasar */
  function RepasoCard(el){
    function pintar(){
      var r=SR.get(L.id), pend=SR.pendientes().filter(function(x){ return x.id!==L.id; }), pg=PG.get(L.id), h='<p class="act-t">'+ic('i-clock')+'Tu avance y tu repaso</p>';
      h+='<ul class="avance" aria-label="Modos de estudio que has usado">'+[['ver','Ver'],['leer','Leer'],['practicar','Practicar']].map(function(m){ var on=!!pg.modos[m[0]]; return '<li class="'+(on?'on':'')+'">'+(on?ic('i-check'):'')+m[1]+'<span class="sr">'+(on?', ya lo usaste':', todavía no')+'</span></li>'; }).join('')+'</ul>';
      h+='<ul class="ins-l" aria-label="Insignias de esta lección">'+[['completo','Lo viste todo','Usaste Ver, Leer y Practicar.'],['sinpistas','Sin pistas','Acertaste el quiz al primer intento y sin pistas.'],['simulacro','Simulacro perfecto','Respondiste bien las 3 preguntas del mini simulacro.'],['puntual','Repasaste a tiempo','Volviste a la lección el día que te tocaba.']].filter(function(i){ return i[0]!=='simulacro'||document.querySelector('.card.sim'); }).map(function(i){ var on=!!pg.ins[i[0]]; return '<li class="'+(on?'on':'')+'"><span class="b" aria-hidden="true">'+(on?ic('i-check'):'')+'</span><span><b>'+i[1]+'</b><span class="sr">'+(on?', conseguida':', por conseguir')+'</span><br><span class="mu">'+i[2]+'</span></span></li>'; }).join('')+'</ul>';
      if(!r) h+='<p>Cuando respondas el quiz o el mini simulacro, aquí queda programado cuándo volver a esta lección. Repasar a intervalos, y no todo el mismo día, ayuda a que se te quede.</p>';
      else { var due=r.prox<=Date.now(); h+='<p>'+(due?'Hoy toca repasar esta lección.':'Vuelve a repasar esta lección el <b>'+fechaCorta(r.prox)+'</b>.')+'</p><p class="mu">Registrados en este navegador, '+r.aciertos+' aciertos y '+r.fallos+' fallos.</p>'; }
      if(pend.length) h+='<p>También te toca repasar</p><ul class="rep-l">'+pend.slice(0,4).map(function(x){ return '<li>'+esc(x.titulo)+'</li>'; }).join('')+'</ul>';
      h+='<p class="mu fine2">Aquí no hay rachas ni puntos. Las insignias solo cuentan cómo estudiaste, y todo queda guardado en este navegador.</p>';
      if(r||Object.keys(pg.ins).length) h+='<button class="btn sec sm" type="button" data-borrar>Borrar mi registro</button>';
      el.innerHTML=h; var bb=el.querySelector('[data-borrar]'); if(bb) bb.addEventListener('click',function(){ SR.borrar(); PG.borrar(L.id); });
    }
    pintar(); document.addEventListener('mu-repaso',pintar);
  }
  function avisoRepaso(){
    var r=SR.get(L.id); if(!r||r.prox>Date.now()) return; var h=document.querySelector('.lhead'); if(!h) return;
    var d=document.createElement('div'); d.className='due'; d.setAttribute('role','status'); d.innerHTML=ic('i-clock')+'<span>Hoy toca repasar esta lección. Te conviene empezar por el mini simulacro.</span>';
    h.parentNode.insertBefore(d,h.nextSibling);
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
      case 'completar': { var cid='c'+(++uid); inits.push(function(){ Completar(document.getElementById(cid),b); });
        return '<div class="card act" id="'+cid+'"><p class="act-t">'+ic('i-flask')+'Completa el paso</p><p>'+gl(b.enunciado)+'</p><div class="eq"><span data-tex="'+attr(b.tex.replace('[[hueco]]','\\boxed{\\ ?\\ }'))+'" data-block data-eq></span></div><div class="chips" role="group" aria-label="Opciones para el hueco">'+b.opciones.map(function(o,i){ return '<button type="button" class="chip-btn" data-i="'+i+'" aria-label="'+attr(o.txt||o.tex)+'"><span data-tex="'+attr(o.tex)+'" aria-hidden="true"></span></button>'; }).join('')+'</div><p class="fb" aria-live="polite"></p></div>'; }
      case 'error': { var eid='e'+(++uid); inits.push(function(){ Encuentra(document.getElementById(eid),b); });
        return '<div class="card act" id="'+eid+'"><p class="act-t">'+ic('i-bulb')+'Encuentra el error</p><p>'+gl(b.enunciado)+'</p><div class="steps-l" role="group" aria-label="Pasos de la solución">'+b.pasos.map(function(s,i){ return '<button type="button" class="stepbtn" data-i="'+i+'" aria-label="Paso '+(i+1)+(s.txt?', '+attr(s.txt):'')+'"><span class="n" aria-hidden="true">'+(i+1)+'</span><span class="stx" aria-hidden="true"><span data-tex="'+attr(s.tex)+'"></span></span></button>'; }).join('')+'</div><p class="fb" aria-live="polite"></p><div class="corr" hidden><p class="mu">La corrección</p><div class="eq"><span data-tex="'+attr(b.correccion)+'" data-block></span></div></div></div>'; }
      case 'ordenar': { var oid='o'+(++uid); inits.push(function(){ Ordena(document.getElementById(oid),b); });
        return '<div class="card act" id="'+oid+'"><p class="act-t">'+ic('i-redo')+'Ordena los pasos</p><p>'+gl(b.enunciado)+'</p><p class="mu">Toca los pasos en el orden correcto.</p><div class="pool steps-l" role="group" aria-label="Pasos desordenados">'+b.mezcla.map(function(k){ return '<button type="button" class="stepbtn" data-k="'+k+'" aria-label="'+attr((b.txt&&b.txt[k])||'Paso desordenado')+'"><span class="stx" aria-hidden="true"><span data-tex="'+attr(b.pasos[k])+'"></span></span></button>'; }).join('')+'</div><p class="mu">Tu orden</p><ol class="put"></ol><p class="fb" aria-live="polite"></p><button class="btn sec sm" type="button" data-reset>Empezar de nuevo</button></div>'; }
      case 'simulacro': { var sid2='m'+(++uid); inits.push(function(){ Simulacro(document.getElementById(sid2),b); });
        return '<div class="card sim quiz" id="'+sid2+'"></div>'; }
      case 'ingenieria': return '<div class="card eng"><p class="act-t">'+ic('i-gear')+'¿Para qué sirve? '+esc(b.titulo||'')+'</p><p>'+gl(b.html)+'</p>'+(b.tex?'<div class="eq"><span data-tex="'+attr(b.tex)+'" data-block></span></div>':'')+(b.datos?'<dl class="datos">'+b.datos.map(function(d){ return '<div><dt>'+esc(d.k)+'</dt><dd class="num">'+esc(d.v)+'</dd></div>'; }).join('')+'</dl>':'')+(b.cierre?'<p>'+gl(b.cierre)+'</p>':'')+'</div>';
      case 'repaso': { var rid='r'+(++uid); inits.push(function(){ RepasoCard(document.getElementById(rid)); }); return '<div class="card act repaso" id="'+rid+'"></div>'; }
      case 'ojo': (actions[secId]=actions[secId]||[]).push(function(){ var w=document.querySelector('#'+secId+' .l-warn'); if(w) w.classList.add('pulse'); });
        return '<div class="l-warn"><h2>'+ic('i-bulb')+'Ojo con esto</h2><p>'+gl(b.html)+'</p></div>';
    }
    return '';
  }
  var art=document.getElementById('l-art');
  art.innerHTML=L.leer.secciones.map(function(s,i){ var id='ls-'+(i+1); return '<div class="l-sec" id="'+id+'" data-t="'+attr(s.corto||s.titulo)+'"><h2><span class="num">'+(i+1)+'</span>'+s.titulo+'</h2>'+s.bloques.map(function(b){ return blockHtml(b,id); }).join('')+'</div>'; }).join('')+'<p class="fine">'+document.getElementById('fine').textContent+'</p>';
  [].forEach.call(document.querySelectorAll('#m-leer [data-quiz]'),Quiz); while(inits.length) inits.shift()();
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
  var zNow=0, zTok=0, P=L.practicar.pasos, gP=Graph(document.getElementById('p-g')), cur=0, curD=TVM?(G.a+0.3*(G.b-G.a)):((ARE||PLA)?(G.a+0.3*(G.b-G.a)):(ASI?(G.deslizador.ancla+G.deslizador.dmin*Math.pow(G.deslizador.dmax/G.deslizador.dmin,0.5)):(NEW?0:0.1))), stepsEl=document.getElementById('p-steps');
  stepsEl.innerHTML=P.map(function(s,i){ return '<div class="p-step" data-i="'+i+'"><button class="top" type="button" aria-expanded="false"><span class="num">'+(i+1)+'</span><h2>'+s.titulo+'</h2></button><div class="p-body">'+s.bloques.map(function(b){ return blockHtml(b,'p'+i); }).join('')+'</div></div>'; }).join('');
  [].forEach.call(stepsEl.querySelectorAll('[data-quiz]'),Quiz); while(inits.length) inits.shift()(); avisoRepaso();
  var dS=document.getElementById('p-d'); function dFrom(v){ if(TVM) return G.a+(G.b-G.a)*(0.05+0.9*v/100); if(NEW) return Math.round(v/100*G.pasos); if(ARE||PLA) return G.a+(G.b-G.a)*(0.03+0.94*v/100); if(ASI){ var m=G.deslizador; return m.ancla+m.dmin*Math.pow(m.dmax/m.dmin,v/100); } return Math.pow(10,-3+(100-v)/100*3); }
  function vFrom(d){ if(TVM) return ((d-G.a)/(G.b-G.a)-0.05)/0.9*100; if(NEW) return d/G.pasos*100; if(ARE||PLA) return ((d-G.a)/(G.b-G.a)-0.03)/0.94*100; if(ASI){ var m=G.deslizador; return Math.log((d-m.ancla)/m.dmin)/Math.log(m.dmax/m.dmin)*100; } return 100-(Math.log(d)/Math.LN10+3)/3*100; }
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
    PG.modo(L.id,m);
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
