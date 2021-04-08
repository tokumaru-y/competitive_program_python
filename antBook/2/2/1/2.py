N,M=list(map(int, input().split()))
coins = list(map(int, input().split()))
dp = [float('inf')] * 50001
dp[0] = 0
for i in range(N+1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i-c] + 1, dp[i])
print(dp[N])