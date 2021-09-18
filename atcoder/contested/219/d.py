N=int(input())
X,Y=list(map(int, input().split()))
AB=[list(map(int, input().split())) for _ in range(N)]
dp = [[float("inf")] * (301) for _ in range(301)]
dp[0][0] = 0
for i in range(N):
    a,b=AB[i]
    for x in reversed(range(301)):
        for y in reversed(range(301)):
            nx = min(x+a, 300)
            ny = min(y+b, 300)
            if dp[x][y] != float("inf"):
                dp[nx][ny]=min(dp[nx][ny], dp[x][y] + 1)
ans = float("inf")
for i in range(X,301):
    for j in range(Y, 301):
        ans = min(ans, dp[i][j])
print(ans if ans != float("inf") else -1)