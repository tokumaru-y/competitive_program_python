A,B,C=list(map(int,input().split()))
dp=[[[0]*110 for _ in range(110)] for _ in range(110)]
for i in reversed(range(A,100)):
    for j in reversed(range(B,100)):
        for k in reversed(range(C,100)):
            dp[i][j][k]+=(dp[i+1][j][k])*(i)/(i+j+k)
            dp[i][j][k]+=(dp[i][j+1][k])*(j)/(i+j+k)
            dp[i][j][k]+=(dp[i][j][k+1])*(k)/(i+j+k)
            dp[i][j][k]+=1
print(dp[A][B][C])