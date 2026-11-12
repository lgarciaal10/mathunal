const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/';
const axeSrc=fs.readFileSync(S+'pw/node_modules/axe-core/axe.min.js','utf8');
(async()=>{const b=await chromium.launch({args:['--no-sandbox']});
for(const [vn,vp] of [['d',{width:1280,height:900}],['m',{width:390,height:844}]]){
const c=await b.newContext({viewport:vp});
await c.route('**/cdnjs.cloudflare.com/**',r=>r.fulfill({path:S+'kx/katex.min.js',contentType:'text/javascript'}));
await c.route('**/fonts.g*/**',r=>r.abort());
const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(8000);
const R={};
// 1. un error en una lección, luego Estudio
const lp=await c.newPage();await lp.goto('file://'+S+'leccion-calcint-sustitucion.test.html');await lp.waitForTimeout(600);await lp.click('#mt-leer');await lp.waitForTimeout(300);
await lp.evaluate(()=>document.querySelectorAll('.l-sec').forEach(s=>s.classList.add('in')));
await lp.locator('#m-leer .card.quiz[data-quiz] .opts button').nth(1).evaluate(e=>e.scrollIntoView({block:'center'}));
await lp.locator('#m-leer .card.quiz[data-quiz] .opts button').nth(1).click();await lp.waitForTimeout(200);await lp.close();
await p.goto('file://'+S+'estudio/estudio.test.html#cuaderno');await p.waitForTimeout(700);
R.cuaderno_desde_leccion=await p.$$eval('#cu-l article',e=>e.length);
R.cuaderno_texto=(await p.$eval('#cu-l article',e=>e.textContent.replace(/\s+/g,' ').slice(0,160))).trim();
R.katex_cuaderno=await p.$$eval('#cu-l .katex',e=>e.length);
// practicar de nuevo, acertar
await p.click('#cu-l article [data-pr]');await p.waitForTimeout(300);
const D=await p.evaluate(()=>window.D);
const q0=D.lecciones.find(l=>l.id==='calcint-m1-l2').q[0];
await p.click('#cu-l article .opts button >> nth='+q0.c);await p.waitForTimeout(200);await p.click('#cu-l article [data-next]');await p.waitForTimeout(300);
R.cuaderno_pend_despues=await p.$$eval('#cu-l article',e=>e.length);
await p.click('[data-e="res"]');await p.waitForTimeout(200);R.cuaderno_res=await p.$$eval('#cu-l article.res',e=>e.length);
// 2. diagnóstico
await p.goto('file://'+S+'estudio/estudio.test.html#diagnostico');await p.waitForTimeout(500);
await p.click('#dg-c button >> nth=1');await p.waitForTimeout(300);
let n=0;
for(let i=0;i<14;i++){ const has=await p.$('#dg-q .q'); if(!has) break; n++;
  const id=await p.evaluate(()=>0);
  const isNum=await p.$('#dg-q input');
  const txt=await p.$eval('#dg-q .chip:nth-child(2)',e=>e.textContent);
  const lec=D.lecciones.find(l=>l.titulo===txt&&l.curso==='Cálculo Integral');
  const qh=await p.$eval('#dg-q .q',e=>e.textContent);
  const cand=lec.q.find(q=>qh.length>0&&true);
  if(isNum){ await p.fill('#dg-q input','0'); await p.click('#dg-q [data-chk]'); }
  else { const mc=lec.q.filter(q=>q.t==='mcq'); await p.click('#dg-q .conf button[data-c="2"]'); await p.click('#dg-q .opts button >> nth='+(i%2?0:1)); }
  await p.waitForTimeout(150); await p.click('#dg-q [data-next]'); await p.waitForTimeout(200); }
R.diag_preguntas=n; R.diag_resultado=(await p.$eval('#dg-b h2',e=>e.textContent));
R.diag_filas=await p.$$eval('#dg-b tbody tr',e=>e.length);
R.diag_guardado=await p.evaluate(()=>Object.keys(JSON.parse(localStorage.getItem('mu-diag')||'{}')));
// 3. repaso mezclado
await p.goto('file://'+S+'estudio/estudio.test.html#repaso');await p.waitForTimeout(400);
await p.selectOption('#rp-n','8');await p.click('#rp-go');await p.waitForTimeout(300);
const lids=[];
for(let i=0;i<8;i++){ const has=await p.$('#rp-q .q'); if(!has) break; lids.push(await p.$eval('#rp-q .chip:nth-child(2)',e=>e.textContent));
  const isNum=await p.$('#rp-q input'); if(isNum){ await p.fill('#rp-q input','1'); await p.click('#rp-q [data-chk]'); } else await p.click('#rp-q .opts button >> nth=0');
  await p.waitForTimeout(120); await p.click('#rp-q [data-next]'); await p.waitForTimeout(150); }
R.repaso_n=lids.length; R.repaso_consecutivas=lids.filter((x,i)=>i&&x===lids[i-1]).length; R.repaso_distintas=new Set(lids).size;
R.repaso_fin=(await p.$eval('#rp-b h2',e=>e.textContent));
R.conf_guardada=await p.evaluate(()=>localStorage.getItem('mu-confianza'));
// 4. mapa
await p.goto('file://'+S+'estudio/estudio.test.html#mapa');await p.waitForTimeout(500);
R.mapa_nodos=await p.$$eval('.nodo',e=>e.length);R.mapa_aristas=await p.$$eval('.arista',e=>e.length);
await p.click('#mp-c button >> nth=2');await p.waitForTimeout(200);R.mapa_alglin=await p.$$eval('.nodo',e=>e.length);
await p.click('.nodo >> nth=3');await p.waitForTimeout(200);R.mapa_panel=(await p.$eval('#mp-p h3',e=>e.textContent));
R.mapa_estados=await p.$$eval('.nodo',e=>e.map(x=>x.getAttribute('aria-label').split(', ').pop()).filter((v,i,a)=>a.indexOf(v)===i));
// 5. inicio
await p.goto('file://'+S+'estudio/estudio.test.html#inicio');await p.waitForTimeout(400);R.inicio_tarjetas=await p.$$eval('.grid .card',e=>e.length);
R.desborde=await p.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
// axe en cada vista
R.axe={};
for(const h of ['inicio','diagnostico','repaso','cuaderno','mapa']){ await p.goto('file://'+S+'estudio/estudio.test.html#'+h);await p.waitForTimeout(500); await p.evaluate(axeSrc); R.axe[h]=await p.evaluate(async()=>{const r=await axe.run({runOnly:['wcag2a','wcag2aa']});return r.violations.map(v=>v.id+':'+v.nodes.length);}); }
await p.goto('file://'+S+'estudio/estudio.test.html#mapa');await p.waitForTimeout(500);await p.screenshot({path:S+'estudio/shot-mapa-'+vn+'.png'});
await p.goto('file://'+S+'estudio/estudio.test.html#cuaderno');await p.waitForTimeout(500);await p.screenshot({path:S+'estudio/shot-cuaderno-'+vn+'.png'});
console.log(vn,JSON.stringify(R),'ERRS',JSON.stringify(errs));await c.close();}
await b.close()})();
