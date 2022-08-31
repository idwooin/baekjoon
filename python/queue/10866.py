from collections import deque
import sys
d = deque([])
n= int(sys.stdin.readline())

while n:
    cmd = list(sys.stdin.readline().strip().split())
    if cmd[0][:4] == "push":
        if cmd[0] == "push_front":
            d.append(cmd[1])
        else:
            d.appendleft(cmd[1])
    elif cmd[0][:3] == "pop":
        if not(d):
            print(-1)
        else:
            if cmd[0] == "pop_front":
                print(d.pop())
            else:
                print(d.popleft())
    else:
        if cmd[0] == "size":
            print(len(d))
        elif cmd[0] == "empty":
            flag = 1 if not(d) else 0
            print(flag)
        else:
            if not(d):
                print(-1)
            else:
                if cmd[0] == "front":
                    temp = d.pop()
                    print(temp)
                    d.append(temp)
                else:
                    temp = d.popleft()
                    print(temp)
                    d.appendleft(temp)

    n-=1
