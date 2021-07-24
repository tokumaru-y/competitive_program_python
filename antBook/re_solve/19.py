W=int(input())
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W+1) for _ in range(K+1)]
for n in range(N):
    a,b = AB[n]
    for k in reversed(range(1,K+1)):
        for w in range(W+1):
            if w-a>=0:
                dp[k][w] = max(dp[k][w], dp[k-1][w-a]+b)
ans = 0
for i in range(N):
    for k in range(K+1):
        ans=max(ans,max(dp[k]))
print(ans)