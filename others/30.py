# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_C&lang=jp 
from sys import stdin
if __name__ == "__main__":
    input = stdin.readline
    N,Q = list(map(int, input().split()))
    A=list(map(int, input().split()))
    Qs = list(map(int, input().split()))
    for q in Qs:
        right = 0
        sum_point = 0
        ans = 0
        for left in range(N):
            while right < N and sum_point + A[right] <= q:
                sum_point+=A[right]
                right += 1
            ans+=(right - left)
            if left == right:
                right += 1
            else:   
                sum_point -= A[left]
        print(ans)