import asyncio,ssl,json,subprocess,sys,edge_tts
import edge_tts.communicate as C
C._SSL_CTX=ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
VOICE=sys.argv[1] if len(sys.argv)>1 else 'es-CO-SalomeNeural'
RATE=sys.argv[2] if len(sys.argv)>2 else '-8%'
PITCH=sys.argv[3] if len(sys.argv)>3 else '-2Hz'
FR=open('frases.txt').read().strip().split('\n')
async def one(i,t):
    com=edge_tts.Communicate(t,VOICE,rate=RATE,pitch=PITCH,boundary='WordBoundary')
    b=bytearray(); ws=[]
    async for ch in com.stream():
        if ch['type']=='audio': b+=ch['data']
        elif ch['type']=='WordBoundary': ws.append((ch['text'],ch['offset']/1e7,(ch['offset']+ch['duration'])/1e7))
    open(f's{i}.mp3','wb').write(b); return ws
async def main():
    return [await one(i,t) for i,t in enumerate(FR)]
res=asyncio.run(main())
json.dump(res,open('tts-raw.json','w'))
print([len(r) for r in res],[len(f.split()) for f in FR])
