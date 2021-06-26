Q=int(input())
from sys import stdin
input = stdin.readline
for _ in range(Q):
    S = list(input().rstrip())
    T = list(input().rstrip())
    ls = len(S)
    lt = len(T)
    dp = [[0] * (lt+1) for _ in range(ls+1)]
    for i in range(ls):
        for j in range(lt):
            if S[i] == T[j]:
                dp[i+1][j+1] += dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
    print(dp[ls][lt])