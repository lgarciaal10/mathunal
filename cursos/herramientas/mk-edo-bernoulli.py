import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
XR=[-1,3]; YR=[-0.3,1.88]
EL=campo(lambda x,y:-2*y+y**3,XR,YR,16,7,0.12)
EL+=[{"t":"recta","p":["0","1.4142"],"dir":["1","0"],"guion":True,"c":3,"guia":True},trazo("1/sqrt(0.5+x*exp(4*{x}))",-1,3,80,2),{"t":"punto","p":["0","1/sqrt(0.5+x)"],"c":1}]
graf={"tipo":"plano","x":XR,"y":YR,"a":0,"b":2,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"C","formula":"x"},{"rotulo":"y(0)","formula":"1/sqrt(0.5+x)"}],
 "etiquetas":["Constante C","Valor inicial y(0)"],"etiquetaSlider":"Constante C",
 "alt":"El campo de pendientes de y prima más 2y igual a y al cubo y las soluciones y igual a 1 sobre la raíz de un medio más C por e a la 4x, que se alejan de la recta y igual a raíz de 2"}
glos={"bernoulli":"Una ecuación de Bernoulli es y prima más p de x por y igual a q de x por y a la n. Con n distinto de 0 y de 1 no es lineal, pero se vuelve lineal con un cambio de variable.",
 "sustitucion":"Una sustitución cambia la incógnita por otra, como v igual a y a la 1 menos n, para convertir una ecuación difícil en una conocida."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima más 2y igual a y al cubo tiene un término y al cubo, así que no es lineal."],
 [4,9,"Tiene un equilibrio en y igual a la raíz de 2, la recta punteada. Las soluciones que parten más abajo bajan hacia 0, y las de arriba suben."],
 [9,15,"Con la sustitución v igual a y a la menos 2 se vuelve lineal, y su solución es v igual a un medio más C por e a la 4x."],
 [15,19,"Al regresar a y, queda y igual a 1 sobre la raíz de (un medio más C e a la 4x)."],
 [19,22,"Con C igual a 0.5, y de 0 vale 1. Todas las soluciones con C positiva se van a 0."]],
 "canales":{"draw":[[0.3,0],[4,1]],"d":[[4,0.5],[9,1.5],[12,0.1],[15,0.5],[22,0.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("Una ecuación de {{gl:bernoulli|Bernoulli}} se parece a una lineal, pero la y de la derecha lleva una potencia n. Entonces ya no se puede usar el factor integrante directamente. Con una {{gl:sustitucion|sustitución}} v igual a y a la 1 menos n, se convierte en una lineal en v, y esa sí se sabe resolver.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación con n igual a 3."),EQ("y'+2y=y^{3}"),{"t":"grafica","animar":"dibujar","alt":"El campo de pendientes y una solución"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con y igual a 1, la pendiente es menos 2y más y al cubo. ¿Cuánto vale?","opciones":[-2,-1,0,1],"correcta":-1,"bien":"Muy bien. Vale menos 1, así que baja. Más abajo se ve el campo.","mal":"Vale menos 1, porque menos 2 más 1 es menos 1. Más abajo se ve el campo."}),
 sec("Las soluciones","Las soluciones",P("Mira cómo cambian las soluciones al variar la constante C."),{"t":"acercando","ds":[0,0.5,1.5],"alt":"Las soluciones para varios valores de C"},P("Con C igual a 0 la solución es constante, y igual a la raíz de 2. Con C positiva, la solución baja a 0.")),
 sec("La sustitución","La sustitución",P("Con n igual a 3, se toma v igual a y a la 1 menos 3, o sea y a la menos 2."),
   PASOS([("v=y^{-2}\\ \\Rightarrow\\ v'=-2y^{-3}y'","Se deriva con la regla de la cadena."),
          ("y'=y^{3}-2y\\ \\Rightarrow\\ v'=-2y^{-3}\\left(y^{3}-2y\\right)=-2+4v","Se reemplaza y prima y se usa que y a la menos 2 es v."),
          ("v'-4v=-2","Es una ecuación lineal en v, con factor integrante e a la menos 4x."),
          ("v=\\dfrac{1}{2}+Ce^{4x}","Se resuelve la lineal.")]),
   OJO("Hay que dividir entre y a la n antes de sustituir, o usar la derivada de v como se hizo aquí. Ese paso es el que más se olvida.")),
 sec("Volver a y","Volver a y",PASOS([("y=v^{-1/2}","Se deshace la sustitución."),
          ("y=\\dfrac{1}{\\sqrt{\\dfrac{1}{2}+Ce^{4x}}}","Es la solución general."),
          ("y\\equiv 0\\ \\text{también es solución}","Se perdió al dividir entre y.")])),
 sec("La receta general","Receta",P("Para cualquier ecuación de Bernoulli el procedimiento es el mismo."),
   PASOS([("y'+p(x)\\,y=q(x)\\,y^{n}","La forma de Bernoulli."),
          ("v=y^{1-n}\\ \\Rightarrow\\ v'+(1-n)\\,p(x)\\,v=(1-n)\\,q(x)","Queda una lineal."),
          ("y'+\\dfrac{y}{x}=y^{2}\\ \\Rightarrow\\ v=y^{-1}","Con n igual a 2 se toma v igual a y a la menos 1.")])),
 eng("El crecimiento con competencia","Una población de bacterias en un reactor crece, pero la competencia por alimento frena el crecimiento más rápido de lo que lo haría una ley lineal. Ese tipo de modelos lleva a ecuaciones de Bernoulli, que se resuelven con el cambio de variable.","y'=r\\,y-s\\,y^{2}",
   [("Tasa de crecimiento r","0.5 1/h"),("Competencia s","0.1"),("Población límite","5")],"Con n igual a 2 y v igual a 1 sobre y, la ecuación se vuelve lineal y su solución es y igual a 5 sobre (1 más C e a la menos 0.5 t). La población se acerca a r sobre s, o sea 5, sin importar la inicial. Es un modelo simplificado, porque supone un reactor bien mezclado y alimento constante."),
 completar("Se linealiza y prima más y sobre x igual a y al cuadrado. Falta la sustitución.","v=y^{[[hueco]]}",
   [("1-n=-1","uno menos n es menos uno"),("n=2","n es dos"),("-n=-2","menos n es menos dos")],0,
   ["","La sustitución usa el exponente 1 menos n, y no n.","El exponente es 1 menos n, o sea menos 1, y no menos n."],"El exponente es uno menos n, con n igual a 2.","Con n igual a 2, el exponente 1 menos n es menos 1, así que v es 1 sobre y."),
 error("Alguien resolvió una ecuación de Bernoulli y se equivocó en un paso. Toca el paso que está mal.",
   [("y'+y=y^{2}\\ (n=2)","Es la ecuación.","y prima más y igual a y al cuadrado, con n igual a 2"),
    ("v=y^{2}\\ \\Rightarrow\\ v'=2yy'","Este paso es el que falla.","v es y al cuadrado, y v prima es 2 y y prima"),
    ("\\text{Se obtiene una lineal en}\\ v","Depende del paso anterior.","Se obtiene una lineal en v")],1,
   "La sustitución es v igual a y elevada a 1 menos n, y aquí es y a la menos 1, o sea 1 sobre y. Con y al cuadrado no se obtiene una ecuación lineal.",
   "v=y^{1-n}=y^{-1}\\ \\Rightarrow\\ v'-v=-1","Usa el exponente 1 menos n."),
 ordenar("Estos son los pasos para resolver y prima más 2y igual a y al cubo, pero están desordenados.",
   [("v=y^{-2}\\ \\Rightarrow\\ v'=-2y^{-3}y'","Se hace la sustitución"),
    ("v'-4v=-2","Queda una lineal en v"),
    ("v=\\dfrac{1}{2}+Ce^{4x}","Se resuelve con factor integrante"),
    ("y=v^{-1/2}","Se regresa a y")],[2,0,3,1],
   "Se hace la sustitución, se obtiene la lineal, se resuelve y se regresa a y.","Primero va la sustitución."),
]
S+=cierre("",None)
prac=[
 {"titulo":"Las soluciones","grafica":{"draw":1,"guide":1},"bloques":[P("Esta ecuación no es lineal."),EQ("y'+2y=y^{3}")]},
 {"titulo":"Cambia C","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Con C igual a 0 la solución es la recta punteada. Con C positiva, la solución baja a 0. Abajo se ven C y y(0).")]},
 {"titulo":"Sustitución","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("v=y^{-2},\\quad v=\\dfrac{1}{2}+Ce^{4x}"),P("Con C igual a 0.5, y de 0 vale 1.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"La sustitución es v igual a y a la 1 menos n."}]}]
preg={"tex":"y'+\\dfrac{y}{x}=y^{2}","encabezado":"Para linealizar y prima más y sobre x igual a y al cuadrado se sustituye:","opciones":["$v=y^{-1}$","$v=y^{2}$","$v=y^{-2}$","$v=y^{3}$"],"correcta":0,
 "explicacion":"Es una ecuación de Bernoulli con n igual a 2. La sustitución es v igual a y a la 1 menos n, o sea y a la menos 1.",
 "pistas":["Identifica n, el exponente de y en el lado derecho.","Aquí n vale 2.","La sustitución es y elevada a 1 menos n."],
 "errores":["","Esa usa n y no 1 menos n.","Ese exponente sería para n igual a 3, y aquí n es 2.","Ese exponente sería para n igual a menos 2, y aquí n es 2."]}
res=["Una ecuación de Bernoulli es y prima más p y igual a q por y a la n.","Con v igual a y a la 1 menos n se vuelve lineal en v.","Al dividir entre y a la n se puede perder la solución y igual a 0."]
write(lesson("edo-m1-l6","Lección 6 de 6","Bernoulli y sustituciones",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales",ejercicios=4),"edo-bernoulli.json")
