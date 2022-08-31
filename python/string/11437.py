from collections import deque

n = int(input())
parent = [_ for _ in range(n+1)]
rank = [0 for _ in range(n+1)]
rank[1] = 1
dic = {}

for i in range(n+1):
    dic[i] = []

def lca(a,b):
    if rank[a] > rank[b]:
        while rank[a]!=rank[b]:
            a = parent[a]
    
    elif rank[b] > rank[a]:
        while rank[b]!=rank[a]:
            b = parent[b]
    
    while a!=b:
        a = parent[a]
        b = parent[b]
    
    return a

def bfs(start):
    q = deque([start])

    while q:
        node = q.popleft()
        for childs in dic[node]:
            if rank[childs]:
                continue
            parent[childs] = node
            rank[childs] = rank[node]+1
            q.append(childs)

for i in range(n-1):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

bfs(1)

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))