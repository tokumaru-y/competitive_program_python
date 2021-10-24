from bisect import bisect_left
N=int(input())
WH=[list(map(int, input().split())) for _ in range(N)]
dp = [float("inf")] * (N+1)
dp[0]=float("-inf")
box = sorted(WH, key=lambda x: (-x[0], x[1]))
for _,h in box:
    target=-h
    ind=bisect_left(dp, target)
    dp[ind]=target
for i in reversed(range(N+1)):
    if dp[i]!=float("inf"):
        print(i)
        exit()