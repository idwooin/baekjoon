import sys

m = int(sys.stdin.readline())
max_val = 1000000007
def convert_modulo(n,s):
    pow = 1000000005
    ans = 1

    while pow>0:
        rest=pow%2
        if rest:
            ans=(ans*n)%max_val
        n=(n*n)%max_val
        pow=pow//2
    
    return (ans*s)%max_val

answer = 0
for i in range(m):
    n,s = list(map(int,sys.stdin.readline().strip().split()))
    answer=(answer+convert_modulo(n,s))%max_val
print(answer)