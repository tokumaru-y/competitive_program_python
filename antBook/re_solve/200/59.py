N,M=list(map(int, input().split()))
ABCW=[list(map(int, input().split())) for _ in range(N)]
XYZ=[list(map(int, input().split())) for _ in range(M)]
dp = [[[0] * (102) for _ in range(102)] for _ in range(102)]
for a,b,c,w in ABCW:
    dp[a][b][c]=max(dp[a][b][c], w)
for a in range(101):
    for b in range(101):
        for c in range(101):
            dp[a+1][b][c]=max(dp[a][b][c], dp[a+1][b][c])
            dp[a][b+1][c]=max(dp[a][b][c], dp[a][b+1][c])
            dp[a][b][c+1]=max(dp[a][b][c], dp[a][b][c+1])
for x,y,z in XYZ:
    print(dp[x][y][z])