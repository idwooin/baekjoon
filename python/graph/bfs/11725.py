import sys
from collections import deque

n = int(sys.stdin.readline())
parent = [i for i in range(n+1)]
edge= {}

def bfs(start):
    queue =deque([start])
    while queue:
        node = queue.popleft()
        for child in edge[node]:
            if parent[child] != child:
                continue
            parent[child]= node
            queue.append(child)

for i in range(n-1):
    a,b = map(int,sys.stdin.readline().strip().split())
    if edge.get(a) == None:
        edge[a] = [b]
    else:
        edge[a].append(b)
    if edge.get(b) == None:
        edge[b] = [a]
    else:
        edge[b].append(a)

bfs(1)

for i in range(2,n+1):
    print(parent[i])