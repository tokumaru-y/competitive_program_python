import heapq
H,W=list(map(int,input().split()))
grid=[list(input()) for _ in range(H)]
dp=[[0] * (W) for _ in range(H)]
X=[[0] * (W) for _ in range(H)]
Y=[[0] * (W) for _ in range(H)]
Z=[[0] * (W) for _ in range(H)]
MOD=10**9+7
dp[0][0]=1
for h in range(H):
    for w in range(W):
        if (h==0 and w== 0) or grid[h][w]=="#":continue
        if w>0:X[h][w]=(X[h][w-1]+dp[h][w-1])%MOD
        if h>0:Y[h][w]=(Y[h-1][w]+dp[h-1][w])%MOD
        if h>0 and w>0:Z[h][w]=(Z[h-1][w-1]+dp[h-1][w-1])%MOD
        dp[h][w]=(X[h][w]+Y[h][w]+Z[h][w])%MOD
print(dp[H-1][W-1])