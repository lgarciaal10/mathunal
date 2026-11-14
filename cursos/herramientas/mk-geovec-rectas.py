import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 1 Vectores y rectas en el plano"
FX="x-3*(3*x-10)/25"; FY="-4*(3*x-10)/25"
graf={"tipo":"plano","x":[-3.5,9.5],"y":[-3.0,4.1],"a":-2,"b":8,"inicio":0,
 "elementos":[
  {"t":"recta","p":["0","2.5"],"dir":["4","-3"],"c":0},
  {"t":"segmento","a":["x","0"],"b":[FX,FY],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":[FX,FY],"c":1},
  {"t":"punto","p":["x","0"],"c":2}],
 "lecturas":[{"rotulo":"valor de 3x más 4y menos 10 en el punto","formula":"3*x-10"},{"rotulo":"distancia del punto a la recta","formula":"abs(3*x-10)/5"}],
 "etiquetas":["Lo que vale el lado izquierdo de la ecuación en el punto","Longitud del segmento perpendicular"],"etiquetaSlider":"Posición x del punto sobre el eje horizontal",
 "alt":"La recta 3x más 4y menos 10 igual a 0 y un punto que se mueve sobre el eje horizontal. Un segmento punteado perpendicular a la recta baja desde el punto hasta su pie en la recta, y su longitud es la distancia"}
glos={"pendiente":"La pendiente de una recta es el cambio en y entre el cambio en x. Con vector director (a, b) vale b entre a.",
 "director":"El vector director de una recta marca su dirección. Cualquier múltiplo de él sirve.",
 "normal":"El vector normal de una recta es perpendicular a ella. En la recta ax más by más c igual a 0 es el vector (a, b).",
 "distancia":"La distancia de un punto a una recta es la longitud del segmento perpendicular que los une. Es la más corta de todas."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La recta es 3x más 4y menos 10 igual a 0. El punto se mueve sobre el eje horizontal."],
 [4,10,"La distancia del punto a la recta es la longitud del segmento perpendicular, que es el más corto de todos los segmentos."],
 [10,15,"Con x igual a 0, el punto es el origen, y la distancia a la recta es 2."],
 [15,19,"Con x igual a 10 sobre 3, el punto está sobre la recta y la distancia es cero."],
 [19,22,"La fórmula es el valor absoluto de a x0 más b y0 más c, dividido entre la raíz de a al cuadrado más b al cuadrado."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,2],[10,0],[14,0],[15,3.3333333333],[19,3.3333333333],[22,3.3333333333]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,22]}}
S=[
 sec("La idea",None,P("Una recta se puede describir de varias formas. Con un punto y una {{gl:pendiente|pendiente}}, con un punto y un {{gl:director|vector director}}, o con una ecuación general en la que el vector {{gl:normal|normal}} sale de los coeficientes. Una pregunta frecuente es la {{gl:distancia|distancia}} de un punto a una recta.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la recta 3x más 4y menos 10 igual a 0 y un punto que se mueve sobre el eje horizontal. El segmento punteado es perpendicular a la recta."),EQ("d=\\dfrac{|a x_{0}+b y_{0}+c|}{\\sqrt{a^{2}+b^{2}}}"),{"t":"grafica","animar":"dibujar","alt":"La recta con un punto y la distancia"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La recta 3x más 4y menos 10 igual a 0 tiene coeficientes 3 y 4. ¿Cuánto vale la raíz de 3 al cuadrado más 4 al cuadrado?","opciones":[5,7,12,25],"correcta":5,"bien":"Muy bien. Vale 5, y es el denominador de la distancia. Más abajo se ve.","mal":"Vale 5, porque 9 más 16 es 25 y la raíz de 25 es 5. Ese es el denominador de la distancia. Más abajo se ve."}),
 sec("Moviendo el punto","El punto",P("Mira la distancia para x igual a 0, 2, 3.33 y 6."),{"t":"acercando","ds":[0,2,3.3333333333,6],"alt":"El punto en cuatro posiciones y su distancia a la recta"},P("Con x igual a <b>10 sobre 3</b> el punto está sobre la recta y la distancia es cero.")),
 sec("Formas de una recta","Formas",P("Una misma recta se escribe de varias maneras, y conviene pasar de una a otra."),
   PASOS([("y-y_{0}=m(x-x_{0})","Forma punto pendiente."),
          ("(x,y)=(1+3t,\\ 2+4t)","Forma paramétrica. Pasa por (1, 2) con vector director (3, 4)."),
          ("m=\\dfrac{4}{3}","La pendiente es la segunda componente del director entre la primera."),
          ("ax+by+c=0","Forma general. El vector (a, b) es normal a la recta.")]),
   OJO("El vector director y el vector normal son perpendiculares. La recta 3x más 4y igual a 10 tiene normal (3, 4) y director (4, menos 3).")),
 sec("Recta por dos puntos","Dos puntos",P("Con dos puntos se calcula la pendiente y después se usa uno de ellos."),
   PASOS([("(1,2)\\ \\text{y}\\ (3,6)","Los dos puntos."),
          ("m=\\dfrac{6-2}{3-1}=2","La pendiente es el cambio en y entre el cambio en x."),
          ("y-2=2(x-1)","Forma punto pendiente con el primer punto."),
          ("y=2x","Al despejar, queda la ecuación de la recta.")]),
   OJO("La pendiente es el cambio en y entre el cambio en x, y no al revés. Una pendiente de 2 sube 2 por cada paso a la derecha.")),
 eng("La distancia a una guía lineal","Una guía lineal recta se describe con la ecuación 3x más 4y menos 10 igual a 0, con medidas en metros. Un sensor está en el origen. La distancia mínima entre el sensor y la guía determina qué tan fuerte llega la señal.","d=\\dfrac{|3\\cdot0+4\\cdot0-10|}{\\sqrt{3^{2}+4^{2}}}=2",
   [("Guía","3x más 4y igual a 10"),("Sensor","en el origen"),("Distancia mínima","2 m")],"La fórmula da 10 entre 5, o sea 2 metros. Esa distancia se mide perpendicular a la guía, y cualquier otra medida entre el sensor y un punto de la guía es mayor. Con la distancia mínima se dimensiona el alcance de la señal. Es un modelo plano, que ignora la altura del sensor."),
 completar("Se calcula la pendiente de una recta con vector director (4, 8). Falta el valor.","m=\\dfrac{8}{4}=[[hueco]]",
   [("2","dos"),("\\dfrac12","un medio"),("4","cuatro")],0,
   ["","Un medio sale al dividir las componentes al revés. La pendiente es la segunda entre la primera.","Cuatro es la primera componente, y no el cociente."],"La pendiente es la segunda componente entre la primera.","8 entre 4 es 2."),
 error("Alguien calculó la pendiente de la recta que pasa por (1, 2) y (3, 6) y se equivocó en un paso. Toca el paso que está mal.",
   [("(1,2)\\ \\text{y}\\ (3,6)","Los dos puntos.","los puntos son estos"),
    ("m=\\dfrac{3-1}{6-2}=\\dfrac12","Este paso es el que falla.","la pendiente es un medio"),
    ("y-2=\\tfrac12(x-1)","Se usa el primer punto.","se usa la forma punto pendiente")],1,
   "La pendiente es el cambio en y entre el cambio en x, o sea 6 menos 2 entre 3 menos 1. El paso invirtió el cociente, y la pendiente correcta es 2.",
   "m=\\dfrac{6-2}{3-1}=2","Recuerda qué va arriba en la pendiente."),
 ordenar("Estos son los pasos para hallar la recta que pasa por (1, 2) y (3, 6), pero están desordenados.",
   [("(1,2)\\ \\text{y}\\ (3,6)","Se toman los dos puntos"),
    ("m=\\dfrac{6-2}{3-1}=2","Se calcula la pendiente"),
    ("y-2=2(x-1)","Se escribe con un punto y la pendiente"),
    ("y=2x","Se despeja y")],[2,0,3,1],
   "Se calcula la pendiente, se escribe la forma punto pendiente y se despeja.","Se empieza con los dos puntos."),
]
S+=cierre("Mini simulacro de rectas en el plano",[
 banco("gv_c1_04","La pendiente es $\\tfrac{6-2}{3-1}=2$ y la recta pasa por el origen."),
 banco("gv_c1_05","$\\dfrac{|{-10}|}{\\sqrt{3^2+4^2}}=\\dfrac{10}{5}=2$."),
 banco("gv_c1_10","Un punto y un director dan la ecuación paramétrica.")])
prac=[
 {"titulo":"La recta y el punto","grafica":{"draw":1},"bloques":[P("La recta 3x más 4y menos 10 igual a 0 y un punto sobre el eje."),EQ("3x+4y-10=0")]},
 {"titulo":"Mueve el punto","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el valor de la ecuación y la distancia a la recta.")]},
 {"titulo":"El punto sobre la recta","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3.3333333333,"bloques":[EQ("3x-10=0\\ \\Rightarrow\\ x=\\tfrac{10}{3}"),P("Con x igual a 10 sobre 3 el punto está sobre la recta y la distancia es cero.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3.3333333333},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Usa el valor absoluto del numerador y la raíz de la suma de cuadrados abajo."}]}]
preg={"tex":"\\text{Distancia de}\\ (1,1)\\ \\text{a la recta}\\ x+y-4=0","opciones":["$\\sqrt{2}$","$2$","$\\dfrac{1}{\\sqrt{2}}$","$2\\sqrt{2}$"],"correcta":0,
 "explicacion":"El numerador es el valor absoluto de 1 más 1 menos 4, que da 2, y el denominador es la raíz de 1 más 1, que es raíz de 2. El cociente es 2 entre raíz de 2, o sea raíz de 2.",
 "verificacion":{"formula":"abs(1+1-4)/sqrt(2)+0*x","a":0,"esperado":1.4142},
 "pistas":["Calcula el valor de x más y menos 4 en el punto.","Da menos 2. Se toma el valor absoluto.","Se divide entre la raíz de 1 más 1."],
 "errores":["","Falta dividir entre la raíz de 2. Ese es solo el valor absoluto del numerador.","Sale de usar un numerador de 1, por no restar 4 al evaluar, y dividir entre raíz de 2.","Se multiplicó en lugar de dividir entre la raíz de 2."]}
res=["Una recta se describe con un punto y una pendiente, con un punto y un director, o con una ecuación general.","La pendiente es el cambio en y entre el cambio en x, o la segunda componente del director entre la primera.","La distancia de un punto a una recta es el valor absoluto de a x0 más b y0 más c, entre la raíz de a al cuadrado más b al cuadrado."]
write(lesson("gv-m1-l3","Lección 3 de 4","Rectas en el plano",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-rectas.json")
