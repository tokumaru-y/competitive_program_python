H,W=list(map(int, input().split()))
table=[]
for _ in range(10):
    table.append(list(map(int, input().split())))
dp=[[float('inf')] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        dp[i][j]=table[i][j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j])
ans = 0
grid = []
for _ in range(H):
    grid.append(list(map(int, input().split())))
for h in range(H):
    for w in range(W):
        if abs(grid[h][w]) == 1:continue
        ans+=dp[grid[h][w]][1]
print(ans)