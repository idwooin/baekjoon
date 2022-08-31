import sys
m = int(sys.stdin.readline())
s = 0
for i in range(m):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 1:
        if cmd =="all":
            s = (1<<20)-1
        else:
            s = 0
    else:
        c,n = cmd[0],int(cmd[1])
        if c=="add":
            s = s|1<<n-1
        elif c == "remove":
            s = s&~(1<<n-1)
        elif c == "check":
            print(1 if s&(1<<n-1) else 0)
        elif c == "toggle": 
            s=s^(1<<n-1)

#s = set()
# for i in range(m):
#     #cmd,num=list(map(str,input().split()))
#     cmd = sys.stdin.readline().strip().split()
#     if len(cmd) == 1:
#         if cmd[0] =="all":
#             s = set([str(j) for j in range(1,21)])
#         else:
#             s = set()
#     else:
#         if cmd[0]=="add":
#             s.add(cmd[1])
#         elif cmd[0] == "remove":
#             s.discard(cmd[1])
#         elif cmd[0] == "check":
#             print(1 if cmd[1] in s else 0)
#         elif cmd[0] == "toggle":
#             if cmd[1] in s:
#                 s.discard(cmd[1])
#             else:
#                 s.add(cmd[1])
