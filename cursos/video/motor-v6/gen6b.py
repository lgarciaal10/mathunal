import json,re,math,os
FMT=os.environ.get('FMT','9x16')
W,Hh={'9x16':(1080,1920),'16x9':(1920,1080),'3x4':(1080,1440),'4x3':(1440,1080)}[FMT]
H='/tmp/ref/v6/hf'+('' if FMT=='9x16' else '_'+FMT)
CX=W//2
CYf={'9x16':.458,'3x4':.45,'16x9':.42,'4x3':.42}[FMT]
CY=int(Hh*CYf)
SY=int(CY+.2*Hh);NY2=int(CY+.155*Hh);CHY=int(CY+.13*Hh);CTT=int(CY+.24*Hh)
SFS=int(max(200,.15*Hh))
CS=1.1 if Hh>1100 else 1.0;CS2=1.15 if Hh>1100 else 1.0
CAT=int(.78*Hh);CAH=int(.2*Hh) if Hh>1500 else int(.22*Hh);CAW=min(W-120,1500) if W>Hh else W-120;CAL=(W-CAW)//2;CAF=70 if Hh>1100 else 62
TOPY=int(.19*Hh);GS=round(min(W/1080,(CAT-20-TOPY)/920),3);GRX=int((W-1080*GS)/2);GRY=TOPY
KKT=int(.104*Hh);ULL=(W-780)//2;K0T=int(CY-175-.075*Hh);ULT=K0T+345;CTL=(W-500)//2
DATAF='measured_'+FMT+'.json'
WB=json.load(open('wb.json'));FR=open('frases.txt').read().strip().split('\n')
DATA=open(DATAF).read()
OFF=2.8
words=[];i=0;SENT=[]
for si,f in enumerate(FR):
    n=len(f.split());ws=WB[i:i+n];i+=n
    SENT.append((ws[0][1]+OFF,ws[-1][2]+OFF))
    for k,w in enumerate(ws): words.append((si,k,f.split()[k],w[1]+OFF,w[2]+OFF))
DUR=121.34+OFF;FIN=round(DUR+3.4,2)
A=lambda s:SENT[s][0]
def norm(t):return re.sub(r'[^\wáéíóúñü]','',t.lower())
def wf(si,txt,nth=0):
    c=[w for w in words if w[0]==si and norm(w[2])==norm(txt)];return c[nth][3]
bounds=[0,A(1)-.3,A(2)-.3,A(3)-.3,A(5)-.3,A(6)-.3,A(12)-.3,A(13)-.3,A(14)-.3,FIN]
b=bounds
f=lambda x:round(x,2)
js=[]
def J(s):js.append(s)
# --- escenas
J(f"var OFF={OFF};")
J(f"kinetic('k0',{f(OFF+.15)},{f(b[1]-.5)});tl.fromTo('#kk0',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(OFF+.1)});tl.to('#kk0',{{opacity:0,duration:.3}},{f(b[1]-.5)});")
J(f"tl.fromTo('#ul0',{{scaleX:0}},{{scaleX:1,duration:.9,ease:'power3.inOut',immediateRender:false}},{f(wf(0,'letras')+.1)});tl.to('#ul0',{{opacity:0,duration:.3}},{f(b[1]-.5)});")
J(f"var n0=note({f(wf(0,'tranquilo'))},{CX},{SY},'Tranquilo, le pasa a casi todo el mundo','#9AA6CF',0,{f(b[1]-.5)});")
# s1 error
J(f"tl.fromTo('#kk1',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[1]+.2)});tl.to('#kk1',{{opacity:0,duration:.3}},{f(b[2]-.5)});")
J(f"var S1=new Seq('s1',{CX},{CY});S1.show({f(b[1]+.5)});S1.go(1,{f(wf(1,'cancelan'))});S1.go(2,{f(wf(1,'mal')-.5)});")
J(f"stamp({f(wf(1,'mal')+.3)},{CX},{SY},'✗','#FF5C6C',{SFS});flash({f(wf(1,'mal')+.3)},'#FF3B4E',.45);shake({f(wf(1,'mal')+.3)},6,8);S1.hide({f(b[2]-.5)});")
# s2 titulo
J(f"kinetic('k2',{f(b[2]+.25)},{f(b[3]-.45)});")
# s3 numeros
J(f"tl.fromTo('#kk3',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[3]+.2)});tl.to('#kk3',{{opacity:0,duration:.3}},{f(b[4]-.5)});")
J(f"var S3=new Seq('s3',{CX},{CY});S3.show({f(wf(3,'Mira')-.1)});S3.go(1,{f(wf(3,'da')-.3)});stamp({f(wf(3,'tres')+.35)},{CX},{SY},'✓','#3DDC84',{SFS});ring({f(wf(3,'tres')+.35)},{CX},{SY},'#3DDC84',6);S3.hide({f(A(4)-.35)});")
J(f"var S4=new Seq('s4',{CX},{CY});S4.show({f(A(4)+.05)});S4.go(1,{f(wf(4,'cancelas')-.1)});S4.go(2,{f(wf(4,'cuatro')-.3)});S4.go(3,{f(wf(4,'cinco')-.45)});S4.go(4,{f(wf(4,'coincide')-.4)});")
J(f"stamp({f(wf(4,'coincide')+.35)},{CX},{SY},'✗','#FF5C6C',{SFS});flash({f(wf(4,'coincide')+.35)},'#FF3B4E',.4);shake({f(wf(4,'coincide')+.35)},6,8);S4.hide({f(b[4]-.45)});")
# s4 regla
J(f"tl.fromTo('#kk4',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[4]+.2)});tl.to('#kk4',{{opacity:0,duration:.3}},{f(b[5]-.5)});")
J(f"var S5=new Seq('s5',{CX},{CY});S5.show({f(A(5)+.5)});S5.go(1,{f(wf(5,'factores')-.1)});S5.go(2,{f(wf(5,'multiplica')-.3)});S5.go(3,{f(wf(5,'suma')-.5)});")
J(f"var n5=note({f(wf(5,'toca')-.5)},{CX},{NY2},'Lo que se suma no se toca','#FF6B6B',0,{f(b[5]-.5)});ring({f(wf(5,'toca')-.5)},{CX},{CY},'#FF6B6B',7);S5.hide({f(b[5]-.45)});")
# s5 solucion
J(f"tl.fromTo('#kk5',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[5]+.2)});tl.to('#kk5',{{opacity:0,duration:.3}},{f(b[6]-.5)});")
J(f"""var S6=new Seq('s6',{CX},{CY});S6.show({f(wf(6,'fracción')-.4)});
var tNum={f(wf(7,'diferencia'))};
S6.go(1,{f(wf(7,'menos')-.2)});
var bx=S6.box(1,0,9);var bn=brace({f(wf(7,'diferencia')+.2)},bx.x,bx.r,bx.y-8,'#6FB1FF',{f(wf(8,'abajo')-.2)},true);
var nn=note({f(wf(7,'diferencia')+.45)},{CX},bx.y-110,'a² − b² = (a − b)(a + b)','#6FB1FF',0,{f(wf(8,'abajo')-.2)});
cam({f(wf(7,'arriba')-.3)},{CX},{CY-60},{CS},1.0);cam({f(wf(8,'abajo')-.4)},{CX},{CY+100},{CS},1.0);
S6.go(2,{f(wf(8,'Son')-.3)});
var dx=S6.box(1,10,15);
var cc=chips({f(wf(8,'multiplicados')+.5)},[{{t:'−2 · 1 = −2',bg:'#FFD9BF',fg:'#3A1B0A',sp:500}},{{t:'−2 + 1 = −1',bg:'#CFE0FF',fg:'#0B1E44',sp:500}}],{CX},dx.b+150,{f(wf(9,'mira')-.3)});
cam({f(wf(9,'mira')-.2)},{CX},{CY},1.0,.9);
S6.go(3,{f(wf(9,'mismo')-.2)});
var b1=S6.box(3,0,4),b2=S6.box(3,10,14);
line({f(wf(9,'mismo')+.1)},(b1.x+b1.r)/2,b1.b+4,(b2.x+b2.r)/2,b2.y-4,'#FF6B6B',{f(wf(10,'sí')-.3)},5);
var Tc={f(wf(10,'cancelar')-.2)};var bar3=S6.st[3].br[0],bo=S6.off(3),barY=bar3.y+bo[1];
S6.go(4,Tc+.95,{{map:[[6,0],[7,1],[8,2],[16,3],[17,4],[18,5]],dur:1.0,enterAt:.3,exit:function(e,k,g,oa){{
  var col=(k<=4||(k>=10&&k<=14));
  if(col){{var up=k<=4;tl.to(e,{{scale:1.3,color:'#FF6B6B',duration:.2,ease:'power2.out'}},Tc-.1);
   tl.to(e,{{x:{CX}-18+(k%5)*8-60,y:barY+(up?-26:-26)+(up?-14:14),rotation:(k%2?1:-1)*540,scale:.55,duration:.9,ease:'power3.in'}},Tc+.05);
   tl.set(e,{{opacity:0}},Tc+.96);}}
  else{{tl.to(e,{{opacity:0,scale:.2,duration:.4}},Tc+.5)}}}}}});
ring(Tc+.96,{CX},barY,'#fff',9);ring(Tc+1.06,{CX},barY,'#FF8A4C',6);burst(Tc+.96,{CX},barY,36,['#FF8A4C','#FFD166','#fff','#6FB1FF'],260);flash(Tc+.96,'#fff',.8);shake(Tc+.96,5,10);
cam(Tc-.2,{CX},barY,{CS2},1.1,'power2.in');cam(Tc+1.0,{CX},{CY},1.0,1.0);
var rb=S6.box(4,0,5);tl.to({{}},{{duration:.01}},{f(wf(11,'queda'))});
ring({f(wf(11,'queda'))},{CX},{CY},'#FFB48A',7);
S6.hide({f(b[6]-.45)});""")
# s6 dominio
J(f"tl.fromTo('#kk6',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[6]+.2)});tl.to('#kk6',{{opacity:0,duration:.3}},{f(b[7]-.5)});")
J(f"var SD=new Seq('sd',{CX},{CY-60});SD.show({f(A(12)+.3)});chips({f(wf(12,'valer')-.2)},[{{t:'x ≠ 2',bg:'#FF8A4C',fg:'#2A1203',sp:380}},{{t:'x ≠ −1',bg:'#6FB1FF',fg:'#06214A',sp:380}}],{CX},{CHY},{f(b[7]-.5)});ring({f(wf(12,'valer')-.1)},{CX},{CHY+30},'#FF8A4C',8);SD.hide({f(b[7]-.45)});")
# s7 grafica
J(f"""var GR=el('div','gr',ANN,'left:{GRX}px;top:{GRY}px;width:1080px;height:920px;transform-origin:0 0;transform:scale({GS})');gsap.set(GR,{{opacity:0}});
function XS(x){{return 70+(x+3)/9*940}};function YS(y){{return 860-(y+3)/9*800}};function F(x){{return (x+2)/(x+1)}};
var gs='<svg width="1080" height="920" viewBox="0 0 1080 920" style="position:absolute;left:0;top:0;overflow:visible"><g stroke="rgba(255,255,255,.12)" stroke-width="2">';
for(var v=-3;v<=6;v++){{if(v!==0)gs+='<path d="M'+XS(v)+' 20V880M70 '+YS(v)+'H1010"/>'}}
gs+='</g><path d="M'+XS(0)+' 20V880M70 '+YS(0)+'H1010" stroke="#EEF2FF" stroke-width="4" fill="none"/><path id="asin" d="M'+XS(-1)+' 20V880" stroke="#FF8A4C" stroke-width="3" stroke-dasharray="14 10" fill="none" opacity="0"/>';
function br(a,b2){{var s='',n=100;for(var k=0;k<=n;k++){{var x=a+(b2-a)*k/n,y=Math.max(-3,Math.min(6,F(x)));s+=(k?'L':'M')+XS(x).toFixed(1)+' '+YS(y).toFixed(1)}}return s}}
['{{a:-3,b:-1.12}}','{{a:-0.9,b:1.93}}','{{a:2.07,b:6}}'].forEach(function(o,ii){{o=eval('('+o+')');gs+='<path class="cvv" d="'+br(o.a,o.b)+'" stroke="#6FB1FF" stroke-width="12" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" style="filter:drop-shadow(0 0 12px rgba(111,177,255,.7))"/>'}});
gs+='<line id="dl" x1="0" y1="0" x2="0" y2="0" stroke="#FFB48A" stroke-width="3" stroke-dasharray="6 6" opacity="0"/><circle id="dot" r="16" cx="0" cy="0" fill="#FFB48A" opacity="0" style="filter:drop-shadow(0 0 16px #FF8A4C)"/><circle id="hole" cx="'+XS(2)+'" cy="'+YS(F(2))+'" r="20" fill="#070B18" stroke="#FF8A4C" stroke-width="7" opacity="0"/></svg>';
GR.innerHTML=gs;
var gt={f(b[7]+.5)};
tl.fromTo('#kk7',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f(b[7]+.2)});tl.to('#kk7',{{opacity:0,duration:.3}},{f(b[8]-.5)});
tl.set(GR,{{opacity:1}},gt-.2);tl.to('#asin',{{opacity:.8,duration:.6}},gt);
document.querySelectorAll('.cvv').forEach(function(p,ii){{tl.to(p,{{strokeDashoffset:0,duration:.9,ease:'power1.inOut'}},gt+ii*.7)}});
var st={{x:-.5}};tl.fromTo('#dot',{{opacity:0}},{{opacity:1,duration:.4,immediateRender:false}},gt+2.4);
tl.fromTo(st,{{x:-.5}},{{x:4.5,duration:3.4,ease:'power1.inOut',immediateRender:false,onUpdate:function(){{var x=st.x,y=F(x),hid=Math.abs(x-2)<.09;var d=document.getElementById('dot');d.setAttribute('cx',XS(x));d.setAttribute('cy',YS(y));d.style.opacity=hid?0:1;var l=document.getElementById('dl');l.setAttribute('x1',XS(x));l.setAttribute('x2',XS(x));l.setAttribute('y1',YS(0));l.setAttribute('y2',YS(y));l.style.opacity=hid?0:.8}}}},gt+2.4);
tl.fromTo('#hole',{{opacity:0,scale:.2,transformOrigin:'50% 50%'}},{{opacity:1,scale:1,duration:.5,ease:'back.out(2.5)',immediateRender:false}},{f(wf(13,'huequito'))});
ring({f(wf(13,'huequito'))},{GRX}+XS(2)*{GS},{GRY}+YS(F(2))*{GS},'#FF8A4C',6);
tl.to(GR,{{opacity:0,duration:.4}},{f(b[8]-.5)});""")
# s8 cierre
J(f"kinetic('k8',{f(b[8]+.25)},{f(FIN)});var sb=note({f(A(15)-.1)},{CX},{SY},'Practica con preguntas reales de parciales','#FFFFFF',0);")
J(f"var ct=document.getElementById('cta');tl.fromTo(ct,{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.7,ease:'elastic.out(1,.5)',immediateRender:false}},{f(A(15)+1.6)});ring({f(A(15)+1.6)},{CX},{CTT+60},'#FF8A4C',8);burst({f(A(15)+1.6)},{CX},{CTT+60},44,['#FF8A4C','#FFD166','#3DDC84','#6FB1FF','#fff'],420);flash({f(A(15)+1.6)},'#fff',.35);")
# --- capitulos HUD y camara de fondo
for k,t in enumerate([b[1],b[3],b[5],b[6],b[8]]):
    J(f"tl.to('#pl{k}',{{backgroundColor:'#FF8A4C',duration:.4}},{f(t)});tl.call(function(){{document.getElementById('hudl').textContent={json.dumps(['El error','La prueba','El método','Dominio y gráfica','Cierre'][k])}}},null,{f(t)});")
# --- subtitulos
chunks=[]
for si,f_ in enumerate(FR):
    ws=[w for w in words if w[0]==si];cur=[]
    for w in ws:
        cur.append(w)
        if (len(cur)>=4 and re.search(r'[.,]$',w[2])) or len(cur)>=6: chunks.append(cur);cur=[]
    if cur:
        if chunks and len(cur)<=2 and chunks[-1][0][0]==si: chunks[-1]+=cur
        else: chunks.append(cur)
caps='';wid=0
for ci,ch in enumerate(chunks):
    a=ch[0][3];nxt=chunks[ci+1][0][3] if ci+1<len(chunks) else FIN
    bb=nxt if nxt-ch[-1][4]<.9 else ch[-1][4]+.3
    spans=''
    for w in ch:
        spans+=f'<span class="w" id="w{wid}">{w[2]}</span> ';J(f'tl.to("#w{wid}",{{backgroundColor:"#FF8A4C",color:"#0A0F1F",scale:1.06,duration:.1}},{f(w[3])});tl.to("#w{wid}",{{backgroundColor:"rgba(255,138,76,0)",color:"#F4F6FF",scale:1,duration:.2}},{f(w[4])});');wid+=1
    caps+=f'<div id="cap{ci}" class="clip capc" data-start="{f(a)}" data-duration="{f(bb-a)}" data-track-index="{3+ci%2}"><div class="cap">{spans}</div></div>'
# particulas fondo
PT=''.join(f'<div class="pt2" id="pt{i}" style="left:{(i*173)%(W-80)}px;top:{(i*311)%(Hh-120)+60}px;font-size:{40+(i%4)*18}px;opacity:{.05+(i%3)*.03}">{["+","−","×","÷","=","x²","√","π","∫","Σ"][i%10]}</div>' for i in range(26))
for i in range(26): J(f'tl.to("#pt{i}",{{y:{-80-(i%5)*50},x:{(i%7-3)*26},rotation:{(i%5-2)*14},duration:{FIN},ease:"none"}},0);')
J(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{FIN},ease:"none"}},0);tl.fromTo("#cam",{{scale:1}},{{scale:1.035,duration:{FIN},ease:"none"}},0);')
J(f'tl.fromTo("#lg",{{opacity:0,scale:.82,letterSpacing:"26px"}},{{opacity:1,scale:1,letterSpacing:"2px",duration:1.0,ease:"power3.out",immediateRender:false}},.25);tl.to("#lgl",{{width:520,duration:.8,ease:"power2.inOut"}},.75);tl.fromTo("#lgs",{{opacity:0,y:14}},{{opacity:1,y:0,duration:.7,immediateRender:false}},1.05);tl.to("#intro",{{opacity:0,duration:.6,ease:"power1.in"}},{f(OFF-.55)});tl.set("#intro",{{display:"none"}},{f(OFF+.1)});')
css=open('style6t.css').read()
for k,v in {'%W%':W,'%H%':Hh,'%CX%':CX,'%CY%':CY,'%KKT%':KKT,'%ULL%':ULL,'%ULT%':ULT,'%CTL%':CTL,'%CTT%':CTT,'%CAL%':CAL,'%CAT%':CAT,'%CAW%':CAW,'%CAH%':CAH,'%CAW2%':CAW-40,'%CAF%':CAF}.items(): css=css.replace(k,str(v))
engine=open('engine6.js').read().replace('CX=540,CY=840','CX=%d,CY=%d'%(CX,CY))
html=f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8"/><meta name="viewport" content="width={W}, height={Hh}"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/katex.css"/>
<style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{FIN}" data-width="{W}" data-height="{Hh}">
<audio id="voz" src="assets/mix.mp3" data-start="0" data-duration="{FIN}" data-track-index="0"></audio>
<div id="bg"></div><div id="dots"></div><div class="blob" id="b1"></div><div class="blob" id="b2"></div><div class="blob" id="b3"></div>{PT}
<div id="cam"><div id="world"><div id="ann">
<div class="kin" id="k0" data-t="Fracciones|con letras" style="top:{K0T}px"></div><div class="ul" id="ul0"></div>

<div class="kin" id="k2" data-t="Probemos|con números" style="top:{K0T+140}px"></div>

<div class="kin" id="k8" data-t="Lo hiciste|muy bien" style="top:{K0T+40}px"></div><div id="cta">mathunal.com</div>
</div></div></div>
<div class="kk" id="kk0">Matemáticas Básicas</div><div class="kk" id="kk1">Lo que casi todos hacen</div><div class="kk" id="kk3">Con números</div><div class="kk" id="kk4">La regla</div><div class="kk" id="kk5">Paso a paso</div><div class="kk" id="kk6">Antes de cancelar</div><div class="kk" id="kk7">Así se ve la fracción</div>
<div class="brand">MATH<b>UNAL</b></div><div id="hud">{''.join(f'<div class="pill" id="pl{i}"></div>' for i in range(5))}</div><div id="hudl">Simplificar fracciones</div>
{caps}
<div id="flash"></div><div id="bar"></div><div id="vig"></div><div id="grain"></div>
<div id="intro"><div id="lg">MATH<b>UNAL</b></div><div id="lgl"></div><div id="lgs">Matemáticas paso a paso</div></div>
<script>window.__timelines=window.__timelines||{{}};
var DATA={DATA};var STFS={SFS};
{engine}
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);</script></div></body></html>'''
open(H+'/index.html','w').write(html)

print('ok',len(html),FIN)
sf={'off':OFF,'fin':FIN,'bounds':bounds,
 'go':[wf(1,'cancelan')-.1,wf(1,'mal')-.5,wf(3,'da')-.3,wf(4,'cancelas')-.1,wf(4,'cuatro')-.3,wf(4,'cinco')-.45,wf(4,'coincide')-.4,wf(5,'factores')-.1,wf(5,'multiplica')-.3,wf(5,'suma')-.5,wf(7,'menos')-.2,wf(8,'Son')-.3,wf(9,'mismo')-.2],
 'chips':[wf(8,'multiplicados')+.5,wf(8,'multiplicados')+.68,wf(12,'valer')-.2,wf(12,'valer')-.02],
 'check':[wf(3,'tres')+.35],'bad':[wf(1,'mal')+.3,wf(4,'coincide')+.35],
 'boom':[wf(10,'cancelar')-.2+.96],'res':[wf(11,'queda')],'cta':[A(15)+1.6],'hole':[wf(13,'huequito')],'big':[],
 'riser':[wf(10,'cancelar')-.2+.05]}
json.dump(sf,open('sfx6.json','w'))
