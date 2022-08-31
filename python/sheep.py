import math
import sys

def bfs(start,sheep,wolves,info,dic):
    if sheep + wolves == len(info): return sheep

    maxval = 0
    
    for d in dic[start]:
        if info[d]==1:
            if sheep <= wolves+1:
                maxval = max(maxval,sheep)
                continue
            else:
                info[d] = -1
                maxval = max(maxval,bfs(d,sheep,wolves+1,info,dic))
                info[d] = 1
        elif info[d] == 0:
            info[d] = -1
            maxval = max(maxval,bfs(d,sheep+1,wolves,info,dic))
            info[d] = 0
        else:
            maxval = max(maxval,bfs(d,sheep,wolves,info,dic))
    
    return maxval

def solution(info, edges):
    answer = 0
    sys.setrecursionlimit(10000)
    dic = {}
    for i in range(len(info)): dic[i] = []
    for e in edges:
        dic[e[0]].append(e[1])
        dic[e[1]].append(e[0])
    
    info[0] = -1
    answer = bfs(0,1,0,info,dic)
    
    return answer

info = list(map(int,input().split()))
edges = [list(map(int,input().split())) for i in range(11)]
print(solution(info,edges))