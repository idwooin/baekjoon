import sys
input = sys.stdin.readline

n = int(input())
buy = []
maxcnt = [[0,10] for _ in range(n)]

for _ in range(n):
    buy.append(input())

answer = 0
dp = [[[0 for _ in range(10)] for _ in range(15)]for _ in range(2**16)]

def dfs(curr,maxp,visited,cnt):
    global buy,dp,answer

    if dp[visited][curr][maxp]!=0:
        return
    
    dp[visited][curr][maxp] = cnt
    answer = max(answer,cnt)
    
    for i in range(n):
        if (visited&(1<<i))>>i == 1:
            continue
        else:
            if int(buy[curr][i]) >= maxp:
                dfs(i,int(buy[curr][i]),visited|(1<<i),cnt+1)

    return

dfs(0,0,1,1)
print(answer)