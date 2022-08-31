mod = 1000000007
n = int(input())
dp = [[0 for _ in range(1516)]for _ in range(3)]

dp[0][2] = dp[1][2]=1

for i in range(3,1516):
    dp[0][i] = (dp[1][i-1] + dp[2][i-1])%mod
    dp[1][i] = (dp[0][i-1] + dp[2][i-1])%mod
    dp[2][i] = (dp[0][i-1] + dp[1][i-1])%mod

print(dp[0][n])