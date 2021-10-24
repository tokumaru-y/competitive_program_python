import sys
sys.setrecursionlimit(10**9)
H,W=list(map(int, input().split()))
dp=[[-1] * W for _ in range(H)]
grid = [list(map(int, input().split())) for _ in range(H)]
hi=[0,1,0,-1]
wi=[1,0,-1,0]
def dfs(h,w):
    if dp[h][w]>-1:return dp[h][w]
    res = 1
    for i in range(4):
        nh=h+hi[i]
        nw=w+wi[i]
        if not(0<=nh<=H-1 and 0<=nw<=W-1):continue
        if grid[h][w] < grid[nh][nw]:
            res += dfs(nh,nw)
            res %= MOD
    dp[h][w] = res
    return res
ans=0
MOD=10**9+7
for h in range(H):
    for w in range(W):
        ans += dfs(h,w)
        ans %= MOD
print(ans)