import sys
import heapq
v,e = list(map(int,sys.stdin.readline().strip().split()))
queue = [[0,1]]
visited = [False for _ in range(v+1)]
edges = [[] for _ in range(v+1)]

for i in range(e):
    a,b,c = list(map(int,sys.stdin.readline().strip().split()))
    edges[a].append([b,c])
    edges[b].append([a,c])

cnt = 0
ans = 0
while queue and cnt!=v:
    weight,node = heapq.heappop(queue)
    if visited[node] == False:
        visited[node] = True
        cnt+=1
        ans+=weight
        for e in edges[node]:
            next_node,weight = e
            heapq.heappush(queue,[weight,next_node])
print(ans)
