import math
N,M,L,K = list(map(int, input().split()))
A=list(map(int, input().split()))
dp = [[float("inf")] * (M) for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(M):
        step = (A[i]+j)
        if step < M:
            dp[i+1][step] = min(dp[i][j], dp[i+1][step])
        else:
            add = step // M
            origin = step % M
            dp[i+1][origin]=min(dp[i][j] + add , dp[i+1][origin])
        dp[i+1][j]=min(dp[i+1][j], dp[i][j])
ans = "Yes" if dp[N][L] < K else "No"
print(ans) 