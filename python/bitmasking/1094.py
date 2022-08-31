n = int(input())

# def check(n):
#     cnt = 0
#     while n>0:
#         if n%2 == 1:
#             cnt+=1
#         n//=2

#     return cnt

def check(n):
    mask = 1
    cnt = 0

    while n>=mask:
        if n&mask !=0:
            cnt+=1
        mask<<=1
    return cnt

ans = check(n)
print(ans)