n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(str,input().split())))

ans = [0,0,0]

def div(n,paper,a,b):
    global ans

    comp = paper[a][b]

    for i in range(n):
        for j in range(n):
            if comp!= paper[a+i][b+j]:
                comp = '-2'
                break
        if comp == '-2':
            break

    if comp == '-2':
        n = n//3
        div(n,paper,a,b)
        div(n,paper,a,b+n)
        div(n,paper,a,b+2*n)
        div(n,paper,a+n,b)
        div(n,paper,a+n,b+n)
        div(n,paper,a+n,b+2*n)
        div(n,paper,a+2*n,b)
        div(n,paper,a+2*n,b+n)
        div(n,paper,a+2*n,b+2*n)
    else:
        ans[int(comp)+1]+=1

div(n,paper,0,0)
for answer in ans:
    print(answer)