"""Volcado legible, desde los JSON, de todo lo que tiene una clave de respuesta.
Muestra cada opción, cuál está marcada como correcta, y el texto de error de cada distractor."""
import json, glob, os, sys, re
carp = sys.argv[1]; dest = sys.argv[2]; os.makedirs(dest, exist_ok=True)
GR = {'matbas':'matbas','calculo':'calculo','calcint':'calcint','alglin':'alglin','edo':'edo','fund':'fund','geovec':'geovec','disc':'disc','mn':'mn','esp':'esp','cv':'cv'}
def L(o): return json.dumps(o, ensure_ascii=False)
def bloques(d):
    r = []
    def w(o):
        if isinstance(o, dict):
            if isinstance(o.get('t'), str): r.append(o)
            for v in o.values(): w(v)
        elif isinstance(o, list):
            for v in o: w(v)
    w(d); return r
out = {k: [] for k in GR}
for p in sorted(glob.glob(os.path.join(carp, '*.json'))):
    stem = os.path.basename(p)[:-5]; d = json.load(open(p)); g = stem.split('-')[0]
    if g == 'calcint': key = 'calcint'
    else: key = g
    s = ['', '=' * 70, 'LECCION ' + stem + ' ' + d.get('titulo', ''), '=' * 70]
    for b in bloques(d):
        t = b['t']
        if t == 'piensa':
            s.append('PIENSA ' + b['pregunta']); s.append('  opciones (valores) ' + L(b['opciones']) + '   CLAVE ' + L(b['correcta']))
        elif t == 'completar':
            s.append('COMPLETAR ' + b['enunciado']); s.append('  ecuacion ' + b['tex'])
            for i, o in enumerate(b['opciones']):
                s.append('  %s opcion %d  %s   [%s]%s' % ('*' if i == b['correcta'] else ' ', i, o['tex'], o.get('txt', ''), '' if i == b['correcta'] else '   ERROR EXPLICADO ' + b['errores'][i]))
        elif t == 'error':
            s.append('ERROR ' + b['enunciado'])
            for i, q in enumerate(b['pasos']):
                s.append('  %s paso %d  %s' % ('*' if i == b['mal'] else ' ', i + 1, q['tex']))
            s.append('  MARCADO COMO ERRONEO el paso %d. explicacion %s. correccion %s' % (b['mal'] + 1, b['explicacion'], b['correccion']))
        elif t == 'ordenar':
            s.append('ORDENAR ' + b['enunciado'])
            for i, q in enumerate(b['pasos']): s.append('  orden correcto %d  %s' % (i + 1, q))
            s.append('  se muestran mezclados como ' + L([b['pasos'][k] for k in b['mezcla']]))
        elif t == 'simulacro':
            for q in b.get('preguntas', []):
                s.append('SIMULACRO ' + (q.get('texto') or q.get('tex') or ''))
                if q.get('tipo') == 'numerica': s.append('  respuesta numerica ' + L(q.get('respuesta')) + ' tolerancia ' + L(q.get('tolNum')) + '. resumen ' + q.get('resumen', ''))
                else:
                    for i, o in enumerate(q.get('opciones', [])): s.append('  %s opcion %d  %s' % ('*' if i == q.get('correcta') else ' ', i, o))
                    s.append('  resumen ' + q.get('resumen', ''))
        elif t == 'ingenieria':
            s.append('INGENIERIA ' + b.get('titulo', '') + ' | ' + b.get('html', b.get('texto', '')) + ' | ' + b.get('tex', '') + ' | datos ' + L(b.get('datos')) + ' | ' + b.get('cierre', b.get('porque', '')))
    q = d.get('pregunta')
    if q:
        s.append('PREGUNTA FINAL ' + q['tex'])
        for i, o in enumerate(q['opciones']): s.append('  %s opcion %d  %s' % ('*' if i == q['correcta'] else ' ', i, o))
        s.append('  explicacion ' + q['explicacion'] + ' | verificacion ' + L(q.get('verificacion')))
        for i, e in enumerate(q.get('errores', [])): s.append('  error explicado de la opcion %d  %s' % (i, e))
    out[key].append('\n'.join(s))
for k, v in out.items():
    open(os.path.join(dest, k + '.md'), 'w', encoding='utf-8').write('\n'.join(v) + '\n')
    print(k, len(v), sum(len(x) for x in v))
