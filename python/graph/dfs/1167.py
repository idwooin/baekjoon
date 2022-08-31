import sys

edges = []
v = int(sys.stdin.readline())
for _ in range(v):
    edges.append(list(map(int,sys.stdin.readline().strip().split())))
dic = {}
visited = [False for _ in range(v+1)]
ans = 0
max_node = 1

def dfs(vertex,total):
    global ans,max_node

    for line in dic[vertex]:
        child,distance = line
        if visited[child]:
            continue
        visited[child] = True
        dfs(child,total+distance)
        if ans < total + distance:
            ans = total+distance
            max_node = child
        visited[child] = False

for e in edges:
    vertex = e[0]
    for idx in range(1,len(e)-2,2):
        if dic.get(vertex) == None:
            dic[vertex] = [[e[idx],e[idx+1]]]
        else:
            dic[vertex].append([e[idx],e[idx+1]])

visited[1] = True
dfs(1,0)
visited[1] = False
visited[max_node] = True
dfs(max_node,0)

print(ans)
