import bisect


N=int(input())
XC=[list(map(int, input().split())) for _ in range(N)]
circles = []
for x,c in XC:
    circles.append([x-c,x+c])
sorted_c = sorted(circles, key=lambda x : (-x[0], -x[1]))
dp=[float("inf")] * (N+1)
dp[0]=0
from bisect import bisect_left
for left, right in sorted_c:
    ind = bisect_left(dp, right)
    dp[ind]=right
for i in reversed(range(N+1)):
    if dp[i]!=float("inf"):
        print(i)
        exit()