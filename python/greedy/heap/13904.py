import heapq

n=int(input())
assign = []
scores = []
max_day = 0
ans=  0

for i in range(n):
    deadline,score = list(map(int,input().split()))
    max_day = max(max_day,deadline)
    heapq.heappush(assign,[-deadline,-score])

for day in range(max_day,0,-1):
    while assign:
        temp = heapq.heappop(assign)
        if day > -temp[0]:
            heapq.heappush(assign, temp)
            break
        heapq.heappush(scores,temp[1])
    
    if scores:
        ans+= -heapq.heappop(scores)

print(ans)