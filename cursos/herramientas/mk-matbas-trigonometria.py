import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 3 Funciones, trigonometría y geometría analítica"
CIR=[[f"cos({2*math.pi*k/72:.4f})",f"sin({2*math.pi*k/72:.4f})"] for k in range(73)]
graf={"tipo":"plano","x":[-2.75,2.75],"y":[-1.5,1.5],"a":0,"b":6.283185,"inicio":0.523599,
 "elementos":[{"t":"trazo","puntos":CIR,"c":3},
  {"t":"segmento","a":["0","0"],"b":["cos(x)","sin(x)"],"c":2},
  {"t":"segmento","a":["cos(x)","0"],"b":["cos(x)","sin(x)"],"c":1,"guia":True,"guion":True},
  {"t":"punto","p":["cos(x)","sin(x)"],"c":2}],
 "lecturas":[{"rotulo":"seno","formula":"sin(x)"},{"rotulo":"coseno","formula":"cos(x)"}],
 "etiquetas":["Seno del ángulo","Coseno del ángulo"],"etiquetaSlider":"Ángulo en radianes",
 "alt":"El círculo de radio 1. Un punto sobre él, a un ángulo que se mueve, tiene como coordenada horizontal el coseno y como coordenada vertical el seno. Con 30 grados el seno vale 0.5 y el coseno 0.866"}
glos={"radian":"Un radián es el ángulo que abarca un arco igual al radio. Una vuelta completa son 2 pi radianes, que equivalen a 360 grados.",
 "circulounitario":"El círculo unitario tiene radio 1 y centro en el origen. El punto a un ángulo θ tiene coordenadas coseno de θ y seno de θ.",
 "identidad":"Una identidad trigonométrica es una igualdad que se cumple para cualquier ángulo. La más importante es seno al cuadrado más coseno al cuadrado igual a 1."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El círculo unitario tiene radio 1. Un punto sobre él queda determinado por el ángulo, medido desde el eje horizontal hacia arriba."],
 [4,8,"Las coordenadas del punto son el coseno y el seno del ángulo. Eso es lo que significan esas dos funciones."],
 [8,14,"Mueve el ángulo. El seno es la altura y el coseno es el desplazamiento horizontal. Los dos cambian de signo según el cuadrante."],
 [14,18,"Con 45 grados, que son pi sobre 4 radianes, las dos coordenadas son iguales, 0.707, y la tangente vale 1."],
 [18,22,"Con 30 grados el seno vale 0.5 y el coseno vale 0.866."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.523599],[8,0.523599],[11,3.141593],[13,5.2],[14,0.785398],[17,0.785398],[18,0.523599],[22,0.523599]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("La trigonometría relaciona ángulos con longitudes. En un triángulo rectángulo, el seno, el coseno y la tangente son cocientes entre lados. En el {{gl:circulounitario|círculo unitario}} son coordenadas de un punto, y eso permite usarlas con cualquier ángulo. Los ángulos se miden en grados o en {{gl:radian|radianes}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira un punto que se mueve sobre el círculo de radio 1."),EQ("(x,y)=(\\cos\\theta,\\ \\operatorname{sen}\\theta)"),{"t":"grafica","animar":"dibujar","alt":"El círculo unitario"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En un triángulo rectángulo el seno es el cateto opuesto sobre la hipotenusa. Con opuesto 3 e hipotenusa 5, ¿cuánto vale el seno?","opciones":[0.4,0.6,0.8,1.67],"correcta":0.6,"bien":"Muy bien. Vale 0.6. Entonces el coseno, por Pitágoras, vale 0.8.","mal":"Vale 0.6, porque 3 dividido entre 5 es 0.6. Entonces el coseno, por Pitágoras, vale 0.8."}),
 sec("Moviendo el ángulo","El ángulo",P("Mira el seno y el coseno en algunos ángulos conocidos."),{"t":"acercando","ds":[0.523599,0.785398,1.570796,3.141593],"alt":"El seno y el coseno en varios ángulos"},P("En 30, 45, 90 y 180 grados los valores son exactos y conviene saberlos de memoria.")),
 sec("Razones y ángulos notables","Razones",P("En un triángulo rectángulo, las razones se definen con los lados."),
   PASOS([("\\operatorname{sen}\\theta=\\dfrac{\\text{op}}{\\text{hip}},\\quad \\cos\\theta=\\dfrac{\\text{ady}}{\\text{hip}},\\quad \\tan\\theta=\\dfrac{\\text{op}}{\\text{ady}}","Las tres razones."),
          ("\\operatorname{sen}30^{\\circ}=\\tfrac{1}{2},\\ \\ \\operatorname{sen}45^{\\circ}=\\tfrac{\\sqrt{2}}{2},\\ \\ \\operatorname{sen}60^{\\circ}=\\tfrac{\\sqrt{3}}{2}","El seno de los ángulos notables."),
          ("\\tan45^{\\circ}=1,\\quad 180^{\\circ}=\\pi\\ \\text{rad}","La tangente de 45 grados y la equivalencia entre unidades.")])),
 sec("Identidades y ecuaciones","Identidades",P("Hay una identidad fundamental que sale del teorema de Pitágoras."),
   PASOS([("\\operatorname{sen}^{2}x+\\cos^{2}x=1","Se cumple para todo x."),
          ("\\operatorname{sen}\\theta=\\tfrac{3}{5}\\ \\Rightarrow\\ \\cos^{2}\\theta=1-\\tfrac{9}{25}=\\tfrac{16}{25}\\ \\Rightarrow\\ \\cos\\theta=\\tfrac{4}{5}","Con el ángulo agudo, el coseno es positivo."),
          ("\\cos x=0\\ \\text{en}\\ [0,2\\pi)\\ \\Rightarrow\\ x=\\tfrac{\\pi}{2},\\ \\tfrac{3\\pi}{2}","Las soluciones de una ecuación sencilla.")]),
   OJO("El signo del seno y del coseno depende del cuadrante. En el segundo cuadrante el seno es positivo y el coseno es negativo.")),
 eng("Una rampa de carga","Una rampa de 4 metros de largo se inclina 15 grados para subir un equipo a una plataforma. La altura que alcanza y la distancia horizontal salen de seno y coseno.","h=L\\operatorname{sen}\\theta,\\qquad d=L\\cos\\theta",
   [("Largo","4 m"),("Inclinación","15 grados"),("Altura","1.04 m")],"La altura es 4 por el seno de 15 grados, unos 1.04 metros. La distancia horizontal es 4 por el coseno de 15 grados, unos 3.86 metros. Si se aumenta la inclinación a 30 grados, la altura sube a 2 metros, pero la rampa es más empinada y cuesta más empujar el equipo. Es un cálculo geométrico, que no incluye la fricción."),
 completar("Se completa la identidad fundamental.","\\operatorname{sen}^{2}x+\\cos^{2}x=[[hueco]]",
   [("1","uno"),("0","cero"),("2","dos")],0,
   ["","Con 0 los cuadrados tendrían que ser opuestos, y los dos son positivos o cero.","Con 2 se estaría sumando dos veces el valor máximo. En el círculo unitario la suma es 1."],"Es el teorema de Pitágoras en el círculo de radio 1.","La hipotenusa es 1, y 1 al cuadrado es 1."),
 error("Alguien halló el coseno de un ángulo agudo con seno 3 sobre 5 y se equivocó en un paso. Toca el paso que está mal.",
   [("\\cos^{2}\\theta=1-\\operatorname{sen}^{2}\\theta","La identidad despejada.","se despeja el coseno al cuadrado"),
    ("\\cos^{2}\\theta=1-\\tfrac{3}{5}=\\tfrac{2}{5}","Este paso es el que falla.","queda 1 menos 3 quintos, igual a 2 quintos"),
    ("\\cos\\theta=\\sqrt{2/5}","El resultado.","el coseno es la raíz de 2 quintos")],1,
   "Falta elevar el seno al cuadrado. Es 3 sobre 5 al cuadrado, o sea 9 sobre 25. Queda 1 menos 9 sobre 25, o sea 16 sobre 25, y el coseno vale 4 sobre 5.",
   "\\cos^{2}\\theta=1-\\tfrac{9}{25}=\\tfrac{16}{25}","Fíjate en el cuadrado del seno."),
 ordenar("Estos son los pasos para resolver coseno de x igual a 0 entre 0 y 2 pi, pero están desordenados.",
   [("\\cos x=0","La ecuación"),
    ("x=\\tfrac{\\pi}{2}+k\\pi","Todas las soluciones"),
    ("k=0,\\ 1\\ \\text{caen en}\\ [0,2\\pi)","Se eligen las que están en el intervalo"),
    ("x=\\tfrac{\\pi}{2},\\ \\tfrac{3\\pi}{2}","Las soluciones")],[2,0,3,1],
   "Se escribe la forma general, se eligen los valores en el intervalo y se listan.","Se empieza con la ecuación."),
]
S+=cierre("Mini simulacro de trigonometría",[
 banco("mb_c3_10","El seno de $30^\\circ$ es $\\tfrac{1}{2}=0.5$."),
 banco("mb_c3_11","Por Pitágoras, $\\cos\\theta=\\sqrt{1-(3/5)^2}=\\tfrac{4}{5}=0.8$."),
 banco("mb_c3_13","Es la identidad fundamental, $\\operatorname{sen}^2x+\\cos^2x=1$.")])
prac=[
 {"titulo":"El círculo","grafica":{"draw":1,"guide":1},"bloques":[P("Un punto sobre el círculo de radio 1."),EQ("(\\cos\\theta,\\ \\operatorname{sen}\\theta)")]},
 {"titulo":"Mueve el ángulo","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el seno y el coseno.")]},
 {"titulo":"Treinta grados","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.523599,"bloques":[EQ("\\operatorname{sen}30^{\\circ}=\\tfrac{1}{2}"),P("Con pi sobre 6 radianes el seno vale 0.5.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.523599},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Piensa en el cuadrante del ángulo."}]}]
preg={"tex":"\\operatorname{sen}150^{\\circ}\\ \\text{vale}","opciones":["$\\tfrac{1}{2}$","$-\\tfrac{1}{2}$","$\\tfrac{\\sqrt{3}}{2}$","$-\\tfrac{\\sqrt{3}}{2}$"],"correcta":0,
 "explicacion":"150 grados está en el segundo cuadrante, donde el seno es positivo. Su ángulo de referencia es 30 grados, y el seno de 30 es un medio.",
 "verificacion":{"formula":"sin(150*pi/180)+0*x","a":0,"esperado":0.5},
 "pistas":["Ubica el ángulo en un cuadrante.","En el segundo cuadrante el seno es positivo.","El ángulo de referencia es 180 menos 150."],
 "errores":["","El seno es positivo en el segundo cuadrante. El signo menos aparece en el tercero y el cuarto.","Ese es el seno de 60 o de 120 grados, y el ángulo de referencia de 150 es 30.","Ese valor es negativo y es el de otro cuadrante, y tampoco es el ángulo de referencia de 30."]}
res=["En un triángulo rectángulo, seno es opuesto sobre hipotenusa, coseno es adyacente sobre hipotenusa y tangente es opuesto sobre adyacente.","En el círculo unitario, el punto del ángulo es coseno y seno.","Seno al cuadrado más coseno al cuadrado vale siempre 1."]
write(lesson("mb-m3-l1","Lección 1 de 4","Trigonometría",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=15,curso="Matemáticas Básicas"),"matbas-trigonometria.json")
