import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
TT=[round(-2.2+0.11*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(t),f"{t*t}*cos(2*x)"] for t in TT],"c":0},
    {"t":"segmento","a":["-2.2","0"],"b":["2.2","0"],"c":3}]
graf={"tipo":"plano","x":[-2.4,2.4],"y":[-5.2,5.2],"a":0,"b":3.14,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"curvatura del corte, coseno de 2 theta","formula":"cos(2*x)"},{"rotulo":"ángulo theta del plano de corte, en grados","formula":"57.2958*x"}],
 "etiquetas":["Si es positiva el corte abre hacia arriba, y si es negativa hacia abajo","El corte se hace con un plano vertical que gira alrededor del origen"],"etiquetaSlider":"Ángulo theta, de 0 a 3.14",
 "alt":"Se corta la superficie z igual a x al cuadrado menos y al cuadrado con un plano vertical que pasa por el origen y gira con el ángulo theta. El corte es una parábola de ecuación t al cuadrado por coseno de 2 theta. Con theta igual a 0 abre hacia arriba, con theta igual a pi medios hacia abajo, y con theta igual a pi cuartos es plano. Eso es un punto silla"}
glos={"critico":"Un punto crítico es un punto donde las dos derivadas parciales valen cero, o donde no existen.",
 "hessiano":"El hessiano es la matriz de segundas derivadas. Su determinante D igual a f sub x x por f sub y y menos f sub x y al cuadrado clasifica los puntos críticos.",
 "silla":"Un punto silla es un punto crítico que es mínimo en una dirección y máximo en otra.",
 "absoluto":"Un extremo absoluto es el mayor o el menor valor de la función en toda la región, y puede estar en la frontera."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es x al cuadrado menos y al cuadrado. Se corta con un plano vertical que gira alrededor del origen."],
 [4,10,"Con el ángulo en 0 el corte es la parábola x al cuadrado, que abre hacia arriba, como un mínimo."],
 [10,16,"Con el ángulo en pi cuartos el corte es plano, la curvatura es cero."],
 [16,20,"Con el ángulo en pi medios el corte es menos y al cuadrado, y abre hacia abajo, como un máximo."],
 [20,24,"Mínimo en una dirección y máximo en otra es lo que define un punto silla, y su discriminante D, el determinante del hessiano, es negativo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0.785],[13,0.785],[16,1.5708],[18,1.5708],[24,1.5708]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un {{gl:critico|punto crítico}} es donde el gradiente se anula. Para saber si es mínimo, máximo o {{gl:silla|silla}}, se usa el {{gl:hessiano|hessiano}}. Si D es positivo y f sub x x es positivo, es mínimo, y si D es negativo es silla. Los extremos {{gl:absoluto|absolutos}} en una región cerrada también pueden estar en la frontera.")),
 sec("Un ejemplo","Un ejemplo",P("La superficie x al cuadrado menos y al cuadrado es una silla. Gira el plano de corte y mira cómo cambia la curvatura."),EQ("f=x^{2}-y^{2},\\qquad D=f_{xx}f_{yy}-f_{xy}^{2}=(2)(-2)-0=-4"),{"t":"grafica","animar":"dibujar","alt":"El corte de la silla con un plano que gira"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si en un punto crítico D es negativo, ¿qué hay allí?","opciones":["Un punto silla","Un mínimo","Un máximo","Nada se puede concluir"],"correcta":"Un punto silla","bien":"Muy bien. Con D negativo siempre es un punto silla.","mal":"Con D negativo es un punto silla. Hay un mínimo en una dirección y un máximo en otra."}),
 sec("Girar el plano","Cortes",P("Mira el corte con theta igual a 0, 0.785, 1.2 y 1.57."),{"t":"acercando","ds":[0,0.785,1.2,1.5708],"alt":"El corte con cuatro ángulos"},P("En 0.785 el corte es una recta, y a partir de allí cambia de concavidad.")),
 sec("Hallar y clasificar","Clasificar",P("Primero se halla el punto crítico, y luego se clasifica con el hessiano."),
   PASOS([("f=x^{2}+y^{2}-4x","La función."),
          ("f_{x}=2x-4=0,\\quad f_{y}=2y=0","El gradiente igual a cero."),
          ("(x,y)=(2,0)","El punto crítico."),
          ("D=f_{xx}f_{yy}-f_{xy}^{2}=(2)(2)-0=4>0,\\ f_{xx}=2>0\\ \\Rightarrow\\ \\text{minimo}","Es un mínimo local.")]),
   OJO("Si D es cero el criterio no decide, y hay que estudiar la función de otra forma. Hay mínimos, máximos y sillas con D igual a cero.")),
 sec("La tabla de decisión","Tabla",P("El criterio del hessiano en un resumen."),
   PASOS([("D>0,\\ f_{xx}>0\\ \\Rightarrow\\ \\text{minimo local}","Abre hacia arriba en todas las direcciones."),
          ("D>0,\\ f_{xx}<0\\ \\Rightarrow\\ \\text{maximo local}","Abre hacia abajo en todas las direcciones."),
          ("D<0\\ \\Rightarrow\\ \\text{punto silla}","Cambia de concavidad según la dirección."),
          ("D=0\\ \\Rightarrow\\ \\text{no concluyente}","Se necesita otro método.")]),
   OJO("El signo de f sub x x decide entre mínimo y máximo, pero solo cuando D es positivo. Con D negativo el signo de f sub x x no importa.")),
 eng("El diseño de un depósito","El costo de material de un depósito abierto depende de su largo y su ancho para un volumen fijo. Se busca el diseño de menor costo, y el punto crítico de la función de costo lo da.","C(x,y)=xy+\\dfrac{2V}{x}+\\dfrac{2V}{y}",
   [("Variables","largo y ancho"),("Punto crítico","dos derivadas parciales iguales a cero"),("Clasificación","D positivo y f sub x x positivo, mínimo")],"Con el hessiano se confirma que el punto crítico es un mínimo y no una silla. Luego se compara con el costo en los bordes, porque el dominio es x e y positivos."),
 completar("En un punto crítico con D positivo y f sub x x positivo, hay un [[hueco]] local.","D>0,\\ f_{xx}>0\\ \\Rightarrow\\ [[hueco]]",
   [("\\text{minimo}","mínimo"),("\\text{maximo}","máximo"),("\\text{silla}","silla")],0,
   ["","El máximo es con f sub x x negativo.","La silla es con D negativo."],"Con f sub x x positivo la función abre hacia arriba.","Es un mínimo local."),
 error("Alguien clasificó el punto crítico de f igual a x al cuadrado menos y al cuadrado, y se equivocó. Toca el paso que está mal.",
   [("f_{xx}=2,\\ f_{yy}=-2,\\ f_{xy}=0","Segundas derivadas.","derivadas"),
    ("D=2+(-2)-0=0","Este paso es el que falla.","suma en lugar de multiplicar"),
    ("\\text{no concluyente}","Conclusión.","no concluyente")],1,
   "D es f sub x x por f sub y y menos f sub x y al cuadrado, o sea 2 por menos 2, que da menos 4. Como D es negativo, es un punto silla.",
   "D=(2)(-2)-0=-4<0","D usa un producto, y no una suma."),
 ordenar("Estos son los pasos para clasificar un punto crítico, pero están desordenados.",
   [("\\nabla f=0","Se iguala el gradiente a cero"),
    ("(a,b)","Se hallan los puntos críticos"),
    ("f_{xx},\\ f_{yy},\\ f_{xy}","Se calculan las segundas derivadas"),
    ("D=f_{xx}f_{yy}-f_{xy}^{2}","Se evalúa D")],[2,0,3,1],
   "Primero el gradiente, luego los puntos, después las segundas derivadas y al final D.","Se empieza igualando el gradiente a cero."),
]
S+=cierre("Mini simulacro de máximos y mínimos",[
 banco("cv_c1_14","D positivo y f sub x x positivo es un mínimo local."),
 banco("cv_c1_15","D negativo es un punto silla."),
 banco("cv_c1_16","El punto crítico de x al cuadrado más y al cuadrado menos 4x."),
 pnum("Para $f=x^{2}+3y^{2}$ en el origen, el valor de $D=f_{xx}f_{yy}-f_{xy}^{2}$ es:","12",0.01,"Con f sub x x igual a 2, f sub y y igual a 6 y f sub x y igual a 0, D es 12.")])
prac=[
 {"titulo":"La silla","grafica":{"draw":1},"bloques":[P("La función tiene un punto crítico en el origen."),EQ("f=x^{2}-y^{2}")]},
 {"titulo":"Gira el corte","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la curvatura del corte y el ángulo.")]},
 {"titulo":"Hacia abajo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.5708,"bloques":[EQ("\\cos2\\left(\\tfrac{\\pi}{2}\\right)=-1"),P("Con theta igual a pi medios el corte abre hacia abajo, y con theta igual a 0, hacia arriba.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.5708},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Mínimo en una dirección y máximo en otra es una silla."}]}]
preg={"tex":"f=x^{2}-y^{2}\\ \\text{en el origen hay}","opciones":["un punto silla","un mínimo local","un máximo local","un punto sin gradiente cero"],"correcta":0,
 "explicacion":"El gradiente es 2x, menos 2y, que vale cero en el origen. D es 2 por menos 2, o sea menos 4, que es negativo, así que es un punto silla.",
 "verificacion":{"formula":"2*(-2)-0+0*x","a":0,"esperado":-4},
 "pistas":["Halla el gradiente.","Calcula D con las segundas derivadas.","D es negativo."],
 "errores":["","Un mínimo pediría D y f sub x x positivos.","Un máximo pediría D positivo y f sub x x negativo.","El gradiente sí vale cero en el origen."]}
res=["Un punto crítico es donde el gradiente es cero, y el hessiano D lo clasifica.","D positivo con f sub x x positivo es mínimo, y D negativo es silla.","Con D igual a cero el criterio no decide."]
write(lesson("cv-m1-l6","Lección 6 de 7","Máximos y mínimos con el hessiano",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-hessiano.json")
