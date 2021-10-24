# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
N,M=list(map(int, input().split()))
P=[0]
for _ in range(N):
    P.append(int(input()))
add_list = []
for i in range(N+1):
    for j in range(i,N+1):
        add_list.append(P[i]+P[j])
add_list.append(float("inf"))
add_list.sort()
ans = float("-inf")
for p in add_list[:-1]:
    target = max(M - p, 0)
    idx = bisect_left(add_list, target)
    if add_list[idx]+p <= M:ans = max(ans, p+add_list[idx])
    if idx > 0:ans = max(ans, p+add_list[idx-1])
print(ans)