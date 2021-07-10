from bisect import bisect_left
N=int(input())
A=[int(input()) for _ in range(N)]
dp=[float("inf")] * N
for a in A:
    ind = bisect_left(dp, a)
    dp[ind] = a
for i in reversed(range(N)):
    if dp[i] < float('inf'):
        print(N-(i+1))
        exit()