# https://atcoder.jp/contests/arc022/tasks/arc022_2
N=int(input())
A=list(map(int, input().split()))
ans = 0
right = 0
used = [False] * (10**5+1)
for left in range(N):
    while right < N and not used[A[right]]:
        used[A[right]] = True
        right += 1
    ans = max(ans, right - left)
    if right == left:
        right += 1
    else:
        used[A[left]] = False
print(ans)