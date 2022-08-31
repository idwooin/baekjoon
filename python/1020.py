num = [6,2,5,5,4,5,6,3,7,5]

s = input()
max_num = 10**len(s)-1
n = int(s)

curr =0
for i in s:
    curr+=num[int(i)]

line = 0
ans = 0
while line!=curr:
    line = 0
    n+=1
    ans+=1
    temp = str(n)
    if len(temp)>len(s):
        n=0
        temp = str(n)
    zeros = ''
    zero_len=len(s)-len(temp)
    for i in range(zero_len):
        zeros+='0'
    temp = zeros+temp
    for st in temp:
        line+=num[int(st)]

print(ans)