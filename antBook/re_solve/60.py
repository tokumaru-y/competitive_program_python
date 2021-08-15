N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
dp=[0] * (W+1)
for v,w in VW:
    for i in range(W+1):
        if i+w<=W:
            dp[i+w] = max(dp[i+w], dp[i]+v)
print(dp[W])