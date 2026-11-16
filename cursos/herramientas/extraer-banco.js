const {chromium}=require('playwright');const http=require('http'),fs=require('fs');
const S=(process.argv[2]||'.')+'/';
const srv=http.createServer((q,r)=>{r.writeHead(200,{'content-type':'text/html; charset=utf-8'});r.end(fs.readFileSync(S+'index.html'))}).listen(4590,async()=>{
 const b=await chromium.launch({args:['--no-sandbox','--host-resolver-rules=MAP mathunal.test 127.0.0.1']});
 const c=await b.newContext();await c.route(u=>!/mathunal\.test/.test(u.hostname),r=>r.abort());
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://mathunal.test:4590/#simulacro',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__muCurrentPage==='simulacro',{timeout:15000}).catch(()=>{});await p.waitForTimeout(2500);
 const data=await p.evaluate(()=>{const E=window.EXAMS||{};const out=[];Object.keys(E).forEach(k=>{const ex=E[k];(ex.preguntas||[]).forEach((q,i)=>out.push({exam:k,semestre:ex.semestre||'',titulo:ex.titulo||'',i:i,tema:q.tema||'',corte:q.corte==null?null:q.corte,freq:q.freq||'',tipoError:q.tipoError||'',tipo:q.tipo||'',id:q.id||null,h:(q.texto||'').replace(/\s+/g,' ').trim().slice(0,160)}))});
   const sim=[];try{Object.keys(SIM_NEW).forEach(m=>SIM_NEW[m].forEach(q=>sim.push({materia:m,id:q.id,tema:q.t||'',corte:q.c==null?null:q.c,freq:q.f||'',tipoError:q.e||'',tipo:q.tipo||'',h:(q.texto||'').replace(/\s+/g,' ').trim().slice(0,160)})))}catch(e){}return {n:out.length,exams:Object.keys(E).length,simnew:sim.length,rows:out,sim:sim}});
 fs.writeFileSync(S+'bank.json',JSON.stringify(data));console.log(data.n,'preguntas',data.exams,'exámenes','SIM_NEW',data.simnew,errs.slice(0,3));
 const pref={};data.rows.forEach(r=>{const m=r.exam.replace(/_.*$/,'');pref[m]=(pref[m]||0)+1});console.log(JSON.stringify(pref));
 await b.close();srv.close();});
