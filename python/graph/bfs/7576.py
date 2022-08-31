from collections import deque

queue = deque([])

m,n = list(map(int,input().split()))
bat = []

def check_zero(bat):
    for i in range(n):
        for j in range(m):
            if bat[i][j] == 0:
                return True

    return False


def bfs(bat,queue):
    
    while queue:
        x,y = queue.popleft()

        if x-1>=0 and bat[y][x-1]==0:
            queue.append([x-1,y])
            bat[y][x-1]=bat[y][x]+1
        if x+1<m and bat[y][x+1]==0:
            queue.append([x+1,y])
            bat[y][x+1]=bat[y][x]+1
        if y-1>=0 and bat[y-1][x]==0:
            queue.append([x,y-1])
            bat[y-1][x]=bat[y][x]+1
        if y+1<n and bat[y+1][x]==0:
            queue.append([x,y+1])
            bat[y+1][x]=bat[y][x]+1

    return


for i in range(n):
    bat.append(list(map(int,input().split())))

idx = check_zero(bat)

if idx == False:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if bat[i][j] == 1:
                queue.append([j,i])

    bfs(bat,queue)
    ans = 0
    for i in bat:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
            ans = max(ans,j)
    print(ans-1)