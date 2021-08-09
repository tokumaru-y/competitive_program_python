import sys
sys.setrecursionlimit(10**9)
H,W=list(map(int, input().split()))
N=int(input())
dp = [[0] * (W+1) for _ in range(H+1)]
grid = [[0] * (W+1) for _  in range(H+1)]
hi = [0,1]
wi = [1,0]
def dfs(h,w):
    for i in range(2):
        nh = h-hi[i]
        nw = w-wi[i]
        if not(0<=nh<=H and 0<=nw<=W):continue
        if grid[nh][nw] == 1:
            dp[h][w]=0
        else:
            dp[h][w]+= dp[nh][nw]
        dfs(nh,nw)
for _ in range(N):
    a,b=list(map(int, input().split()))
    grid[a][b]=1
dp[1][1]=grid[1][1]
dfs(H,W)
print(dp[0][0])
