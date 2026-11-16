#!/bin/bash
# uso sync.sh "tema" nombre1 nombre2 ...   (copia jsons y scripts al repo, marca estado y hace commit y push)
S=/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad
MSG="$1"; shift
cd /home/user/mathunal || exit 1
cp $S/plantilla/motor.js $S/plantilla/motor.css $S/plantilla/validar.js cursos/plantilla/
cp $S/ci/mklib.py $S/ci/mk-*.py cursos/herramientas/
for n in "$@"; do cp $S/plantilla/calcint-$n.json cursos/lecciones/; done
git add cursos && git commit -q -m "$MSG

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01KeDp96hq5xtS1sDmf7QC6t" && git push -q origin cursos-mockups && git log --oneline | head -1
