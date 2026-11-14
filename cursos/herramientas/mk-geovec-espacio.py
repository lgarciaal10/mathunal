import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 3 Rectas, planos y cónicas"
graf={"tipo":"plano","x":[-10.3,10.3],"y":[-3.6,7.6],"a":-3,"b":2,"inicio":0,
 "elementos":[
  {"t":"recta","p":["0","1"],"dir":["1","0"],"c":3,"guion":True},
  {"t":"recta","p":["1","3"],"dir":["1","2"],"c":0},
  {"t":"segmento","a":["1+x","1"],"b":["1+x","3+2*x"],"guion":True,"c":2,"guia":True},
  {"t":"punto","p":["1+x","3+2*x"],"c":1}],
 "lecturas":[{"rotulo":"coordenada z del punto de la recta","formula":"3+2*x"},{"rotulo":"coordenada y del punto de la recta","formula":"2-x"}],
 "etiquetas":["Altura del punto, el plano está a altura 1","Segunda coordenada del punto"],"etiquetaSlider":"Parámetro t",
 "alt":"La recta que pasa por (1, 2, 3) con dirección (1, menos 1, 2), vista en el plano x z. El plano z igual a 1 aparece como una recta horizontal. Un punto se mueve sobre la recta con el parámetro t y cruza el plano cuando t vale menos 1"}
glos={"vectorial":"La ecuación vectorial de una recta es r igual a r0 más t v, donde r0 es un punto y v es el vector director.",
 "parametrica":"Las ecuaciones paramétricas dan cada coordenada en función de t. Es la ecuación vectorial escrita componente a componente.",
 "alabeadas":"Dos rectas del espacio que no se cortan y no son paralelas se llaman alabeadas. No están en un mismo plano.",
 "interseccion":"Para hallar la intersección de una recta con un plano se sustituye la recta en la ecuación del plano y se despeja t."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La recta pasa por (1, 2, 3) con dirección (1, menos 1, 2). En esta vista se ven x y z, y el plano z igual a 1 aparece como una recta horizontal."],
 [4,10,"El punto se mueve con el parámetro t. Cada valor de t da un punto de la recta."],
 [10,15,"Con t igual a menos 1, z vale 1 y la recta cruza el plano. El punto de corte es (0, 3, 1)."],
 [15,19,"En ese punto y vale 3, que se lee en la segunda lectura."],
 [19,22,"Para cortar una recta con un plano se sustituye la recta en la ecuación del plano y se despeja t."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,2],[9,-3],[10,-1],[15,-1],[19,-1],[22,-1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,22]}}
S=[
 sec("La idea",None,P("Una recta del espacio se describe con un punto y un vector director, en forma {{gl:vectorial|vectorial}} o {{gl:parametrica|paramétrica}}. Dos rectas pueden cortarse, ser paralelas o ser {{gl:alabeadas|alabeadas}}. Una recta puede cortar a un plano en un punto, ser paralela a él o estar contenida en él. Para hallar el corte se usa la {{gl:interseccion|intersección}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la recta que pasa por (1, 2, 3) con dirección (1, menos 1, 2) y el plano z igual a 1. Mueve el parámetro t hasta que el punto toque el plano."),EQ("(x,y,z)=(1,2,3)+t\\,(1,-1,2)"),{"t":"grafica","animar":"dibujar","alt":"La recta y el plano z igual a 1"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La recta tiene z igual a 3 más 2t. Para que z valga 1 hace falta que 2t valga menos 2. ¿Cuánto vale t?","opciones":[-2,-1,1,2],"correcta":-1,"bien":"Muy bien. Vale menos 1. Más abajo se ve el punto de corte.","mal":"Vale menos 1, porque menos 2 entre 2 es menos 1. Más abajo se ve el punto de corte."}),
 sec("Moviendo el punto","El parámetro",P("Mira el punto con t igual a menos 3, menos 1, 0 y 2."),{"t":"acercando","ds":[-3,-1,0,2],"alt":"El punto sobre la recta para cuatro valores de t"},P("Con t igual a <b>menos 1</b> el punto está en el plano. Allí (x, y, z) vale (0, 3, 1).")),
 sec("Formas de la recta","Formas",P("Una recta se escribe con un punto y una dirección."),
   PASOS([("\\mathbf{r}=\\mathbf{r}_{0}+t\\,\\mathbf{v}","Forma vectorial."),
          ("(x,y,z)=(1+t,\\ 2-t,\\ 3+2t)","Forma paramétrica, coordenada por coordenada."),
          ("(x,y)=(1+3t,\\ 2+4t)","En el plano es lo mismo con dos componentes, como en el banco."),
          ("\\mathbf{v}=(1,-1,2)","El vector director marca la dirección de la recta.")])),
 sec("Intersecciones","Intersecciones",P("Para hallar dónde una recta corta a un plano se reemplaza la recta en la ecuación del plano."),
   PASOS([("z=3+2t,\\quad \\text{plano}\\ z=1","Se sustituye en la ecuación del plano."),
          ("3+2t=1\\ \\Rightarrow\\ t=-1","Se despeja t."),
          ("(1-1,\\ 2+1,\\ 3-2)=(0,3,1)","Se evalúa la recta en ese t."),
          ("\\mathbf{v}\\cdot\\mathbf{n}=0\\ \\Leftrightarrow\\ \\text{recta paralela al plano o contenida en él}","Si la dirección es perpendicular a la normal, no hay un único corte.")]),
   OJO("Una recta paralela a un plano puede estar contenida en él o no cortarlo nunca. Para saber cuál es el caso, se prueba si un punto de la recta está en el plano.")),
 sec("Dos rectas en el espacio","Dos rectas",P("En el espacio, dos rectas tienen tres posibilidades, y la tercera no existe en el plano."),
   PASOS([("\\mathbf{v}_{1}\\parallel\\mathbf{v}_{2}","Paralelas, o la misma recta."),
          ("\\text{existe}\\ t,s:\\ \\mathbf{r}_{1}(t)=\\mathbf{r}_{2}(s)","Se cortan en un punto."),
          ("\\text{ni paralelas ni con punto común}","Se cruzan, y se llaman alabeadas u oblicuas.")]),
   OJO("En el plano, dos rectas no paralelas siempre se cortan. En el espacio no, porque pueden cruzarse sin tocarse.")),
 eng("El rayo láser sobre una placa","Un láser sale del punto (1, 2, 3) metros con dirección (1, menos 1, menos 2) y apunta hacia una placa plana en z igual a 1. El punto donde la toca se obtiene al sustituir la recta del rayo en la ecuación del plano.","3-2t=1\\ \\Rightarrow\\ t=1\\ \\Rightarrow\\ (2,1,1)",
   [("Origen del rayo","(1, 2, 3) m"),("Dirección","(1, menos 1, menos 2)"),("Punto en la placa","(2, 1, 1) m")],"El rayo llega a la placa en el punto (2, 1, 1) metros, después de un parámetro t igual a 1, es decir, hacia adelante en la dirección dada. Si la dirección fuera paralela a la placa, el rayo nunca la tocaría. Este cálculo se usa en visión por computador y en trazado de rayos."),
 completar("Se sustituye la recta en el plano z igual a 1. Falta el valor de la derecha.","3+2t=[[hueco]]",
   [("1","uno"),("0","cero"),("3","tres")],0,
   ["","Cero sería el plano z igual a 0. El plano de este ejemplo es z igual a 1.","Tres es el valor de z en el punto de partida, y no el valor del plano."],"La derecha es el valor de z en el plano.","El plano z igual a 1 pide que 3 más 2t valga 1."),
 error("Alguien halló dónde la recta corta al plano z igual a 1 y se equivocó en un paso. Toca el paso que está mal.",
   [("z=3+2t","La coordenada z de la recta.","z es 3 más 2t"),
    ("3+2t=1","Se iguala al plano.","se iguala a 1"),
    ("\\text{Entonces}\\ t=1","Este paso es el que falla.","queda t igual a 1")],2,
   "De 3 más 2t igual a 1 se despeja 2t igual a menos 2, y t vale menos 1. Con t igual a 1 se obtendría z igual a 5.",
   "t=-1","Despeja t con cuidado del signo."),
 ordenar("Estos son los pasos para hallar el punto donde la recta corta al plano z igual a 1, pero están desordenados.",
   [("(x,y,z)=(1+t,\\ 2-t,\\ 3+2t)","Se escribe la recta en paramétricas"),
    ("3+2t=1","Se sustituye en la ecuación del plano"),
    ("t=-1","Se despeja t"),
    ("(0,3,1)","Se evalúa la recta en ese t")],[2,0,3,1],
   "Se escribe la recta, se sustituye en el plano, se despeja t y se evalúa.","Se empieza escribiendo la recta."),
]
S+=cierre("Mini simulacro de rectas en el espacio e intersecciones",[
 banco("gv_c3_10","La ecuación vectorial de una recta es un punto más un múltiplo del director."),
 banco("gv_c3_11","Dos rectas que ni se cortan ni son paralelas se cruzan, y se llaman alabeadas."),
 banco("gv_c3_12","Una recta es paralela a un plano, o está contenida en él, si su director es perpendicular a la normal.")])
prac=[
 {"titulo":"La recta y el plano","grafica":{"draw":1},"bloques":[P("La recta vista en el plano x z, y el plano z igual a 1 como una recta horizontal."),EQ("(x,y,z)=(1,2,3)+t\\,(1,-1,2)")]},
 {"titulo":"Mueve el parámetro","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen las coordenadas z y y del punto de la recta.")]},
 {"titulo":"El corte","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":-1,"bloques":[EQ("t=-1\\ \\Rightarrow\\ (0,3,1)"),P("Con t igual a menos 1, z vale 1 y la recta toca el plano.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":-1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el producto punto del director con la normal."}]}]
preg={"tex":"\\text{La recta}\\ (1,0,0)+t(0,1,1)\\ \\text{y el plano}\\ x+y-z=5","opciones":["es paralela al plano","es perpendicular al plano","está contenida en el plano","corta al plano en un punto"],"correcta":0,
 "explicacion":"El director es (0, 1, 1) y la normal es (1, 1, menos 1). Su producto punto es 0 más 1 menos 1, o sea 0, así que la recta es paralela al plano. El punto (1, 0, 0) da 1 en la ecuación, y no 5, entonces no está contenida.",
 "verificacion":{"formula":"0*1+1*1+1*(-1)+0*x","a":0,"esperado":0},
 "pistas":["Calcula el producto punto del director con la normal.","Da 0.","Un producto cero indica que la recta es paralela al plano."],
 "errores":["","Perpendicular exigiría que el director fuera paralelo a la normal, y aquí el producto punto es cero.","Para estar contenida, el punto (1, 0, 0) debería cumplir la ecuación, y da 1.","Un corte en un punto exige que el producto punto sea distinto de cero."]}
res=["Una recta del espacio es un punto más un múltiplo del vector director, en forma vectorial o paramétrica.","Para cortar una recta con un plano se sustituye la recta en la ecuación del plano y se despeja t.","Una recta es paralela a un plano si su director es perpendicular a la normal, y dos rectas que no se cortan ni son paralelas son alabeadas."]
write(lesson("gv-m3-l4","Lección 4 de 4","Rectas en el espacio e intersecciones",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-espacio.json")
