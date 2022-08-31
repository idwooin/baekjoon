def divide(a,b,c):
    if b==1:
        return a%c

    res = divide(a,b//2,c)

    temp = (res*res)%c
    return (temp*a)%c if b%2 else temp

a,b,c= list(map(int,input().split()))

print(divide(a,b,c))
