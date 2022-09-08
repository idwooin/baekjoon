import sys
input = sys.stdin.readline

mat = []
n,m = map(int,input().split())
for i in range(n):
    mat.append(input())
k = int(input())

answer = 0
for i in range(n):
    zcnt = 0
    for j in range(m):
        if mat[i][j] == '0':
            zcnt+=1

    same= 0
    if k >= zcnt and k%2 == zcnt%2:
        for i2 in range(n):
            if mat[i] == mat[i2]:
                same+=1
    
    answer = max(answer,same)

print(answer)