n=int(input())
ans = 0
prime = [0 for _ in range(4000001)]
prime_list=[]
prime[0] = 1
prime[1] = 1
for i in range(2,2001):
    if prime[i] == 1:
        continue
    gap = i
    for j in range(2*i,4000001,gap):
        prime[j] = 1

for i in range(4000001):
    if prime[i] == 0:
        prime_list.append(i)

i=j=0
l = len(prime_list)

while i<l and j<l:
    if n > sum(prime_list[i:j+1]):
        j+=1
    elif n<sum(prime_list[i:j+1]):
        i+=1
    else:
        ans+=1
        j+=1

print(ans)