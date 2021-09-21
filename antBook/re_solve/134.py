# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_H&lang=jp
import bisect


N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
half = []
for i in range(1<<(N//2)):
    sv,sw = 0,0
    for j in range(N//2):
        if i & 1<<j:
            sv += VW[j][0]
            sw += VW[j][1]
    if sw <= W:
        half.append([sw,sv])
half.sort()
ans = 0
for i in range(1<<(N-N//2)):
    sv,sw = 0,0
    for j in range(N-N//2):
        if i & 1<<j:
            sv += VW[N//2+j][0]
            sw += VW[N//2+j][1]
    if sw<= W:
        idx = bisect.bisect_left(half, [W-sw, float("inf")])
        idx -=1
        ans = max(ans, sv + half[idx][1])
print(ans)