n = int(input())
h = list(map(int,input().split()))
show = [0 for _ in range(n)]

def check(i,j):
    global h

    slope = (h[j]-h[i])/(j-i)

    for k in range(i+1,j):
        if slope*(k-i)+h[i] > h[k]:
            continue
        return False
    
    return True
    

if n != 1:
    for i in range(n):
        for j in range(i,n):
            if i==j:
                continue

            if check(i,j):
                show[i]+=1
                show[j]+=1
    print(max(*show))
else:
    print(*show)