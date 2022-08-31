from collections import deque

n = int(input())
time = []
for i in range(n):
    start,end = list(map(int,input().split()))
    time.append([start,end])

time.sort()
ans = deque([])
ans.append(time[0])

for i in range(1,n):
    if ans[-1][0] <= time[i][0] and time[i][1] <= ans[-1][1]:
        diff =time[i][1] - time[i][0]
        if diff == 0 and time[i][1] == ans[-1][1]:
            ans.append(time[i])
            continue
        ans.popleft()
        ans.append(time[i])
        continue

    if ans[-1][1] <= time[i][0]:
        ans.append(time[i])

print(len(ans))
