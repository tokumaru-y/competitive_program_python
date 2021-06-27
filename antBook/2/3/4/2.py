import math
N,K=list(map(int, input().split()))
A=[int(input()) for _ in range(N)]
dp = [[float('inf')] * (N+1) for _ in range(N+1)]
dp[0][0]=0
sum_game = [0] * (N+1)
for i in range(N):
    sum_game[i+1] = sum_game[i] + A[i]
if sum_game[N] == K:
    print(1)
    exit()
for i in range(N):
    for j in range(N):
        if dp[i][j] == float('inf'):continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        if i == 0:
            dp[i+1][j+1]=min(dp[i+1][j+1], dp[i][j]+1)
        else:
            least = (dp[i][j] * sum_game[i+1] // sum_game[i]) + 1
            if least <= A[i] + dp[i][j]:
                dp[i+1][j+1] = min(dp[i+1][j+1], least)
ans = 0
for i in range(N+1):
    if dp[N][i] <= K:
        ans = max(ans, i)
print(ans)