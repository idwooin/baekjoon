import sys
import math

n = int(sys.stdin.readline())
mat = [[0,0] for _ in range(n+1)]
for i in range(1,n+1):
    r,c = list(map(int,sys.stdin.readline().strip().split()))
    mat[i] = [r,c]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for gap in range(1,n):
    for start in range(1,n-gap+1):
        minval = math.inf
        mul = mat[start][0]*mat[start+gap][1]
        for k in range(start,start+gap):
            mul*=mat[k][1]
            minval = min(minval,dp[start][k]+dp[k+1][start+gap]+mul)
            mul//=mat[k][1]
        dp[start][start+gap] = minval
    
print(dp[1][n])