N,M,L,X=list(map(int, input().split()))
A=list(map(int, input().split()))
dp = [[float("inf")] * (M+1) for _ in range(N+1)]
for i in range(N+1):dp[i][0]=1
for i in range(1,N+1):
    gas = A[i-1]
    for j in range(M+1):
        next = (j+gas)%M
        cnt = (j+gas)//M
        if dp[i-1][j] != float("inf"):
            dp[i][next] = min(dp[i][next], dp[i-1][j] + cnt)
        dp[i][j]=min(dp[i][j], dp[i-1][j])
ans = "Yes" if dp[N][L] <= X else "No"
print(ans)