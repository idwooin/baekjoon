from collections import deque

n = int(input())
maps=[]
ans = 0

def dfs(maps,cnt):
    global ans

    if cnt == 5:
        return

    q1 = deque([])
    q2 = deque([])
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n-1,-1,-1):
            if maps[i][j] == 0:
                continue
            q1.append(maps[i][j])
        while q1:
            a = q1.popleft()
            if q1 and a==q1[0]:
                q2.append(a*2)
                q1.popleft()
            else:
                q2.append(a)

        k = n-1
        while q2:
            r = q2.popleft()
            ans = max(ans,r)
            temp[i][k] = r
            k-=1
        while k>=0:
            temp[i][k] = 0
            k-=1

    dfs(temp,cnt+1)

    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n-1,-1,-1):
            if maps[j][i] == 0:
                continue
            q1.append(maps[j][i])
        while q1:
            a = q1.popleft()
            if q1 and a==q1[0]:
                q2.append(a*2)
                q1.popleft()
            else:
                q2.append(a)

        k = n-1
        while q2:
            r = q2.popleft()
            ans = max(ans,r)
            temp[k][i] = r
            k-=1
        while k>=0:
            temp[k][i] = 0
            k-=1

    dfs(temp,cnt+1)

    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                continue
            q1.append(maps[i][j])
        while q1:
            a = q1.popleft()
            if q1 and a==q1[0]:
                q2.append(a*2)
                q1.popleft()
            else:
                q2.append(a)
        k = n-1
        k = 0
        while q2:
            r = q2.popleft()
            ans = max(ans,r)
            temp[i][k] = r
            k+=1
        while k<n:
            temp[i][k] = 0
            k+=1

    dfs(temp,cnt+1)

    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maps[j][i] == 0:
                continue
            q1.append(maps[j][i])
        while q1:
            a = q1.popleft()
            if q1 and a==q1[0]:
                q2.append(a*2)
                q1.popleft()
            else:
                q2.append(a)
        k = 0
        while q2:
            r = q2.popleft()
            ans = max(ans,r)
            temp[k][i] = r
            k+=1
        while k<n:
            temp[k][i] = 0
            k+=1

    dfs(temp,cnt+1)

for i in range(n):
    maps.append(list(map(int,input().split())))
dfs(maps,0)
print(ans)