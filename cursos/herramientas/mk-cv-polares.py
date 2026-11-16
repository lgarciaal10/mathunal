import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
RS=[round(0.05*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(r),f"{4-r*r:.4f}"] for r in RS],"c":3},
    {"t":"segmento","a":["x","0"],"b":["x","4-x*x"],"c":1},
    {"t":"punto","p":["x","4-x*x"],"c":0}]
graf={"tipo":"plano","x":[-0.3,2.6],"y":[-0.6,4.7],"a":0,"b":2,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"altura del paraboloide en r, z igual a 4 menos r al cuadrado","formula":"4-x*x"},{"rotulo":"volumen bajo el paraboloide dentro del radio r","formula":"2*pi*(2*x*x-x*x*x*x/4)"}],
 "etiquetas":["La altura solo depende de r, y por eso el perfil basta para describir toda la superficie","El volumen crece con el radio R, y con R igual a 2 llega a 8 pi"],"etiquetaSlider":"Radio R, de 0 a 2",
 "alt":"El perfil de la superficie z igual a 4 menos r al cuadrado, que depende solo de la distancia r al eje. Al girar el perfil alrededor del eje se obtiene el paraboloide. El volumen dentro del radio R se calcula con una integral en coordenadas polares, y para R igual a 2 vale 8 pi"}
glos={"polares":"En coordenadas polares un punto se da por su distancia r al origen y su ángulo theta, con x igual a r coseno de theta y y igual a r seno de theta.",
 "elemento":"El elemento de área en polares es r dr d theta. El factor r aparece porque los pedazos lejos del origen son más grandes.",
 "disco":"Para un disco centrado en el origen, r va de 0 al radio y theta va de 0 a 2 pi.",
 "simetria":"Cuando la región o la función tienen simetría circular, las polares simplifican mucho la integral."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El paraboloide z igual a 4 menos x al cuadrado menos y al cuadrado solo depende de la distancia r al eje."],
 [4,10,"En polares, el área de un pedazo es r dr d theta, y la integral de volumen queda con ese factor r."],
 [10,16,"Con radio 1 el volumen es 3.5 pi, que es 11. Con radio 1.5 es cerca de 20.3."],
 [16,20,"Con radio 2 se llega al borde del paraboloide, y el volumen total es 8 pi, cerca de 25.1."],
 [20,24,"El factor r es lo que hace que la integral sea sencilla. Sin el factor, el resultado sería incorrecto."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.3],[8,0.3],[10,1],[13,1],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("En {{gl:polares|coordenadas polares}} se describe un punto por su distancia r y su ángulo theta. Cuando la región o la función tienen {{gl:simetria|simetría circular}}, la integral se simplifica. Se usa el {{gl:elemento|elemento de área}} r dr d theta, y un {{gl:disco|disco}} tiene límites constantes.")),
 sec("Un ejemplo","Un ejemplo",P("El paraboloide z igual a 4 menos r al cuadrado se integra sobre un disco. Mueve el radio y mira cómo crece el volumen."),EQ("V=\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{R}(4-r^{2})\\,r\\,dr\\,d\\theta=2\\pi\\left(2R^{2}-\\dfrac{R^{4}}{4}\\right)"),{"t":"grafica","animar":"dibujar","alt":"El perfil del paraboloide y el volumen hasta el radio R"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En polares, ¿cuál es el elemento de área?","opciones":["r dr d theta","dr d theta","r al cuadrado dr d theta","uno entre r dr d theta"],"correcta":"r dr d theta","bien":"Muy bien. El factor r es el jacobiano de las polares.","mal":"Es r dr d theta. El factor r aparece porque los pedazos crecen al alejarse del origen."}),
 sec("Hasta distintos radios","Radios",P("Mira el volumen con R igual a 0.5, 1, 1.5 y 2."),{"t":"acercando","ds":[0.5,1,1.5,2],"alt":"El volumen con cuatro radios"},P("A R igual a 2 se llega a 8 pi, cerca de 25.1.")),
 sec("Pasar a polares","Pasos",P("Se reemplazan las variables y se agrega el factor r."),
   PASOS([("x=r\\cos\\theta,\\quad y=r\\operatorname{sen}\\theta","El cambio."),
          ("x^{2}+y^{2}=r^{2},\\quad dA=r\\,dr\\,d\\theta","Se reemplaza el área y la suma de cuadrados."),
          ("x^{2}+y^{2}\\le1\\ \\Rightarrow\\ 0\\le r\\le1,\\ 0\\le\\theta\\le2\\pi","Los límites de un disco."),
          ("\\displaystyle\\iint_{D}dA=\\int_{0}^{2\\pi}\\!\\int_{0}^{1}r\\,dr\\,d\\theta=\\pi","El área del disco unidad.")]),
   OJO("El factor r no se puede olvidar. Sin él se calcularía otra cosa, y el área del disco no daría pi.")),
 sec("El volumen del paraboloide","Volumen",P("Se calcula el volumen bajo la superficie sobre el disco de radio 2."),
   PASOS([("V=\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{2}(4-r^{2})\\,r\\,dr\\,d\\theta","La integral en polares."),
          ("\\displaystyle\\int_{0}^{2}(4r-r^{3})\\,dr=\\left[2r^{2}-\\dfrac{r^{4}}{4}\\right]_{0}^{2}=8-4=4","La parte en r."),
          ("V=2\\pi\\cdot4=8\\pi","Se multiplica por la vuelta completa."),
          ("\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{2}r\\,dr\\,d\\theta=4\\pi\\approx12.5664","Un ejemplo sencillo, que es el área de un disco de radio 2.")]),
   OJO("Si la función solo depende de r, la integral en theta da 2 pi y se separa. Es la forma más corta de calcular volúmenes de revolución.")),
 eng("El tanque de forma paraboloide","Un depósito tiene un fondo con forma de paraboloide, de altura 4 metros en el centro y radio 2 metros. El volumen se calcula con una integral doble en polares.","V=\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{2}(4-r^{2})\\,r\\,dr\\,d\\theta=8\\pi\\approx25.1\\ \\text{m}^{3}",
   [("Altura","4 m"),("Radio","2 m"),("Volumen","cerca de 25.1 m³")],"En polares el cálculo es corto, mientras que en rectangulares aparecen raíces cuadradas en los límites. Esto vale para cualquier recipiente con simetría de giro."),
 completar("En coordenadas polares, el elemento de área es [[hueco]] dr d theta.","dA=[[hueco]]\\,dr\\,d\\theta",
   [("r","r"),("1","uno"),("r^{2}","r al cuadrado")],0,
   ["","Sin el factor r se calcularía mal el área.","Con r al cuadrado se calcularía un volumen de otra forma."],"Es el jacobiano de las polares.","Es r."),
 error("Alguien calculó el área del disco unidad en polares y se equivocó. Toca el paso que está mal.",
   [("0\\le r\\le1,\\quad 0\\le\\theta\\le2\\pi","Límites.","límites"),
    ("\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{1}dr\\,d\\theta","Este paso es el que falla.","falta el factor r"),
    ("=2\\pi","Resultado.","da 2 pi")],1,
   "Falta el factor r del elemento de área. La integral es 2 pi por la integral de r dr, o sea 2 pi por un medio, que da pi.",
   "\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{1}r\\,dr\\,d\\theta=\\pi","El elemento de área es r dr d theta."),
 ordenar("Estos son los pasos para integrar en polares, pero están desordenados.",
   [("x=r\\cos\\theta,\\ y=r\\operatorname{sen}\\theta","Se hace el cambio"),
    ("dA=r\\,dr\\,d\\theta","Se agrega el factor r"),
    ("0\\le r\\le R,\\ 0\\le\\theta\\le2\\pi","Se escriben los límites"),
    ("\\displaystyle\\int\\!\\int\\cdots\\,dr\\,d\\theta","Se integra")],[2,0,3,1],
   "Se hace el cambio, se agrega el factor r, se escriben los límites y se integra.","Se empieza con el cambio de variables."),
]
S+=cierre("Mini simulacro de coordenadas polares",[
 banco("cv_c2_02","El área del disco unidad en polares."),
 banco("cv_c2_04","El volumen bajo el paraboloide."),
 banco("cv_c2_09","El elemento de área en polares."),
 banco("cv_c2_10","La integral de r de 0 a 2 sobre la vuelta completa."),
 banco("cv_c2_11","La integral de r al cuadrado de 0 a 1.")])
prac=[
 {"titulo":"El paraboloide","grafica":{"draw":1},"bloques":[P("La altura depende solo de la distancia r al eje."),EQ("z=4-r^{2}")]},
 {"titulo":"Cambia el radio","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la altura en el borde del disco y el volumen hasta ese radio.")]},
 {"titulo":"El disco completo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("V=8\\pi\\approx25.13"),P("Con R igual a 2 se llega al borde del paraboloide.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"No olvides el factor r."}]}]
preg={"tex":"\\displaystyle\\int_{0}^{2\\pi}\\!\\int_{0}^{1}r\\cdot r\\,dr\\,d\\theta\\ \\text{vale}","opciones":["$\\dfrac{2\\pi}{3}$","$\\dfrac{\\pi}{3}$","$\\pi$","$2\\pi$"],"correcta":0,
 "explicacion":"La integral de r al cuadrado de 0 a 1 es un tercio, y se multiplica por 2 pi, o sea 2 pi tercios.",
 "verificacion":{"formula":"2*pi/3+0*x","a":0,"esperado":2.0944},
 "pistas":["La integral en r es r al cubo entre 3.","Evalúa de 0 a 1 y da un tercio.","Multiplica por 2 pi."],
 "errores":["","Un pi tercio olvidó la vuelta completa, que es 2 pi.","Pi sería la integral de r, y no de r al cuadrado.","2 pi olvidó integrar en r."]}
res=["En polares, dA es r dr d theta, y el factor r no se puede olvidar.","Un disco tiene r de 0 al radio y theta de 0 a 2 pi.","Con simetría circular, la integral se separa en r y en theta."]
write(lesson("cv-m2-l2","Lección 2 de 6","Coordenadas polares",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-polares.json")
