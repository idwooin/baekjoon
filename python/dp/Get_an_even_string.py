import sys

# def recursion(s,dp,curr):
#     if curr == len(s):
#         return 0
    
#     if dp[curr] >= 0:
#         return dp[curr]

#     if curr == len(s)-1:
#         return 1

#     if curr < len(s)-1 and s[curr] == s[curr+1]:
#         return recursion(s,dp,curr+2)

#     i = curr+1
#     while i < len(s) and s[curr] != s[i]:
#         i+=1
#     if i == len(s):
#         return 1+recursion(s,dp,curr+1)
#     else:
#         mina =  1+recursion(s,dp,curr+1)
#         minb = i-curr-1 + recursion(s,dp,i+1)
    
#     dp[curr] = min(mina,minb)
#     return dp[curr]

def solve(s,dp):
    dp[len(s)] = 0
    dp[len(s)-1] = 1
    for i in range(len(s)-2,-1,-1):
        if s[i] == s[i+1]:
            dp[i] = dp[i+2]
            continue
        
        j = i+1
        while j<len(s) and s[i]!=s[j]:
            j+=1
        
        if j == len(s):
            dp[i] = 1+dp[i+1]
        else:
            dp[i] = min(1+dp[i+1],j-i-1 + dp[j+1])

    return dp[0]


t = int(sys.stdin.readline())
for i in range(t):
    s = sys.stdin.readline().strip()
    dp = [-1 for _ in range(len(s)+1)]
    print(solve(s,dp))
    
    