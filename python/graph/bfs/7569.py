from collections import deque

m,n,h = list(map(int,input().split()))
tensor = [[[0 for k in range(m)] for j in range(n)] for i in range(h)]
queue = deque([])
cnt_zero = 0
for i in range(h):
    for j in range(n):
        temp = list(map(int,input().split()))
        for k in range(m):
            if temp[k] == 1:
                queue.append([i,j,k,0])
            elif temp[k] == 0:
                cnt_zero+=1
            tensor[i][j][k] = temp[k]

indices = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

ans = -1

while queue:
    i,j,k,day=queue.popleft()
    ans = max(ans,day)

    for t in range(6):
        idx,idy,idz = indices[t]
        idx = i+idx; idy = j+idy; idz = k+idz;
        if idx>=0 and idx<h and idy>=0 and idy<n and idz>=0 and idz<m:
            if tensor[idx][idy][idz] == 0:
                cnt_zero-=1
                tensor[idx][idy][idz] = 1
                queue.append([idx,idy,idz,day+1])

ans = -1 if cnt_zero>0 else ans
print(ans)

    