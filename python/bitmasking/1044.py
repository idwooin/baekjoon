N = int(input())
score1 = list(map(int,input().split()))
score2 = list(map(int,input().split()))
picked = [0 for i in range(N)]
max_num = 1000000000000001
map = [[max_num for i in range(N)] for j in range(N)]

max_1 = max_2 = N/2

for i in range(N):
    for j in range(N):
        if i==j:
            continue

        map[i][j] = abs(score1[i] - score2[j])

for i in range(N):
    if picked[i]:
        continue
    

    list_temp_1 = [map[i][j] for j in range(N)]
    list_temp_2 = [map[j][i] for j in range(N)]
    val1=min(list_temp_1)
    idx1 = list_temp_1.index(val1)
    val2=min(list_temp_2)
    idx2 = list_temp_2.index(val2)

    if val1 <= val2:
        picked[i] = 1
        picked[idx1] = 2
        for j in range(N):
            map[j][i] = max_num
            map[i][j] = max_num
            map[idx1][j] = max_num
            map[j][idx1] = max_num
    else:
        picked[i] = 2
        picked[idx2] = 1
        for j in range(N):
            map[j][i] = max_num
            map[i][j] = max_num
            map[idx2][j] = max_num
            map[j][idx2] = max_num


print(picked)