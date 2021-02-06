h,w=list(map(int,input().split()))
grid=[input().rstrip() for _ in range(h)]
MOD=10**9+7
dp = [[0] * (w+1) for _ in range(h+1)]
dpx = [[0] * (w+1) for _ in range(h+1)]
dpy = [[0] * (w+1) for _ in range(h+1)]
dpxy = [[0] * (w+1) for _ in range(h+1)]
dp[1][1]=1
for i in range(1,h+1):
    for j in range(1,w+1):
        if i== 0 and j==0:continue
        if grid[i-1][j-1]=='#':
            dpx[i][j]=0
            dpy[i][j]=0
            dpxy[i][j]=0
            continue
        dp[i][j]+=(dpx[i][j-1]+dpy[i-1][j]+dpxy[i-1][j-1])%MOD
        dpx[i][j]+=dpx[i][j-1]+dp[i][j]%MOD
        dpy[i][j]+=dpy[i-1][j]+dp[i][j]%MOD
        dpxy[i][j]+=dpxy[i-1][j-1]+dp[i][j]%MOD
print(dp[h][w])