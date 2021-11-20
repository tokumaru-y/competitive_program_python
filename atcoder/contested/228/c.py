from bisect import bisect_left
N,K=list(map(int,input().split()))
P = [list(map(int, input().split())) for _ in range(N)]
sum_list = [sum(l) for l in P]
ss = [-x for x in sum_list]
ss.sort()
for i in range(N):
    idx = bisect_left(ss, -(sum_list[i]+300))
    if idx<K:
        print("Yes")
        continue
    print("No")