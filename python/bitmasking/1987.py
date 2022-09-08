from collections import deque

mat=[]

r,c = map(int,input().split())
directions = [(0,1),(1,0),(0,-1),(-1,0)]

for i in range(r):
    mat.append(input())

answer = 1
def dfs(y,x,val,cnt):
    global answer,mat
    answer = max(answer,cnt)
    for i in range(4):
        dy,dx = directions[i]
        if y+dy<0 or y+dy>=r or x+dx<0 or x+dx>=c:
            continue

        nextalpha = ord(mat[y+dy][x+dx])-65

        if (val >> nextalpha)&1 == 0:
            dfs(y+dy,x+dx,val|(1<<nextalpha),cnt+1)

dfs(0,0,1<<ord(mat[0][0])-65,1)
print(answer)

# queue = deque([(0,0,1<<ord(mat[0][0])-65,1)])


# answer = 1
# while queue:
#     y,x,val,cnt = queue.popleft()

#     answer = max(answer,cnt)
#     for i in range(4):
#         dy,dx = directions[i]
#         if y+dy<0 or y+dy>=r or x+dx<0 or x+dx>=c:
#             continue

#         nextalpha = ord(mat[y+dy][x+dx])-65

#         if (val >> nextalpha)&1 == 1:
#             continue

#         queue.append((y+dy,x+dx,val|(1<<nextalpha),cnt+1))

# print(answer)
