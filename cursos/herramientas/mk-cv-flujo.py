import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 3 Cálculo vectorial"
RS=[round(0.035*i,4) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(r),f"{4*math.pi*r*r:.4f}"] for r in RS],"c":3},
    {"t":"trazo","puntos":[[str(r),f"{4*math.pi*r**3:.4f}"] for r in RS],"c":0},
    {"t":"punto","p":["x","4*pi*x*x"],"c":3},
    {"t":"punto","p":["x","4*pi*x*x*x"],"c":0}]
graf={"tipo":"plano","x":[-0.1,1.55],"y":[-2,45],"a":0,"b":1.4,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"área de la esfera de radio R, 4 pi R al cuadrado","formula":"4*pi*x*x"},{"rotulo":"flujo de x, y, z hacia afuera, igual a R por el área","formula":"4*pi*x*x*x"}],
 "etiquetas":["El área de la superficie crece con el cuadrado del radio","El flujo crece con el cubo, porque el campo también crece con R"],"etiquetaSlider":"Radio R, de 0 a 1.4",
 "alt":"El área de una esfera de radio R, que es 4 pi R al cuadrado, y el flujo hacia afuera del campo x, y, z a través de ella. Sobre la esfera el campo es perpendicular a la superficie y mide R, así que el flujo es R por el área, 4 pi R al cubo. Con R igual a 1 el flujo vale 4 pi, cerca de 12.57"}
glos={"superficie":"Una superficie se puede describir con una parametrización, y su elemento de área dS mide el tamaño de un pedacito.",
 "flujo":"El flujo de un campo a través de una superficie es la integral de F punto n dS, y mide cuánto campo atraviesa la superficie.",
 "normal":"La normal es el vector perpendicular a la superficie. En una superficie cerrada se toma hacia afuera.",
 "orientacion":"La orientación elige hacia qué lado se cuenta el flujo, y cambiarla cambia el signo."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se mide cuánto campo atraviesa una esfera, con el campo x, y, z que sale del origen."],
 [4,10,"En cada punto de la esfera el campo es perpendicular a la superficie, y su módulo es igual al radio R."],
 [10,16,"Entonces el flujo es R por el área, que es 4 pi R al cubo. Con R igual a 1 vale 4 pi, cerca de 12.57."],
 [16,20,"Con R igual a 1.4 el flujo es 34.5, y el área es 24.6. El flujo crece más rápido que el área."],
 [20,24,"El flujo cuenta el campo que atraviesa, y cambia de signo si se invierte la orientación."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.4],[8,0.4],[10,1],[13,1],[16,1.4],[18,1.4],[24,1.4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("El {{gl:flujo|flujo}} de un campo a través de una {{gl:superficie|superficie}} mide cuánto campo la atraviesa. Se calcula como la integral de F por la {{gl:normal|normal}}, y la {{gl:orientacion|orientación}} define el signo. En una superficie cerrada se usa la normal hacia afuera, y el flujo total dice si hay fuentes adentro.")),
 sec("Un ejemplo","Un ejemplo",P("El campo x, y, z sale del origen. Mueve el radio de la esfera y mira el flujo."),EQ("\\iint_{S}\\mathbf{F}\\cdot d\\mathbf{S}=\\iint_{S}R\\,dS=R\\cdot4\\pi R^{2}=4\\pi R^{3}"),{"t":"grafica","animar":"dibujar","alt":"El área y el flujo según el radio"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Sobre la esfera de radio R, el campo x, y, z apunta hacia afuera. ¿Qué ángulo hace con la normal?","opciones":["Ninguno, es paralelo","90 grados","180 grados","45 grados"],"correcta":"Ninguno, es paralelo","bien":"Muy bien. Por eso F punto n es igual al módulo de F, que es R.","mal":"Son paralelos, porque la normal de la esfera apunta hacia afuera igual que el campo. Entonces F punto n vale R."}),
 sec("Distintos radios","Radios",P("Mira el flujo con radios 0.4, 1, 1.2 y 1.4."),{"t":"acercando","ds":[0.4,1,1.2,1.4],"alt":"El flujo con cuatro radios"},P("Con R igual a 1 el flujo es 4 pi, cerca de 12.57.")),
 sec("El flujo por una esfera","Esfera",P("Se calcula el flujo por una esfera con el campo radial."),
   PASOS([("\\mathbf{F}=(x,y,z),\\quad \\mathbf{n}=\\dfrac{(x,y,z)}{R}","El campo y la normal hacia afuera."),
          ("\\mathbf{F}\\cdot\\mathbf{n}=\\dfrac{x^{2}+y^{2}+z^{2}}{R}=R","Sobre la esfera, el producto punto es R."),
          ("\\iint_{S}R\\,dS=R\\cdot\\text{area}(S)=R\\cdot4\\pi R^{2}","Se multiplica por el área."),
          ("R=1\\ \\Rightarrow\\ 4\\pi\\approx12.5664","El flujo por la esfera unidad.")]),
   OJO("Se usa la normal hacia afuera en una superficie cerrada. Si se usa la normal hacia adentro, el flujo cambia de signo.")),
 sec("El flujo por una cara","Cara",P("Para una superficie plana, el flujo es más corto."),
   PASOS([("\\mathbf{F}=(0,0,z),\\quad z=1\\ \\text{cara superior del cubo}","El campo y la cara."),
          ("\\mathbf{n}=(0,0,1)","La normal hacia arriba."),
          ("\\mathbf{F}\\cdot\\mathbf{n}=z=1","El producto punto en la cara."),
          ("\\Phi=\\displaystyle\\iint_{[0,1]^{2}}1\\,dA=1","El flujo por la cara.")]),
   OJO("En una cara plana, F punto n suele ser constante, y la integral se reduce a esa constante por el área de la cara.")),
 eng("Una ventilación en un ducto","El aire se mueve por un ducto, y se quiere saber cuánto caudal pasa por una sección. El caudal es el flujo del campo de velocidad a través de la sección.","Q=\\iint_{S}\\mathbf{v}\\cdot\\mathbf{n}\\,dS",
   [("Velocidad","2 m/s perpendicular"),("Área de la sección","0.5 m²"),("Caudal","1 m³/s")],"Si el aire entra de forma inclinada, solo cuenta la componente perpendicular a la sección. Por eso en el flujo aparece el producto punto con la normal."),
 completar("El flujo del campo F a través de una superficie con normal n es la integral de F [[hueco]] n dS.","\\Phi=\\iint_{S}\\mathbf{F}\\ [[hueco]]\\ \\mathbf{n}\\,dS",
   [("\\cdot","el producto punto"),("\\times","el producto cruz"),("+","la suma")],0,
   ["","El producto cruz da un vector, y el flujo es un número.","La suma da un vector, y no un número."],"Solo cuenta la componente perpendicular a la superficie.","Es el producto punto."),
 error("Alguien calculó el flujo de 0, 0, z por la cara superior del cubo y se equivocó. Toca el paso que está mal.",
   [("\\mathbf{n}=(0,0,1)","Normal.","normal"),
    ("\\mathbf{F}\\cdot\\mathbf{n}=0","Este paso es el que falla.","cero"),
    ("\\Phi=0","Resultado.","cero")],1,
   "El producto punto de 0, 0, z con 0, 0, 1 es z, que en la cara superior vale 1. Entonces el flujo es 1 por el área de la cara, o sea 1.",
   "\\mathbf{F}\\cdot\\mathbf{n}=z=1","Multiplica solo la tercera componente."),
 ordenar("Estos son los pasos para calcular un flujo, pero están desordenados.",
   [("S,\\ \\mathbf{n}","Se escoge la superficie y su normal"),
    ("\\mathbf{F}\\cdot\\mathbf{n}","Se calcula el producto punto"),
    ("\\iint_{S}\\mathbf{F}\\cdot\\mathbf{n}\\,dS","Se plantea la integral"),
    ("\\Phi","Se calcula")],[2,0,3,1],
   "Se escoge la superficie con su normal, se hace el producto punto, se plantea la integral y se calcula.","Se empieza escogiendo la normal."),
]
S+=cierre("Mini simulacro de flujo y superficies",[
 banco("cv_c3_05","El flujo por la cara superior del cubo."),
 banco("cv_c3_18","El flujo del campo x, y, z por la esfera unidad."),
 pnum("El área de la esfera de radio 1 es (decimal, 4 cifras):","12.5664",0.001,"Es 4 pi por 1 al cuadrado, o sea 4 pi.")])
prac=[
 {"titulo":"La esfera","grafica":{"draw":1},"bloques":[P("El campo sale del origen."),EQ("\\mathbf{F}=(x,y,z),\\quad S:\\ x^{2}+y^{2}+z^{2}=R^{2}")]},
 {"titulo":"Cambia R","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el área de la esfera y el flujo.")]},
 {"titulo":"Con R igual a 1","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("\\Phi=4\\pi\\approx12.57"),P("Con R igual a 1 el flujo es 4 pi.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Solo cuenta la componente perpendicular."}]}]
preg={"tex":"\\mathbf{F}=(0,0,z),\\ \\text{cara}\\ z=1\\ \\text{de}\\ [0,1]^{3}.\\ \\Phi\\ \\text{vale}","opciones":["$1$","$0$","$\\tfrac12$","$3$"],"correcta":0,
 "explicacion":"En la cara superior, F punto n es z, que vale 1. El área de la cara es 1, y el flujo es 1.",
 "verificacion":{"formula":"1*1+0*x","a":0,"esperado":1},
 "pistas":["La normal de la cara superior es 0, 0, 1.","F punto n vale z.","En la cara, z vale 1."],
 "errores":["","El cero sería con una cara lateral, donde el campo no la atraviesa.","Un medio sería con el campo z sobre un triángulo.","El 3 sería con las tres componentes."]}
res=["El flujo es la integral de F punto n sobre la superficie, y mide el campo que la atraviesa.","En una superficie cerrada se usa la normal hacia afuera.","Cambiar la orientación cambia el signo del flujo."]
write(lesson("cv-m3-l4","Lección 4 de 5","Integrales de superficie y flujo",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-flujo.json")
