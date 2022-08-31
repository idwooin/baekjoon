import math
x = int(input())
dp = [[math.inf,""] for _ in range(x+1)]
dp[1][0] = 0
dp[1][1] = ''

for i in range(2,x+1):
    dp[i][0] = min(dp[i][0],dp[i-1][0]+1)
    if dp[i][0] == dp[i-1][0]+1:
        dp[i][1] = dp[i-1][1] + '1'
    if i%2 == 0:
        dp[i][0] = min(dp[i][0],dp[i//2][0]+1)
        if dp[i][0] == dp[i//2][0]+1:
            dp[i][1] = dp[i//2][1] + '2'
    if i>=3 and i%3 == 0:
        dp[i][0] = min(dp[i][0],dp[i//3][0]+1)
        if dp[i][0] == dp[i//3][0]+1:
            dp[i][1] = dp[i//3][1] + '3'

print(dp[x][0])
final_str = dp[x][1]
ans = []
ans = str(x)
for i in range(len(final_str)-1,-1,-1):
    s = final_str[i]
    if s == '1':
        x-=1
        ans+=' '+str(x)
    elif s == '2':
        x//=2
        ans+=' '+str(x)
    else:
        x//=3
        ans+=' '+str(x)

print(''.join(ans))

# for i in range(x-1,0,-1):
#     val = min(dp[i+1][0][0],dp[i+1][1][0],dp[i+1][2][0])
#     dp[i][0][0] = val+1
#     if val == dp[i+1][0][0]:
#         dp[i][0][1] = dp[i+1][0][1] + '1'
#     elif val == dp[i+1][1][0]:
#         dp[i][0][1] = dp[i+1][1][1] + '1'
#     else:
#         dp[i][0][1] = dp[i+1][2][1] + '1'

#     if 2*i <= x:
#         val = min(dp[2*i][0][0],dp[2*i][1][0],dp[2*i][2][0])
#         dp[i][1][0] = val +1 
#         if val == dp[2*i][0][0]:
#             dp[i][1][1] = dp[2*i][0][1] + '2'
#         elif val == dp[2*i][1][0]:
#             dp[i][1][1] = dp[2*i][1][1] + '2'
#         else:
#             dp[i][1][1] = dp[2*i][2][1] + '2'
#     if 3*i <= x:
#         val = min(dp[3*i][0][0],dp[3*i][1][0],dp[3*i][2][0])
#         dp[i][2][0] = val +1
#         if val == dp[3*i][0][0]:
#             dp[i][2][1] = dp[3*i][0][1] + '3'
#         elif val == dp[3*i][1][0]:
#             dp[i][2][1] = dp[3*i][1][1] + '3'
#         else:
#             dp[i][2][1] = dp[3*i][2][1] + '3'

# val = min(dp[1][0][0],dp[1][1][0],dp[1][2][0])
# print(val)
# if val == dp[1][0][0]: final_str = dp[1][0][1]
# elif val == dp[1][1][0]: final_str = dp[1][1][1]
# else: final_str = dp[1][2][1]

# ans = []
# ans = str(x)
# for s in final_str:
#     if s == '1':
#         x-=1
#         ans+=' '+str(x)
#     elif s == '2':
#         x//=2
#         ans+=' '+str(x)
#     else:
#         x//=3
#         ans+=' '+str(x)

# print(''.join(ans))