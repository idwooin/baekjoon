import heapq
from math import sqrt

n = int(input())
pq = []
loc = []
parent = [i for i in range(n)]
for i in range(n):
    x,y = map(float,input().split())
    loc.append((x,y))

def dist(a,b,c,d):
    return sqrt((c-a)**2+(d-b)**2)

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        
        heapq.heappush(pq,(dist(*loc[i],*loc[j]),i,j))


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

print(round(answer,2))