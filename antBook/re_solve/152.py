# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c
N,M=list(map(int, input().split()))
ABCW=[list(map(int, input().split())) for _ in range(N)]
XYZ=[list(map(int, input().split())) for _ in range(M)]
dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
for a,b,c,w in ABCW:
    dp[a][b][c]=max(dp[a][b][c],w)
for ai in range(101):
    for bi in range(101):
        for ci in range(101):
            t = dp[ai][bi][ci]
            dp[ai+1][bi][ci] = max(dp[ai+1][bi][ci], t)
            dp[ai][bi+1][ci] = max(dp[ai][bi+1][ci], t)
            dp[ai][bi][ci+1] = max(dp[ai][bi][ci+1], t)
for x,y,z in XYZ:
    print(dp[x][y][z])