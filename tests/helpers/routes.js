// Descubre las rutas del router leyendo index.html (no se mantiene una lista a mano):
//  - KNOWN: páginas del router (la de materia necesita ?s=<código>)
//  - SUBJECTS: códigos de materia (code:'1000003', …)
const fs = require('fs');
const path = require('path');

function load(root) {
  const html = fs.readFileSync(path.join(root || path.join(__dirname, '..', '..'), 'index.html'), 'utf8');
  const known = (html.match(/var KNOWN\s*=\s*\[([^\]]*)\]/) || [, ''])[1].match(/'([^']+)'/g).map(s => s.slice(1, -1));
  const codes = [...new Set([...html.matchAll(/\{code:'(\d{7})'/g)].map(m => m[1]))];
  const routes = [];
  for (const k of known) {
    if (k === 'materia') codes.forEach(c => routes.push({ name: `materia-${c}`, hash: `materia?s=${c}`, page: 'materia' }));
    else routes.push({ name: k, hash: k, page: k });
  }
  return { known, codes, routes };
}

module.exports = { load, LANGS: ['es', 'en'], THEMES: ['dark', 'black', 'gray', 'light'], WIDTHS: [360, 768, 1280] };
