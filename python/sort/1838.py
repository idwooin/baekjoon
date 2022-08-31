n = int(input())
a = list(map(int,input().split()))
ans = 0
dic1 = {}
dic2 = {}
for i in range(n):
    dic1[a[i]] = i
a.sort()
for i in range(n):
    dic2[a[i]] = i

for key in dic1:
    ans = max(ans,dic1[key]-dic2[key])

print(ans)
