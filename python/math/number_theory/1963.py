from collections import deque
import math

t = int(input())

prime = [0 for _ in range(10000)]
prime[0] = prime[1] = 1

for i in range(2,101):
    if prime[i] == 1:
        continue
    gap = i
    for j in range(2*i,10000,gap):
        prime[j] = 1

def bfs(a,b):
    q = deque([[a,0]])
    visited = [False for i in range(10000)]
    visited[a] = True
    ans = math.inf

    while q:
        num, cnt = q.popleft()

        if num == b: return cnt

        temp = str(num)

        for i in range(1,40):
            qnt = i//10
            rest = i%10
            temp_n = int(temp[:qnt]+str(rest)+temp[qnt+1:])

            if temp_n < 1000 : continue

            if visited[temp_n] == False and prime[temp_n]==0:
                visited[temp_n] = True
                q.append([temp_n,cnt+1])

    return ans

while t:
    a,b = list(map(int,input().split()))
    ans = bfs(a,b)
    if ans == math.inf:
        print("Impossible")
    else:
        print(ans)
    t-=1

    