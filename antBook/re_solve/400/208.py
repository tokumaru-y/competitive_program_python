# https://atcoder.jp/contests/arc006/tasks/arc006_3
from bisect import bisect_left
N = int(input())
boxes = [float("inf")] * N
for _ in range(N):
    b=int(input())
    _idx=bisect_left(boxes, b)
    boxes[_idx] = b
for i in range(N):
    if boxes[i] == float("inf"):
        print(i)
        exit()
else:
    print(N)