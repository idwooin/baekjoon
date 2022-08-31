import heapq
import math

n,k = list(map(int,input().split()))
order = list(map(int,input().split()))
capacity = []
ans = 0

pred = [math.inf for i in range(k)]
dict={}

for i in range(101):
    dict[i] = 0

for i in range(len(order)-1,-1,-1):
    pred[i] = dict[order[i]]
    dict[order[i]] = i

print(pred)

for i in range(n):
    heapq.heappush(capacity,[pred[i]-(n-i+1),order[i]])

for i in range(n,k):
    for i in range(n):
        capacity[i][0]-=1
    p,o = capacity.get()

    if p < math.inf and o==order[i]:
        capacity.put((pred[i],order[i]))
    elif p < math.inf and o!=order[i]:
        capacity.put((pred[i],order[i]))
        ans+=1


print(ans)