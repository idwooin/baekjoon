def list_initialize(n):
    arr=[]
    for i in range(n):
        arr.append(0)
    
    return arr

def army(n,w,in_list,out_list,dp_outer,dp_inner,dp_vert):
    for i in range(1,n):
        outer = 1 if (out_list[i-1]+out_list[i])<=w else 2
        inner = 1 if (in_list[i-1]+in_list[i])<=w else 2
        vert = 1 if (in_list[i]+out_list[i])<=w else 2
        dp_outer[i] = min(dp_inner[i-1] + outer, dp_vert[i-1]+1)
        dp_inner[i] = min(dp_outer[i-1] + inner, dp_vert[i-1]+1)
        dp_vert[i] = min(dp_inner[i] + 1,dp_outer[i]+1,dp_vert[i-1]+vert,dp_vert[i-2]+outer+inner)

    return


T = int(input())
ans = []
max_num = 10001

for i in range(T):
    N,W = map(int,input().split())
    in_list = list(map(int,input().split()))
    out_list = list(map(int,input().split()))
    answer = 0
    if N==1:
        ans.append(1 if in_list[0]+out_list[0]<=W else 2)
    else:
        [dp_outer,dp_inner,dp_vert] = map(list_initialize,[N,N,N])
        dp_outer[0] = dp_inner[0] = 1
        dp_vert[0] = 1 if in_list[0]+out_list[0]<=W else 2
        army(N,W,in_list,out_list,dp_outer,dp_inner,dp_vert)
        answer = dp_vert[N-1]

        if in_list[N-1] + in_list[0] <=W:
            dp_vert[N-1] = max_num #적용되면 안됨
            dp_inner[0] = 1
            dp_outer[0] = max_num #적용되면 안됨
            dp_vert[0] = 2
            army(N,W,in_list,out_list,dp_outer,dp_inner,dp_vert)
            answer = min(answer,dp_outer[N-1])
        
        if out_list[N-1] + out_list[0] <=W:
            dp_vert[N-1] = max_num #적용되면 안됨
            dp_outer[0] = 1
            dp_inner[0] = max_num #적용되면 안됨
            dp_vert[0] = 2
            army(N,W,in_list,out_list,dp_outer,dp_inner,dp_vert)
            answer = min(answer,dp_inner[N-1])
        
        if (in_list[N-1] + in_list[0] <=W) and (out_list[N-1] + out_list[0] <=W):
            dp_vert[N-1] = max_num #적용되면 안됨
            dp_outer[0] = max_num
            dp_inner[0] = max_num #적용되면 안됨
            dp_vert[0] = 2
            army(N,W,in_list,out_list,dp_outer,dp_inner,dp_vert)
            answer = min(answer,dp_vert[N-2])

        ans.append(answer)

for i in range(T):
    print(ans[i])