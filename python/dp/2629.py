import sys

n = int(sys.stdin.readline())
chu = list(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
bead = list(map(int,sys.stdin.readline().strip().split()))
dp = [[0 for _ in range((n+1)*500+1)] for _ in range(n+1)]

def dfs(curr,w):
    if curr > n:
        return
    
    if dp[curr][w] > 0:
        return
    
    dp[curr][w] = 1

    dfs(curr+1,abs(w-chu[curr-1]))
    dfs(curr+1,w)
    dfs(curr+1,w+chu[curr-1])
    
    return

dfs(0,0)
ans = []
for b in bead:
    if b > n*500: ans.append('N')
    else: ans.append('Y') if dp[n][b]==1 else ans.append('N')
for a in ans:
    print(a, end=' ')
