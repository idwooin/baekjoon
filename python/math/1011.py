T = int(input())
for i in range(T):
    ans = 0
    x,y = list(map(int,input().split()))
    diff = y-x
    pluses = 0
    i=1

    while True:
        diff-=i
        ans+=1
        if diff<=0:
            break
        diff-=i
        ans+=1
        if diff<=0:
            break

        i+=1
    
    print(ans)