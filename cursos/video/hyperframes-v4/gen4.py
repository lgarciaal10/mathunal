import json, re, math
H = '/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/hf/reel4'
K = json.load(open('/tmp/ref/v4/kx.json'))
for _k in K:
    for _a,_b in (('#D94A4A','#FF6B6B'),('#1E9E5A','#3DDC84'),('#E8632A','#FF8A4C'),('#2F6FED','#6FB1FF')): K[_k]=K[_k].replace(_a,_b)
WB = json.load(open('/tmp/ref/v4/wb.json'))
FR = open('/tmp/ref/v4/frases.txt').read().strip().split('\n')
# ---- tiempos por frase y palabra
words = []  # (sent, k, text, a, b)
i = 0
SENT = []
for si, f in enumerate(FR):
    n = len(f.split())
    ws = WB[i:i + n]; i += n
    SENT.append((ws[0][1], ws[-1][2]))
    for k, w in enumerate(ws):
        words.append((si, k, f.split()[k], w[1], w[2]))
OFF = 2.8
words = [(a,b,c,d+OFF,e+OFF) for (a,b,c,d,e) in words]
SENT = [(a+OFF,b+OFF) for a,b in SENT]
DUR = 121.34 + OFF
FIN = round(DUR + 3.4, 2)
A = lambda s: SENT[s][0]
B = lambda s: SENT[s][1]
def norm(t): return re.sub(r'[^\wáéíóúñü]', '', t.lower())
def wf(si, txt, nth=0):
    c = [w for w in words if w[0] == si and norm(w[2]) == norm(txt)]
    return c[nth][3]

INK, ORG, BLU, GRN, RED = '#EEF2FF', '#FF8A4C', '#6FB1FF', '#3DDC84', '#FF6B6B'
js = []
def J(o): return json.dumps(o)
PRE = []
def FT(sel, frm, to, t, dur=.7, ease='power2.out'):
    if frm.get('opacity') == 0 and sel not in PRE: PRE.append(sel)
    to = dict(to); to.update(duration=dur, ease=ease, immediateRender=False)
    js.append(f'tl.fromTo("{sel}",{J(frm)},{J(to)},{t:.2f});')
def TO(sel, to, t, dur=.5, ease='power2.out'):
    to = dict(to); to.update(duration=dur, ease=ease)
    js.append(f'tl.to("{sel}",{J(to)},{t:.2f});')
def IN(sel, t, dur=.8, y=26, sc=None):
    f = {'opacity': 0, 'y': y}
    to = {'opacity': 1, 'y': 0}
    if sc: f['scale'] = sc; to['scale'] = 1
    FT(sel, f, to, t, dur)
def POP(sel, t, dur=.6):  # solo para pegatinas pequenas
    FT(sel, {'opacity': 0, 'scale': .6}, {'opacity': 1, 'scale': 1}, t, dur, 'back.out(1.4)')

def clip(id, a, b, inner, cls='', style='', track=1):
    return f'<div id="{id}" class="clip {cls}" data-start="{a:.2f}" data-duration="{b-a:.2f}" data-track-index="{track}" style="{style}">{inner}</div>'

# ---- limites de escena
bounds = [0, A(1) - .3, A(2) - .3, A(3) - .3, A(5) - .3, A(6) - .3, A(12) - .3, A(13) - .3, A(14) - .3, FIN]
# s0 s1 s2 s3(3-4) s4(5) s5(6-11) s6(12) s7(13) s8(14-15)
sc = []
def scene(n, inner):
    sc.append(clip(f's{n}', bounds[n], bounds[n + 1], f'<div class="in" id="i{n}" style="top:{ {0:210,1:170,2:230,3:140,4:140,5:20,6:230,7:70,8:190}[n] }px">{inner}</div>'))

E = lambda k, size, extra='': f'<div class="eq" style="font-size:{size}px;{extra}">{K[k]}</div>'

# ----- s0
scene(0, f'''<div class="kick" id="k0">Matemáticas Básicas</div>
<div class="h1" id="t0">Fracciones<br>con <span class="mk">letras</span></div>
<svg id="ul0" width="760" height="40" viewBox="0 0 760 40" style="position:absolute;left:100px;top:530px"><path d="M6 24 C150 6 330 38 520 16 S700 22 752 12" stroke="{ORG}" stroke-width="10" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>
<div class="note" id="n0">Tranquilo, le pasa a casi todo el mundo</div>''')
# ----- s1
scene(1, f'''<div class="kick" id="k1">Lo que casi todos hacen</div>
<div class="stack" id="st1"><div id="a1" style="position:relative">{E('h1', 120)}</div>
<div id="a2" class="eq2">{E('h2', 120)}</div></div><div class="bigx" id="x1">✗</div>''')
# ----- s2
scene(2, f'''<svg id="lupa" width="240" height="240" viewBox="0 0 240 240"><circle cx="100" cy="100" r="62" fill="#FFF6D8" stroke="{INK}" stroke-width="14"/><path d="M148 148 L212 212" stroke="{INK}" stroke-width="22" stroke-linecap="round"/><path d="M70 92 Q100 60 132 88" stroke="{ORG}" stroke-width="9" fill="none" stroke-linecap="round"/></svg>
<div class="h2" id="t2">Probemos con <span class="mk">números</span></div>''')
# ----- s3
scene(3, f'''<div class="row3" id="r1"><div class="kick l">Con números</div><div class="line">{E('n1', 80)}<div id="n1b" class="eq" style="font-size:80px">{K['n1b']}</div></div><div class="ck" id="c1">✓</div></div>
<div class="row3" id="r2"><div class="kick l" style="color:{RED}">Cancelando el 2</div><div class="line">{E('n2', 80)}<div id="n2b" class="eq" style="font-size:80px">{K['n2b']}</div></div><div class="ck bad" id="c2">✗</div></div>
<div class="verd" id="vd">{E('neq', 130)}<div class="sub">No coincide</div></div>''')
# ----- s4
scene(4, f'''<div class="h2" id="t4">La regla</div>
<div class="card okc" id="rk1"><div class="lab" style="color:{GRN}">Se multiplica, sí se cancela</div>{E('ok', 86)}</div>
<div class="card badc" id="rk2"><div class="lab" style="color:{RED}">Se suma, no se toca</div>{E('mal', 86)}</div>''')
# ----- s5 solucion
sol = f'''<div id="fr" class="eq" style="position:absolute;left:0;width:960px;top:40px;font-size:130px;transform-origin:50% 0">{K['frac']}</div>
<div id="l1" class="blk" style="top:225px"><div class="tag" style="color:{BLU}">Arriba</div><div class="helper" id="hp">{K['dif']}</div><div class="row"><span>{K['num']}</span><span id="p1">{K['d1']}</span><span id="p2">{K['d2']}</span></div></div>
<div id="l2" class="blk" style="top:395px"><div class="tag" style="color:{BLU}">Abajo, multiplican −2 y suman −1</div><div class="chips"><span class="chip" id="c1b" style="background:#FFD9BF">−2</span><span class="chip" id="c2b" style="background:#CFE0FF">+1</span></div><div class="row"><span>{K['den']}</span><span id="p3">{K['d3']}</span><span id="p4">{K['d4']}</span></div></div>
<div id="big" style="position:absolute;top:560px;left:0;width:960px;display:flex;justify-content:center"><div style="position:relative"><div id="f1" class="eq" style="font-size:92px">{K['f1']}</div><div id="f2" class="eq" style="position:absolute;inset:0;font-size:92px;opacity:0">{K['f2']}</div><div id="glow" style="position:absolute;inset:-18px;border-radius:30px;border:6px solid {ORG};opacity:0"></div></div></div>
<div id="resb" style="position:absolute;top:835px;left:0;width:960px;display:flex;justify-content:center"><div class="resbox"><span class="eq" style="font-size:72px">{K['res']}</span></div></div>'''
scene(5, sol)
# ----- s6 dominio
scene(6, f'''<div class="h2" id="t6">Antes de cancelar<br>anota el <span class="mk">dominio</span></div>
<div class="dom" id="d1"><b>x ≠ 2</b><i>se anula el factor x − 2</i></div>
<div class="dom" id="d2"><b>x ≠ −1</b><i>se anula el factor x + 1</i></div>''')
# ----- s7 grafica
def X(x): return 50 + (x + 3) / 9 * 800
def Y(y): return 820 - (y + 3) / 9 * 780
f = lambda x: (x + 2) / (x + 1)
def br(a, b, n=90):
    return ' '.join(('M' if k == 0 else 'L') + f'{X(a+(b-a)*k/n):.1f} {Y(max(-3,min(6,f(a+(b-a)*k/n)))):.1f}' for k in range(n + 1))
paths = [br(-3, -1.12), br(-0.9, 1.93), br(2.07, 6)]
curv = ''.join(f'<path class="cv" d="{p}" stroke="{BLU}" stroke-width="9" fill="none" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>' for p in paths)
gsvg = f'''<svg width="900" height="860" viewBox="0 0 900 860" style="position:absolute;left:30px;top:90px"><g stroke="#C9CFDF" stroke-width="2">{''.join(f'<path d="M{X(v)} 10 V840"/><path d="M30 {Y(v)} H880"/>' for v in range(-3,7) if v!=0)}</g><path d="M{X(0)} 10 V840 M30 {Y(0)} H880" stroke="{INK}" stroke-width="3.5" fill="none" opacity=".75"/><path id="asin" d="M{X(-1)} 10 V840" stroke="{RED}" stroke-width="4" stroke-dasharray="14 12" fill="none" opacity="0"/>{curv}<g id="dotg" opacity="0"><line id="dl" x1="0" y1="{Y(0)}" x2="0" y2="0" stroke="{GRN}" stroke-width="4" stroke-dasharray="8 8"/><circle id="dot" r="17" fill="{GRN}" cx="0" cy="0"/></g><circle id="hole" cx="{X(2)}" cy="{Y(f(2))}" r="21" fill="#FFFFFF" stroke="{ORG}" stroke-width="8" opacity="0"/><text id="htx" x="{X(2)+34}" y="{Y(f(2))-58}" fill="{ORG}" font-family="IBM Plex Mono,monospace" font-size="38" font-weight="700" opacity="0">hueco en x = 2</text></svg>'''
scene(7, f'<div class="kick" id="k7">Así se ve la fracción</div>{gsvg}')
# ----- s8
scene(8, f'''<div class="h2" id="t8" style="top:200px">Lo hiciste<br><span class="mk">muy bien</span></div>
<div class="h3" id="t8b">Practica con preguntas reales de parciales</div>
<div class="cta" id="cta">mathunal.com</div>''')

# ---- subtitulos en burbuja: trozos de <=6 palabras cortando en puntuacion
chunks = []
for si, f_ in enumerate(FR):
    ws = [w for w in words if w[0] == si]
    cur = []
    for w in ws:
        cur.append(w)
        if (len(cur) >= 4 and re.search(r'[.,]$', w[2])) or len(cur) >= 6:
            chunks.append(cur); cur = []
    if cur:
        if chunks and len(cur) <= 2 and chunks[-1][0][0] == si: chunks[-1] += cur
        else: chunks.append(cur)
caps = []; wid = 0; wjs = []
for ci, ch in enumerate(chunks):
    a = ch[0][3]
    nxt = chunks[ci + 1][0][3] if ci + 1 < len(chunks) else FIN
    b = nxt if nxt - ch[-1][4] < .9 else ch[-1][4] + .3
    spans = ''
    for w in ch:
        spans += f'<span class="w" id="w{wid}">{w[2]}</span> '
        wjs.append((wid, w[3], w[4])); wid += 1
    caps.append(clip(f'cap{ci}', a, b, f'<div class="cap">{spans}</div>', 'capc', '', 3 + ci % 2))

# ---- animaciones de escena
def sceneio(n):
    t0, t1 = bounds[n], bounds[n + 1]
    FT(f'#i{n}', {'opacity': 0, 'y': 24}, {'opacity': 1, 'y': 0}, t0 + .25, .7)
    if n < 8: TO(f'#i{n}', {'opacity': 0, 'y': -16}, t1 - .55, .4, 'power1.in')
for n in range(9): sceneio(n)
# wipes
for n in range(1, 9):
    t = bounds[n]
    js.append(f'tl.fromTo("#wipe",{{x:-1400}},{{x:1000,duration:.9,ease:"power2.inOut",immediateRender:false}},{t-.45:.2f});')
# s0
IN('#k0', OFF+.1, .7); IN('#t0', OFF+.3, 1.0)
js.append(f'tl.to("#ul0 path",{{strokeDashoffset:0,duration:1.0,ease:"power2.inOut"}},{wf(0,"letras")+.2:.2f});')
IN('#n0', wf(0, 'tranquilo'), .8)
# s1
IN('#k1', bounds[1] + .5, .7)
IN('#a1', bounds[1] + .8, .8)
FT('#a2', {'opacity': 0, 'y': 20}, {'opacity': 1, 'y': 0}, wf(1, 'cancelan'), .8)
FT('#x1', {'opacity': 0, 'scale': 2}, {'opacity': 1, 'scale': 1}, wf(1, 'mal'), .55, 'power3.out')
# s2
FT('#lupa', {'opacity': 0, 'scale': .7, 'rotation': -14}, {'opacity': 1, 'scale': 1, 'rotation': 0}, bounds[2] + .4, 1.0, 'back.out(1.3)')
IN('#t2', bounds[2] + .9, .8)
# s3
IN('#r1', wf(3, 'cuatro'), .8)
FT('#n1b', {'opacity': 0, 'x': -14}, {'opacity': 1, 'x': 0}, wf(3, 'da'), .7)
POP('#c1', wf(3, 'tres') + .3)
IN('#r2', wf(4, 'cancelas'), .8)
FT('#n2b', {'opacity': 0, 'x': -14}, {'opacity': 1, 'x': 0}, wf(4, 'cuatro'), .7)
POP('#c2', wf(4, 'cinco') + .35)
IN('#vd', wf(4, 'coincide') - .2, .8)
# s4
IN('#t4', bounds[4] + .5, .7)
IN('#rk1', wf(5, 'factores') - .3, .8, 26, .94)
IN('#rk2', wf(5, 'suma') - .6, .8, 26, .94)
# s5
IN('#fr', wf(6, 'fracción') - .2, 1.0, 20, .8)
TO('#fr', {'y': -20, 'scale': .5}, A(7) + .1, 1.0, 'power2.inOut')
IN('#l1', wf(7, 'arriba'), .8)
FT('#hp', {'opacity': 0}, {'opacity': 1}, wf(7, 'diferencia'), .8)
FT('#p1', {'opacity': 0, 'y': 14}, {'opacity': 1, 'y': 0}, wf(7, 'menos'), .6)
FT('#p2', {'opacity': 0, 'y': 14}, {'opacity': 1, 'y': 0}, wf(7, 'más'), .6)
IN('#l2', wf(8, 'abajo'), .8)
POP('#c1b', wf(8, 'multiplicados') + .6); POP('#c2b', wf(8, 'sumados') + .6)
FT('#p3', {'opacity': 0, 'y': 14}, {'opacity': 1, 'y': 0}, wf(8, 'Son'), .6)
FT('#p4', {'opacity': 0, 'y': 14}, {'opacity': 1, 'y': 0}, wf(8, 'uno', 1), .6)
IN('#big', A(9) + .2, .9)
js.append(f'tl.fromTo("#glow",{{opacity:0}},{{opacity:1,duration:.5,repeat:3,yoyo:true,ease:"sine.inOut",immediateRender:false}},{wf(9,"mismo"):.2f});tl.set("#glow",{{opacity:0}},{A(10):.2f});')
TO('#f1', {'opacity': 0}, wf(10, 'cancelar'), .8); TO('#f2', {'opacity': 1}, wf(10, 'cancelar'), .8)
FT('#resb .resbox', {'opacity': 0, 'y': 24, 'scale': .9}, {'opacity': 1, 'y': 0, 'scale': 1}, wf(11, 'queda'), .9)
# s6
IN('#t6', bounds[6] + .5, .8)
IN('#d1', wf(12, 'valer'), .8, 20, .94)
IN('#d2', wf(12, 'menos'), .8, 20, .94)
# s7
IN('#k7', bounds[7] + .5, .7)
a8 = bounds[7] + 1.0
FT('#asin', {'opacity': 0}, {'opacity': .8}, a8, .6)
js.append(f'document.querySelectorAll(".cv").forEach((p,i)=>tl.to(p,{{strokeDashoffset:0,duration:.9,ease:"power1.inOut"}},{a8:.2f}+i*.7));')
dstart = a8 + 2.4
js.append(f'''const XS=(x)=>{50}+(x+3)/9*800, YS=(y)=>{820}-(y+3)/9*780, F=(x)=>(x+2)/(x+1);
const st={{x:-0.5}};tl.fromTo("#dotg",{{opacity:0}},{{opacity:1,duration:.4,immediateRender:false}},{dstart:.2f});
tl.to(st,{{x:4.5,duration:3.4,ease:"power1.inOut",onUpdate:()=>{{const x=st.x,y=F(x);const hid=Math.abs(x-2)<0.09;gsap.set("#dot",{{attr:{{cx:XS(x),cy:YS(y)}}}});gsap.set("#dl",{{attr:{{x1:XS(x),x2:XS(x),y2:YS(y)}}}});gsap.set("#dotg",{{opacity:hid?0:1}});}}}},{dstart:.2f});''')
FT('#hole', {'opacity': 0, 'scale': .3, 'transformOrigin': '50% 50%'}, {'opacity': 1, 'scale': 1}, wf(13, 'huequito'), .6, 'back.out(1.6)')
FT('#htx', {'opacity': 0}, {'opacity': 1}, wf(13, 'huequito') + .3, .6)
# s8
IN('#t8', bounds[8] + .5, 1.0)
IN('#t8b', A(15) - .1, .8)
FT('#cta', {'opacity': 0, 'scale': .8}, {'opacity': 1, 'scale': 1}, A(15) + 1.6, .8, 'back.out(1.5)')

# ---- subtitulos
for i, a, b in wjs:
    js.append(f'tl.to("#w{i}",{{backgroundColor:"#FF8A4C",color:"#0A0F1F",scale:1.06,duration:.1}},{a:.2f});tl.to("#w{i}",{{backgroundColor:"rgba(255,138,76,0)",color:"#F4F6FF",scale:1,duration:.2}},{b:.2f});')
# mascota: habla, parpadea, flota
for i, a, b in wjs:
    js.append(f'tl.fromTo("#mo",{{scaleY:.2}},{{scaleY:1,duration:{min(.12,(b-a)/2):.2f},yoyo:true,repeat:1,ease:"sine.inOut",immediateRender:false}},{a:.2f});')
js.append(f'tl.to("#mas",{{y:-10,duration:2.2,repeat:{int(FIN/2.2)},yoyo:true,ease:"sine.inOut"}},0);')
for k in range(int(FIN / 3.6)):
    t = 1.8 + k * 3.6 + (k % 3) * .4
    js.append(f'tl.to("#eyes",{{scaleY:.1,duration:.08,yoyo:true,repeat:1,transformOrigin:"50% 50%"}},{t:.2f});')
# fondo: manchas pastel lentas
js.append(f'tl.to("#b1",{{x:120,y:90,duration:{FIN},ease:"none"}},0);tl.to("#b2",{{x:-110,y:-70,duration:{FIN},ease:"none"}},0);tl.to("#b3",{{x:70,y:-100,duration:{FIN},ease:"none"}},0);')
js.append(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{FIN},ease:"none"}},0);')
# celebracion suave (estrellas) en s8
for i in range(14):
    ang = i / 14 * 2 * math.pi; r = 260 + (i % 3) * 70
    js.append(f'tl.fromTo("#sp{i}",{{x:0,y:0,opacity:0,scale:.3}},{{x:{math.cos(ang)*r:.0f},y:{math.sin(ang)*r*0.8:.0f},opacity:1,scale:1,duration:1.4,ease:"power2.out",immediateRender:false}},{bounds[8]+.9+(i%4)*.08:.2f});tl.to("#sp{i}",{{opacity:0,duration:.8}},{bounds[8]+2.3:.2f});')
sp = ''.join(f'<div class="sp" id="sp{i}" style="background:{[ORG,BLU,GRN,"#F2B705"][i%4]}"></div>' for i in range(14))

PT = ''.join(f'<div class="pt" id="pt{i}" style="left:{(i*173)%980}px;top:{(i*311)%1750+80}px">{["+","−","×","÷","=","x²","√","π","∫","Σ"][i%10]}</div>' for i in range(22))
for i in range(22):
    js.append(f'tl.to("#pt{i}",{{y:{-60-(i%5)*30},x:{(i%7-3)*18},rotation:{(i%5-2)*12},duration:{FIN},ease:"none"}},0);')
# intro
js.append(f'tl.fromTo("#lg",{{opacity:0,scale:.82,letterSpacing:"26px"}},{{opacity:1,scale:1,letterSpacing:"2px",duration:1.0,ease:"power3.out",immediateRender:false}},.25);')
js.append('tl.to("#lgl",{width:520,duration:.8,ease:"power2.inOut"},.75);tl.fromTo("#lgs",{opacity:0,y:14},{opacity:1,y:0,duration:.7,immediateRender:false},1.05);')
js.append(f'tl.to("#intro",{{opacity:0,duration:.6,ease:"power1.in"}},{OFF-.55:.2f});tl.set("#intro",{{display:"none"}},{OFF+.1:.2f});')
# hud capitulos
_ch=[bounds[1],bounds[3],bounds[5],bounds[6],bounds[8]]
_nm=['El error','La prueba','El método','Dominio y gráfica','Cierre']
for i,t in enumerate(_ch):
    js.append(f'tl.to("#pl{i}",{{backgroundColor:"#FF8A4C",duration:.4}},{t:.2f});')
    js.append(f'tl.call(()=>{{document.getElementById("hudl").textContent="{_nm[i]}";}},null,{t:.2f});')
js.append(f'tl.call(()=>{{document.getElementById("hudl").textContent="Simplificar fracciones";}},null,0);')
# camara lenta
js.append(f'tl.fromTo("#card",{{scale:1.04}},{{scale:1.09,duration:{FIN},ease:"none",immediateRender:false}},0);')
import json as _j
_sf={'off':OFF,'fin':FIN,'bounds':bounds,'chips':[wf(8,'multiplicados')+.6, wf(8,'sumados')+.6],'check':[wf(3,'tres')+.3],'bad':[wf(4,'cinco')+.35, wf(1,'mal')],'res':[wf(11,'queda')],'cta':[A(15)+1.6],'hole':[wf(13,'huequito')],'big':[A(9)+.2]}
_j.dump(_sf,open('/tmp/ref/v4/sfx.json','w'))
lines = ''
css = f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#FBF6EA}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;color:{INK};font-family:'Space Grotesk',sans-serif;background:#FBF6EA}}
.ln{{position:absolute;left:0;width:1080px;height:2px;background:#DDE6F4;opacity:.8}}
#margin{{position:absolute;left:96px;top:0;width:3px;height:1920px;background:#F2B9B0;opacity:.7}}
.blob{{position:absolute;border-radius:50%;filter:blur(70px)}}
#b1{{left:-150px;top:140px;width:520px;height:520px;background:#FFD9BF;opacity:.7}}
#b2{{left:700px;top:700px;width:480px;height:480px;background:#CFE0FF;opacity:.6}}
#b3{{left:100px;top:1250px;width:500px;height:500px;background:#D7F2DE;opacity:.55}}
#bar{{position:absolute;left:0;top:0;height:8px;width:1080px;background:{ORG};transform-origin:left}}
.brand{{position:absolute;left:70px;top:80px;font:900 46px Literata,Georgia,serif}}
.brand b{{color:{ORG};font-weight:900}}
.topic{{position:absolute;right:70px;top:84px;font:700 28px 'Space Grotesk';letter-spacing:2px;text-transform:uppercase;color:#6B7494}}
#card{{position:absolute;left:60px;top:200px;width:960px;height:1130px;background:#FFFFFF;border-radius:36px;box-shadow:0 30px 70px rgba(31,42,68,.16),0 4px 0 rgba(31,42,68,.05);overflow:hidden}}
#tape{{position:absolute;left:400px;top:178px;width:280px;height:46px;background:rgba(232,99,42,.55);transform:rotate(-2deg);border-radius:4px;z-index:3}}
.clip{{position:absolute;left:0;top:0;width:960px;height:1130px}}
.in{{position:absolute;inset:0;opacity:0}}
#wipe{{position:absolute;left:0;top:0;width:1300px;height:1130px;background:linear-gradient(90deg,rgba(255,255,255,0) 0,#fff 14%,#fff 92%,{ORG} 92%,{ORG} 94%,rgba(255,255,255,0) 100%);transform:translateX(-1400px);z-index:5}}
.eq{{text-align:center;white-space:nowrap;color:{INK}}}
.kick{{position:absolute;left:0;width:960px;top:70px;text-align:center;font:700 34px 'Space Grotesk';letter-spacing:3px;text-transform:uppercase;color:{ORG}}}
.kick.l{{position:static;text-align:left;font-size:30px;margin-bottom:6px;color:{BLU}}}
.h1{{position:absolute;left:0;width:960px;top:240px;text-align:center;font:900 124px/1.05 Literata,Georgia,serif}}
.h2{{position:absolute;left:0;width:960px;top:120px;text-align:center;font:900 84px/1.1 Literata,Georgia,serif}}
.h3{{position:absolute;left:60px;width:840px;top:560px;text-align:center;font:700 54px/1.25 Literata,Georgia,serif}}
.mk{{background:linear-gradient(transparent 58%,#FFE08A 58%);padding:0 8px}}
.note{{position:absolute;left:120px;width:720px;top:680px;text-align:center;font:500 46px/1.3 'Space Grotesk';color:#46506E;background:#FFF6D8;border-radius:24px;padding:26px 30px;transform:rotate(-1.2deg);box-shadow:0 8px 24px rgba(31,42,68,.1)}}
.stack{{position:absolute;left:0;width:960px;top:200px;display:flex;flex-direction:column;align-items:center;gap:70px}}
.bigx{{position:absolute;right:50px;top:520px;font:900 190px 'Space Grotesk';color:{RED}}}
#lupa{{position:absolute;left:360px;top:230px}}
#t2{{top:600px}}
.row3{{position:absolute;left:60px;width:840px}}
#r1{{top:100px}}#r2{{top:480px}}
.line{{display:flex;align-items:center;gap:22px;white-space:nowrap}}
.ck{{position:absolute;right:-20px;top:-34px;width:100px;height:100px;border-radius:50%;background:#DFF5E6;color:{GRN};font:900 70px/100px 'Space Grotesk';text-align:center}}
.ck.bad{{background:#FBE0E0;color:{RED}}}
.verd{{position:absolute;left:0;width:960px;top:880px;text-align:center}}
.sub{{font:700 40px 'Space Grotesk';color:{RED};margin-top:10px;letter-spacing:2px;text-transform:uppercase}}
.card{{position:absolute;left:60px;width:840px;border:6px solid;border-radius:32px;padding:26px 30px;background:#FFFFFF}}
.okc{{top:300px;border-color:{GRN};background:#F3FBF5}}.badc{{top:700px;border-color:{RED};background:#FEF4F4}}
.lab{{font:700 40px 'Space Grotesk';margin-bottom:14px;text-align:center}}
.blk{{position:absolute;left:30px;width:900px}}
.tag{{font:700 30px 'Space Grotesk';letter-spacing:2px;text-transform:uppercase;margin-bottom:6px}}
.helper{{position:absolute;right:0;top:-6px;font-size:34px;color:#46506E;background:#EEF3FF;padding:6px 20px;border-radius:16px;opacity:0}}
.row{{display:flex;align-items:center;gap:14px;font-size:58px;margin-top:20px;white-space:nowrap}}.row span{{white-space:nowrap}}
.chips{{position:absolute;right:0;top:-6px;display:flex;gap:14px}}
.chip{{color:{INK};border-radius:40px;padding:4px 26px;font:700 44px 'IBM Plex Mono',monospace;opacity:0}}
.resbox{{border:7px solid {ORG};border-radius:32px;padding:10px 70px;background:#FFF1E8;box-shadow:0 18px 40px rgba(232,99,42,.2);opacity:0}}
.dom{{position:absolute;left:60px;width:840px;display:flex;align-items:center;gap:30px;border:5px solid {ORG};border-radius:28px;padding:26px 34px;background:#FFF6EF}}
.dom b{{font:700 72px 'IBM Plex Mono',monospace;color:{ORG}}}.dom i{{font:400 40px 'Space Grotesk';color:#46506E;font-style:normal}}
#d1{{top:520px}}#d2{{top:740px}}
.cta{{position:absolute;left:260px;top:800px;width:440px;text-align:center;background:{ORG};color:#fff;font:700 62px 'Space Grotesk';padding:26px 0;border-radius:100px;box-shadow:0 14px 30px rgba(232,99,42,.35)}}
.sp{{position:absolute;left:470px;top:1010px;width:20px;height:20px;border-radius:50%;opacity:0}}
#mascot{{position:absolute;left:56px;top:1388px;width:190px;height:190px}}
#bub{{position:absolute;left:272px;top:1380px;width:752px;height:218px;background:#fff;border-radius:34px;box-shadow:0 14px 36px rgba(31,42,68,.14);display:flex;align-items:center;justify-content:center}}
#bub:before{{content:"";position:absolute;left:-14px;top:92px;width:34px;height:34px;background:#fff;transform:rotate(45deg);border-radius:6px}}
.capc{{position:absolute;left:272px;top:1380px;width:752px;height:218px;display:flex;align-items:center;justify-content:center}}
.cap{{width:700px;text-align:center;font:700 54px/1.3 'Space Grotesk';color:#5A6380}}
.w{{display:inline-block;padding:0 8px;border-radius:12px;color:#5A6380;background:rgba(255,224,138,0)}}
'''

EXTRA = """
html,body{background:#070B18}
#root{background:radial-gradient(1200px 900px at 15% 8%,#18244A 0,#0B1122 55%,#060914 100%);color:#EEF2FF}
#margin,#bub,#mascot,#tape,.topic{display:none}
.blob{filter:blur(110px)}
#b1{background:#FF8A4C;opacity:.22}#b2{background:#4A7DFF;opacity:.26}#b3{background:#3DDC84;opacity:.12}
#dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.10) 1.6px,transparent 1.7px);background-size:54px 54px;opacity:.55}
#vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.55) 100%);pointer-events:none;z-index:30}
#bar{height:10px;background:linear-gradient(90deg,#FF8A4C,#FFC36B);z-index:40}
.brand{top:62px;left:64px;font:900 44px Literata,Georgia,serif;color:#fff;z-index:20}
.brand b{color:#FF8A4C}
#hud{position:absolute;right:64px;top:74px;display:flex;gap:10px;z-index:20}
.pill{width:44px;height:10px;border-radius:6px;background:rgba(255,255,255,.18)}
#hudl{position:absolute;right:64px;top:100px;font:700 24px 'Space Grotesk';letter-spacing:3px;text-transform:uppercase;color:#9AA6CF;z-index:20}
#card{top:300px;left:60px;background:transparent;box-shadow:none;border-radius:0;overflow:visible;transform-origin:50% 0}
#wipe{background:linear-gradient(90deg,rgba(7,11,24,0) 0,#070B18 14%,#070B18 92%,#FF8A4C 92%,#FF8A4C 94%,rgba(7,11,24,0) 100%);height:1180px;top:-20px}
.kick{color:#FF8A4C;font-size:36px}.kick.l{color:#6FB1FF}
.mk{background:linear-gradient(transparent 62%,rgba(255,138,76,.55) 62%)}
.note{background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.16);color:#DDE4FF;backdrop-filter:blur(4px)}
.card,.dom{background:rgba(255,255,255,.06)!important;border-width:3px}
.okc{border-color:#3DDC84}.badc{border-color:#FF6B6B}
.chip{color:#0A0F1F}
#card svg g[stroke="#C9CFDF"]{stroke:rgba(255,255,255,.13)}
#card svg text{fill:#9AA6CF}
.helper{background:rgba(111,177,255,.16);color:#CFE0FF}
.resbox{background:rgba(255,138,76,.12);border-color:#FF8A4C;box-shadow:0 0 60px rgba(255,138,76,.35)}
.dom b{color:#FF8A4C}.dom i{color:#C9D2F0}
.ck{background:rgba(61,220,132,.18);color:#3DDC84}.ck.bad{background:rgba(255,107,107,.18);color:#FF6B6B}
.cta{background:linear-gradient(90deg,#FF8A4C,#FF6B3D);color:#fff}
.h1,.h2,.h3{color:#fff}
.capc{left:60px;top:1490px;width:960px;height:320px}
.cap{width:900px;font:700 68px/1.28 'Space Grotesk';color:#7D88AD;text-shadow:0 4px 24px rgba(0,0,0,.6)}
.w{padding:2px 12px;border-radius:14px;color:#7D88AD}
#intro{position:absolute;inset:0;background:radial-gradient(900px 700px at 50% 45%,#1B2A58 0,#070B18 70%);z-index:60;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px}
#lg{font:900 150px Literata,Georgia,serif;color:#fff;letter-spacing:2px;opacity:0}#lg b{color:#FF8A4C}
#lgs{font:700 34px 'Space Grotesk';letter-spacing:8px;text-transform:uppercase;color:#9AA6CF;opacity:0}
#lgl{width:0;height:8px;background:#FF8A4C;border-radius:6px}
.pt{position:absolute;font:700 64px 'IBM Plex Mono',monospace;color:#fff;opacity:.07;z-index:1}
"""
css += EXTRA

mascot = f'''<svg id="mascot" viewBox="0 0 200 200"><g id="mas"><ellipse cx="100" cy="188" rx="58" ry="8" fill="rgba(31,42,68,.12)"/><circle cx="100" cy="102" r="84" fill="{ORG}"/><path d="M52 60 Q70 30 104 28" stroke="#FFB48A" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/><path d="M96 20 Q92 2 112 6" stroke="{GRN}" stroke-width="8" fill="none" stroke-linecap="round"/><g id="eyes" style="transform-origin:100px 92px"><ellipse cx="70" cy="92" rx="11" ry="15" fill="{INK}"/><ellipse cx="130" cy="92" rx="11" ry="15" fill="{INK}"/><circle cx="74" cy="86" r="4" fill="#fff"/><circle cx="134" cy="86" r="4" fill="#fff"/></g><circle cx="48" cy="122" r="12" fill="#FF9A7A" opacity=".75"/><circle cx="152" cy="122" r="12" fill="#FF9A7A" opacity=".75"/><ellipse id="mo" cx="100" cy="128" rx="17" ry="11" fill="#7A2410" style="transform-origin:100px 128px;transform:scaleY(.2)"/></g></svg>'''
html = f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/katex.css"/>
<style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{FIN}" data-width="1080" data-height="1920">
<audio id="voz" src="assets/mix.mp3" data-start="0" data-duration="{FIN}" data-track-index="0"></audio>
<div id="dots"></div>{lines}<div id="margin"></div><div class="blob" id="b1"></div><div class="blob" id="b2"></div><div class="blob" id="b3"></div>
<div id="bar"></div><div class="brand">MATH<b>UNAL</b></div><div class="topic">Simplificar fracciones</div><div id="hud">{''.join(f'<div class="pill" id="pl{i}"></div>' for i in range(5))}</div><div id="hudl">Simplificar fracciones</div>{PT}<div id="vig"></div>
<div id="card">{''.join(sc)}{sp}<div id="wipe"></div></div><div id="tape"></div>
<div id="bub"></div>{''.join(caps)}{mascot}
<script>window.__timelines=window.__timelines||{{}};
{chr(10).join(['tl.set(%s,{opacity:0},0);'%json.dumps(', '.join(PRE))]+js)}
window.__timelines["main"]=tl;tl.seek(0);</script><div id="intro"><div id="lg">MATH<b>UNAL</b></div><div id="lgl"></div><div id="lgs">Matemáticas paso a paso</div></div></div></body></html>'''
# el timeline debe crearse antes de los tweens
html = html.replace('{chr(10).join(js)}', '')
html = html.replace('<script>window.__timelines=window.__timelines||{};', '<script>window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});', 1)
open(H + '/index.html', 'w').write(html)
print('ok', len(html), 'FIN', FIN, 'chunks', len(chunks), [round(b, 1) for b in bounds])
