# Matemáticas Especiales — Digitalización MathUNAL

Contenido de este ZIP: los 3 bloques del catálogo `fa8c40_21fc71f6963f4d39a7707a8e0a09da4c.pdf`
(43 páginas), ya digitalizados a LaTeX limpio y compilados a PDF.

## Archivos

| Archivo | Contenido |
|---|---|
| `p1_entrenamiento_2019.tex/pdf` | "P1 (Entrenamiento) 2019 ME" — 14 preguntas de repaso con soluciones |
| `p1_2013_2.tex/pdf` | "Primer parcial ME, Semestre 02 de 2013" — examen físico, 3 preguntas |
| `p1_2019_2_taller.tex/pdf` | "P1 2019-2 ME" — taller/quiz de Moodle, 12 preguntas |

## Notas importantes

- **Pregunta 4 del taller 2019-2** (masa para 880 Hz) quedó **sin respuesta indicada**:
  el material original traía un bug de exportación de Moodle (las 4 opciones aparecían
  marcadas como "correctas" simultáneamente). Pendiente resolver si se desea indicar
  la respuesta real.
- **Pregunta 12 del taller 2019-2**, opciones (c) y (d): el original omite el factor
  `cos(·)` en la fórmula — se transcribió tal cual con nota `[sic]`, sin corregir en silencio.
- Ninguno de estos documentos contiene datos personales de estudiantes (nombre, carné,
  calificaciones a mano) — todos limpios según las reglas de contenido del proyecto.
- **Pendiente:** `Parcial 1 Matemáticas Especiales.pdf` (17 páginas originales) resultaron
  ser apuntes de teoría de un estudiante (no exámenes) — no se han digitalizado aún,
  a la espera de decisión sobre si entran en el alcance del proyecto.
- **Nota técnica:** estos `.tex` requieren el paquete `lmodern` para compilar con el peso
  de fuente correcto (sans, no delgado). Si el entorno no lo trae instalado, no hay red
  para `tlmgr`/`apt`; hay que instalarlo manualmente desde un paquete `lm.zip` (TDS) con
  `texhash` + `updmap-sys`.
- Nada de esto se ha subido a Supabase todavía — pendiente confirmar convención de
  carpeta/nombre.
