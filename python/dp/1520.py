import sys

m,n = list(map(int,sys.stdin.readline().strip().split()))
maps = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(m)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
dp = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(i,j):
    if i==m-1 and j==n-1:
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    dp[i][j] = 0

    for k in range(4):
        newi = i+di[k]
        newj = j+dj[k]
        if not(0<=newi<m and 0<=newj<n):
            continue
        if maps[i][j] > maps[newi][newj]:
            dp[i][j]+= dfs(newi,newj)
    
    return dp[i][j]

print(dfs(0,0))
