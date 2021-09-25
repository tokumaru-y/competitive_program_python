# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_H&lang=jp
import sys
input = sys.stdin.readline
N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
half = N//2
pre = []
for bit in range(1<<half):
    tmp_w,tmp_v=0,0
    for i in range(half):
        if bit & (1<<i):
            _v,_w=VW[i]
            tmp_w += _w
            tmp_v += _v
    if tmp_w<=W:pre.append([tmp_w,tmp_v])
pre.sort()
# これをしないと最大の価値を求められない。例えばw=2の時の最大値は５w=3の時は３といったときにうまくいかなくなる。
for i in range(1, len(pre)):
    if pre[i-1][1] >= pre[i][1]:
        pre[i] = pre[i-1][:]
ans = 0
from bisect import bisect
for bit in range(1<<(N-half)):
    tmp_w,tmp_v=0,0
    for i in range(half, N):
        if bit & (1<<(i-half)):
            tmp_w+=VW[i][1]
            tmp_v+=VW[i][0]
    if tmp_w<=W:
        _idx = bisect(pre, [W-tmp_w, float("inf")]) - 1
        ans = max(ans, pre[_idx][1] + tmp_v)
print(ans)