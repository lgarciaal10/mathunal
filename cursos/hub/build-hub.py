import json,glob,base64,re,html
S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/'
URL={'limite-1':'MEe4ZsqVYZh8Scuffrkm6J','limite-2':'DfLdWbhUCMSCtmevKgFXkk','limite-3':'TnYQvAK32tQvAxPn1JKCPK','limite-4':'FLPBjxpgTrBq4YDcTdRBsn','infinito':'CWUYz7ad2qMVePzyKzXs5Z','asintotas':'HyyaHKjEKbc92oqwK9N9UU',
'derivada-1':'G9un4RmMz9gsEeyL3u4Xfj','derivada-2':'T3oDZrjz5qRLvVSjmQQ1U2','derivada-3':'SsyxFR7HeW4e7htTm2KU7N','derivada-4':'KGhXqwZrCgHB4FY3y84taV','derivada-5':'FFPeDqjfC5XoThNqTxHECv','derivada-6':'6BcdkekSK3PknmLi5PEnKy','derivada-7':'97D5pf9BKd32iPdMjwkzmd','derivada-8':'VcQiFP76xrcD6fSDYwGFhg','derivada-9':'WTaRj6nb57AZGiu8hKp52g','derivada-10':'5vRnURJjgP49zZcbWuGZNf',
'valor-medio':'XPe9RKwNThyQuZEdH9DTCV','derivada-11':'G4FwomdF1BNqPkycc27QsC','derivada-12':'SBdayeF1z5ZTVee7HZkLEW','derivada-13':'BrFyE9m4kDRrQaExnAGE3s','derivada-14':'H4cPUXxouAWLZVPRSwP3PJ','lhopital':'44qhxnvMFNKajLVBwmCoks','newton':'7tKr792EYwgg6J2cq8bQYh','tfc':'NYkwQjQvRi7QZKuWUD6zep'}
TIPO={'hueco':'Hueco','secante':'Secante','tvm':'Cuerda y tangente','newton':'Newton','area':'Área','asintota':'Asíntotas','entre':'Entre curvas','polar':'Polar'}
URL2={'tfc':'X83qjecCB8a82HjsnMLLP8','sustitucion':'FpXNniKzBdVDysxhapvmEx','partes':'7kmd6n39MPBsWv3maQXWTg','entre':'B8bLSXgWsgWsAVLi1u8hd2','trig':'TV1EpabT8uL9FKW5eMzeT3','sentri':'Cutr3fxsNukh5oTryHLhh3','fparc':'XxhJ895h7MDWqQE7Rpwbd7','impropias':'9PcgLtbxP8GikgiWAmJDpJ','volumenes':'JDJ6oaL3xE6vWaAVhpiWfG','trabajo':'8oiENYBURzs8bRGs6mra2r','arco':'F3oCUxNpXkPbwmzkVZKq8y','polares':'M35k8QRJM57ua1ifsTTzRv','series':'XLqVVNUnZUgxFtKVrLNmU3'}
CURSOS=[('Cálculo Diferencial','calculo',URL),('Cálculo Integral','calcint',URL2)]
mods={}
for ci,(cn,pre,UD) in enumerate(CURSOS):
  for k in UD:
    L=json.load(open(S+f'plantilla/{pre}-{k}.json'))
    n=int(re.search(r'Lección (\d+) de (\d+)',L['posicion']).group(1)); tot=int(re.search(r'de (\d+)',L['posicion']).group(1))
    bl=[b for s in L['leer']['secciones'] for b in s['bloques']]
    sim=[b for b in bl if b['t']=='simulacro']
    d=dict(k=k,n=n,titulo=L['titulo'],min=L['minutos'],tipo=TIPO[L['grafica'].get('tipo','hueco')],zoom=bool(L['grafica'].get('zoom')),
      sim=sum(len(b['preguntas']) for b in sim),eng=any(b['t']=='ingenieria' for b in bl),
      act=sum(1 for b in bl if b['t'] in('completar','error','ordenar')),guiado=bool(L['pregunta'].get('pistas')),url='https://claude.ai/artifact/'+UD[k])
    mods.setdefault((ci,L['modulo'],tot),[]).append(d)
orden=sorted(mods.items(),key=lambda kv:(kv[0][0],kv[0][1]))
for _,v in orden: v.sort(key=lambda d:d['n'])
todas=[d for _,v in orden for d in v]
N=len(todas); nsim=sum(1 for d in todas if d['sim']); npreg=sum(d['sim'] for d in todas); neng=sum(d['eng'] for d in todas); nzoom=sum(d['zoom'] for d in todas)
NMOD=len(orden); NDIF=sum(1 for d in todas if d['url'].split('/')[-1] in URL.values()); NINT=N-NDIF
print(N,nsim,npreg,neng,nzoom)
def b64(p,mime): return f"data:{mime};base64,"+base64.b64encode(open(p,'rb').read()).decode()
img={n:b64(S+f'hub/{n}.jpg','image/jpeg') for n in ['zoom','newton','tfc','asint','quiz','ordenar','eng','insignias','poster','entre','polar','series']}
vid=b64(S+'video-cadena-vertical.mp4','video/mp4')
ICON={'ok':'<svg class="ic ok" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.8l4.6 4.6L19 7.6"/></svg>','no':'<svg class="ic no" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 12h10"/></svg>'}
def celda(c,titulo): return f'<span class="cell {"on" if c else "off"}">{ICON["ok"] if c else ICON["no"]}<span class="lab">{titulo}</span><span class="sr">{"sí" if c else "no"}</span></span>'
def nombre_mod(m):
    m2=re.sub(r'^Módulo (\d+)\s*','',m[0]); return int(re.search(r'\d+',m[0]).group(0)),m2
filas=''
ultimo=-1
for (ci,m,tot),v in orden:
    num,nom=nombre_mod((m,tot))
    hechas=len(v)
    if ci!=ultimo:
        ultimo=ci; cuenta=sum(len(w) for (c2,_,_),w in orden if c2==ci)
        filas+=f'<div class="curso-h"><h3>{html.escape(CURSOS[ci][0])}</h3><p class="num"><b>{cuenta}</b> lecciones</p></div>'
    filas+=f'<section class="mod" aria-labelledby="m{ci}{num}"><header class="modh"><div><p class="eyebrow">Módulo {num}</p><h3 id="m{ci}{num}">{html.escape(nom)}</h3></div><p class="modc num"><b>{hechas}</b> de {tot} lecciones</p></header><div class="bar" role="img" aria-label="{hechas} de {tot} lecciones hechas"><i style="width:{hechas/tot*100:.0f}%"></i></div><ul class="les">'
    for d in v:
        att=f'data-sim="{1 if d["sim"] else 0}" data-eng="{1 if d["eng"] else 0}" data-zoom="{1 if d["zoom"] else 0}"'
        extra=f'<span class="chip soft">{d["act"]} actividades</span>' if d['act'] else ''
        filas+=f'<li class="les-i" {att}><a class="lt" href="{d["url"]}" target="_blank" rel="noopener"><span class="num ln">{d["n"]}</span><span class="lname">{html.escape(d["titulo"])}</span>{extra}</a><span class="tipo">{d["tipo"]}</span><span class="feat">{celda(d["zoom"],"Zoom")}{celda(d["guiado"],"Pistas")}{celda(d["sim"],"Simulacro")}{celda(d["eng"],"Ingeniería")}</span></li>'
    filas+='</ul></section>'
gal=[('zoom','Zoom en el hueco','En Regla de L\'Hôpital la gráfica se acerca 2000 veces. Los dos puntos casi tocan el hueco y las marcas pasan a cuatro decimales.','ancha'),
('quiz','Quiz con pistas','Se pide una pista a la vez. Cada error explica qué se hizo mal, como olvidar la derivada de lo de adentro.',''),
('newton','Tangentes de Newton','Cada tangente corta el eje más cerca de la raíz cuadrada de 2. Abajo se lee x y f(x) en cada paso.',''),
('tfc','Área acumulada','La zona se llena mientras x avanza, y la franja amarilla muestra por qué el área crece al ritmo de la altura.',''),
('asint','Asíntotas','La curva se dispara junto a x igual a 2 y se aplana contra y igual a 1.',''),
('ordenar','Ordena los pasos','Se tocan los pasos en el orden correcto. Si falla, una pista dice qué hacer primero.',''),
('eng','¿Para qué sirve?','Un caso de ingeniería con cifras. Aquí, el pistón de un motor y la regla de la cadena.',''),
('insignias','Tu avance','Cuatro insignias que cuentan cómo se estudió. No hay rachas ni puntos.',''),
('entre','Dos curvas','Área entre una recta y una parábola. La franja amarilla mide la curva de arriba menos la de abajo.',''),
('polar','Coordenadas polares','El radio gira y barre el área de una cardioide. Abajo se leen el área y el radio en cada ángulo.',''),
('series','Sumas parciales','Cada término suma menos y la curva se pega a la recta y igual a 3 sobre 2, que es el valor de la serie.','')]
g=''.join(f'<figure class="sh {c}"><img src="{img[n]}" alt="{html.escape(t)}" loading="lazy"><figcaption><b>{html.escape(t)}</b><span>{html.escape(d)}</span></figcaption></figure>' for n,t,d,c in gal)
page=f'''<title>Cursos MathUNAL</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:wght@600;900&family=Space+Grotesk:wght@400;500;600&family=IBM+Plex+Mono:wght@400;600&display=swap">
<style>
/* Concepto, una libreta de avance. Titulares en Literata, texto en Space Grotesk y cifras en IBM Plex Mono, naranja sobre azul marino como el sitio. */
:root{{--bg:#F5F7FC;--surf:#FFFFFF;--surf2:#EAEFFA;--line:#D3DBEF;--tx:#0B1230;--mu:#46557A;--acc:#A63A08;--acc-soft:rgba(166,58,8,.10);--curve:#2F5DB8;--ok:#117A3D;--on-acc:#FFFFFF;--serif:'Literata',Georgia,serif;--sans:'Space Grotesk',system-ui,sans-serif;--mono:'IBM Plex Mono',ui-monospace,monospace;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#060B1E;--surf:#0E1A3F;--surf2:#14224F;--line:#233468;--tx:#EAF0FF;--mu:#A5B4DB;--acc:#E8632A;--acc-soft:rgba(232,99,42,.16);--curve:#8FB4F2;--ok:#4ADE80;--on-acc:#060B1E;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#060B1E;--surf:#0E1A3F;--surf2:#14224F;--line:#233468;--tx:#EAF0FF;--mu:#A5B4DB;--acc:#E8632A;--acc-soft:rgba(232,99,42,.16);--curve:#8FB4F2;--ok:#4ADE80;--on-acc:#060B1E;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--tx);font-family:var(--sans);font-size:16px;line-height:1.55;padding-inline:max(16px,env(safe-area-inset-left,0px)) max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}}
.wrap{{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:56px}}
h1,h2,h3{{font-family:var(--serif);font-weight:900;line-height:1.1;margin:0;text-wrap:balance}}
h1{{font-size:clamp(2rem,6vw,3.4rem)}} h2{{font-size:clamp(1.5rem,3.6vw,2.1rem)}} h3{{font-size:1.25rem;font-weight:600}}
p{{margin:0}} a{{color:inherit}}
.num{{font-family:var(--mono);font-variant-numeric:tabular-nums}}
.eyebrow{{font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);font-weight:600}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
:focus-visible{{outline:3px solid var(--acc);outline-offset:3px;border-radius:10px}}
.brand{{display:flex;align-items:center;gap:10px;font-family:var(--serif);font-weight:900;font-size:1.15rem;letter-spacing:.02em}}
.brand svg{{width:22px;height:22px;stroke:var(--acc);fill:none;stroke-width:2.4;stroke-linecap:round}}
.brand b{{color:var(--acc)}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}}
.chip{{display:inline-flex;align-items:center;padding:4px 14px;border-radius:999px;background:var(--surf2);color:var(--mu);font-size:.85rem}}
.chip.soft{{background:var(--acc-soft);color:var(--tx)}}
.hero{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:40px;align-items:end}}
.hero p.lead{{color:var(--mu);font-size:1.1rem;max-width:56ch;margin-top:16px}}
.cifras{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 24px}}
.cifras li{{display:flex;flex-direction:column;gap:2px;border-top:2px solid var(--line);padding-top:10px}}
.cifras .big{{font-family:var(--mono);font-weight:600;font-size:2.1rem;line-height:1.05;color:var(--tx)}}
.cifras span{{color:var(--mu);font-size:.92rem}}
.sec-h{{display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap;margin-bottom:22px}}
.sec-h p{{color:var(--mu);max-width:58ch}}
.filtros{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px}}
.filtros button{{font:inherit;font-size:.92rem;min-height:40px;padding:8px 16px;border-radius:999px;border:1px solid var(--line);background:var(--surf);color:var(--tx);cursor:pointer}}
.filtros button[aria-pressed="true"]{{background:var(--acc);border-color:var(--acc);color:var(--on-acc);font-weight:600}}
.mods{{display:flex;flex-direction:column;gap:34px}}
.mod{{background:var(--surf);border-radius:28px;padding:24px clamp(16px,3vw,32px) 12px}}
.modh{{display:flex;justify-content:space-between;align-items:end;gap:12px;flex-wrap:wrap}}
.curso-h{{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:10px;margin-top:20px}}.curso-h h3{{font-size:1.7rem}}.curso-h p{{margin:0;color:var(--mu)}}.curso-h b{{color:var(--tx)}}
.modc{{color:var(--mu);font-size:.95rem}} .modc b{{color:var(--tx)}}
.bar{{height:8px;border-radius:999px;background:var(--surf2);margin:14px 0 8px;overflow:hidden}}
.bar i{{display:block;height:100%;background:var(--acc);border-radius:999px}}
.les{{list-style:none;margin:0;padding:0}}
.les-i{{display:grid;grid-template-columns:minmax(0,1fr) 150px 150px;gap:6px 16px;align-items:center;padding:12px 0;border-top:1px solid var(--line)}}
.les-i:first-child{{border-top:0}}
.les-i[hidden]{{display:none}}
.lt{{display:flex;gap:14px;align-items:baseline;text-decoration:none;min-width:0}}
.lt:hover .lname{{text-decoration:underline;text-decoration-color:var(--acc);text-underline-offset:4px}}
.ln{{color:var(--acc);font-weight:600;width:1.6em;flex:none}}
.lname{{font-weight:500;overflow-wrap:anywhere}}
.tipo{{color:var(--mu);font-size:.88rem}}
.feat{{display:flex;gap:16px;justify-content:flex-start}}
.cell{{display:inline-flex;width:24px;justify-content:center;align-items:center}}
.lab{{display:none}}
.lt .chip{{margin-left:6px;white-space:nowrap}}
.ic{{width:20px;height:20px;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}}
.ic.ok{{stroke:var(--ok)}} .ic.no{{stroke:var(--line)}}
.leyenda{{display:grid;grid-template-columns:minmax(0,1fr) 150px 150px;gap:6px 16px;color:var(--mu);font-size:.82rem;padding:0 clamp(16px,3vw,32px);margin-bottom:-18px}}
.leyenda .feat{{gap:16px}} .leyenda .feat span{{width:24px;text-align:center}}
.sheet{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:18px}}
.sheet{{align-items:start}}
.sh{{margin:0;grid-column:span 2;display:flex;flex-direction:column;gap:10px;min-width:0}}
.sh.ancha{{grid-column:span 4}}
.sh img{{width:100%;border-radius:20px;border:1px solid var(--line);display:block;background:var(--surf)}}
.sh figcaption{{display:flex;flex-direction:column;gap:2px;font-size:.93rem;color:var(--mu)}}
.sh figcaption b{{color:var(--tx);font-weight:600}}
.vid{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:36px;align-items:center}}
.vid video{{width:100%;max-width:300px;border-radius:24px;border:1px solid var(--line);background:var(--surf);display:block}}
.vid ul{{margin:16px 0 0;padding-left:1.1em;color:var(--mu);display:grid;gap:6px}}
.falta{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}}
.falta>div{{background:var(--surf);border-radius:24px;padding:24px;display:flex;flex-direction:column;gap:12px}}
.falta ul{{margin:0;padding-left:1.1em;display:grid;gap:8px;color:var(--mu)}} .falta li b{{color:var(--tx);font-weight:600}}
footer{{color:var(--mu);font-size:.88rem;display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line);padding-top:20px}}
@media (max-width:860px){{.hero{{grid-template-columns:1fr;gap:28px}}.sh,.sh.ancha{{grid-column:span 6}}.vid{{grid-template-columns:1fr}}.falta{{grid-template-columns:1fr}}.leyenda{{display:none}}
.les-i{{grid-template-columns:minmax(0,1fr);gap:4px}} .tipo{{padding-left:calc(1.6em + 14px)}} .feat{{padding-left:calc(1.6em + 14px);flex-wrap:wrap;gap:6px}}
.cell.off{{display:none}} .cell.on{{width:auto;gap:4px;padding:2px 10px 2px 6px;border-radius:999px;background:var(--surf2);color:var(--mu);font-size:.8rem}} .cell.on .lab{{display:inline}} .cell.on .ic{{width:14px;height:14px}}}}
@media (min-width:861px) and (max-width:1000px){{.sh{{grid-column:span 3}}.sh.ancha{{grid-column:span 6}}}}
@media (prefers-reduced-motion:no-preference){{.mod{{animation:sube .5s ease both}}@keyframes sube{{from{{opacity:.001;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}}}
</style>
<div class="wrap">
<header class="top"><div class="brand"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 3.5c-2.6 0-3.4 1.6-3.4 4.2v8.6c0 2.6-.8 4.2-3.4 4.2"/></svg><span>MATH<b>UNAL</b></span></div><span class="chip">Borrador para revisar</span></header>
<section class="hero">
<div><p class="eyebrow">Cálculo Diferencial e Integral</p><h1>Las {N} lecciones ya están escritas</h1><p class="lead">Cada lección tiene tres formas de estudiar, Ver, Leer y Practicar. Después se le fue sumando lo que ayuda a aprender de verdad, como pistas de a una, simulacros con preguntas reales de parciales, ejemplos de ingeniería y repaso espaciado. Esta página junta todo y se arma con los archivos reales de las lecciones.</p></div>
<ul class="cifras"><li><span class="big">{N}</span><span>lecciones en {NMOD} módulos, {NDIF} de Diferencial y {NINT} de Integral</span></li><li><span class="big">{npreg}</span><span>preguntas reales del banco, en {nsim} simulacros</span></li><li><span class="big">{neng}</span><span>con ejemplo de ingeniería</span></li><li><span class="big">{nzoom}</span><span>con zoom en la gráfica</span></li></ul>
</section>
<section aria-labelledby="les"><div class="sec-h"><div><p class="eyebrow">El curso</p><h2 id="les">Lección por lección</h2></div><p>Cada título abre la lección en una pestaña nueva. Las marcas dicen qué trae cada una.</p></div>
<div class="filtros" role="group" aria-label="Filtrar lecciones"><button type="button" aria-pressed="true" data-f="todas">Todas</button><button type="button" aria-pressed="false" data-f="sim">Con simulacro</button><button type="button" aria-pressed="false" data-f="eng">Con ejemplo de ingeniería</button><button type="button" aria-pressed="false" data-f="zoom">Con zoom</button></div>
<div class="leyenda" aria-hidden="true"><span></span><span>Gráfica</span><div class="feat"><span>Zoom</span><span>Pistas</span><span>Simul.</span><span>Ing.</span></div></div>
<div class="mods" id="mods">{filas}</div></section>
<section aria-labelledby="vis"><div class="sec-h"><div><p class="eyebrow">Capturas reales</p><h2 id="vis">Lo nuevo, visto</h2></div><p>Salen de las lecciones publicadas, en tema oscuro o claro según la captura.</p></div><div class="sheet">{g}</div></section>
<section class="vid" aria-labelledby="vd"><video controls preload="none" poster="{img['poster']}" playsinline aria-label="Video de 25 segundos sobre la regla de la cadena"><source src="{vid}" type="video/mp4"></video>
<div><p class="eyebrow">Video de prueba</p><h2 id="vd">La regla de la cadena en 25 segundos</h2><ul><li>Vertical para redes, 1080 por 1920.</li><li>Sin voz y sin música, con subtítulos.</li><li>Usa las mismas cifras de la lección, hecho con Remotion.</li><li>Falta mejorarlo. Cuando lleguen tus reels de referencia ajusto el estilo.</li></ul></div></section>
<section aria-labelledby="fl"><div class="sec-h"><div><p class="eyebrow">Para decidir</p><h2 id="fl">Lo que falta</h2></div></div><div class="falta">
<div><h3>Necesito de ti</h3><ul><li><b>Leer las explicaciones.</b> La redacción de las pistas, los errores y los textos nuevos no la ha revisado nadie más, y las {NINT} lecciones de Integral son borradores completos.</li><li><b>Ejemplos de ingeniería de confianza media y baja.</b> Son 8 y están en el documento que te mandé. Dos necesitan un caso tuyo.</li><li><b>Los reels de referencia</b> para ajustar el estilo de los videos.</li><li><b>El temario oficial,</b> porque el orden de los módulos sale del banco y de mi criterio.</li></ul></div>
<div><h3>Sin probar</h3><ul><li>Con estudiantes reales, para saber si las pistas están bien dosificadas.</li><li>En un celular real, en Safari y en Firefox, y con lector de pantalla.</li><li>El repaso y las insignias guardan datos por navegador. Con todas las lecciones en un solo sitio, una vista global de repaso sí funcionaría.</li><li>Las lecciones de Integral solo traen simulacro cuando el banco tiene 3 preguntas distintas del tema, y por eso unas no lo traen. Su orden y su contenido salen del banco y de mi criterio, sin el temario oficial.</li><li>Las otras 9 materias tienen solo su estructura, sin lecciones.</li></ul></div></div></section>
<footer><p>Las cifras de esta página se calculan de los archivos de las lecciones. Todo está en el repositorio, rama cursos-mockups, solicitud 13 en borrador.</p><p>Las lecciones son privadas, así que los enlaces solo abren para quien tenga acceso.</p></footer>
</div>
<script>
(function(){{
  var btns=[].slice.call(document.querySelectorAll('.filtros button')), items=[].slice.call(document.querySelectorAll('.les-i'));
  function aplicar(f){{
    btns.forEach(function(b){{ b.setAttribute('aria-pressed',b.getAttribute('data-f')===f?'true':'false'); }});
    items.forEach(function(li){{ li.hidden=!(f==='todas'||li.getAttribute('data-'+f)==='1'); }});
    [].forEach.call(document.querySelectorAll('.mod'),function(m){{ var v=m.querySelectorAll('.les-i:not([hidden])').length; m.hidden=(v===0); }});
  }}
  btns.forEach(function(b){{ b.addEventListener('click',function(){{ aplicar(b.getAttribute('data-f')); }}); }});
}})();
</script>
'''
open(S+'hub/cursos-mathunal.html','w').write(page)
print(len(page)/1e6,'MB')
