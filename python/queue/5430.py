import sys
from collections import deque

t = int(sys.stdin.readline())

while t:
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    strs = sys.stdin.readline().lstrip('[').rstrip(']\n')
    if strs=="":
        l = list()
    else:
        l = list(map(int,strs.split(',')))
    q = deque([])
    flage = False
    for item in l:
        q.append(item)

    flag = True
    for cmd in p:
        if cmd=='R':
            flag = not(flag)
        else:
            if not(q):
                flage= True
                print("error")
                break
            else:
                if flag:
                    q.popleft()
                else:
                    q.pop()

    if flage:
        t-=1
        continue
    
    ans = '['
    if flag:
        while q:
            ans+= str(q.popleft()) + ','
    else:
        while q:
            ans+= str(q.pop()) + ','

    ans = ans.rstrip(',') + ']'
    print(ans)

    t-=1