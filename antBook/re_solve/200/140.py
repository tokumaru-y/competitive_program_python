# https://atcoder.jp/contests/arc022/tasks/arc022_2
N=int(input())
A=list(map(int, input().split()))
cnt_table = [0] * (10**5+1)
right = 0
ans = 0
for left in range(N):
    while right < N and cnt_table[A[right]] < 1:
        cnt_table[A[right]] +=1
        right += 1
    ans = max(ans, right - left)
    if right == left:
        right += 1
    else:
        cnt_table[A[left]] -=1
print(ans)