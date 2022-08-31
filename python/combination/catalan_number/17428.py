n,k = map(int,input().split())

def kth(n,j,k):
    if n==1: return 1
    if k>=dp[n][j]: return -1
    if k<dp[n-1][j+1]: return kth(n-1,j+1,k)
    return (1<<(n-1)) + kth(n-1,j-1,k-dp[n-1][j+1])

dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
dp[0][0] = 1

for i in range(1,n+1):
    for j in range(i+1):
        if j==0:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]


ans = kth(n,0,k)
if ans==-1:
    print(-1)
else:
    answer =''
    for i in range(n-1,-1,-1):
        if (1<<i)&ans:
            answer+=')'
        else:
            answer+='('
    print(answer)

    