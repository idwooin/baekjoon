import heapq
wire = int(input())
queue =[]
num = []
dic = {}

for i in range(wire):
    a,b = map(int,input().split())
    heapq.heappush(queue,[a,b])

cnt = 0
while queue:
    a,b = heapq.heappop(queue)
    dic[cnt] = a
    num.append(b)
    cnt+=1

lis = [num[0]]
idx = [[0,num[0]]]
def binary_search(lis,target):
    left = 0
    right = len(lis)-1

    while left<right:
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid+1
        else:
            right = mid

    return right

for i in range(1,len(num)):
    target = num[i]
    if lis[-1] < target:
        lis.append(target)
        idx.append([len(lis)-1,target])
        continue
    f=binary_search(lis,target)
    idx.append([f,target])
    lis[f] = target

print(len(num)-len(lis))
ans = [0 for _ in range(len(lis))]

j = len(lis)-1
for i in range(wire-1,-1,-1):
    id,t = idx[i]
    if id == j:
        ans[id] = t
        j-=1

j = 0
final = []
for i in range(len(num)):
    if j < len(ans):
        if num[i] == ans[j]:
            j+=1
            continue
    final.append(dic[i])

final.sort()
for f in final:
    print(f)
