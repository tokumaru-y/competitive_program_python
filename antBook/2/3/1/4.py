W=int(input())
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [[[-1] * (W+1) for _ in range(N+1)] for _ in range(K+1)]
for k in range(K):
    dp[k][0][0]=0
for n in range(N):
    width, value = AB[n]
    for k in range(K+1):
        for w in range(W+1):
            if dp[k][n][w] == -1:continue
            sw = w + width
            if sw <= W  and k < K:
                dp[k+1][n+1][sw] = max(dp[k+1][n+1][sw], dp[k][n][w] + value)
            dp[k][n+1][w] = max(dp[k][n+1][w], dp[k][n][w])
            # dp[k][n+1][w]=max(dp[k][n][w], dp[k][n+1][w])
print(max(dp[K][N]))