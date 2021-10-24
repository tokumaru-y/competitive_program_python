# https://atcoder.jp/contests/abc041/tasks/abc041_d
N,M=list(map(int, input().split()))
XY=[list(map(int, input().split())) for _ in range(M)]
ng = [[False] * N for _ in range(N)]
for x,y in XY:
    x-=1
    y-=1
    ng[y][x]=True
dp = [0] * (1<<N)
dp[0]=1
for bit in range(1<<N):
    for i in range(N):
        if bit & 1<<i:continue
        ok = True
        for j in range(N):
            if bit & 1<<j and ng[j][i]:ok=False
        if ok:
            dp[bit | 1<<i] += dp[bit]
print(dp[(1<<N)-1])