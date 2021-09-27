# https://atcoder.jp/contests/tdpc/tasks/tdpc_number
D=int(input())
N=input()
len_n = len(N)
dp = [[[0] * (2) for _ in range(101)] for _ in range(len_n+1)]
dp[0][0][0]=1
MOD = 10 ** 9 + 7
for i in range(len_n):
    for j in range(D):
        for num in range(10):
            dp[i+1][(j+num)%D][True] += dp[i][j][True]
            dp[i+1][(j+num)%D][True] %= MOD
        limit = int(N[i])
        for num in range(limit):
            dp[i+1][(j+num)%D][True] += dp[i][j][False]
            dp[i+1][(j+num)%D][True] %= MOD
        dp[i+1][(j+limit)%D][False] += dp[i][j][False]
        dp[i+1][(j+limit)%D][False] %= MOD
print((dp[len_n][0][True] + dp[len_n][0][False] - 1)%MOD)