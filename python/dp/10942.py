import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline())
query = [list(map(int,sys.stdin.readline().strip().split())) for i in range(m)]
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

def check(dp,a,b):
    if num[a-1]!=num[b-1]:
        dp[a][b] = 0
        return 0

    if a==b or a+1==b:
        dp[a][b] = 1
        return 1
    
    if dp[a+1][b-1] == 1:
        dp[a][b] = 1
        return 1
    elif dp[a+1][b-1] == -1:
        result = check(dp,a+1,b-1)
        if result:
            dp[a][b] = 1
            return 1
        else:
            dp[a][b] = 0
            return 0
    else:
        dp[a][b] = 0
        return 0

for q in query:
    a,b = q
    print(check(dp,a,b))