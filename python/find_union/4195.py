from sys import stdin
t = int(input())

def find(a,friends):
    if friends[a] == a:
        return a
    
    return find(friends[a],friends)

def parent_and_compression(a,friends):
    if friends[a] == a:
        return a
    
    root_parent = parent_and_compression(friends[a],friends)
    friends[a] = root_parent

    return root_parent

def union(a,b,friends,cnt):
    a = parent_and_compression(a,friends)
    b = parent_and_compression(b,friends)

    if a!=b:
        friends[a] = b
        cnt[b]+=cnt[a]

for i in range(t):
    friends={}
    cnt={}
    n = int(input())

    for j in range(n):
        a,b = list(map(str,input().split()))

        if cnt.get(a) == None and cnt.get(b) == None:
            friends[a] = a
            friends[b] = b
            cnt[a] = cnt[b] = 1
        elif cnt.get(a) == None:
            friends[a] = a
            cnt[a] = 1
        elif cnt.get(b) == None:
            friends[b] = b
            cnt[b] = 1

        union(a,b,friends,cnt)
        root = find(a,friends)
        print(cnt[root])
