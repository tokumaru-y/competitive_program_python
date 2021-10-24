N,M=list(map(int, input().split()))
companies = [list(map(int, input().split())) for _ in range(N)]
recruters = [list(map(int, input().split())) for _ in range(M)]
dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
for a,b,c,w in companies:
    dp[a][b][c]=max(dp[a][b][c],w)
for i in range(101):
    for j in range(101):
        for k in range(101):
            dp[i+1][j][k]=max(dp[i+1][j][k], dp[i][j][k])
            dp[i][j+1][k]=max(dp[i][j+1][k], dp[i][j][k])
            dp[i][j][k+1]=max(dp[i][j][k+1], dp[i][j][k])
for a,b,c in recruters:
    print(dp[a][b][c])