H,W,C=list(map(int, input().split()))
dp = [[float("inf")] * (W+1) for _ in range(H+1)]
re_dp = [[float("inf")] * (W+1) for _ in range(H+1)]
grid = [list(map(int, input().split())) for _ in range(H)]
re_grid = []
for h in range(H):
    re_grid.append(list(reversed(grid[h])))
for h in range(1,H+1):
    for w in range(1,W+1):
        dp[h][w] = min(grid[h-1][w-1], dp[h-1][w]+C, dp[h][w-1]+C)
        re_dp[h][w] = min(re_grid[h-1][w-1], re_dp[h-1][w]+C, re_dp[h][w-1]+C)
ans = float("inf")
for h in range(1,H+1):
    for w in range(1,W+1):
        ans = min(ans, dp[h-1][w]+C+grid[h-1][w-1], dp[h][w-1]+C+grid[h-1][w-1])
        ans = min(ans, re_dp[h-1][w]+C+re_grid[h-1][w-1], re_dp[h][w-1]+C+re_grid[h-1][w-1])

print(ans)