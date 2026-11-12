import json
FU="Banco MathUNAL, simulacro de Cálculo Integral"
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
def lesson(id_,posicion,titulo,minutos,graf,glos,ver,secciones,prac,preg,resumen,modulo="Módulo 1 Integral definida y técnicas básicas",ejercicios=7):
    return {"esquema":1,"id":id_,"ejemplo":True,"curso":"Cálculo Integral","modulo":modulo,"posicion":posicion,"titulo":titulo,"minutos":minutos,"ejercicios":ejercicios,"grafica":graf,"glosario":glos,"ver":ver,"leer":{"secciones":secciones},"practicar":{"pasos":prac},"pregunta":preg,"resumen":resumen}
def write(L,name):
    json.dump(L,open(name,'w'),ensure_ascii=False,indent=1)
