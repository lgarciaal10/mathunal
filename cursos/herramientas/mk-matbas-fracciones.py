import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 1 Álgebra y expresiones"
def tr(a,b,n):
    return {"t":"trazo","puntos":[[f"{a+(b-a)*k/n:.4f}",f"({a+(b-a)*k/n:.4f}+2)/({a+(b-a)*k/n:.4f}+1)"] for k in range(n+1)],"c":2}
graf={"tipo":"plano","x":[-4.5,5.5],"y":[-3,7],"a":0,"b":4.5,"inicio":0,
 "elementos":[tr(-4.5,-1.05,40),tr(-0.93,1.96,50),tr(2.04,5.5,60),
  {"t":"recta","p":["-1","0"],"dir":["0","1"],"guion":True,"c":3,"guia":True},
  {"t":"recta","p":["2","0"],"dir":["0","1"],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":["x","(x+2)/(x+1)"],"c":1}],
 "lecturas":[{"rotulo":"valor de x","formula":"x"},{"rotulo":"(x+2)/(x+1)","formula":"(x+2)/(x+1)"}],
 "etiquetas":["Valor de x","Valor de la fracción simplificada"],"etiquetaSlider":"Valor de x",
 "alt":"La gráfica de x más 2 sobre x más 1, con una asíntota vertical en x igual a menos 1 y un hueco en x igual a 2, donde la fracción original x al cuadrado menos 4 sobre x al cuadrado menos x menos 2 no está definida"}
glos={"algebraica":"Una fracción algebraica es un cociente de polinomios, como x más 2 sobre x más 1.",
 "simplificar":"Simplificar una fracción es cancelar los factores comunes del numerador y del denominador. Solo se cancelan factores, no términos que se suman.",
 "dominio":"El dominio de una fracción algebraica son los valores de x para los que el denominador no vale 0."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Esta es la gráfica de x al cuadrado menos 4, sobre x al cuadrado menos x menos 2."],
 [4,8,"El numerador y el denominador tienen un factor común, x menos 2. Al cancelarlo queda x más 2 sobre x más 1."],
 [8,14,"La curva es la de x más 2 sobre x más 1, con un hueco en x igual a 2, donde la fracción original no está definida. Mueve el punto para verlo."],
 [14,18,"En x igual a 3 la fracción vale 1.25. Cuanto más grande es x, más se acerca a 1."],
 [18,22,"En x igual a 2 el punto cae en el hueco, a la altura 1.33. La fracción simplificada sí vale eso, pero la original no existe ahí."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[11,3],[17,3],[18,2],[22,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Las {{gl:algebraica|fracciones algebraicas}} se manejan igual que las numéricas. Se factoriza para {{gl:simplificar|simplificar}}, se busca un denominador común para sumar, y se invierte para dividir. Lo que hay que cuidar es el {{gl:dominio|dominio}}, porque los valores que anulan un denominador nunca se permiten.")),
 sec("Un ejemplo","Un ejemplo",P("Esta fracción parece complicada, pero tiene un factor repetido."),EQ("\\dfrac{x^{2}-4}{x^{2}-x-2}=\\dfrac{(x-2)(x+2)}{(x-2)(x+1)}"),{"t":"grafica","animar":"dibujar","alt":"La gráfica de la fracción"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En una fracción, el factor x menos 2 se puede cancelar arriba y abajo. ¿Qué valor de x hay que excluir del dominio?","opciones":[0,1,2,-2],"correcta":2,"bien":"Muy bien. Hay que excluir x igual a 2, porque ahí el denominador original vale 0. Más abajo se ve el hueco.","mal":"Hay que excluir x igual a 2, porque ahí x menos 2 vale 0. Más abajo se ve el hueco."}),
 sec("Moviendo el punto","Moviendo x",P("Mira el valor de la fracción simplificada en varios puntos."),{"t":"acercando","ds":[0,1,3,2],"alt":"El valor de la fracción en varios x"},P("Con x igual a 2 la fracción simplificada vale 4 tercios, pero la original no está definida. Por eso la gráfica tiene un hueco.")),
 sec("Simplificar","Simplificar",P("Se factoriza todo y se cancelan los factores comunes."),
   PASOS([("\\dfrac{x^{2}-4}{x^{2}-x-2}=\\dfrac{(x-2)(x+2)}{(x-2)(x+1)}","Se factorizan el numerador y el denominador."),
          ("=\\dfrac{x+2}{x+1},\\quad x\\ne 2,\\ x\\ne -1","Se cancela el factor x menos 2, y se recuerdan los valores excluidos.")]),
   OJO("Solo se cancelan factores, no términos. En x más 3 sobre x no se puede cancelar la x, porque el 3 se suma.")),
 sec("Sumar y dividir","Operaciones",P("Para sumar se busca un denominador común. Para dividir se multiplica por el inverso."),
   PASOS([("\\dfrac{1}{x}+\\dfrac{1}{x+1}=\\dfrac{(x+1)+x}{x(x+1)}=\\dfrac{2x+1}{x(x+1)}","Cada fracción se escribe con el denominador común x por x más 1."),
          ("\\dfrac{x^{2}-1}{x}\\div\\dfrac{x-1}{x^{2}}=\\dfrac{(x-1)(x+1)}{x}\\cdot\\dfrac{x^{2}}{x-1}","Dividir es multiplicar por el inverso."),
          ("=x(x+1)=x^{2}+x","Se cancelan x menos 1 y una x.")])),
 eng("Resistencias en paralelo","Cuando dos resistencias se conectan en paralelo, la resistencia total sale de sumar los inversos. Es una suma de fracciones.","\\dfrac{1}{R}=\\dfrac{1}{R_{1}}+\\dfrac{1}{R_{2}}\\ \\Rightarrow\\ R=\\dfrac{R_{1}R_{2}}{R_{1}+R_{2}}",
   [("R1","6 ohmios"),("R2","12 ohmios"),("Total","4 ohmios")],"Con 6 y 12 ohmios, la suma de inversos es un sexto más un doceavo, que es un cuarto, y la resistencia total es 4 ohmios. Siempre es menor que la más pequeña de las dos, porque la corriente tiene dos caminos. Es un modelo ideal, que supone cables sin resistencia."),
 completar("Se suman dos fracciones con el denominador común x por x más 1.","\\dfrac{1}{x}+\\dfrac{1}{x+1}=\\dfrac{[[hueco]]}{x(x+1)}",
   [("2x+1","dos x más uno"),("2","dos"),("x+2","x más dos")],0,
   ["","Con 2 arriba se estaría sumando 1 más 1, pero los denominadores son distintos y hay que multiplicar.","Con x más 2 se sumaron mal los numeradores. Cada uno se multiplica por el factor que le falta al denominador."],"A la primera fracción le falta el factor x más 1, y a la segunda le falta x.","Queda x más 1 más x, que es 2x más 1."),
 error("Alguien simplificó una fracción y se equivocó en un paso. Toca el paso que está mal.",
   [("\\dfrac{x^{2}-9}{x^{2}-3x}=\\dfrac{(x-3)(x+3)}{x(x-3)}","Se factoriza.","se factoriza arriba y abajo"),
    ("=\\dfrac{x+3}{x}","Se cancela x menos 3.","se cancela el factor x menos 3 y queda x más 3 sobre x"),
    ("=1+3=4","Este paso es el que falla.","se cancela la x con el 3 y queda 4")],2,
   "La x de abajo no es un factor del numerador. En x más 3 la x se suma con el 3, así que no se puede cancelar. El resultado se deja como x más 3 sobre x, o como 1 más 3 sobre x.",
   "\\dfrac{x+3}{x}=1+\\dfrac{3}{x}","Recuerda que solo se cancelan factores."),
 ordenar("Estos son los pasos para restar 2 sobre x menos 1 sobre x más 2, pero están desordenados.",
   [("\\dfrac{2}{x}-\\dfrac{1}{x+2}","La resta original"),
    ("\\dfrac{2(x+2)}{x(x+2)}-\\dfrac{x}{x(x+2)}","Se usa el denominador común"),
    ("\\dfrac{2x+4-x}{x(x+2)}","Se resta"),
    ("\\dfrac{x+4}{x(x+2)}","Se reducen términos")],[2,0,3,1],
   "Se escribe con denominador común, se restan los numeradores y se reducen términos.","Se empieza con la resta original."),
]
S+=cierre("Mini simulacro de fracciones algebraicas",[
 banco("mb_c1_11","Se factoriza $x^2-4=(x-2)(x+2)$ y $x^2-x-2=(x-2)(x+1)$, y se cancela $x-2$."),
 banco("mb_c1_12","Con denominador común $x(x+1)$, el numerador es $(x+1)+x=2x+1$."),
 banco("mb_c1_13","Se multiplica por el inverso, y queda $\\dfrac{(x-1)(x+1)}{x}\\cdot\\dfrac{x^2}{x-1}=x^2+x$.")])
prac=[
 {"titulo":"La fracción","grafica":{"draw":1,"guide":1},"bloques":[P("La curva de la fracción simplificada, con un hueco en x igual a 2."),EQ("\\dfrac{x^{2}-4}{x^{2}-x-2}")]},
 {"titulo":"Mueve el punto","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el valor de la fracción simplificada.")]},
 {"titulo":"El hueco","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("x=2\\ \\Rightarrow\\ \\dfrac{x+2}{x+1}=\\dfrac{4}{3}"),P("En x igual a 2 la fracción original no existe, pero la simplificada vale 1.33.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Factoriza arriba y abajo antes de cancelar."}]}]
preg={"tex":"\\dfrac{x^{2}-1}{x^{2}+x}\\ \\text{se simplifica como}","opciones":["$\\dfrac{x-1}{x}$","$\\dfrac{x-1}{x+1}$","$\\dfrac{1}{x}$","$-1$"],"correcta":0,
 "explicacion":"El numerador es x menos 1 por x más 1, y el denominador es x por x más 1. Se cancela x más 1 y queda x menos 1 sobre x, con x distinto de 0 y de menos 1.",
 "verificacion":{"formula":"(x*x-1)/(x*x+x)-(x-1)/x","a":3,"esperado":0},
 "pistas":["Factoriza el numerador como una diferencia de cuadrados.","El denominador tiene factor común x.","El factor que se repite es x más 1."],
 "errores":["","Esa respuesta cancela x con x menos 1, y no son factores iguales. El que se repite es x más 1.","Se cancelaron mal los términos. Después de cancelar x más 1 queda x menos 1 arriba.","Eso sale de cancelar x al cuadrado con x al cuadrado como si fueran términos. Hay que factorizar primero."]}
res=["Para simplificar se factoriza y se cancelan factores comunes, no términos.","Para sumar se usa un denominador común, y para dividir se multiplica por el inverso.","Los valores que anulan un denominador quedan fuera del dominio, aunque se cancelen."]
write(lesson("mb-m1-l4","Lección 4 de 4","Fracciones algebraicas",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=3,curso="Matemáticas Básicas"),"matbas-fracciones.json")
