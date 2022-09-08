import heapq

n = int(input())
pq = []
for _ in range(n):
    x,y = map(int,input().split())
    heapq.heappush(pq,(x,y))

x,y = heapq.heappop(pq)
start = x
end = y
minus = 0

while pq:
    x,y = heapq.heappop(pq)

    if x <= end:
        if y > end:
            end = y
    else:
        minus+=(x-end)
        end=y

print(end-start-minus)