N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
dp = [0] * (10**4+1)
for value,weight in VW:
    for w in range(10**4+1):
        if w-weight>=0:
            dp[w]=max(dp[w], dp[w-weight]+value)
print(dp[W])