# https://atcoder.jp/contests/arc057/tasks/arc057_b
import math
N,K=list(map(int, input().split()))
A=[int(input()) for _ in range(N)]
# dp[i][j]:=i日目までにj回勝つときの最小勝利回数
dp = [[float("inf")] * (N+1) for _ in range(N+1)]
dp[0][0]=0
dp[1][0]=0
dp[1][1]=1
if sum(A) == K:
    print(1)
    exit()
sum = A[0]
for i in range(1,N):
    for j in range(i+1):
        if j+1 <= N and dp[i][j] < float("inf"):
            add = (dp[i][j] * A[i]) // sum 
            add += 1
            dp[i+1][j+1]=min(dp[i][j] + add, dp[i+1][j+1])
        dp[i+1][j]=min(dp[i][j], dp[i+1][j])
    sum += A[i]
for i in reversed(range(N+1)):
    if dp[N][i] <= K:
        print(i)
        exit()