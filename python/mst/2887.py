import heapq
from math import sqrt

n = int(input())
pq = []
loc = []
parent = [i for i in range(n)]
for i in range(n):
    x,y,z = map(int,input().split())
    loc.append((x,y,z,i))

def dist(a,b,c,d,e,f):
    return min(abs(d-a),abs(e-b),abs(f-c))

for i in range(3):
    loc.sort(key=lambda x:x[i])
    for j in range(1,n):        
        heapq.heappush(pq,(abs(loc[j][i]-loc[j-1][i]),loc[j-1][3],loc[j][3]))


def head(node):
    global parent
    if parent[node]!=node:
        parent[node] = head(parent[node])
    
    return parent[node]

def union(a,b):
    global parent
    ha = head(a)
    hb = head(b)
    parent[ha] = hb

answer = 0
cnt = 0
while cnt < n-1:
    c,a,b = heapq.heappop(pq)
    if head(a)!=head(b):
        answer+=c
        cnt+=1
        union(a,b)

print(answer)