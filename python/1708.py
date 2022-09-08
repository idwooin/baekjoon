import sys
from functools import cmp_to_key
from collections import deque

input = sys.stdin.readline

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))

points.sort(key=lambda x:(x[1],x[0]))

def ccw(p1,p2):
    if p2[1]*p1[0] < p2[0]*p1[1]:
        return -1
    elif p2[1]*p1[0] == p2[0]*p1[1]:
        return 0
    else:
        return 1

ori = points[0]

def compare(x,y):
    global ori

    p1 = [(x[0]-ori[0]),(x[1]-ori[1])]
    p2 = [(y[0]-ori[0]),(y[1]-ori[1])]
    flag = ccw(p1,p2)
    print(x,y,flag)

    if ccw(ori,x) == 0:
        if (x[0]+x[1]) > (y[0]+y[1]):
            return 1
        else:
            return -1
    else:
        if flag == -1:
            return 1
        else:
            return -1

points_ori = sorted(points[1:],key=cmp_to_key(compare))
print(points_ori)
answer = 2
stack = deque([ori])
stack.append(points_ori[1])

for p in points_ori[1:]:
    p1 = stack[-2]
    p2 = stack[-1]
    p3 = p
    cvec = [(p3[0]-p1[0]),(p3[1]-p1[1])]
    bvec = [(p2[0]-p1[0]),(p2[1]-p1[1])]
    print(p,stack)
    if ccw(bvec,cvec) > 0:
        stack.append(p3)
        print(p3)
        answer+=1
    elif ccw(bvec,cvec) == 0:
        stack.pop()
        stack.append(p3)
    else:
        stack.pop()
        stack.append(p3)
        continue

print(stack)
print(answer)