import math
n = int(input())

ph = list(map(int,input().split()))
ph.sort()

min_sum = 3000000000
ans = []
for mid_p in range(n):
    neg_p = 0
    pos_p = n-1
    while neg_p!=pos_p:
        if neg_p == mid_p:
            neg_p+=1
            continue
        if pos_p == mid_p:
            pos_p-=1
            continue

        sum = ph[neg_p]+ph[pos_p]+ph[mid_p]

        if sum == 0:
            ans = [ph[neg_p],ph[mid_p],ph[pos_p]]
            break
        if abs(sum) < min_sum:
            min_sum = abs(sum)
            ans = [ph[neg_p],ph[mid_p],ph[pos_p]]

        if sum > 0:
            pos_p-=1
        elif sum < 0:
            neg_p+=1
ans.sort()
print(*ans)
