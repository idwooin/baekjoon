import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
edges = dict()
ratio = []
answer = [1 for _ in range(n)]

def gcd(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

def dfs(node,prop,visited):
    global edges,answer

    queue = deque([])
    for e in edges[node]:
        queue.append(e)
    
    while queue:
        e = queue.popleft()
        if visited&(1<<e):
            continue
        visited|=(1<<e)
        answer[e]*=prop

        for f in edges[e]:
            queue.append(f)

    return


for i in range(n-1):
    a,b,p,q = map(int,input().split())
    ratio.append((a,b,p,q))

    if a in edges:
        edges[a].append(b)
    else:
        edges[a] = [b]
    
    if b in edges:
        edges[b].append(a)
    else:
        edges[b] = [a]

for i in range(n-1):
    a,b,p,q = ratio[i]

    answer[a] *= p
    answer[b] *= q
    visited = (1<<a)|(1<<b)
    dfs(a,p,visited)
    dfs(b,q,visited)

g=answer[0]
for i in range(n):
    g=gcd(g, answer[i])
for i in range(n): answer[i]//=g
print(*answer,sep=' ')