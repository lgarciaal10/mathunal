#!/bin/bash
# uso probar.sh nombre   (nombre sin prefijo, por ejemplo tfc para calcint-tfc)
S=/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad
N=calcint-$1
cd $S/ci && python3 mk-$1.py && cp $N.json $S/plantilla/ && cd $S/plantilla || exit 1
VAL=$(node validar.js $N.json --katex ../kx/katex.min.js 2>&1); echo "$VAL" | tail -4
if echo "$VAL" | grep -q "Falló"; then echo STOP_VALIDACION; exit 1; fi
python3 construir.py $N.json $S/leccion-$N.html --katex-inline $S/kx/katex-inline.css >/dev/null
python3 construir.py $N.json $S/leccion-$N.test.html --katex-inline $S/kx/katex-inline.css --doctype >/dev/null
cd $S
timeout 250 node smoke-leccion.js leccion-$N 2>&1 | cut -c1-330
node axe-run.js leccion-$N | tail -2
timeout 250 node guiado-gen.js $N 2>&1 | cut -c1-1400
