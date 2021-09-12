N,A=list(map(int, input().split()))
X=list(map(int, input().split()))
dp = [[[0] * 2510 for _ in range(51)] for _ in range(51)]
dp[0][0][0]=1
for i in range(N):
    for j in range(i+1):
        for k in range(2501):
            dp[i+1][j][k] += dp[i][j][k]
            if k+X[i] <= 2500:
                dp[i+1][j+1][k+X[i]] += dp[i][j][k]
ans = 0
for i in range(1,N+1):
    ans += dp[N][i][i*A]
print(ans)