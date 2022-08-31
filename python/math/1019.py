# import sys

# n = sys.stdin.readline().strip()
# num = [0 for _ in range(10)]

# while n>0:
#     temp = int(n)
#     while temp%10 != 9:
#         temp+=1
#         s = str(temp)
#         for i in s:
#             num[int(i)]-=1
    
#     n = temp
#     l = len(str(n))-1

# for s in n:
#     m = int(s)
#     rest = int(n)%(10**l)
#     num[m]+=rest+1
#     for i in range(10):
#             num[i]+=int(l*(10**(l-1)))
#     m-=1
#     while m>0:
#         num[m]+=int(10**l)
#         for i in range(10):
#             num[i]+=int(l*(10**(l-1)))
#         m-=1
#     l-=1

# print(num)

import sys
 
N = int(sys.stdin.readline().replace("\n", ""))
 
counts = [0 for _ in range(10)]
 
weight = 1
for step in range(len(str(N))):
    replaced = int(str(N // 10) + "9")
    remaining = replaced - N
    for i in range(len(counts)): counts[i] += (N // 10 + 1) * weight
    for i in range(10-remaining, 10): counts[i] -= weight
    for number in list(str(N)[:-1]):
        number = int(number)
        counts[number] -= remaining * weight
 
    counts[0] -= weight
 
    N //= 10
    weight *= 10
 
print(' '.join(map(str, counts)))

