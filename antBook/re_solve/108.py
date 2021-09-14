# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp
def solve():
    import sys
    input = sys.stdin.readline
    N,Q=list(map(int, input().split()))
    A=list(map(int, input().split()))
    X=list(map(int, input().split()))
    for x in X:
        ans = 0
        right = 0
        sum_num = 0
        for left in range(N):
            while right < N and sum_num + A[right] <= x:
                sum_num += A[right]
                right += 1
            ans += right - left
            if right == left:
                right += 1
            else:
                sum_num -= A[left]
        print(ans)
solve()