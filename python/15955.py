n,q = list(map(int,input().split()))
x=[]
y=[]
query=[]

for i in range(n):
    temp_x,temp_y = list(map(int,input().split()))
    x.append(temp_x)
    y.append(temp_y)

for i in range(q):
    query.append(list(map(int,input().split())))
ans = [False for i in range(q)] 