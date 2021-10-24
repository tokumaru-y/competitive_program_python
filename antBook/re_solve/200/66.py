from bisect import bisect_left
N=int(input())
C=[int(input()) for _ in range(N)]
dp = [float("inf")] * (N+1)
dp[0]=0
for c in C:
    ind=bisect_left(dp, c)
    dp[ind]=c
for i in reversed(range(N+1)):
    if dp[i]!=float("inf"):
        print(N-i)
        exit()