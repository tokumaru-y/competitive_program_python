N=int(input())
XYZ=[list(map(int,input().split())) for _ in range(N)]
dp= [[float('inf')] * N for _ in range(1<<N)]
def calc(a,b,c,p,q,r):
    return abs(a-p)+abs(b-q)+max(0,r-c)

dp[1][0]=0
for b in range(1<<N):
    for i in range(N):
        if not (b & (1<<i)):continue
        for j in range(N):
            if (b & (1<<j)):continue
            nb = b | 1<<j
            if dp[nb][j] > dp[b][i] + calc(XYZ[i][0],XYZ[i][1],XYZ[i][2],XYZ[j][0], XYZ[j][1], XYZ[j][2]):
                dp[nb][j] = dp[b][i] + calc(XYZ[i][0],XYZ[i][1],XYZ[i][2],XYZ[j][0], XYZ[j][1], XYZ[j][2])
ans = float('inf')
for i in range(N):
    ans = min(ans, dp[(1<<N)-1][i]+calc(XYZ[i][0],XYZ[i][1],XYZ[i][2],XYZ[0][0],XYZ[0][1], XYZ[0][2]))
print(ans)