import heapq
import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x==0:
        if not(arr):
            print(0)
        else:
            y,b = heapq.heappop(arr)
            print(y) if b else print(-y)
    else:
        if x < 0:
            heapq.heappush(arr,(-x,0))
        else:
            heapq.heappush(arr,(x,1))
