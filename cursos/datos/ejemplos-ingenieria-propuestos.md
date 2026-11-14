# Ejemplos de ingeniería propuestos para las lecciones

Este documento es para que Lucho lo revise antes de meter los ejemplos en las lecciones. La regla de la cadena ya tiene el suyo, el pistón de un motor. Las cifras de cada ejemplo las calculé y las verifiqué, pero que un número sea correcto no garantiza que el caso suene real a un ingeniero. Por eso cada ejemplo trae una calificación de confianza.

Cómo leer la confianza
- **Alta** significa un caso clásico de ingeniería con cifras razonables.
- **Media** significa que el caso existe, pero las cifras o el planteamiento necesitan tu ojo.
- **Baja** significa que el vínculo con ingeniería es débil y prefiero que me des un caso tuyo.

## Módulo 1, Funciones, límites y continuidad

**1. Qué es un límite** (confianza media). Velocidad instantánea con un sensor que mide la posición en intervalos de tiempo cada vez más cortos. Con s(t) = t² metros, el cociente (s(2.1) − s(2)) sobre 0.1 da 4.1 m/s, y al achicar el intervalo se acerca a 4 m/s. Es más conceptual que de ingeniería.

**2. Límites por factorización** (confianza baja). Simplificar una fórmula que da 0 sobre 0 en un punto, como las fórmulas de deflexión de vigas con carga por tramos. No tengo un caso con cifras que me convenza. Necesito uno tuyo.

**3. Límites notables** (confianza alta). El péndulo y la aproximación de ángulos pequeños. Con un ángulo de 10° (0.1745 rad), sen θ vale 0.17365 y usar θ en su lugar produce un error de 0.51 %. Con 30° el error ya es de 4.7 %. Eso explica hasta dónde se puede usar la aproximación.

**4. Continuidad** (confianza media). La temperatura en la pared de dos materiales en contacto. La temperatura no puede dar un salto en la interfaz, así que la función por tramos tiene que ser continua. Las constantes de cada tramo se calculan imponiendo esa condición. Falta fijar materiales y espesores reales.

**5. Límites al infinito** (confianza alta). El enfriamiento de una pieza. Con T(t) = 25 + 175·e^(−t/120) en °C y t en segundos, la temperatura tiende a 25 °C. A los 600 s vale 26.18 °C.

**6. Asíntotas** (confianza alta). La velocidad terminal de un objeto que cae con resistencia del aire, v(t) = 40·tanh(9.81·t/40) en m/s. La asíntota horizontal es 40 m/s. A los 5 s vale 33.7 m/s y a los 10 s vale 39.4 m/s.

## Módulo 2, La derivada y sus reglas

**7. La derivada como pendiente** (confianza media). La pendiente de la curva esfuerzo contra deformación es el módulo de elasticidad. Para el acero, cerca de 200 GPa. Falta decidir si se usa una curva real del acero o un modelo.

**8. Reglas de derivación** (confianza alta). La pendiente de una viga empotrada con carga puntual en el extremo. Con P = 1000 N, L = 2 m, E = 200 GPa e I = 8·10⁻⁶ m⁴, la pendiente en el extremo es 0.00125 rad y la flecha máxima es 1.67 mm.

**9. Derivación implícita** (confianza alta). Un proceso adiabático del aire cumple P·V^1.4 = constante. Derivando se obtiene dP/dV = −1.4·P/V. Con P = 100 kPa y V = 0.02 m³ sale −7·10⁶ Pa por m³.

**10. Razón de cambio** (confianza alta). Un tanque cilíndrico de 0.5 m de radio que se llena a 20 litros por segundo. El nivel sube 0.0255 m/s, o sea 2.5 cm por segundo.

**11. Movimiento rectilíneo** (confianza alta). El frenado de un carro que va a 20 m/s, unos 72 km/h, con desaceleración de 5 m/s². Se detiene en 4 s y recorre 40 m.

**12. Recta tangente y normal** (confianza media). El reflector parabólico de un faro, con foco a 5 cm. En x = 10 cm la tangente tiene pendiente 1 y la normal tiene pendiente −1. Es el principio de la reflexión hacia el foco.

**13. Aproximación lineal** (confianza alta). La dilatación térmica de una placa de acero de 1 m por 1 m al calentarla 100 °C. Cada lado crece 1.2 mm. El área crece 2.4·10⁻³ m² con la aproximación lineal y 2.40144·10⁻³ m² con el cálculo exacto, un error de 0.06 %.

**14. Derivación logarítmica** (confianza alta). La sensibilidad de la flecha de una viga rectangular, que es proporcional a 1/h³. Derivar el logaritmo muestra que un error de 2 % en el espesor h produce cerca de 6 % de error en la flecha, y el valor exacto es 5.77 %.

**15. Derivadas de orden superior** (confianza alta). La segunda derivada de la elástica de una viga da el momento flector, M = EI·y″. Con el ejemplo de la lección 8, en el empotramiento M = P·L = 2000 N·m.

## Módulo 3, Aplicaciones de la derivada

**16. Teorema del valor medio** (confianza alta). El control de velocidad por tramo. Quien recorre 3 km en 2 minutos tiene velocidad promedio de 90 km/h, y por el teorema, en algún instante iba exactamente a 90 km/h.

**17. Valores extremos** (confianza alta). El momento máximo en una viga simplemente apoyada con carga distribuida. Con w = 5 kN/m y L = 4 m, el máximo está en el centro y vale w·L²/8 = 10 kN·m.

**18. Monotonía y concavidad** (confianza media). La concavidad de la elástica de una viga depende del signo del momento flector, y el punto de inflexión está donde el momento vale 0. Falta elegir una viga con voladizo y sus cargas.

**19. Análisis de gráficas** (confianza baja). Una curva de eficiencia de una bomba o de torque de un motor. Ahí sí hay máximos y puntos de operación, pero necesito datos reales tuyos para no inventar una curva.

**20. Optimización** (confianza alta). Una lata de 1 litro con el mínimo material. El radio óptimo es 5.42 cm y la altura es 10.84 cm, o sea el doble del radio. El área es 553.6 cm².

**21. Regla de L'Hôpital** (confianza media). La eficiencia de una aleta de enfriamiento, tanh(m·L) sobre (m·L). Cuando m·L tiende a 0 da 0 sobre 0 y el límite es 1. Con m·L = 0.1 vale 0.9967. Requiere explicar qué es una aleta.

**22. Método de Newton** (confianza alta). El factor de fricción de una tubería con la ecuación de Colebrook, que no se puede despejar. Con Re = 10⁵ y rugosidad relativa 0.0005, partiendo de f = 0.03, Newton converge en 4 pasos a f = 0.02033.

**23. Teorema fundamental del cálculo** (confianza alta). El trabajo de un resorte. Con k = 2000 N/m, estirarlo 0.1 m cuesta la integral de k·x, o sea 10 J.

## Lo que necesito de ti
1. Dime cuáles de los de confianza alta te suenan bien y cuáles forzados.
2. Para las lecciones 2 y 19, que son de confianza baja, dame un caso real que hayas visto en tu carrera.
3. Para las de confianza media, dime si prefieres que las ajuste con otras cifras.
4. Si hay algún caso que consideres que sobra o está mal planteado, dímelo sin rodeos.
