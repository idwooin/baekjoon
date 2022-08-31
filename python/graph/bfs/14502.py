from collections import deque
import copy

l = []
virus = deque([])
n,m = list(map(int,input().split()))
lab = []
ans = 0

def check(lab_temp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lab_temp[i][j] == 0:
                cnt+=1

    return cnt

def bfs(lab,n,m):
    virus = deque([])
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virus.append((i,j))

    lab_temp = copy.deepcopy(lab)

    while virus:
        i,j = virus.popleft()

        if i-1>=0 and lab_temp[i-1][j] == 0:
            lab_temp[i-1][j] = 2
            virus.append((i-1,j))
        if i+1<n and lab_temp[i+1][j] == 0:
            lab_temp[i+1][j] = 2
            virus.append((i+1,j))
        if j-1>=0 and lab_temp[i][j-1] == 0:
            lab_temp[i][j-1] = 2
            virus.append((i,j-1))
        if j+1<m and lab_temp[i][j+1] == 0:
            lab_temp[i][j+1] = 2
            virus.append((i,j+1))

    return check(lab_temp)
    
    
for i in range(n):
    lab.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            l.append((i,j))

length = len(l)

for i in range(length-2):
    onei,onej = l[i]
    for j in range(i+1,length-1):
        twoi,twoj = l[j]
        for k in range(j+1,length):
            threei,threej = l[k]
            lab[onei][onej] = 1
            lab[twoi][twoj] = 1
            lab[threei][threej] = 1
            ans = max(ans,bfs(lab,n,m))
            lab[onei][onej] = 0
            lab[twoi][twoj] = 0
            lab[threei][threej] = 0
            



print(ans)