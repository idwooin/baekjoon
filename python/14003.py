import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().strip().split()))

ls = [-1000000001]
idx = [0 for _ in range(n+1)]

def binary_search(num,start,end):

    while start!=end:
        mid = (start+end)//2
        if num > ls[mid]:
            start = mid+1
        else:
            end = mid
    
    ls[start] = num
    return start
    

for i in range(n):
    if ls[-1] < a[i]:
        idx[i+1] = len(ls)
        ls.append(a[i])
    else:
        temp = binary_search(a[i],0,len(ls)-1)
        idx[i+1] = temp

ans = deque([])
max_num = len(ls)-1
for i in range(n,0,-1):
    if max_num == 0:
        break

    if idx[i] != max_num:
        continue
    ans.append(a[i-1])
    max_num-=1


print(len(ls)-1)

while ans:
    print(ans.pop(),end=' ')