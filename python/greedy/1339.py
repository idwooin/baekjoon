from sys import stdin
n = int(input())
dict={}
dict_final={}
strs=[]

for i in range(26):
    dict[chr(65+i)] = 0
    dict_final[chr(65+i)] = 0

for i in range(n):
    str = stdin.readline().strip('\n')
    strs.append(str)
    length = len(str)-1
    for j in range(len(str)):
        dict[str[j]]+=pow(10,length)
        length-=1

sorted_dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)

for idx,item in enumerate(sorted_dict):
    if idx == 10:
        break
    dict_final[item[0]] = 9-idx

result = 0
for i in range(n):
    str=strs[i]
    length = len(str)-1

    for j in range(len(str)):
        result+= dict_final[str[j]]*pow(10,length)
        length-=1

print(result)
