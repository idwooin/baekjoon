# 15654.py

# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# for i in range(1,n+1):
#     v = 1<<i
#     heapq.heappush(q,[str(i),v])

# while q:
#     num,v=heapq.heappop(q)
#     if len(num) == m:
#         temp = []
#         for a in num: temp.append(nat[int(a)-1])
#         print(*temp, sep=' ')
#         continue

#     for i in range(1,n+1):
#         temp = 1<<i
#         b = (v&temp)>>i
#         if b:
#             continue
#         v = v|temp
#         heapq.heappush(q,[num+str(i),v])
#         v = v^temp

#15655.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# for i in range(1,n+1):
#     v = 1<<i
#     max_num = i
#     heapq.heappush(q,[str(i),max_num,v])

# while q:
#     num,max_num,v=heapq.heappop(q)
#     if len(num) == m:
#         temp = []
#         for a in num: temp.append(nat[int(a)-1])
#         print(*temp, sep=' ')
#         continue

#     for i in range(max_num+1,n+1):
#         temp = 1<<i
#         b = (v&temp)>>i
#         if b:
#             continue
#         v = v|temp
#         heapq.heappush(q,[num+str(i),i,v])
#         v = v^temp

#15656.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# for i in range(1,n+1):
#     v = 1<<i
#     max_num = i
#     heapq.heappush(q,str(i))

# while q:
#     num = heapq.heappop(q)
#     if len(num) == m:
#         temp = []
#         for a in num: temp.append(nat[int(a)-1])
#         print(*temp, sep=' ')
#         continue

#     for i in range(1,n+1):
#         heapq.heappush(q,num+str(i))

#15657.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# for i in range(1,n+1):
#     max_num = i
#     heapq.heappush(q,[str(i),max_num])

# while q:
#     num, max_num = heapq.heappop(q)
#     if len(num) == m:
#         temp = []
#         for a in num: temp.append(nat[int(a)-1])
#         print(*temp, sep=' ')
#         continue

#     for i in range(max_num,n+1):
#         heapq.heappush(q,[num+str(i),i])

#15663.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# dict = {}

# for i in range(0,len(nat)):
#     v = 1<<i
#     heapq.heappush(q,[str(i),v])

# while q:
#     num, v = heapq.heappop(q)
#     if len(num) == m:
#         result = ""
#         #print(num)
#         for a in num: result+=str(nat[int(a)])+' '
#         if dict.get(result.rstrip())==None:
#             dict[result.rstrip()] = 1
#             print(result)
#         continue

#     for i in range(0,len(nat)):
#         temp = 1<<i
#         b = (v&temp)>>i
#         if b:
#             continue
#         v = v|temp
#         heapq.heappush(q,[num+str(i),v])
#         v = v^temp

#15664.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# dict = {}

# for i in range(0,len(nat)):
#     v = 1<<i
#     heapq.heappush(q,[str(i),v])

# while q:
#     num, v = heapq.heappop(q)
#     if len(num) == m:
#         result = ""
#         flag = True
#         for i in range(len(num)-1):
#             if int(num[i]) > int(num[i+1]):
#                 flag = False
#                 break

#         if not(flag):
#             continue

#         for a in num: result+=str(nat[int(a)])+' '
#         if dict.get(result.rstrip())==None:
#             dict[result.rstrip()] = 1
#             print(result)
#         continue

#     for i in range(0,len(nat)):
#         temp = 1<<i
#         b = (v&temp)>>i
#         if b:
#             continue
#         v = v|temp
#         heapq.heappush(q,[num+str(i),v])
#         v = v^temp

#15665.py
# import sys
# import heapq

# q = []
# nat = []
# n,m = map(int,sys.stdin.readline().strip().split())
# nat = list(map(int,sys.stdin.readline().strip().split()))
# nat.sort()

# dict = {}

# for i in range(0,len(nat)):
#     heapq.heappush(q,str(i))

# while q:
#     num = heapq.heappop(q)
#     if len(num) == m:
#         result = ""
#         for a in num: result+=str(nat[int(a)])+' '
#         if dict.get(result.rstrip())==None:
#             dict[result.rstrip()] = 1
#             print(result)
#         continue

#     for i in range(0,len(nat)):
#         heapq.heappush(q,num+str(i))

#15666.py
import sys
import heapq

q = []
nat = []
n,m = map(int,sys.stdin.readline().strip().split())
nat = list(map(int,sys.stdin.readline().strip().split()))
nat.sort()

dict = {}

for i in range(0,len(nat)):
    heapq.heappush(q,str(i))

while q:
    num = heapq.heappop(q)
    if len(num) == m:

        flag = True
        for i in range(len(num)-1):
            if int(num[i]) > int(num[i+1]):
                flag = False
                break

        if not(flag):
            continue

        result = ""
        for a in num: result+=str(nat[int(a)])+' '
        if dict.get(result.rstrip())==None:
            dict[result.rstrip()] = 1
            print(result)
        continue

    for i in range(0,len(nat)):
        heapq.heappush(q,num+str(i))

