N,W=list(map(int, input().split()))
goods = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W+1) for _ in range(N+1)]
for w in range(W+1):
    for i in range(N):
        sum_w = goods[i][1] + w
        if sum_w <= W:
            dp[i+1][sum_w] = max(dp[i][w] + goods[i][0], dp[i+1][sum_w])
        dp[i+1][w] = max(dp[i+1][w], dp[i][w])
print(max(dp[N]))