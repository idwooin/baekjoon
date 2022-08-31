from collections import deque

T = int(input())

def bfs(list1,i,j,n,m):
    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        list1[i][j] = False

        if i+1<n and list1[i+1][j]:
            list1[i+1][j] = False
            queue.append((i+1,j))
        if i-1>=0 and list1[i-1][j]:
            list1[i-1][j] = False
            queue.append((i-1,j))
        if j-1>=0 and list1[i][j-1]:
            list1[i][j-1] = False
            queue.append((i,j-1))
        if j+1<m and list1[i][j+1]:
            list1[i][j+1] = False
            queue.append((i,j+1))

    return

for i in range(T):
    ans = 0
    m,n,k = list(map(int,input().split()))
    list1 = [[False for j in range(m)] for t in range(n)]

    for j in range(k):
        x,y = list(map(int,input().split()))
        list1[y][x] = True

    for j in range(n):
        for t in range(m):
            if list1[j][t]:
                bfs(list1,j,t,n,m)
                ans+=1


    print(ans)