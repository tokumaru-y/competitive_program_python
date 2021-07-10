N,W=list(map(int, input().split()))
dp=[0] * (W+1)
AB=[list(map(int, input().split())) for _ in range(N)]
for w in range(W+1):
    for value, weight in AB:
        if w - weight >= 0:
            dp[w] = max(dp[w], dp[w-weight] + value)
print(dp[W])