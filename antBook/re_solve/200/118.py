# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b
from bisect import bisect
D=int(input())
Shop_cnt = int(input())
Target = int(input())
shops = [0,0,D,D]
for _ in range(Shop_cnt-1):
    s = int(input())
    shops.append(s)
targets = []
for _ in range(Target):
    t = int(input())
    targets.append(t)
shops.sort()
ans = 0
for t in targets:
    idx = bisect(shops,t)
    dif = min(shops[idx] - t, t - shops[idx-1])
    ans +=dif
print(ans)