import sys

n = int(sys.stdin.readline())
tip = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    tip.append([a,b])

ans = 0.0
for i in range(n-1):
    ans += tip[i][0]*tip[i+1][1]
    ans -= tip[i][1]*tip[i+1][0]
ans += (tip[n-1][0]*tip[0][1] - tip[0][0]*tip[n-1][1])

print(round(abs(ans)/2,1))
