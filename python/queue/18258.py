import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])

while n:
    cmd = list(sys.stdin.readline().strip().split())

    if len(cmd) == 2:
        q.append(cmd[1])
    else:
        if cmd[0] == "size" or cmd[0]=="empty":
            if cmd[0] == "size":
                print(len(q))
            else:
                flag = 1 if not(q) else 0
                print(flag)
        else:
            if not(q):
                print(-1)
            else:
                if cmd[0] == "pop":
                    print(q.popleft())
                elif cmd[0] == "front":
                    print(q[0])
                else:
                    print(q[-1])
    n-=1