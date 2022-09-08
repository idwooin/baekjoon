# import sys
# import heapq
# input = sys.stdin.readline

# diff = dict()
# alp = dict()
# z_match = dict()
# for i in range(36):
#     alp[i] = 0
#     diff[i] = 0
#     z_match[i] = i

# def convert(s):
#     if '0'<=s<='9':
#         ch = ord(s)-48     
#     else:
#         ch = ord(s)-55

#     return ch

# def r_convert(r):
#     if 0<=r<=9:
#         ch = chr(r+48)     
#     else:
#         ch = chr(r+55)

#     return ch

# n = int(input())
# num = [[] for _ in range(n)]
# numbers=[]
# for i in range(n):
#     numbers.append(str.strip(input()))
#     m = len(numbers[i])
#     for j in range(m):
#         tn = convert(numbers[i][j])
#         num[i].append([tn,m-j-1])
# k = int(input())

# for i in range(n):
#     visited = [False for _ in range(36)]
#     for s,d in num[i]:
#         diff[s]-=(35-s)*(36**d)
#         if not(visited[s]):
#             visited[s] =True
#             alp[s]+=1

# candidate = []
# for key,item in alp.items():
#     if item==n:
#         heapq.heappush(candidate,(diff[key],key))

# while candidate and k>0:
#     _,key=heapq.heappop(candidate)
#     z_match[key] = 35
#     k-=1

# def sum():
#     global n,num
#     answer = 0

#     for i in range(n):
#         print(num[i])
#         for j,idx in num[i]:
#             answer+=(z_match[j]*(36**idx))
    
#     final = []
#     while answer >= 36:
#         final.append(r_convert(answer%36))
#         answer = answer//36
#     final.append(r_convert(answer))
#     return ''.join(final[::-1])

# print(sum())

def f(n):
    q = n//36
    r = n%36
    return f(q) + (chr(r+48) if 0<=r<=9 else chr(r+55)) if q else chr(r+48) if 0<=r<=9 else chr(r+55)
n = int(input())
c=[0]*36
for i in range(n):
    n = input()
    l = len(n)
    for j in range(l):
        c[int(n[j],36)]+=36**(l-j-1)
k = int(input())
A = [[c[i]*(35-i),i] for i in range(36)]
A.sort()
print(f(sum(map(lambda i: c[A[i][1]] * (A[i][1] if i<36-k else 35), range(36)))))