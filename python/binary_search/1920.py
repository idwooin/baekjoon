import sys
n = int(sys.stdin.readline())
nl = list(map(int,sys.stdin.readline().strip().split()))
nl.sort()
m = int(sys.stdin.readline())
ml = list(map(int,sys.stdin.readline().strip().split()))

def binary_search(l,start,end,item):
    if start==end:
        return 1 if l[start]==item else 0
    
    mid = (start+end)//2
    if l[mid] >= item:
        return binary_search(l,start,mid,item)
    else:
        return binary_search(l,mid+1,end,item)

for item in ml:
    print(binary_search(nl,0,n-1,item))
    m-=1