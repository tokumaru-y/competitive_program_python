W=int(input())
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W+1) for _ in range(K+1)]
for width,value in AB:
    for k in reversed(range(1, K+1)):
        for w in range(W+1):
            sw = w - width
            if sw <= W and sw >= 0:
                dp[k][w] = max(dp[k][w], dp[k-1][sw]+value)
print(max(dp[K]))