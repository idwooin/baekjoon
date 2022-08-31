n,m = list(map(int,input().split()))
ans = 0

if n<=m:
    ans = 0

else:
    edge = [[[0]*n for j in range(n+1)]for i in range(n+1)]
    for i in range(m):
        a,b = list(map(int,input().split()))


print(ans)