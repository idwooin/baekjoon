import heapq

n,k  = list(map(int,input().split()))

jew = []

for i in range(n):
    heapq.heappush(jew,list(map(int,input().split())))

capacity=[]
for i in range(k):
    capacity.append(int(input()))
capacity.sort()

ans = 0
temp = []
for bag in capacity:
    i=0
    while jew and bag>=jew[0][0]:
        heapq.heappush(temp,-heapq.heappop(jew)[1])
    if temp:
        ans-= heapq.heappop(temp)
    elif not jew:
        break

print(ans)