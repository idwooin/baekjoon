t = int(input())
list1 = [0,1,3,6,10,15,21,100]
money1 = [500,300,200,50,30,10,0]
list2 = [0,1,3,7,15,31,100]
money2 = [512,256,128,64,32,0]

for i in range(t):
    ans = 0
    a,b = list(map(int,input().split()))

    for i in range(7):
        if a>list1[i] and a<=list1[i+1]:
            ans+=money1[i]

    for i in range(6):
        if b>list2[i] and b<=list2[i+1]:
            ans+=money2[i]

    print(ans*10000)

