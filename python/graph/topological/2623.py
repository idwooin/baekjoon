from collections import deque
n,m = map(int,input().split())
top = [0 for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
queue = deque([])

for i in range(m):
    l = list(map(int,input().split()))
    visited = [0 for _ in range(n+1)]
    real = []
    for j in range(len(l)-1,1,-1):
        top[l[j]]+=1
        edges[l[j-1]].append(l[j])

for i in range(1,n+1):
    if top[i] == 0:
        queue.append(i)

ans = []
while queue:
    node = queue.popleft()
    ans.append(node)
    for nodes in edges[node]:
        top[nodes]-=1
        if top[nodes] == 0:
            queue.append(nodes)

flag = True
for i in range(1,n+1):
    if top[i] > 0:
        flag = False
        break

if flag:
    for a in ans:
        print(a)
else:
    print(0)