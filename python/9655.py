n = int(input())

dp = ["" for i in range(1001)]
dp[1] = "SY"
dp[2] = "CY"
dp[3] = "SY"

for i in range(4,n+1):
    dp[i] = "CY" if dp[i-1] == "SY" else "SY"

print(dp[n])
