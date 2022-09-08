from collections import deque

n = int(input())
m = int(input())
adj = [[0]*(n+1) for _ in range(n+1)]
for i in  range(m):
    v1,v2 = map(int,input().split())
    adj[v1][v2]=1
    adj[v2][v1]=1

queue = deque([1])
visited = [0]*(n+1)
answer = -1

while queue:
    virus = queue.popleft()
    if visited[virus]:
        continue
    visited[virus] = 1
    answer+=1

    for j,nextv in enumerate(adj[virus]):
        if nextv == 1 and visited[j]==0:
            queue.append(j)

print(answer)

