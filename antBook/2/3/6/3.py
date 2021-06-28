from bisect import bisect_left
N=int(input())
box=[list(map(int, input().split())) for _ in range(N)]
box=sorted(box, key = lambda x: (x[0], -x[1]))
dp=[float("inf")] * N
for h, w in box:
    ind=bisect_left(dp, w)
    dp[ind]=w
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()