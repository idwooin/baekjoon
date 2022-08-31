def divide(a,b):
    if b==1:
        return a%max

    res = divide(a,b//2)

    temp = (res*res)%max
    return (temp*a)%max if b%2 else temp

global max
max = 1000000007
t = int(input())
for i in range(t):
    r,g,b,k = list(map(int,input().split()))
    exp = k

    res = (divide(b,k)*divide(b+1,max-(k+1)))%max
    res = (1-res+max)%max
    res = (res*r)%max
    exp = (exp+res)%max

    res = (g*divide(b,max-2))%max
    res = (res*k)%max
    exp = (exp + res)%max

    print(exp)