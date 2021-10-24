# https://atcoder.jp/contests/abc180/tasks/abc180_e
N=int(input())
XYZ=[list(map(int,input().split())) for _ in range(N)]
dp = [[float("inf")] * (N) for _ in range(1<<N)]
dp[1][0]=0
for bit in range(1<<N):
    for i in range(N):
        if bit & (1<<i):
            for j in range(N):  
                if i == j or not (bit & 1<<j): continue
                x1,y1,z1=XYZ[i]
                x2,y2,z2=XYZ[j]
                dp[bit][i] = min(dp[bit][i], dp[bit^(1<<i)][j] + abs(x1-x2) + abs(y1-y2) + max(0, z1-z2))
ans = float("inf")
for i in range(N):
    tmp = dp[(1<<N)-1][i]
    if i > 0:
        x1,y1,z1=XYZ[0]
        x2,y2,z2=XYZ[i]
        tmp += abs(x1-x2) + abs(y1-y2) + max(0, z1-z2)
    ans = min(ans, tmp)
print(ans)