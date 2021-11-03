# https://atcoder.jp/contests/tdpc/tasks/tdpc_target
from bisect import bisect_left
N=int(input())
XR = [list(map(int, input().split())) for _ in range(N)]
dif_list = []
for x,r in XR:
    left, right = x-r, x+r
    dif_list.append([left,right])
dif_list.sort(key=lambda x: (x[0],x[1]))
dp=[float("inf")] * N
for left, right in dif_list:
    _idx = bisect_left(dp, -right)
    dp[_idx] = -right
for i in reversed(range(N)):
    if dp[i] < float("inf"):
        print(i+1)
        exit()