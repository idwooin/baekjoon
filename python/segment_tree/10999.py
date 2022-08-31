n,m,k = list(map(int,input().split()))
arr=[]
ans = []
tree = [[0,0] for i in range(2*n+1)]

def init(start,end,tree,arr,node):
    if start==end:
        tree[node][0] = arr[start]
        return tree[node][0]
    
    mid = (start+end)//2
    tree[node][0] = init(start,mid,tree,arr,node*2) + init(mid+1,end,tree,arr,node*2+1)

    return tree[node][0]

def find(start,end,left,right,tree,node):
    if tree[node][1]!=0:
        tree[node][0] += (end-start+1)*tree[node][1]
        if start!=end:
            tree[node*2][1] += tree[node][1]
            tree[node*2+1][1] += tree[node][1]
        tree[node][1] = 0

    if left > end or right < start:
        return 0
    
    if left<=start and end<=right:
        return tree[node][0]
    
    mid = (start+end)//2
    return find(start,mid,left,right,tree,node*2) + find(mid+1,end,left,right,tree,node*2+1)

def update(start,end,tree,node,left,right,val):
    if tree[node][1]!=0:
        tree[node][0] += (end-start+1)*tree[node][1]
        if start!=end:
            tree[node*2][1] += tree[node][1]
            tree[node*2+1][1] += tree[node][1]
        tree[node][1] = 0

    if right < start or end < left:
        return

    if left<=start and end<=right:
        tree[node][0]+=(end-start+1)*val
        if start!=end:
            tree[node*2][1] += val
            tree[node*2+1][1] += val
        return

    mid = (start+end)//2
    update(start,mid,tree,node*2,left,right,val)
    update(mid+1,end,tree,node*2+1,left,right,val)

    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
    return

for i in range(n):
    arr.append(int(input()))

init(0,n-1,tree,arr,1)

for i in range(m+k):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        update(0,n-1,tree,1,temp[1]-1,temp[2]-1,temp[3])
    else:
        ans.append(find(0,n-1,temp[1]-1,temp[2]-1,tree,1))

for num in ans:
    print(num)