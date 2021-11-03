# https://atcoder.jp/contests/arc057/tasks/arc057_b
from math import floor
N,K=list(map(int, input().split()))
A=[int(input()) for _ in range(N)]
if sum(A) == K:
    print(1)
    exit()
dp = [[float("inf")] * (N+1)  for _ in range(N+1)]
dp[0][0] = 0
dp[1][0] = 0
dp[1][1] = 1
sum_game = A[0]
for i in range(1,N):
    for j in range(N):
        if dp[i][j] == float("inf"):continue
        pre_wins = floor((dp[i][j] * A[i]) / sum_game) + 1
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1], pre_wins + dp[i][j])
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    sum_game += A[i]
for i in reversed(range(N+1)):
    if dp[N][i]<=K:
        print(i)
        exit()