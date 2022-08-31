s1 = '0' + input().strip()
s2 = '0' + input().strip()

dp = [[""]*len(s2) for i in range(len(s1))]

for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        # s1의 현재 문자와 s2의 문자가 같을 시
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[len(s1)-1][len(s2)-1]))
print(dp[len(s1)-1][len(s2)-1])