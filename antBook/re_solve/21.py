D=int(input())
N=list(input())
len_n = len(N)
MOD =  10**9+7
dp = [[[0] * D for _ in range(2)] for _ in range(len_n+1)]
dp[0][0][0]=1
for i in range(len_n):
    for j in range(D):
        for k in range(10):
            dp[i+1][1][(j+k)%D] += dp[i][1][j]
            dp[i+1][1][(j+k)%D] %= MOD
        limit = int(N[i])
        for k in range(limit):
            dp[i+1][1][(j+k)%D] += dp[i][0][j]
            dp[i+1][1][(j+k)%D] %= MOD
        dp[i+1][0][(j+limit)%D] = dp[i][0][j]
ans = dp[len_n][0][0] + dp[len_n][1][0] - 1
print(ans)