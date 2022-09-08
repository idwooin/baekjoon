import math

n = int(input())
m = int(input())

bustoll = [[math.inf]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    bustoll[a][b] = min(bustoll[a][b],c)

for i in range(1,n+1):
    bustoll[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            bustoll[i][j] = min(bustoll[i][j],bustoll[i][k] + bustoll[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bustoll[i][j] == math.inf:
            bustoll[i][j] = 0

for idx,f in enumerate(bustoll):
    if idx==0:
        continue
    print(*f[1:],sep=' ')