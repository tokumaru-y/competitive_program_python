# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c
N,M=list(map(int, input().split()))
ABCW = [list(map(int, input().split())) for _ in range(N)]
XYZ = [list(map(int, input().split())) for _ in range(M)]
idx = 102
dp = [[[0] * (idx) for _ in range(idx)] for _ in range(idx)]
for a,b,c,w in ABCW:dp[a][b][c] = max(dp[a][b][c], w)
for i in range(idx-1):
    for j in range(idx-1):
        for k in range(idx-1):
            dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])
            dp[i+1][j+1][k] = max(dp[i][j][k], dp[i+1][j+1][k], dp[i+1][j][k])
            dp[i+1][j][k+1] = max(dp[i][j][k], dp[i+1][j][k], dp[i+1][j][k+1])
            dp[i][j+1][k] = max(dp[i][j][k], dp[i][j+1][k])
            dp[i][j+1][k+1] = max(dp[i][j][k], dp[i][j+1][k], dp[i][j+1][k+1])
            dp[i][j][k+1] = max(dp[i][j][k], dp[i][j][k+1])
for x,y,z in XYZ:
    print(dp[x][y][z])