N=int(input())
circles = []
for _ in range(N):
    x,r = list(map(int, input().split()))
    circles.append([x+r, x-r])
circles.sort()
dp = [float("inf")] * N
from bisect import bisect_left
for right, left in circles:
    ind = bisect_left(dp, -left)
    dp[ind] = -left
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()
