n,m = list(map(int,input().split()))
parent = []
for i in range(n+1):
    parent.append([i,0])

def find(a,parent):
    # while parent[a][0] != a:
    #     a = parent[a][0]
    # return a
    if parent[a][0] == a:
        return a
    
    return find(parent[a][0],parent)

def union(a,b,parent):
    parent_a = find(a,parent)
    parent_b = find(b,parent)

    if parent_a == parent_b:
        return

    if parent[parent_a][1] < parent[parent_b][1]:
        parent[parent_a] = parent[parent_b]
    elif parent[parent_a][1] > parent[parent_b][1]:
        parent[parent_b] = parent[parent_a]
    else:
        parent[parent_b][1] +=1
        parent[parent_a] = parent[parent_b]

for i in range(m):
    a,b,c = list(map(int,input().split()))

    if a == 0:
        union(b,c,parent)
    else:
        parent_b = find(b,parent)
        parent_c = find(c,parent)

        print("YES") if parent_b==parent_c else print("NO")
