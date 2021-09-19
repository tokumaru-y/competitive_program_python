# https://atcoder.jp/contests/arc037/tasks/arc037_c
from bisect import bisect_right
N,K=list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B.sort()
def check(mid):
    cnt = 0
    for a in A:
        cnt += bisect_right(B, mid//a)
    return (cnt>=K)

right = 10**20
left = 0
while right - left > 1:
    mid = (right+left)//2
    if check(mid):
        right= mid
    else:
        left = mid
print(right)