import sys

n,s = map(int,sys.stdin.readline().strip().split())
num = list(map(int,sys.stdin.readline().strip().split()))
sums = [0 for _ in range(n)]
sums[0] = num[0]

for i in range(1,n):
    sums[i] = sums[i-1] + num[i]

i=-1
j=0
ans = n+1
while i != n and j!=n:
    curr = sums[j] - sums[i] if i!=-1 else sums[j]

    if curr < s:
        j+=1
    else:
        ans = min(ans,j-i)
        i+=1

if ans == n+1:
    print(0)
else:
    print(ans)