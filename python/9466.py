from collections import deque

t = int(input())
n = 0
a = []

for i in range(t):
    n = int(input())
    a = [0]+list(map(int,input().split()))
    top = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        top[a[i]]+=1
    q = deque([])
    for i in range(1,n+1):
        if top[i] == 0:
            q.append(i)

    ans = 0
    while q:
        ans+=1
        node =q.popleft()
        top[a[node]]-=1
        if top[a[node]] == 0: q.append(a[node])

    print(ans)
