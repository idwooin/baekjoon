#hop-craft algorithm

from collections import deque
import math
left = []
right = []
levels = []
mm = []
edges = []

def bfs():
    q = deque([])

    for i in range(n):
        if mm[i] == 0:
            levels[i] = 0
            q.append(i)
        else:
            levels[i] = math.inf

    while q:
        node = q.popleft()
        for r in edges[node]:
            if right[r] == -1:
                continue
            if levels[right[r]] != math.inf:
                continue
            levels[right[r]] = levels[node] + 1
            q.append(right[r])

    return

def dfs(node):
    for b in edges[node]:
        if right[b] == -1 or (levels[right[b]] == levels[node]+1 and dfs(right[b])):
            mm[node] = 1
            left[node] = b
            right[b] = node
            return True

    return False

while True:
    try:
        n = input()
        n = int(n)
        left = [-1 for i in range(n)]
        edges = [[] for _ in range(n)]
        right = [-1 for i in range(n)]
        mm = [0 for i in range(n)]
        levels = [0 for i in range(n)]

        for i in range(n):
            s = input()
            j = 0
            k = 0
            while k < len(s):
                if s[k] != ' ':
                    arr = ""
                    if j ==0:
                        while s[k]!=' ':
                            arr += s[k]
                            k+=1
                        v = int(arr[:-1])
                        j+=1
                    elif j==1:
                        while s[k]!=' ':
                            arr += s[k]
                            k+=1
                        right_n = int(arr[1:-1])
                        j+=1
                    else:
                        while k<len(s) and s[k]!=' ':
                            arr += s[k]
                            k+=1
                        edges[v].append(int(arr)-n)
                k+=1

        ans = 0
        while True:
            bfs()
            flow = 0
            for j in range(n):
                if mm[j]==0 and dfs(j): flow+=1
            # p 집합이 공집합이라면
            if flow == 0:break
            ans+=flow

        print(ans)
    except EOFError:
        break