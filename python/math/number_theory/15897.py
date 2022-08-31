n=int(input())
ans = n
j=1
i=1
while i<n:
    temp = (n-1)//i
    j=(n-1)//temp
    how_many = (j-i+1)
    ans+=temp*how_many
    i=j+1

print(ans)