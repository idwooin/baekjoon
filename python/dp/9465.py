import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    up = list(map(int,sys.stdin.readline().strip().split()))
    d = list(map(int,sys.stdin.readline().strip().split()))

    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0][1] = up[0]
    dp[0][2] = d[0]

    for j in range(1,n):
        dp[j][0] = max(dp[j-1][0],dp[j-1][1],dp[j-1][2])
        dp[j][1] = up[j]+max(dp[j-1][0],dp[j-1][2])
        dp[j][2] = d[j]+max(dp[j-1][0],dp[j-1][1])

    print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))