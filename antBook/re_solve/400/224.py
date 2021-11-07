# https://yukicoder.me/problems/no/269
N,S,K=list(map(int, input().split()))
left = S - N*(N-1)*K//2
if left<0:
    print(0)
    exit()
MOD = 10**9+7
dp = [[0] * (left+1) for _ in range(N+1)]
dp[0][0]=1
for i in range(1,N+1):
    for j in range(left+1):
        if j-i>=0:
            dp[i][j] = dp[i-1][j] + dp[i][j-i]
        else:
            dp[i][j] = dp[i-1][j]
        dp[i][j] %= MOD
print(dp[N][left])