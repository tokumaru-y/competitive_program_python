from bisect import bisect_left
N=int(input())
WH=[list(map(int, input().split())) for _ in range(N)]
dp = [float("inf")] * N
sortwh = sorted(WH, key=lambda x: (x[0], -x[1]))
for h,w in sortwh:
    ind = bisect_left(dp, w)
    dp[ind] = w
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()