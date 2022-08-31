import math
n = int(input())

ph = list(map(int,input().split()))

neg_p = 0
pos_p = n-1
min_sum = 2000000000
ans = []
while neg_p!=pos_p:
    sum = ph[neg_p]+ph[pos_p]
    if sum == 0:
        ans = [ph[neg_p],ph[pos_p]]
        break
    if abs(sum) < min_sum:
        min_sum = abs(sum)
        ans = [ph[neg_p],ph[pos_p]]

    if sum > 0:
        pos_p-=1
    elif sum < 0:
        neg_p+=1

print(*ans)
