// uso node exportar.js N > salida.json   (N semillas por plantilla)
const P = require('./gen.js');
const N = parseInt(process.argv[2] || '200', 10);
const out = [];
P.plantillas.forEach((t, i) => { for (let s = 1; s <= N; s++) out.push(P.crear(i, s)); });
process.stdout.write(JSON.stringify(out));
