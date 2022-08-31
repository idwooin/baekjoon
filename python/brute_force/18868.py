m,n = map(int,input().split())
uni = []
for i in range(m):
    uni.append(list(map(int,input().split())))

def comp(u1,u2):
    for i in range(n):
        for j in range(i,n):
            if u1[i] < u1[j]:
                if u2[i] >= u2[j]:
                    return False
            elif u1[i] > u1[j]:
                if u2[i] <= u2[j]:
                    return False
            else:
                if u2[i] != u2[j]:
                    return False
    
    return True

ans = 0
for i in range(m):
    for j in range(i+1,m):
        ans+=comp(uni[i],uni[j])

print(ans)