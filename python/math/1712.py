a,b,c = map(int,input().split())
profit = -b+c
if profit == 0:
    print(-1)
else:
    ans =(abs(a)+1)//profit
    if ans < 0:
        print(-1)
    else:
        if (abs(a)+1)%profit:
            print(ans+1)
        else:
            print(ans)