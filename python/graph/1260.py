from collections import deque
import heapq

n,m,v = map(int,input().split())

dfslist= [v]
bfslist= [v]

def dfs(start,visited):
    al = []
    stack = deque([start])
    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = 1
        al.append(node)
        temp=[]

        if node not in dict:
            continue

        for e in dict[node]:
            if visited[e]:
                continue
            else:
                heapq.heappush(temp,-e)

        while temp:
            stack.append(-heapq.heappop(temp))

    print(*al,sep=' ')
    return

def bfs(start,visited):
    al = []
    queue = deque([start])
    while queue:
        node = queue.popleft()

        if visited[node]:
            continue

        visited[node] = 1
        al.append(node)
        temp=[]

        if node not in dict:
            continue
        
        for e in dict[node]:
            if visited[e]:
                continue
            else:
                heapq.heappush(temp,e)

        while temp:
            queue.append(heapq.heappop(temp))
    
    print(*al,sep=' ')
    return

dict = {}
for i in range(m):
    v1,v2 = map(int,input().split())
    if v1 in dict:
        dict[v1].append(v2)
    else:
        dict[v1] = [v2]
    
    if v2 in dict:
        dict[v2].append(v1)
    else:
        dict[v2] = [v1]

dfs(v,[0 for i in range(n+1)])
bfs(v,[0 for i in range(n+1)])


