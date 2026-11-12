const {chromium}=require('/opt/node-tools/node_modules/playwright');const S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/';
(async()=>{const b=await chromium.launch({args:['--no-sandbox']});const c=await b.newContext({viewport:{width:1280,height:900}});
await c.route('**/cdnjs.cloudflare.com/**',r=>r.fulfill({path:S+'kx/katex.min.js',contentType:'text/javascript'}));
for(const n of process.argv.slice(2)){const p=await c.newPage();await p.goto('file://'+S+'leccion-'+n+'.test.html');await p.waitForTimeout(800);
await p.click('#v-script li:last-child button');await p.waitForTimeout(400);
await p.locator('#v-g').screenshot({path:S+'g-'+n+'.png'});await p.close();}
await b.close()})();
