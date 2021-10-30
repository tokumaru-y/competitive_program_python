# https://atcoder.jp/contests/abc038/tasks/abc038_d
N=int(input())
WH=[list(map(int, input().split())) for _ in range(N)]
sorted_list = sorted(WH, key = lambda x :(-x[0], x[1]))
boxes = [float("inf")] * N
from bisect import bisect_left
for _,h in sorted_list:
    _h = -h
    idx = bisect_left(boxes, _h)
    boxes[idx] = _h
for i in reversed(range(N)):
    if boxes[i] < float("inf"):
        print(i+1)
        exit()