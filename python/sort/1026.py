n = int(input())
min = 1000000000000000
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

c = [x*y for x,y in zip(a,b)]

print(sum(c))