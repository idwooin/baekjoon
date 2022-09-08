import heapq

n,m = map(int,input().split())
pq = []
parent = [i for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(pq,(c,a,b))

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
while cnt < n-2:
    c,a,b = heapq.heappop(pq)
    if head(a)!=head(b):
        answer+=c
        cnt+=1
        union(a,b)

print(answer)
