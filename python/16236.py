from collections import deque
import heapq
import math

n = int(input())
mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))

cy=cx=0
dict={}
for i in range(n):
    for j in range(n):
        if mat[i][j]!=0 and mat[i][j]!=9:
            if mat[i][j] in dict:
                dict[mat[i][j]].append((i,j))
            else:
                dict[mat[i][j]] = [(i,j)]
        elif mat[i][j] == 9:
            cy=i; cx=j

level = 2
eat = 0

if 1 in dict:
    queue = deque([*dict[1]])
else:
    print(0)
    exit()

directions=[(0,1),(1,0),(0,-1),(-1,0)]
visited = [[math.inf]*n for _ in range(n)]
def dfs(cy,cx,y,x,d):
    global level,mat,visited,n

    if visited[cy][cx] <= d:
        return
    
    visited[cy][cx] = d

    if cy==y and cx==x:
        return

    for i in range(4):
        dy,dx = directions[i]
        if cy+dy<0 or cy+dy>=n or cx+dx<0 or cx+dx>=n:
            continue
        if mat[cy+dy][cx+dx] <= level:
            dfs(cy+dy,cx+dx,y,x,d+1)

    return

answer = 0
while True:
    l1=[]

    if not(queue):
        break

    while queue:
        y,x = queue.popleft()
        visited = [[math.inf]*n for _ in range(n)]
        dfs(cy,cx,y,x,0)
        dist = visited[y][x]
        if dist!=math.inf:
            heapq.heappush(l1,(dist,y,x))
    
    if l1:
        dist,y,x = heapq.heappop(l1)
        answer+=dist
        eat+=1
        mat[cy][cx] = 0
        mat[y][x] = 9
        cy=y; cx=x

        if eat == level:
            level+=1
            eat=0
            if level-1 in dict:
                for item in dict[level-1]:
                    queue.append(item)

        while l1:
            dist,y,x = heapq.heappop(l1)
            queue.append((y,x))
    else:
        break

print(answer)