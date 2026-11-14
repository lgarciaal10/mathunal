import json,glob,re,ast
S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/'
hub=open(S+'hub/build-hub.py').read()
URLS={}
for n,pre in [('URL','calculo'),('URL2','calcint'),('URL3','alglin'),('URL4','edo'),('URL6','matbas'),('URL7','fund'),('URL8','geovec'),('URL9','disc'),('URL10','mn'),('URL11','esp'),('URL12','cv')]:
    m=re.search(r'^'+n+r"=(\{.*?\})\s*$",hub,re.M|re.S)
    for k,v in ast.literal_eval(m.group(1)).items(): URLS[pre+'-'+k]=v
CP={'matbas':'Matemáticas Básicas','calculo':'Cálculo Diferencial','calcint':'Cálculo Integral','alglin':'Álgebra Lineal','edo':'Ecuaciones Diferenciales','fund':'Fundamentos de Matemáticas','geovec':'Geometría Vectorial y Analítica','disc':'Matemáticas Discretas','mn':'Métodos Numéricos','esp':'Matemáticas Especiales','cv':'Cálculo en Varias Variables'}
out=[]
for pre,cn in CP.items():
    for f in sorted(glob.glob(S+f'plantilla/{pre}-*.json')):
        d=json.load(open(f));stem=f.split('/')[-1][:-5]
        if stem not in URLS: continue
        eq=None;pasos=[]
        for s in d['leer']['secciones']:
            for b in s['bloques']:
                if b['t']=='eq' and eq is None: eq=b['tex']
                if b['t']=='pasos' and len(pasos)<4 and not pasos: pasos=[(i['tex'],i.get('porque','')) for i in b['items']]
        m=re.search(r'Lección (\d+) de',d['posicion'])
        out.append(dict(c=cn,m=d['modulo'],n=int(m.group(1)) if m else 0,t=d['titulo'],u='https://claude.ai/artifact/'+URLS[stem],eq=eq,p=pasos,r=d['resumen']))
mods=sorted(set((o['c'],o['m']) for o in out))
# orden de cursos y modulos por aparicion
order=list(CP.values())
out.sort(key=lambda o:(order.index(o['c']),o['m'],o['n']))
data=json.dumps(out,ensure_ascii=False)
tpl=open(S+'formulario/tpl.html').read()
css=open(S+'kx/katex-inline.css').read()
open(S+'formulario/formulario.html','w').write(tpl.replace('/*KATEXCSS*/',css).replace('/*DATA*/',data))
print(len(out),len(data))
