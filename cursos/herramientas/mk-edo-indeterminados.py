import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 2 Orden superior y coeficientes constantes"
N=100
TS=[20.0*k/N for k in range(N+1)]
TOT=[[f"{t:.4f}",f"(cos(x*{t:.4f})-cos(2*{t:.4f}))/(4-x*x)"] for t in TS]
PAR=[[f"{t:.4f}",f"cos(x*{t:.4f})/(4-x*x)"] for t in TS]
graf={"tipo":"plano","x":[-1,20.5],"y":[-4,4],"a":0.2,"b":1.85,"inicio":0.5,
 "elementos":[{"t":"trazo","puntos":PAR,"c":3,"guia":True},{"t":"trazo","puntos":TOT,"c":2},{"t":"punto","p":["0","0"],"c":1}],
 "lecturas":[{"rotulo":"frecuencia de la fuerza","formula":"x"},{"rotulo":"amplitud de la solución particular","formula":"1/(4-x*x)"}],
 "etiquetas":["Frecuencia de la fuerza","Amplitud de la solución particular"],"etiquetaSlider":"Frecuencia de la fuerza",
 "alt":"La respuesta de una masa en un resorte, y segunda más 4y igual a coseno de omega t, que parte del reposo. Al acercar omega a 2 la amplitud crece mucho"}
glos={"particular":"Una solución particular es cualquier función que cumple la ecuación completa, con el lado derecho incluido. No lleva constantes arbitrarias.",
 "indeterminados":"El método de coeficientes indeterminados propone una solución particular con la misma forma del lado derecho, con coeficientes sin conocer, y los halla al reemplazar en la ecuación.",
 "resonancia":"Hay resonancia cuando la fuerza tiene la misma frecuencia natural del sistema. La respuesta crece sin parar y la forma propuesta se multiplica por x."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y segunda más 4y igual a coseno de omega t describe una masa en un resorte, empujada por una fuerza. Esta es la respuesta cuando omega vale 0.5 y parte del reposo."],
 [4,8,"La curva de apoyo es la solución particular. Tiene la misma forma que la fuerza, un coseno de omega t por una constante."],
 [8,14,"Al acercar omega a 2, la frecuencia natural del resorte, la amplitud de la solución particular crece, porque se divide entre 4 menos omega al cuadrado."],
 [14,18,"Con omega cerca de 2 la amplitud se dispara. Justo en 2 la forma A coseno de 2t ya no sirve, porque coseno de 2t es solución de la homogénea. Hay que multiplicar por t."],
 [18,22,"Con omega igual a 1.85 la amplitud de la solución particular es 1.73, y la respuesta total muestra pulsos."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[9,1],[13,1.85],[22,1.85]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Cuando una ecuación lineal tiene un lado derecho que no es cero, la solución general es la suma de dos partes. Una es la solución de la homogénea. La otra es una {{gl:particular|solución particular}}. El método de {{gl:indeterminados|coeficientes indeterminados}} la encuentra proponiendo una función con la misma forma del lado derecho y calculando sus coeficientes.")),
 sec("Un ejemplo","Un ejemplo",P("Mira una masa en un resorte empujada por una fuerza que oscila con frecuencia omega."),EQ("y''+4y=\\cos(\\omega t),\\qquad y(0)=0,\\ y'(0)=0"),{"t":"grafica","animar":"dibujar","alt":"La respuesta de la masa"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En y segunda más 4y igual a 3 se propone una constante y igual a A. Como la segunda derivada de una constante es 0, queda 4A igual a 3. ¿Cuánto vale A?","opciones":[0.75,1.5,3,12],"correcta":0.75,"bien":"Muy bien. Vale 0.75. Más abajo se ve el mismo método con un coseno.","mal":"Vale 0.75, porque 3 dividido entre 4 es 0.75. Más abajo se ve el mismo método con un coseno."}),
 sec("Acercando la frecuencia","Resonancia",P("Mira cómo cambia la respuesta al subir la frecuencia de la fuerza."),{"t":"acercando","ds":[0.5,1,1.5,1.85],"alt":"La respuesta para varias frecuencias"},P("La amplitud de la solución particular es 1 sobre 4 menos omega al cuadrado. Al acercarse omega a 2 el denominador tiende a 0 y la amplitud crece sin límite. Eso se llama {{gl:resonancia|resonancia}}.")),
 sec("El método","El método",P("Se propone la forma, se reemplaza en la ecuación y se comparan los coeficientes."),
   PASOS([("y''+4y=\\cos t,\\quad y_{p}=A\\cos t+B\\operatorname{sen}t","La fuerza es un coseno. Se proponen un coseno y un seno, porque al derivar uno aparece el otro."),
          ("y_{p}''=-A\\cos t-B\\operatorname{sen}t","Se deriva dos veces."),
          ("3A\\cos t+3B\\operatorname{sen}t=\\cos t","Se reemplaza en la ecuación y se agrupa."),
          ("A=\\dfrac{1}{3},\\quad B=0\\ \\Rightarrow\\ y_{p}=\\dfrac{1}{3}\\cos t","Se igualan los coeficientes de coseno y de seno a ambos lados.")])),
 sec("Qué forma proponer","Qué proponer",P("La forma depende del lado derecho. Cuando es un polinomio, se propone un polinomio completo del mismo grado."),
   PASOS([("g(x)=\\text{polinomio de grado }n\\ \\Rightarrow\\ y_{p}=A_{n}x^{n}+\\dots+A_{1}x+A_{0}","Hay que incluir todos los términos, aunque g no los tenga."),
          ("g(x)=e^{kx}\\ \\Rightarrow\\ y_{p}=Ae^{kx}","Una exponencial de la misma tasa."),
          ("g(x)=\\cos kx\\ \\text{o}\\ \\operatorname{sen}kx\\ \\Rightarrow\\ y_{p}=A\\cos kx+B\\operatorname{sen}kx","Siempre los dos, el coseno y el seno.")])),
 sec("Cuando la forma choca","Cuando choca",P("Si la forma propuesta ya es solución de la homogénea, al reemplazarla sale 0 y no se puede igualar a la fuerza. Se multiplica por x, y si sigue chocando, por x al cuadrado."),
   PASOS([("y''-2y'+y=e^{x}","La homogénea tiene raíz doble r igual a 1, así que e a la x y x e a la x son soluciones."),
          ("y_{p}=Ax^{2}e^{x}","Se multiplica por x dos veces, hasta que deje de ser solución de la homogénea."),
          ("y_{p}''-2y_{p}'+y_{p}=2Ae^{x}=e^{x}\\ \\Rightarrow\\ A=\\dfrac{1}{2}","Al reemplazar solo queda 2A e a la x.")]),
   OJO("La solución general es la suma. Primero se resuelve la homogénea, después se halla la particular y al final se suman. Las constantes c1 y c2 se calculan con las condiciones iniciales usando la suma completa, no solo la homogénea.")),
 eng("Un motor sobre una base","Un motor desbalanceado empuja la base con una fuerza que oscila con la velocidad de giro. La base se modela como una masa y un resorte. Si la fuerza tiene la frecuencia natural de la base, aparece la resonancia y las vibraciones crecen.","m\\,y''+k\\,y=F\\cos\\omega t",
   [("Masa","400 kg"),("Rigidez","1.6 millones de N/m"),("Giro del motor","600 rpm")],"La frecuencia natural es la raíz de k sobre m, o sea 63.2 radianes por segundo, que son unas 604 revoluciones por minuto. El motor gira a 600, muy cerca de ese valor, así que la base vibraría mucho. Se arregla cambiando la rigidez o la masa para alejar las dos frecuencias. Es un modelo simplificado, porque no tiene amortiguamiento, que en la práctica limita el crecimiento."),
 completar("Se propone la forma de la solución particular de y segunda menos y igual a x cuadrado.","y_{p}=Ax^{2}+Bx+[[hueco]]",
   [("C","una constante"),("0","cero"),("Cx^{3}","un término cúbico")],0,
   ["","Si se omite la constante, el polinomio queda incompleto y puede no alcanzar para igualar los términos.","El lado derecho es de grado 2, así que no hace falta un término de grado 3."],"Debe ser un polinomio completo de grado 2.","Se propone el polinomio completo, con el término constante incluido."),
 error("Alguien resolvió una ecuación y se equivocó en un paso. Toca el paso que está mal.",
   [("y''-2y'+y=e^{x}\\ \\Rightarrow\\ (r-1)^{2}=0","La ecuación característica tiene raíz doble 1.","la característica es r al cuadrado menos 2r más 1, con raíz doble 1"),
    ("y_{h}=(c_{1}+c_{2}x)\\,e^{x}","La solución de la homogénea.","y de la homogénea es c1 más c2 x, por e a la x"),
    ("y_{p}=Ae^{x}","Este paso es el que falla.","se propone y particular igual a A e a la x")],2,
   "La función e a la x ya es solución de la homogénea, y x e a la x también. Reemplazar A e a la x da 0 y no se puede igualar a e a la x. Hay que proponer A x al cuadrado por e a la x.",
   "y_{p}=Ax^{2}e^{x}","Revisa si la forma propuesta aparece en la solución de la homogénea."),
 ordenar("Estos son los pasos para hallar una solución particular de y segunda menos 3y prima más 2y igual a 4x, pero están desordenados.",
   [("y_{p}=Ax+B","La forma propuesta"),
    ("y_{p}'=A,\\quad y_{p}''=0","Las derivadas"),
    ("-3A+2Ax+2B=4x","Se reemplaza en la ecuación"),
    ("A=2,\\ B=3\\ \\Rightarrow\\ y_{p}=2x+3","Se igualan los coeficientes")],[1,3,0,2],
   "Se propone el polinomio, se deriva, se reemplaza y se comparan los coeficientes de x y del término constante.","Se empieza proponiendo la forma."),
]
S+=cierre("Mini simulacro de coeficientes indeterminados",[
 banco("ed_c2_04","El lado derecho es un polinomio de grado 1 y no está en la homogénea, así que se propone $y_p=Ax+B$."),
 banco("ed_c2_13","El lado derecho es una exponencial, así que se propone una exponencial con la misma tasa, $Ae^{2x}$."),
 banco("ed_c2_14","El lado derecho es un polinomio de grado 2, así que se propone el polinomio completo de grado 2.")])
prac=[
 {"titulo":"La respuesta","grafica":{"draw":1,"guide":1},"bloques":[P("Una masa en un resorte, empujada por una fuerza de frecuencia omega."),EQ("y''+4y=\\cos\\omega t")]},
 {"titulo":"Cambia omega","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Cerca de 2 la amplitud de la solución particular crece mucho. Abajo se leen omega y esa amplitud.")]},
 {"titulo":"Cerca de la resonancia","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.85,"bloques":[EQ("\\omega\\to 2\\ \\Rightarrow\\ \\dfrac{1}{4-\\omega^{2}}\\to\\infty"),P("Con omega en 1.85 la amplitud ya es 1.73.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.85},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Propón la forma, reemplaza y compara coeficientes."}]}]
preg={"tex":"y''+y=2e^{x}\\ \\text{tiene como solución particular}","opciones":["$y_p=e^{x}$","$y_p=2e^{x}$","$y_p=xe^{x}$","$y_p=\\tfrac{1}{2}e^{x}$"],"correcta":0,
 "explicacion":"Se propone y particular igual a A e a la x. Como la segunda derivada también es A e a la x, la ecuación queda A más A igual a 2, o sea A igual a 1. La homogénea tiene coseno y seno, así que no hay choque y no se multiplica por x.",
 "verificacion":{"formula":"2/(1+1)+0*x","a":0,"esperado":1},
 "pistas":["Propón y particular igual a A e a la x y reemplaza.","La segunda derivada de A e a la x es A e a la x.","Queda 2A igual a 2."],
 "errores":["","Ese es el lado derecho. Falta dividir entre el coeficiente que sale al reemplazar, que es 2.","Solo se multiplica por x cuando la forma choca con la homogénea. Aquí la homogénea tiene coseno y seno.","Eso resulta de dividir dos veces. La ecuación queda 2A igual a 2, y A vale 1."]}
res=["La solución general es la homogénea más una solución particular.","Se propone una forma igual a la del lado derecho, con coeficientes sin conocer, y se hallan al reemplazar.","Si la forma propuesta ya es solución de la homogénea, se multiplica por x hasta que deje de serlo. Ese es el caso de la resonancia."]
write(lesson("edo-m2-l2","Lección 2 de 4","Coeficientes indeterminados",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=6,curso="Ecuaciones Diferenciales"),"edo-indeterminados.json")
