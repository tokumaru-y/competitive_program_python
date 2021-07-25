import math
N,M,L,K=list(map(int, input().split()))
A=list(map(int, input().split()))
dp = [[float("inf")] * (M) for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
    a = A[i]
    for j in reversed(range(M)):
        dp[i+1][j] = min(dp[i][j],dp[i+1][j])
        if dp[i][j] == float("inf"):continue
        if j+a >= M:
            dp[i+1][(j+a)%(M)] = min(dp[i+1][(j+a)%(M)], dp[i][j]+math.ceil(a/M))
        else:
            dp[i+1][j+a] = min(dp[i+1][j+a], dp[i][j])
# print(dp)
ans = "Yes"
if dp[N][L] == float("inf") or dp[N][L] >= K:ans = "No"
print(ans)