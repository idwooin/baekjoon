import sys
from collections import deque

n = int(sys.stdin.readline())
edges = [[] for _ in range(n+1)]
d = [0 for _ in range(n+1)]
weight = [0 for _ in range(n+1)]
times = [0 for _ in range(n+1)]
queue = deque([])

for i in range(1,n+1):
    task = list(map(int,sys.stdin.readline().strip().split()))
    weight[i]=task[0];d[i] = task[1]
    if d[i] == 0:
        queue.append(i)
    else:
        for j in range(task[1]):
            edges[task[j+2]].append(i)

while queue:
    node = queue.popleft()
    times[node] += weight[node]

    for e in edges[node]:
        d[e]-=1
        times[e]=max(times[e],times[node])
        if d[e] == 0:
            queue.append(e)

print(max(times))