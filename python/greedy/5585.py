pay = int(input())
pay = 1000-pay
zan = [500,100,50,10,5,1]
curr = 0
ans = 0

while pay>0:
    if pay < zan[curr]:
        curr+=1
        continue
    
    ans+= pay//zan[curr]
    pay = pay%zan[curr]

print(ans)
