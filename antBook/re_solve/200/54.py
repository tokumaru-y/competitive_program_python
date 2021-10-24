W=int(input())
N,K=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp=[[0] * (W+1) for _ in range(K+1)]
for i in range(N):
    w,v=AB[i]
    for k in reversed(range(K)):
        for j in range(W+1):
            if j+w<=W:
                dp[k+1][j+w]=max(dp[k+1][j+w], dp[k][j]+v)
ans = 0
for k in range(1,K+1):
    for j in range(W+1):
        ans = max(ans,dp[k][j])
print(ans)