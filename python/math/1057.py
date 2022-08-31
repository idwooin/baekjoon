n,a,b = map(int,input().split())
round = 0

while a!=b:
    if a%2 == 1:
        a+=1
    if b%2 == 1:
        b+=1
    
    a//=2
    b//=2
    round+=1

print(round)
