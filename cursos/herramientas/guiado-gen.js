const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/';
const name=process.argv[2];const J=JSON.parse(fs.readFileSync(S+'plantilla/'+name+'.json','utf8'));
const blocks=[];J.leer.secciones.forEach(s=>s.bloques.forEach(b=>blocks.push(b)));
const B=t=>blocks.find(b=>b.t===t);
(async()=>{const b=await chromium.launch({args:['--no-sandbox']});const out={};
for(const [vn,vp] of [['d',{width:1280,height:900}],['m',{width:390,height:844}]]){
const c=await b.newContext({viewport:vp,deviceScaleFactor:1});
await c.route('**/cdnjs.cloudflare.com/**',r=>r.fulfill({path:S+'kx/katex.min.js',contentType:'text/javascript'}));
const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+S+'leccion-'+name.replace('calcint-','calcint-')+'.test.html');await p.waitForTimeout(800);
await p.click('#mt-leer');await p.waitForTimeout(500);p.setDefaultTimeout(8000);
const R={};
const ck=async(sel)=>{await p.locator(sel).first().evaluate(e=>e.scrollIntoView({block:'center'}));await p.waitForTimeout(60);await p.locator(sel).first().click({force:true});};
const t=async(sel)=>await p.$eval(sel,e=>e.textContent.replace(/\s+/g,' ').trim());
await p.evaluate(()=>document.querySelectorAll('.l-sec').forEach(s=>s.classList.add('in')));
let card;
const comp=B('completar');
if(comp){card='#m-leer .card.act:has([data-eq])';const w=comp.opciones.findIndex((_,i)=>i!==comp.correcta);
 await ck(card+` .chip-btn >> nth=${w}`);R.comp_mal=(await t(card+' .fb')).slice(0,40);
 await ck(card+` .chip-btn >> nth=${comp.correcta}`);R.comp_ok=(await t(card+' .fb')).slice(0,30);}
const er=B('error');
if(er){card='#m-leer .card.act:has(.stepbtn):not(:has(.pool))';const ok=er.pasos.findIndex((_,i)=>i!==er.mal);
 await ck(card+` .stepbtn >> nth=${ok}`);R.err_bien=(await t(card+' .fb')).slice(0,30);
 await ck(card+` .stepbtn >> nth=${er.mal}`);R.err_ok=(await t(card+' .fb')).slice(0,30);R.err_corr=await p.$eval(card+' .corr',e=>!e.hidden);}
const od=B('ordenar');
if(od){card='#m-leer .card.act:has(.pool)';const n=od.pasos.length;
 await ck(card+` .pool .stepbtn[data-k="${n-1}"]`);R.ord_mal=(await t(card+' .fb')).slice(0,30);
 for(let k=0;k<n;k++)await ck(card+` .pool .stepbtn[data-k="${k}"]`);
 R.ord_ok=(await t(card+' .fb')).slice(0,30);R.ord_n=await p.$$eval(card+' .put li',e=>e.length);
 R.ord_aria=await p.$$eval(card+' .pool .stepbtn',e=>e.every(x=>x.getAttribute('aria-label')&&x.getAttribute('aria-label')!=='Paso desordenado'));}
const Q=J.pregunta;
card='#m-leer .card.quiz[data-quiz]';
await ck(card+' [data-hint]');R.pistas1=await p.$$eval(card+' .hints li',e=>e.length);
const wr=Q.opciones.map((_,i)=>i).filter(i=>i!==Q.correcta);
await ck(card+` .opts button >> nth=${wr[0]}`);R.q_err1=(await t(card+' .fb')).slice(0,50);
await ck(card+` .opts button >> nth=${wr[1]}`);R.giveup=await p.$eval(card+' .giveup',e=>!e.hidden);
await ck(card+` .opts button >> nth=${Q.correcta}`);R.q_ok=(await t(card+' .fb')).slice(0,30);
const sm=B('simulacro');
if(sm){card='#m-leer .card.sim';R.sim=[];
 for(const q of sm.preguntas){
  if(q.tipo==='numerica'){await p.fill(card+' input',q.respuesta);await ck(card+' [data-chk]');}
  else await ck(card+` .opts button >> nth=${q.correcta}`);
  R.sim.push((await t(card+' .fb')).slice(0,12));
  await ck(card+' .sim-n button');await p.waitForTimeout(250);}
 R.sim_fin=(await t(card)).slice(0,40);}
R.desborde=await p.evaluate(()=>document.documentElement.scrollWidth>document.documentElement.clientWidth+1);
R.errs=errs;out[vn]=R;await c.close();}
console.log(JSON.stringify(out));await b.close();})();
