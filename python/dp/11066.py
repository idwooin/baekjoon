import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    book = list(map(int,sys.stdin.readline().strip().split()))
    answer = 0
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
    sums = [0 for _ in range(k+1)]

    for i in range(1,k+1):
        sums[i] = sum(book[:i])

    for gap in range(1,k):
        for j in range(1,k+1-gap):
            minval = math.inf
            for u in range(j,j+gap):
                minval = min(minval, dp[j][u]+dp[u+1][j+gap])
            dp[j][j+gap] = minval + sums[j+gap] - sums[j-1]
    
    print(dp[1][k])