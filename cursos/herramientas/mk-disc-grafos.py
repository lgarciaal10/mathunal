import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 3 Recurrencias, grafos y teoría de números"
R=3.0; NV=7
C=[round(R*math.cos(2*math.pi*j/NV),5) for j in range(NV)]
Sn=[round(R*math.sin(2*math.pi*j/NV),5) for j in range(NV)]
IND=[lagr([1 if xx>j else 0 for xx in range(NV+1)]) for j in range(NV)]
def VP(j):
    return (f"{C[0]}+({IND[j]})*({C[j]-C[0]:.5f})", f"{Sn[0]}+({IND[j]})*({Sn[j]-Sn[0]:.5f})")
EL=[]
for i in range(NV):
    for j in range(i+1,NV):
        ax=f"{C[0]}+({IND[j]})*({C[i]-C[0]:.5f})"; ay=f"{Sn[0]}+({IND[j]})*({Sn[i]-Sn[0]:.5f})"
        bx,by=VP(j)
        EL.append({"t":"segmento","a":[ax,ay],"b":[bx,by],"c":0})
for j in range(NV):
    px,py=VP(j)
    EL.append({"t":"punto","p":[px,py],"c":2 if j else 1})
graf={"tipo":"plano","x":[-8.1,8.1],"y":[-4.4,4.4],"a":2,"b":7,"inicio":5,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"aristas del grafo completo con n vértices","formula":"x*(x-1)/2"},{"rotulo":"suma de los grados, el doble de las aristas","formula":"x*(x-1)"}],
 "etiquetas":["Número de aristas, n por n menos 1 entre 2","Suma de los grados de todos los vértices"],"etiquetaSlider":"Número de vértices n, de 2 a 7",
 "alt":"El grafo completo con n vértices puestos en un círculo, y una arista entre cada par de vértices. Con 5 vértices hay 10 aristas, y con 7 vértices hay 21 aristas"}
glos={"grafo":"Un grafo es un conjunto de vértices unidos por aristas. Se usa para modelar redes y relaciones.",
 "grado":"El grado de un vértice es el número de aristas que llegan a él.",
 "completo":"El grafo completo K de n tiene n vértices y una arista entre cada par de ellos. Tiene n por n menos 1 entre 2 aristas.",
 "arbol":"Un árbol es un grafo conexo sin ciclos. Con n vértices tiene exactamente n menos 1 aristas.",
 "euleriano":"Un circuito euleriano recorre cada arista exactamente una vez y vuelve al inicio. Existe en un grafo conexo si y solo si todos los vértices tienen grado par."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Cada punto es un vértice y cada segmento es una arista. Este es el grafo completo, donde todos los vértices están unidos."],
 [4,9,"Con 3 vértices hay 3 aristas, y con 4 vértices hay 6."],
 [9,14,"Con 5 vértices hay 10 aristas. Cada vértice tiene grado 4."],
 [14,19,"La suma de los grados es el doble de las aristas, porque cada arista toca dos vértices."],
 [19,22,"Con 7 vértices hay 21 aristas, y todos los vértices tienen grado 6, que es par, así que hay un circuito euleriano."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,2],[6,3],[8,4],[10,5],[16,5],[17,7],[22,7]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[9,22]}}
S=[
 sec("La idea",None,P("Un {{gl:grafo|grafo}} tiene vértices y aristas, y sirve para modelar redes. El {{gl:grado|grado}} de un vértice cuenta sus aristas. El grafo {{gl:completo|completo}} une todos los pares. Un {{gl:arbol|árbol}} es un grafo conexo sin ciclos. Y un circuito {{gl:euleriano|euleriano}} recorre cada arista una sola vez.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el grafo completo con n vértices. Cada par de vértices tiene una arista."),EQ("|E|=\\dbinom{n}{2}=\\dfrac{n(n-1)}{2}"),{"t":"grafica","animar":"dibujar","alt":"El grafo completo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En el grafo completo con 4 vértices, cada vértice se une con los otros 3. Si se suman los grados, ¿cuánto da?","opciones":[7,8,12,16],"correcta":12,"bien":"Muy bien. Es 4 por 3, o sea 12, que es el doble de las 6 aristas. Más abajo se ve.","mal":"Es 12, porque son 4 vértices con grado 3 cada uno. Es el doble de las 6 aristas. Más abajo se ve."}),
 sec("Añadiendo vértices","Los vértices",P("Mira el grafo completo con 3, 4, 5 y 7 vértices."),{"t":"acercando","ds":[3,4,5,7],"alt":"El grafo completo con cuatro cantidades de vértices"},P("Con 5 vértices hay 10 aristas, y con 7 hay 21.")),
 sec("Grados y aristas","Grados",P("Cada arista toca dos vértices, y eso relaciona los grados con el número de aristas."),
   PASOS([("\\displaystyle\\sum_{v}\\deg(v)=2\\,|E|","Lema del apretón de manos."),
          ("K_{5}:\\ 5\\cdot4=20=2\\cdot10","En K5 hay 10 aristas, y la suma de los grados es 20."),
          ("|E|=\\dfrac{n(n-1)}{2}","Las aristas del grafo completo."),
          ("\\text{árbol con}\\ n\\ \\text{vértices}\\ \\Rightarrow\\ n-1\\ \\text{aristas}","Los árboles tienen la menor cantidad de aristas para estar conectados.")]),
   OJO("La suma de los grados siempre es par. Por eso no existe un grafo con un número impar de vértices de grado impar.")),
 sec("Circuitos eulerianos","Euler",P("Un circuito euleriano pasa por todas las aristas una sola vez."),
   PASOS([("\\text{conexo y todos los grados pares}\\ \\Leftrightarrow\\ \\text{circuito euleriano}","El criterio de Euler."),
          ("K_{5}:\\ \\text{grado}\\ 4\\ \\text{en cada vértice}","Todos son pares, así que K5 tiene circuito euleriano."),
          ("K_{4}:\\ \\text{grado}\\ 3\\ \\text{en cada vértice}","Son impares, y K4 no lo tiene.")]),
   OJO("Hace falta que el grafo sea conexo. Si tiene dos partes separadas no hay circuito que las recorra a las dos.")),
 eng("Una red de computadores","En una red de 8 equipos donde cada uno se conecta con todos los demás hacen falta 28 cables. Una red en forma de árbol conecta los 8 equipos con 7 cables. Las dos son grafos, pero con una cantidad de aristas muy diferente.","\\dbinom{8}{2}=28,\\qquad n-1=7",
   [("Equipos","8"),("Cables si todos se unen","28"),("Cables en árbol","7")],"Unir todos con todos da mucha redundancia, pero cuesta cuatro veces más cables. El árbol es lo más barato, pero si un cable falla se desconecta una parte. En el diseño de redes se elige un punto intermedio, con unos pocos ciclos. Entender cuántas aristas cuesta cada diseño permite estimar costos antes de instalar."),
 completar("Se completa el lema del apretón de manos.","\\displaystyle\\sum_{v}\\deg(v)=[[hueco]]\\cdot|E|",
   [("2","dos"),("1","uno"),("|V|","la cantidad de vértices")],0,
   ["","Con uno se contaría cada arista una sola vez, pero cada arista toca dos vértices.","La cantidad de vértices no interviene, y la suma de grados depende de las aristas."],"Cada arista aporta a dos grados.","Cada arista se cuenta una vez en cada uno de sus dos extremos."),
 error("Alguien contó las aristas de K5 y se equivocó en un paso. Toca el paso que está mal.",
   [("K_{5}\\ \\text{tiene 5 vértices}","El dato.","K5 tiene 5 vértices"),
    ("\\text{cada vértice se une con 4 más}","El grado de cada vértice.","cada vértice tiene grado 4"),
    ("\\text{Entonces hay}\\ 5\\cdot4=20\\ \\text{aristas}","Este paso es el que falla.","hay 20 aristas")],2,
   "El producto 5 por 4 cuenta cada arista dos veces, una desde cada extremo, y es la suma de grados. Las aristas son la mitad, o sea 10.",
   "|E|=\\dfrac{5\\cdot4}{2}=10","Piensa cuántas veces se cuenta cada arista."),
 ordenar("Estos son los pasos para decidir si un grafo tiene un circuito euleriano, pero están desordenados.",
   [("\\text{se calcula el grado de cada vértice}","Se calculan los grados"),
    ("\\text{todos los grados son pares}","Se verifica que son pares"),
    ("\\text{el grafo es conexo}","Se verifica que es conexo"),
    ("\\text{hay circuito euleriano}","Se concluye")],[2,0,3,1],
   "Se calculan los grados, se verifica que son pares, se verifica que es conexo y se concluye.","Se empieza calculando los grados."),
]
S+=cierre("Mini simulacro de teoría de grafos",[
 banco("di_c3_02","La suma de los grados es el doble del número de aristas."),
 banco("di_c3_09","$\\binom{5}{2}=10$ aristas."),
 banco("di_c3_10","Un grafo conexo tiene un circuito euleriano si todos sus vértices tienen grado par.")])
prac=[
 {"titulo":"El grafo completo","grafica":{"draw":1},"bloques":[P("Un grafo con una arista entre cada par de vértices."),EQ("|E|=\\dfrac{n(n-1)}{2}")]},
 {"titulo":"Añade vértices","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 2 a 7. Abajo se leen las aristas y la suma de los grados.")]},
 {"titulo":"Con 5 vértices","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("\\dfrac{5\\cdot4}{2}=10"),P("Con 5 vértices hay 10 aristas y la suma de los grados es 20.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"La suma de los grados es el doble de las aristas."}]}]
preg={"tex":"\\text{Un grafo de 6 vértices con grados 3, 3, 2, 2, 2 y 2 tiene cuántas aristas}","opciones":["$7$","$14$","$6$","$12$"],"correcta":0,
 "explicacion":"La suma de los grados es 3 más 3 más 2 más 2 más 2 más 2, o sea 14. Como la suma de los grados es el doble de las aristas, el grafo tiene 7 aristas.",
 "verificacion":{"formula":"(3+3+2+2+2+2)/2+0*x","a":0,"esperado":7},
 "pistas":["Suma los grados.","Da 14.","Las aristas son la mitad."],
 "errores":["","Catorce es la suma de los grados, que es el doble de las aristas.","Seis es el número de vértices, y no el de aristas.","Doce sale de una suma mal hecha. Suma los seis grados, 3 más 3 más 2 más 2 más 2 más 2."]}
res=["En todo grafo, la suma de los grados es el doble del número de aristas.","El grafo completo con n vértices tiene n por n menos 1 entre 2 aristas, y un árbol tiene n menos 1.","Un grafo conexo tiene circuito euleriano si y solo si todos sus vértices tienen grado par."]
write(lesson("di-m3-l2","Lección 2 de 4","Teoría de grafos",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-grafos.json")
