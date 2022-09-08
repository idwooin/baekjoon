str = []
t = int(input())
scores =[0 for i in range(100)]


for i in range(t):
    str.append(input())

for i in range(1,100):
    scores[i] = scores[i-1] + i

for i in range(t):
    strs = str[i]

    circles = 0
    cons = 0

    for c in strs:
        if c=='X':
            if cons!=0:
                circles+= scores[cons]
            cons = 0
        else:
            cons+=1

    if cons!=0:
        circles+= scores[cons]

    print(circles)

