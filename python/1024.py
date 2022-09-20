import sys

input = sys.stdin.readline
n,l = map(int,input().split())

def final(a,b):
    for i in range(b):
        print(a+i,end='')
        if i!=b-1:
            print(end=' ')

while True:
    if l > 100:
        print(-1)
        exit(0)
    
    result = 0
    for i in range(l):
        result+=i

    diff = n-result

    if diff < 0:
        print(-1)
        exit(0)
    
    if diff%l!=0:
        l+=1
    else:
        final(diff//l,l)
        exit(0)