from bisect import bisect_left
N=int(input())
dp = [float("inf")] * N
A=list(map(int,input().split()))
for a in A:
    ind = bisect_left(dp, a)
    dp[ind] = a
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()