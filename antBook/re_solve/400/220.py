# https://atcoder.jp/contests/arc057/tasks/arc057_b
from math import floor
N,K=list(map(int, input().split()))
A=[int(input()) for _ in range(N)]
if sum(A) == K:
    print(1)
    exit()
dp = [float("inf")] * (N+1)
dp[0] = 0
dp[1] = 1
sum_game = A[0]
for i in range(1,N):
    left_value = floor(((dp[i]*A[i]) / sum_game))
    dp[i+1]=left_value + 1
    sum_game+=A[i]
tmp_cnt = 0
for i in range(N):
    tmp_cnt += dp[i+1]
    if tmp_cnt > K:
        print(i)
        exit()
