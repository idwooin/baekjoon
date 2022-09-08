import heapq

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

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
    return

queue = []
for i in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(queue,(c,a,b))

answer = 0
cnt = 0
while True:
    c,a,b = heapq.heappop(queue)
    if head(a)!=head(b):
        union(a,b)
        answer+=c
        cnt+=1
    
    if cnt == n-1:
        break

print(answer)