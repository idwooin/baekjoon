import math

line1 = list(map(int,input().split()))
x1,y1 = line1[0:2]; x2,y2 = line1[2:]
line2 = list(map(int,input().split()))
x3,y3 = line2[0:2]; x4,y4 = line2[2:]

def ccw(x1,y1,x2,y2,x3,y3):
    y = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    if y>0:
        return 1
    elif y<0:
        return -1
    else:
        return 0

ans = 0

if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2) == 0:
    if min(x1,x2) <= max(x3,x4) and max(x1,x2) >= min(x3,x4) and min(y1,y2) <= max(y3,y4) and min(y3,y4) <= max(y1,y2):
        ans = 1
elif ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2) <= 0:
    ans = 1
print(ans)

