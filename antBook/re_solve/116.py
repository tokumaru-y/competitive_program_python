# https://atcoder.jp/contests/abc077/tasks/arc084_a
from bisect import bisect_left,bisect_right
N=int(input())
A=list(map(int,input().split()))
B=list(map(int, input().split()))
C=list(map(int ,input().split()))
A.sort()
C.sort()
ans = 0
for b in B:
    a_idx = bisect_left(A,b)
    c_idx = bisect_right(C,b)
    c_idx = len(C) - c_idx
    ans += a_idx * c_idx
print(ans)