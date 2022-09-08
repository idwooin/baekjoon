from collections import deque

n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(input())

visited = [[-1]*m for _ in range(n)]

queue = deque([(0,0,0)])
direction = [(0,1),(1,0),(0,-1),(-1,0)]

while queue:
    y,x,val = queue.popleft()
    if visited[y][x] != -1:
        if val+1 >= visited[y][x]:
            continue
        else:
            visited[y][x] = val+1
    else:
        visited[y][x] = val+1

    for i in range(4):
        dy,dx = direction[i]
        if y+dy>=0 and y+dy<n and x+dx>=0 and x+dx<m:
            if mat[y+dy][x+dx] == '1':
                queue.append((y+dy,x+dx,visited[y][x]))

print(visited[n-1][m-1])
