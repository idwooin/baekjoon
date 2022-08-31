import sys
import heapq

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
ans = []
prime_list = [True for _ in range(2001)]
prime_list[0]=prime_list[1]=False

for i in range(2,int(2000**0.5)+1):
    if prime_list[i] == False:
        continue
    for j in range(2*i,2001,i):
        prime_list[j] = False

# def prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# def primes(arr,n):
#     if n == 0:
#         return True

#     a = arr[0]
#     arr = arr[1:]

#     for i in range(n-1):
#         if prime_list[a+arr[i]]:
#             if primes(arr[:i]+arr[i+1:],n-2):
#                 return True

def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if x + y in prime_list:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

a = num[0]
num = num[1:]

for i in range(n-1):
    matched = {}
    if a+num[i] in prime_list:
        if n==2:
            heapq.heappush(ans,num[i])
            break

        Y = num[:i]+num[i+1:]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)

    if n!=2 and len(matched) == n-2: heapq.heappush(ans,num[i])

if len(ans)>0:
    ans = sorted(ans)
    print(*ans)
else:
    print(-1)