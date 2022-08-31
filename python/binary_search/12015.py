import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().strip().split()))

def binary_search(l,start,end,item):
    if l[end] <item:
        l.append(item)
        return

    while start<=end:
        if start==end:
            l[start] = item
            return

        mid = (start+end)//2

        if l[mid] < item:
            start = mid+1
        else:
            end = mid
l=[0]
for num in a:
    binary_search(l,0,len(l)-1,num)

print(len(l)-1)
