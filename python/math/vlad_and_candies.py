import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    candies = list(map(int,sys.stdin.readline().strip().split()))
    candies.sort()
    if n == 1:
        print("YES") if candies[0] == 1 else print("NO")
    else:
        print("YES") if candies[n-1]-candies[n-2] <= 1 else print("NO")
