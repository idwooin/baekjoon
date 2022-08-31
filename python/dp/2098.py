import sys
import math

n = int(sys.stdin.readline())
edges = []
dp = [[math.inf]*(1<<n) for _ in range(n)]
for i in range(n):
    cost = list(map(int,sys.stdin.readline().strip().split()))
    edges.append(cost)

ans = math.inf

def dfs(curr,visited):
    if visited == (1<<n)-1:
        if edges[curr][0]:
            return edges[curr][0]
        else:
            return math.inf

    if dp[curr][visited]!=math.inf:
        return dp[curr][visited]

    for i in range(1,n):
        e = edges[curr][i]
        if e == 0: continue
        temp = 1<<i
        if visited&temp:
            continue
        a = dfs(i,visited|temp)+e
        dp[curr][visited] = min(dp[curr][visited],a)
    
    return dp[curr][visited]

print(dfs(0,1))

