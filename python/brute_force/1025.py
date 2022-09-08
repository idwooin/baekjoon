import math

n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(input())

answer = -1

def check_sqrt(num):
    s = math.sqrt(num)
    diff = s - int(s)
    if diff == 0:
        return True

for r in range(n):
    for c in range(m):
        for rd in range(-n,n):
            for cd in range(-m,m):
                if rd==0 and cd==0:
                    continue
                
                i = 0
                value = ''
                tr = r
                tc = c
                while 0<=tr<n and 0<=tc<m:
                    value+=mat[tr][tc]
                    i+=1
                    tr=r+(i*rd)
                    tc=c+(i*cd)
                
                    v = int(''.join(value))
                    if check_sqrt(v):
                        answer = max(answer,v)

print(answer)