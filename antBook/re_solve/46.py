from collections import deque
import sys
sys.setrecursionlimit(10**9)
H,W=list(map(int, input().split()))
N=int(input())
dp = [[0] * (W+1) for _ in range(H+1)]
grid = [[1] * (W+1) for _  in range(H+1)]
hi = [0,1]
wi = [1,0]
for _ in range(N):
    a,b=list(map(int, input().split()))
    grid[a][b]=0
dp[1][1]=grid[1][1]
for i in range(H):
    for j in range(W):
        if i == 0 and j== 0:continue
        if grid[i+1][j+1]==0:
            dp[i+1][j+1]=0
        else:
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
print(dp[H][W])