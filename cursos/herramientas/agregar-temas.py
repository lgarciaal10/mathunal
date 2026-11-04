#!/usr/bin/env python3
"""Agrupa por tema las preguntas que saca extraer-banco.js (bank.json) y escribe mapa-temas.json.
Uso  python3 agregar-temas.py carpeta/con/bank.json"""
import json, collections, re, sys, os
B = sys.argv[1] if len(sys.argv) > 1 else '.'
d = json.load(open(os.path.join(B, 'bank.json'), encoding='utf8'))
MAT = {'calcdif': ('Cálculo Diferencial', 'Diferencial'), 'calcint': ('Cálculo Integral', 'Integral'), 'calcvec': ('Cálculo en Varias Variables', 'Varias variables'),
       'alglin': ('Álgebra Lineal', 'Álgebra lineal'), 'edo': ('Ecuaciones Diferenciales', 'Ecuaciones diferenciales'), 'geovec': ('Geometría Vectorial y Analítica', 'Geometría vectorial'),
       'matbas': ('Matemáticas Básicas', 'Básicas'), 'discretas': ('Matemáticas Discretas', 'Discretas'), 'metnum': ('Métodos Numéricos', 'Métodos numéricos'),
       'fundamentos': ('Fundamentos de Matemáticas', 'Fundamentos'), 'especiales': ('Matemáticas Especiales', 'Especiales')}
SIGLAS = {'edo', 'edp', 'ecuaciones'}
def bonito(txt):
    t = txt.strip().lower()
    t = re.sub(r'\b(edo|edp)\b', lambda m: m.group(1).upper(), t)
    t = re.sub(r'\b(fourier|laplace)\b', lambda m: m.group(1).capitalize(), t)
    return t[:1].upper() + t[1:]
out = {'fuente': 'index.html subido por Luis (banco EXAMS y SIM_NEW)', 'aviso': 'Sale del banco de MathUNAL y no del programa oficial de la materia', 'materias': {}}
for m, (nombre, corto) in MAT.items():
    ex = {}
    for r in d['rows']:
        if r['exam'].startswith(m + '_'):
            e = ex.setdefault(r['exam'], {'semestre': r['semestre'], 'n': 0}); e['n'] += 1
    tipo = lambda k: 'corte' if re.search(r'_c\d$', k) else 'parcial'
    parc = [k for k in ex if tipo(k) == 'parcial']
    temas = collections.OrderedDict()
    def t(n): return temas.setdefault(n, {'tema': n, 'parciales_n': 0, 'parciales_examenes': set(), 'simulacros_n': 0, 'cortes': collections.Counter(), 'freq': collections.Counter(), 'error': collections.Counter(), '_h': set()})
    for r in d['rows']:
        if not r['exam'].startswith(m + '_'): continue
        x = t(r['tema'])
        if tipo(r['exam']) == 'parcial': x['parciales_n'] += 1; x['parciales_examenes'].add(r['exam'])
        else:
            if r['h'] in x['_h']: continue
            x['_h'].add(r['h']); x['simulacros_n'] += 1
        c = r['corte']
        if c is None and re.search(r'_c(\d)$', r['exam']): c = int(re.search(r'_c(\d)$', r['exam']).group(1))
        if c is not None: x['cortes'][c] += 1
        x['freq'][r['freq']] += 1; x['error'][r['tipoError']] += 1
    for r in d['sim']:
        if r['materia'] != m: continue
        x = t(r['tema'])
        if r['h'] in x['_h']: continue
        x['_h'].add(r['h']); x['simulacros_n'] += 1
        if r['corte'] is not None: x['cortes'][r['corte']] += 1
        x['freq'][r['freq']] += 1; x['error'][r['tipoError']] += 1
    lst = []
    for v in temas.values():
        corte = v['cortes'].most_common(1)[0][0] if v['cortes'] else None
        lst.append({'tema': v['tema'], 'corte': corte, 'cortes': dict(sorted(v['cortes'].items())), 'parciales_n': v['parciales_n'], 'parciales_con_el_tema': len(v['parciales_examenes']), 'simulacros_n': v['simulacros_n'], 'total': v['parciales_n'] + v['simulacros_n'], 'freq': dict(v['freq']), 'error': dict(v['error'])})
    lst.sort(key=lambda a: (a['corte'] or 9, -a['total'], a['tema']))
    cortes_info = {}
    for k in ex:
        mm = re.search(r'^(.*) · CORTE (\d) \((\d+)%\)$', ex[k]['semestre'])
        if mm and re.search(r'_c\d$', k): cortes_info[int(mm.group(2))] = {'nombre': bonito(mm.group(1)), 'peso': int(mm.group(3))}
    out['materias'][m] = {'nombre': nombre, 'corto': corto, 'cortes_info': cortes_info, 'examenes_parcial': [{'clave': k, 'semestre': ex[k]['semestre'], 'preguntas': ex[k]['n']} for k in parc], 'examenes_corte': [{'clave': k, 'semestre': ex[k]['semestre'], 'preguntas': ex[k]['n']} for k in ex if tipo(k) == 'corte'], 'n_parciales': len(parc), 'temas': lst}
json.dump(out, open(os.path.join(B, 'mapa-temas.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('listo')
