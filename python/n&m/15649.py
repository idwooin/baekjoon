import sys
import heapq

q = []
n,m = map(int,sys.stdin.readline().strip().split())

for i in range(1,n+1):
    v = 1<<i
    heapq.heappush(q,[str(i),v])

while q:
    num,v=heapq.heappop(q)
    if len(num) == m:
        print(*num, sep=' ')
        continue

    for i in range(1,n+1):
        temp = 1<<i
        b = (v&temp)>>i
        if b:
            continue
        v = v|temp
        heapq.heappush(q,[num+str(i),v])
        v = v^temp
