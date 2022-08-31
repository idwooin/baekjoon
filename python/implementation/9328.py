import sys
from collections import deque

t = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]

maps = []
ans = 0
dic = []
h = 0
w = 0

def bfs(i,j):
    q = deque()
    visited = [[0]*(w+2) for _ in range(h+2)]
    q.append([i,j])
    visited[i][j] = 1
    cnt = 0
    while q:
        ci,cj = q.popleft()
        for k in range(4):
            newi,newj = ci+di[k],cj+dj[k]
            if 0<=newi<h+2 and 0<=newj<w+2:
                if visited[newi][newj]:
                    continue

                if maps[newi][newj] == '.':
                    visited[newi][newj] = 1
                    q.append([newi,newj])
                elif maps[newi][newj].islower():
                    dic[ord(maps[newi][newj])-ord('a')] = 1
                    q = deque()
                    visited = [[0]*(w+2) for _ in range(h+2)]
                    maps[newi][newj] = '.'
                    q.append([newi,newj])
                elif maps[newi][newj].isupper():
                    if dic[ord(maps[newi][newj])-ord('A')]:
                        visited[newi][newj] = 1
                        maps[newi][newj] = '.'
                        q.append([newi,newj])
                elif maps[newi][newj] == '$':
                    visited[newi][newj] = 1
                    cnt+=1
                    maps[newi][newj] = '.'
                    q.append([newi,newj])

    return cnt

for i in range(t):
    dic = [0]*26
    ans = 0
    h,w = map(int,sys.stdin.readline().strip().split())
    maps = [['.']*(w+2) for _ in range(h+2)]
    for i in range(1,h+1):
        temp = sys.stdin.readline().strip()
        for j in range(w):
            maps[i][j+1] = temp[j]
    keys = sys.stdin.readline().strip()
    if keys != '0':
        for k in keys:
            dic[ord(k)-97] = 1

    print(bfs(0,0))