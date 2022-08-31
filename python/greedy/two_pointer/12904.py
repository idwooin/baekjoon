s = input()
t = input()

sl = len(s)
tl = len(t)

flag = "R"
right_point = tl-1
left_point = 0

for i in range(tl-sl):
    if flag == "R":
        if t[right_point] == 'A':
            right_point-=1
        else:
            right_point-=1
            flag = 'L'
    else:
        if t[left_point] == 'A':
            left_point+=1
        else:
            left_point+=1
            flag = 'R'

final_s = ""

if flag == 'R':
    for i in range(sl):
        final_s += t[left_point]
        left_point+=1
else:
    for i in range(sl):
        final_s += t[right_point]
        right_point-=1

if s==final_s:
    print(1)
else:
    print(0)