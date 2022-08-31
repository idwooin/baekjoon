from collections import deque
# def init(tree,node,rec,start,end):
#     tree[node] = sum(rec[start:end])

#     mid = (start+end)//2

#     init(tree,node*2,rec,start,mid)
#     init(tree,node*2+1,rec,mid+1,end)

# def seg_tree(n,start,end,rec):
#     rec.index
#     return max(curr,seg_tree(n,rec),seg_tree(n,rec))

q = deque([])
while True:
    ans = 0
    rec = list(map(int,input().split()))
    n = rec[0]; del rec[0]

    if n == 0:
        exit(0)

    for i in range(n):
        idx = i
        if not(q) or q[-1][1] < rec[i]:
            q.append([idx,rec[i]])
        else:
            while q and q[-1][1] >= rec[i]:
                idx,height= q.pop()
                ans = max(ans,(i-idx)*height)
            q.append([idx,rec[i]])

    while q:
        idx,height = q.pop()
        ans = max(ans,(n-idx)*height)

    
    print(ans)