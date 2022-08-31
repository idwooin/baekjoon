import sys
from collections import deque

n,q = list(map(int,sys.stdin.readline().strip().split()))

parent = [0 for _ in range(n+1)]
parent[1] = 1

def find(parent,node):
    cnt = 0
    while parent[node] != node:
        node = parent[node]
        cnt+=1
    
    return node

offline_query = deque([])
exist = []

for i in range(2,n+1):
    parent[i] = int(sys.stdin.readline())
for i in range(q+n-1):
    query = list(sys.stdin.readline().strip().split())

    if query[0] == '0':
        # b와 부모 지움
        b = int(query[1])
        offline_query.append([0,parent[b],b])
    else:
        # c와 d 경로 존재하냐
        c = int(query[1])
        d = int(query[2])
        offline_query.append([1,c,d])

parent = [i for i in range(n+1)]
parent[1] = 1
ans = deque([])
# stack 사용
while offline_query:
    a,b,c=offline_query.pop()

    if a == 0:
        parent[c] = b
    else:
        rootb= find(parent,b)
        rootc= find(parent,c)
        ans.append("YES") if rootb == rootc else ans.append("NO")

while ans:
    print(ans.pop())