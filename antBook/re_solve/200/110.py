# https://atcoder.jp/contests/abc038/tasks/abc038_c
N=int(input())
A=list(map(int, input().split()))
ans = 0
right = 1
for left in range(N):
    while right < N and (A[right-1] < A[right] or right <= left):
        right += 1
    ans += right - left
print(ans)