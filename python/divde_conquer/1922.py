from sys import stdin
n = int(stdin.readline())
mp4 = []

def div_conquer(mp4,n,i,j):
    if n==2:
        temp = mp4[i][j] + mp4[i][j+1] + mp4[i+1][j] + mp4[i+1][j+1]
        temp2 = temp.strip('0') if mp4[i][j] == '0' else temp.strip('1')
        if temp2!="":
            str = '(' + temp + ')'
            return str
        else:
            str = mp4[i][j]
            return str

    str1=div_conquer(mp4,n//2,i,j)
    str2=div_conquer(mp4,n//2,i,j+n//2)
    str3=div_conquer(mp4,n//2,i+n//2,j)
    str4=div_conquer(mp4,n//2,i+n//2,j+n//2)

    temp = str1 + str2 + str3 + str4
    temp2 = temp.strip('0') if mp4[i][j] == '0' else temp.strip('1')

    if temp2!="":
        str = '(' + temp + ')'
        return str
    else:
        str = str1
        return str

for i in range(n):
    mp4.append(stdin.readline().rstrip('\n'))

ans = div_conquer(mp4,n,0,0)
print(ans)