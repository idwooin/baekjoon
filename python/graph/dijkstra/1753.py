import heapq
import math

v,e = list(map(int,input().split()))
k = int(input())

edges=[[] for i in range(v)]
for i in range(e):
    a,b,c = list(map(int,input().split()))
    edges[a-1].append((b-1,c))

min_dist = [math.inf for i in range(v)]
min_dist[k-1] = 0

def dijkstra_with_heap(k):
    q=[]
    heapq.heappush(q,(0,k-1))

    while q:
        dist,node = heapq.heappop(q)
        for to,d in edges[node]:
            curr = dist+d
            if curr < min_dist[to]:
                heapq.heappush(q,(curr,to))
                min_dist[to] = curr

dijkstra_with_heap(k)

for i in range(v):
    if min_dist[i] == math.inf:
        print("INF")
    else:
        print(min_dist[i])
