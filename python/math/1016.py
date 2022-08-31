import math

min,max = map(int,input().split())
list=[]

for i in range(max-min+1):
    list.append(False)

max_sqrt = math.floor(math.sqrt(max))
cnt = 0

for i in range(2,max_sqrt+1):
    pow = i*i
    j=math.ceil(min/pow)*pow
    while j<min:
        j+=pow

    while j<=max:
        list[j-min] = True
        j+=pow

for val in list:
    if val == False:
        cnt+=1

print(cnt)