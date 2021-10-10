# https://atcoder.jp/contests/abc180/tasks/abc180_e
N=int(input())
XYZ=[list(map(int,input().split())) for _ in range(N)]
dp = [[float("inf")] * (N) for _ in range(1<<N)]
dp[0][0]=0
for bit in range(1<<N):
    for i in range(N):
        if bit & (1<<i):
            for j in range(N):
                if i == j or (bit & 1<<j): continue
                x1,y1,z1=XYZ[i]
                x2,y2,z2=XYZ[j]
                print(bit,i,j)
                dp[bit][i] = min(dp[bit][i], dp[bit^i][j] + abs(x1-x2) + abs(y1-y2) + max(0, z1-z2))
for i in range(1<<N):
    print(dp[i])
print(min(dp[(1<<N) - 1 ]))