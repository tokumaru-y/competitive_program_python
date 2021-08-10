N,W=list(map(int, input().split()))
goods=[list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W+1) for _ in range(N+1)]
for i in range(N):
    v,w=goods[i]
    for j in range(W+1):
        if j+w<=W:
            dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j]+v)
        dp[i+1][j]=max(dp[i+1][j], dp[i][j])
print(dp[N][W])