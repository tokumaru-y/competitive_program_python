# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
D=int(input())
N=list(input())
MOD = 10**9+7
dp = [[[0] * 2 for _ in range(D)] for _ in range(len(N)+1)]
dp[0][0][0]=1
# dp[0][0][1]=1
for i in range(len(N)):
    for j in range(D):
        for k in range(10):
            dp[i+1][(j+k)%D][1] += dp[i][j][1]
            dp[i+1][(j+k)%D][1] %= MOD
        limit = int(N[i])
        for k in range(limit):
            dp[i+1][(j+k)%D][1] += dp[i][j][0]
            dp[i+1][(j+k)%D][1] %= MOD
        dp[i+1][(j+limit)%D][0] = dp[i][j][0]
        dp[i+1][(j+limit)%D][0] %= MOD
print((dp[len(N)][0][0] + dp[len(N)][0][1] - 1) % MOD)