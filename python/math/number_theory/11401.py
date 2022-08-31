mod = 1000000007
n,k = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[0] = dp[1] = 1
for i in range(2,n+1):
    dp[i] = (dp[i-1]*i)%mod

def power(a,n,mod):
    ans = 1

    while n>0:
        rest = n%2
        if rest==1:
            ans=(ans*a)%mod
        a=(a*a)%mod
        n=n//2

    return ans

div = (dp[k]*dp[n-k])%mod
result = (dp[n]*power(div,mod-2,mod))%mod
print(int(result))