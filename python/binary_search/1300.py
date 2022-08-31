n = int(input())
k = int(input())
start = 1
end = n*n
while True:
    if start==end:
        print(start)
        exit(0)
    mid = (start + end)//2
    ans = 0
    for i in range(1,n+1):
        ans+=min(mid//i,n)

    if ans >= k:
        end = mid
    else:
        start = mid+1