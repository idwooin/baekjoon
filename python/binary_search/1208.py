import heapq

sums1 = []
sums2 = []
n,s = map(int,input().split())
a = list(map(int,input().split()))
if len(a)==1:
    if a[0] == s:
        print(1)
    else:
        print(0)
    exit(0)

a.sort()
a1 = a[:n//2]
a2 = a[n//2:]

def dfs(cnt,sum,minidx,flag,visited,aa,sums):
    if cnt == 0:
        if flag:
            heapq.heappush(sums,-sum)
        else:
            heapq.heappush(sums,sum)
        return
    
    for i in range(minidx,len(aa)):
        if visited[i]: continue
        visited[i] = True
        dfs(cnt-1,sum+aa[i],i,flag,visited,aa,sums)
        visited[i] = False

for i in range(len(a1)+1):
    visited = [False for _ in range(len(a1))]
    dfs(i,0,0,0,visited,a1,sums1)

for i in range(len(a2)+1):
    visited = [False for _ in range(len(a2))]
    dfs(i,0,0,1,visited,a2,sums2)

ans = 0
c1 = heapq.heappop(sums1)
c2 = heapq.heappop(sums2)
while True:
    if c1-c2 > s:
        if not(sums2):
            break
        c2 = heapq.heappop(sums2)
    elif c1-c2 < s:
        if not(sums1):
            break
        c1 = heapq.heappop(sums1)
    else:
        flag = False
        r = 0
        temp = c2
        while c2==temp:
            r+=1
            if not(sums2):
                flag = True
                break
            temp = heapq.heappop(sums2)
        if not(flag):
            c2 = temp

        l = 0
        temp = c1
        while c1==temp:
            l+=1
            if not(sums1):
                flag = True
                break
            temp = heapq.heappop(sums1)
        if not(flag):
            c1 = temp

        ans += l*r
        if flag:
            break

if s == 0:
    print(ans-1)
else:
    print(ans)
