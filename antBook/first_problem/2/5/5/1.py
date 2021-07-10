N,M = list(map(int, input().split()))
dp = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a,b,c = list(map(int, input().split()))
    a-=1
    b-=1
    dp[a][b]=c
    dp[b][a]=c

for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
ans = float('inf')
for i in range(N):
    ans = min(ans, max(dp[i]))
print(ans)