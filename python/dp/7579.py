import math

n,m = map(int,input().split())
memory = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
sum_cost = sum(cost)

dp = [[0 for _ in range(sum_cost+1)] for _ in range(n+1)]

ans = math.inf

for i in range(1,n+1):
    for j in range(sum_cost+1):
        # if not(dp[i-1][j]):
        #     continue

        if dp[i][j] !=0:
            dp[i][j] = max(dp[i][j],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        if cost[i]+j <= sum_cost:
            if dp[i][j+cost[i]]!=0:
                dp[i][j+cost[i]] = max(dp[i][j+cost[i]], dp[i-1][j] + memory[i])
            else:
                dp[i][j+cost[i]] = dp[i-1][j] + memory[i]

for i in range(sum_cost+1):
    if dp[n][i] >= m:
        ans = i
        break
print(ans)