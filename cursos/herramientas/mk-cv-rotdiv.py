import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 3 Cálculo vectorial"
PTS=[(1.5,0),(-1.5,0),(0,1.5),(0,-1.5),(1,1),(-1,1),(1,-1),(-1,-1)]
EL=[]
for (px,py) in PTS:
    EL.append({"t":"vector","a":[str(px),str(py)],"b":[f"{px}+0.5*(cos(x)*({px})-sin(x)*({py}))",f"{py}+0.5*(sin(x)*({px})+cos(x)*({py}))"],"c":0})
EL.append({"t":"punto","p":["0","0"],"c":3})
graf={"tipo":"plano","x":[-4.03,4.03],"y":[-2.4,2.4],"a":0,"b":1.57079633,"inicio":0,"elementos":EL,
 "lecturas":[{"rotulo":"divergencia del campo, 2 coseno de alfa","formula":"2*cos(x)"},{"rotulo":"rotacional del campo, 2 seno de alfa","formula":"2*sin(x)"}],
 "etiquetas":["Con alfa igual a 0 el campo sale del origen, y la divergencia es 2","Con alfa igual a pi medios el campo gira, y el rotacional es 2"],"etiquetaSlider":"Ángulo alfa, de 0 a 1.57",
 "alt":"El campo F igual a coseno de alfa por x, y más seno de alfa por menos y, x. Con alfa igual a 0 las flechas apuntan hacia afuera del origen y el campo se expande, con divergencia 2 y rotacional 0. Con alfa igual a pi medios las flechas giran alrededor del origen, con divergencia 0 y rotacional 2"}
glos={"divergencia":"La divergencia de un campo mide cuánto se expande o se comprime en un punto, y es la suma de las derivadas parciales de cada componente.",
 "rotacional":"El rotacional de un campo mide cuánto gira el campo alrededor de un punto. En dos dimensiones es Q sub x menos P sub y.",
 "nabla":"El operador nabla es el vector de derivadas parciales. Con producto punto da la divergencia, y con producto cruz da el rotacional.",
 "identidades":"Para campos suaves, el rotacional de un gradiente es cero, y la divergencia de un rotacional es cero."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se mira un campo que mezcla dos comportamientos, uno que sale del origen y otro que gira alrededor."],
 [4,10,"Con alfa igual a 0 el campo es x, y. Las flechas salen del origen, y la divergencia es 2."],
 [10,16,"Con alfa igual a 0.8 el campo sale y gira a la vez. La divergencia baja y el rotacional sube."],
 [16,20,"Con alfa igual a pi medios el campo es menos y, x. Solo gira, la divergencia es 0 y el rotacional es 2."],
 [20,24,"La divergencia mide la expansión y el rotacional mide el giro, y son dos medidas distintas. En general son independientes, y en este campo particular quedan ligadas por el ángulo alfa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0.8],[13,0.8],[16,1.57079633],[18,1.57079633],[24,1.57079633]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La {{gl:divergencia|divergencia}} mide si el campo se expande en un punto, y el {{gl:rotacional|rotacional}} mide si gira. Ambos se calculan con el operador {{gl:nabla|nabla}}. Hay dos {{gl:identidades|identidades}} que siempre se cumplen para campos suaves, y se usan para verificar cálculos.")),
 sec("Un ejemplo","Un ejemplo",P("El campo mezcla una expansión y un giro con el ángulo alfa. Cambia alfa y mira la divergencia y el rotacional."),EQ("\\mathbf{F}=(x\\cos\\alpha-y\\operatorname{sen}\\alpha,\\ x\\operatorname{sen}\\alpha+y\\cos\\alpha),\\quad \\nabla\\cdot\\mathbf{F}=2\\cos\\alpha,\\quad \\nabla\\times\\mathbf{F}=2\\operatorname{sen}\\alpha"),{"t":"grafica","animar":"dibujar","alt":"El campo con expansión y giro según alfa"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El campo es x, y, z. ¿Cuánto vale su divergencia?","opciones":[3,1,0,2],"correcta":3,"bien":"Muy bien. Es 1 más 1 más 1.","mal":"La divergencia suma las derivadas parciales de las componentes, y vale 3."}),
 sec("De la expansión al giro","Giro",P("Mira el campo con alfa igual a 0, 0.4, 0.8 y 1.57."),{"t":"acercando","ds":[0,0.4,0.8,1.57079633],"alt":"El campo con cuatro valores de alfa"},P("La divergencia baja de 2 a 0, y el rotacional sube de 0 a 2.")),
 sec("La divergencia","Divergencia",P("Se suman las derivadas parciales de las componentes."),
   PASOS([("\\mathbf{F}=(P,Q,R)\\ \\Rightarrow\\ \\nabla\\cdot\\mathbf{F}=P_{x}+Q_{y}+R_{z}","La definición."),
          ("\\mathbf{F}=(x,y,z):\\ 1+1+1=3","Un campo que sale del origen."),
          ("\\mathbf{F}=(x^{2},y^{2},z^{2}):\\ 2x+2y+2z","Otro campo."),
          ("(1,1,1):\\ 2+2+2=6","Evaluado en un punto.")]),
   OJO("La divergencia es un número, un campo escalar. El rotacional, en tres dimensiones, es un vector.")),
 sec("El rotacional","Rotacional",P("En tres dimensiones es un determinante, y en dos es una resta."),
   PASOS([("\\nabla\\times\\mathbf{F}=(R_{y}-Q_{z},\\ P_{z}-R_{x},\\ Q_{x}-P_{y})","La definición."),
          ("\\mathbf{F}=(-y,x,0):\\ \\nabla\\times\\mathbf{F}=(0,0,2)","El campo que gira."),
          ("\\nabla\\times(\\nabla f)=\\mathbf{0}","El rotacional de un gradiente es cero."),
          ("\\nabla\\cdot(\\nabla\\times\\mathbf{F})=0","La divergencia de un rotacional es cero.")]),
   OJO("Las dos identidades piden segundas derivadas continuas. Si el rotacional no es cero, el campo no es gradiente de nada, y no es conservativo.")),
 eng("El flujo de un fluido","En un fluido, la divergencia de la velocidad dice si hay fuentes o sumideros, y el rotacional dice si hay remolinos. En un fluido incompresible la divergencia es cero.","\\nabla\\cdot\\mathbf{v}=0\\ \\text{en un fluido incompresible}",
   [("Divergencia positiva","fuente"),("Divergencia negativa","sumidero"),("Rotacional distinto de cero","remolino")],"El agua se puede modelar como incompresible, y por eso su campo de velocidad tiene divergencia cero. El aire, a velocidades altas, ya no cumple eso."),
 completar("La divergencia del campo x, y, z vale [[hueco]].","\\nabla\\cdot(x,y,z)=[[hueco]]",
   [("3","tres"),("0","cero"),("1","uno")],0,
   ["","Cero sería de un campo con tantas fuentes como sumideros.","Uno solo tendría una componente que se expande."],"Es la suma de tres derivadas, cada una igual a 1.","Vale 3."),
 error("Alguien calculó la divergencia de x al cuadrado, y al cuadrado, z al cuadrado en 1, 1, 1 y se equivocó. Toca el paso que está mal.",
   [("P=x^{2},\\ Q=y^{2},\\ R=z^{2}","Componentes.","componentes"),
    ("\\nabla\\cdot\\mathbf{F}=x^{2}+y^{2}+z^{2}","Este paso es el que falla.","no deriva"),
    ("\\text{en }(1,1,1)=3","Resultado.","3")],1,
   "Hay que derivar cada componente respecto a su variable. La divergencia es 2x más 2y más 2z, y en 1, 1, 1 vale 6.",
   "\\nabla\\cdot\\mathbf{F}=2x+2y+2z=6","Deriva P respecto a x, Q respecto a y y R respecto a z."),
 ordenar("Estos son los pasos para calcular una divergencia, pero están desordenados.",
   [("\\mathbf{F}=(P,Q,R)","Se identifican las componentes"),
    ("P_{x},\\ Q_{y},\\ R_{z}","Se derivan cada una respecto a su variable"),
    ("P_{x}+Q_{y}+R_{z}","Se suman"),
    ("\\text{evaluar en el punto}","Se evalúa")],[2,0,3,1],
   "Primero las componentes, luego las derivadas, después la suma y al final se evalúa.","Se empieza identificando las componentes."),
]
S+=cierre("Mini simulacro de rotacional y divergencia",[
 banco("cv_c3_01","La divergencia de x y, y z, z x en 1, 1, 1."),
 banco("cv_c3_02","El rotacional del gradiente."),
 banco("cv_c3_13","El rotacional de un gradiente es cero."),
 banco("cv_c3_14","La divergencia de un rotacional es cero."),
 banco("cv_c3_15","La divergencia de x al cuadrado, y al cuadrado, z al cuadrado en 1, 1, 1.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1},"bloques":[P("El campo mezcla expansión y giro."),EQ("\\mathbf{F}=\\cos\\alpha\\,(x,y)+\\operatorname{sen}\\alpha\\,(-y,x)")]},
 {"titulo":"Cambia alfa","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la divergencia y el rotacional.")]},
 {"titulo":"Solo giro","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.57079633,"bloques":[EQ("\\nabla\\cdot\\mathbf{F}=0,\\quad \\nabla\\times\\mathbf{F}=2"),P("Con alfa igual a pi medios el campo solo gira.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.57079633},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Divergencia es expansión y rotacional es giro."}]}]
preg={"tex":"\\nabla\\cdot(x^{2},y^{2},z^{2})\\Big|_{(1,1,1)}\\ \\text{vale}","opciones":["$6$","$3$","$2$","$0$"],"correcta":0,
 "explicacion":"La divergencia es 2x más 2y más 2z, y en 1, 1, 1 vale 2 más 2 más 2, o sea 6.",
 "verificacion":{"formula":"2+2+2+0*x","a":0,"esperado":6},
 "pistas":["Deriva cada componente respecto a su variable.","Da 2x, 2y y 2z.","Evalúa en 1, 1, 1 y suma."],
 "errores":["","El 3 sería con las componentes x, y, z, sin elevar al cuadrado.","El 2 es solo una de las derivadas.","El 0 sería si las derivadas fueran cero."]}
res=["La divergencia es P sub x más Q sub y más R sub z, y mide la expansión.","El rotacional mide el giro, y en dos dimensiones es Q sub x menos P sub y.","El rotacional de un gradiente es cero, y la divergencia de un rotacional es cero."]
write(lesson("cv-m3-l2","Lección 2 de 5","Rotacional y divergencia",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-rotdiv.json")
