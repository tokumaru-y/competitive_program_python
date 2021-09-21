# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_H&lang=jp
N,W=list(map(int, input().split()))
VW=[list(map(int, input().split())) for _ in range(N)]
VW1 = VW[:N//2]
VW2 = VW[N//2:]
def calc(target_list):
    n = len(target_list)
    res = [[w,v] for v,w in target_list]
    for i in range(n):
        _v,_w = target_list[i]
        for j in range(i+1, n):
            v,w = target_list[j]
            res.append([_w+w, _v+v])
    return res

accum1 = calc(VW1)
accum2 = calc(VW2)
accum2.append([0,0])
accum2.append([float("inf"), float("inf")])
accum2.sort()
ans = 0
from bisect import bisect_left
print(accum1, VW1)
for i in range(len(accum1)):
    v,w = accum1[i]
    target = W-w
    if target < 0:continue
    idx = bisect_left(accum2, target)
    if accum2[idx][0] + w == W:
        ans = max(ans, v + accum2[idx][1])
    else:
        ans = max(ans, v + accum2[idx-1][1])
print(ans)