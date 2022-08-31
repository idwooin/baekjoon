import math

n,k = list(map(int,input().split()))
prefer = list(map(int,input().split()))
min_n = math.inf

def avg(arr,n):
    return sum(arr)/n

def var(arr,avr,n):
    v = sum([pow(arr[i]-avr,2) for i in range(n)])/n
    return v, math.sqrt(v)

for j in range(k,n+1):
    for i in range(n-j+1):
        a = avg(prefer[i:i+j],j)
        v,d = var(prefer[i:i+j],a,j)
        min_n = min(min_n,d)

print(min_n)