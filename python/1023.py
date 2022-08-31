n,k = map(int,input().split())

dp = [[] for _ in range(n)]
dp[0].append(['(',-1])
dp[0].append([')',1])

if n == 1:
    if k==0:
        print('(')
    elif k==1:
        print(')')
    else:
        print(-1)
    exit(0)

for i in range(1,n-1):
    for j in range(len(dp[i-1])):
        dp[i].append([dp[i-1][j][0] + '(',dp[i-1][j][1]-1])
        dp[i].append([dp[i-1][j][0] + ')',dp[i-1][j][1]+1])

for j in range(len(dp[n-2])):
    dp[n-1].append([dp[n-2][j][0] + '(',dp[n-2][j][1]-1])
    if dp[n-2][j][1] + 1 != 0:
        dp[n-1].append([dp[n-2][j][0] + ')',dp[n-2][j][1]+1])


print(dp[n-1][k][0]) if k< len(dp[n-1]) else print(-1)