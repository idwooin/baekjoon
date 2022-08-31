from queue import PriorityQueue

n = int(input())
w = list(map(int,input().split()))
w.sort()


num=1
for i in w:
    if num<i:
        break
    num+=i

print(num)