from bisect import bisect_left
N=int(input())
A=list(map(int, input().split()))
dp = [float("inf")] * N
for a in A:
    index = bisect_left(dp, a)
    dp[index]=a
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()