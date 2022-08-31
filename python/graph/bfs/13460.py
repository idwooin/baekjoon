from collections import deque
import math

n,m = map(int,input().split())
maps = []
di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = math.inf
q = deque([])
for i in range(n):
    maps.append(input())

def bfs(q):
    global ans
    visited = {}
    while q:
        b1,b2,r1,r2,cnt=q.popleft()
        if ans <= cnt:
            continue

        if cnt == 10:
            continue

        for i in range(4):
            mover = 0
            moveb = 0
            flag = False
            temp = []
            
            row = b1
            col = b2
            while True:
                row+=di[i]
                col+=dj[i]
                moveb+=1
                if maps[row][col] == 'O':
                    ans = min(ans,11)
                    flag = True
                    break
                if maps[row][col] == '#':
                    temp.append(row-di[i])
                    temp.append(col-dj[i])
                    moveb-=1
                    break

            if flag:
                continue

            row = r1
            col = r2
            while True:
                row+=di[i]
                col+=dj[i]
                mover+=1
                if maps[row][col] == 'O':
                    ans = min(ans,cnt+1)
                    flag = True
                    break
                if maps[row][col] == '#':
                    temp.append(row-di[i])
                    temp.append(col-dj[i])
                    mover-=1
                    break

            if flag:
                continue
            
            if temp[0] == temp[2] and temp[1] == temp[3]:   
                if moveb > mover:
                    temp[0] = temp[2]-di[i]
                    temp[1] = temp[3]-dj[i]
                elif mover > moveb:
                    temp[2] = temp[0]-di[i]
                    temp[3] = temp[1]-dj[i]

            if (temp[0],temp[1],temp[2],temp[3]) in visited:
                continue
            visited[(temp[0],temp[1],temp[2],temp[3])] = 1

            temp.append(cnt+1)
            q.append([*temp])
    return

r = []
b = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            r = [i,j]
        elif maps[i][j] == 'B':
            b = [i,j]

q.append([*b,*r,0])

bfs(q)
print(ans) if ans <= 10 else print(-1)