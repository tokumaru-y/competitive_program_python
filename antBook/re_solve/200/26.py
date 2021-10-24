S=input().rstrip()
T=input().rstrip()
ls = len(S)+1
lt = len(T)+1
dp = [[float("inf")] * lt for _ in range(ls)]
for i in range(ls):
    dp[i][0] = i
for i in range(lt):
    dp[0][i] = i
for i in range(ls-1):
    for j in range(lt-1):
        if S[i] == T[j]:
            dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1])
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1)
print(dp[ls-1][lt-1])