import math

def isPrime(a):
    for i in range(2,int(math.sqrt(a))+2):
        if a%i == 0:
            return False
    return True

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


def goldbach(n):
    a=b=-1
    for i in range(3,n-2):
        if isPrime(i) and isPrime(n-i):
            return i,n-i

    return a,b

while True:
    n = int(input())
    if n==0:
        break
    
    a,b = goldbach(n)
    if a==-1 and b==-1:
        print("Goldbach's conjecture is wrong.")
    else:
        print(n,'=',a,'+',b)