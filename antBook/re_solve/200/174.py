# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
N,M=list(map(int,input().split()))
P=[int(input()) for _ in range(N)]
half_ind = N//2
sum_list = []
for i in range(half_ind):
    sum_list.append(P[i])
    for j in range(i, half_ind):
        sum_list.append(P[i]+P[j])
for i in range(half_ind,N):
    tmp_sum = 0
    sum_list.append(P[i])
    for j in range(i, N):
        sum_list.append(P[j]+P[i])
sum_list.append(0)
sum_list.append(float("inf"))
sum_list.sort()
from bisect import bisect_right
ans = 0
for i in range(len(sum_list)):
    left = M - sum_list[i]
    if left < 0:continue
    ind = bisect_right(sum_list, left)
    ind-=1
    ans = max(ans, sum_list[i]+sum_list[ind])
print(ans)
