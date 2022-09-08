import sys
from collections import deque
from itertools import permutations,combinations
import math

input = sys.stdin.readline
mat = []
pieceloc = []
answer = 0
piece = 0
directions= [[0,1],[1,0],[0,-1],[-1,0]]

for i in range(5):
    mat.append(input())
    for j,s in enumerate(mat[i]):
        if s=='*':
            piece+=1
            pieceloc.append([i,j])

def check(loc):
    cnt = 0
    queue =deque([loc[0]])
    visited = [[False]*5 for _ in range(5)]
    tempmat = [[False]*5 for _ in range(5)]

    for l in loc:
        tempmat[l[0]][l[1]] = True

    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            dy,dx = directions[i]
            ny = y+dy; nx=x+dx

            if 0<=nx<5 and 0<=ny<5 and tempmat[ny][nx] and visited[ny][nx]==False:
                visited[ny][nx] = True
                cnt+=1
                queue.append([ny,nx])

    return (cnt==len(loc))

def dist(loc):
    global pieceloc
    perm = list(permutations([i for i in range(len(loc))],len(loc)))
    tanswer = math.inf

    for per in perm:
        tempdist = 0
        for idx,p in enumerate(pieceloc):
            tempdist+=abs(p[0]-loc[per[idx]][0])+abs(p[1]-loc[per[idx]][1])

        tanswer = min(tanswer,tempdist)

    return tanswer

def cal_loc(c):
    loc =[]
    for i in range(len(c)):
        loc.append([c[i]//5,c[i]%5])
    
    return loc

def bfs(k):
    answer = math.inf
    comb = list(combinations([i for i in range(25)],k))
    
    for c in comb:
        loc = cal_loc(c)
        if check(loc):
            answer = min(answer,dist(loc))

    return answer


print(bfs(piece))