from collections import deque

n = int(input())
colors = []

for i in range(n):
    temp = input()
    colors.append([s for s in temp])

def bfs(start_queue,colors,visited,ans):

    queue = deque([])

    while start_queue:
        sx,sy=start_queue.popleft()
        #print(sx,sy)
        if visited[sx][sy]:
            continue
        ans+=1
        curr = colors[sx][sy]
        queue.append([sx,sy])

        while queue:
            x,y = queue.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True

            if x-1>=0 and not(visited[x-1][y]):
                if colors[x-1][y]== curr: 
                    queue.append([x-1,y])
                else:
                    start_queue.append([x-1,y])

            if y-1>=0 and not(visited[x][y-1]):
                if colors[x][y-1]== curr: 
                    queue.append([x,y-1])
                else:
                    start_queue.append([x,y-1])

            if x+1<n and not(visited[x+1][y]):
                if colors[x+1][y]== curr: 
                    queue.append([x+1,y])
                else:
                    start_queue.append([x+1,y])

            if y+1<n and not(visited[x][y+1]):
                if colors[x][y+1]== curr: 
                    queue.append([x,y+1])
                else:
                    start_queue.append([x,y+1])

    return ans

visited = [[False for i in range(n)] for i in range(n)]
normal_ans = abnormal_ans = 0
start_queue = deque([[0,0]])
normal_ans = bfs(start_queue,colors,visited,normal_ans)

visited = [[False for i in range(n)] for i in range(n)]
start_queue = deque([[0,0]])

for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'
abnormal_ans = bfs(start_queue,colors,visited,abnormal_ans)

print(normal_ans,abnormal_ans)