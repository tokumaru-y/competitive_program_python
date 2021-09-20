# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp
import sys
input = sys.stdin.readline
N,Q=list(map(int,input().split()))
A=list(map(int, input().split()))
X=list(map(int, input().split()))
for x in X:
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total + A[right] <= x:
            total += A[right]
            right += 1
        ans += right - left
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)