import sys

r1,c1,r2,c2 = map(int,input().split())
mat = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
total = (c2-c1+1) * (r2-r1+1)
direction = 1
x = 0
y = 0
cnt = 1
l = 1
maxnum = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while total > 0:
    for _ in range(2):
        for _ in range(l):
            if x>=c1 and x<=c2 and y>=r1 and y<=r2:
                mat[y-r1][x-c1] = cnt
                maxnum = cnt
                total-=1
            cnt+=1
            y+=dy[direction]
            x+=dx[direction]
        direction = (direction-1)%4
    l+=1

ten = len(str(maxnum))

for i in range(len(mat)):
    for j in range(len(mat[i])-1):
        temp = str(mat[i][j])
        temp = ' '*(ten-len(temp))+temp
        print(temp,end=' ')
    temp = str(mat[i][len(mat[i])-1])
    temp = ' '*(ten-len(temp))+temp
    print(temp)