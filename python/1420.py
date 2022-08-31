import math
from tracemalloc import start
n,m = map(int,input().split())
maps = []

di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(n):
    maps.append(input().strip())

s = []
t = []
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 'K':
            s = [i,j]
        if maps[i][j] == 'H':
            t = [i,j]

for i in range(n):
    for j in range(m):
        flow[i][2*j]
flow = [[math.inf for _ in range(m*2)] for _ in range(n*2)]
edges[s[0]*2*m+s[1]*2][s[0]*2*m+s[1]*2+1] = 1