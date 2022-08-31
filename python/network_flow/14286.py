import sys
from collections import deque

n,m = map(int,sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]
edge = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    edge[a][b] = c
    edge[b][a] = c

s,t = map(int,sys.stdin.readline().strip().split())

def bfs(s,t,graph,edge):
    global n

    prev = [-1 for _ in range(n+1)]
    q = deque([])
    q.append(s)

    while q and prev[t] == -1:
        node = q.popleft()

        for next in graph[node]:
            if edge[node][next] > 0:
                if prev[next] != -1: continue
                prev[next] = node
                q.append(next)
                if next==t: break
    
    return prev

def edmond_karf(s,t,graph,edge):
    total_flow = 0

    while True:
        prev = bfs(s,t,graph,edge)

        if prev[t] == -1: break
        
        node = t
        min_flow = 10**10

        while node != s:
            curr_flow = edge[prev[node]][node]
            min_flow = min(min_flow,curr_flow)
            node = prev[node]
        
        node = t
        while node != s:
            edge[prev[node]][node] -=min_flow
            edge[node][prev[node]] +=min_flow 
            node = prev[node]

        total_flow+=min_flow

    return total_flow

ans = edmond_karf(s,t,graph,edge)
print(ans)