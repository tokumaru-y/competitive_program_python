# https://atcoder.jp/contests/arc098/tasks/arc098_b
N=int(input())
A=list(map(int, input().split()))
sum=0
right = 0
ans = 0
for left in range(N):
    while right < N and (sum ^ A[right] == sum + A[right]):
        sum += A[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        sum -= A[left]
print(ans)