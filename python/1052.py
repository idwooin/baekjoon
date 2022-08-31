from collections import deque

n,k = map(int,input().split())
bottle_type = [0 for _ in range(25)]

q = deque([])
cnt = 0
while n>0:
    if n%2:
        bottle_type[cnt]+=1
        q.append(cnt)
    n//=2
    cnt+=1

diff = k-sum(bottle_type)
if diff>=0:
    print(0)
else:
    while len(q) > abs(diff-1):
        q.pop()
    max_bottle = q.pop()
    ans=1<<max_bottle
    while q:
        ans-=1<<q.pop()
    
    print(ans)
