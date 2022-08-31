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
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr,-x)