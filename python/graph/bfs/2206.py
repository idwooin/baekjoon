from collections import deque
import math
import sys

n,m = list(map(int,input().split()))
ans = math.inf
maps = [list(map(int, input())) for _ in range(n)]
queue = deque([])
visited = [[[0 for j in range(m)] for i in range(n)]for k in range(2)]
indices = [[-1,0],[1,0],[0,-1],[0,1]]

# def dfs(maps,n,m,visited,indices,x,y,cnt,wall):
#     global ans

#     if x==n-1 and y==m-1:
#         ans = min(ans,cnt)
#         return


#     for k in range(4):
#         idx = x+indices[k][0]
#         idy = y+indices[k][1]
#         if (idx>=0 and idx<n) and (idy>=0 and idy<m) and visited[idx][idy]==False:
#             if maps[idx][idy]=='1':
#                 if wall==1:
#                     continue
#                 else:
#                     wall+=1

#             visited[idx][idy] = True
#             dfs(maps,n,m,visited,indices,idx,idy,cnt+1,wall)
#             if maps[idx][idy]=='1':
#                 wall-=1
#             visited[idx][idy] = False
        
#     return

def bfs(maps,n,m,ans,visited,queue,indices):
    queue.append([0,0,0])
    visited[0][0][0] = 1

    while queue:
        i,j,h = queue.popleft()
        if i==n-1 and j==m-1:
            return visited[h][i][j]

        for k in range(4):
            idx = i+indices[k][0]
            idy = j+indices[k][1]
            if (idx>=0 and idx<n) and (idy>=0 and idy<m) and visited[h][idx][idy]==0:
                if maps[idx][idy]==1:
                    if h==0:
                        queue.append([idx,idy,h+1])
                        visited[h+1][idx][idy] = visited[h][i][j]+1
                    else:
                        continue
                else:
                    queue.append([idx,idy,h])
                    visited[h][idx][idy] = visited[h][i][j]+1
        
    return ans

ans = bfs(maps,n,m,ans,visited,queue,indices)
ans = -1 if ans == math.inf else ans
print(ans)