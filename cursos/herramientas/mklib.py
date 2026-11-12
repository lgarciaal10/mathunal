import json
import os
FU="Banco MathUNAL, simulacro de "+os.environ.get("CURSO_FU","Cálculo Integral")
P=lambda h:{"t":"p","html":h}
EQ=lambda t:{"t":"eq","tex":t}
PASOS=lambda items:{"t":"pasos","items":[{"tex":a,"porque":b} for a,b in items]}
OJO=lambda h:{"t":"ojo","html":h}
def sec(titulo,corto,*bl):
    d={"titulo":titulo}
    if corto: d["corto"]=corto
    d["bloques"]=list(bl); return d
def cierre(simtitle,preguntas):
    if not preguntas:
        return [sec("Revisa tu respuesta","Revisa",{"t":"pregunta"},{"t":"nota","html":"Puedes pedir pistas de a una. Si fallas, el mensaje te dice qué error se cometió."}),sec("Tu repaso","Repaso",{"t":"repaso"}),sec("En resumen","Resumen",{"t":"resumen"})]
    return [
     sec("Revisa tu respuesta","Revisa",{"t":"pregunta"},{"t":"nota","html":"Puedes pedir pistas de a una. Si fallas, el mensaje te dice qué error se cometió."}),
     sec("Mini simulacro","Simulacro",P("Tres preguntas reales del banco de MathUNAL sobre este tema. Responde sin mirar los pasos."),{"t":"simulacro","titulo":simtitle,"preguntas":preguntas}),
     sec("Tu repaso","Repaso",{"t":"repaso"}),
     sec("En resumen","Resumen",{"t":"resumen"})]
def mcq(texto,ops,c,res): return {"tipo":"mcq","texto":texto,"opciones":ops,"correcta":c,"resumen":res,"fuente":FU}
def num(texto,r,tol,res): return {"tipo":"numerica","texto":texto,"respuesta":r,"tolNum":tol,"resumen":res,"fuente":FU}
def eng(titulo,html,tex,datos,cierre_):
    d={"t":"ingenieria","titulo":titulo,"html":html}
    if tex: d["tex"]=tex
    d["datos"]=[{"k":k,"v":v} for k,v in datos]; d["cierre"]=cierre_; return sec("¿Para qué sirve?","En ingeniería",d)
def completar(enun,tex,ops,c,errs,pista,porque):
    return sec("Completa el paso","Completa",{"t":"completar","enunciado":enun,"tex":tex,"opciones":[{"tex":a,"txt":b} for a,b in ops],"correcta":c,"errores":errs,"pista":pista,"porque":porque})
def error(enun,pasos,mal,expl,corr,pista):
    return sec("Encuentra el error","Error",{"t":"error","enunciado":enun,"pasos":[{"tex":a,"porque":b,"txt":c} for a,b,c in pasos],"mal":mal,"explicacion":expl,"correccion":corr,"pista":pista})
def ordenar(enun,pasos,mezcla,porque,pista):
    # pasos: lista de (tex, txt) en el orden correcto
    return sec("Ordena los pasos","Ordena",{"t":"ordenar","enunciado":enun,"pasos":[a for a,b in pasos],"mezcla":mezcla,"porque":porque,"pista":pista,"txt":[b for a,b in pasos]})
def lesson(id_,posicion,titulo,minutos,graf,glos,ver,secciones,prac,preg,resumen,modulo="Módulo 1 Integral definida y técnicas básicas",ejercicios=7,curso="Cálculo Integral"):
    return {"esquema":1,"id":id_,"ejemplo":True,"curso":curso,"modulo":modulo,"posicion":posicion,"titulo":titulo,"minutos":minutos,"ejercicios":ejercicios,"grafica":graf,"glosario":glos,"ver":ver,"leer":{"secciones":secciones},"practicar":{"pasos":prac},"pregunta":preg,"resumen":resumen}
def write(L,name):
    json.dump(L,open(name,'w'),ensure_ascii=False,indent=1)

def M(*c):
    n=int(len(c)**0.5+0.5); rows=[c[i*n:(i+1)*n] for i in range(n)]
    return "\\begin{pmatrix}"+"\\\\".join("&".join(str(v) for v in r) for r in rows)+"\\end{pmatrix}"
_BANCO=None
def banco(i,resumen=None):
    """arma una pregunta del simulacro con el registro del banco, sacado de bank/alglin-todo.json"""
    global _BANCO
    if _BANCO is None:
        _d=os.path.dirname(os.path.abspath(__file__)); _n=os.environ.get('BANCO','alglin'); _p=[os.path.join(_d,'..','bank',_n+'-todo.json'),os.path.join(_d,'..','datos',_n+'-banco.json')]
        _BANCO={q['id']:q for v in json.load(open(next(p for p in _p if os.path.exists(p)))).values() for q in v}
    q=_BANCO[i]
    if q['tipo']=='mcq': return mcq(q['texto'],q['opciones'],q['correcta'],resumen or q.get('resumen') or '')
    return num(q['texto'],str(q['respuesta']),q.get('tolNum') or 0.001,resumen or q.get('resumen') or '')

def MC(n,*c):
    rows=[c[i:i+n] for i in range(0,len(c),n)]
    return "\\begin{pmatrix}"+"\\\\".join("&".join(str(v) for v in r) for r in rows)+"\\end{pmatrix}"

import math as _m
def campo(fm,xr,yr,nx,ny,d,margen=0.05):
    """segmentos del campo de pendientes. fm(x,y) da la pendiente. xr e yr son las ventanas"""
    el=[]
    for i in range(nx):
        for j in range(ny):
            x0=xr[0]+(xr[1]-xr[0])*(i+0.5)/nx; y0=yr[0]+(yr[1]-yr[0])*(j+0.5)/ny
            try: m=fm(x0,y0)
            except Exception: continue
            if m is None or _m.isnan(m): continue
            n=_m.hypot(1,m); ax,ay,bx,by=x0-d/n,y0-d*m/n,x0+d/n,y0+d*m/n
            if all(xr[0]+margen<v<xr[1]-margen for v in (ax,bx)) and all(yr[0]+margen<v<yr[1]-margen for v in (ay,by)):
                el.append({"t":"segmento","a":[f"{ax:.4f}",f"{ay:.4f}"],"b":[f"{bx:.4f}",f"{by:.4f}"],"c":0})
    return el
def trazo(f,x0,x1,n,c=2):
    """curva dada por una función de xk (cadena con {x} para el valor y x del parámetro)"""
    return {"t":"trazo","puntos":[[f"{x0+(x1-x0)*k/n:.4f}",f.replace("{x}",f"({x0+(x1-x0)*k/n:.4f})")] for k in range(n+1)],"c":c}
