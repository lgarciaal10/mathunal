#!/bin/bash
cd /tmp/ref/v7
for id in basicas diferencial integral algebra edo fundamentos geometria discretas numericos especiales varias; do
  python3 gen7.py $id > /tmp/ref/v7/$id.log 2>&1 || { echo "FALLO gen $id"; continue; }
  (cd /tmp/ref/v7/$id/hf && npx -y hyperframes@0.9.40 render --quality looks -o /tmp/ref/reel-$id.mp4 > /tmp/ref/v7/$id.render.log 2>&1)
  ls -la /tmp/ref/reel-$id.mp4
done
echo TODOS
