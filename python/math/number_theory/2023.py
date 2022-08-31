from collections import deque
import heapq

n = int(input())

strq = deque(['2','3','5','7'])
# prime_list = [True for i in range(3,10**8+1,2)]
# prime_list[0]=prime_list[1] = False
# ans_list=[]

# def init():
#     for i in range(3,10**4+1,2):
#         if prime_list[(i-3)//2] == False and i%5==0:
#             continue
#         for j in range(3*i,10**8+1,2*i):
#             prime_list[(j-3)//2] = False

# def prime(n):
#     return True if prime_list[(n-3)//2] else False

# init()
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

ans_list = []
prime_list = ['1','3','7','9']
if n==1:
    print(2)
    print(3)
    print(5)
    print(7)
else:
    while strq:
        strs=strq.pop()
        for p in prime_list:
            temp= strs + p
            if prime(int(temp)):
                if len(temp)!=n:
                    strq.append(temp)
                else:
                    heapq.heappush(ans_list,temp)

    while ans_list:
        print(heapq.heappop(ans_list))