import sys
import heapq

n = int(sys.stdin.readline())
lowl = []
highl = []
lmid = -10001
rmid = 10001
flagodd = True if n%2==1 else False

for i in range(n//2):
    numl = int(sys.stdin.readline())

    if rmid<numl:
        heapq.heappush(highl,numl)
        temp = heapq.heappop(highl)
        heapq.heappush(lowl,-temp)
        rmid = highl[0]
        lmid = -lowl[0]
    else:
        heapq.heappush(lowl,-numl)
        lmid = -lowl[0]
    
    print(lmid)
    
    numr = int(sys.stdin.readline())

    if lmid>numr:
        heapq.heappush(lowl,-numr)
        temp = heapq.heappop(lowl)
        heapq.heappush(highl,-temp)
        lmid = -lowl[0]
        rmid = highl[0]
    else:
        heapq.heappush(highl,numr)
        rmid = highl[0]

    print(lmid)

if flagodd:
    numl = int(sys.stdin.readline())

    if rmid<numl:
        heapq.heappush(highl,numl)
        temp = heapq.heappop(highl)
        heapq.heappush(lowl,-temp)
        rmid = highl[0]
        lmid = -lowl[0]
    else:
        heapq.heappush(lowl,-numl)
        lmid = -lowl[0]
    
    print(lmid)
   