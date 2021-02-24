N=int(input())
XYZ=[list(map(int,input().split())) for _ in range(N)]
dp=[[float('inf')]*N for _ in range(1<<N)]
dp[1][0]=0
for i in range(1<<N):
    for j in range(N):
        if not(i & 1<<j):continue
        print(i,j)
        print(dp[i])
        print(i^j)
        if dp[i][j] > dp[i^j][i] + abs(XYZ[i^j][0]-XYZ[j][0]) + abs(XYZ[i^j][1]-XYZ[j][1]) + min(0,XYZ[i^j][2]-XYZ[i][2]):
            dp[i][j] = dp[i^j][i] + abs(XYZ[i^j][0]-XYZ[j][0]) + abs(XYZ[i^j][1]-XYZ[j][1]) + min(0,XYZ[i^j][2]-XYZ[i][2])
ans=float('inf')
for i in range(1,N):
    ans=min(ans,dp[(1<<N)-1][i] + abs(XYZ[i][0]-XYZ[0][0]) + abs(XYZ[i][1]-XYZ[0][1]) + min(0,XYZ[j][2]-XYZ[0][2]))
print(ans)