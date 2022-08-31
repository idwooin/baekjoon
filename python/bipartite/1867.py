import sys

n,k = map(int,sys.stdin.readline().strip().split())
left = [[] for _ in range(n+1)]
right = [0 for _ in range(n+1)]

def bipartite(a,visited):
    global left,right

    for item in left[a]:
        if visited[item] == 1:
            continue
        visited[item] = 1

        if right[item] == 0 or bipartite(right[item],visited):
            right[item] = a
            return True

    return False

for i in range(k):
    a,b = map(int,sys.stdin.readline().strip().split())
    left[a].append(b)

ans = 0
for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    bipartite(i,visited)

for i in range(1,n+1):
    if right[i] !=0:
        ans+=1
print(ans)
