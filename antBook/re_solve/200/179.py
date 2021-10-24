# https://atcoder.jp/contests/abc077/tasks/arc084_a
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
C.sort()
from bisect import bisect_right,bisect_left
ans = 0
for b in B:
    a_ind = bisect_left(A,b)
    c_ind = bisect_right(C,b)
    ans += (a_ind) * (N-c_ind)
print(ans)