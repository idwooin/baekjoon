import math
import sys

n = int(sys.stdin.readline())
points = []
for i in range(n):
    points.append(list(map(float,sys.stdin.readline().split())))

points.sort()

def dist(a,b):
    return math.sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2) - a[2] - b[2]

def find_min(start,end,points):
    min_dist = math.inf

    for i in range(start,end):
        for j in range(i+1,end+1):
            temp = dist(points[i],points[j])
            if min_dist > temp:
                min_dist = temp

    return min_dist

def find_miny(start,end,points):
    min_dist = math.inf

    if len(points) == 1:
        return min_dist
    
    for i in range(start,end):
        for j in range(i+1,end+1):
            if (points[i][1]-points[j][1])**2 < min_dist:
                min_dist = min(min_dist,dist(points[i],points[j]))
            else:
                break

    return min_dist

def check_bound(mindist,mid,start,end,points):
    cpoints = []
    for i in range(start,end+1):
        if math.sqrt((points[mid][0] - points[i][0])**2)-points[mid][2]-points[i][2] <= mindist:
            cpoints.append(points[i])
    
    return cpoints

def divide_conquer(start,end):
    global points

    if end-start+1 <= 3:
        return find_min(start,end,points)
    
    mid = (start+end)//2
    lmin = divide_conquer(start,mid)
    rmin = divide_conquer(mid+1,end)

    mindist = min(lmin,rmin)
    cpoints = check_bound(mindist,mid,start,end,points)
    cpoints.sort(key=lambda x:x[1])

    cend = len(cpoints)-1
    cmid = cend//2
    cpoints = check_bound(mindist,cmid,0,cend,cpoints)

    return min(lmin,rmin,find_miny(0,len(cpoints)-1,cpoints))

print(divide_conquer(0,n-1))