# import sys
# c = int(sys.stdin.readline())
# di = [-1,0]
# dj = [1,1]

# def bipartite(left,right,arr,idx,check):
#     i,j = idx

#     for r_i,r_j in left[i][j]:
#         if arr[r_i][r_j] == '-':
#             return False

#         if check[r_i][r_j] == True:
#             continue
#         check[r_i][r_j] = True

#         if right[r_i][r_j] == [-1,-1] or bipartite(left,right,arr,right[r_i][r_j],check):
#             right[r_i][r_j] = idx
#             return True

#     return False

# while c>0:
#     ans = 0
#     xcnt = 0
#     n,m = map(int,sys.stdin.readline().split())
#     arr = [['.' for _ in range(m)] for _ in range(n)]
#     left = [[[] for _ in range(m)] for _ in range(n)]
#     right = [[[-1,-1] for _ in range(m)] for _ in range(n)]
#     total = n*m

#     for i in range(n):
#         strs = sys.stdin.readline().strip()
#         for j in range(m):
#             if strs[j] == 'x':
#                 arr[i][j] = 'x'
#                 total-=1
#                 #continue

#             for k in range(2):
#                 newi=i+di[k]
#                 newj=j+dj[k]
#                 if newi>=0 and newi<n and newj>=0 and newj<m:
#                     left[i][j].append([newi,newj])

#     for i in range(n):
#         for j in range(m):
#             if right[i][j] != [-1,-1]:
#                 continue
#             check = [[False for _ in range(m)] for _ in range(n)]
#             if bipartite(left,right,arr,[i,j],check):
#                 arr[i][j] = '-'

#     s = set()

#     for i in range(n):
#         for j in range(m):
#             if right[i][j] == [-1,-1]:
#                 continue

#             x,y = right[i][j]
#             temp = str(x)+str(y)
#             s.add(temp)

#     ans = len(s)

#     if m%2 == 1:
#         for i in range(n):
#             if arr[i][m-1]=='.':
#                 if j-1>=0 and arr[i][j-1]=='-':
#                     continue
#                 if i-1>=0 and j-1>=0 and arr[i-1][j-1]=='-':
#                     continue
#                 ans+=1

#     ans = ans-xcnt
#     if ans < total-ans:
#         ans = total-ans

#     print(ans)
#     c-=1

import sys
import re
T = int(sys.stdin.readline())
results = []
 
def dfs(x):
    global bimap
    global matched
    global visited
    if visited[x]: return False
    visited[x] = True
    for y, link in enumerate(bimap[x]):
        if link:
            # bimap[x][y] = 0 # visited
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False
 
for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    x_start = 0
    x_idx = 0
    y_start = 0
    y_idx = 0
    max = 0
    matched = {}
    sit_cnt = 0
 
    # ?????? ?????? ????????? 0?????? ?????????
    coord_map = []
    for _ in range(M):
        coord_map.append([0 for _ in range(N)])
 
    X = {}
    Y = {}
    
    bimap = []
    if N % 2 == 0:
        for _ in range(int(N/2)*M): bimap.append([0 for _ in range(int(N/2)*M)])
    else:
        for _ in range((int(N/2)+1)*M): bimap.append([0 for _ in range(int(N/2)*M)])
 
    # ???????????? ?????? ????????? ????????? ?????? ??????(?????? ?????? X, ?????? ?????? Y??? ??????)??? ????????? ?????????.
    # X??? ?????????, Y??? ???????????? ???. ??? ??? ???????????? ????????? ???????????????
    # ???????????? ???????????? ?????? ?????? ????????? ?????? ???????????? ?????? ??? ??????.
    # X, Y ?????? ???????????? ??????, {(X ??????, Y ??????): (?????? ??????????????? ??????, ????????? ????????? ??????)} ????????? ??????.
    for x in range(M):
        row = sys.stdin.readline().replace("\n", "")
 
        turn = "X"
        x_idx = x_start
        y_idx = y_start
        for y, value in enumerate(row):
            if turn == "X":
                if value == ".":
                    X[(x, y)] = (x_idx, 1)
                    sit_cnt += 1
                else: X[(x, y)] = (x_idx, 0)
                x_idx += M
                turn = "Y"
            else:
                if value == ".":
                    Y[(x, y)] = (y_idx, 1)
                    sit_cnt += 1
                else: Y[(x, y)] = (y_idx, 0)
                y_idx += M
                turn = "X"
        x_start += 1
        y_start += 1
 
        # ??? ????????? ????????? ????????? ????????? ?????? ??? ??????
        for y, value in enumerate(row):
            if value == ".": coord_map[x][y] = 1
 
    # ?????????(X)??? ???????????? ????????? ??????
    for x, y in X:
        item = X[(x, y)]
        if not item[1]: continue
        # ????????? ????????? ?????????
        candidates = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y+1), (x, y+1), (x+1, y+1)]
        for cx, cy in candidates:
            # ????????? ????????? ????????? ????????? ????????? ?????? ??????, 
            if 0 <= cx < M and 0 <= cy < N and coord_map[cx][cy]:
                # ????????? ?????? ?????? ????????? ?????? ????????? X index???
                # ????????? ????????? ???????????? ?????? ????????? Y index??? ????????????
                bigraph_x = X[(x, y)][0]
                bigraph_y = Y[(cx, cy)][0]
 
                # ??? ??? ????????? ??????.
                bimap[bigraph_x][bigraph_y] = 1
 
    # ?????? ?????????????????? ?????? ????????? ????????? ????????? ?????? dfs??? ??????.
    for i in range(len(X)):
        visited = [False for _ in range(len(X))]
        dfs(i)
    
    result = sit_cnt - len(matched)
    results.append(result)
 
for result in results:
    sys.stdout.write(str(result)+'\n')