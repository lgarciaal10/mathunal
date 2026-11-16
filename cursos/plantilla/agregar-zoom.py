#!/usr/bin/env python3
"""Agrega zoom a una lección que tenga el capítulo final en 15.8 s.
Uso  python3 agregar-zoom.py leccion.json FACTOR
FACTOR es cuántas veces se acerca la gráfica. Para un hueco conviene ancho final de unos 0.004
y para una secante de unos 0.08, o sea FACTOR = ancho del eje x dividido entre ese valor.
Hace tres cosas. En Ver mete un capítulo de 4 segundos con el zoom, en Leer agrega una frase
y en Practicar agrega el paso Mira de cerca antes de Revisa tu respuesta."""
import json, sys
p, factor = sys.argv[1], float(sys.argv[2])
L = json.load(open(p)); G = L['grafica']; V = L['ver']; SEC = G.get('tipo') == 'secante'
if G.get('zoom'): sys.exit('La lección ya tiene zoom')
T0, DT = 15.8, 4.0
G['zoom'] = {'factor': int(factor) if factor == int(factor) else factor}
txt_ver = ('De cerca, la curva casi se ve como una recta, y esa recta es la tangente.' if SEC
           else 'Con mucho zoom se ve que los dos puntos casi tocan el hueco.')
caps = V['capitulos']; i = next(k for k, c in enumerate(caps) if abs(c[0] - T0) < 1e-9)
for c in caps[i:]: c[0] += DT; c[1] += DT
caps.insert(i, [T0, T0 + DT, txt_ver]); V['duracion'] += DT
for name, kf in V['canales'].items():
    for k in kf:
        if k[0] >= T0: k[0] += DT
V['canales']['zoom'] = [[T0, 0], [T0 + 2.5, 1], [T0 + 3.2, 1], [T0 + DT, 0]]
for k, iv in (V.get('intervalos') or {}).items():
    if iv[0] >= T0: iv[0] += DT; iv[1] += DT
# Leer
sec_text = ' Al terminar, la gráfica hace zoom para que veas el detalle.'
for s in L['leer']['secciones']:
    b = s['bloques']
    for j, x in enumerate(b):
        if x['t'] == 'acercando' and j + 1 < len(b) and b[j + 1]['t'] == 'p' and 'zoom' not in b[j + 1]['html']:
            b[j + 1]['html'] += sec_text
# Practicar
pas = L['practicar']['pasos']; ult = pas[-1]
assert ult['bloques'][0]['t'] == 'pregunta', 'el último paso debería ser la pregunta'
if SEC:
    paso = {'titulo': 'Mira de cerca', 'grafica': {'draw': 1, 'hole': 1, 'guide': 1, 'zoom': 1}, 'laboratorio': True, 'd': 0.01,
            'bloques': [{'t': 'p', 'html': 'Ahora la gráfica está con zoom. De cerca, la curva casi se ve como una recta y la secante se pega a la tangente. Mueve h para comprobarlo.'}]}
else:
    paso = {'titulo': 'Mira de cerca', 'grafica': {'draw': 1, 'hole': 1, 'guide': 1, 'zoom': 1}, 'laboratorio': True, 'd': 0.001,
            'bloques': [{'t': 'p', 'html': 'Ahora la gráfica está con mucho zoom. Los dos puntos casi tocan el hueco. Mueve el deslizador para alejarlos.'}]}
pas.insert(len(pas) - 1, paso)
json.dump(L, open(p, 'w'), ensure_ascii=False, indent=1)
print('Zoom agregado a', p, 'factor', G['zoom']['factor'], 'duración', V['duracion'])
