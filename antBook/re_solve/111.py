# https://atcoder.jp/contests/arc022/tasks/arc022_2
N=int(input())
A=list(map(int, input().split()))
ans = 0
table = {}
right = 0
for left in range(N):
    while right < N and A[right] not in table:
        table[A[right]] = 1
        right+=1
    ans = max(ans, right-left)
    if right == left:
        right += 1
    else:
        table.pop(A[left])
print(ans)