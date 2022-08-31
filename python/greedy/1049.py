import math

n,m = map(int,input().split())
pack = math.inf
nat = math.inf
for i in range(m):
    p,t = map(int,input().split())
    pack = min(pack,p)
    nat = min(nat,t)

if pack > 6*nat:
    print(n*nat)
else:
    pack_p=n//6
    nat_p = n%6
    if pack <= nat_p*nat:
        print((pack_p+1)*pack)
    else:
        print(pack_p*pack + nat_p*nat)