str_cond = input()
str_parse = []
last_parse = 0
flag = False

def parent(n):
    pa = [i for i in range(n+1)]

def find(num,cnt):
    if num == parent[num]:
        return num, cnt
    return find(parent[num],cnt+1)

def merge(a,b):
    a,cnt0 = find(a,0)
    b,cnt1 = find(b,0)

    if a==b:
        return
    
    if cnt0 > cnt1:
        a,b = b,a
    parent[a] = b

    if cnt0 == cnt1

for i in range(len(str_cond)-1):
    if not(str_cond[i]=='&'):
        continue

    if str_cond[i+1] == '&':
        flag = True
        str_parse.append(str_cond[last_parse:i])
        last_parse = i+2

parent(len(str_parse)*2)

if flag:
    print(str_cond)
else:
    dict = {}
    for i in range(len(str_parse)):
        first=second=''
        for j in range(len(str_parse[i])):
            if not(str_parse[i][j]=='=' or str_parse[i][j]=='!'):
                continue
            first = str_parse[i][0:j]
            second = str_parse[i][j+2:]
            break

        print(first,second)
        p_key = first if len(first) <= len(second) else second
        s = set(first,second)

        