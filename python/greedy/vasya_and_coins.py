import sys

t = int(sys.stdin.readline())
for i in range(t):
    a,b = map(int,sys.stdin.readline().strip().split())
    if a==0:
        print(1)
    else:
        print(a*1+b*2+1)