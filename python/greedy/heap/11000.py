import heapq
n = int(input())

start_heap = []

for i in range(n):
    start,end = list(map(int,input().split()))
    heapq.heappush(start_heap,(start,end))

end_heap = []
ans = 0

while start_heap:
    start,end = heapq.heappop(start_heap)
    if not(end_heap):
        heapq.heappush(end_heap,end)
        ans+=1
        continue

    min_time=heapq.heappop(end_heap)

    if min_time > start:
        heapq.heappush(end_heap,end)
        heapq.heappush(end_heap,min_time)
        ans+=1
    else:
        heapq.heappush(end_heap,end)

print(ans)

