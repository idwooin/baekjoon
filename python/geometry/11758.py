p1 = list(map(float,input().split()))
p2 = list(map(float,input().split()))
p3 = list(map(float,input().split()))

v1 = (p2[0]-p1[0],p2[1]-p1[1])
v2 = (p3[0]-p2[0],p3[1]-p2[1])

v3 = (v2[1]*v1[0]-v2[0]*v1[1])

if v3>0:
    print(1)
elif v3<0:
    print(-1)
else:
    print(0)