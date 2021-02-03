a,b,c=list(map(int,input().split()))
dp=[[[0] * 110 for _ in range(110)] for _ in range(110)]

for i in reversed(range(a,100)):
    for j in reversed(range(b,100)):
        for k in reversed(range(c,100)):
            dp[i][j][k]+=i/(i+j+k) * (dp[i+1][j][k] + 1)
            dp[i][j][k]+=j/(i+j+k) * (dp[i][j+1][k] + 1)
            dp[i][j][k]+=k/(i+j+k) * (dp[i][j][k+1] + 1)
print(dp[a][b][c])