import sys
from collections import deque
n,m = list(map(int,sys.stdin.readline().strip().split()))
l = list(map(int,sys.stdin.readline().strip().split()))
ans = 0
q = deque([])
for i in range(1,n+1):
    q.append(i)

for item in l:
    cnt = 0

    while True:
        temp = q.popleft()
        if temp==item:
            break
        q.append(temp)
        cnt+=1
    
    ans+=min(cnt,len(q)+1-cnt)
     
print(ans)