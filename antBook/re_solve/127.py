# https://atcoder.jp/contests/abc032/tasks/abc032_c
N,K=list(map(int, input().split()))
S=[int(input()) for _ in range(N)]
for s in S:
    if s == 0:
        print(N)
        exit()
ans = 0
right = 0
total = 1
for left in range(N):
    while right < N and total * S[right] <= K:
        total *= S[right]
        right += 1
    ans = max(right - left,ans)
    if right == left:
        right += 1
    else:
        total //= S[left]
print(ans)