import heapq

n = int(input())
a = []
for i in range(n):
    heapq.heappush(a,int(input()))

avg = 0
cent = 0
cnt = 0
maxitem = [4001]
maxcnt = 0
lcnt = 0
litem = 4001
diff =0
while a:
    temp=heapq.heappop(a)
    avg+=temp
    cnt+=1
    if cnt == 1:
        diff -=temp
    if cnt == n:
        diff +=temp
        
    if cnt == (n//2)+1:
        cent = temp

    if temp!=litem:
        if maxcnt < lcnt:
            maxcnt = lcnt
            maxitem = [litem]
        elif maxcnt == lcnt:
            if litem != 4001:
                heapq.heappush(maxitem,litem)
        litem = temp
        lcnt = 1
    else:
        lcnt+=1

if maxcnt < lcnt:
    maxcnt = lcnt
    maxitem = [litem]
elif maxcnt == lcnt:
    heapq.heappush(maxitem,litem)

print(round(avg/n))
print(cent)
m = heapq.heappop(maxitem)
print(m) if len(maxitem) == 0 else print(heapq.heappop(maxitem))
print(diff)
