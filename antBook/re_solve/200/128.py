# https://atcoder.jp/contests/abc038/tasks/abc038_c
N=int(input())
A=list(map(int, input().split()))
A.append(0)
ans = 0
right = 0
for left in range(N):
    while right < N and A[right] < A[right+1]:
        right += 1
    ans += right - left + 1
    if right == left:
        right+=1
print(ans)