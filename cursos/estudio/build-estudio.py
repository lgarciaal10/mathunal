import json,glob,re,html,ast,sys
S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/'
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;')
def attr(s): return str(s).replace('&','&amp;').replace('"','&quot;').replace('<','&lt;')
def mt(s): return ''.join(('<span data-tex="'+attr(x)+'"></span>') if i%2 else esc(x) for i,x in enumerate(str(s).split('$')))
def clave(s):
    h=0; b=str(s).encode('utf-16-le')
    for i in range(0,len(b),2):
        c=b[i]|(b[i+1]<<8); h=(h*31+c) & 0xFFFFFFFF
        if h>=2**31: h-=2**32
    h&=0xFFFFFFFF
    d='0123456789abcdefghijklmnopqrstuvwxyz'; o=''
    while h: o=d[h%36]+o; h//=36
    return o or '0'
hub=open(S+'hub/build-hub.py').read()
URLS={}
for n,pre in [('URL','calculo'),('URL2','calcint'),('URL3','alglin'),('URL4','edo'),('URL5','otras'),('URL6','matbas'),('URL7','fund'),('URL8','geovec'),('URL9','disc'),('URL10','mn')]:
    m=re.search(r'^'+n+r"=(\{.*?\})\s*$",hub,re.M|re.S)
    if m:
        for k,v in ast.literal_eval(m.group(1)).items(): URLS[(pre if n!='URL5' else k.split(':')[0])+'-'+k]=v
CURSOS=['Matemáticas Básicas','Cálculo Diferencial','Cálculo Integral','Álgebra Lineal','Ecuaciones Diferenciales','Fundamentos de Matemáticas','Geometría Vectorial y Analítica','Matemáticas Discretas','Métodos Numéricos']
CPRE={'matbas':'Matemáticas Básicas','calculo':'Cálculo Diferencial','calcint':'Cálculo Integral','alglin':'Álgebra Lineal','edo':'Ecuaciones Diferenciales','fund':'Fundamentos de Matemáticas','geovec':'Geometría Vectorial y Analítica','disc':'Matemáticas Discretas','mn':'Métodos Numéricos'}
exec(open(S+'estudio/prereq.py').read())
lec=[]; stem2id={}
for pre in CPRE:
    for f in sorted(glob.glob(S+f'plantilla/{pre}-*.json')):
        d=json.load(open(f)); stem=f.split('/')[-1][:-5]
        if stem not in URLS or URLS[stem]=='PENDIENTE': continue
        stem2id[stem]=d['id']
        qs=[]
        P=d['pregunta']
        if P.get('encabezado'): h=P['encabezado']; hq=mt(h)
        else: h='Calcula $'+P['tex']+'$'; hq='Calcula <span data-tex="'+attr(P['tex'])+'"></span>'
        qs.append(dict(id=d['id']+'#p',lid=d['id'],t='mcq',h=h,hq=hq,hk=clave(hq),o=P['opciones'],c=P['correcta'],e=P.get('explicacion',''),er=P.get('errores'),sim=False))
        n=0
        for s in d['leer']['secciones']:
            for b in s['bloques']:
                if b['t']=='simulacro':
                    for q in b['preguntas']:
                        n+=1; hq=mt(q['texto'])
                        if q['tipo']=='mcq': qs.append(dict(id=d['id']+'#s%d'%n,lid=d['id'],t='mcq',h=q['texto'],hq=hq,hk=clave(hq),o=q['opciones'],c=q['correcta'],e=q.get('resumen',''),er=None,sim=True))
                        else: qs.append(dict(id=d['id']+'#s%d'%n,lid=d['id'],t='num',h=q['texto'],hq=hq,hk=clave(hq),r=q['respuesta'],tol=q.get('tolNum',0.001),e=q.get('resumen',''),sim=True))
        lec.append(dict(id=d['id'],curso=CPRE[pre],modulo=d['modulo'],titulo=d['titulo'],url='https://claude.ai/artifact/'+URLS[stem],q=qs,_stem=stem))
pr={}
for k,v in PREREQ.items():
    if k in stem2id: pr[stem2id[k]]=[stem2id[x] for x in v if x in stem2id]
for l in lec: l.pop('_stem')
def _orden(l):
    m=re.search(r'm(\d+)-l(\d+)$',l['id']); return (CURSOS.index(l['curso']),int(m.group(1)),int(m.group(2)))
lec.sort(key=_orden)
data=dict(lecciones=lec,prereq=pr,cursos=CURSOS)
t=open(S+'estudio/estudio.tpl.html').read()
css=open(S+'kx/katex-inline.css').read()
t=t.replace('/*KATEXCSS*/',css).replace('/*DATA*/',json.dumps(data,ensure_ascii=False,separators=(',',':')))
open(S+'estudio/estudio.html','w').write(t)
open(S+'estudio/estudio.test.html','w').write('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">'+t+'</body></html>')
print(len(lec),sum(len(l['q']) for l in lec),'preguntas',len(t)/1e6,'MB')
