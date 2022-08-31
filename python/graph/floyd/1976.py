import math

n = int(input())
m = int(input())

def floyd(mat):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if start==end: continue
                mat[start][end] = min(mat[start][end],mat[start][mid] + mat[mid][end])
    return

mat = [[math.inf for i in range(n)]for j in range(n)]

for i in range(n):
    mat[i][i] = 0

for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] != 0:
            mat[i][j] = 1

floyd(mat)
plan = list(map(int,input().split()))
flag = True
for i in range(m-1):
    if mat[plan[i]-1][plan[i+1]-1] < math.inf:
        continue
    flag = False
    break

print("YES") if flag else print("NO")