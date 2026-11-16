var D=DATA,CX=540,CY=840;
var tl=gsap.timeline({paused:true});
var WORLD=document.getElementById('world'),ANN=document.getElementById('ann');
function el(tag,cls,parent,css){var e=document.createElement(tag);if(cls)e.className=cls;if(css)e.style.cssText=css;(parent||ANN).appendChild(e);return e}
var ZF='drop-shadow(0 0 0px rgba(255,150,90,0)) blur(0px)',HF='drop-shadow(0 0 18px rgba(255,150,90,.95)) blur(2.5px)';
function mkEl(layer,g,ox,oy){var e=el('span','g',layer);e.textContent=g.text;
  e.style.fontFamily=g.ff;e.style.fontStyle=g.fst;e.style.fontWeight=g.fw;e.style.fontSize=g.fs+'px';e.style.lineHeight=g.h+'px';e.style.height=g.h+'px';e.style.color=g.color;
  e._fs=g.fs;gsap.set(e,{x:g.x+ox,y:g.y+oy,filter:ZF});return e}
function mkBar(layer,b,ox,oy){var e=el('div','bar',layer);gsap.set(e,{x:b.x+ox,y:b.y+oy,width:b.w,height:b.h});return e}
function lcs(a,b){var n=a.length,m=b.length,d=[],i,j;for(i=0;i<=n;i++)d.push(new Array(m+1).fill(0));
  for(i=n-1;i>=0;i--)for(j=m-1;j>=0;j--)d[i][j]=a[i].k===b[j].k?d[i+1][j+1]+1:Math.max(d[i+1][j],d[i][j+1]);
  var pr=[];i=0;j=0;while(i<n&&j<m){if(a[i].k===b[j].k){pr.push([i,j]);i++;j++}else if(d[i+1][j]>=d[i][j+1])i++;else j++}return pr}
function Seq(id,cx,cy,layerCls){this.d=D[id];this.cx=cx||CX;this.cy=cy||CY;this.layer=el('div','lay '+(layerCls||''),ANN);this.st=this.d.states;
  var me=this;this.off=function(i){return [me.cx-me.st[i].w/2,me.cy-me.st[i].h/2]};
  var o=this.off(0);this.cur=this.st[0].gl.map(function(g){return mkEl(me.layer,g,o[0],o[1])});this.curB=this.st[0].br.map(function(b){return mkBar(me.layer,b,o[0],o[1])});
  this.i=0;gsap.set(this.layer,{opacity:0})}
Seq.prototype.box=function(i,a,b){var o=this.off(i),G=this.st[i].gl.slice(a,b+1),x1=1e9,x2=-1e9,y1=1e9,y2=-1e9;
  G.forEach(function(g){x1=Math.min(x1,g.x);x2=Math.max(x2,g.x+g.w);y1=Math.min(y1,g.y);y2=Math.max(y2,g.y+g.h)});
  return {x:x1+o[0],y:y1+o[1],w:x2-x1,h:y2-y1,r:x2+o[0],b:y2+o[1]}};
Seq.prototype.show=function(t){var all=this.cur.concat(this.curB);
  tl.set(this.layer,{opacity:1},t);
  tl.fromTo(all,{opacity:0,scale:.2,y:'+=70',rotation:-18},{opacity:1,scale:1,y:'-=70',rotation:0,duration:.8,stagger:.035,ease:'back.out(2.2)',immediateRender:false},t);
  return this};
Seq.prototype.go=function(i,T,o){o=o||{};var me=this,A=this.st[i-1],B=this.st[i],oa=this.off(i-1),ob=this.off(i),dur=o.dur||1.15;
  var pr=o.map||lcs(A.gl,B.gl),mA={},mB={};pr.forEach(function(p){mA[p[0]]=p[1];mB[p[1]]=p[0]});
  var nxt=new Array(B.gl.length),rank=0;
  var order=A.gl.map(function(g,k){return k}).sort(function(a,b){return A.gl[a].x-A.gl[b].x});
  order.forEach(function(k,rk){var e=me.cur[k],g=A.gl[k];
    if(mA[k]!==undefined){var gb=B.gl[mA[k]];nxt[mA[k]]=e;var dx=gb.x+ob[0]-(g.x+oa[0]),dy=gb.y+ob[1]-(g.y+oa[1]),dist=Math.sqrt(dx*dx+dy*dy),amp=Math.min(110,dist*.28)*(k%2?-1:1);
      var d0=rk*.022;
      tl.to(e,{scale:1.16,duration:.16,ease:'power2.out'},T-.16+d0);
      tl.to(e,{x:gb.x+ob[0],y:gb.y+ob[1],scale:gb.fs/e._fs,color:gb.color,duration:dur,ease:'power3.inOut'},T+d0);
      if(dist>6){tl.to(e,{marginTop:-amp,duration:dur/2,ease:'sine.out'},T+d0);tl.to(e,{marginTop:0,duration:dur/2,ease:'sine.in'},T+d0+dur/2);
        tl.to(e,{filter:HF,duration:dur/2,ease:'sine.out'},T+d0);tl.to(e,{filter:ZF,duration:dur/2,ease:'sine.in'},T+d0+dur/2)}}
    else if(o.exit){o.exit(e,k,g,oa)}
    else{tl.to(e,{opacity:0,scale:.2,y:'-='+(o.exitDown?-50:50),rotation:(k%2?1:-1)*50,filter:'blur(8px)',duration:.55,ease:'power2.in'},T+rk*.015)}});
  B.gl.forEach(function(g,j){if(mB[j]===undefined){var e=mkEl(me.layer,g,ob[0],ob[1]);gsap.set(e,{opacity:0,scale:.2});nxt[j]=e;
    tl.to(e,{opacity:1,scale:1,duration:.65,ease:'back.out(2.4)'},T+(o.enterAt||.5)+j*.025);
    tl.to(e,{filter:HF,duration:.3,ease:'sine.out'},T+(o.enterAt||.5)+j*.025);tl.to(e,{filter:ZF,duration:.4},T+(o.enterAt||.5)+j*.025+.3)}});
  var nb=[],q;for(q=0;q<this.curB.length;q++){var e2=this.curB[q];
    if(q<B.br.length){var b2=B.br[q];nb[q]=e2;tl.to(e2,{x:b2.x+ob[0],y:b2.y+ob[1],width:b2.w,height:b2.h,duration:dur,ease:'power3.inOut'},T)}else{tl.to(e2,{opacity:0,scaleX:0,duration:.4},T)}}
  for(q=this.curB.length;q<B.br.length;q++){var e3=mkBar(this.layer,B.br[q],ob[0],ob[1]);gsap.set(e3,{opacity:0,scaleX:0});nb[q]=e3;tl.to(e3,{opacity:1,scaleX:1,duration:.6,ease:'power2.out'},T+.45)}
  this.cur=nxt;this.curB=nb;this.i=i;return this};
Seq.prototype.hide=function(t,d){tl.to(this.layer,{opacity:0,duration:d||.5},t);return this};
/* efectos */
function cam(t,fx,fy,s,dur,ease){tl.to(WORLD,{x:(CX-fx)*s,y:(CY-fy)*s,scale:s,duration:dur||1,ease:ease||'power3.inOut'},t)}
function ring(t,x,y,col,R){var r=el('i','ringf',ANN,'left:'+(x-60)+'px;top:'+(y-60)+'px;border-color:'+(col||'#fff'));tl.fromTo(r,{scale:.1,opacity:1},{scale:R||8,opacity:0,duration:.8,ease:'power2.out',immediateRender:false},t);tl.set(r,{opacity:0},0)}
var SEED=7;function rnd(){SEED=(SEED*16807)%2147483647;return (SEED-1)/2147483646}
function burst(t,x,y,n,cols,R){for(var i=0;i<n;i++){var p=el('i','pt',ANN,'left:'+(x-6)+'px;top:'+(y-6)+'px;background:'+cols[i%cols.length]);gsap.set(p,{opacity:0});var a=i/n*6.283+rnd(),r=R*(.4+rnd()*.9);
  tl.fromTo(p,{x:0,y:0,opacity:1,scale:1},{x:Math.cos(a)*r,y:Math.sin(a)*r,opacity:0,scale:.1,duration:.9+rnd()*.4,ease:'power3.out',immediateRender:false},t)}}
function flash(t,col,a){var f=document.getElementById('flash');tl.fromTo(f,{opacity:a||.5,backgroundColor:col||'#fff'},{opacity:0,duration:.35,immediateRender:false},t)}
function shake(t,amp,n){tl.fromTo(WORLD,{rotation:0},{rotation:amp,duration:.045,yoyo:true,repeat:n||9,ease:'none',immediateRender:false},t);tl.set(WORLD,{rotation:0},t+.045*((n||9)+1))}
function stamp(t,x,y,txt,col,fs,hideAt){var s=el('div','stamp',ANN,'left:'+(x-150)+'px;top:'+(y-150)+'px;color:'+col+';font-size:'+(fs||260)+'px');s.textContent=txt;gsap.set(s,{opacity:0});
  tl.fromTo(s,{opacity:0,scale:3.2,rotation:-18},{opacity:1,scale:1,rotation:0,duration:.35,ease:'power4.in',immediateRender:false},t);tl.to(s,{scale:1.12,duration:.12,yoyo:true,repeat:1},t+.35);tl.to(s,{opacity:0,scale:.8,duration:.35},hideAt||t+1.7);return s}
function note(t,x,y,txt,col,anchor,hideAt){var n=el('div','note',ANN,'left:'+x+'px;top:'+y+'px;border-color:'+col+';color:'+col);n.textContent=txt;gsap.set(n,{opacity:0,xPercent:-50});
  tl.fromTo(n,{opacity:0,scale:.4,y:14},{opacity:1,scale:1,y:0,duration:.5,ease:'back.out(2.4)',immediateRender:false},t);if(hideAt)tl.to(n,{opacity:0,duration:.3},hideAt);return n}
function brace(t,x1,x2,y,col,hideAt,up){var h=up?-26:26,w=x2-x1,s=el('svg','svgx',ANN,'left:'+x1+'px;top:'+(y-(up?30:0))+'px;width:'+w+'px;height:40px;overflow:visible');
  s.setAttribute('viewBox','0 0 '+w+' 40');var p=document.createElementNS('http://www.w3.org/2000/svg','path');
  var d=up?'M0 34 Q0 22 '+(w*.15)+' 22 L'+(w*.42)+' 22 Q'+(w*.5)+' 22 '+(w*.5)+' 8 Q'+(w*.5)+' 22 '+(w*.58)+' 22 L'+(w*.85)+' 22 Q'+w+' 22 '+w+' 34':'M0 6 Q0 18 '+(w*.15)+' 18 L'+(w*.42)+' 18 Q'+(w*.5)+' 18 '+(w*.5)+' 32 Q'+(w*.5)+' 18 '+(w*.58)+' 18 L'+(w*.85)+' 18 Q'+w+' 18 '+w+' 6';
  p.setAttribute('d',d);p.setAttribute('fill','none');p.setAttribute('stroke',col);p.setAttribute('stroke-width','6');p.setAttribute('stroke-linecap','round');p.setAttribute('pathLength','1');p.setAttribute('stroke-dasharray','1');p.setAttribute('stroke-dashoffset','1');s.appendChild(p);
  tl.to(p,{strokeDashoffset:0,duration:.7,ease:'power2.inOut'},t);if(hideAt)tl.to(s,{opacity:0,duration:.3},hideAt);return s}
function line(t,x1,y1,x2,y2,col,hideAt,w){var L=Math.hypot(x2-x1,y2-y1),a=Math.atan2(y2-y1,x2-x1)*180/Math.PI;var d=el('div','ln',ANN,'left:'+x1+'px;top:'+(y1-(w||4)/2)+'px;height:'+(w||4)+'px;width:'+L+'px;background:'+col+';transform-origin:0 50%;transform:rotate('+a+'deg) scaleX(0)');
  tl.to(d,{scaleX:1,duration:.5,ease:'power2.inOut'},t);if(hideAt)tl.to(d,{opacity:0,duration:.3},hideAt);return d}
function chips(t,list,cx,y,hideAt){var out=[];list.forEach(function(c,i){var n=el('div','chip',ANN,'left:'+(cx+(i-(list.length-1)/2)*c.sp)+'px;top:'+y+'px;background:'+c.bg+';color:'+c.fg);n.textContent=c.t;gsap.set(n,{opacity:0,xPercent:-50});
  tl.fromTo(n,{opacity:0,scale:0,y:40},{opacity:1,scale:1,y:0,duration:.6,ease:'back.out(2.6)',immediateRender:false},t+i*.18);if(hideAt)tl.to(n,{opacity:0,duration:.3},hideAt);out.push(n)});return out}
function kinetic(id,t,hideAt,x,y,fs,col){var d=document.getElementById(id);d.style.fontSize=fs+'px';var txt=d.getAttribute('data-t');d.innerHTML='';var lines=txt.split('|'),all=[];
  lines.forEach(function(L){var row=el('div','krow',d);L.split('').forEach(function(c){var s=el('span','kc',row);s.innerHTML=c===' '?'&nbsp;':c;all.push(s)})});
  gsap.set(d,{opacity:1});gsap.set(all,{opacity:0});
  tl.fromTo(all,{opacity:0,rotateX:-90,y:60,scale:.6},{opacity:1,rotateX:0,y:0,scale:1,duration:.7,stagger:.035,ease:'back.out(2)',immediateRender:false},t);
  if(hideAt)tl.to(all,{opacity:0,y:-40,duration:.4,stagger:.01},hideAt);return all}
