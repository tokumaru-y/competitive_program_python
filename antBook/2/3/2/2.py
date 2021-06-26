S=input().rstrip()
T=input().rstrip()
ls = len(S)
lt = len(T)
dp=[[float('inf')] *(lt+1) for _ in range(ls+1)]
for i in range(ls+1):
    dp[i][0] = i
for i in range(lt+1):
    dp[0][i] = i
for i in range(ls):
    for j in range(lt):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j]
        dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)
print(dp[ls][lt])