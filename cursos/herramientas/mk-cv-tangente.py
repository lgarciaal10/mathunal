import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
XS=[round(-0.5+0.1*i,3) for i in range(36)]
EL=[{"t":"trazo","puntos":[[str(xv),f"{xv*xv+1:.4f}"] for xv in XS],"c":0},
    {"t":"recta","p":["1","2"],"dir":["1","2"],"c":1},
    {"t":"segmento","a":["x","2*x"],"b":["x","x*x+1"],"c":3},
    {"t":"punto","p":["x","x*x+1"],"c":0},
    {"t":"punto","p":["x","2*x"],"c":1}]
graf={"tipo":"plano","x":[-0.5,3.1],"y":[-0.5,8.4],"a":0,"b":2.7,"inicio":1.5,"elementos":EL,
 "lecturas":[{"rotulo":"valor real f de x y 1, igual a x al cuadrado más 1","formula":"x*x+1"},{"rotulo":"aproximación del plano tangente, igual a 2 x","formula":"2*x"}],
 "etiquetas":["La superficie, cortada por el plano y igual a 1","El plano tangente en 1, 1, que se ve como una recta"],"etiquetaSlider":"Posición x, de 0 a 2.7",
 "alt":"El corte de z igual a x al cuadrado más y al cuadrado con el plano y igual a 1 es una parábola, y el plano tangente en el punto 1, 1, 2 deja una recta tangente. Cerca de x igual a 1 la recta y la parábola casi coinciden, y lejos se separan. El segmento muestra el error de la aproximación"}
glos={"tangente":"El plano tangente a una superficie en un punto es el plano que mejor se pega a la superficie cerca de ese punto.",
 "linealizacion":"La linealización de f en el punto a b es la función lineal L de x y igual a f de a b más las derivadas parciales por los incrementos.",
 "diferencial":"La diferencial total es df igual a f sub x dx más f sub y dy, y estima el cambio de f para cambios pequeños en x y en y.",
 "error":"El error de la aproximación lineal es la diferencia entre el valor real y la linealización, y crece como el cuadrado de la distancia al punto."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La superficie z igual a x al cuadrado más y al cuadrado se corta con el plano y igual a 1, y queda una parábola."],
 [4,10,"El plano tangente en el punto 1, 1, 2 deja una recta tangente, de ecuación 2 x."],
 [10,16,"Con x igual a 1.1 el valor real es 2.21 y la aproximación es 2.2, muy cerca."],
 [16,20,"Con x igual a 2 el valor real es 5 y la aproximación es 4. El error crece."],
 [20,24,"Por eso la linealización sirve solo cerca del punto de tangencia."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,1.1],[13,1.1],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El {{gl:tangente|plano tangente}} es el equivalente en dos variables de la recta tangente. Con él se arma la {{gl:linealizacion|linealización}}, que aproxima la función cerca de un punto. Su uso más común es la {{gl:diferencial|diferencial}}, para estimar cambios pequeños. El {{gl:error|error}} crece con el cuadrado de la distancia.")),
 sec("Un ejemplo","Un ejemplo",P("La función es x al cuadrado más y al cuadrado, y el punto de tangencia es 1, 1. Mueve la posición x y mira el error."),EQ("z=x^{2}+y^{2},\\qquad L(x,y)=2x+2y-2"),{"t":"grafica","animar":"dibujar","alt":"La parábola de corte y la recta del plano tangente"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La función f vale x al cuadrado más y al cuadrado. ¿Cuánto vale f en el punto 1, 1?","opciones":[2,1,4,0],"correcta":2,"bien":"Muy bien. Vale 2, y es la altura del plano tangente en el punto.","mal":"f de 1, 1 es 1 más 1, o sea 2. Esa es la altura del plano tangente en el punto."}),
 sec("Cerca y lejos","Error",P("Mira la aproximación con x igual a 1.1, 1.5, 2 y 2.5."),{"t":"acercando","ds":[1.1,1.5,2,2.5],"alt":"La aproximación en cuatro posiciones"},P("Cerca de x igual a 1 el error es pequeño, y a 2.5 ya pasa de 2.")),
 sec("El plano tangente","Plano",P("Se calcula con el valor de la función y las dos derivadas parciales en el punto."),
   PASOS([("f(1,1)=2,\\quad f_{x}=2x=2,\\quad f_{y}=2y=2","Valor y derivadas parciales en el punto."),
          ("z=f(a,b)+f_{x}(a,b)(x-a)+f_{y}(a,b)(y-b)","La fórmula del plano tangente."),
          ("z=2+2(x-1)+2(y-1)","Se reemplazan los valores."),
          ("z=2x+2y-2","Se simplifica.")]),
   OJO("El plano tangente pasa por el punto de la superficie, y por eso lleva el término f de a, b. Si se olvida, el plano queda a la altura equivocada.")),
 sec("Linealización y diferencial","Linealización",P("La linealización estima valores cerca del punto, y la diferencial estima el cambio."),
   PASOS([("L(x,y)=2x+2y-2","La linealización en 1, 1."),
          ("L(1.1,\\,0.9)=2.2+1.8-2=2","Una estimación del valor en 1.1, 0.9."),
          ("f(1.1,\\,0.9)=1.21+0.81=2.02","El valor real."),
          ("df=2\\,dx+2\\,dy=2(0.1)+2(-0.1)=0","La diferencial estima un cambio de 0, y el real fue 0.02.")]),
   OJO("La diferencial estima el cambio a primer orden. El error es de segundo orden, y por eso, si los incrementos son pequeños, sale despreciable.")),
 eng("Un error de medición en un área","Se mide un rectángulo de 10 por 20 centímetros con un error de 0.1 centímetros en cada lado. La diferencial estima el error del área sin hacer el cálculo exacto.","A=xy,\\quad dA=y\\,dx+x\\,dy=20(0.1)+10(0.1)=3\\ \\text{cm}^{2}",
   [("Área","200 cm²"),("Error por la diferencial","cerca de 3 cm²"),("Error relativo","cerca de 1.5 por ciento")],"La diferencial total es la herramienta estándar para propagar errores de medición. Con ella se decide qué medida conviene hacer con más cuidado, la que más peso tiene en el error."),
 completar("El plano tangente a f en el punto a, b tiene la forma z igual a f de a, b más f sub x por x menos a más [[hueco]].","z=f(a,b)+f_{x}(a,b)(x-a)+[[hueco]]",
   [("f_{y}(a,b)(y-b)","f sub y por y menos b"),("f_{y}(a,b)\\,y","f sub y por y"),("f_{xy}(a,b)","la derivada mixta")],0,
   ["","Sin el menos b, el plano no pasa por el punto de tangencia.","La derivada mixta no es la pendiente en la dirección y."],"Cada pendiente se multiplica por el incremento de su variable.","Falta el término con y."),
 error("Alguien halló el plano tangente a z igual a x al cuadrado más y al cuadrado en 1, 1, y se equivocó. Toca el paso que está mal.",
   [("f_{x}=2x=2,\\ f_{y}=2y=2","Derivadas parciales.","derivadas"),
    ("z=2(x-1)+2(y-1)","Este paso es el que falla.","falta f de 1, 1"),
    ("z=2x+2y-4","Resultado.","da 2x más 2y menos 4")],1,
   "Falta el valor de la función en el punto, que es 2. Entonces z es 2 más 2 por x menos 1 más 2 por y menos 1, o sea 2x más 2y menos 2.",
   "z=2+2(x-1)+2(y-1)=2x+2y-2","Suma f de 1, 1."),
 ordenar("Estos son los pasos para hallar un plano tangente, pero están desordenados.",
   [("f(a,b)","Se evalúa la función en el punto"),
    ("f_{x}(a,b),\\ f_{y}(a,b)","Se evalúan las derivadas parciales"),
    ("z=f(a,b)+f_{x}(x-a)+f_{y}(y-b)","Se arma el plano"),
    ("z=2x+2y-2","Se simplifica")],[2,0,3,1],
   "Se evalúa la función, las derivadas, se arma el plano y se simplifica.","Se empieza con el valor de la función."),
]
S+=cierre("Mini simulacro de plano tangente",[
 banco("cv_c1_04","El plano tangente a x al cuadrado más y al cuadrado en 1, 1, 2."),
 banco("cv_c1_13","La fórmula del plano tangente."),
 pnum("Con la linealización $L(x,y)=2x+2y-2$, el valor aproximado en el punto $(1.1,\\,0.9)$ es (decimal, 1 cifra):","2.0",0.01,"L de 1.1 y 0.9 es 2.2 más 1.8 menos 2, o sea 2.0.")])
prac=[
 {"titulo":"La superficie","grafica":{"draw":1},"bloques":[P("Se corta con el plano y igual a 1."),EQ("z=x^{2}+y^{2}")]},
 {"titulo":"Mueve el punto","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el valor real y la aproximación del plano tangente.")]},
 {"titulo":"Con x igual a 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("f=5,\\quad L=4"),P("Con x igual a 2 el error es 1, y la aproximación ya no es buena.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"La linealización sirve cerca del punto de tangencia."}]}]
preg={"tex":"z=x^{2}+y^{2}\\ \\text{en}\\ (1,1,2).\\ \\text{El plano tangente es}","opciones":["$z=2x+2y-2$","$z=2x+2y+2$","$z=x+y$","$z=2x+2y$"],"correcta":0,
 "explicacion":"Se usa z igual a 2 más 2 por x menos 1 más 2 por y menos 1, que se simplifica en 2x más 2y menos 2.",
 "verificacion":{"formula":"2*1+2*1-2+0*x","a":0,"esperado":2},
 "pistas":["Calcula las dos derivadas parciales en 1, 1.","Usa la fórmula con f de a, b.","El plano debe valer 2 en el punto 1, 1."],
 "errores":["","El signo del término constante no es más 2, porque en 1, 1 daría 6.","En 1, 1 daría 2, pero la pendiente no es 1.","En 1, 1 daría 4, y debe dar 2."]}
res=["El plano tangente es z igual a f de a, b más f sub x por x menos a más f sub y por y menos b.","La linealización aproxima la función cerca del punto, y el error crece con el cuadrado de la distancia.","La diferencial total estima cambios pequeños de la función."]
write(lesson("cv-m1-l3","Lección 3 de 7","Plano tangente y linealización",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-tangente.json")
