import re

T = int(input())
for i in range(T):
    str = input()
    res = re.compile('(100+1+|01)+')
    ans = "YES" if res.fullmatch(str) else "NO"
    print(ans)