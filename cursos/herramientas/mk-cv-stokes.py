import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 3 Cálculo vectorial"
RS=[round(0.03*i,4) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(r),f"{2*math.pi*r*r:.4f}"] for r in RS],"c":3},
    {"t":"punto","p":["x","x*(2*pi*x)"],"c":0},
    {"t":"punto","p":["x","2*(pi*x*x)"],"c":3}]
graf={"tipo":"plano","x":[-0.1,1.35],"y":[-0.5,11],"a":0,"b":1.2,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"circulación de F igual a menos y, x, z, por la frontera, r por 2 pi r","formula":"x*(2*pi*x)"},{"rotulo":"flujo del rotacional por el disco, 2 por pi r al cuadrado","formula":"2*(pi*x*x)"}],
 "etiquetas":["Por la frontera, el campo mide r y es tangente a la circunferencia, que mide 2 pi r","Por la superficie, el rotacional vale 2 y el disco tiene área pi r al cuadrado"],"etiquetaSlider":"Radio r, de 0 a 1.2",
 "alt":"El teorema de Stokes con el campo F igual a menos y, x, 0 y un disco de radio r. La circulación sobre la circunferencia, que es r por 2 pi r, y el flujo del rotacional a través del disco, que es 2 por pi r al cuadrado, dan lo mismo para todo r. Se muestran como dos puntos sobre la misma curva"}
glos={"stokes":"El teorema de Stokes dice que la circulación de un campo sobre la frontera de una superficie es el flujo del rotacional a través de la superficie.",
 "gauss":"El teorema de la divergencia o de Gauss dice que el flujo de un campo a través de una superficie cerrada es la integral triple de la divergencia en el sólido que encierra.",
 "frontera":"La frontera de una superficie es la curva que la bordea, y la de un sólido es la superficie cerrada que lo envuelve.",
 "generalizacion":"Green, Stokes y Gauss son versiones del mismo principio, que relaciona una integral en el borde con una en el interior."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Stokes y Gauss dicen que una integral sobre el borde de un objeto es igual a una integral sobre su interior."],
 [4,10,"En Stokes, la circulación sobre la frontera de una superficie es el flujo del rotacional a través de ella."],
 [10,16,"Con el campo menos y, x, 0 y un disco de radio 1, la circulación es 2 pi, y el flujo del rotacional también."],
 [16,20,"Para cualquier radio los dos valores coinciden. Con r igual a 1.2 valen 9.05."],
 [20,24,"En Gauss, el flujo por una superficie cerrada es la integral de la divergencia en el interior. Con el campo x, y, z en la esfera unidad, da 4 pi."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.4],[8,0.4],[10,1],[13,1],[16,1.2],[18,1.2],[24,1.2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El teorema de {{gl:stokes|Stokes}} relaciona una circulación sobre una curva con un flujo del rotacional por una superficie. El de {{gl:gauss|Gauss}} o de la divergencia relaciona un flujo por una superficie cerrada con una integral triple. Ambos son una {{gl:generalizacion|generalización}} de Green, que usa siempre la {{gl:frontera|frontera}} de la región.")),
 sec("Un ejemplo","Un ejemplo",P("El campo menos y, x, 0 se integra sobre un disco de radio r. Mueve r y mira que los dos lados del teorema de Stokes coinciden."),EQ("\\oint_{\\partial S}\\mathbf{F}\\cdot d\\mathbf{r}=\\iint_{S}(\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}=2\\pi r^{2}"),{"t":"grafica","animar":"dibujar","alt":"La circulación y el flujo del rotacional, iguales"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El rotacional de menos y, x, 0 es 0, 0, 2. ¿Cuánto vale su flujo por un disco de área A en el plano horizontal?","opciones":["2A","A","0","A entre 2"],"correcta":"2A","bien":"Muy bien. La normal es 0, 0, 1, y el producto punto es 2.","mal":"La normal del disco horizontal es 0, 0, 1, y el producto punto con 0, 0, 2 vale 2. El flujo es 2A."}),
 sec("Dos formas de calcular","Dos lados",P("Mira los dos lados con r igual a 0.3, 0.6, 1 y 1.2."),{"t":"acercando","ds":[0.3,0.6,1,1.2],"alt":"Los dos lados de Stokes con cuatro radios"},P("En los cuatro casos los dos números son iguales.")),
 sec("El teorema de Stokes","Stokes",P("Se puede calcular por la curva o por la superficie, y se escoge la más corta."),
   PASOS([("\\oint_{C}\\mathbf{F}\\cdot d\\mathbf{r}=\\iint_{S}(\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}","El enunciado, con C la frontera de S."),
          ("\\mathbf{F}=(-y,x,0)\\ \\Rightarrow\\ \\nabla\\times\\mathbf{F}=(0,0,2)","El rotacional."),
          ("\\iint_{S}2\\,dA=2\\pi r^{2}","El flujo por el disco."),
          ("r=1\\ \\Rightarrow\\ 2\\pi","Es la misma circulación que dio Green.")]),
   OJO("La orientación de la curva y la de la superficie deben concordar, con la regla de la mano derecha. Si no, el resultado sale con el signo cambiado.")),
 sec("El teorema de la divergencia","Gauss",P("El flujo hacia afuera de una superficie cerrada es una integral triple."),
   PASOS([("\\iint_{S}\\mathbf{F}\\cdot d\\mathbf{S}=\\iiint_{E}(\\nabla\\cdot\\mathbf{F})\\,dV","El enunciado, con S la frontera de E."),
          ("\\mathbf{F}=(x,y,z)\\ \\Rightarrow\\ \\nabla\\cdot\\mathbf{F}=3","La divergencia."),
          ("\\iiint_{E}3\\,dV=3\\cdot\\dfrac{4\\pi}{3}=4\\pi","El volumen de la esfera unidad por 3."),
          ("\\text{flujo}=4\\pi\\approx12.5664","Coincide con el cálculo directo.")]),
   OJO("El teorema pide una superficie cerrada, con normal hacia afuera. Si le falta una tapa, hay que sumar el flujo de la tapa que falta.")),
 eng("Una ley física en dos formas","La ley de Gauss en electricidad dice que el flujo del campo eléctrico por una superficie cerrada es la carga encerrada dividida entre una constante. Con el teorema de la divergencia, esa ley también se escribe con una ecuación local.","\\nabla\\cdot\\mathbf{E}=\\dfrac{\\rho}{\\varepsilon_{0}}",
   [("Forma integral","flujo por una superficie"),("Forma local","divergencia en cada punto"),("Puente","teorema de la divergencia")],"Esto es lo que usan las ecuaciones de Maxwell. Con Stokes, las otras dos leyes pasan de integrales de línea a ecuaciones con rotacional."),
 completar("El teorema de la divergencia dice que el flujo por una superficie cerrada es la integral triple de la [[hueco]].","\\iint_{S}\\mathbf{F}\\cdot d\\mathbf{S}=\\iiint_{E}[[hueco]]\\,dV",
   [("\\nabla\\cdot\\mathbf{F}","divergencia"),("\\nabla\\times\\mathbf{F}","rotacional"),("\\|\\mathbf{F}\\|","la norma de F")],0,
   ["","El rotacional aparece en Stokes, y no en Gauss.","La norma de F no resulta de un teorema de este tipo."],"Gauss usa la divergencia.","Es la divergencia."),
 error("Alguien aplicó el teorema de Stokes a menos y, x, 0 sobre un disco de radio 1 y se equivocó. Toca el paso que está mal.",
   [("\\nabla\\times\\mathbf{F}=(0,0,2)","Rotacional.","rotacional"),
    ("\\oint\\mathbf{F}\\cdot d\\mathbf{r}=\\iint2\\,dA=2","Este paso es el que falla.","olvida el área"),
    ("\\text{circulacion}=2","Resultado.","2")],1,
   "La integral doble de 2 sobre el disco es 2 por el área, que es pi. Entonces la circulación vale 2 pi, y no 2.",
   "\\iint_{D}2\\,dA=2\\pi","El área del disco es pi por r al cuadrado."),
 ordenar("Estos son los pasos para aplicar el teorema de la divergencia, pero están desordenados.",
   [("S=\\partial E","Se verifica que S sea cerrada"),
    ("\\nabla\\cdot\\mathbf{F}","Se calcula la divergencia"),
    ("\\iiint_{E}(\\nabla\\cdot\\mathbf{F})\\,dV","Se plantea la integral triple"),
    ("\\text{flujo}","Se calcula el flujo")],[2,0,3,1],
   "Se verifica la superficie, se calcula la divergencia, se plantea la integral triple y se obtiene el flujo.","Se empieza verificando que la superficie sea cerrada."),
]
S+=cierre("Mini simulacro de los teoremas de Stokes y de la divergencia",[
 banco("cv_c3_16","El teorema de la divergencia."),
 banco("cv_c3_17","El teorema de Stokes."),
 pnum("Con el campo $\\mathbf{F}=(x,y,z)$, el flujo hacia afuera de la esfera unidad es, por el teorema de la divergencia (decimal, 4 cifras):","12.5664",0.001,"La divergencia es 3, y el volumen de la esfera unidad es 4 pi sobre 3. El flujo es 4 pi.")])
prac=[
 {"titulo":"El campo","grafica":{"draw":1},"bloques":[P("El campo gira alrededor del eje z."),EQ("\\mathbf{F}=(-y,x,0)")]},
 {"titulo":"Cambia el radio","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la circulación por la frontera y el flujo del rotacional por el disco.")]},
 {"titulo":"Con r igual a 1.2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.2,"bloques":[EQ("2\\pi(1.44)\\approx9.05"),P("Los dos lados dan lo mismo, como dice Stokes.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Stokes usa el rotacional, y Gauss usa la divergencia."}]}]
preg={"tex":"\\oint_{C}\\mathbf{F}\\cdot d\\mathbf{r}\\ \\text{con}\\ C=\\partial S\\ \\text{es igual a}","opciones":["$\\displaystyle\\iint_{S}(\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}$","$\\displaystyle\\iint_{S}(\\nabla\\cdot\\mathbf{F})\\,dS$","$\\displaystyle\\iiint_{E}\\mathbf{F}\\,dV$","$\\displaystyle\\iint_{S}\\mathbf{F}\\cdot d\\mathbf{S}$"],"correcta":0,
 "explicacion":"Es el teorema de Stokes. La circulación sobre la frontera es el flujo del rotacional por la superficie.",
 "verificacion":{"formula":"2*pi*1*1+0*x","a":0,"esperado":6.2832},
 "pistas":["Es una circulación sobre una curva que es el borde de una superficie.","Es el teorema de Stokes.","Involucra el rotacional."],
 "errores":["","La divergencia aparece en el teorema de Gauss, y no en el de Stokes.","Una integral triple de F no sale de ninguno de los teoremas.","Ese es el flujo de F, pero no la circulación."]}
res=["Stokes iguala la circulación sobre la frontera con el flujo del rotacional por la superficie.","Gauss iguala el flujo por una superficie cerrada con la integral triple de la divergencia.","Green, Stokes y Gauss relacionan una integral en el borde con una en el interior."]
write(lesson("cv-m3-l5","Lección 5 de 5","Teoremas de Stokes y de la divergencia",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-stokes.json")
