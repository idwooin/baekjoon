import heapq

n = int(input())

pos = []
neg = []
ans = 0

for i in range(n):
    num = int(input())
    heapq.heappush(pos, num) if num>0 else heapq.heappush(neg, -num)

if len(pos)%2:
    ans+=heapq.heappop(pos)

if len(neg)%2:
    ans-=heapq.heappop(neg)

while pos:
    a1 = heapq.heappop(pos)
    a2 = heapq.heappop(pos)
    if a1 == 1:
        ans+=(a1+a2)
    else:
        ans+=(a1*a2)

while neg:
    n1 = heapq.heappop(neg)
    n2 = heapq.heappop(neg)
    ans+=(n1*n2)

print(ans)
